# WeCom CLI UX 规范（v1）

## 1. 命令规范

## 1.1 命名约定

- 命令结构：`wecom <resource> <action> [flags]`
- `resource` 使用名词单数（如 `agent`、`user`）。
- `action` 使用动词原形（如 `get`、`list`、`create`、`update`、`delete`）。

## 1.2 参数约定

- 长参数统一使用 kebab-case：`--output`、`--request-id`。
- 短参数仅用于高频选项：`-o` (`--output`)、`-q` (`--quiet`)。
- 布尔参数默认 false，显式启用用 `--xxx`。
- 列表参数支持重复输入：`--field id --field name`。

## 1.3 全局参数

- `--output <table|json|text>`：输出格式，默认 `table`。
- `--quiet`：仅输出必要结果，抑制提示信息。
- `--verbose`：显示调试信息（请求路径、耗时、trace id）。
- `--no-color`：禁用颜色输出，便于日志采集。

---

## 2. 输出规范

## 2.1 成功输出

- **table（默认）**：面向人读，字段顺序稳定。
- **json**：面向程序，字段命名与 schema 一致。
- **text**：仅输出核心值（如 ID、token），适合 shell 管道。

示例：

```bash
wecom agent list --output table
wecom agent get --agent-id 100001 --output json
```

## 2.2 稳定性规则

- 非破坏性迭代不得更改既有字段语义。
- `json` 输出字段不得随意改名或改变类型。
- 额外字段仅允许追加，不允许替换。

## 2.3 退出码

- `0`：成功。
- `2`：用户输入错误（参数缺失、格式非法）。
- `3`：认证/授权失败。
- `4`：远端服务错误或网络错误。
- `5`：内部异常（bug）。

---

## 3. 错误规范

## 3.1 错误结构

统一输出结构（`--output json` 时）：

```json
{
  "error": {
    "code": "INVALID_ARGUMENT",
    "message": "agent-id is required",
    "hint": "Use --agent-id <id>",
    "request_id": "req-xxxx"
  }
}
```

## 3.2 错误分类

- `INVALID_ARGUMENT`：参数不合法。
- `UNAUTHORIZED`：凭证缺失或过期。
- `FORBIDDEN`：无权限。
- `NOT_FOUND`：目标资源不存在。
- `CONFLICT`：状态冲突。
- `UPSTREAM_ERROR`：远端异常。
- `INTERNAL_ERROR`：本地执行异常。

## 3.3 用户可操作性

- 错误信息必须包含可执行 hint。
- 如可重试，明确提示重试建议（例：等待后重试）。
- `--verbose` 下增加调试上下文（trace id、endpoint）。

---

## 4. 帮助与示例

- 每个命令至少包含 1 条最小可用示例。
- 对危险命令（delete/update）提供确认说明或 `--yes` 机制。
- 帮助文案优先中文，关键术语保留英文。

---

## 5. v1 命令面冻结策略

- 冻结范围：命令名、参数名、退出码、错误码、json 输出字段。
- 冻结时点：评审通过并打上 `v1-freeze` 标签后生效。
- 冻结后仅允许：
  - 向后兼容的字段追加；
  - 新命令新增（不得破坏已有命令行为）。
- 破坏性变更必须进入 v2 规划并提供迁移指南。
