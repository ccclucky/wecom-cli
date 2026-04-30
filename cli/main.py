"""Command-line interface for WeCom CLI."""

from __future__ import annotations

import argparse
import json
import os
import sys

from apis.generated_client import GeneratedWeComClient
from cli.generated_commands import CommandHandler, register_generated_commands
from core.auth import AccessTokenProvider
from core.config import WeComConfig
from core.errors import WeComCLIError
from core.requester import UnifiedRequester


def bootstrap(*, verbose: bool = False, debug: bool = False) -> GeneratedWeComClient:
    config = WeComConfig.load()
    requester = UnifiedRequester(config)
    requester.set_verbose(verbose, debug)
    token_provider = AccessTokenProvider(requester, config)
    requester.bind_token_provider(token_provider)
    return GeneratedWeComClient(requester)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="wecom", description="WeCom command line tool")
    parser.add_argument("--verbose", action="store_true", default=bool(os.getenv("WECOM_VERBOSE")),
                        help="Print request URLs to stderr")
    parser.add_argument("--debug", action="store_true", default=bool(os.getenv("WECOM_DEBUG")),
                        help="Print full request/response JSON to stderr")
    return parser


def register_domain_commands(
    parser: argparse.ArgumentParser, client: GeneratedWeComClient,
) -> dict[tuple[str, str], CommandHandler]:
    subparsers = parser.add_subparsers(dest="domain", required=True)
    return register_generated_commands(subparsers, client)


def route(args: argparse.Namespace, command_table: dict[tuple[str, str], CommandHandler]) -> dict:
    action = getattr(args, "__action", None) or getattr(args, "action", None)
    key = (args.domain, action)
    if key not in command_table:
        raise WeComCLIError(f"Unknown command: {args.domain} {action}")
    return command_table[key](args)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args, _ = parser.parse_known_args(argv)

    remaining = [a for a in (argv or []) if a not in {"--verbose", "--debug"}]
    if not remaining:
        parser.print_help()
        return 0

    try:
        client = bootstrap(verbose=args.verbose, debug=args.debug)
        command_table = register_domain_commands(parser, client)
        args = parser.parse_args(argv)
        payload = route(args, command_table)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0
    except WeComCLIError as exc:
        print(f"[wecom-cli] {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        print(f"[wecom-cli] Unexpected error: {exc}", file=sys.stderr)
        print(f"[wecom-cli] Re-run with --debug for details.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
