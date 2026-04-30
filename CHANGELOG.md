# Changelog

## 0.1.0a1 (2026-04-30)

Initial alpha release.

## v0.1.0a2 (2026-04-30)

### Feat

- add commitizen for version management and fix release workflow

## v0.1.0a2 (2026-04-30)

### Feat

- add GitHub Actions workflow to automate alpha releases to PyPI
- add GitHub Actions workflow for automated alpha releases

## v0.1.0-alpha.1 (2026-04-30)

### Feat

- configure automated CLAUDE.local.md context and update project guidelines with standard behavioral rules
- add UnifiedRequester for API calls and configure local project settings for graphify integration
- implement CLI command generation and routing infrastructure with comprehensive test suite
- implement code generation scripts and core infrastructure for WeCom API client and CLI
- improve help output with domain listing and Chinese descriptions
- implement initial CLI entry point and development environment configuration
- harden discovery pipeline with seed filtering, empty-page cache, CAPTCHA detection, and cookie support
- add automated WeCom API discovery, catalog synchronization, and scaffolding tools
- auto-generate POST request contracts from doc metadata
- add scripts to validate API coverage, generate client code, and discover WeCom endpoints
- add WeCom API discovery and automated catalog synchronization tooling
- add WeCom catalog synchronization orchestrator script and GitHub automated watch workflow
- update code graph cache and report with new test coverage analysis data
- add script to discover and catalog WeCom API endpoints from documentation pages
- implement WeCom API discovery tool and configure Claude project environment for graph-enhanced context
- add WeCom school domain API specifications and generate corresponding CLI commands and client code
- sync wecom specs and close agent workflow loop
- Enhance catalog synchronization and scaffolding
- add scaffolding step to turn catalog changes into spec/code updates
- clarify sync flow and support doc id range seeding
- support multi-seed discovery and baseline auto-reconcile
- add daily catalog watch workflow with diff reporting
- add doc crawler script for api catalog discovery
- add api catalog coverage gate for 100 percent tracking
- add spec-driven api/cli codegen workflow
- bootstrap wecom cli core domains and ci pipelines

### Fix

- explicit package discovery for setuptools build
- resolve mypy type error in route() function
- use parse_known_args in main() first pass + add 4 CLI integration tests
- harden core infra — retry, error handling, bootstrap delay, verbose/debug
- harden codegen pipeline — type mapping, dest collision, body mode, spec validation
- prevent catalog shrinkage in reconciler and relax coverage exit code
- align discovery pipeline and fix CI (lint/type/test)
- keep scaffold domains aligned with catalog operation ids
- prune removed catalog ops during scaffold auto-apply

### Refactor

- clean up unused imports and update timeout exception handling in discovery tests
- increase sleep interval to prevent HTTP 429 errors during API discovery

### Perf

- add seed_only mode to crawl() to prevent link-following explosion
