"""Auto-generated CLI command registration from specs/wecom/*.yaml. DO NOT EDIT."""

from __future__ import annotations

import argparse
from collections.abc import Callable

from apis.generated_client import GeneratedWeComClient

CommandHandler = Callable[[argparse.Namespace], dict]


def register_generated_commands(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
    client: GeneratedWeComClient,
) -> dict[tuple[str, str], CommandHandler]:
    table: dict[tuple[str, str], CommandHandler] = {}

    contacts_parser = subparsers.add_parser(
        'contacts',
        help='contacts 域命令',
    )
    contacts_sub = contacts_parser.add_subparsers(dest='action', required=True)

    contacts_list_users_parser = contacts_sub.add_parser(
        'list',
        help='列出成员',
    )
    contacts_list_users_parser.add_argument(
        '--department-id',
        type=int,
        default=1,
        help='部门 ID',
    )
    contacts_list_users_parser.add_argument(
        '--fetch-child',
        action='store_true',
        help='是否递归拉取子部门',
    )

    def _handle_contacts_list_users(a: argparse.Namespace) -> dict:
        return client.contacts_list_users(
            department_id=a.department_id,
            fetch_child=a.fetch_child,
        )
    table[('contacts', 'list')] = _handle_contacts_list_users

    customers_parser = subparsers.add_parser(
        'customers',
        help='customers 域命令',
    )
    customers_sub = customers_parser.add_subparsers(dest='action', required=True)

    customers_sub.add_parser(
        'list-follow-users',
        help='列出配置了客户联系的成员',
    )

    def _handle_customers_list_follow_users(a: argparse.Namespace) -> dict:
        return client.customers_list_follow_users()
    table[('customers', 'list-follow-users')] = _handle_customers_list_follow_users

    messages_parser = subparsers.add_parser(
        'messages',
        help='messages 域命令',
    )
    messages_sub = messages_parser.add_subparsers(dest='action', required=True)

    messages_send_text_parser = messages_sub.add_parser(
        'send-text',
        help='发送文本消息',
    )
    messages_send_text_parser.add_argument(
        '--to-user',
        type=str,
        required=True,
        help='接收者用户 ID',
    )
    messages_send_text_parser.add_argument(
        '--agent-id',
        type=int,
        required=True,
        help='应用 agent id',
    )
    messages_send_text_parser.add_argument(
        '--content',
        type=str,
        required=True,
        help='文本内容',
    )

    def _handle_messages_send_text(a: argparse.Namespace) -> dict:
        return client.messages_send_text(
            to_user=a.to_user,
            agent_id=a.agent_id,
            content=a.content,
        )
    table[('messages', 'send-text')] = _handle_messages_send_text

    return table
