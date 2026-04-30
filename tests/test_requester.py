from __future__ import annotations

import json

import pytest

from core.config import WeComConfig
from core.errors import APIRequestError, APIResponseError
from core.requester import UnifiedRequester, _strip_none


class DummyTokenProvider:
    def __init__(self, token: str = "token", refresh_token: str = "new_token"):
        self._token = token
        self._refresh_token = refresh_token
        self.refresh_called = False

    def get_token(self, force_refresh: bool = False) -> str:
        if force_refresh:
            self.refresh_called = True
            return self._refresh_token
        return self._token


class FakeResponse:
    def __init__(self, payload: dict):
        self._payload = payload

    def read(self):
        return json.dumps(self._payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


def _make_requester(token_provider=None):
    return UnifiedRequester(
        WeComConfig(corp_id="id", corp_secret="sec"),
        token_provider or DummyTokenProvider(),
    )


def test_request_success(monkeypatch):
    def fake_open(*args, **kwargs):
        return FakeResponse({"errcode": 0, "errmsg": "ok", "data": [1]})

    monkeypatch.setattr("urllib.request.urlopen", fake_open)
    payload = _make_requester().request(method="GET", endpoint="/a")
    assert payload["data"] == [1]


def test_request_api_error(monkeypatch):
    def fake_open(*args, **kwargs):
        return FakeResponse({"errcode": 40014, "errmsg": "invalid access_token"})

    monkeypatch.setattr("urllib.request.urlopen", fake_open)
    with pytest.raises(APIResponseError) as exc_info:
        _make_requester().request(method="GET", endpoint="/a")
    assert exc_info.value.errcode == 40014


def test_request_network_error_raises_api_request_error(monkeypatch):
    import urllib.error

    def fake_open(*args, **kwargs):
        raise urllib.error.URLError("Connection refused")

    monkeypatch.setattr("urllib.request.urlopen", fake_open)
    with pytest.raises(APIRequestError, match="Connection refused"):
        _make_requester().request(method="GET", endpoint="/a")


def test_request_json_decode_error_raises_api_request_error(monkeypatch):
    class BadResponse:
        def read(self):
            return b"not json"

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

    monkeypatch.setattr("urllib.request.urlopen", lambda *a, **k: BadResponse())
    with pytest.raises(APIRequestError, match="Invalid JSON"):
        _make_requester().request(method="GET", endpoint="/a")


def test_request_token_expired_retries_with_refresh(monkeypatch):
    call_count = 0

    def fake_open(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            return FakeResponse({"errcode": 42001, "errmsg": "access_token expired"})
        return FakeResponse({"errcode": 0, "errmsg": "ok", "data": "success"})

    monkeypatch.setattr("urllib.request.urlopen", fake_open)
    monkeypatch.setattr("time.sleep", lambda x: None)
    tp = DummyTokenProvider()
    payload = _make_requester(tp).request(method="GET", endpoint="/a")
    assert payload["data"] == "success"
    assert tp.refresh_called


def test_request_token_expired_no_infinite_loop(monkeypatch):
    def fake_open(*args, **kwargs):
        return FakeResponse({"errcode": 40014, "errmsg": "always expired"})

    monkeypatch.setattr("urllib.request.urlopen", fake_open)
    with pytest.raises(APIResponseError):
        _make_requester().request(method="GET", endpoint="/a")


def test_request_rate_limit_retries_with_backoff(monkeypatch):
    call_count = 0
    slept = []

    def fake_open(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            return FakeResponse({"errcode": 45001, "errmsg": "rate limit"})
        return FakeResponse({"errcode": 0, "errmsg": "ok"})

    monkeypatch.setattr("urllib.request.urlopen", fake_open)
    monkeypatch.setattr("time.sleep", lambda x: slept.append(x))
    payload = _make_requester().request(method="GET", endpoint="/a")
    assert payload["errcode"] == 0
    assert len(slept) == 1
    assert slept[0] == pytest.approx(0.5, abs=0.01)


def test_request_non_retryable_error_no_retry(monkeypatch):
    call_count = 0

    def fake_open(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        return FakeResponse({"errcode": 40056, "errmsg": "invalid param"})

    monkeypatch.setattr("urllib.request.urlopen", fake_open)
    monkeypatch.setattr("time.sleep", lambda x: None)
    with pytest.raises(APIResponseError) as exc_info:
        _make_requester().request(method="GET", endpoint="/a")
    assert exc_info.value.errcode == 40056
    assert call_count == 1


def test_strip_none_recursively():
    payload = {
        "a": 1,
        "b": None,
        "c": {"d": None, "e": 2},
        "f": [1, None, {"g": None, "h": 3}],
    }
    assert _strip_none(payload) == {"a": 1, "c": {"e": 2}, "f": [1, {"h": 3}]}
