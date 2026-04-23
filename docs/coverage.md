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

## 4. 接口目录抓取方案（多入口，不是单页面）

抓取不是只看一个页面，而是使用 `specs/wecom/seeds.txt` 多入口 crawl：

```bash
python scripts/discover_wecom_apis.py \
  --seed-file specs/wecom/seeds.txt \
  --max-pages 2000 \
  --output artifacts/catalog.discovery.yaml
```

说明：

- 脚本会在官方文档站内（`developer.work.weixin.qq.com`）抓取 `/document/path/*` 页面；
- 支持维护多个种子页（持续扩展 `seeds.txt`），降低漏抓风险；
- 通过正则提取 `/cgi-bin/...` endpoint，并尝试识别页面上的 GET/POST。

## 5. 差异判断与修复

差异类型（`scripts/catalog_diff_report.py`）：

- `Added`：新出现 endpoint；
- `Removed`：基线有但发现结果没有；
- `Modified(method)`：endpoint 相同但请求方法变化。

先出报告（人工审阅）：

```bash
python scripts/catalog_diff_report.py \
  --baseline specs/wecom/catalog.yaml \
  --discovered artifacts/catalog.discovery.yaml \
  --report artifacts/wecom-catalog-report.md \
  --sync-output artifacts/catalog.synced.yaml
```

确认后可自动回写基线（修复动作）：

```bash
python scripts/catalog_diff_report.py \
  --baseline specs/wecom/catalog.yaml \
  --discovered artifacts/catalog.discovery.yaml \
  --report artifacts/wecom-catalog-report.md \
  --apply-baseline specs/wecom/catalog.yaml
```

> 建议策略：默认“报告 + 人工审阅”，确认后再执行 `--apply-baseline`。

## 6. 每日自动巡检（GitHub Actions）

仓库新增 `.github/workflows/wecom-catalog-watch.yml`：

- 每天 UTC 01:00 自动执行（也支持手动触发）；
- 从 `specs/wecom/seeds.txt` 多入口抓取候选接口；
- 生成新增/删除/修改报告（`artifacts/wecom-catalog-report.md`）；
- 有变化时自动创建 Issue，并发起同步 PR（草稿）。
