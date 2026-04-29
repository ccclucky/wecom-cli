---
status: ACTIVE
generated_by: /office-hours
date: 2026-04-29
branch: main
---

# Design Doc: wecom-cli

## Problem Statement

Enterprise WeChat (WeCom) provides a rich public API with 309+ endpoints, but using them requires writing custom code for each operation. The official CLI (WecomTeam/wecom-cli) has significant limitations: it gates features behind a 10-person company limit for commercialization purposes, covers fewer endpoints, and restricts what users can do.

**Pain point (real):** Developers and teams who want to automate WeCom operations must either write custom scripts or tolerate the official CLI's restrictions. This is a daily frustration for teams using WeCom at scale.

**Trend (agent era):** The rise of AI agents (Claude Code, etc.) creates a new use case: a CLI tool that agents can call directly to perform enterprise operations (messaging, scheduling, contacts, todos, meetings, docs). The CLI becomes the "hands" of a digital employee agent.

## User

**Primary:** Developers and teams using WeCom who want CLI-based automation without restrictions.

**Secondary:** AI agents that need a command-line interface to interact with WeCom APIs. Users install the CLI, wrap it as a skill, and agents can perform enterprise operations.

**Ultimate vision:** Digital employee agent that handles scheduling, communication, document management, and other assistant work.

## Differentiation

| Dimension | Official CLI (WecomTeam) | wecom-cli (this project) |
|-----------|--------------------------|--------------------------|
| Endpoint coverage | Limited | 309+ (100% of documented APIs) |
| Commercial restrictions | Yes (10-person company limit) | None |
| Open source freedom | Restrictive license | Full access, no gating |
| Extensibility | Closed | Spec-driven codegen, easy to extend |
| Agent-friendly | Partial | Designed for agent consumption |

**Core differentiation:** No commercial restrictions. Users can implement any creative use case without hitting paywalls or feature gates.

## Architecture

```
                    ┌─────────────────┐
                    │   CLI (argparse) │  ← cli/main.py (~55 lines) + generated_commands.py
                    │   Entry point    │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ GeneratedWeCom   │  ← apis/generated_client.py (auto-generated)
                    │ Client           │  ← apis/contacts.py, messages.py, customers.py
                    └────────┬────────┘     (legacy, not wired to CLI yet)
                             │
                    ┌────────▼────────┐
                    │ UnifiedRequester │  ← core/requester.py
                    │ (HTTP + auth)    │     core/auth.py (token management)
                    └────────┬────────┘     core/config.py (env/file config)
                             │              core/errors.py (exception hierarchy)
                    ┌────────▼────────┐
                    │  WeCom API       │
                    │  (309 endpoints) │
                    └─────────────────┘
```

**Key architectural property:** Core (config, auth, requester, errors) and API layer are pure Python with zero CLI coupling. The only argparse binding exists in auto-generated `cli/generated_commands.py` and the ~55-line `cli/main.py` router. This CLI-agnostic design is a deliberate quality property, not accidental, even though SDK/library mode is not a deliverable.

**Hand-written API modules:** `apis/contacts.py`, `apis/messages.py`, `apis/customers.py` are legacy implementations that predate the codegen pipeline. They are not currently wired into the CLI (only `GeneratedWeComClient` is used). They should be considered deprecated once their functionality is fully covered by generated methods.

**Zero external dependencies:** The project uses only Python stdlib (`urllib.request`, `argparse`, `json`). This is a deliberate constraint: no `httpx`, no `requests`, no third-party runtime dependencies. Tradeoff: no connection pooling, no retry logic, no HTTP/2. Acceptable for a CLI tool; upgrade to `httpx` if batch/heavy usage patterns emerge.

### Spec Format

Each YAML spec defines a domain of endpoints. Example:

```yaml
# Simplified illustration; see specs/wecom/*.yaml for the actual schema
# consumed by codegen.py.
domain: messages
endpoints:
  - name: send
    method: POST
    path: /cgi-bin/message/send
    params:
      - name: touser
        type: string
        required: false
      - name: msgtype
        type: string
        required: true
```

Regenerate with: `python scripts/codegen.py`

### Discovery Pipeline

The discovery pipeline scrapes WeCom's public API documentation pages, extracts endpoint metadata (method, path, parameters), and writes YAML specs to `specs/wecom/`.

