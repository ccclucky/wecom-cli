from __future__ import annotations

import pytest

from cli.generated_commands import register_generated_commands
from cli.main import route


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
