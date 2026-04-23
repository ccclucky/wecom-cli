# WeCom Catalog Watch Issue 处理手册（拿到工单后怎么做）

> 适用于类似：`[WeCom Catalog Watch] API changes detected` 的自动工单。

## 你要做的不是“修 issue”，而是“确认并执行同步”

issue 里会给你三类变化：

- Added（新增接口）
- Removed（文档里消失）
- Modified(method)（同 endpoint 方法变了）

你的目标是判断这些变化是否可信，然后把可信变化落地到仓库。

---

## 5 分钟快速流程

> 自动化现状：daily workflow 检测到变化后，会自动更新 `catalog.yaml`、scaffold domain spec、运行 codegen 并尝试创建草稿 PR。你主要做审核与抽样确认。

### Step 1：取工单报告产物

在对应 workflow run 下载 artifact：

- `catalog.discovery.yaml`
- `wecom-catalog-report.md`
- `catalog.synced.yaml`

### Step 2：本地复现（推荐）

```bash
python scripts/run_catalog_sync.py --mode dry-run
```

看本地报告是否和 issue 一致。

### Step 3：人工抽样校验

对 Added/Removed/Modified 各抽样 3~5 条，确认确实来自官方文档页面。

### Step 4：确认后同步 catalog

```bash
python scripts/run_catalog_sync.py --mode apply
```

这一步会把确认后的目录写回 `specs/wecom/catalog.yaml`。

### Step 5：把目录变化落实为代码变化

```bash
python scripts/scaffold_from_catalog.py --catalog specs/wecom/catalog.yaml --spec-dir specs/wecom --apply
python scripts/codegen.py
```

然后手工补全每个接口：`args/request/examples/test`。

### Step 6：校验

```bash
pytest -q
python scripts/check_api_coverage.py
```

通过后再提 PR 合并。

---

## 决策标准（避免误同步）

- **Added**：文档新增并且路径稳定 -> 接受。
- **Removed**：先确认是否只是文档迁移/折叠，不要立即删。
- **Modified(method)**：优先视为高风险，必须人工核对页面正文。

---

## 一句话

自动 issue 只是“报警器”。
你真正的动作是：**复现 -> 抽样确认 -> apply -> scaffold -> codegen -> 测试 -> PR**。
