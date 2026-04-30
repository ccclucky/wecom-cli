# Release Workflow Redesign

**Date:** 2026-04-30
**Status:** Approved
**Scope:** Release workflow, version management, release notes

## Problem

Current release flow is over-engineered for a solo Python CLI project:
- commitizen adds dependency and configuration overhead for simple version bumps
- CHANGELOG.md requires maintenance but provides no value over GitHub Releases
- Release workflow re-runs lint/type/test already covered by CI
- Tag format inconsistency (v0.1.0-alpha.1 vs v0.1.0a2)
- Immutable release errors from complex draft→publish two-step

## Design

### Version Format

SemVer + dash: `MAJOR.MINOR.PATCH-PRERELEASE.N`

```
0.1.0-alpha.1    → alpha (internal testing)
0.1.0-beta.1     → beta (public testing)
0.1.0-rc.1       → release candidate
0.1.0            → stable release
1.0.0            → major version
```

Tag format: `v` prefix → `v0.1.0-alpha.1`, `v0.1.0`

pip and setuptools recognize this format natively.

### Release Flow

**Daily development:**
```
git commit -m "feat: xxx"
git push
→ CI: lint + type check + test
```

**Release:**
```
1. Update version in pyproject.toml
2. git commit -m "bump: 0.1.0-alpha.1 → 0.1.0-alpha.2"
3. git tag v0.1.0-alpha.2
4. git push && git push --tags
→ CI triggers release workflow:
   - build wheel + sdist
   - publish to PyPI
   - create draft GitHub Release
5. Edit draft on GitHub, write Chinese release notes, publish
```

### CI Workflow

**release.yml** — triggered on `v*` tag push:
1. Checkout + setup Python
2. Install build deps
3. `python -m build`
4. Publish to PyPI via `pypa/gh-action-pypi-publish`
5. Create draft GitHub Release via `softprops/action-gh-release`

No lint, no type check, no test — CI workflow handles those on every push.

**ci.yml** — unchanged, runs on push/PR to main.

### Cleanup

- Remove `[tool.commitizen]` from pyproject.toml
- Remove `commitizen` from dev dependencies
- Delete CHANGELOG.md
- Rename release-alpha.yml → release.yml
- Simplify to single job (no separate build/publish stages needed)

### Release Notes

- Maintained manually on GitHub Releases page
- Written in Chinese
- No CHANGELOG.md file
- No auto-generation

### Tag Trigger

Single pattern `v*` matches all version tags. No distinction between alpha/stable in CI — build+publish is identical.
