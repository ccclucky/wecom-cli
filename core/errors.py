"""Unified error hierarchy for WeCom CLI."""

from __future__ import annotations


class WeComCLIError(Exception):
    """Base class for predictable CLI failures."""


class ConfigError(WeComCLIError):
    """Raised when loading configuration fails."""


class AuthError(WeComCLIError):
    """Raised when access token acquisition fails."""


class APIRequestError(WeComCLIError):
    """Raised when a transport-level request error occurs."""


class APIResponseError(WeComCLIError):
    """Raised when WeCom API returns a non-success errcode."""

    def __init__(self, *, endpoint: str, errcode: int, errmsg: str) -> None:
        self.endpoint = endpoint
        self.errcode = errcode
        self.errmsg = errmsg
        super().__init__(f"{endpoint}: errcode={errcode}, errmsg={errmsg}")
