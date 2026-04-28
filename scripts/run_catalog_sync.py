"""One-command orchestrator for WeCom catalog discovery/diff/sync workflow."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _run(cmd: list[str], ok_codes: set[int] | None = None) -> int:
    print("+", " ".join(cmd))
    proc = subprocess.run(cmd, check=False, cwd=ROOT)
    if ok_codes is None:
        ok_codes = {0}
    if proc.returncode not in ok_codes:
        raise subprocess.CalledProcessError(proc.returncode, cmd)
    return proc.returncode


def _task_catalog_path(mode: str, baseline: str, synced: str) -> str:
    if mode == "dry-run":
        return synced
    return baseline


def _load_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def _clean_summary(diff_path: str, tasks_path: str) -> dict[str, int]:
    diff_payload = _load_json(diff_path)
    tasks_payload = _load_json(tasks_path)
    diff_summary = diff_payload.get("summary", {})
    return {
        "added": int(diff_summary.get("added", 0)),
        "removed": int(diff_summary.get("removed", 0)),
        "modified": int(diff_summary.get("modified", 0)),
        "task_count": int(tasks_payload.get("task_count", 0)),
    }


def _assert_clean(diff_path: str, tasks_path: str) -> None:
    summary = _clean_summary(diff_path, tasks_path)
    if any(summary.values()):
        raise RuntimeError(
            "workflow did not converge to a clean state: "
            f"added={summary['added']}, removed={summary['removed']}, "
            f"modified={summary['modified']}, task_count={summary['task_count']}"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Run WeCom catalog sync pipeline")
    parser.add_argument("--seed-file", default="specs/wecom/seeds.txt")
    parser.add_argument("--menu-tree-file", default="specs/wecom/menu_tree.json")
    parser.add_argument("--max-pages", type=int, default=2000)
    parser.add_argument("--delay-min", type=float, default=1.0,
                        help="Minimum delay between page fetches in seconds")
    parser.add_argument("--delay-max", type=float, default=3.0,
                        help="Maximum delay between page fetches in seconds")
    parser.add_argument("--mode", choices=["dry-run", "apply", "auto-apply"], default="dry-run")
    parser.add_argument("--discovered", default="artifacts/catalog.discovery.yaml")
    parser.add_argument("--report", default="artifacts/wecom-catalog-report.md")
    parser.add_argument("--diff-output", default="artifacts/catalog.diff.yaml")
    parser.add_argument("--synced", default="artifacts/catalog.synced.yaml")
    parser.add_argument("--baseline", default="specs/wecom/catalog.yaml")
    parser.add_argument(
        "--allow-prune-unknown",
        action="store_true",
        help="Allow auto-apply to delete spec operations missing from the reconciled catalog",
    )
    args = parser.parse_args()

    _run(["python", "scripts/update_menu_tree.py", "--output", args.menu_tree_file])
    _run(
        [
            "python",
            "scripts/discover_wecom_apis.py",
            "--seed-file",
            args.seed_file,
            "--menu-tree-file",
            args.menu_tree_file,
            "--max-pages",
            str(args.max_pages),
            "--delay-min",
            str(args.delay_min),
            "--delay-max",
            str(args.delay_max),
            "--output",
            args.discovered,
        ]
    )

    diff_cmd = [
        "python",
        "scripts/catalog_diff_report.py",
        "--baseline",
        args.baseline,
        "--discovered",
        args.discovered,
        "--report",
        args.report,
        "--diff-output",
        args.diff_output,
        "--sync-output",
        args.synced,
    ]
    if args.mode in {"apply", "auto-apply"}:
        diff_cmd += ["--apply-baseline", args.baseline]
    _run(diff_cmd, ok_codes={0, 1})

    if args.mode == "auto-apply":
        scaffold_cmd = [
            "python",
            "scripts/scaffold_from_catalog.py",
            "--catalog",
            args.baseline,
            "--spec-dir",
            "specs/wecom",
            "--apply",
        ]
        if args.allow_prune_unknown:
            scaffold_cmd.append("--prune-unknown")
        _run(
            scaffold_cmd
        )
        _run(["python", "scripts/sync_spec_docs.py", "--catalog", args.baseline, "--spec-dir", "specs/wecom", "--apply"])
        _run(["python", "scripts/codegen.py"])
        _run(["python", "scripts/check_api_coverage.py"])
        task_catalog = args.baseline
    else:
        task_catalog = _task_catalog_path(args.mode, args.baseline, args.synced)
        _run(
            [
                "python",
                "scripts/build_agent_tasks.py",
                "--catalog",
                task_catalog,
                "--spec-dir",
                "specs/wecom",
                "--diff",
                args.diff_output,
            ]
        )

    if args.mode == "auto-apply":

        _run(
            [
                "python",
                "scripts/catalog_diff_report.py",
                "--baseline",
                args.baseline,
                "--discovered",
                args.discovered,
                "--report",
                args.report,
                "--diff-output",
                args.diff_output,
                "--sync-output",
                args.synced,
            ],
            ok_codes={0, 1},
        )
        _run(
            [
                "python",
                "scripts/build_agent_tasks.py",
                "--catalog",
                args.baseline,
                "--spec-dir",
                "specs/wecom",
                "--diff",
                args.diff_output,
            ]
        )
        _assert_clean(args.diff_output, "artifacts/implementation.tasks.yaml")

    print("\n=== NEXT ===")
    if args.mode == "dry-run":
        print("1) 打开报告 artifacts/wecom-catalog-report.md 审阅差异")
        print("2) 查看 artifacts/implementation.tasks.yaml，确认任务分配是否合理")
        print("3) 如确认同步：重新执行加 --mode apply")
    elif args.mode == "apply":
        print("1) baseline catalog 已更新")
        print("2) 补齐 specs/wecom/<domain>.yaml")
        print("3) 运行 python scripts/codegen.py")
        print("4) 运行 pytest -q 和 python scripts/check_api_coverage.py")
        print("5) 最后重新运行 python scripts/build_agent_tasks.py 刷新 agent 任务产物")
    else:
        print("1) baseline/specs/codegen 已自动同步并完成契约校验")
        print("2) 最终 diff/tasks 已回到 clean state")
        print("3) 如需放行，请人工 spot-check 报告后合并 PR")
        if not args.allow_prune_unknown:
            print("4) removed 任务仍需人工确认；本次未自动 prune")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
