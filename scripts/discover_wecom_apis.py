"""Discover WeCom API endpoints from documentation pages.

Usage:
  python scripts/discover_wecom_apis.py \
    --seed-file specs/wecom/seeds.txt \
    --doc-id-from 90000 \
    --doc-id-to 100200 \
    --max-pages 400 \
    --output specs/wecom/catalog.discovery.yaml
"""

from __future__ import annotations

import argparse
import json
import re
from collections import deque
from collections.abc import Iterable
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

ALLOWED_HOST = "developer.work.weixin.qq.com"
DOC_PATH_PREFIX = "https://developer.work.weixin.qq.com/document/path/"
ENDPOINT_RE = re.compile(r"/cgi-bin/[a-zA-Z0-9_./-]+")
METHOD_RE = re.compile(r"(?:请求方式|Request Method)\s*[:：]?\s*(GET|POST)", re.IGNORECASE)


@dataclass(frozen=True)
class DiscoveredOperation:
    endpoint: str
    method: str | None
    source_url: str


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        for key, value in attrs:
            if key == "href" and value:
                self.links.append(value)


def build_seed_urls(
    explicit_seeds: list[str],
    seed_file: Path | None,
    doc_id_from: int | None,
    doc_id_to: int | None,
) -> list[str]:
    seeds = list(explicit_seeds)

    if seed_file and seed_file.exists():
        for line in seed_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                seeds.append(line)

    if doc_id_from is not None and doc_id_to is not None and doc_id_to >= doc_id_from:
        for doc_id in range(doc_id_from, doc_id_to + 1):
            seeds.append(f"{DOC_PATH_PREFIX}{doc_id}")

    if not seeds:
        seeds = [f"{DOC_PATH_PREFIX}90665"]

    # keep order + dedupe
    return list(dict.fromkeys(seeds))


def fetch_html(url: str, timeout: float = 15.0) -> str:
    req = Request(
        url,
        headers={
            "User-Agent": "wecom-cli-catalog-discovery/1.0",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    with urlopen(req, timeout=timeout) as resp:  # nosec B310 - fixed allowed host via crawl filter
        return resp.read().decode("utf-8", errors="ignore")


def extract_links(base_url: str, html: str) -> list[str]:
    parser = LinkParser()
    parser.feed(html)
    out: list[str] = []
    for href in parser.links:
        resolved = urljoin(base_url, href)
        parsed = urlparse(resolved)
        if parsed.netloc != ALLOWED_HOST:
            continue
        if "/document/path/" not in parsed.path:
            continue
        out.append(resolved)
    return out


def extract_operations(source_url: str, html: str) -> list[DiscoveredOperation]:
    methods = [m.upper() for m in METHOD_RE.findall(html)]
    method = methods[0] if methods else None
    endpoints = sorted(set(ENDPOINT_RE.findall(html)))
    return [
        DiscoveredOperation(endpoint=e, method=method, source_url=source_url)
        for e in endpoints
    ]


def crawl(seed_urls: Iterable[str], max_pages: int) -> list[DiscoveredOperation]:
    q: deque[str] = deque(seed_urls)
    seen: set[str] = set()
    discovered: dict[tuple[str, str | None], DiscoveredOperation] = {}

    while q and len(seen) < max_pages:
        url = q.popleft()
        if url in seen:
            continue
        seen.add(url)
        try:
            html = fetch_html(url)
        except Exception:
            continue

        for op in extract_operations(url, html):
            key = (op.endpoint, op.method)
            discovered[key] = op

        for child in extract_links(url, html):
            if child not in seen:
                q.append(child)

    return sorted(discovered.values(), key=lambda x: (x.endpoint, x.method or ""))


def main() -> int:
    parser = argparse.ArgumentParser(description="Discover WeCom APIs from doc pages")
    parser.add_argument("--seed", action="append", default=[], help="Seed doc URLs")
    parser.add_argument("--seed-file", type=Path, help="File containing seed URLs, one per line")
    parser.add_argument("--doc-id-from", type=int, help="Optional doc id range start")
    parser.add_argument("--doc-id-to", type=int, help="Optional doc id range end")
    parser.add_argument("--max-pages", type=int, default=300)
    parser.add_argument("--output", type=Path, default=Path("specs/wecom/catalog.discovery.yaml"))
    args = parser.parse_args()

    seeds = build_seed_urls(
        explicit_seeds=list(args.seed),
        seed_file=args.seed_file,
        doc_id_from=args.doc_id_from,
        doc_id_to=args.doc_id_to,
    )

    operations = crawl(seeds, args.max_pages)
    payload = {
        "snapshot_date": "2026-04-23",
        "source": ALLOWED_HOST,
        "seed_urls": seeds,
        "operations": [asdict(op) for op in operations],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"discovered operations: {len(operations)} -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
