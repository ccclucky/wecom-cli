from __future__ import annotations

import json

import pytest

from core.config import WeComConfig
from core.errors import APIResponseError
from core.requester import UnifiedRequester


class DummyTokenProvider:
    def get_token(self, force_refresh: bool = False) -> str:
        return "token"


class FakeResponse:
    def __init__(self, payload: dict):
        self._payload = payload

    def read(self):
        return json.dumps(self._payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


def test_request_success(monkeypatch):
    def fake_open(*args, **kwargs):
        return FakeResponse({"errcode": 0, "errmsg": "ok", "data": [1]})

    monkeypatch.setattr("urllib.request.urlopen", fake_open)
    requester = UnifiedRequester(WeComConfig(corp_id="id", corp_secret="sec"), DummyTokenProvider())

    payload = requester.request(method="GET", endpoint="/a")
    assert payload["data"] == [1]


def test_request_api_error(monkeypatch):
    def fake_open(*args, **kwargs):
        return FakeResponse({"errcode": 40014, "errmsg": "invalid access_token"})

    monkeypatch.setattr("urllib.request.urlopen", fake_open)
    requester = UnifiedRequester(WeComConfig(corp_id="id", corp_secret="sec"), DummyTokenProvider())

    with pytest.raises(APIResponseError):
        requester.request(method="GET", endpoint="/a")
