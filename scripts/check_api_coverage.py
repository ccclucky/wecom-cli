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
    invalid_contracts: list[str]



def _load_json_yaml(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _collect_from_arg_refs(value: Any) -> set[str]:
    refs: set[str] = set()
    if isinstance(value, dict):
        from_arg = value.get("from_arg")
        if isinstance(from_arg, str):
            refs.add(from_arg)
        for nested in value.values():
            refs.update(_collect_from_arg_refs(nested))
    elif isinstance(value, list):
        for nested in value:
            refs.update(_collect_from_arg_refs(nested))
    return refs


def _collect_spec_operations(spec_dir: Path) -> tuple[set[str], list[str], list[str]]:
    operation_ids: set[str] = set()
    missing_examples: list[str] = []
    invalid_contracts: list[str] = []

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
            args = op.get("args", [])
            arg_names = [arg.get("name") for arg in args]
            arg_name_set = {name for name in arg_names if isinstance(name, str)}
            if len(arg_name_set) != len(args):
                invalid_contracts.append(f"{op_id}: duplicate/missing arg names")

            request = op.get("request", {})
            if not isinstance(request, dict):
                invalid_contracts.append(f"{op_id}: request must be an object")
                continue

            if op.get("method") == "GET" and "json_body" in request:
                invalid_contracts.append(f"{op_id}: GET must not define json_body")

            request_refs = _collect_from_arg_refs(request)
            unknown_refs = sorted(request_refs - arg_name_set)
            if unknown_refs:
                invalid_contracts.append(
                    f"{op_id}: request uses unknown args {', '.join(unknown_refs)}"
                )

            required_args = {arg["name"] for arg in args if arg.get("required")}
            missing_required_mappings = sorted(required_args - request_refs)
            if missing_required_mappings:
                invalid_contracts.append(
                    f"{op_id}: required args not mapped {', '.join(missing_required_mappings)}"
                )

            output = op.get("output")
            if output is not None:
                if not isinstance(output, dict):
                    invalid_contracts.append(f"{op_id}: output must be an object")
                    continue
                formats = output.get("formats")
                if not isinstance(formats, list) or "json" not in formats:
                    invalid_contracts.append(f"{op_id}: output.formats must include json")
                json_schema = output.get("json_schema")
                if not isinstance(json_schema, dict):
                    invalid_contracts.append(f"{op_id}: output.json_schema must be an object")
                    continue
                if json_schema.get("type") != "object":
                    invalid_contracts.append(f"{op_id}: output.json_schema.type must be object")
                    continue
                properties = json_schema.get("properties")
                if not isinstance(properties, dict):
                    invalid_contracts.append(f"{op_id}: output.json_schema.properties must be an object")
                    continue
                table = output.get("table")
                if table is not None:
                    columns = table.get("columns") if isinstance(table, dict) else None
                    if not isinstance(columns, list):
                        invalid_contracts.append(f"{op_id}: output.table.columns must be a list")
                    else:
                        bad_columns = [
                            col.get("key")
                            for col in columns
                            if not isinstance(col, dict) or col.get("key") not in properties
                        ]
                        if bad_columns:
                            invalid_contracts.append(
                                f"{op_id}: output.table.columns reference unknown keys {', '.join(str(x) for x in bad_columns)}"
                            )

    return operation_ids, missing_examples, invalid_contracts


def build_coverage_report(
    spec_dir: Path = SPEC_DIR,
    catalog_path: Path = CATALOG_PATH,
) -> CoverageReport:
    catalog = _load_json_yaml(catalog_path)
    catalog_ids = {item["id"] for item in catalog["operations"]}
    implemented_ids, missing_examples, invalid_contracts = _collect_spec_operations(spec_dir)

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
        invalid_contracts=sorted(invalid_contracts),
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
                "invalid_contracts": report.invalid_contracts,
            },
            ensure_ascii=False,
            indent=2,
        )
    )

    if report.coverage < 1.0:
        return 2
    if report.unknown_ids or report.missing_examples or report.invalid_contracts:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
