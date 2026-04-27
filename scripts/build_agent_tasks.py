"""Build machine-readable implementation tasks and operator docs for Coding Agents."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any

try:
    from scripts.scaffold_from_catalog import (
        _build_args_and_request,
        _build_doc_payload,
        _build_output_from_doc,
    )
    from scripts.sync_spec_docs import _review_hints_for_operation
except ModuleNotFoundError:
    from scaffold_from_catalog import _build_args_and_request, _build_doc_payload, _build_output_from_doc
    from sync_spec_docs import _review_hints_for_operation


def _load_json_yaml(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _op_id(domain: str, name: str) -> str:
    return f"{domain}.{name}"


def _load_spec_indices(spec_dir: Path) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    by_id: dict[str, dict[str, Any]] = {}
    by_endpoint: dict[str, dict[str, Any]] = {}
    for spec_path in sorted(spec_dir.glob("*.yaml")):
        if spec_path.name == "catalog.yaml":
            continue
        payload = _load_json_yaml(spec_path)
        domain = payload.get("domain")
        if not isinstance(domain, str):
            continue
        for op in payload.get("operations", []):
            name = op.get("name")
            endpoint = op.get("endpoint")
            if not isinstance(name, str):
                continue
            entry = {
                "spec_path": spec_path,
                "spec": payload,
                "op": op,
            }
            by_id[_op_id(domain, name)] = entry
            if isinstance(endpoint, str) and endpoint:
                by_endpoint[endpoint] = entry
    return by_id, by_endpoint


def _load_diff_index(diff_payload: dict[str, Any] | None) -> dict[str, str]:
    if not isinstance(diff_payload, dict):
        return {}
    index: dict[str, str] = {}
    for status in ("added", "removed", "modified"):
        for item in diff_payload.get(status, []):
            endpoint = item.get("endpoint")
            if isinstance(endpoint, str):
                index[endpoint] = status
    return index


def _confidence_for_task(method: str | None, doc: dict[str, Any], review_hints: list[str]) -> float:
    if method == "GET":
        score = 0.85
    elif method == "POST":
        score = 0.60
    else:
        score = 0.40

    if not doc.get("request_params"):
        score -= 0.15
    if not doc.get("response_example_json"):
        score -= 0.20
    if not doc.get("response_params"):
        score -= 0.10
    score -= min(0.25, 0.05 * len(review_hints))
    return round(max(0.05, min(0.95, score)), 2)


def _priority_for_status(status: str, confidence: float) -> str:
    if status == "missing":
        return "high" if confidence >= 0.6 else "medium"
    if status == "incomplete":
        return "medium" if confidence >= 0.5 else "low"
    if status == "review_required":
        return "medium" if confidence >= 0.5 else "low"
    return "low"


def _determine_status(spec_op: dict[str, Any] | None, draft: dict[str, Any], review_hints: list[str]) -> str:
    if spec_op is None:
        return "missing"

    if draft.get("args") and not spec_op.get("args"):
        return "incomplete"
    if draft.get("request") and not spec_op.get("request"):
        return "incomplete"
    if draft.get("output") and not spec_op.get("output"):
        return "incomplete"
    if review_hints:
        return "review_required"
    return "implemented"


def build_agent_tasks(
    catalog: dict[str, Any],
    spec_dir: Path,
    diff_payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    spec_index, spec_endpoint_index = _load_spec_indices(spec_dir)
    diff_index = _load_diff_index(diff_payload)
    tasks: list[dict[str, Any]] = []

    for op_id, spec_entry in sorted(spec_index.items()):
        op = spec_entry["op"]
        endpoint = op.get("endpoint")
        if not isinstance(endpoint, str):
            continue
        if diff_index.get(endpoint) != "removed":
            continue
        domain = spec_entry["spec"].get("domain")
        name = op.get("name")
        if not isinstance(domain, str) or not isinstance(name, str):
            continue
        tasks.append(
            {
                "id": f"task.remove.{op_id}",
                "operation_id": op_id,
                "change_type": "removed",
                "status": "review_required",
                "priority": "high",
                "confidence": 0.95,
                "domain": domain,
                "operation_name": name,
                "target_spec": f"specs/wecom/{domain}.yaml",
                "endpoint": endpoint,
                "method": op.get("method"),
                "summary": op.get("summary") or name,
                "source_url": None,
                "doc": {},
                "draft": {},
                "review_hints": [
                    "Discovery no longer reports this endpoint. Do not delete it automatically. Report it for explicit human confirmation first.",
                ],
                "current_spec": {
                    "has_operation": True,
                    "has_args": bool(op.get("args")),
                    "has_request": bool(op.get("request")),
                    "has_output": bool(op.get("output")),
                },
            }
        )

    for catalog_op in sorted(catalog.get("operations", []), key=lambda item: item.get("id", "")):
        op_id = catalog_op.get("id")
        domain = catalog_op.get("domain")
        name = catalog_op.get("name")
        endpoint = catalog_op.get("endpoint")
        method = catalog_op.get("method")
        if not all(isinstance(v, str) for v in (op_id, domain, name, endpoint)):
            continue

        spec_entry = spec_index.get(op_id) or spec_endpoint_index.get(endpoint)
        spec_op = spec_entry["op"] if spec_entry else None
        doc = _build_doc_payload(catalog_op)
        request_params = doc.get("request_params", [])
        if not isinstance(request_params, list):
            request_params = []
        draft_args, draft_request = _build_args_and_request(method, request_params)
        draft_output = _build_output_from_doc(doc)
        review_hints = _review_hints_for_operation(spec_op or {}, doc)
        confidence = _confidence_for_task(method, doc, review_hints)

        draft: dict[str, Any] = {}
        if draft_args:
            draft["args"] = draft_args
        if draft_request:
            draft["request"] = draft_request
        if draft_output:
            draft["output"] = draft_output

        status = _determine_status(spec_op, draft, review_hints)
        target_spec: str | None
        if spec_entry:
            target_spec = f"specs/wecom/{spec_entry['spec']['domain']}.yaml"
        elif domain != "unknown":
            target_spec = f"specs/wecom/{domain}.yaml"
        else:
            target_spec = None
            review_hints.append(
                "No deterministic target spec mapping is available yet. Do not invent a new domain file without updating catalog/domain mapping first."
            )
            status = "review_required"
            confidence = min(confidence, 0.3)
        if status == "implemented":
            continue

        tasks.append(
            {
                "id": f"task.{op_id}",
                "operation_id": op_id,
                "change_type": diff_index.get(endpoint, "unchanged"),
                "status": status,
                "priority": _priority_for_status(status, confidence),
                "confidence": confidence,
                "domain": domain,
                "operation_name": name,
                "target_spec": target_spec,
                "endpoint": endpoint,
                "method": method,
                "summary": doc.get("title") or (spec_op or {}).get("summary") or name,
                "source_url": doc.get("source_url"),
                "doc": doc,
                "draft": draft,
                "review_hints": review_hints,
                "current_spec": {
                    "has_operation": spec_op is not None,
                    "has_args": bool((spec_op or {}).get("args")),
                    "has_request": bool((spec_op or {}).get("request")),
                    "has_output": bool((spec_op or {}).get("output")),
                },
            }
        )

    by_status: dict[str, int] = {}
    by_priority: dict[str, int] = {}
    for task in tasks:
        by_status[task["status"]] = by_status.get(task["status"], 0) + 1
        by_priority[task["priority"]] = by_priority.get(task["priority"], 0) + 1

    return {
        "generated_at": str(date.today()),
        "catalog_snapshot": catalog.get("snapshot_date"),
        "diff_snapshot": (diff_payload or {}).get("discovery_snapshot"),
        "task_count": len(tasks),
        "by_status": by_status,
        "by_priority": by_priority,
        "tasks": tasks,
    }


def _render_summary(tasks_payload: dict[str, Any]) -> str:
    lines = [
        "# Coding Agent Task Summary",
        "",
        f"- Generated at: `{tasks_payload.get('generated_at', 'unknown')}`",
        f"- Catalog snapshot: `{tasks_payload.get('catalog_snapshot', 'unknown')}`",
        f"- Diff snapshot: `{tasks_payload.get('diff_snapshot', 'unknown')}`",
        f"- Total tasks: **{tasks_payload.get('task_count', 0)}**",
        "",
        "## Breakdown",
        "",
    ]
    for key, value in sorted(tasks_payload.get("by_status", {}).items()):
        lines.append(f"- `{key}`: **{value}**")
    for key, value in sorted(tasks_payload.get("by_priority", {}).items()):
        lines.append(f"- `priority:{key}`: **{value}**")

    lines.extend(["", "## Tasks", ""])
    tasks = tasks_payload.get("tasks", [])
    if not tasks:
        lines.append("_No pending tasks._")
        lines.append("")
        return "\n".join(lines)

    lines.append("| Priority | Status | Change | Operation | Spec | Confidence |")
    lines.append("|---|---|---|---|---|---|")
    for task in tasks:
        lines.append(
            f"| {task['priority']} | {task['status']} | {task['change_type']} | "
            f"`{task['operation_id']}` | `{task['target_spec']}` | {task['confidence']} |"
        )
    lines.append("")
    return "\n".join(lines)


def _render_prompt(tasks_path: Path) -> str:
    return "\n".join(
        [
            "# Coding Agent Prompt",
            "",
            "Use the generated task artifact to implement or refine WeCom specs in this repository.",
            "",
            "Instructions:",
            "",
            f"1. Read `{tasks_path.as_posix()}`.",
            "2. Process tasks in this order: high priority first, then higher confidence first.",
            "3. Modify only the target spec files referenced by each task unless codegen or validation requires generated outputs to be updated. If `target_spec` is null, report the task as blocked instead of inventing a new file.",
            "4. Preserve existing hand-written request mappings when they already exist; prefer enriching missing fields over overwriting current logic.",
            "5. Treat `artifacts/implementation.tasks.yaml` as authoritative. Treat the summary markdown as informational only.",
            "6. For tasks with `change_type=removed` or `status=review_required`, do not delete files or prune operations unless a human explicitly confirms removal. Update low-risk metadata only.",
            "7. Do not invent complex POST `json_body` mappings unless the draft is explicit.",
            "8. After edits, run:",
            "   - `python scripts/codegen.py`",
            "   - `python scripts/check_api_coverage.py`",
            "9. Report completed tasks, blocked tasks, and any remaining manual review items.",
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Coding Agent task artifacts")
    parser.add_argument("--catalog", type=Path, default=Path("specs/wecom/catalog.yaml"))
    parser.add_argument("--spec-dir", type=Path, default=Path("specs/wecom"))
    parser.add_argument("--diff", type=Path, help="Optional machine-readable catalog diff")
    parser.add_argument("--tasks-output", type=Path, default=Path("artifacts/implementation.tasks.yaml"))
    parser.add_argument("--summary-output", type=Path, default=Path("artifacts/implementation.summary.md"))
    parser.add_argument("--prompt-output", type=Path, default=Path("artifacts/coding-agent-prompt.md"))
    args = parser.parse_args()

    catalog = _load_json_yaml(args.catalog)
    diff_payload = _load_json_yaml(args.diff) if args.diff else None
    tasks_payload = build_agent_tasks(catalog, args.spec_dir, diff_payload)

    args.tasks_output.parent.mkdir(parents=True, exist_ok=True)
    args.tasks_output.write_text(
        json.dumps(tasks_payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    args.summary_output.write_text(_render_summary(tasks_payload), encoding="utf-8")
    args.prompt_output.write_text(_render_prompt(args.tasks_output), encoding="utf-8")

    print(
        json.dumps(
            {
                "task_count": tasks_payload["task_count"],
                "tasks_output": str(args.tasks_output),
                "summary_output": str(args.summary_output),
                "prompt_output": str(args.prompt_output),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
