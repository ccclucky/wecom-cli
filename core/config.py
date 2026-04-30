"""Configuration loading for WeCom CLI."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path

from core.errors import ConfigError

DEFAULT_CONFIG_PATH = Path.home() / ".wecom-cli" / "config.json"


@dataclass(frozen=True)
class WeComConfig:
    corp_id: str
    corp_secret: str
    base_url: str = "https://qyapi.weixin.qq.com"
    timeout_seconds: float = 10.0

    @classmethod
    def load(cls, config_path: Path | None = None) -> WeComConfig:
        path = config_path or DEFAULT_CONFIG_PATH
        raw_data: dict[str, object] = {}

        if path.exists():
            try:
                raw_data = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                raise ConfigError(f"Failed to read config from {path}: {exc}") from exc

        corp_id = str(os.getenv("WECOM_CORP_ID") or raw_data.get("corp_id") or "")
        corp_secret = str(os.getenv("WECOM_CORP_SECRET") or raw_data.get("corp_secret") or "")
        base_url = str(os.getenv("WECOM_BASE_URL") or raw_data.get("base_url") or cls.base_url)
        timeout_raw = os.getenv("WECOM_TIMEOUT_SECONDS") or raw_data.get("timeout_seconds")

        if not corp_id or not corp_secret:
            raise ConfigError(f"corp_id/corp_secret are required (env vars or config file at {path})")

        timeout_seconds = cls.timeout_seconds
        if timeout_raw is not None:
            try:
                timeout_seconds = float(str(timeout_raw))
            except (TypeError, ValueError) as exc:
                raise ConfigError("timeout_seconds should be a valid number") from exc

        return cls(
            corp_id=corp_id,
            corp_secret=corp_secret,
            base_url=base_url.rstrip("/"),
            timeout_seconds=timeout_seconds,
        )
