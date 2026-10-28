"""Bump the package version and emit the matching release tag.

Used by the auto-release workflow. The script decides whether a release is
warranted at all: commits that only touch documentation, CI configuration or
the helper scripts under ``scripts/`` do not change the distributed package,
so they must not consume a version number.

Version scheme
--------------
PEP 440 is the single source of truth. The Git tag is that exact version with
a ``v`` prefix, so the three places that carry a version never diverge::

    pyproject.toml   tag           PyPI
    0.1.0a5          v0.1.0a5      0.1.0a5     alpha
    0.1.0b1          v0.1.0b1      0.1.0b1     beta
    0.1.0rc1         v0.1.0rc1     0.1.0rc1    release candidate
    0.1.0            v0.1.0        0.1.0       stable

The legacy ``0.1.0-alpha.5`` form is still accepted on input and normalised to
``0.1.0a5`` so the repository can migrate without a manual edit.

Bump transitions
----------------
=========  ================  ==============================
current    --bump            result
=========  ================  ==============================
0.1.0a5    alpha (default)   0.1.0a6
0.1.0a5    beta              0.1.0b1
0.1.0b2    rc                0.1.0rc1
0.1.0rc1   stable            0.1.0
0.1.0      patch (default)   0.1.1
0.1.0      minor             0.2.0
0.1.0      major             1.0.0
=========  ================  ==============================
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

PYPROJECT = Path("pyproject.toml")

# Matches both the canonical PEP 440 spelling and the legacy hyphenated form.
VERSION_RE = re.compile(
    r"^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)"
    r"(?:(?:-?)(?P<stage>alpha|a|beta|b|rc|rc)\.?(?P<num>\d+))?$"
)

STAGE_ALIASES = {
    "alpha": "alpha",
    "a": "alpha",
    "beta": "beta",
    "b": "beta",
    "rc": "rc",
}

STAGE_SUFFIX = {"alpha": "a", "beta": "b", "rc": "rc"}

# Paths whose contents actually ship inside the wheel. A commit that touches
# none of these does not justify a new release.
RELEASE_PATHS = ("core/", "cli/", "apis/", "models/", "pyproject.toml")

BUMP_KINDS = ("auto", "alpha", "beta", "rc", "stable", "patch", "minor", "major")


class Version:
    __slots__ = ("major", "minor", "patch", "stage", "num")

    def __init__(self, major: int, minor: int, patch: int, stage: str | None, num: int) -> None:
        self.major = major
        self.minor = minor
        self.patch = patch
        self.stage = stage
        self.num = num

    @property
    def is_prerelease(self) -> bool:
        return self.stage is not None

    def __str__(self) -> str:
        base = f"{self.major}.{self.minor}.{self.patch}"
        if self.stage is None:
            return base
        return f"{base}{STAGE_SUFFIX[self.stage]}{self.num}"


def parse_version(raw: str) -> Version:
    match = VERSION_RE.match(raw.strip())
    if not match:
        raise SystemExit(f"Unsupported version format: {raw}")

    stage_raw = match.group("stage")
    stage = STAGE_ALIASES[stage_raw] if stage_raw else None
    num = int(match.group("num")) if match.group("num") else 0
    return Version(
        major=int(match.group("major")),
        minor=int(match.group("minor")),
        patch=int(match.group("patch")),
        stage=stage,
        num=num,
    )


def bump(current: Version, kind: str) -> Version:
    major, minor, patch = current.major, current.minor, current.patch

    if kind == "auto":
        # Stay in the current channel; a stable release advances the patch.
        kind = current.stage if current.stage else "patch"

    if kind == "alpha":
        if current.stage == "alpha":
            return Version(major, minor, patch, "alpha", current.num + 1)
        if current.stage is None:
            return Version(major, minor, patch + 1, "alpha", 1)
        raise SystemExit(f"Cannot start alpha from {current}")

    if kind == "beta":
        if current.stage == "beta":
            return Version(major, minor, patch, "beta", current.num + 1)
        if current.stage in ("alpha", None):
            return Version(major, minor, patch, "beta", 1)
        raise SystemExit(f"Cannot start beta from {current}")

    if kind == "rc":
        if current.stage == "rc":
            return Version(major, minor, patch, "rc", current.num + 1)
        if current.stage in ("alpha", "beta", None):
            return Version(major, minor, patch, "rc", 1)
        raise SystemExit(f"Cannot start rc from {current}")

    if kind == "stable":
        if current.stage is not None:
            return Version(major, minor, patch, None, 0)
        return Version(major, minor, patch + 1, None, 0)

    if kind == "patch":
        return Version(major, minor, patch + 1, None, 0)

    if kind == "minor":
        return Version(major, minor + 1, 0, None, 0)

    if kind == "major":
        return Version(major + 1, 0, 0, None, 0)

    raise SystemExit(f"Unknown bump kind: {kind}")


def _run_git(*args: str) -> str:
    result = subprocess.run(["git", *args], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return ""
    return result.stdout.strip()


def _read_version() -> str:
    text = PYPROJECT.read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, re.MULTILINE)
    if not match:
        raise SystemExit("Could not find a version field in pyproject.toml")
    return match.group(1)


def _write_version(new_version: str) -> None:
    text = PYPROJECT.read_text(encoding="utf-8")
    updated, count = re.subn(
        r'^version\s*=\s*"[^"]+"',
        f'version = "{new_version}"',
        text,
        count=1,
        flags=re.MULTILINE,
    )
    if count != 1:
        raise SystemExit("Failed to rewrite the version field in pyproject.toml")
    PYPROJECT.write_text(updated, encoding="utf-8")


def _changed_files_since_last_tag() -> list[str]:
    last_tag = _run_git("describe", "--tags", "--abbrev=0", "--match", "v*")
    if not last_tag:
        return _run_git("ls-files").splitlines()
    output = _run_git("diff", "--name-only", f"{last_tag}..HEAD")
    return [line for line in output.splitlines() if line.strip()]


def needs_release(changed: list[str]) -> bool:
    return any(path.startswith(RELEASE_PATHS) for path in changed)


def _emit(key: str, value: str) -> None:
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a", encoding="utf-8") as handle:
            handle.write(f"{key}={value}\n")
    print(f"{key}={value}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Bump version and emit release tag")
    parser.add_argument(
        "--bump",
        choices=BUMP_KINDS,
        default="auto",
        help="Which part to advance. 'auto' keeps the current channel and increments it.",
    )
    parser.add_argument("--force", action="store_true", help="Release even when no shippable paths changed")
    parser.add_argument("--dry-run", action="store_true", help="Print the decision without writing pyproject.toml")
    args = parser.parse_args()

    changed = _changed_files_since_last_tag()
    release = args.force or needs_release(changed)

    if not release:
        print("No shippable paths changed since the last tag; skipping release.")
        _emit("should_release", "false")
        return 0

    current_raw = _read_version()
    current = parse_version(current_raw)
    next_version = bump(current, args.bump)

    tag = f"v{next_version}"
    prerelease = "true" if next_version.is_prerelease else "false"

    print(f"Version: {current_raw} -> {next_version}")
    print(f"Channel: {next_version.stage or 'stable'}")
    print(f"Tag: {tag}")
    print("Changed shippable files:")
    for path in changed:
        if path.startswith(RELEASE_PATHS):
            print(f"  - {path}")

    if not args.dry_run:
        _write_version(str(next_version))

    _emit("should_release", "true")
    _emit("version", str(next_version))
    _emit("previous_version", current_raw)
    _emit("tag", tag)
    _emit("prerelease", prerelease)
    _emit("channel", next_version.stage or "stable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
