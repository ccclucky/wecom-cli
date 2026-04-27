from __future__ import annotations

import json

from scripts.check_api_coverage import build_coverage_report


def test_api_coverage_is_100_percent_for_catalog_snapshot():
    report = build_coverage_report()
    assert report.coverage == 1.0
    assert report.missing_ids == []
    assert report.unknown_ids == []
    assert report.missing_examples == []
    assert report.invalid_contracts == []


def test_contract_validation_detects_unmapped_required_args(tmp_path):
    (tmp_path / "catalog.yaml").write_text(
        json.dumps(
            {
                "operations": [
                    {
                        "id": "messages.send_text",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / "messages.yaml").write_text(
        json.dumps(
            {
                "domain": "messages",
                "operations": [
                    {
                        "name": "send_text",
                        "method": "POST",
                        "endpoint": "/cgi-bin/message/send",
                        "args": [
                            {"name": "to_user", "required": True},
                            {"name": "content", "required": True},
                        ],
                        "request": {"json_body": {"touser": {"from_arg": "to_user"}}},
                        "examples": ["ok"],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    report = build_coverage_report(spec_dir=tmp_path, catalog_path=tmp_path / "catalog.yaml")
    assert report.coverage == 1.0
    assert any("required args not mapped content" in item for item in report.invalid_contracts)


def test_contract_validation_detects_invalid_output_schema(tmp_path):
    (tmp_path / "catalog.yaml").write_text(
        json.dumps(
            {
                "operations": [
                    {
                        "id": "contacts.list_users",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / "contacts.yaml").write_text(
        json.dumps(
            {
                "domain": "contacts",
                "operations": [
                    {
                        "name": "list_users",
                        "method": "GET",
                        "endpoint": "/cgi-bin/user/simplelist",
                        "args": [],
                        "request": {},
                        "examples": ["ok"],
                        "output": {
                            "formats": ["table"],
                            "json_schema": {"type": "array"},
                        },
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    report = build_coverage_report(spec_dir=tmp_path, catalog_path=tmp_path / "catalog.yaml")
    assert report.coverage == 1.0
    assert any("output.formats must include json" in item for item in report.invalid_contracts)
    assert any("output.json_schema.type must be object" in item for item in report.invalid_contracts)
