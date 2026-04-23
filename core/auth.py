"""WeCom access token acquisition and caching."""

from __future__ import annotations

import time
from dataclasses import dataclass

from core.config import WeComConfig
from core.errors import APIRequestError, APIResponseError, AuthError
from core.requester import UnifiedRequester


@dataclass
class TokenBundle:
    access_token: str
    expires_at_epoch: float


class AccessTokenProvider:
    def __init__(self, requester: UnifiedRequester, config: WeComConfig) -> None:
        self._requester = requester
        self._config = config
        self._bundle: TokenBundle | None = None

    def get_token(self, force_refresh: bool = False) -> str:
        if not force_refresh and self._bundle and self._bundle.expires_at_epoch > time.time() + 30:
            return self._bundle.access_token

        try:
            payload = self._requester.request(
                method="GET",
                endpoint="/cgi-bin/gettoken",
                query={"corpid": self._config.corp_id, "corpsecret": self._config.corp_secret},
                require_auth=False,
            )
        except (APIRequestError, APIResponseError) as exc:
            raise AuthError(str(exc)) from exc

        token = str(payload.get("access_token") or "")
        expires_in = int(payload.get("expires_in") or 0)
        if not token or expires_in <= 0:
            raise AuthError("Token response missing access_token/expires_in")

        self._bundle = TokenBundle(access_token=token, expires_at_epoch=time.time() + expires_in)
        return token
