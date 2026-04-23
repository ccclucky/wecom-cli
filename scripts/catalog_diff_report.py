"""Generate a markdown diff report between baseline catalog and newly discovered APIs."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ApiItem:
    endpoint: str
    method: str | None
    raw: dict[str, Any]

    @property
    def key(self) -> tuple[str, str | None]:
        return self.endpoint, self.method


def _load_json_yaml(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _as_items(payload: dict[str, Any]) -> dict[tuple[str, str | None], ApiItem]:
    items: dict[tuple[str, str | None], ApiItem] = {}
    for op in payload.get("operations", []):
        endpoint = op.get("endpoint")
        if not endpoint:
            continue
        method = op.get("method")
        if isinstance(method, str):
            method = method.upper()
        item = ApiItem(endpoint=endpoint, method=method, raw=op)
        items[item.key] = item
    return items


def build_diff(baseline: dict[str, Any], discovered: dict[str, Any]) -> dict[str, list[ApiItem]]:
    baseline_items = _as_items(baseline)
    discovered_items = _as_items(discovered)

    baseline_by_endpoint = {v.endpoint: v for v in baseline_items.values()}
    discovered_by_endpoint = {v.endpoint: v for v in discovered_items.values()}

    modified: list[ApiItem] = []
    for endpoint in sorted(set(baseline_by_endpoint) & set(discovered_by_endpoint)):
        b = baseline_by_endpoint[endpoint]
        d = discovered_by_endpoint[endpoint]
        if b.method != d.method:
            modified.append(d)

    modified_endpoints = {item.endpoint for item in modified}
    added = [
        discovered_by_endpoint[e]
        for e in sorted(set(discovered_by_endpoint) - set(baseline_by_endpoint))
    ]
    removed = [
        baseline_by_endpoint[e]
        for e in sorted(set(baseline_by_endpoint) - set(discovered_by_endpoint))
    ]

    # method changes are reported only in "modified" section.
    added = [item for item in added if item.endpoint not in modified_endpoints]
    removed = [item for item in removed if item.endpoint not in modified_endpoints]

    return {"added": added, "removed": removed, "modified": modified}


def to_markdown(
    diff: dict[str, list[ApiItem]],
    baseline: dict[str, Any],
    discovered: dict[str, Any],
) -> str:
    lines: list[str] = [
        "# WeCom API Catalog Daily Report",
        "",
        f"- Baseline snapshot: `{baseline.get('snapshot_date', 'unknown')}`",
        f"- Discovery snapshot: `{discovered.get('snapshot_date', 'unknown')}`",
        f"- Baseline total: **{len(baseline.get('operations', []))}**",
        f"- Discovered total: **{len(discovered.get('operations', []))}**",
        "",
        "## Summary",
        "",
        f"- Added: **{len(diff['added'])}**",
        f"- Removed: **{len(diff['removed'])}**",
        f"- Modified(method): **{len(diff['modified'])}**",
        "",
    ]

    for section in ("added", "removed", "modified"):
        lines.append(f"## {section.title()}")
        lines.append("")
        if not diff[section]:
            lines.append("_None_")
            lines.append("")
            continue
        lines.append("| Method | Endpoint | Source |")
        lines.append("|---|---|---|")
        for item in diff[section]:
            src = item.raw.get("source_url", "-")
            lines.append(f"| {item.method or '-'} | `{item.endpoint}` | {src} |")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate API diff report")
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--discovered", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--sync-output", type=Path, help="Optional synced catalog output path")
    args = parser.parse_args()

    baseline = _load_json_yaml(args.baseline)
    discovered = _load_json_yaml(args.discovered)
    diff = build_diff(baseline, discovered)

    report_text = to_markdown(diff, baseline, discovered)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(report_text, encoding="utf-8")

    if args.sync_output:
        sync_payload = {
            "snapshot_date": discovered.get("snapshot_date"),
            "source": discovered.get("source"),
            "operations": [
                {
                    "id": op.get("id") or f"todo.{idx}",
                    "domain": op.get("domain", "unknown"),
                    "name": op.get("name", "unknown"),
                    "endpoint": op.get("endpoint"),
                    "method": op.get("method"),
                }
                for idx, op in enumerate(discovered.get("operations", []), start=1)
            ],
        }
        args.sync_output.write_text(
            json.dumps(sync_payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    has_changes = any(diff.values())
    return 1 if has_changes else 0


if __name__ == "__main__":
    raise SystemExit(main())
