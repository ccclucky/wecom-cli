from __future__ import annotations

import json

import pytest

from core.config import WeComConfig
from core.errors import ConfigError


def test_load_config_from_file(tmp_path):
    config_file = tmp_path / "config.json"
    config_file.write_text(
        json.dumps(
            {
                "corp_id": "corp-id",
                "corp_secret": "corp-secret",
                "base_url": "https://example.com/",
                "timeout_seconds": 3,
            }
        ),
        encoding="utf-8",
    )

    config = WeComConfig.load(config_file)

    assert config.corp_id == "corp-id"
    assert config.corp_secret == "corp-secret"
    assert config.base_url == "https://example.com"
    assert config.timeout_seconds == 3.0


def test_missing_file_raises_config_error_with_path(tmp_path):
    missing = tmp_path / "nonexistent.json"
    with pytest.raises(ConfigError):
        WeComConfig.load(missing)


def test_env_vars_override_file(tmp_path, monkeypatch):
    config_file = tmp_path / "config.json"
    config_file.write_text(
        json.dumps(
            {
                "corp_id": "file-id",
                "corp_secret": "file-sec",
            }
        ),
        encoding="utf-8",
    )

    monkeypatch.setenv("WECOM_CORP_ID", "env-id")
    monkeypatch.setenv("WECOM_CORP_SECRET", "env-sec")
    monkeypatch.setenv("WECOM_TIMEOUT_SECONDS", "20")

    config = WeComConfig.load(config_file)
    assert config.corp_id == "env-id"
    assert config.corp_secret == "env-sec"
    assert config.timeout_seconds == 20.0


def test_invalid_json_raises_config_error(tmp_path):
    bad_file = tmp_path / "config.json"
    bad_file.write_text("{invalid json", encoding="utf-8")

    with pytest.raises(ConfigError, match="Failed to read config"):
        WeComConfig.load(bad_file)
