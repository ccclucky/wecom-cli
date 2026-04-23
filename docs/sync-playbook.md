# WeCom 接口发现与同步（不看代码版）

这份文档回答一个问题：**“到底怎么拿到所有接口，然后同步？”**

## 一图流

1. **发现候选接口**：抓官方文档（多入口 + doc-id 范围）输出 `catalog.discovery.yaml`
2. **对比差异**：拿 discovery 和 baseline `catalog.yaml` 比较，产出报告
3. **人工确认**：看报告里的 Added / Removed / Modified(method)
4. **同步目录**：确认后把 reconciled 结果写回 `catalog.yaml`
5. **补业务 spec + 生成代码**：更新 `specs/wecom/<domain>.yaml`，再 `codegen`
6. **跑测试与覆盖率校验**：确保没漏实现

---

## 一条命令跑完整流程

### 只看差异（推荐日常）

```bash
python scripts/run_catalog_sync.py --mode dry-run
```

会产出：

- `artifacts/catalog.discovery.yaml`
- `artifacts/wecom-catalog-report.md`
- `artifacts/catalog.synced.yaml`

### 审阅后执行同步

```bash
python scripts/run_catalog_sync.py --mode apply
```

这会把 `artifacts/catalog.synced.yaml` 的结果回写到 `specs/wecom/catalog.yaml`。

---

## 关键澄清

### Q1：URL 后缀（如 100067）是分页吗？

不是传统分页参数。这里按 **doc-id** 处理。脚本支持 `--doc-id-from/--doc-id-to` 做范围探测，并结合 `seeds.txt` 多入口抓取。

### Q2：写入 `catalog.yaml` 就算完成了吗？

不算。`catalog.yaml` 只是“目录分母同步”。
真正能调用的逻辑来自 `specs/wecom/<domain>.yaml` + `python scripts/codegen.py` 生成物。

如果只改 `catalog.yaml` 不补 domain spec，`python scripts/check_api_coverage.py` 会报缺失。

---

## 推荐团队操作规范

1. 每天 workflow 自动跑 `dry-run`（报告+草稿 PR）。
2. 维护者审阅报告。
3. 仅在确认后做 `apply`。
4. 同步补齐 domain spec / 文档示例 / 测试。
