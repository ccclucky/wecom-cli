# WeCom CLI 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

企业微信（WeCom）高效率命令行工具。
**37 个业务域，300+ 接口，100% 覆盖。**

---

## 💡 为什么选择 WeCom CLI?

- **工业级同步**：基于 API Menu 树自动发现接口，每日 GitHub Actions 自动巡检接口变更。
- **类型安全**：100% Mypy 静态类型覆盖，生成的 API Client 具备完整的 IDE 补全。
- **现代化体验**：支持中文帮助信息、领域分组导航、自动 Token 刷新。
- **开发者友好**：基于 YAML Spec 的代码生成架构，极易扩展和维护。

---

## 📦 安装

```bash
pip install -e .
```

*要求 Python >= 3.11*

## 🚀 快速上手

配置凭证（支持环境变量或配置文件）：

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

### 常用命令示例
```bash
# 查看帮助（交互式分组）
wecom --help

# 通讯录：列出成员
wecom contacts list --department-id 1 --fetch-child

# 消息：发送文本
wecom messages send-text --to-user zhangsan --agent-id 1000002 --content "hello"

# 客户联系：列出已配置成员
wecom customers list-follow-users
```

## ✨ 核心特性

- **业务域全覆盖** — 通讯录、消息、客户、会议、文档、审批、打卡等所有 Endpoint。
- **自动化生命周期** — 自动获取和刷新 `access_token`，统一错误分类输出。
- **自愈式架构** — 每日自动扫描文档发现新接口，自动提交 PR 更新 Spec 和 Client。
- **强类型保障** — 拒绝 Any 类型，确保开发时的逻辑准确性。

## 🛠️ 开发者指南

我们使用 `pre-commit` 来保障代码质量。

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 安装并激活 pre-commit hooks
pre-commit install

# 手动运行全量检查
pre-commit run --all-files
```

### 自动化脚本
- **Catalog 同步**: `python scripts/run_catalog_sync.py --mode auto-apply`
- **代码生成**: `python scripts/codegen.py`
- **覆盖率检查**: `python scripts/check_api_coverage.py`

## 📚 文档中心

| 文档 | 说明 |
|------|------|
| [Architecture](docs/architecture.md) | 分层架构设计 |
| [CLI UX Spec](docs/cli-ux.md) | 命令命名、输出格式规范 |
| [Bootstrap](docs/bootstrap.md) | 环境初始化指南 |
| [Coverage](docs/coverage.md) | 100% 覆盖率保障机制 |
| [Sync Playbook](docs/sync-playbook.md) | 接口发现与同步流程 |

## 🤝 贡献指南

1. Fork 本仓库并创建特性分支。
2. 确保所有检查通过：`pre-commit run --all-files`。
3. 接口变更需更新对应 `specs/wecom/<domain>.yaml` 并重新 codegen。
4. 提交 PR 并在描述中说明背景。

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源。
