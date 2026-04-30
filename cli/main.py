"""Command-line interface for WeCom CLI."""

from __future__ import annotations

import argparse
import json
import os
import sys

from apis.generated_client import GeneratedWeComClient
from cli.generated_commands import CommandHandler, register_generated_commands
from cli.help_formatter import DOMAIN_DESCRIPTIONS, WeComHelpFormatter, install_formatter
from core.auth import AccessTokenProvider
from core.config import WeComConfig
from core.errors import WeComCLIError
from core.requester import UnifiedRequester


def register_domain_help(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    for name, desc in DOMAIN_DESCRIPTIONS.items():
        subparsers.add_parser(name, help=desc, formatter_class=WeComHelpFormatter)


class _HelpOnlyClient:
    """Stub client for --help mode. Handler closures capture this but are never called."""

    def __getattr__(self, _name: str) -> object:
        raise RuntimeError("Help-only client method called unexpectedly")


def bootstrap(*, verbose: bool = False, debug: bool = False) -> GeneratedWeComClient:
    config = WeComConfig.load()
    requester = UnifiedRequester(config)
    requester.set_verbose(verbose, debug)
    token_provider = AccessTokenProvider(requester, config)
    requester.bind_token_provider(token_provider)
    return GeneratedWeComClient(requester)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wecom",
        formatter_class=WeComHelpFormatter,
        add_help=False,
        description="企业微信命令行工具 — 通过命令行调用企业微信API",
    )
    # Bind formatter immediately so add_subparsers() doesn't crash
    parser._get_formatter = lambda: WeComHelpFormatter(parser.prog)  # type: ignore[assignment]
    parser.add_argument(
        "-h",
        "--help",
        action="store_true",
        default=False,
        dest="wecom_help",
    )
    parser.add_argument(
        "--verbose", action="store_true", default=bool(os.getenv("WECOM_VERBOSE")), help="Print request URLs to stderr"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        default=bool(os.getenv("WECOM_DEBUG")),
        help="Print full request/response JSON to stderr",
    )
    return parser


def route(args: argparse.Namespace, command_table: dict[tuple[str, str], CommandHandler]) -> dict:
    action = str(getattr(args, "__action", None) or getattr(args, "action", ""))
    key = (args.domain, action)
    if key not in command_table:
        raise WeComCLIError(f"Unknown command: {args.domain} {action}")
    return command_table[key](args)


def main(argv: list[str] | None = None) -> int:
    effective_argv = argv if argv is not None else sys.argv[1:]
    parser = build_parser()

    # No args → root help with domain list
    if not effective_argv:
        subparsers = parser.add_subparsers(dest="domain")
        register_domain_help(subparsers)
        install_formatter(parser)
        parser.print_help()
        return 0

    has_help = "-h" in effective_argv or "--help" in effective_argv

    if has_help:
        positional = [a for a in effective_argv if not a.startswith("-")]
        subparsers = parser.add_subparsers(dest="domain")
        if not positional:
            # Root help → lightweight domain list only
            register_domain_help(subparsers)
        else:
            # Domain/action help → full registration with stub client
            register_generated_commands(subparsers, _HelpOnlyClient())  # type: ignore[arg-type]
        install_formatter(parser)
        parser.parse_args(effective_argv)
        # print_help was triggered by our custom flag or argparse
        # For domain-level, the sub-parser's format_help handles it
        # For root level, we need to explicitly print
        if not positional:
            parser.print_help()
        else:
            # argparse handles sub-parser help via SystemExit
            try:
                parser.parse_args(effective_argv)
            except SystemExit:
                pass
        return 0

    # Normal execution path
    args, _ = parser.parse_known_args(effective_argv)
    remaining = [a for a in effective_argv if a not in {"--verbose", "--debug"}]
    if not remaining:
        subparsers = parser.add_subparsers(dest="domain")
        register_domain_help(subparsers)
        install_formatter(parser)
        parser.print_help()
        return 0

    try:
        client = bootstrap(verbose=args.verbose, debug=args.debug)
        subparsers = parser.add_subparsers(dest="domain", required=True)
        command_table = register_generated_commands(subparsers, client)
        install_formatter(parser)
        args = parser.parse_args(effective_argv)
        payload = route(args, command_table)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0
    except WeComCLIError as exc:
        print(f"[wecom-cli] {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        print(f"[wecom-cli] Unexpected error: {exc}", file=sys.stderr)
        print("[wecom-cli] Re-run with --debug for details.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
