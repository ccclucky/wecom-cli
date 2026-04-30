from __future__ import annotations

import pytest

from cli.generated_commands import register_generated_commands
from cli.main import build_parser, main, route
from core.errors import WeComCLIError


class DummyClient:
    def contacts_list_users(self, *, department_id, fetch_child, **kwargs):
        return {"department_id": department_id, "fetch_child": fetch_child}

    def messages_send_text(self, *, to_user, agent_id, content, **kwargs):
        return {"to_user": to_user, "agent_id": agent_id, "content": content}

    def customers_list_follow_users(self, **kwargs):
        return {"user": ["zhangsan"]}


def _build_parser_and_table():
    import argparse

    parser = argparse.ArgumentParser(prog="wecom")
    sub = parser.add_subparsers(dest="domain", required=True)
    table = register_generated_commands(sub, DummyClient())
    return parser, table


def test_route_contacts():
    parser, table = _build_parser_and_table()
    args = parser.parse_args(["contacts", "list", "--department-id", "2", "--fetch-child"])
    result = route(args, table)
    assert result == {"department_id": 2, "fetch_child": True}


def test_route_messages():
    parser, table = _build_parser_and_table()
    args = parser.parse_args(
        [
            "messages",
            "send-text",
            "--to-user",
            "zhangsan",
            "--agent-id",
            "1",
            "--content",
            "hello",
        ]
    )
    result = route(args, table)
    assert result["to_user"] == "zhangsan"


@pytest.mark.xfail(reason="customers spec not yet implemented", strict=True)
def test_route_customers():
    parser, table = _build_parser_and_table()
    args = parser.parse_args(["customers", "list-follow-users"])
    result = route(args, table)
    assert result["user"] == ["zhangsan"]


def test_route_unknown_command():
    parser, table = _build_parser_and_table()
    # domain "contacts" exists but action "nonexistent" should fail
    import argparse

    ns = argparse.Namespace(domain="contacts", __action="nonexistent")
    with pytest.raises(WeComCLIError, match="Unknown command"):
        route(ns, table)


def test_main_no_args_shows_help(capsys):
    ret = main([])
    assert ret == 0
    captured = capsys.readouterr()
    assert "wecom" in captured.out


def test_main_unknown_domain_returns_error(monkeypatch, capsys):
    monkeypatch.setenv("WECOM_CORP_ID", "x")
    monkeypatch.setenv("WECOM_CORP_SECRET", "y")
    with pytest.raises(SystemExit):
        main(["--debug", "nonexistent_domain", "action"])


def test_verbose_flag_in_parser():
    parser = build_parser()
    args = parser.parse_args(["--verbose"])
    assert args.verbose is True


def test_debug_flag_in_parser():
    parser = build_parser()
    args = parser.parse_args(["--debug"])
    assert args.debug is True


def test_main_unhandled_exception_clean_error(monkeypatch, capsys):
    monkeypatch.setenv("WECOM_CORP_ID", "x")
    monkeypatch.setenv("WECOM_CORP_SECRET", "y")

    def boom(*args, **kwargs):
        raise RuntimeError("kaboom")

    monkeypatch.setattr("cli.main.bootstrap", boom)
    ret = main(["contacts", "list"])
    assert ret == 1
    captured = capsys.readouterr()
    assert "kaboom" in captured.err
    assert "--debug" in captured.err


def test_main_wecom_cli_error_to_stderr(monkeypatch, capsys):
    monkeypatch.setenv("WECOM_CORP_ID", "x")
    monkeypatch.setenv("WECOM_CORP_SECRET", "y")

    def fake_bootstrap(**kwargs):
        raise WeComCLIError("config broken")

    monkeypatch.setattr("cli.main.bootstrap", fake_bootstrap)
    ret = main(["contacts", "list"])
    assert ret == 2
    captured = capsys.readouterr()
    assert "[wecom-cli] config broken" in captured.err


def test_main_verbose_prints_request_info(monkeypatch, capsys):
    import io
    import json

    monkeypatch.setenv("WECOM_CORP_ID", "x")
    monkeypatch.setenv("WECOM_CORP_SECRET", "y")

    class FakeHttpResponse:
        def read(self):
            return json.dumps({"errcode": 0, "errmsg": "ok", "userlist": []}).encode()

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

    monkeypatch.setattr("urllib.request.urlopen", lambda *a, **k: FakeHttpResponse())
    monkeypatch.setattr("time.sleep", lambda x: None)

    # Patch gettoken response so auth succeeds
    call_count = {"n": 0}

    def selective_open(*args, **kwargs):
        call_count["n"] += 1
        if call_count["n"] == 1:
            return io.BytesIO(json.dumps({"errcode": 0, "access_token": "tok", "expires_in": 7200}).encode())
        return FakeHttpResponse()

    monkeypatch.setattr("urllib.request.urlopen", selective_open)

    ret = main(["--verbose", "contacts", "list", "--department-id", "1"])
    assert ret == 0
    captured = capsys.readouterr()
    assert "[wecom-cli]" in captured.err


def test_main_debug_prints_full_request_response(monkeypatch, capsys):
    import io
    import json

    monkeypatch.setenv("WECOM_CORP_ID", "x")
    monkeypatch.setenv("WECOM_CORP_SECRET", "y")

    call_count = {"n": 0}

    def selective_open(*args, **kwargs):
        call_count["n"] += 1
        if call_count["n"] == 1:
            return io.BytesIO(json.dumps({"errcode": 0, "access_token": "tok", "expires_in": 7200}).encode())
        return io.BytesIO(json.dumps({"errcode": 0, "errmsg": "ok", "data": "test"}).encode())

    monkeypatch.setattr("urllib.request.urlopen", selective_open)
    monkeypatch.setattr("time.sleep", lambda x: None)

    ret = main(["--debug", "contacts", "list", "--department-id", "1"])
    assert ret == 0
    captured = capsys.readouterr()
    assert "[wecom-cli]" in captured.err


def test_build_parser_has_chinese_description():
    parser = build_parser()
    assert "企业微信" in parser.description


def test_help_shows_domain_list_no_bootstrap(capsys):
    """wecom --help should show domain list without requiring config/env."""
    with pytest.raises(SystemExit) as exc_info:
        main(["--help"])
    assert exc_info.value.code == 0
    captured = capsys.readouterr()
    assert "contacts" in captured.out
    assert "messages" in captured.out
    assert "departments" in captured.out


def test_help_no_args_shows_domain_list(capsys):
    """wecom (no args) should show domain list without requiring config/env."""
    ret = main([])
    assert ret == 0
    captured = capsys.readouterr()
    assert "contacts" in captured.out
    assert "企业微信" in captured.out


def test_help_domain_shows_actions_no_bootstrap(capsys):
    """wecom contacts --help should show actions without requiring config/env."""
    with pytest.raises(SystemExit) as exc_info:
        main(["contacts", "--help"])
    assert exc_info.value.code == 0
