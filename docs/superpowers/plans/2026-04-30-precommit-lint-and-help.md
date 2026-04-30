# Pre-commit Lint + --help Improvement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add pre-commit hooks matching CI checks, and improve `--help` to show domain list and usage examples without requiring bootstrap.

**Architecture:** Pre-commit uses official ruff hook + local mypy/pytest hooks. Help improvement uses a stub client (`_HelpOnlyClient`) to run `register_generated_commands` without bootstrap — argparse exits before any handler is called. Root `wecom --help` uses a lightweight `register_domain_help` with Chinese descriptions. Domain/action-level help uses full registration with stub client.

**Tech Stack:** pre-commit, ruff, mypy, pytest, argparse

---

## File Structure

| File | Action | Responsibility |
|------|--------|---------------|
| `.pre-commit-config.yaml` | Create | Pre-commit hook config matching CI |
| `cli/main.py` | Modify | Add DOMAIN_DESCRIPTIONS, register_domain_help, _HelpOnlyClient; restructure build_parser and main |
| `tests/test_cli.py` | Modify | Add tests for help output, ensure existing tests pass |

---

### Task 1: Pre-commit Config

**Files:**
- Create: `.pre-commit-config.yaml`

- [ ] **Step 1: Create `.pre-commit-config.yaml`**

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

- [ ] **Step 2: Install pre-commit**

Run: `pip install pre-commit && pre-commit install`
Expected: `pre-commit installed at .git/hooks/pre-commit`

- [ ] **Step 3: Verify hooks run**

Run: `pre-commit run --all-files`
Expected: All hooks pass (ruff, ruff-format, mypy, pytest). May take 30-60s on first run.

- [ ] **Step 4: Commit**

```bash
git add .pre-commit-config.yaml
git commit -m "chore: add pre-commit hooks matching CI checks"
```

---

### Task 2: Improve build_parser() — Description and Epilog

**Files:**
- Modify: `cli/main.py:28-33` (`build_parser` function)
- Test: `tests/test_cli.py`

- [ ] **Step 1: Write failing test for new help content**

Add to `tests/test_cli.py`:

```python
def test_build_parser_has_chinese_description():
    parser = build_parser()
    assert "企业微信" in parser.description
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_cli.py::test_build_parser_has_chinese_description -v`
Expected: FAIL — `assert '企业微信' in 'WeCom command line tool'`

- [ ] **Step 3: Update `build_parser()` in `cli/main.py`**

Replace the entire `build_parser` function:

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

使用 wecom <domain> --help 查看指定域的可用命令""",
    )
    parser.add_argument("--verbose", action="store_true", default=bool(os.getenv("WECOM_VERBOSE")),
                        help="Print request URLs to stderr")
    parser.add_argument("--debug", action="store_true", default=bool(os.getenv("WECOM_DEBUG")),
                        help="Print full request/response JSON to stderr")
    return parser
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_cli.py::test_build_parser_has_chinese_description -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add cli/main.py tests/test_cli.py
git commit -m "feat: improve build_parser with Chinese description and usage examples"
```

---

### Task 3: Add Help-Without-Bootstrap — DOMAIN_DESCRIPTIONS, _HelpOnlyClient, main() Restructure

This is the core change. We add three new components to `cli/main.py`:
1. `DOMAIN_DESCRIPTIONS` — Chinese descriptions for all 37 domains
2. `register_domain_help(subparsers)` — lightweight domain listing for root help
3. `_HelpOnlyClient` — stub that lets `register_generated_commands` run without bootstrap

Then restructure `main()` to route help requests through the stub path.

**Files:**
- Modify: `cli/main.py`
- Test: `tests/test_cli.py`

- [ ] **Step 1: Write failing tests for help-without-bootstrap**

Add to `tests/test_cli.py`:

```python
def test_help_shows_domain_list_no_bootstrap(capsys):
    """wecom --help should show domain list without requiring config/env."""
    ret = main(["--help"])
    assert ret == 0
    captured = capsys.readouterr()
    assert "contacts" in captured.out
    assert "messages" in captured.out
    assert "departments" in captured.out


def test_help_no_args_shows_domain_list(capsys):
    """wecom (no args) should show domain list without requiring config/env."""
    ret = main([])
    assert ret == 0
    captured = capsys.readouterr()
    assert "contacts" in captured.out
    assert "企业微信" in captured.out


def test_help_domain_shows_actions_no_bootstrap(capsys):
    """wecom contacts --help should show actions without requiring config/env."""
    with pytest.raises(SystemExit) as exc_info:
        main(["contacts", "--help"])
    assert exc_info.value.code == 0
```

Note: `contacts --help` triggers argparse's built-in `--help` which calls `sys.exit(0)`. The test uses `pytest.raises(SystemExit)`.

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_cli.py::test_help_shows_domain_list_no_bootstrap tests/test_cli.py::test_help_no_args_shows_domain_list tests/test_cli.py::test_help_domain_shows_actions_no_bootstrap -v`
Expected: All FAIL — `main` currently requires bootstrap for domain registration

- [ ] **Step 3: Add DOMAIN_DESCRIPTIONS, register_domain_help, and _HelpOnlyClient to `cli/main.py`**

Add these after the imports, before the `bootstrap` function:

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


def register_domain_help(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    for name, desc in DOMAIN_DESCRIPTIONS.items():
        subparsers.add_parser(name, help=desc)


class _HelpOnlyClient:
    """Stub client for --help mode. Handler closures capture this but are never called."""

    def __getattr__(self, _name: str) -> object:
        raise RuntimeError("Help-only client method called unexpectedly")
```

- [ ] **Step 4: Restructure `main()` in `cli/main.py`**

Replace the entire `main` function:

```python
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
        print(f"[wecom-cli] Re-run with --debug for details.", file=sys.stderr)
        return 1
```

- [ ] **Step 5: Remove unused `register_domain_commands` function from `cli/main.py`**

The old `register_domain_commands` wrapper is no longer called — `main()` now calls `register_generated_commands` directly. Remove the function:

```python
# DELETE this function (lines 37-41):
def register_domain_commands(
    parser: argparse.ArgumentParser, client: GeneratedWeComClient,
) -> dict[tuple[str, str], CommandHandler]:
    subparsers = parser.add_subparsers(dest="domain", required=True)
    return register_generated_commands(subparsers, client)
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `pytest tests/test_cli.py -v`
Expected: All tests PASS

- [ ] **Step 7: Commit**

```bash
git add cli/main.py tests/test_cli.py
git commit -m "feat: add help-without-bootstrap with domain listing and Chinese descriptions"
```

---

### Task 4: Full Suite Verification

**Files:**
- All modified files

- [ ] **Step 1: Run full lint + type check + tests**

Run: `ruff check . && mypy && pytest -q`
Expected: All pass, 0 errors

- [ ] **Step 2: Verify help output manually**

Run: `python -m cli.main --help`
Expected output should include:
- `企业微信命令行工具` in description
- Domain list with Chinese descriptions (contacts, messages, etc.)
- Usage examples in epilog

Run: `python -m cli.main contacts --help`
Expected: Shows contacts subcommands (list, etc.) without requiring env vars

- [ ] **Step 3: Commit any fixes if needed**

```bash
git add -A
git commit -m "fix: address lint/type/test issues from help improvement"
```
