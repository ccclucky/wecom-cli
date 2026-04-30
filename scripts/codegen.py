"""Generate API client and CLI command skeletons from specs/wecom/*.yaml."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SPEC_DIR = ROOT / "specs" / "wecom"
APIS_OUT = ROOT / "apis" / "generated_client.py"
CLI_OUT = ROOT / "cli" / "generated_commands.py"


def _py_expr(value: Any) -> str:
    if isinstance(value, dict):
        if "from_arg" in value:
            return value["from_arg"]
        if "const" in value:
            return repr(value["const"])
        if "int_bool_arg" in value:
            arg_name = value["int_bool_arg"]
            return f"int({arg_name})"
        if not value:
            return "{}"
        items = ",\n".join(f"{repr(k)}: {_py_expr(v)}" for k, v in value.items())
        return "{\n" + items + "\n}"
    if isinstance(value, list):
        return "[" + ", ".join(_py_expr(v) for v in value) + "]"
    return repr(value)


def _indent_block(text: str, spaces: int) -> str:
    prefix = " " * spaces
    return "\n".join(f"{prefix}{line}" if line else line for line in text.splitlines())


def _load_specs() -> list[dict[str, Any]]:
    specs: list[dict[str, Any]] = []
    for file in sorted(SPEC_DIR.glob("*.yaml")):
        if file.name == "catalog.yaml":
            continue
        with file.open("r", encoding="utf-8") as fp:
            data = json.load(fp)
        if "domain" not in data:
            # Skip non-spec files (e.g. catalog.discovery.yaml landed here by mistake)
            continue
        specs.append(data)
    return specs


_PAGINATION_NAMES = frozenset({
    "limit", "offset", "count", "page", "size",
    "pagesize", "page_size", "per_page",
})


def _signature_type(arg_type: str, arg_name: str = "") -> str:
    if arg_type == "bool" and arg_name in _PAGINATION_NAMES:
        return "int"
    if arg_type in {"int", "float", "str", "bool"}:
        return arg_type
    if arg_type == "json":
        return "Any"
    return "Any"


def _render_client(specs: list[dict[str, Any]]) -> str:
    lines: list[str] = [
        '"""Auto-generated API client from specs/wecom/*.yaml. DO NOT EDIT."""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
        "from core.requester import UnifiedRequester",
        "",
        "",
        "class GeneratedWeComClient:",
        "    def __init__(self, requester: UnifiedRequester) -> None:",
        "        self._requester = requester",
        "",
    ]

    for spec in specs:
        domain = spec["domain"]
        for op in spec.get("operations", []):
            method_name = f"{domain}_{op['name']}"
            uses_body = op.get("mode") == "body"
            if uses_body:
                signature = ", *, body: dict[str, Any]"
            else:
                args = op.get("args", [])
                signature_parts: list[str] = []
                for arg in args:
                    arg_type = arg.get("type", "str")
                    signature_type = _signature_type(arg_type, arg["name"])
                    if arg.get("required", False):
                        signature_parts.append(f"{arg['name']}: {signature_type}")
                    elif "default" in arg:
                        signature_parts.append(f"{arg['name']}: {signature_type} = {repr(arg['default'])}")
                    else:
                        signature_parts.append(f"{arg['name']}: {signature_type} | None = None")
                signature = ", ".join(signature_parts)
                if signature:
                    signature = ", *, " + signature

            lines.extend(
                [
                    f"    def {method_name}(self{signature}) -> dict:",
                    "        return self._requester.request(",
                    f"            method={repr(op['method'])},",
                    f"            endpoint={repr(op['endpoint'])},",
                ]
            )
            if uses_body:
                lines.append("            json_body=body,")
            else:
                request = op.get("request", {})
                for req_key in ("query", "json_body"):
                    if req_key in request:
                        expr = _indent_block(_py_expr(request[req_key]), 16).lstrip()
                        lines.append(f"            {req_key}={expr},")
            lines.extend(["        )", ""])

    return "\n".join(lines)


def _render_add_argument(line_prefix: str, arg: dict[str, Any], dest: str | None = None) -> list[str]:
    kwargs: list[str] = []
    effective_type = arg.get("type", "str")
    if effective_type == "bool" and arg.get("name", "") in _PAGINATION_NAMES:
        effective_type = "int"
    if arg.get("action"):
        kwargs.append(f"action={repr(arg['action'])}")
    elif effective_type == "int":
        kwargs.append("type=int")
    elif effective_type == "float":
        kwargs.append("type=float")
    elif effective_type == "json":
        kwargs.append("type=json.loads")
    elif effective_type == "str":
        kwargs.append("type=str")

    if arg.get("required"):
        kwargs.append("required=True")
    if "default" in arg and not arg.get("action"):
        kwargs.append(f"default={repr(arg['default'])}")
    if arg.get("help"):
        kwargs.append(f"help={repr(arg['help'])}")
    if dest is not None:
        kwargs.append(f"dest={repr(dest)}")

    return [
        f"    {line_prefix}.add_argument(",
        f"        {repr(arg['flag'])},",
        *[f"        {kw}," for kw in kwargs],
        "    )",
    ]


def _dedup_args(args: list[dict[str, Any]]) -> list[tuple[str, dict[str, Any]]]:
    """Return (unique_name, arg) pairs, deduplicating repeated names."""
    seen: dict[str, int] = {}
    result: list[tuple[str, dict[str, Any]]] = []
    for a in args:
        base = a["name"]
        if base in seen:
            seen[base] += 1
            uniq = f"{base}_{seen[base]}"
        else:
            seen[base] = 0
            uniq = base
        result.append((uniq, a))
    return result


def _render_cli(specs: list[dict[str, Any]]) -> str:
    lines: list[str] = [
        '"""Auto-generated CLI command registration from specs/wecom/*.yaml. DO NOT EDIT."""',
        "",
        "from __future__ import annotations",
        "",
        "import argparse",
        "import json",
        "from collections.abc import Callable",
        "",
        "from apis.generated_client import GeneratedWeComClient",
        "",
        "CommandHandler = Callable[[argparse.Namespace], dict]",
        "",
        "",
        "def register_generated_commands(",
        "    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],",
        "    client: GeneratedWeComClient,",
        ") -> dict[tuple[str, str], CommandHandler]:",
        "    table: dict[tuple[str, str], CommandHandler] = {}",
        "",
    ]

    for spec in specs:
        domain = spec["domain"]
        lines.extend(
            [
                f"    {domain}_parser = subparsers.add_parser(",
                f"        {repr(domain)},",
                f"        help={repr(domain + ' 域命令')},",
                "    )",
                f"    {domain}_sub = {domain}_parser.add_subparsers(dest='__action', required=True)",
                "",
            ]
        )
        for op in spec.get("operations", []):
            action = op["cli_action"]
            parser_name = f"{domain}_{op['name']}_parser"
            uses_body = op.get("mode") == "body"
            has_args = bool(op.get("args")) or uses_body
            if has_args:
                lines.extend(
                    [
                        f"    {parser_name} = {domain}_sub.add_parser(",
                        f"        {repr(action)},",
                        f"        help={repr(op.get('summary', ''))},",
                        "    )",
                    ]
                )
            else:
                lines.extend(
                    [
                        f"    {domain}_sub.add_parser(",
                        f"        {repr(action)},",
                        f"        help={repr(op.get('summary', ''))},",
                        "    )",
                    ]
                )
            if uses_body:
                lines.extend([
                    f"    {parser_name}.add_argument(",
                    f"        '--body',",
                    f"        type=json.loads,",
                    f"        required=True,",
                    f"        help='JSON request body',",
                    f"    )",
                ])
            else:
                deduped = _dedup_args(op.get("args", []))
                for uniq, arg in deduped:
                    dest = uniq if uniq != arg["name"] else None
                    lines.extend(_render_add_argument(parser_name, arg, dest=dest))

            lines.append("")
            lines.append(f"    def _handle_{domain}_{op['name']}(a: argparse.Namespace) -> dict:")
            if uses_body:
                lines.append(f"        return client.{domain}_{op['name']}(body=a.body)")
            else:
                deduped = _dedup_args(op.get("args", []))
                call_args = [f"{uniq}=a.{uniq}" for uniq, _ in deduped]
                if call_args:
                    lines.append(
                        f"        return client.{domain}_{op['name']}("
                    )
                    for part in call_args:
                        lines.append(f"            {part},")
                    lines.append("        )")
                else:
                    lines.append(f"        return client.{domain}_{op['name']}()")
            lines.append(
                f"    table[({repr(domain)}, {repr(action)})] = "
                f"_handle_{domain}_{op['name']}"
            )
            lines.append("")

    lines.extend(["    return table", ""])
    return "\n".join(lines)


_VALID_TYPES = frozenset({"str", "int", "float", "bool", "json"})
_VALID_METHODS = frozenset({"GET", "POST"})


def _validate_specs(specs: list[dict[str, Any]]) -> None:
    errors: list[str] = []
    for spec in specs:
        domain = spec.get("domain", "<unknown>")
        for i, op in enumerate(spec.get("operations", [])):
            op_id = f"{domain}::{op.get('name', f'op[{i}]')}"
            if not op.get("name"):
                errors.append(f"{op_id}: missing 'name'")
            if op.get("method", "") not in _VALID_METHODS:
                errors.append(f"{op_id}: invalid method {op.get('method')!r}")
            if not op.get("endpoint", "").startswith("/"):
                errors.append(f"{op_id}: endpoint must start with '/'")
            for j, arg in enumerate(op.get("args", [])):
                if not arg.get("name"):
                    errors.append(f"{op_id}: arg[{j}] missing 'name'")
                arg_type = arg.get("type", "str")
                if arg_type not in _VALID_TYPES:
                    errors.append(f"{op_id}: arg '{arg.get('name')}' has invalid type {arg_type!r}")
    if errors:
        raise ValueError("Spec validation failed:\n" + "\n".join(f"  - {e}" for e in errors))


def main() -> None:
    specs = _load_specs()
    _validate_specs(specs)

    client_code = _render_client(specs)
    cli_code = _render_cli(specs)

    compile(client_code, str(APIS_OUT), "exec")
    compile(cli_code, str(CLI_OUT), "exec")

    APIS_OUT.write_text(client_code, encoding="utf-8")
    CLI_OUT.write_text(cli_code, encoding="utf-8")


if __name__ == "__main__":
    main()
