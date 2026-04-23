from __future__ import annotations

import json

from core.config import WeComConfig


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
