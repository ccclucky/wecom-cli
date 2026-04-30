"""Custom argparse help formatter for WeCom CLI — grouped, readable output."""

from __future__ import annotations

import argparse
import sys

# Domains grouped by function, ordered by usage frequency.
DOMAIN_GROUPS: dict[str, dict[str, str]] = {
    "通讯录": {
        "contacts": "成员、部门、标签",
        "departments": "部门管理",
        "users": "用户管理",
        "tags": "标签管理",
        "idconvert": "ID 转换",
    },
    "消息": {
        "messages": "文本、卡片、文件推送",
    },
    "OA / 协同": {
        "oa": "OA 数据接口",
        "checkin": "打卡管理",
        "meeting": "会议管理",
        "living": "直播管理",
        "appchat": "应用群聊管理",
        "wedoc": "企业文档",
        "wedrive": "企业微盘",
    },
    "客户 / 外部": {
        "customers": "外部联系人管理",
        "kf": "客服管理",
        "externalpay": "外部支付",
    },
    "安全 / 审计": {
        "security": "安全管理",
        "msgaudit": "会话审计",
        "chatdata": "会话内容存档",
    },
    "企业": {
        "corp": "企业信息",
        "corpgroup": "企业互联",
        "batch": "异步任务",
        "export": "数据导出",
    },
    "应用": {
        "auth": "授权验证",
        "miniprogram": "小程序管理",
        "miniapppay": "小程序支付",
        "advanced_feature": "高级功能账号管理",
    },
    "其他": {
        "exmail": "企业邮箱",
        "dial": "公费电话",
        "pstncc": "企业专线电话",
        "hardware": "硬件管理",
        "health": "健康上报",
        "hr": "人事管理",
        "school": "家校沟通",
        "ticket": "电子发票",
        "network": "网络管理",
        "unknown": "未知域",
    },
}

# Flat lookup: domain -> description
DOMAIN_DESCRIPTIONS: dict[str, str] = {
    domain: desc for group in DOMAIN_GROUPS.values() for domain, desc in group.items()
}

# ANSI helpers (no-op when not a tty)
_BOLD = "\033[1m" if sys.stderr.isatty() else ""
_DIM = "\033[2m" if sys.stderr.isatty() else ""
_CYAN = "\033[36m" if sys.stderr.isatty() else ""
_RESET = "\033[0m" if sys.stderr.isatty() else ""


def _pad(text: str, width: int) -> str:
    return text.ljust(width)


