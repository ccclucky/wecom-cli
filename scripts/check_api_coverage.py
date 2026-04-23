"""Validate API coverage from specs against the frozen catalog list."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SPEC_DIR = ROOT / "specs" / "wecom"
CATALOG_PATH = SPEC_DIR / "catalog.yaml"


@dataclass(frozen=True)
class CoverageReport:
    total_catalog: int
    total_implemented: int
    coverage: float
    missing_ids: list[str]
    unknown_ids: list[str]
    missing_examples: list[str]



def _load_json_yaml(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _collect_spec_operations(spec_dir: Path) -> tuple[set[str], list[str]]:
    operation_ids: set[str] = set()
    missing_examples: list[str] = []

    for spec_path in sorted(spec_dir.glob("*.yaml")):
        if spec_path.name == "catalog.yaml":
            continue
        payload = _load_json_yaml(spec_path)
        domain = payload["domain"]
        for op in payload.get("operations", []):
            op_id = f"{domain}.{op['name']}"
            operation_ids.add(op_id)
            if not op.get("examples"):
                missing_examples.append(op_id)

    return operation_ids, missing_examples


def build_coverage_report(
    spec_dir: Path = SPEC_DIR,
    catalog_path: Path = CATALOG_PATH,
) -> CoverageReport:
    catalog = _load_json_yaml(catalog_path)
    catalog_ids = {item["id"] for item in catalog["operations"]}
    implemented_ids, missing_examples = _collect_spec_operations(spec_dir)

    missing_ids = sorted(catalog_ids - implemented_ids)
    unknown_ids = sorted(implemented_ids - catalog_ids)
    coverage = 1.0 if not catalog_ids else (len(catalog_ids) - len(missing_ids)) / len(catalog_ids)

    return CoverageReport(
        total_catalog=len(catalog_ids),
        total_implemented=len(implemented_ids),
        coverage=coverage,
        missing_ids=missing_ids,
        unknown_ids=unknown_ids,
        missing_examples=sorted(missing_examples),
    )


def _main() -> int:
    report = build_coverage_report()
    print(
        json.dumps(
            {
                "total_catalog": report.total_catalog,
                "total_implemented": report.total_implemented,
                "coverage": f"{report.coverage * 100:.2f}%",
                "missing_ids": report.missing_ids,
                "unknown_ids": report.unknown_ids,
                "missing_examples": report.missing_examples,
            },
            ensure_ascii=False,
            indent=2,
        )
    )

    if report.coverage < 1.0:
        return 2
    if report.unknown_ids or report.missing_examples:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
