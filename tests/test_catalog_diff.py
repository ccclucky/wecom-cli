from __future__ import annotations

from scripts.catalog_diff_report import (
    build_diff,
    build_diff_payload,
    build_reconciled_catalog,
    to_markdown,
)


def test_build_diff_detects_add_remove_modify():
    baseline = {
        "snapshot_date": "2026-04-22",
        "operations": [
            {
                "id": "contacts.list_users",
                "domain": "contacts",
                "name": "list_users",
                "endpoint": "/cgi-bin/user/simplelist",
                "method": "GET",
            },
            {"endpoint": "/cgi-bin/message/send", "method": "POST"},
        ],
    }
    discovered = {
        "snapshot_date": "2026-04-23",
        "operations": [
            {
                "endpoint": "/cgi-bin/user/simplelist",
                "method": "POST",
                "source_url": "u1",
                "title": "获取成员",
            },
            {
                "endpoint": "/cgi-bin/department/list",
                "method": "GET",
                "source_url": "u2",
                "title": "获取部门列表",
                "request_params": [{"name": "department_id", "required": True, "description": "部门 ID"}],
            },
        ],
    }

    diff = build_diff(baseline, discovered)
    assert len(diff["added"]) == 1
    assert diff["added"][0].endpoint == "/cgi-bin/department/list"
    assert len(diff["removed"]) == 1
    assert diff["removed"][0].endpoint == "/cgi-bin/message/send"
    assert len(diff["modified"]) == 1
    assert diff["modified"][0].endpoint == "/cgi-bin/user/simplelist"

    reconciled = build_reconciled_catalog(baseline, discovered)
    by_endpoint = {op["endpoint"]: op for op in reconciled["operations"]}
    assert by_endpoint["/cgi-bin/user/simplelist"]["id"] == "contacts.list_users"
    assert by_endpoint["/cgi-bin/user/simplelist"]["method"] == "POST"
    assert by_endpoint["/cgi-bin/department/list"]["id"] == "departments.list"
    assert by_endpoint["/cgi-bin/department/list"]["doc"]["title"] == "获取部门列表"
    assert by_endpoint["/cgi-bin/department/list"]["doc"]["request_params"][0]["name"] == "department_id"
    # Baseline-only operation must be preserved
    assert "/cgi-bin/message/send" in by_endpoint
    assert by_endpoint["/cgi-bin/message/send"]["method"] == "POST"

    md = to_markdown(diff, baseline, discovered)
    assert "Added: **1**" in md
    assert "Removed: **1**" in md
    assert "Modified(method): **1**" in md
    assert "How to fix" in md

    payload = build_diff_payload(diff, baseline, discovered)
    assert payload["summary"] == {"added": 1, "removed": 1, "modified": 1}
    assert payload["added"][0]["endpoint"] == "/cgi-bin/department/list"
    assert payload["removed"][0]["endpoint"] == "/cgi-bin/message/send"


def test_build_reconciled_catalog_infers_domain_identity_and_skips_methodless_pages():
    baseline = {"snapshot_date": "2026-04-22", "operations": []}
    discovered = {
        "snapshot_date": "2026-04-23",
        "operations": [
            {
                "endpoint": "/cgi-bin/department/list",
                "method": "GET",
                "title": "获取部门列表",
            },
            {
                "endpoint": "/cgi-bin/gettoken",
                "method": "GET",
                "title": "获取access_token",
            },
            {
                "endpoint": "/cgi-bin/wxpush",
                "method": None,
                "title": "加解密方案说明",
            },
        ],
    }

    reconciled = build_reconciled_catalog(baseline, discovered)
    by_endpoint = {op["endpoint"]: op for op in reconciled["operations"]}

    assert by_endpoint["/cgi-bin/department/list"]["id"] == "departments.list"
    assert by_endpoint["/cgi-bin/department/list"]["domain"] == "departments"
    assert by_endpoint["/cgi-bin/gettoken"]["id"] == "auth.get_token"
    assert "/cgi-bin/wxpush" not in by_endpoint


def test_build_diff_skips_methodless_discovery_pages():
    baseline = {"snapshot_date": "2026-04-22", "operations": []}
    discovered = {
        "snapshot_date": "2026-04-23",
        "operations": [
            {
                "endpoint": "/cgi-bin/wxpush",
                "method": None,
                "title": "加解密方案说明",
            }
        ],
    }

    diff = build_diff(baseline, discovered)
    assert diff == {"added": [], "removed": [], "modified": []}


def test_build_reconciled_catalog_preserves_baseline_only_ops():
    baseline = {
        "snapshot_date": "2026-04-22",
        "operations": [
            {
                "id": "messages.send_text",
                "domain": "messages",
                "name": "send_text",
                "endpoint": "/cgi-bin/message/send",
                "method": "POST",
            },
            {
                "id": "tags.create",
                "domain": "tags",
                "name": "create",
                "endpoint": "/cgi-bin/tag/create",
                "method": "POST",
                "doc": {"title": "创建标签"},
            },
        ],
    }
    discovered = {
        "snapshot_date": "2026-04-23",
        "operations": [
            {
                "endpoint": "/cgi-bin/department/list",
                "method": "GET",
                "title": "获取部门列表",
            },
        ],
    }

    reconciled = build_reconciled_catalog(baseline, discovered)
    by_endpoint = {op["endpoint"]: op for op in reconciled["operations"]}

    # Discovered operation is present
    assert "/cgi-bin/department/list" in by_endpoint
    assert by_endpoint["/cgi-bin/department/list"]["id"] == "departments.list"

    # Baseline-only operations are preserved verbatim
    assert "/cgi-bin/message/send" in by_endpoint
    assert by_endpoint["/cgi-bin/message/send"]["id"] == "messages.send_text"
    assert by_endpoint["/cgi-bin/message/send"]["method"] == "POST"

    assert "/cgi-bin/tag/create" in by_endpoint
    assert by_endpoint["/cgi-bin/tag/create"]["id"] == "tags.create"
    assert by_endpoint["/cgi-bin/tag/create"]["doc"]["title"] == "创建标签"