class WeComHelpFormatter(argparse.HelpFormatter):
    """Produces grouped, readable help output for wecom CLI.

    Stores a back-reference to the owning parser via bind().
    When format_help is called without a bound parser (e.g. during
    add_subparsers prog computation), falls back to default formatting.
    """

    _bound_parser: argparse.ArgumentParser | None = None

    def bind(self, parser: argparse.ArgumentParser) -> None:
        self._bound_parser = parser

    def format_help(self) -> str:
        parser = self._bound_parser
        if parser is None:
            return super().format_help()

        # Find subparsers action
        sp_action = None
        for action in parser._actions:
            if isinstance(action, argparse._SubParsersAction):
                sp_action = action
                break

        if sp_action is None:
            return super().format_help()

        # Root parser has prog="wecom", domain parser has prog="wecom <domain>"
        is_root = " " not in parser.prog

        if is_root:
            return self._format_root_help(sp_action)

        # Domain level — check if sub-choices have subparsers (real actions)
        if sp_action.choices:
            first_choice = next(iter(sp_action.choices.values()))
            has_sub_subparsers = any(isinstance(a, argparse._SubParsersAction) for a in first_choice._actions)
            if has_sub_subparsers:
                # This is a domain parser whose sub-choices are action parsers with their own subparsers
                # Shouldn't happen normally but handle gracefully
                return self._format_domain_help(sp_action)
            return self._format_domain_help(sp_action)

        return super().format_help()

    def _format_root_help(self, sp_action: argparse._SubParsersAction) -> str:
        lines: list[str] = []

        lines.append(f"{_BOLD}Usage:{_RESET}  wecom {_DIM}[options]{_RESET} <domain> <action> [action-flags]")
        lines.append("")
        lines.append("企业微信命令行工具 — 通过命令行调用企业微信 API")
        lines.append("")

        lines.append(f"{_CYAN}{_BOLD}常用命令:{_RESET}")
        lines.append("  wecom contacts list --department-id 1     查看部门成员")
        lines.append("  wecom departments list                    查看部门列表")
        lines.append("  wecom messages send-text --to-user ...    发送文本消息")
        lines.append("")

        max_name_len = max(len(d) for d in DOMAIN_DESCRIPTIONS)
        for group_name, domains in DOMAIN_GROUPS.items():
            lines.append(f"{_CYAN}{_BOLD}{group_name}:{_RESET}")
            for domain, desc in domains.items():
                lines.append(f"  {_pad(domain, max_name_len)}  {desc}")
            lines.append("")

        lines.append(f"用 {_CYAN}wecom <domain> --help{_RESET} 查看域内命令")
        lines.append("")
        lines.append(f"{_CYAN}{_BOLD}Options:{_RESET}")
        lines.append("  -h, --help     显示帮助")
        lines.append("  --verbose      打印请求 URL 到 stderr")
        lines.append("  --debug        打印完整请求/响应 JSON 到 stderr")
        lines.append("")

        return "\n".join(lines)

    def _format_domain_help(self, sp_action: argparse._SubParsersAction) -> str:
        lines: list[str] = []
        prog = self._prog
        domain = prog.split()[-1] if " " in prog else prog

        domain_desc = DOMAIN_DESCRIPTIONS.get(domain, "")
        desc_suffix = f" — {domain_desc}" if domain_desc else ""

        lines.append(f"{_BOLD}Usage:{_RESET}  wecom {_DIM}[options]{_RESET} {domain} <action> [action-flags]")
        lines.append("")
        lines.append(f"{domain}{desc_suffix}")
        lines.append("")

        lines.append(f"{_CYAN}{_BOLD}命令:{_RESET}")
        # Get help text from _SubParsersAction._choices_actions, not from sub-parser internals
        choices_help: dict[str, str] = {}
        for choice_act in sp_action._choices_actions:
            choices_help[choice_act.dest] = choice_act.help or ""

        actions: list[tuple[str, str]] = []
        for name in sp_action.choices:
            actions.append((name, choices_help.get(name, "")))

        if actions:
            max_name_len = max(len(a[0]) for a in actions)
            for name, help_text in actions:
                lines.append(f"  {_pad(name, max_name_len)}  {help_text}")

        lines.append("")
        lines.append(f"用 {_CYAN}wecom {domain} <action> --help{_RESET} 查看参数详情")
        lines.append("")

        return "\n".join(lines)


def install_formatter(parser: argparse.ArgumentParser) -> None:
    """Attach WeComHelpFormatter to parser and all sub-parsers."""
    parser.formatter_class = WeComHelpFormatter  # type: ignore[assignment]

    def _make_fmt(p: argparse.ArgumentParser = parser) -> WeComHelpFormatter:
        fmt = WeComHelpFormatter(p.prog)
        fmt.bind(p)
        return fmt

    parser._get_formatter = _make_fmt  # type: ignore[assignment]

    for action in parser._actions:
        if isinstance(action, argparse._SubParsersAction):
            for sub_parser in action.choices.values():
                sub_parser.formatter_class = WeComHelpFormatter  # type: ignore[assignment]
                _install_sub(sub_parser)


def _install_sub(parser: argparse.ArgumentParser) -> None:
    def _make_fmt(p: argparse.ArgumentParser = parser) -> WeComHelpFormatter:
        fmt = WeComHelpFormatter(p.prog)
        fmt.bind(p)
        return fmt

    parser._get_formatter = _make_fmt  # type: ignore[assignment]
