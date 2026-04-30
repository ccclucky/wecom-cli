# WeCom CLI 接口元数据 Schema（v1）

> 目标：提供稳定的接口描述文件，供命令注册、帮助生成、客户端 codegen 与兼容性校验使用。

## 1. 设计原则

- **声明式**：命令、参数、输出、错误均通过 spec 描述。
- **可生成**：可以从 spec 生成 CLI 骨架与文档。
- **可校验**：可做 spec lint、兼容性检查（breaking change detect）。

---

## 2. 文件组织

每个业务域一个 YAML 文件，位于 `specs/wecom/<domain>.yaml`。

当前覆盖 37 个业务域，309 个 endpoint。

示例：`specs/wecom/contacts.yaml`、`specs/wecom/messages.yaml`。

---

## 3. 顶层结构

```yaml
domain: contacts
operations:
  - name: list_users
    cli_action: list
    summary: 列出成员
    method: GET
    endpoint: /cgi-bin/user/simplelist
    args: [...]
    request: {...}
    examples: [...]
    output: {...}
```

### 字段说明

- `domain`：业务域名（对应 CLI 子命令名）。
- `operations[]`：该域下的接口列表。

---

## 4. Operation 对象

```yaml
name: list_users
cli_action: list
summary: 列出成员
method: GET
endpoint: /cgi-bin/user/simplelist
args:
  - name: department_id
    flag: --department-id
    type: int
    default: 1
    help: 部门 ID
    required: true
request:
  query:
    department_id:
      from_arg: department_id
examples:
  - wecom contacts list --department-id 1 --fetch-child
output:
  formats:
    - json
  json_schema:
    type: object
    properties: {...}
```

### 关键字段

- `name`：内部操作名（snake_case）。
- `cli_action`：CLI 子命令名（kebab-case 映射）。
- `summary`：帮助文案。
- `method`：HTTP 方法（GET/POST）。
- `endpoint`：API 路径（`/cgi-bin/...`）。
- `args[]`：参数定义。
- `request`：请求映射（query/body 参数来源）。
- `examples[]`：CLI 使用示例。
- `output`：输出定义。

---

## 5. Arg 对象

```yaml
name: department_id
flag: --department-id
type: int
default: 1
help: 部门 ID
required: true
```

### 参数字段

- `name`：参数名（snake_case）。
- `flag`：CLI 标志名（kebab-case）。
- `type`：`int` | `str` | `bool` | 其他。
- `required`：是否必填。
- `default`：默认值。
- `help`：帮助说明。
- `action`：argparse action（如 `store_true`）。

---

## 6. Request 映射

```yaml
request:
  query:
    department_id:
      from_arg: department_id
    fetch_child:
      int_bool_arg: fetch_child
  body:
    touser:
      from_arg: to_user
```

### 映射类型

- `from_arg`：直接从 CLI 参数取值。
- `int_bool_arg`：将布尔参数转为 int（0/1）。
- 其他映射类型按需扩展。

---

## 7. Output Schema

```yaml
output:
  formats:
    - json
  json_schema:
    type: object
    properties:
      errcode:
        type: integer
      errmsg:
        type: string
      userlist:
        type: array
        items:
          type: object
```

### 约束

- `formats` 至少包含 `json`。
- `json_schema` 为兼容性判断基准。

---

## 8. Codegen 最小输入要求

为保证可生成命令骨架，Operation 至少应包含：

- `name`
- `cli_action`
- `summary`
- `args[]`
- `method` + `endpoint`

可选增强：

- `request`（参数映射）
- `examples[]`
- `output.json_schema`

---

## 9. Catalog（接口目录）

`specs/wecom/catalog.yaml` 是接口目录基线，记录所有应实现接口的元信息：

- `id`：全局唯一标识（如 `contacts.list_users`）
- `domain`、`name`、`endpoint`、`method`
- `doc`：官方文档链接与参数描述

覆盖率以 catalog 为分母计算。运行 `python scripts/check_api_coverage.py` 校验。

---

## 10. 版本与兼容性策略

- Spec 变更需通过 codegen + coverage check 验证。
- 以下变更视为 breaking：
  - 删除 operation；
  - 删除参数；
  - 修改参数类型；
  - 变更 endpoint 或 method。
- v1 冻结后，仅允许向后兼容追加。

---

## 11. 评审通过后的 v1 冻结声明

当以下文档评审通过后，spec 格式与 CLI 命令面进入冻结：

1. `docs/architecture.md`
2. `docs/cli-ux.md`
3. `docs/spec-schema.md`

冻结后任何 breaking 变更必须走 v2 提案流程。
