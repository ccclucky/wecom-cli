from __future__ import annotations

from scripts.check_api_coverage import build_coverage_report


def test_api_coverage_is_100_percent_for_catalog_snapshot():
    report = build_coverage_report()
    assert report.coverage == 1.0
    assert report.missing_ids == []
    assert report.unknown_ids == []
    assert report.missing_examples == []
