# 企微接口 100% 覆盖保障机制

> 结论先行：**“100%”不是主观判断，而是由“官方接口清单 + 自动校验 + CI 阻断”共同保证。**

## 1. 单一事实源（Catalog）

- 文件：`specs/wecom/catalog.yaml`
- 内容：当前已冻结的“应实现接口全集”，每个接口有稳定 `id`（如 `contacts.list_users`）。
- 每次同步企微官方文档后，先更新 catalog，再补齐各域 spec。

## 2. 可执行覆盖率校验

运行：

```bash
python scripts/check_api_coverage.py
```

该脚本会输出：

- `coverage`：按 `catalog` 为分母计算覆盖率；
- `missing_ids`：catalog 有但 spec 未实现；
- `unknown_ids`：spec 有但 catalog 未登记；
- `missing_examples`：缺少文档示例的接口。

退出码约束：

- `0`：覆盖率 100%，且无 unknown / missing_examples；
- `2`：覆盖率 < 100%；
- `3`：有未登记接口或缺示例。

## 3. 落地流程（建议）

1. 定期（例如每周）从企微开放平台同步接口目录到 `catalog.yaml`。
2. 每个新增接口都必须在对应 `specs/wecom/<domain>.yaml` 增加 operation。
3. 运行 `python scripts/codegen.py` 生成 API client 与 CLI 骨架。
4. 补测试 + 文档示例，确保 `pytest -q` 与 coverage check 均通过。
5. 在 CI 里把 `python scripts/check_api_coverage.py` 设为必过项。

这样即使接口很多，也可以持续证明“当前分母下的 100% 已实现”。
