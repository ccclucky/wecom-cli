# WeCom CLI（企业微信命令行工具）

一个面向企业微信（WeCom）开放接口的轻量 CLI 原型，当前版本聚焦：

- **基础设施能力**：配置、鉴权、统一请求器、统一错误处理
- **全量 API 覆盖**：37 个业务域，309 个 endpoint，100% catalog 覆盖率
- **工程化基线**：lint / type / test CI，alpha 发布流程，每日 catalog 自动巡检

---

## 1. 项目结构

```text
core/      # 配置、鉴权、请求器、统一错误
cli/       # 命令入口、参数解析、路由
apis/      # 业务域 API 适配层（codegen 生成）
models/    # 共享模型
scripts/   # 构建/同步/发现脚本
specs/     # WeCom 接口元数据（YAML）
tests/     # 单元测试
docs/      # 架构与设计文档
artifacts/ # 构建产物（报告、任务清单）
```

---

## 2. 环境要求

- Python >= 3.11

建议先安装开发工具：

```bash
pip install ruff mypy pytest
```

---

## 3. 配置方式

支持两种来源，优先级：**环境变量 > 配置文件**。

### 3.1 环境变量

- `WECOM_CORP_ID`
- `WECOM_CORP_SECRET`
- `WECOM_BASE_URL`（可选，默认 `https://qyapi.weixin.qq.com`）
- `WECOM_TIMEOUT_SECONDS`（可选，默认 `10`）

### 3.2 配置文件

路径：`~/.wecom-cli/config.json`

示例：

```json
{
  "corp_id": "wwxxxxxxxxxxxxxxxx",
  "corp_secret": "xxxxxxxxxxxxxxxxxxxxxxxx",
  "base_url": "https://qyapi.weixin.qq.com",
  "timeout_seconds": 10
}
```

---

## 4. 快速开始

### 4.1 查看帮助

```bash
python -m cli.main --help
```

### 4.2 通讯录：列出成员

```bash
python -m cli.main contacts list --department-id 1 --fetch-child
```

### 4.3 消息：发送文本

```bash
python -m cli.main messages send-text \
  --to-user zhangsan \
  --agent-id 1000002 \
  --content "hello from wecom-cli"
```

### 4.4 客户联系：列出已配置成员

```bash
python -m cli.main customers list-follow-users
```

### 4.5 生成代码（基于 specs）

```bash
python scripts/codegen.py
```

接口元数据位于 `specs/wecom/*.yaml`，生成物包括：

- `apis/generated_client.py`
- `cli/generated_commands.py`
- 文档示例：`docs/examples/generated-apis.md`

---

## 5. 当前已实现能力说明

### 5.1 配置加载（`core/config.py`）
- 读取环境变量与本地配置文件。
- 校验 `corp_id` / `corp_secret` 必填。
- 统一默认值与超时参数解析。

### 5.2 鉴权（`core/auth.py`）
- 通过 `gettoken` 获取 `access_token`。
- 内存缓存 token，并在到期前进行刷新。

### 5.3 统一请求器（`core/requester.py`）
- 统一处理 query / body 编码。
- 自动注入 `access_token`。
- 解析 JSON 并统一处理 WeCom `errcode` 语义。

### 5.4 统一错误处理（`core/errors.py`）
- `ConfigError` / `AuthError` / `APIRequestError` / `APIResponseError`
- CLI 层统一捕获并输出友好错误信息。

---

## 6. 测试与质量检查

```bash
ruff check .
mypy
pytest -q
python scripts/check_api_coverage.py
python scripts/scaffold_from_catalog.py --catalog specs/wecom/catalog.yaml --spec-dir specs/wecom --apply
python scripts/sync_spec_docs.py --catalog specs/wecom/catalog.yaml --spec-dir specs/wecom --apply
python scripts/build_agent_tasks.py --catalog specs/wecom/catalog.yaml --spec-dir specs/wecom
# 一键自动同步（发现 -> catalog apply -> scaffold -> codegen -> contract check）
python scripts/run_catalog_sync.py --mode auto-apply
# 如需允许 auto-apply 清理 catalog 已移除项，必须显式确认
python scripts/run_catalog_sync.py --mode auto-apply --allow-prune-unknown
# 如果触发 CAPTCHA 验证，传入浏览器 cookie 绕过
python scripts/run_catalog_sync.py --mode auto-apply \
  --cookie "$(cat /path/to/cookie.txt)" --delay-min 2.0 --delay-max 4.0
# 单独抓取官方文档候选接口目录
python scripts/discover_wecom_apis.py \
  --seed-file specs/wecom/seeds.txt \
  --menu-tree-file specs/wecom/menu_tree.json \
  --empty-pages-file specs/wecom/empty_pages.json \
  --max-pages 1000 \
  --cookie "$COOKIE_STRING"
```

`check_api_coverage.py` 会同时校验 catalog 覆盖率与接口契约一致性（如 required 参数是否映射到 request）。

> **CAPTCHA 注意**：企微文档站有腾讯验证码反爬。首次访问建议先在浏览器打开 `developer.work.weixin.qq.com` 完成验证，导出 cookie 后通过 `--cookie` 传入。爬虫连续 5 次被拦截会自动终止，避免 IP 被长期封锁。延迟建议 ≥ 2s。

`build_agent_tasks.py` 会生成面向外部 Coding Agent 的产物：

- `artifacts/implementation.tasks.yaml`
- `artifacts/implementation.summary.md`
- `artifacts/coding-agent-prompt.md`

其中 `implementation.tasks.yaml` 是给 Coding Agent 的权威输入；`implementation.summary.md` 仅供人工快速浏览。

---

## 7. CI 与发布

- CI 工作流：`.github/workflows/ci.yml`
  - 执行 ruff / mypy / pytest
- Alpha 发布工作流：`.github/workflows/release-alpha.yml`
  - 触发条件：`v*-alpha*` 标签
  - 构建并发布到 PyPI（需仓库配置发布凭据）

---

## 8. 版本计划（建议）

- **v0.1.x-alpha**：稳定命令面与错误模型
- **v0.2.x**：补齐更多域能力（部门管理、素材、群机器人等）
- **v0.3.x**：引入更完整的输出格式（table/json）、分页与重试策略

欢迎继续补充需求，我们可以按 TDD 节奏逐步迭代。

补充：接口全量覆盖治理可见 `docs/coverage.md`。


> 提示：`catalog.yaml` 仅是目录同步（覆盖率分母），要真正生效还需要补 `specs/wecom/<domain>.yaml` 并执行 `python scripts/codegen.py`。


同步流程说明（不看代码版）：`docs/sync-playbook.md`


自动 issue 处理手册：`docs/issue-runbook.md`

无脑执行版 SOP：`docs/workflow-sop.md`

### 完整文档索引

| 文档 | 说明 |
|------|------|
| `docs/architecture.md` | 分层架构设计（CLI / Application / Domain / Infrastructure） |
| `docs/cli-ux.md` | CLI 命令命名、输出格式、错误码规范 |
| `docs/spec-schema.md` | 接口元数据 YAML Schema 定义 |
| `docs/prd.md` | v1 产品需求文档（覆盖率目标与验收标准） |
| `docs/bootstrap.md` | 项目初始化与快速上手 |
| `docs/coverage.md` | 100% 覆盖率保障机制 |
| `docs/sync-playbook.md` | 接口发现与同步流程说明 |
| `docs/issue-runbook.md` | 自动 Issue 处理手册 |
| `docs/workflow-sop.md` | 日常 Catalog 同步 SOP（照抄执行版） |
| `docs/examples/generated-apis.md` | 生成 API 使用示例 |