- `scripts/discover_wecom_apis.py` — scrapes doc pages, extracts endpoint metadata
- `scripts/sync_spec_docs.py` — reconciles discovered endpoints with existing specs
- `scripts/run_catalog_sync.py` — orchestrates full discovery + sync + codegen
- `scripts/catalog_diff_report.py` — reports what changed between runs
- `specs/wecom/catalog.yaml` — master catalog of all known endpoints

Maintainers run the pipeline when WeCom adds or changes APIs. CI can validate coverage on each run.

## Scope Decisions

### In scope (this project)
- CLI tool covering all 309+ WeCom API endpoints
- Spec-driven code generation pipeline
- Auto-discovery and catalog sync from WeCom docs
- Structured JSON output for machine consumption
- pip install distribution

### NOT in scope (separate projects)
- Claude Code skill file (separate project wraps this CLI)
- MCP server (separate project wraps this CLI)
- SDK / library mode (the CLI IS the interface)
- Web UI or dashboard

**Rationale:** Clean separation of concerns. The CLI does one thing well: expose WeCom APIs as commands. Upper layers (skill, MCP, SDK) are free to wrap it however they want. The CLI-agnostic core is an architectural quality, not a deliverable.

## Configuration

**Config file:** `~/.wecom-cli/config.json`
```json
{
  "corp_id": "string",
  "corp_secret": "string",
  "base_url": "https://qyapi.weixin.qq.com",
  "timeout_seconds": 10.0
}
```

**Environment variables (override file):**
- `WECOM_CORP_ID`
- `WECOM_CORP_SECRET`
- `WECOM_BASE_URL`
- `WECOM_TIMEOUT_SECONDS`

**Precedence:** env vars > config file

**Auth flow:** CLI fetches access token via `/cgi-bin/gettoken` using corp_id + corp_secret. `AccessTokenProvider` caches the token with a 30-second expiry buffer to prevent stale token usage.

## Error Handling & Exit Codes

| Exit code | Meaning | Source |
|-----------|---------|--------|
| 0 | Success | `main()` returns 0 |
| 2 | WeComCLIError (config/auth/API error) | Caught in `main()` |
| 1 | Unexpected crash (unhandled exception) | Python default |

**Error hierarchy:**
```
WeComCLIError
  ├── ConfigError     — missing/invalid config
  ├── AuthError       — token fetch failure, expired token
  ├── APIRequestError — network/timeout errors
  └── APIResponseError — WeCom API returned error (errcode != 0)
```

**Output format (errors):**
```
[wecom-cli] Error message here
```
Printed to stderr. JSON output is not produced on error exit code 2.

**Output format (success):**
```json
{
  "errcode": 0,
  "errmsg": "ok",
  "...": "response fields"
}
```
WeCom API response is passed through as-is. No normalization layer.

**Transient failures:** No retry logic currently. `urllib.request.urlopen` uses the configured timeout (default 10s). Token expiry is handled by `AccessTokenProvider` (refetch on stale). WeCom rate limit errors (errcode 45001) are surfaced to the caller as `APIResponseError`.

## Distribution

- **Package:** `pip install wecom-cli`
- **Entry point:** `wecom` command (registered via `pyproject.toml`)
- **Python:** >= 3.11 (stdlib-only, no external dependencies)

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| WeCom API changes break endpoints | Med | Med | Auto-discovery pipeline detects changes, codegen regenerates |
| Official CLI adds more features | Low | Low | Unrestricted access remains our moat |
| Agent ecosystem shifts away from CLI | Low | High | CLI-agnostic core allows easy MCP/SDK wrapping |
| Maintenance burden for 309 endpoints | Med | Med | Codegen reduces manual work to spec updates |
| urllib fragility (no retry/pooling) | Low | Med | Acceptable for CLI; upgrade to httpx if needed |
| WeCom removes/renames endpoints | Low | High | Generated methods are unstable across releases; deprecation workflow needed |
| Testing 309 generated endpoints | Med | Med | Codegen validated by unit tests (parameter wiring); runtime contracts verified via discovery pipeline diff report, not live API calls |

## Next Steps

1. **Error path hardening** — All exit codes return documented values; all error paths write to stderr with structured messages
2. **Output stabilization** — JSON output is valid and consistent for all 309 endpoints; errcode/errmsg passed through as-is
3. **User documentation** — README covers install, config, first command; spec format documented for contributors
4. **Agent skill ecosystem** — Provide example skill file showing how to wrap `wecom` CLI for Claude Code; let community build MCP/SDK wrappers
