"""Bump the package version and emit the matching release tag.

Used by the auto-release workflow. The script decides whether a release is
warranted at all: commits that only touch documentation, CI configuration or
the helper scripts under ``scripts/`` do not change the distributed package,
so they must not consume a version number.

Version schemes supported:

* ``X.Y.Z-alpha.N`` -> ``X.Y.Z-alpha.N+1`` (tag ``vX.Y.Z-alpha.N+1``)
* ``X.Y.Z``         -> ``X.Y.(Z+1)``         (tag ``vX.Y.(Z+1)``)

PEP 440 normalises ``0.1.0-alpha.4`` to ``0.1.0a4``, so the tag naming and the
published version stay consistent with what PyPI already hosts.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

PYPROJECT = Path("pyproject.toml")

ALPHA_RE = re.compile(r"^(?P<base>\d+\.\d+\.\d+)-alpha\.(?P<num>\d+)$")
STABLE_RE = re.compile(r"^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)$")

# Paths whose contents actually ship inside the wheel. A commit that touches
# none of these does not justify a new release.
RELEASE_PATHS = ("core/", "cli/", "apis/", "models/", "pyproject.toml")


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


def bump(version: str) -> tuple[str, str]:
    """Return (new_version, tag) for the given current version."""
    alpha = ALPHA_RE.match(version)
    if alpha:
        base = alpha.group("base")
        num = int(alpha.group("num")) + 1
        new_version = f"{base}-alpha.{num}"
        return new_version, f"v{new_version}"

    stable = STABLE_RE.match(version)
    if stable:
        major = stable.group("major")
        minor = stable.group("minor")
        patch = int(stable.group("patch")) + 1
        new_version = f"{major}.{minor}.{patch}"
        return new_version, f"v{new_version}"

    raise SystemExit(f"Unsupported version format: {version}")


def _changed_files_since_last_tag() -> list[str]:
    last_tag = _run_git("describe", "--tags", "--abbrev=0", "--match", "v*")
    if not last_tag:
        # No tags at all: treat every tracked file as changed.
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
    parser.add_argument("--force", action="store_true", help="Release even when no shippable paths changed")
    parser.add_argument("--dry-run", action="store_true", help="Print the decision without writing pyproject.toml")
    args = parser.parse_args()

    changed = _changed_files_since_last_tag()
    release = args.force or needs_release(changed)

    if not release:
        print("No shippable paths changed since the last tag; skipping release.")
        _emit("should_release", "false")
        return 0

    current = _read_version()
    new_version, tag = bump(current)

    print(f"Version: {current} -> {new_version}")
    print(f"Tag: {tag}")
    print("Changed shippable files:")
    for path in changed:
        if path.startswith(RELEASE_PATHS):
            print(f"  - {path}")

    if not args.dry_run:
        _write_version(new_version)

    _emit("should_release", "true")
    _emit("version", new_version)
    _emit("previous_version", current)
    _emit("tag", tag)
    return 0


if __name__ == "__main__":
    sys.exit(main())
