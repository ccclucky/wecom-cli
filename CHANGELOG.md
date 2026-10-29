# Changelog

All notable changes to this project are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versions follow [PEP 440](https://peps.python.org/pep-0440/): the same string
appears in `pyproject.toml`, in the Git tag (prefixed with `v`) and on PyPI.

| Stage | `pyproject.toml` | Git tag | PyPI |
| --- | --- | --- | --- |
| Alpha | `0.1.0a6` | `v0.1.0a6` | `0.1.0a6` |
| Beta | `0.1.0b1` | `v0.1.0b1` | `0.1.0b1` |
| Release candidate | `0.1.0rc1` | `v0.1.0rc1` | `0.1.0rc1` |
| Stable | `0.1.0` | `v0.1.0` | `0.1.0` |

Releases are cut from `main` by the **Auto Release** workflow. Entries below
`Unreleased` are generated from conventional commits and appended automatically.

> Tags `v0.1.0-alpha.1`, `v0.1.0a2`, `v0.1.0a3` and `v0.1.0-alpha.4` predate this
> convention and mix two spellings. They are left untouched because they are
> already published; every tag from `v0.1.0a6` onward is PEP 440 only.

## [Unreleased]

## [0.1.0a7] - 2026-10-29

### Features

- **catalog:** sync discovered WeCom API catalog (#20)
- **ci:** open a tracking issue when the doc cookie goes stale
- **ci:** add cookie health probe and self-report in watch run

### Bug Fixes

- **catalog:** report the sweep pause without naming a specific budget
- **catalog:** bound the sweep by wall clock, not request count
- **catalog:** make the catalog sweep resumable across runs

### Documentation

- correct the PEP 440 cut-over tag in CHANGELOG

**Full Changelog**: https://github.com/ccclucky/wecom-cli/compare/v0.1.0a6...v0.1.0a7

## [0.1.0a6] - 2026-10-28

### Bug Fixes

- **release:** filter legacy version bump commits from release notes

**Full Changelog**: https://github.com/ccclucky/wecom-cli/compare/v0.1.0-alpha.5...v0.1.0a6

## [0.1.0a5] - 2026-10-28

### Added

- Automated catalog sync that merges discovered WeCom API changes to `main`
- Coverage gate that blocks a diff when the crawl re-covers less than 90% of the baseline
- Structured release notes grouped by conventional-commit type

### Fixed

- Catalog crawler no longer exits successfully when anti-bot protection aborts the run
- Diff report no longer reports false removals from an incomplete snapshot
- Sync pull requests are merged automatically instead of accumulating as drafts

### Changed

- Version strings use PEP 440 (`0.1.0a5` rather than `0.1.0-alpha.5`)

## [0.1.0-alpha.4] - 2026-04-30

### Changed

- Simplified the release workflow: removed commitizen, adopted SemVer with a dash separator

## [0.1.0a3] - 2026-04-30

### Changed

- Version bump only

## [0.1.0a2] - 2026-04-30

### Added

- GitHub Actions workflow to automate alpha releases to PyPI

## [0.1.0a1] - 2026-04-30

### Added

- Initial public alpha: core client, CLI entry point, API specs and codegen

### Fixed

- Explicit package discovery for the setuptools build
