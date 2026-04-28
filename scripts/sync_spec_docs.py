"""Sync structured catalog doc metadata into existing WeCom specs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

try:
    from scripts.scaffold_from_catalog import (
        _build_args_and_request,
        _build_doc_payload,
        _build_output_from_doc,
    )
except ModuleNotFoundError:
    from scaffold_from_catalog import (
        _build_args_and_request,
        _build_doc_payload,
        _build_output_from_doc,
    )


def _load_json_yaml(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _op_id(domain: str, name: str) -> str:
    return f"{domain}.{name}"


def _should_replace_summary(summary: str | None) -> bool:
    if not summary:
        return True
    normalized = summary.strip()
    return normalized.startswith("TODO:") or normalized in {"", "TBD"}


def _merge_doc(existing: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    merged = dict(existing)
    for key, value in incoming.items():
        if value not in (None, "", [], ()):
            merged[key] = value
    return merged


def _merge_get_contract(op: dict[str, Any], request_params: list[dict[str, Any]]) -> bool:
    changed = False
    generated_args, generated_request = _build_args_and_request(op.get("method"), request_params)
    if not generated_args and not generated_request:
        return False

    existing_args = op.setdefault("args", [])
    existing_by_name = {
        arg.get("name"): arg for arg in existing_args if isinstance(arg.get("name"), str)
    }
    for generated_arg in generated_args:
        name = generated_arg["name"]
        current = existing_by_name.get(name)
        if current is None:
            existing_args.append(generated_arg)
            changed = True
            continue
        for key, value in generated_arg.items():
            if key not in current:
                current[key] = value
                changed = True

    if generated_request:
        request = op.setdefault("request", {})
        query = request.setdefault("query", {})
        for key, value in generated_request.get("query", {}).items():
            if key not in query:
                query[key] = value
                changed = True

    return changed


def _review_hints_for_operation(op: dict[str, Any], doc: dict[str, Any]) -> list[str]:
    hints: list[str] = []
    if op.get("method") == "POST":
        if doc.get("request_example_json") and not op.get("request", {}).get("json_body"):
            hints.append("POST interface has request_example_json; json_body mapping still needs manual review.")
        if doc.get("request_params") and len(doc["request_params"]) <= 1:
            hints.append("POST parameter table is incomplete on the doc page; inspect request_example_json and follow-up sections manually.")
    if doc.get("notes"):
        hints.append("Review doc.notes for conditional fields, limits, and permission caveats.")
    return hints


def _merge_output(op: dict[str, Any], doc: dict[str, Any]) -> bool:
    generated_output = _build_output_from_doc(doc)
    if not generated_output:
        return False
    current_output = op.get("output")
    if current_output == generated_output:
        return False
    if not isinstance(current_output, dict):
        op["output"] = generated_output
        return True

    merged = dict(current_output)
    formats = merged.get("formats")
    generated_formats = generated_output.get("formats", [])
    if not isinstance(formats, list):
        merged["formats"] = generated_formats
    else:
        merged["formats"] = list(dict.fromkeys(formats + generated_formats))
    if "json_schema" not in merged:
        merged["json_schema"] = generated_output["json_schema"]
    op["output"] = merged
    return op["output"] != current_output


def sync_specs_with_catalog(
    catalog: dict[str, Any], spec_dir: Path, *, apply: bool = False
) -> tuple[list[Path], dict[str, int]]:
    catalog_by_id = {
        op["id"]: op for op in catalog.get("operations", []) if isinstance(op.get("id"), str)
    }
    changed_paths: list[Path] = []
    stats = {
        "spec_files_changed": 0,
        "operations_doc_synced": 0,
        "operations_review_hinted": 0,
        "get_contracts_enriched": 0,
    }

    for spec_path in sorted(spec_dir.glob("*.yaml")):
        if spec_path.name == "catalog.yaml":
            continue
        payload = _load_json_yaml(spec_path)
        domain = payload.get("domain")
        if not domain:
            continue

        spec_changed = False
        for op in payload.get("operations", []):
            op_id = _op_id(domain, op["name"])
            catalog_op = catalog_by_id.get(op_id)
            if not catalog_op:
                continue

            incoming_doc = _build_doc_payload(catalog_op)
            if incoming_doc:
                merged_doc = _merge_doc(op.get("doc", {}), incoming_doc)
                if merged_doc != op.get("doc"):
                    op["doc"] = merged_doc
                    spec_changed = True
                stats["operations_doc_synced"] += 1

                title = incoming_doc.get("title")
                if isinstance(title, str) and _should_replace_summary(op.get("summary")):
                    op["summary"] = title
                    spec_changed = True

                request_params = incoming_doc.get("request_params", [])
                if isinstance(request_params, list) and _merge_get_contract(op, request_params):
                    stats["get_contracts_enriched"] += 1
                    spec_changed = True

                if _merge_output(op, incoming_doc):
                    spec_changed = True

                review_hints = _review_hints_for_operation(op, incoming_doc)
                if review_hints:
                    doc = op.setdefault("doc", {})
                    if doc.get("review_hints") != review_hints:
                        doc["review_hints"] = review_hints
                        spec_changed = True
                    stats["operations_review_hinted"] += 1

        if spec_changed and apply:
            spec_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        if spec_changed:
            changed_paths.append(spec_path)

    stats["spec_files_changed"] = len(changed_paths)
    return changed_paths, stats


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync catalog doc metadata into spec files")
    parser.add_argument("--catalog", type=Path, default=Path("specs/wecom/catalog.yaml"))
    parser.add_argument("--spec-dir", type=Path, default=Path("specs/wecom"))
    parser.add_argument("--apply", action="store_true", help="Apply updates to spec files")
    args = parser.parse_args()

    catalog = _load_json_yaml(args.catalog)
    if not args.apply:
        _, stats = sync_specs_with_catalog(catalog, args.spec_dir, apply=False)
        print(json.dumps(stats, ensure_ascii=False, indent=2))
        return 0

    changed_paths, stats = sync_specs_with_catalog(catalog, args.spec_dir, apply=True)
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    for path in changed_paths:
        print(f"updated {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
