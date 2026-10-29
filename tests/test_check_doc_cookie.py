"""Tests for the doc-site cookie probe."""

import json

import pytest

from scripts.check_doc_cookie import _parse_userinfo


def _page(userinfo: dict) -> str:
    return f'<html><script>var x = {{"_userinfo":{json.dumps(userinfo)}}};</script></html>'


def test_anonymous_profile_is_flat_empty_object():
    page = _page({"profile": {}, "isLogin": False})
    userinfo = _parse_userinfo(page)
    assert userinfo == {"profile": {}, "isLogin": False}


def test_logged_in_profile_has_nested_braces():
    # A real logged-in profile nests objects; a regex over this would stop at
    # the first closing brace and fail to parse.
    page = _page({"profile": {"name": "dev", "corp": {"id": "ww1"}}, "isLogin": True})
    userinfo = _parse_userinfo(page)
    assert userinfo is not None
    assert userinfo["isLogin"] is True
    assert userinfo["profile"]["corp"]["id"] == "ww1"


def test_missing_marker_returns_none():
    assert _parse_userinfo("<html>no marker here</html>") is None


def test_malformed_marker_returns_none():
    assert _parse_userinfo('x "_userinfo":{not json') is None


@pytest.mark.parametrize(
    "payload",
    [
        {"profile": {}, "isLogin": False},
        {"profile": {"name": "dev", "tags": ["a", "b"]}, "isLogin": True},
    ],
)
def test_parse_survives_payload(payload):
    assert _parse_userinfo(_page(payload)) == payload
