# B-Path Implementation Summary
Generated: 2026-04-29
Branch: main
Commit: aa2ebfc

## Review Status
- CEO Review: ISSUES_OPEN (4 critical gaps, HOLD_SCOPE)
- Eng Review: ISSUES_OPEN (14 issues found, 0 unresolved)
- Outside Voice: ISSUES (10 findings, 3 cross-model tensions resolved)

## 14 Issues to Fix

### P0 (Critical - must fix before release)

| # | Issue | File | Resolution |
|---|-------|------|------------|
| A1 | 类型映射 bug | codegen.py + specs | 修 spec + codegen 名字守卫 (limit/offset→int) |
| A3 | dest='action' 冲突 | codegen.py + main.py | 改 dest='__action'，更新 route() |
| A5 | 嵌套 JSON 处理 | codegen.py + specs | Spec 显式 `mode: body` 标记 |
| X3 | 嵌套检测改标记 | specs | 用 spec mode 字段替代自动检测 |

### P1 (Should fix)

| # | Issue | File | Resolution |
|---|-------|------|------------|
| A2 | Spec 无验证层 | codegen.py | 加 `_validate_spec()` + `compile()` |
| A4 | 重试 + errcode 分类 | requester.py | token 刷新 + 限流退避 + 防重入标记 |
| C1 | 死代码 | apis/*.py | 删除 3 个 legacy 文件 |
| C2 | bootstrap 延迟 | main.py | 拆分 parser 构建 + handler 注册 |
| C4 | verbose/debug | main.py + requester.py | 加 --verbose + --debug 输出到 stderr |
| X1 | 214 bool 审计 | specs | 系统性检查哪些 bool 应为 int |
| X2 | 重试防重入 | requester.py | 标记 `_retrying` 防递归 |
| X4 | diff 验证 | codegen.py | codegen 后 diff 新旧生成文件 |
| X5 | config 错误含路径 | config.py | ConfigError 加文件路径 |

### Deferred

| # | Issue | Reason |
|---|-------|--------|
| C3 | `_strip_none()` | 保持现状，预期行为 |

## Test Coverage
- Current: 21% (8/38 paths)
- Target: 100% (30 gaps to fill)
- Test plan: `.gstack/ITTLN015-main-eng-review-test-plan-*.md`

## Parallelization Strategy
- Lane A: codegen fixes (A1, A3, A5, X3, A2, X4) — scripts/codegen.py + specs/
- Lane B: core infra (A4, X2, C1, C2, C4, X5) — core/, cli/, apis/
- Merge order: A + B parallel → codegen → pytest

## Architecture
```
CLI (argparse)
  ├── build_parser_skeleton()  -- before bootstrap
  ├── bootstrap()              -- load config, create client
  └── register_handlers()      -- after bootstrap
      ↓
GeneratedWeComClient
  ├── 309 generated methods
  └── call UnifiedRequester.request()
      ↓
UnifiedRequester
  ├── request() + retry logic
  ├── errcode classification
  └── token refresh on 40014/42001
      ↓
AccessTokenProvider
  ├── get_token() + cache
  └── force_refresh on retry
```

## Next Steps
1. `/ship` 开始实现
2. 先做 Lane A (codegen) 或 Lane B (core infra)，并行
3. Merge 后运行 `python scripts/codegen.py`
4. `python -m pytest` 验证
5. 309 endpoint smoke test (手动试几个 domain)