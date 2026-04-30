# Pre-commit Lint + --help Improvement Design

**Date**: 2026-04-30
**Status**: Approved
**Affects**: `cli/main.py`, `cli/generated_commands.py`, `.pre-commit-config.yaml`

---

## Feature 1: Pre-commit Lint Hooks

### Goal

Run same checks as CI (`ruff check .` + `mypy` + `pytest -q`) on every `git commit`, preventing CI lint failures after push.

### Implementation

**File**: `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.14.13
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: local
    hooks:
      - id: mypy
        name: mypy
        entry: mypy
        language: system
        types: [python]
        pass_filenames: false

      - id: pytest
        name: pytest
        entry: pytest -q
        language: system
        types: [python]
        pass_filenames: false
```

### Key Decisions

- **ruff**: Official pre-commit repo. Runs lint + format. `--fix` auto-fixes; if files change, commit fails and user re-stages.
- **mypy + pytest**: Local hooks matching CI commands exactly. `pass_filenames: false` — these tools scan files themselves.
- **All checks on commit**: User explicitly requested full parity with CI, accepting slower commits.

### Setup

```bash
pip install pre-commit
pre-commit install
```

### CI Alignment

| Check | CI | Pre-commit |
|-------|----|------------|
| `ruff check .` | yes | yes (+ ruff-format) |
| `mypy` | yes | yes |
| `pytest -q` | yes | yes |

---

## Feature 2: --help Improvement

### Current Problem

`wecom --help` only shows `--verbose` and `--debug` flags. 37 domain subcommands are invisible because `register_domain_commands()` requires `bootstrap()` (config + auth), which shouldn't run during help.

### Solution: Empty-shell Subparsers

Register domain subparsers without handlers for `--help` display. No bootstrap, no auth, no config needed.

### Implementation

#### 1. Domain description mapping (`cli/main.py`)

```python
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
```

#### 2. New function: `register_domain_help(parser)`

```python
def register_domain_help(parser: argparse.ArgumentParser) -> None:
    subparsers = parser.add_subparsers(dest="domain")
    for name, desc in DOMAIN_DESCRIPTIONS.items():
        subparsers.add_parser(name, help=desc)
```

#### 3. Updated `build_parser()`

```python
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

使用 wecom <domain> --help 查看指定域的可用命令
""")
    parser.add_argument("--verbose", ...)
    parser.add_argument("--debug", ...)
    register_domain_help(parser)
    return parser
```

#### 4. Updated `main()` flow

```python
def main(argv=None):
    parser = build_parser()
    args, _ = parser.parse_known_args(argv or sys.argv[1:])

    # Help path: no bootstrap needed (covers -h and --help)
    remaining = [a for a in (argv or sys.argv[1:]) if a not in {"--verbose", "--debug"}]
    if not remaining or "-h" in effective_argv or "--help" in effective_argv:
        parser.print_help()
        return 0

    # Normal path: bootstrap + real command registration
    client = bootstrap(verbose=args.verbose, debug=args.debug)
    command_table = register_domain_commands(parser, client)
    args = parser.parse_args(argv or sys.argv[1:])
    payload = route(args, command_table)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0
```

**subparsers 复用方案**: `build_parser()` 创建 parser 和 subparsers 对象并返回。`register_domain_help()` 注册空壳 domain subparser。`register_domain_commands()` 复用同一个 subparsers 对象（通过参数传入），在已有 domain subparser 上追加 action subparsers 和 handlers。argparse 不允许 `add_subparsers()` 调用两次，所以 subparsers 对象只创建一次。

### Help Output Levels

| Command | Shows |
|---------|-------|
| `wecom --help` | Description + domain list (37 domains with Chinese descriptions) + usage examples |
| `wecom contacts --help` | All actions under contacts domain (from generated_commands, but needs empty-shell actions too) |
| `wecom contacts list --help` | Full parameter details (argparse auto-generated, already works) |

### Domain action help

`wecom contacts --help` 显示该 domain 下所有 action。实现方式：给 `register_generated_commands` 增加 `help_only: bool = False` 参数。`help_only=True` 时不绑定 handler 函数，只注册 subparser + 参数定义。这样 `--help` 路径调用 `register_generated_commands(subparsers, DummyClient(), help_only=True)` 即可获得完整 action 列表，无需 bootstrap。

---

## Risks

| Risk | Mitigation |
|------|------------|
| Pre-commit slows commits | User accepted. Can add `SKIP=pytest git commit` to bypass |
| `register_domain_help` + `register_domain_commands` conflict | Reuse subparsers object or restructure registration flow |
| Domain descriptions need maintenance | Single source of truth in `DOMAIN_DESCRIPTIONS` dict |
| ruff --fix modifies files mid-commit | Pre-commit re-stages automatically; if not, commit fails with clear message |
