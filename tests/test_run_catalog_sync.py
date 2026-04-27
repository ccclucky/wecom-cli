from __future__ import annotations

import json

from scripts.run_catalog_sync import _clean_summary, _task_catalog_path


def test_task_catalog_path_uses_synced_catalog_for_dry_run():
    assert _task_catalog_path("dry-run", "specs/wecom/catalog.yaml", "artifacts/catalog.synced.yaml") == (
        "artifacts/catalog.synced.yaml"
    )


def test_task_catalog_path_uses_baseline_for_apply_modes():
    assert _task_catalog_path("apply", "specs/wecom/catalog.yaml", "artifacts/catalog.synced.yaml") == (
        "specs/wecom/catalog.yaml"
    )
    assert _task_catalog_path("auto-apply", "specs/wecom/catalog.yaml", "artifacts/catalog.synced.yaml") == (
        "specs/wecom/catalog.yaml"
    )


def test_clean_summary_reads_diff_and_tasks(tmp_path, monkeypatch):
    repo = tmp_path / "repo"
    repo.mkdir()
    artifacts = repo / "artifacts"
    artifacts.mkdir()
    (artifacts / "catalog.diff.yaml").write_text(
        json.dumps({"summary": {"added": 0, "removed": 0, "modified": 0}}),
        encoding="utf-8",
    )
    (artifacts / "implementation.tasks.yaml").write_text(
        json.dumps({"task_count": 0}),
        encoding="utf-8",
    )

    monkeypatch.setattr("scripts.run_catalog_sync.ROOT", repo)
    assert _clean_summary("artifacts/catalog.diff.yaml", "artifacts/implementation.tasks.yaml") == {
        "added": 0,
        "removed": 0,
        "modified": 0,
        "task_count": 0,
    }
