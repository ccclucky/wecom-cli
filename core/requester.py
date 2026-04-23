"""Unified requester for WeCom API calls."""

from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Protocol

from core.config import WeComConfig
from core.errors import APIRequestError, APIResponseError


class TokenProvider(Protocol):
    def get_token(self, force_refresh: bool = False) -> str:
        ...


class UnifiedRequester:
    def __init__(self, config: WeComConfig, token_provider: TokenProvider | None = None) -> None:
        self._config = config
        self._token_provider = token_provider

    def bind_token_provider(self, token_provider: TokenProvider) -> None:
        self._token_provider = token_provider

    def request(
        self,
        *,
        method: str,
        endpoint: str,
        query: dict[str, Any] | None = None,
        json_body: dict[str, Any] | None = None,
        require_auth: bool = True,
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
            body_data = json.dumps(json_body).encode("utf-8")
            headers["Content-Type"] = "application/json"

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
