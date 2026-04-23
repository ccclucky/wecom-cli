"""One-command orchestrator for WeCom catalog discovery/diff/sync workflow."""

from __future__ import annotations

import argparse
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


def main() -> int:
    parser = argparse.ArgumentParser(description="Run WeCom catalog sync pipeline")
    parser.add_argument("--seed-file", default="specs/wecom/seeds.txt")
    parser.add_argument("--doc-id-from", type=int, default=90000)
    parser.add_argument("--doc-id-to", type=int, default=100500)
    parser.add_argument("--max-pages", type=int, default=2000)
    parser.add_argument("--mode", choices=["dry-run", "apply", "auto-apply"], default="dry-run")
    parser.add_argument("--discovered", default="artifacts/catalog.discovery.yaml")
    parser.add_argument("--report", default="artifacts/wecom-catalog-report.md")
    parser.add_argument("--synced", default="artifacts/catalog.synced.yaml")
    parser.add_argument("--baseline", default="specs/wecom/catalog.yaml")
    args = parser.parse_args()

    _run(
        [
            "python",
            "scripts/discover_wecom_apis.py",
            "--seed-file",
            args.seed_file,
            "--doc-id-from",
            str(args.doc_id_from),
            "--doc-id-to",
            str(args.doc_id_to),
            "--max-pages",
            str(args.max_pages),
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
        "--sync-output",
        args.synced,
    ]
    if args.mode in {"apply", "auto-apply"}:
        diff_cmd += ["--apply-baseline", args.baseline]
    _run(diff_cmd, ok_codes={0, 1})

    if args.mode == "auto-apply":
        _run(
            [
                "python",
                "scripts/scaffold_from_catalog.py",
                "--catalog",
                args.baseline,
                "--spec-dir",
                "specs/wecom",
                "--apply",
            ]
        )
        _run(["python", "scripts/codegen.py"])
        _run(["python", "scripts/check_api_coverage.py"])

    print("\n=== NEXT ===")
    if args.mode == "dry-run":
        print("1) 打开报告 artifacts/wecom-catalog-report.md 审阅差异")
        print("2) 如确认同步：重新执行加 --mode apply")
    elif args.mode == "apply":
        print("1) baseline catalog 已更新")
        print("3) 补齐 specs/wecom/<domain>.yaml")
        print("4) 运行 python scripts/codegen.py")
        print("5) 运行 pytest -q 和 python scripts/check_api_coverage.py")
    else:
        print("1) baseline/specs/codegen 已自动同步并完成契约校验")
        print("2) 如需放行，请人工 spot-check 报告后合并 PR")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
