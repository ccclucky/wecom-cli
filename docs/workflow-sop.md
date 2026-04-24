# WeCom Catalog 日常处理 SOP（照抄执行版）

> 目标：让维护者拿到自动 issue 后，**不需要理解代码细节**，只按步骤完成一次完整闭环。

---

## 0. 你会在哪些地方操作

1. **GitHub / Actions**：下载 workflow 产物（artifact）。
2. **GitHub / Draft PR**：查看自动生成的改动并决定是否合并。
3. **本地终端（仓库根目录）**：做抽样复核、跑自动化命令、补充修复。

---

## 1. 先下载 workflow 产物（必须）

进入：

- `Actions` -> `WeCom Catalog Watch` -> 对应 run（和 issue 时间一致）

下载 artifact：`wecom-catalog-report`，解压后应看到：

- `catalog.discovery.yaml`
- `wecom-catalog-report.md`
- `catalog.synced.yaml`

如果缺文件：
- 检查 run 是否成功执行到 `Upload report artifacts` 步骤；
- 检查是否打开了正确的 run。

---

## 2. 抽样校验（必须）

打开 `wecom-catalog-report.md`，分别从以下类型抽样 3~5 条：

- Added
- Removed
- Modified(method)

对每条抽样，打开其 `source_url`，核对：

1. endpoint 是否一致；
2. method 是否一致；
3. 是否确为官方文档页面。

> 抽样不通过：先不要合并 PR，在 issue 里备注“本次发现存在误抓取”并附上样本。

---

## 3. 执行自动同步（推荐命令）

在仓库根目录执行（本地）：

```bash
python scripts/run_catalog_sync.py --mode auto-apply
```

该命令会自动完成：

1. 发现并生成 report；
2. 对比并 apply 到 `specs/wecom/catalog.yaml`；
3. scaffold 缺失 spec，并清理已从 catalog 移除的旧 operation；
4. 运行 codegen；
5. 运行 coverage + contract check。

---

## 4. 覆盖文件说明（防止看不懂改动）

一次正常自动同步，通常会改这些位置：

- 目录基线：`specs/wecom/catalog.yaml`
- 规格骨架：`specs/wecom/<domain>.yaml`
- 生成代码：`apis/generated_client.py`、`cli/generated_commands.py`
- 产物报告：`artifacts/*`

你需要重点看：

1. `catalog.yaml` 是否合理（没有明显误删核心接口）；
2. domain spec 是否出现大量 TODO（如果太多，说明仍需补参数）；
3. generated 代码是否跟 spec 数量一致。

---

## 5. 必跑检查命令（提交前）

```bash
pytest -q
python scripts/check_api_coverage.py
```

通过标准：

- `pytest -q` 全绿；
- `check_api_coverage.py` 输出中：
  - `missing_ids = []`
  - `unknown_ids = []`
  - `missing_examples = []`
  - `invalid_contracts = []`

---

## 6. GitHub 上的最终动作

1. 打开自动创建的 Draft PR（通常分支是 `chore/sync-wecom-catalog`）。
2. 把抽样结果写到 PR 描述或评论（简写即可）。
3. 确认检查通过后：
   - 可直接改为 Ready for review 并合并；
   - 或指派同事复核后再合并。

---

## 7. 失败处理（最常见）

### A) workflow 有 issue 但没有 PR

- 先看 run 日志里 `Create sync PR draft when changes detected`；
- 若该步失败，按 issue 报告本地执行第 3/5 步，再手动开 PR。

### B) 发现了很多新增，但参数不完整

- 这是正常情况：catalog 发现的是“接口目录”，参数仍需后续补全；
- 先合并目录同步，再按域逐步补 spec 参数并回归测试。

---

## 8. 一句话流程图

下载 artifact -> 抽样核对 -> `auto-apply` -> 测试/覆盖率 -> 审核 Draft PR -> 合并。
