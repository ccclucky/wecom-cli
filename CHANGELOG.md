# Changelog

## 0.1.0a3 (2026-04-30)

### Feat

- Add commitizen for version management and fix release workflow
- Fix release workflow: draft→publish pattern for immutable releases
- Create initial CHANGELOG.md
- Fix copyright holder name in LICENSE

## 0.1.0a2 (2026-04-30)

### Feat

- Add GitHub Actions workflow to automate alpha releases to PyPI
- Add GitHub Actions workflow for automated alpha releases

## 0.1.0-alpha.1 (2026-04-30)

### Feat

- Configure automated CLAUDE.local.md context and update project guidelines
- Add UnifiedRequester for API calls and configure local project settings
- Implement CLI command generation and routing infrastructure with test suite
- Implement code generation scripts and core infrastructure for WeCom API client and CLI
- Improve help output with domain listing and Chinese descriptions
- Implement initial CLI entry point and development environment configuration
- Add automated WeCom API discovery, catalog synchronization, and scaffolding tools
- Auto-generate POST request contracts from doc metadata
- Add WeCom school domain API specs and generate CLI commands and client code
- Bootstrap wecom CLI core domains and CI pipelines

### Fix

- Explicit package discovery for setuptools build
- Resolve mypy type error in route() function
- Use parse_known_args in main() first pass + add 4 CLI integration tests
- Harden core infra — retry, error handling, bootstrap delay, verbose/debug
- Harden codegen pipeline — type mapping, dest collision, body mode, spec validation
- Prevent catalog shrinkage in reconciler and relax coverage exit code

### Refactor

- Clean up unused imports and update timeout exception handling

### Perf

- Add seed_only mode to crawl() to prevent link-following explosion
