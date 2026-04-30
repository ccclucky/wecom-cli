"""Unified requester for WeCom API calls."""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Protocol

from core.config import WeComConfig
from core.errors import APIRequestError, APIResponseError

_TOKEN_EXPIRED_CODES = frozenset({40014, 42001})
_RATE_LIMIT_CODES = frozenset({45001, 45009})
_MAX_RETRIES = 2


class TokenProvider(Protocol):
    def get_token(self, force_refresh: bool = False) -> str: ...


class UnifiedRequester:
    def __init__(self, config: WeComConfig, token_provider: TokenProvider | None = None) -> None:
        self._config = config
        self._token_provider = token_provider
        self._verbose = False
        self._debug = False

    def bind_token_provider(self, token_provider: TokenProvider) -> None:
        self._token_provider = token_provider

    def set_verbose(self, verbose: bool, debug: bool = False) -> None:
        self._verbose = verbose or debug
        self._debug = debug

    def request(
        self,
        *,
        method: str,
        endpoint: str,
        query: dict[str, Any] | None = None,
        json_body: dict[str, Any] | None = None,
        require_auth: bool = True,
        _retrying: bool = False,
    ) -> dict[str, Any]:
        return self._request_with_retry(
            method=method,
            endpoint=endpoint,
            query=query,
            json_body=json_body,
            require_auth=require_auth,
            _retrying=_retrying,
            _attempt=0,
        )

    def _request_with_retry(
        self,
        *,
        method: str,
        endpoint: str,
        query: dict[str, Any] | None,
        json_body: dict[str, Any] | None,
        require_auth: bool,
        _retrying: bool,
        _attempt: int,
    ) -> dict[str, Any]:
        try:
            return self._do_request(
                method=method,
                endpoint=endpoint,
                query=query,
                json_body=json_body,
                require_auth=require_auth,
            )
        except APIResponseError as exc:
            if _retrying or _attempt >= _MAX_RETRIES:
                raise
            if exc.errcode in _TOKEN_EXPIRED_CODES and require_auth and self._token_provider:
                self._log_verbose(f"[retry {exc.errcode}] refreshing token")
                self._token_provider.get_token(force_refresh=True)
                return self._request_with_retry(
                    method=method,
                    endpoint=endpoint,
                    query=query,
                    json_body=json_body,
                    require_auth=require_auth,
                    _retrying=True,
                    _attempt=_attempt + 1,
                )
            if exc.errcode in _RATE_LIMIT_CODES:
                wait = 0.5 * (2**_attempt)
                self._log_verbose(f"[retry {exc.errcode}] backing off {wait:.1f}s")
                time.sleep(wait)
                return self._request_with_retry(
                    method=method,
                    endpoint=endpoint,
                    query=query,
                    json_body=json_body,
                    require_auth=require_auth,
                    _retrying=_retrying,
                    _attempt=_attempt + 1,
                )
            raise

    def _do_request(
        self,
        *,
        method: str,
        endpoint: str,
        query: dict[str, Any] | None,
        json_body: dict[str, Any] | None,
        require_auth: bool,
    ) -> dict[str, Any]:
        query_data: dict[str, Any] = dict(query or {})
        if require_auth:
            if self._token_provider is None:
                raise APIRequestError("Token provider is not configured")
            query_data["access_token"] = self._token_provider.get_token()

        query_text = urllib.parse.urlencode(query_data)
        url = f"{self._config.base_url}{endpoint}"
        if query_text:
            url = f"{url}?{query_text}"

        body_data = None
        headers: dict[str, str] = {"Accept": "application/json"}
        if json_body is not None:
            body_data = json.dumps(_strip_none(json_body)).encode("utf-8")
            headers["Content-Type"] = "application/json"

        if self._verbose:
            import sys

            print(f"[wecom-cli] {method} {url}", file=sys.stderr)
        if self._debug:
            import sys

            if json_body:
                print(f"[wecom-cli] body: {json.dumps(_strip_none(json_body), ensure_ascii=False)}", file=sys.stderr)

        request = urllib.request.Request(
            url=url,
            data=body_data,
            headers=headers,
            method=method.upper(),
        )
        try:
            with urllib.request.urlopen(request, timeout=self._config.timeout_seconds) as response:
                raw = response.read().decode("utf-8")
        except urllib.error.URLError as exc:
            raise APIRequestError(f"Request failed for {endpoint}: {exc}") from exc

        if self._debug:
            import sys

            print(f"[wecom-cli] response: {raw[:500]}", file=sys.stderr)

        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise APIRequestError(f"Invalid JSON response for {endpoint}: {raw[:200]}") from exc

        errcode = int(payload.get("errcode") or 0)
        if errcode != 0:
            raise APIResponseError(
                endpoint=endpoint,
                errcode=errcode,
                errmsg=str(payload.get("errmsg") or "unknown"),
            )
        return payload

    def _log_verbose(self, msg: str) -> None:
        if self._verbose:
            import sys

            print(f"[wecom-cli] {msg}", file=sys.stderr)


def _strip_none(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _strip_none(item) for key, item in value.items() if item is not None}
    if isinstance(value, list):
        return [_strip_none(item) for item in value if item is not None]
    return value
