# WeCom CLI

企业微信（WeCom）命令行工具。37 个业务域，309 个接口，100% 覆盖。

## Install

```bash
pip install -e .
```

要求 Python >= 3.11。

## Quick Start

先配置凭证（二选一）：

**环境变量：**

```bash
export WECOM_CORP_ID="wwxxxxxxxxxxxxxxxx"
export WECOM_CORP_SECRET="xxxxxxxxxxxxxxxxxxxxxxxx"
```

**配置文件** `~/.wecom-cli/config.json`：

```json
{
  "corp_id": "wwxxxxxxxxxxxxxxxx",
  "corp_secret": "xxxxxxxxxxxxxxxxxxxxxxxx"
}
```

然后用：

```bash
# 查看帮助
wecom --help

# 通讯录：列出成员
wecom contacts list --department-id 1 --fetch-child

# 消息：发送文本
wecom messages send-text --to-user zhangsan --agent-id 1000002 --content "hello"

# 客户联系：列出已配置成员
wecom customers list-follow-users
```

## Features

- **37 个业务域全覆盖** — 通讯录、消息、客户、会议、文档、审批、打卡等 309 个 endpoint
- **统一鉴权** — 自动获取和刷新 access_token
- **统一错误处理** — 配置错误、认证失败、API 错误分级输出
- **代码生成** — 基于 YAML spec 自动生成 CLI 命令和 API client
- **每日自动巡检** — GitHub Actions 每日检测接口变更，自动开 PR 同步

## Configuration

| 变量 | 必填 | 默认值 | 说明 |
|------|------|--------|------|
| `WECOM_CORP_ID` | 是 | — | 企业 ID |
| `WECOM_CORP_SECRET` | 是 | — | 应用 Secret |
| `WECOM_BASE_URL` | 否 | `https://qyapi.weixin.qq.com` | API 地址 |
| `WECOM_TIMEOUT_SECONDS` | 否 | `10` | 请求超时（秒） |

优先级：环境变量 > 配置文件。

## Development

```bash
pip install -e ".[dev]"  # 或 pip install ruff mypy pytest
ruff check .
mypy
pytest -q
```

### Catalog 同步

```bash
# 查看差异（日常推荐）
python scripts/run_catalog_sync.py --mode dry-run

# 自动同步（目录 + spec + codegen + 校验）
python scripts/run_catalog_sync.py --mode auto-apply

# 覆盖率检查
python scripts/check_api_coverage.py
```

### Codegen

```bash
python scripts/codegen.py
```

从 `specs/wecom/*.yaml` 生成 `apis/generated_client.py` 和 `cli/generated_commands.py`。

## CI & Release

- **CI**（`.github/workflows/ci.yml`）：ruff + mypy + pytest
- **Catalog Watch**（`.github/workflows/wecom-catalog-watch.yml`）：每日 UTC 01:00 巡检接口变更
- **Release**（`.github/workflows/release-alpha.yml`）：`v*-alpha*` 标签触发，发布到 PyPI

## Documentation

| 文档 | 说明 |
|------|------|
| [Architecture](docs/architecture.md) | 分层架构设计 |
| [CLI UX Spec](docs/cli-ux.md) | 命令命名、输出格式、错误码规范 |
| [Spec Schema](docs/spec-schema.md) | 接口元数据 YAML Schema |
| [PRD](docs/prd.md) | v1 产品需求文档 |
| [Bootstrap](docs/bootstrap.md) | 初始化与快速上手 |
| [Coverage](docs/coverage.md) | 100% 覆盖率保障机制 |
| [Sync Playbook](docs/sync-playbook.md) | 接口发现与同步流程 |
| [Issue Runbook](docs/issue-runbook.md) | 自动 Issue 处理手册 |
| [Workflow SOP](docs/workflow-sop.md) | 日常 Catalog 同步 SOP |

## Project Structure

```
core/       配置、鉴权、请求器、错误处理
cli/        命令入口、参数解析、路由
apis/       业务域 API 适配层（codegen 生成）
models/     共享模型
scripts/    构建/同步/发现脚本
specs/      WeCom 接口元数据（YAML）
tests/      单元测试
docs/       架构与设计文档
artifacts/  构建产物
```

## Roadmap

- **v0.1.x-alpha** — 稳定命令面与错误模型
- **v0.2.x** — 输出格式（table/json）、分页、重试策略
- **v0.3.x** — 插件生态、批量编排

## Contributing

1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/my-feature`
3. 提交改动，确保通过检查：`ruff check . && mypy && pytest -q`
4. 推送并创建 Pull Request

**PR 要求：**
- 通过 CI（ruff / mypy / pytest）
- 新功能需附带测试
- 接口变更需更新对应 `specs/wecom/<domain>.yaml` 并重新 codegen

开发细节见 [Bootstrap](docs/bootstrap.md)，接口同步流程见 [Sync Playbook](docs/sync-playbook.md)。

## Issues

- **Bug 报告**：描述复现步骤、预期行为、实际行为，附上 `wecom --debug` 输出
- **功能请求**：说明使用场景和期望的命令形式（`wecom <resource> <action> [flags]`）
- **接口覆盖**：参考 [Coverage](docs/coverage.md) 检查当前状态，缺少的接口会由每日巡检自动跟踪

提交 Issue 前请先搜索已有 Issue，避免重复。

## License

Private. All rights reserved.
