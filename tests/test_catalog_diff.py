from __future__ import annotations

from scripts.catalog_diff_report import build_diff, build_reconciled_catalog, to_markdown


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
            {"endpoint": "/cgi-bin/user/simplelist", "method": "POST", "source_url": "u1"},
            {"endpoint": "/cgi-bin/department/list", "method": "GET", "source_url": "u2"},
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
    assert by_endpoint["/cgi-bin/department/list"]["id"].startswith("todo.")

    md = to_markdown(diff, baseline, discovered)
    assert "Added: **1**" in md
    assert "Removed: **1**" in md
    assert "Modified(method): **1**" in md
    assert "How to fix" in md
