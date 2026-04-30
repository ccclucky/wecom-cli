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

DOMAIN_DESCRIPTIONS: dict[str, str] = {
    "advanced_feature": "高级功能账号管理",
    "appchat": "应用群聊管理",
    "auth": "授权验证",
    "batch": "异步任务",
    "chatdata": "会话内容存档",
    "checkin": "打卡管理",
    "contacts": "通讯录管理 — 成员、部门、标签",
    "corp": "企业信息",
    "corpgroup": "企业互联",
    "customers": "外部联系人管理",
    "departments": "部门管理",
    "dial": "公费电话",
    "exmail": "企业邮箱",
    "export": "数据导出",
    "externalpay": "外部支付",
    "hardware": "硬件管理",
    "health": "健康上报",
    "hr": "人事管理",
    "idconvert": "ID转换",
    "kf": "客服管理",
    "living": "直播管理",
    "meeting": "会议管理",
    "messages": "消息推送 — 文本、卡片、文件",
    "miniapppay": "小程序支付",
    "miniprogram": "小程序管理",
    "msgaudit": "会话审计",
    "network": "网络管理",
    "oa": "OA数据接口",
    "pstncc": "企业专线电话",
    "school": "家校沟通",
    "security": "安全管理",
    "tags": "标签管理",
    "ticket": "电子发票",
    "unknown": "未知域",
    "users": "用户管理",
    "wedoc": "企业文档",
    "wedrive": "企业微盘",
}


def register_domain_help(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    for name, desc in DOMAIN_DESCRIPTIONS.items():
        subparsers.add_parser(name, help=desc)


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
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="企业微信命令行工具 — 通过命令行调用企业微信API",
        epilog="""\
常用命令:
  wecom contacts list --department-id 1     查看部门成员
  wecom departments list                    查看部门列表
  wecom messages send-text --to-user ...    发送文本消息

使用 wecom <domain> --help 查看指定域的可用命令""",
    )
    parser.add_argument("--verbose", action="store_true", default=bool(os.getenv("WECOM_VERBOSE")),
                        help="Print request URLs to stderr")
    parser.add_argument("--debug", action="store_true", default=bool(os.getenv("WECOM_DEBUG")),
                        help="Print full request/response JSON to stderr")
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
        parser.parse_args(effective_argv)
        return 0

    # Normal execution path
    args, _ = parser.parse_known_args(effective_argv)
    remaining = [a for a in effective_argv if a not in {"--verbose", "--debug"}]
    if not remaining:
        subparsers = parser.add_subparsers(dest="domain")
        register_domain_help(subparsers)
        parser.print_help()
        return 0

    try:
        client = bootstrap(verbose=args.verbose, debug=args.debug)
        subparsers = parser.add_subparsers(dest="domain", required=True)
        command_table = register_generated_commands(subparsers, client)
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
