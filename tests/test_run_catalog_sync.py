from __future__ import annotations

import json

import pytest

from scripts.run_catalog_sync import _assert_clean, _clean_summary, _task_catalog_path, main


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


def test_assert_clean_raises_on_non_clean_state(tmp_path, monkeypatch):
    repo = tmp_path / "repo"
    repo.mkdir()
    artifacts = repo / "artifacts"
    artifacts.mkdir()
    (artifacts / "catalog.diff.yaml").write_text(
        json.dumps({"summary": {"added": 2, "removed": 1, "modified": 0}}),
        encoding="utf-8",
    )
    (artifacts / "implementation.tasks.yaml").write_text(
        json.dumps({"task_count": 3}),
        encoding="utf-8",
    )

    monkeypatch.setattr("scripts.run_catalog_sync.ROOT", repo)
    with pytest.raises(RuntimeError, match="did not converge"):
        _assert_clean("artifacts/catalog.diff.yaml", "artifacts/implementation.tasks.yaml")


def test_assert_clean_passes_on_clean_state(tmp_path, monkeypatch):
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
    _assert_clean("artifacts/catalog.diff.yaml", "artifacts/implementation.tasks.yaml")


def test_main_dry_run_calls_pipeline_in_order(monkeypatch):
    calls: list[tuple[list[str], set[int] | None]] = []

    def fake_run(cmd: list[str], ok_codes: set[int] | None = None) -> int:
        calls.append((cmd, ok_codes))
        return 0

    monkeypatch.setattr("scripts.run_catalog_sync._run", fake_run)
    monkeypatch.setattr("sys.argv", ["run_catalog_sync.py", "--mode", "dry-run"])

    assert main() == 0
    assert [cmd for cmd, _ in calls] == [
        ["python", "scripts/update_menu_tree.py", "--output", "specs/wecom/menu_tree.json"],
        [
            "python",
            "scripts/discover_wecom_apis.py",
            "--seed-file",
            "specs/wecom/seeds.txt",
            "--menu-tree-file",
            "specs/wecom/menu_tree.json",
            "--max-pages",
            "2000",
            "--delay-min",
            "1.0",
            "--delay-max",
            "3.0",
            "--output",
            "artifacts/catalog.discovery.yaml",
        ],
        [
            "python",
            "scripts/catalog_diff_report.py",
            "--baseline",
            "specs/wecom/catalog.yaml",
            "--discovered",
            "artifacts/catalog.discovery.yaml",
            "--report",
            "artifacts/wecom-catalog-report.md",
            "--diff-output",
            "artifacts/catalog.diff.yaml",
            "--sync-output",
            "artifacts/catalog.synced.yaml",
        ],
        [
            "python",
            "scripts/build_agent_tasks.py",
            "--catalog",
            "artifacts/catalog.synced.yaml",
            "--spec-dir",
            "specs/wecom",
            "--diff",
            "artifacts/catalog.diff.yaml",
        ],
    ]
    assert calls[2][1] == {0, 1}


def test_main_auto_apply_converges_on_clean_state(tmp_path, monkeypatch):
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

    calls: list[tuple[list[str], set[int] | None]] = []

    def fake_run(cmd: list[str], ok_codes: set[int] | None = None) -> int:
        calls.append((cmd, ok_codes))
        return 0

    monkeypatch.setattr("scripts.run_catalog_sync.ROOT", repo)
    monkeypatch.setattr("scripts.run_catalog_sync._run", fake_run)
    monkeypatch.setattr("sys.argv", ["run_catalog_sync.py", "--mode", "auto-apply"])

    assert main() == 0
    assert [cmd[:2] for cmd, _ in calls] == [
        ["python", "scripts/update_menu_tree.py"],
        ["python", "scripts/discover_wecom_apis.py"],
        ["python", "scripts/catalog_diff_report.py"],
        ["python", "scripts/scaffold_from_catalog.py"],
        ["python", "scripts/sync_spec_docs.py"],
        ["python", "scripts/codegen.py"],
        ["python", "scripts/check_api_coverage.py"],
        ["python", "scripts/catalog_diff_report.py"],
        ["python", "scripts/build_agent_tasks.py"],
    ]
    assert calls[2][1] == {0, 1}
    assert calls[7][1] == {0, 1}


def test_main_auto_apply_raises_when_final_state_not_clean(tmp_path, monkeypatch):
    repo = tmp_path / "repo"
    repo.mkdir()
    artifacts = repo / "artifacts"
    artifacts.mkdir()
    (artifacts / "catalog.diff.yaml").write_text(
        json.dumps({"summary": {"added": 1, "removed": 0, "modified": 0}}),
        encoding="utf-8",
    )
    (artifacts / "implementation.tasks.yaml").write_text(
        json.dumps({"task_count": 0}),
        encoding="utf-8",
    )

    calls: list[list[str]] = []

    def fake_run(cmd: list[str], ok_codes: set[int] | None = None) -> int:
        calls.append(cmd)
        return 0

    monkeypatch.setattr("scripts.run_catalog_sync.ROOT", repo)
    monkeypatch.setattr("scripts.run_catalog_sync._run", fake_run)
    monkeypatch.setattr("sys.argv", ["run_catalog_sync.py", "--mode", "auto-apply"])

    with pytest.raises(RuntimeError, match="did not converge"):
        main()
    assert calls[-1][:2] == ["python", "scripts/build_agent_tasks.py"]
    assert len(calls) == 9
