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
        if not isinstance(method, str) or not method.strip():
            continue
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

    added = [discovered_by_endpoint[e] for e in sorted(set(discovered_by_endpoint) - set(baseline_by_endpoint))]
    removed = [baseline_by_endpoint[e] for e in sorted(set(baseline_by_endpoint) - set(discovered_by_endpoint))]

    return {"added": added, "removed": removed, "modified": modified}


def _serialize_item(item: ApiItem) -> dict[str, Any]:
    payload = {
        "endpoint": item.endpoint,
        "method": item.method,
    }
    source_url = item.raw.get("source_url")
    if source_url:
        payload["source_url"] = source_url
    title = item.raw.get("title")
    if title:
        payload["title"] = title
    return payload


def build_diff_payload(
    diff: dict[str, list[ApiItem]],
    baseline: dict[str, Any],
    discovered: dict[str, Any],
) -> dict[str, Any]:
    return {
        "baseline_snapshot": baseline.get("snapshot_date"),
        "discovery_snapshot": discovered.get("snapshot_date"),
        "summary": {
            "added": len(diff["added"]),
            "removed": len(diff["removed"]),
            "modified": len(diff["modified"]),
        },
        "added": [_serialize_item(item) for item in diff["added"]],
        "removed": [_serialize_item(item) for item in diff["removed"]],
        "modified": [_serialize_item(item) for item in diff["modified"]],
    }


def _slug_from_endpoint(endpoint: str) -> str:
    return endpoint.strip("/").replace("/", "_").replace("-", "_").replace(".", "_")


EXACT_ENDPOINT_IDENTITY: dict[str, tuple[str, str]] = {
    "/cgi-bin/gettoken": ("auth", "get_token"),
    "/cgi-bin/getcallbackip": ("network", "get_callback_ip"),
    "/cgi-bin/get_api_domain_ip": ("network", "get_api_domain_ip"),
}

PATH_DOMAIN_MAP: dict[str, str] = {
    "agent": "agents",
    "batch": "batch",
    "corp": "corp",
    "department": "departments",
    "externalcontact": "customers",
    "idconvert": "idconvert",
    "message": "messages",
    "tag": "tags",
    "user": "users",
}


def _infer_catalog_identity(endpoint: str) -> tuple[str, str]:
    if endpoint in EXACT_ENDPOINT_IDENTITY:
        return EXACT_ENDPOINT_IDENTITY[endpoint]

    parts = [part for part in endpoint.strip("/").split("/") if part]
    if len(parts) < 3 or parts[0] != "cgi-bin":
        slug = _slug_from_endpoint(endpoint)
        return "unknown", slug

    head = parts[1].replace("-", "_")
    tail = [part.replace("-", "_") for part in parts[2:]]
    domain = PATH_DOMAIN_MAP.get(head, head)
    name = "_".join(tail) if tail else head
    return domain, name


def _doc_from_discovered(op: dict[str, Any]) -> dict[str, Any]:
    doc: dict[str, Any] = {}
    for key in (
        "title",
        "source_url",
        "request_url",
        "request_params",
        "response_params",
        "request_example_text",
        "request_example_json",
        "response_example_text",
        "response_example_json",
        "permissions",
        "notes",
    ):
        value = op.get(key)
        if value not in (None, "", [], ()):
            doc[key] = value
    return doc


def build_reconciled_catalog(
    baseline: dict[str, Any],
    discovered: dict[str, Any],
) -> dict[str, Any]:
    baseline_by_endpoint = {op["endpoint"]: op for op in baseline.get("operations", []) if op.get("endpoint")}

    reconciled_ops: list[dict[str, Any]] = []
    for op in sorted(discovered.get("operations", []), key=lambda x: x.get("endpoint", "")):
        endpoint = op.get("endpoint")
        if not endpoint:
            continue

        old = baseline_by_endpoint.get(endpoint)
        if old:
            doc = _doc_from_discovered(op)
            if not doc and isinstance(old.get("doc"), dict):
                doc = old["doc"]
            reconciled_ops.append(
                {
                    "id": old.get("id"),
                    "domain": old.get("domain", "unknown"),
                    "name": old.get("name", _slug_from_endpoint(endpoint)),
                    "endpoint": endpoint,
                    "method": op.get("method") or old.get("method"),
                    **({"doc": doc} if doc else {}),
                }
            )
            continue

        method = op.get("method")
        if not method:
            # Skip explanatory pages that mention a /cgi-bin path but do not define an API method.
            continue

        domain, name = _infer_catalog_identity(endpoint)
        doc = _doc_from_discovered(op)
        reconciled_ops.append(
            {
                "id": f"{domain}.{name}",
                "domain": domain,
                "name": name,
                "endpoint": endpoint,
                "method": method,
                **({"doc": doc} if doc else {}),
            }
        )

    # Preserve baseline operations that the crawler did not re-discover.
    discovered_endpoints = {op.get("endpoint") for op in discovered.get("operations", []) if op.get("endpoint")}
    for op in baseline.get("operations", []):
        endpoint = op.get("endpoint")
        if not endpoint or endpoint in discovered_endpoints:
            continue
        reconciled_ops.append(
            {
                "id": op.get("id"),
                "domain": op.get("domain", "unknown"),
                "name": op.get("name", _slug_from_endpoint(endpoint)),
                "endpoint": endpoint,
                "method": op.get("method"),
                **({"doc": op["doc"]} if isinstance(op.get("doc"), dict) else {}),
            }
        )

    reconciled_ops.sort(key=lambda x: x.get("endpoint", ""))
    return {
        "snapshot_date": discovered.get("snapshot_date"),
        "source": discovered.get("source"),
        "operations": reconciled_ops,
    }


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
        "## How to fix",
        "",
        "- Review `Added/Removed/Modified` below.",
        "- If confirmed, run `python scripts/catalog_diff_report.py` with:",
        "  - `--baseline specs/wecom/catalog.yaml`",
        "  - `--discovered artifacts/catalog.discovery.yaml`",
        "  - `--report artifacts/wecom-catalog-report.md`",
        "  - `--apply-baseline specs/wecom/catalog.yaml`",
        "- Then update `specs/wecom/<domain>.yaml`,",
        "  run `python scripts/codegen.py`, and add tests/examples.",
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
    parser.add_argument("--diff-output", type=Path, help="Optional machine-readable diff output path")
    parser.add_argument("--apply-baseline", type=Path, help="Write reconciled catalog to this path")
    args = parser.parse_args()

    baseline = _load_json_yaml(args.baseline)
    discovered = _load_json_yaml(args.discovered)
    diff = build_diff(baseline, discovered)

    report_text = to_markdown(diff, baseline, discovered)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(report_text, encoding="utf-8")
    if args.diff_output:
        args.diff_output.write_text(
            json.dumps(build_diff_payload(diff, baseline, discovered), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    reconciled = build_reconciled_catalog(baseline, discovered)
    if args.sync_output:
        args.sync_output.write_text(
            json.dumps(reconciled, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    if args.apply_baseline:
        args.apply_baseline.write_text(
            json.dumps(reconciled, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    has_changes = any(diff.values())
    return 1 if has_changes else 0


if __name__ == "__main__":
    raise SystemExit(main())
