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


def _slug_to_cli_action(name: str) -> str:
    return name.replace("_", "-")


def _infer_json_schema(value: Any) -> dict[str, Any]:
    if isinstance(value, bool):
        return {"type": "boolean"}
    if isinstance(value, int) and not isinstance(value, bool):
        return {"type": "integer"}
    if isinstance(value, float):
        return {"type": "number"}
    if isinstance(value, str):
        return {"type": "string"}
    if value is None:
        return {"type": "null"}
    if isinstance(value, list):
        if not value:
            return {"type": "array", "items": {}}
        return {"type": "array", "items": _infer_json_schema(value[0])}
    if isinstance(value, dict):
        properties = {key: _infer_json_schema(item) for key, item in value.items()}
        return {
            "type": "object",
            "properties": properties,
            "required": list(value.keys()),
        }
    return {}


def _response_descriptions(response_params: list[dict[str, Any]]) -> dict[str, str]:
    descriptions: dict[str, str] = {}
    for field in response_params:
        name = field.get("name")
        description = field.get("description")
        if isinstance(name, str) and isinstance(description, str) and description.strip():
            descriptions[name] = description.strip()
    return descriptions


def _annotate_schema_descriptions(schema: dict[str, Any], descriptions: dict[str, str]) -> dict[str, Any]:
    if schema.get("type") != "object":
        return schema
    properties = schema.get("properties")
    if not isinstance(properties, dict):
        return schema
    for key, prop in properties.items():
        if not isinstance(prop, dict):
            continue
        if key in descriptions and "description" not in prop:
            prop["description"] = descriptions[key]
        if prop.get("type") == "object":
            _annotate_schema_descriptions(prop, descriptions)
        elif prop.get("type") == "array":
            items = prop.get("items")
            if isinstance(items, dict) and items.get("type") == "object":
                _annotate_schema_descriptions(items, descriptions)
    return schema


def _build_output_from_doc(doc: dict[str, Any]) -> dict[str, Any]:
    response_example = doc.get("response_example_json")
    response_params = doc.get("response_params", [])
    if not isinstance(response_params, list):
        response_params = []
    if not isinstance(response_example, (dict, list)):
        return {}

    json_schema = _infer_json_schema(response_example)
    descriptions = _response_descriptions(response_params)
    if descriptions and isinstance(json_schema, dict):
        json_schema = _annotate_schema_descriptions(json_schema, descriptions)

    return {
        "formats": ["json"],
        "json_schema": json_schema,
    }


def _infer_arg_type(field: dict[str, Any]) -> str:
    field_type = str(field.get("type") or "").lower()
    description = str(field.get("description") or "").lower()
    if "bool" in field_type or "是否" in description:
        return "bool"
    if field_type in {"int", "integer"}:
        return "int"
    return "str"


