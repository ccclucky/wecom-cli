"""Command-line interface for WeCom CLI."""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Callable

from apis.contacts import ContactsAPI
from apis.customers import CustomersAPI
from apis.messages import MessagesAPI
from core.auth import AccessTokenProvider
from core.config import WeComConfig
from core.errors import WeComCLIError
from core.requester import UnifiedRequester

CommandHandler = Callable[[argparse.Namespace], dict]


def bootstrap() -> tuple[ContactsAPI, MessagesAPI, CustomersAPI]:
    config = WeComConfig.load()
    requester = UnifiedRequester(config)
    token_provider = AccessTokenProvider(requester, config)
    requester.bind_token_provider(token_provider)
    return ContactsAPI(requester), MessagesAPI(requester), CustomersAPI(requester)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="wecom", description="WeCom command line tool")
    subparsers = parser.add_subparsers(dest="domain", required=True)

    contacts_parser = subparsers.add_parser("contacts", help="通讯录域命令")
    contacts_sub = contacts_parser.add_subparsers(dest="action", required=True)
    contacts_list = contacts_sub.add_parser("list", help="列出成员")
    contacts_list.add_argument("--department-id", type=int, default=1)
    contacts_list.add_argument("--fetch-child", action="store_true")

    messages_parser = subparsers.add_parser("messages", help="消息域命令")
    messages_sub = messages_parser.add_subparsers(dest="action", required=True)
    send_text = messages_sub.add_parser("send-text", help="发送文本消息")
    send_text.add_argument("--to-user", required=True)
    send_text.add_argument("--agent-id", required=True, type=int)
    send_text.add_argument("--content", required=True)

    customers_parser = subparsers.add_parser("customers", help="客户联系域命令")
    customers_sub = customers_parser.add_subparsers(dest="action", required=True)
    customers_sub.add_parser("list-follow-users", help="列出配置了客户联系的成员")

    return parser


def route(
    args: argparse.Namespace,
    contacts: ContactsAPI,
    messages: MessagesAPI,
    customers: CustomersAPI,
) -> dict:
    table: dict[tuple[str, str], CommandHandler] = {
        ("contacts", "list"): lambda a: contacts.list_users(a.department_id, a.fetch_child),
        ("messages", "send-text"): lambda a: messages.send_text(
            to_user=a.to_user,
            agent_id=a.agent_id,
            content=a.content,
        ),
        ("customers", "list-follow-users"): lambda _a: customers.list_follow_users(),
    }

    key = (args.domain, args.action)
    if key not in table:
        raise WeComCLIError(f"Unknown command: {args.domain} {args.action}")
    return table[key](args)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        contacts, messages, customers = bootstrap()
        payload = route(args, contacts, messages, customers)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0
    except WeComCLIError as exc:
        print(f"[wecom-cli] {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
