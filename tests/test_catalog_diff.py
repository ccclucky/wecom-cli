from __future__ import annotations

from scripts.catalog_diff_report import build_diff, to_markdown


def test_build_diff_detects_add_remove_modify():
    baseline = {
        "snapshot_date": "2026-04-22",
        "operations": [
            {"endpoint": "/cgi-bin/user/simplelist", "method": "GET"},
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

    md = to_markdown(diff, baseline, discovered)
    assert "Added: **1**" in md
    assert "Removed: **1**" in md
    assert "Modified(method): **1**" in md
