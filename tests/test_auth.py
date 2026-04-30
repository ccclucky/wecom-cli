from __future__ import annotations

import json

import pytest

from core.auth import AccessTokenProvider
from core.config import WeComConfig
from core.errors import AuthError


class FakeResponse:
    def __init__(self, payload: dict):
        self._payload = payload

    def read(self):
        return json.dumps(self._payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def _make_provider():
    config = WeComConfig(corp_id="id", corp_secret="sec")
    from core.requester import UnifiedRequester
    requester = UnifiedRequester(config)
    provider = AccessTokenProvider(requester, config)
    requester.bind_token_provider(provider)
    return provider


def test_token_cached_within_ttl(monkeypatch):
    monkeypatch.setattr("time.time", lambda: 1000.0)
    monkeypatch.setattr("urllib.request.urlopen", lambda *a, **k: FakeResponse({
        "errcode": 0, "access_token": "tok_abc", "expires_in": 7200,
    }))

    provider = _make_provider()
    token1 = provider.get_token()
    assert token1 == "tok_abc"

    # Second call hits cache — urlopen not called again
    token2 = provider.get_token()
    assert token2 == "tok_abc"


def test_token_refresh_on_expiry(monkeypatch):
    current_time = 1000.0

    def fake_time():
        return current_time

    monkeypatch.setattr("time.time", fake_time)

    call_count = 0
    def fake_open(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        return FakeResponse({
            "errcode": 0, "access_token": f"tok_{call_count}", "expires_in": 7200,
        })

    monkeypatch.setattr("urllib.request.urlopen", fake_open)
    provider = _make_provider()

    token1 = provider.get_token()
    assert token1 == "tok_1"

    # Advance time past expiry + 30s buffer
    current_time = 1000.0 + 7200 + 31
    token2 = provider.get_token()
    assert token2 == "tok_2"
    assert call_count == 2


def test_network_failure_raises_auth_error(monkeypatch):
    import urllib.error
    monkeypatch.setattr("urllib.request.urlopen", lambda *a, **k: (_ for _ in ()).throw(urllib.error.URLError("Connection refused")))

    provider = _make_provider()
    with pytest.raises(AuthError, match="Connection refused"):
        provider.get_token()


def test_invalid_credentials_raises_auth_error(monkeypatch):
    monkeypatch.setattr("urllib.request.urlopen", lambda *a, **k: FakeResponse({
        "errcode": 40001, "errmsg": "invalid credential",
    }))

    provider = _make_provider()
    with pytest.raises(AuthError, match="invalid credential"):
        provider.get_token()