def _build_args_and_request(
    method: str | None,
    request_params: list[dict[str, Any]],
    request_example_json: Any = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if method == "GET":
        return _build_get_args_and_request(request_params)
    if method == "POST":
        return _build_post_args_and_request(request_params, request_example_json)
    return [], {}


def _build_get_args_and_request(
    request_params: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    args: list[dict[str, Any]] = []
    query: dict[str, Any] = {}
    for field in request_params:
        name = field.get("name")
        if not isinstance(name, str) or not name or name == "access_token":
            continue
        arg_type = _infer_arg_type(field)
        arg = {
            "name": name,
            "flag": f"--{name.replace('_', '-')}",
            "type": arg_type,
            "help": field.get("description") or f"TODO: {name}",
        }
        if field.get("required") is True:
            arg["required"] = True
        args.append(arg)
        if arg_type == "bool":
            arg["action"] = "store_true"
            query[name] = {"int_bool_arg": name}
        else:
            query[name] = {"from_arg": name}

    return args, {"query": query} if query else {}


def _build_post_args_and_request(
    request_params: list[dict[str, Any]],
    request_example_json: Any = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    params = [
        p for p in request_params
        if p.get("name") and p["name"] != "access_token"
    ]

    # When params are available, build args from them
    if params:
        args: list[dict[str, Any]] = []
        json_body: dict[str, Any] = {}
        seen_names: dict[str, int] = {}
        for field in params:
            name = field["name"]
            if name in seen_names:
                seen_names[name] += 1
                # Try to make it unique by appending a suffix
                # If it's a nested field with └, we try to preserve the prefix
                prefix = ""
                stripped = name
                while stripped.startswith("└"):
                    prefix += "└"
                    stripped = stripped[1:]
                name = f"{prefix}{stripped.strip()}_{seen_names[name]}"
            else:
                seen_names[name] = 0

            arg_type = _infer_arg_type(field)
            clean_name = name.replace('└', '').strip()
            arg = {
                "name": name,
                "flag": f"--{clean_name.replace('_', '-').replace(' ', '-')}",
                "type": arg_type,
                "help": field.get("description") or f"TODO: {name}",
            }
            if field.get("required") is True:
                arg["required"] = True
            args.append(arg)
            json_body[name] = {"from_arg": name}
        return args, {"json_body": json_body} if json_body else {}

    # Fallback: derive from request_example_json top-level keys
    if isinstance(request_example_json, dict):
        args = []
        json_body = {}
        for key, value in request_example_json.items():
            if isinstance(value, dict):
                arg_type = "json"
            elif isinstance(value, list):
                arg_type = "json"
            elif isinstance(value, bool):
                arg_type = "bool"
            elif isinstance(value, int):
                arg_type = "int"
            else:
                arg_type = "str"
            arg = {
                "name": key,
                "flag": f"--{key.replace('_', '-')}",
                "type": arg_type,
                "help": f"TODO: {key}",
            }
            args.append(arg)
            json_body[key] = {"from_arg": key}
        return args, {"json_body": json_body} if json_body else {}

    return [], {}


def _build_example(domain: str, cli_action: str, args: list[dict[str, Any]]) -> str:
    parts = [f"wecom {domain} {cli_action}"]
    for arg in args:
        if arg.get("required"):
            parts.append(f"{arg['flag']} <{arg['name']}>")
        else:
            parts.append(f"[{arg['flag']} <{arg['name']}>]")
    return " ".join(parts)


def _build_doc_payload(op: dict[str, Any]) -> dict[str, Any]:
    doc = op.get("doc")
    if not isinstance(doc, dict):
        return {}
    payload: dict[str, Any] = {}
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
        value = doc.get(key)
        if value not in (None, "", [], ()):
            payload[key] = value
    return payload


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

        if "." in op_id:
            id_domain, id_name = op_id.split(".", 1)
        else:
            id_domain, id_name = "unknown", op_id

        # Keep scaffold ids consistent with catalog ids.
        # If catalog has mismatched domain/name fields, op_id is authoritative.
        domain = id_domain
        name = id_name
        doc_payload = _build_doc_payload(op)
        request_params = doc_payload.get("request_params", [])
        if not isinstance(request_params, list):
            request_params = []
        args, request = _build_args_and_request(
            op.get("method"), request_params, doc_payload.get("request_example_json"),
        )
        output = _build_output_from_doc(doc_payload)
        summary = (
            str(doc_payload.get("title")).strip()
            if doc_payload.get("title")
            else f"TODO: {name}"
        )
        scaffold = {
            "name": name,
            "cli_action": _slug_to_cli_action(name),
            "summary": summary,
            "method": op.get("method", "GET"),
            "endpoint": op.get("endpoint"),
            "args": args,
            "request": request,
            "examples": [_build_example(domain, _slug_to_cli_action(name), args)],
        }
        if output:
            scaffold["output"] = output
        if doc_payload:
            scaffold["doc"] = doc_payload
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


def prune_unknown_operations(catalog: dict[str, Any], spec_dir: Path) -> list[Path]:
    catalog_ids = {op.get("id") for op in catalog.get("operations", []) if op.get("id")}
    changed: list[Path] = []

    for spec_file in sorted(spec_dir.glob("*.yaml")):
        if spec_file.name == "catalog.yaml":
            continue
        payload = _load_json_yaml(spec_file)
        domain = payload.get("domain")
        if not domain:
            continue
        operations = payload.get("operations", [])
        filtered = [op for op in operations if _op_id(domain, op.get("name", "")) in catalog_ids]
        if len(filtered) != len(operations):
            payload["operations"] = filtered
            spec_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
            changed.append(spec_file)
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold missing specs from catalog")
    parser.add_argument("--catalog", type=Path, default=Path("specs/wecom/catalog.yaml"))
    parser.add_argument("--spec-dir", type=Path, default=Path("specs/wecom"))
    parser.add_argument("--apply", action="store_true", help="Apply scaffolding to spec files")
    parser.add_argument(
        "--prune-unknown",
        action="store_true",
        help="Remove operations that are no longer present in catalog ids",
    )
    args = parser.parse_args()

    catalog = _load_json_yaml(args.catalog)
    plan = build_missing_plan(catalog, args.spec_dir)
    total = sum(len(v) for v in plan.values())

    summary = {"missing_total": total, "by_domain": {k: len(v) for k, v in plan.items()}}
    print(json.dumps(summary, indent=2))

    if not args.apply:
        return 0

    changed = apply_plan(plan, args.spec_dir)
    if args.prune_unknown:
        changed.extend(prune_unknown_operations(catalog, args.spec_dir))
    for path in changed:
        print(f"updated {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
