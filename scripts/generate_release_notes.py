"""Generate structured release notes from conventional commits.

Replaces GitHub's ``generate_release_notes``, which mixes documentation and
CI chores into a single "What's Changed" list and credits the automation bot
as a new contributor. The output groups changes by type so a reader can tell
what actually affects the package.

Usage::

    python scripts/generate_release_notes.py \
        --tag v0.1.0a6 \
        --output release-notes.md

The previous tag is discovered automatically; pass ``--previous-tag`` to
override it (useful when re-running a release).
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

# Ordered: the first matching type wins.
SECTIONS: tuple[tuple[str, str], ...] = (
    ("feat", "Features"),
    ("fix", "Bug Fixes"),
    ("perf", "Performance"),
    ("refactor", "Refactoring"),
    ("docs", "Documentation"),
    ("build", "Build"),
    ("ci", "CI/CD"),
    ("test", "Tests"),
    ("chore", "Chores"),
)

OTHER_SECTION = "Other Changes"

CONVENTIONAL_RE = re.compile(
    r"^(?P<type>[a-zA-Z]+)(?:\((?P<scope>[^)]*)\))?(?P<breaking>!)?:\s*(?P<desc>.+)$"
)

# Commits that must never appear in the notes.
SKIP_PATTERNS = (
    re.compile(r"^chore\(release\):"),
    re.compile(r"\[skip release\]"),
)


def _run_git(*args: str) -> str:
    result = subprocess.run(["git", *args], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return ""
    return result.stdout


def _repo_slug() -> str:
    url = _run_git("remote", "get-url", "origin").strip()
    if not url:
        return ""
    match = re.search(r"github\.com[:/](?P<slug>[^/]+/[^/.]+)", url)
    return match.group("slug") if match else ""


def _last_tag(exclude: str | None = None) -> str:
    tags = _run_git("tag", "--sort=-creatordate", "--list", "v*").split()
    for tag in tags:
        if tag != exclude:
            return tag
    return ""


def _read_commits(rev_range: str) -> list[dict[str, str]]:
    raw = _run_git("log", "--no-merges", "--format=%s%x1f%b%x1e", rev_range)
    commits: list[dict[str, str]] = []
    for record in raw.split("\x1e"):
        record = record.strip("\n")
        if not record.strip():
            continue
        subject, _, body = record.partition("\x1f")
        subject = subject.strip()
        if not subject:
            continue
        if any(pattern.search(subject) for pattern in SKIP_PATTERNS):
            continue
        commits.append({"subject": subject, "body": body.strip()})
    return commits


def _classify(commit: dict[str, str]) -> tuple[str, str, bool]:
    """Return (section, description, is_breaking)."""
    subject = commit["subject"]
    body = commit["body"]
    match = CONVENTIONAL_RE.match(subject)

    if not match:
        return OTHER_SECTION, subject, "BREAKING CHANGE" in body.upper()

    change_type = match.group("type").lower()
    desc = match.group("desc").strip()
    scope = (match.group("scope") or "").strip()
    if scope:
        desc = f"**{scope}:** {desc}"

    breaking = bool(match.group("breaking")) or "BREAKING CHANGE" in body.upper()

    for prefix, section in SECTIONS:
        if change_type == prefix:
            return section, desc, breaking

    return OTHER_SECTION, desc, breaking


def _tag_exists(tag: str) -> bool:
    return bool(_run_git("rev-parse", "--verify", "--quiet", f"refs/tags/{tag}").strip())


def build_notes(tag: str, previous_tag: str) -> str:
    if previous_tag:
        rev_range = f"{previous_tag}..{tag}" if _tag_exists(tag) else f"{previous_tag}..HEAD"
    else:
        rev_range = tag if _tag_exists(tag) else "HEAD"
    commits = _read_commits(rev_range)

    grouped: dict[str, list[str]] = {}
    breaking: list[str] = []

    for commit in commits:
        section, desc, is_breaking = _classify(commit)
        grouped.setdefault(section, []).append(desc)
        if is_breaking:
            breaking.append(desc)

    order = [section for _, section in SECTIONS] + [OTHER_SECTION]

    lines: list[str] = []
    if breaking:
        lines.append("### Breaking Changes")
        lines.append("")
        lines.extend(f"- {item}" for item in dict.fromkeys(breaking))
        lines.append("")

    for section in order:
        items = grouped.get(section)
        if not items:
            continue
        lines.append(f"### {section}")
        lines.append("")
        lines.extend(f"- {item}" for item in dict.fromkeys(items))
        lines.append("")

    if not lines:
        lines.append("No notable changes in this release.")
        lines.append("")

    slug = _repo_slug()
    if slug:
        if previous_tag:
            compare = f"https://github.com/{slug}/compare/{previous_tag}...{tag}"
        else:
            compare = f"https://github.com/{slug}/releases/tag/{tag}"
        lines.append(f"**Full Changelog**: {compare}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def update_changelog(path: Path, version: str, notes: str, date: str) -> bool:
    """Insert a release entry under ``## [Unreleased]``.

    Returns False when the version is already present, so re-running a release
    does not duplicate the entry.
    """
    if not path.exists():
        print(f"Changelog not found at {path}; skipping.")
        return False

    text = path.read_text(encoding="utf-8")
    heading = f"## [{version}]"
    if heading in text:
        print(f"Changelog already contains {version}; skipping.")
        return False

    marker = "## [Unreleased]"
    if marker not in text:
        print(f"No '{marker}' section in {path}; skipping.")
        return False

    start = text.index(marker)
    following = text.find("\n## [", start + 1)
    insert_at = len(text) if following == -1 else following + 1

    entry = f"## [{version}] - {date}\n\n{notes.strip()}\n\n"
    updated = text[:insert_at] + entry + text[insert_at:]
    path.write_text(updated, encoding="utf-8")
    print(f"Changelog updated with {version}.")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate structured release notes")
    parser.add_argument("--tag", required=True, help="Tag being released, e.g. v0.1.0a6")
    parser.add_argument("--previous-tag", default=None, help="Previous tag; auto-detected when omitted")
    parser.add_argument("--output", type=Path, required=True, help="Where to write the markdown")
    parser.add_argument("--version", default=None, help="Version for the changelog heading; defaults to the tag")
    parser.add_argument("--update-changelog", type=Path, default=None, help="Path to CHANGELOG.md to prepend to")
    parser.add_argument("--date", default=None, help="Release date (YYYY-MM-DD); defaults to today")
    args = parser.parse_args()

    previous = args.previous_tag if args.previous_tag is not None else _last_tag(exclude=args.tag)
    notes = build_notes(args.tag, previous)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(notes, encoding="utf-8")
    print(notes)

    if args.update_changelog:
        from datetime import date as _date

        version = args.version or args.tag.lstrip("v")
        release_date = args.date or _date.today().isoformat()
        update_changelog(args.update_changelog, version, notes, release_date)

    return 0


if __name__ == "__main__":
    sys.exit(main())
