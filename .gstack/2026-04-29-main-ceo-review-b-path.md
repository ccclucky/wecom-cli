---
status: ACTIVE
mode: HOLD_SCOPE
approach: B
generated_by: /plan-ceo-review
date: 2026-04-29
branch: main
commit: aa2ebfc
---

# CEO Review Report: wecom-cli B-Path (PRD-Aligned Release)

## Review Scope

Path B: PRD-aligned release. Stabilize MVP, fix critical issues, meet PRD acceptance criteria, prepare for first publish.

## NOT in scope
- MCP server / SDK / library mode (separate project)
- Claude Code skill file (separate project)
- Web UI or dashboard
- 4-layer architecture evolution (v0.2+)
- Connection pooling / httpx migration (only if batch usage emerges)

## What already exists
- Complete request pipeline: UnifiedRequester + AccessTokenProvider
- 309 endpoint coverage via GeneratedWeComClient + generated_commands.py
- Spec-driven codegen pipeline (YAML → Python)
- Auto-discovery pipeline (WeCom docs → YAML specs)
- CI coverage checking
- Config management (env > file)
- Error hierarchy (4 exception classes)
- PRD, architecture doc, spec schema doc

## Critical Issues (must fix before release)

### Issue 1: Codegen type mapping bug
**What:** Codegen produces incorrect type hints (e.g., `limit: bool | None` should be `int | None`).
**Impact:** Arguments passed as wrong types to WeCom API. Requests may fail or produce incorrect results.
**Fix:** Audit `scripts/codegen.py` type mapping logic, fix mapping from spec types to Python types.

### Issue 2: Nested JSON body flattening
**What:** Codegen flattens nested JSON structures into flat function parameters. Complex endpoints (approvals, meetings) generate broken request bodies.
**Impact:** All endpoints with nested request bodies will fail at runtime.
**Fix:** Accept raw JSON via `--body '{...}'` for complex parameters. Simple endpoints keep individual flags.

### Issue 3: Dead code removal
**What:** `apis/contacts.py`, `apis/messages.py`, `apis/customers.py` are not wired to CLI.
**Impact:** Confusing for contributors, dead code in codebase.
**Fix:** Remove or add `# DEPRECATED` markers.

### Issue 4: No catch-all exception handler
**What:** `main()` only catches `WeComCLIError`. Unhandled exceptions produce raw Python tracebacks.
**Impact:** Users see ugly crashes instead of helpful error messages.
**Fix:** Add `except Exception` handler in `main()` that prints clean error and suggests `--debug`.

### Issue 5: No retry on transient failures
**What:** `UnifiedRequester` has no retry logic. Network timeouts and rate limits (errcode 45001) fail immediately.
**Impact:** CLI fails on transient network issues that would succeed on retry.
**Fix:** Add retry with exponential backoff (max 2 retries) to UnifiedRequester.

### Issue 6: Config file not found gives poor error
**What:** When config file is missing, error says "corp_id/corp_secret are required" without mentioning config file path.
**Impact:** Users can't figure out where to put their config.
**Fix:** Include config file path in error message.

### Issue 7: No verbose/debug mode
**What:** No way to see what request was sent or what response was received.
**Impact:** Users can't debug API issues.
**Fix:** Add `--verbose` / `--debug` flags to CLI.

## Error & Rescue Registry

| Method | Failure | Exception | Rescued | User Sees |
|--------|---------|-----------|---------|-----------|
| UnifiedRequester.request | Network timeout | APIRequestError | Y (main) | stderr, exit 2 |
| UnifiedRequester.request | Connection refused | APIRequestError | Y (main) | stderr, exit 2 |
| UnifiedRequester.request | Malformed JSON | APIRequestError | Y (main) | stderr, exit 2 |
| UnifiedRequester.request | errcode != 0 | APIResponseError | Y (main) | stderr, exit 2 |
| UnifiedRequester.request | Rate limit (45001) | APIResponseError | Y (main) | stderr, exit 2 |
| AccessTokenProvider.get_token | Network failure | AuthError | Y (main) | stderr, exit 2 |
| AccessTokenProvider.get_token | Invalid credentials | AuthError | Y (main) | stderr, exit 2 |
| AccessTokenProvider.get_token | Missing fields | AuthError | Y (main) | stderr, exit 2 |
| WeComConfig.load | Missing config | ConfigError | Y (main) | stderr, exit 2 (no path hint) |
| WeComConfig.load | Malformed JSON | ConfigError | Y (main) | stderr, exit 2 |
| WeComConfig.load | Missing corp_id | ConfigError | Y (main) | stderr, exit 2 (no path hint) |
| main() | Unhandled Exception | (various) | N ← GAP | Python traceback |

## Failure Modes Registry

| Codepath | Failure Mode | Rescued? | Tested? | User Sees? | Logged? |
|----------|-------------|----------|---------|------------|---------|
| requester.request | Timeout | Y | Y | stderr | N (no logging) |
| requester.request | DNS failure | Y | N | stderr | N |
| requester.request | Rate limit | Y | N | stderr | N |
| requester.request | Malformed response | Y | Y | stderr | N |
| auth.get_token | Token endpoint down | Y | N | stderr | N |
| auth.get_token | Expired credentials | Y | N | stderr | N |
| config.load | File not found | Y (silent) | N | (auth error later) | N |
| config.load | Invalid JSON | Y | Y | stderr | N |
| main() | Unknown exception | N ← CRITICAL | N | Python traceback | N |
| codegen | Wrong type mapping | N ← CRITICAL | N | Silent wrong behavior | N |
| codegen | Flat nested JSON | N ← CRITICAL | N | API rejection | N |

## Test Gaps (must add for B-path)

1. **test_auth.py** — Token cache hit, refresh, expired, network failure
2. **Codegen type correctness** — Validate generated types match spec types
3. **Nested JSON body structure** — Verify complex endpoints produce correct JSON
4. **Error output format** — Verify stderr output, exit codes for each error type

## Dream State Delta

```
CURRENT STATE              THIS PLAN (B-path)             12-MONTH IDEAL
─────────────────────      ────────────────────────      ─────────────────────
Flat CLI → Client → HTTP   Fix codegen types/body        4-layer architecture
No retry, no logging       Add retry, verbose mode       Full observability
Dead code in apis/         Clean up dead code            Clean codebase
No tests for auth/codegen  Add critical tests            Full test coverage
No version/release process Add version, changelog        Automated release pipeline
No docs for users          Write quickstart guide        Complete documentation
```

## Next Skill Recommendation

Run `/plan-eng-review` to get an engineering-focused deep dive on the codegen fixes and retry logic before implementation.
