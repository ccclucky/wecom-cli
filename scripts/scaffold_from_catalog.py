"""Scaffold missing domain specs from catalog entries."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def _load_json_yaml(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _op_id(domain: str, name: str) -> str:
    return f"{domain}.{name}"


def build_missing_plan(catalog: dict[str, Any], spec_dir: Path) -> dict[str, list[dict[str, Any]]]:
    existing: set[str] = set()
    for spec_file in sorted(spec_dir.glob("*.yaml")):
        if spec_file.name in {"catalog.yaml"}:
            continue
        spec = _load_json_yaml(spec_file)
        domain = spec.get("domain")
        if not domain:
            continue
        for op in spec.get("operations", []):
            existing.add(_op_id(domain, op["name"]))

    plan: dict[str, list[dict[str, Any]]] = {}
    for op in catalog.get("operations", []):
        op_id = op.get("id")
        if not op_id or op_id in existing:
            continue

        domain = op.get("domain") or op_id.split(".", 1)[0]
        name = op.get("name") or op_id.split(".", 1)[-1]
        scaffold = {
            "name": name,
            "cli_action": name.replace("_", "-"),
            "summary": f"TODO: {name}",
            "method": op.get("method", "GET"),
            "endpoint": op.get("endpoint"),
            "args": [],
            "request": {},
            "examples": [f"TODO: wecom {domain} {name.replace('_', '-')}"] ,
        }
        plan.setdefault(domain, []).append(scaffold)

    return plan


def apply_plan(plan: dict[str, list[dict[str, Any]]], spec_dir: Path) -> list[Path]:
    changed: list[Path] = []
    for domain, ops in sorted(plan.items()):
        spec_file = spec_dir / f"{domain}.yaml"
        if spec_file.exists():
            payload = _load_json_yaml(spec_file)
        else:
            payload = {"domain": domain, "operations": []}

        payload.setdefault("operations", []).extend(ops)
        spec_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        changed.append(spec_file)
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold missing specs from catalog")
    parser.add_argument("--catalog", type=Path, default=Path("specs/wecom/catalog.yaml"))
    parser.add_argument("--spec-dir", type=Path, default=Path("specs/wecom"))
    parser.add_argument("--apply", action="store_true", help="Apply scaffolding to spec files")
    args = parser.parse_args()

    catalog = _load_json_yaml(args.catalog)
    plan = build_missing_plan(catalog, args.spec_dir)
    total = sum(len(v) for v in plan.values())

    summary = {"missing_total": total, "by_domain": {k: len(v) for k, v in plan.items()}}
    print(json.dumps(summary, indent=2))

    if not args.apply:
        return 0

    changed = apply_plan(plan, args.spec_dir)
    for path in changed:
        print(f"updated {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
