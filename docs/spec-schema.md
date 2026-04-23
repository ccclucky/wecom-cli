# WeCom CLI 接口元数据 Schema（v1 草案）

> 目标：提供稳定的接口描述文件，供命令注册、帮助生成、客户端 codegen 与兼容性校验使用。

## 1. 设计原则

- **声明式**：命令、参数、输出、错误均通过 schema 描述。
- **可生成**：可以从 schema 生成 CLI 骨架与文档。
- **可校验**：可做 schema lint、兼容性检查（breaking change detect）。

---

## 2. 顶层结构

建议文件：`spec/commands.v1.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "version": "1.0.0",
  "resources": [
    {
      "name": "agent",
      "commands": []
    }
  ]
}
```

### 字段说明

- `version`：schema 版本（语义化版本）。
- `resources[]`：资源集合（如 `agent`、`user`）。
- `commands[]`：该资源下命令定义。

---

## 3. Command 对象

```json
{
  "name": "get",
  "summary": "Get agent detail",
  "description": "Fetch one agent by id",
  "stability": "stable",
  "input": {},
  "output": {},
  "errors": []
}
```

### 关键字段

- `name`：动作名。
- `summary` / `description`：帮助文案来源。
- `stability`：`experimental | stable | deprecated`。
- `input`：参数定义。
- `output`：成功输出定义。
- `errors[]`：可预期错误码清单。

---

## 4. Input Schema

```json
{
  "args": [
    {
      "name": "agent-id",
      "type": "string",
      "required": true,
      "location": "flag",
      "short": "a",
      "description": "Agent id"
    }
  ]
}
```

### 参数字段

- `name`：参数名（kebab-case）。
- `type`：`string | number | integer | boolean | array | object`。
- `required`：是否必填。
- `location`：`flag | arg | env`。
- `short`：可选短参数。
- `enum`：可选枚举值。
- `default`：默认值。
- `description`：帮助说明。

---

## 5. Output Schema

```json
{
  "formats": ["table", "json", "text"],
  "json_schema": {
    "type": "object",
    "properties": {
      "id": { "type": "string" },
      "name": { "type": "string" }
    },
    "required": ["id", "name"]
  },
  "table": {
    "columns": [
      { "key": "id", "title": "ID" },
      { "key": "name", "title": "Name" }
    ]
  },
  "text": {
    "template": "{{id}}"
  }
}
```

### 约束

- `formats` 至少包含 `json`。
- `json_schema` 为兼容性判断基准。
- `table.columns[].key` 必须存在于 `json_schema.properties`。

---

## 6. Error Schema

```json
[
  {
    "code": "INVALID_ARGUMENT",
    "http_status": 400,
    "retryable": false,
    "message_template": "{{field}} is invalid"
  }
]
```

### 字段说明

- `code`：错误码（与 CLI UX 规范一致）。
- `http_status`：上游状态码映射。
- `retryable`：是否建议重试。
- `message_template`：可用于统一格式化。

---

## 7. Codegen 最小输入要求

为保证可生成命令骨架，Command 至少应包含：

- `name`
- `summary`
- `input.args[]`
- `output.formats`
- `output.json_schema`

可选增强：

- 示例（`examples[]`）
- 权限标记（`scopes[]`）
- 弃用信息（`deprecated.since`、`deprecated.replacement`）

---

## 8. 版本与兼容性策略

- `version` 使用语义化版本。
- 以下变更视为 breaking：
  - 删除命令；
  - 删除参数；
  - 修改参数类型；
  - 删除 json 输出字段；
  - 变更错误码语义。
- v1 冻结后，仅允许向后兼容追加。

---

## 9. 评审通过后的 v1 冻结声明

当以下文档评审通过后，`commands.v1.json` 与 CLI 命令面进入冻结：

1. `docs/architecture.md`
2. `docs/cli-ux.md`
3. `docs/spec-schema.md`

冻结后任何 breaking 变更必须走 v2 提案流程。
