"""Command-line interface for WeCom CLI."""

from __future__ import annotations

import argparse
import json
import sys

from apis.generated_client import GeneratedWeComClient
from cli.generated_commands import CommandHandler, register_generated_commands
from core.auth import AccessTokenProvider
from core.config import WeComConfig
from core.errors import WeComCLIError
from core.requester import UnifiedRequester


def bootstrap() -> GeneratedWeComClient:
    config = WeComConfig.load()
    requester = UnifiedRequester(config)
    token_provider = AccessTokenProvider(requester, config)
    requester.bind_token_provider(token_provider)
    return GeneratedWeComClient(requester)


def build_parser(
    client: GeneratedWeComClient,
) -> tuple[argparse.ArgumentParser, dict[tuple[str, str], CommandHandler]]:
    parser = argparse.ArgumentParser(prog="wecom", description="WeCom command line tool")
    subparsers = parser.add_subparsers(dest="domain", required=True)
    command_table = register_generated_commands(subparsers, client)
    return parser, command_table


def route(args: argparse.Namespace, command_table: dict[tuple[str, str], CommandHandler]) -> dict:
    key = (args.domain, args.__action)
    if key not in command_table:
        raise WeComCLIError(f"Unknown command: {args.domain} {args.__action}")
    return command_table[key](args)


def main(argv: list[str] | None = None) -> int:
    client = bootstrap()
    parser, command_table = build_parser(client)
    args = parser.parse_args(argv)

    try:
        payload = route(args, command_table)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0
    except WeComCLIError as exc:
        print(f"[wecom-cli] {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
