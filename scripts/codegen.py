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
        specs.append(data)
    return specs


def _signature_type(arg_type: str) -> str:
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
            args = op.get("args", [])
            signature_parts: list[str] = []
            for arg in args:
                arg_type = arg.get("type", "str")
                signature_type = _signature_type(arg_type)
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
            request = op.get("request", {})
            for req_key in ("query", "json_body"):
                if req_key in request:
                    expr = _indent_block(_py_expr(request[req_key]), 16).lstrip()
                    lines.append(f"            {req_key}={expr},")
            lines.extend(["        )", ""])

    return "\n".join(lines)


def _render_add_argument(line_prefix: str, arg: dict[str, Any]) -> list[str]:
    kwargs: list[str] = []
    if arg.get("action"):
        kwargs.append(f"action={repr(arg['action'])}")
    elif arg.get("type") == "int":
        kwargs.append("type=int")
    elif arg.get("type") == "float":
        kwargs.append("type=float")
    elif arg.get("type") == "json":
        kwargs.append("type=json.loads")
    elif arg.get("type") == "str":
        kwargs.append("type=str")

    if arg.get("required"):
        kwargs.append("required=True")
    if "default" in arg and not arg.get("action"):
        kwargs.append(f"default={repr(arg['default'])}")
    if arg.get("help"):
        kwargs.append(f"help={repr(arg['help'])}")

    return [
        f"    {line_prefix}.add_argument(",
        f"        {repr(arg['flag'])},",
        *[f"        {kw}," for kw in kwargs],
        "    )",
    ]


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
                f"    {domain}_sub = {domain}_parser.add_subparsers(dest='action', required=True)",
                "",
            ]
        )
        for op in spec.get("operations", []):
            action = op["cli_action"]
            parser_name = f"{domain}_{op['name']}_parser"
            if op.get("args"):
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
            for arg in op.get("args", []):
                lines.extend(_render_add_argument(parser_name, arg))

            lines.append("")
            lines.append(f"    def _handle_{domain}_{op['name']}(a: argparse.Namespace) -> dict:")
            call_args = [f"{a['name']}=a.{a['name']}" for a in op.get("args", [])]
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


def main() -> None:
    specs = _load_specs()
    APIS_OUT.write_text(_render_client(specs), encoding="utf-8")
    CLI_OUT.write_text(_render_cli(specs), encoding="utf-8")


if __name__ == "__main__":
    main()
