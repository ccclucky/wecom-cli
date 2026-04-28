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
import logging
import random
import re
import time
from collections import deque
from collections.abc import Iterable
from dataclasses import asdict, dataclass
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

ALLOWED_HOST = "developer.work.weixin.qq.com"
CAPTCHA_SIGNALS = ("TencentCaptcha", "captcha", "verify", "/security/verify")
CAPTCHA_HTML_MAX = 3000
CAPTCHA_CONSECUTIVE_LIMIT = 5


def _is_captcha_block(html: str) -> bool:
    if len(html) > CAPTCHA_HTML_MAX:
        return False
    return any(sig in html for sig in CAPTCHA_SIGNALS)
DOC_PATH_PREFIX = "https://developer.work.weixin.qq.com/document/path/"
_TREE_PREFIX_RE = re.compile(r"^[\s│├└─┬┴┌┐┘└]+")
ENDPOINT_RE = re.compile(r"/cgi-bin/[a-zA-Z0-9_./-]+")
METHOD_RE = re.compile(r"(?:请求方式|Request Method)\s*[:：]?\s*(GET|POST)", re.IGNORECASE)
REQUEST_URL_RE = re.compile(
    r"(?:请求地址|Request URL)\s*[:：]?\s*(https://qyapi\.weixin\.qq\.com/cgi-bin/[^\s<]+)",
    re.IGNORECASE,
)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)

logger = logging.getLogger("wecom-discovery")


def setup_logging(log_file: Path | None = None) -> None:
    """Setup logging to console and optionally to a file."""
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File handler
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(log_file, encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)


_INVALID_IDENT_RE = re.compile(r"[^\w]")
_PY_KEYWORDS = frozenset({
    "False", "None", "True", "and", "as", "assert", "async", "await",
    "break", "class", "continue", "def", "del", "elif", "else", "except",
    "finally", "for", "from", "global", "if", "import", "in", "is",
    "lambda", "nonlocal", "not", "or", "pass", "raise", "return",
    "try", "while", "with", "yield",
})


def _safe_ident(name: str) -> str:
    if name in _PY_KEYWORDS:
        return f"{name}_"
    return name


def _strip_tree_prefix(name: str) -> str:
    cleaned = _TREE_PREFIX_RE.sub("", name).strip()
    cleaned = _INVALID_IDENT_RE.sub("_", cleaned)
    cleaned = re.sub(r"_+", "_", cleaned).strip("_")
    return _safe_ident(cleaned)


def _normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _normalize_block_text(text: str) -> str:
    text = text.replace("\r", "")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _bool_from_required(value: str) -> bool | None:
    normalized = _normalize_whitespace(value).lower()
    if normalized in {"是", "必须", "true", "yes", "required"}:
        return True
    if normalized in {"否", "false", "no", "optional"}:
        return False
    return None


def _strip_title_suffix(text: str) -> str:
    title = _normalize_whitespace(unescape(text))
    suffixes = [
        " - 文档 - 企业微信开发者中心",
        " - 企业微信开发者中心",
    ]
    for suffix in suffixes:
        if title.endswith(suffix):
            return title[: -len(suffix)].strip()
    return title


@dataclass(frozen=True)
class DiscoveredField:
    name: str
    required: bool | None = None
    description: str | None = None
    type: str | None = None


@dataclass(frozen=True)
class DiscoveredOperation:
    endpoint: str
    method: str | None
    source_url: str
    title: str | None = None
    request_url: str | None = None
    request_params: tuple[DiscoveredField, ...] = ()
    response_params: tuple[DiscoveredField, ...] = ()
    request_example_text: str | None = None
    request_example_json: object | None = None
    response_example_text: str | None = None
    response_example_json: object | None = None
    permissions: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class CrawlFailure:
    url: str
    error: str


@dataclass(frozen=True)
class CrawlReport:
    operations: list[DiscoveredOperation]
    visited_pages: int
    failed_pages: int
    blocked_pages: int
    failures: list[CrawlFailure]


@dataclass
class DocBlock:
    kind: str
    text: str = ""
    headers: list[str] | None = None
    rows: list[list[str]] | None = None


class DocBlockParser(HTMLParser):
    TEXT_TAGS = {"p", "blockquote", "title", "h1", "h2", "h3", "h4", "h5", "h6"}

    def __init__(self) -> None:
        super().__init__()
        self.blocks: list[DocBlock] = []
        self._text_tag: str | None = None
        self._text_chunks: list[str] = []
        self._in_pre = False
        self._code_chunks: list[str] = []
        self._table_headers: list[str] = []
        self._table_rows: list[list[str]] = []
        self._current_row: list[str] = []
        self._current_row_has_header = False
        self._current_cell: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            return
        if tag in self.TEXT_TAGS and not self._in_pre and self._current_cell is None:
            self._start_text(tag)
        elif tag == "br":
            if self._text_tag is not None:
                self._text_chunks.append("\n")
            if self._in_pre:
                self._code_chunks.append("\n")
            if self._current_cell is not None:
                self._current_cell.append("\n")
        elif tag == "pre":
            self._in_pre = True
            self._code_chunks = []
        elif tag == "table":
            self._table_headers = []
            self._table_rows = []
        elif tag == "tr":
            self._current_row = []
            self._current_row_has_header = False
        elif tag in {"th", "td"}:
            self._current_cell = []
            if tag == "th":
                self._current_row_has_header = True

    def handle_endtag(self, tag: str) -> None:
        if tag == self._text_tag:
            self._flush_text(kind="blockquote" if tag == "blockquote" else "text")
        elif tag == "pre" and self._in_pre:
            code = _normalize_block_text("".join(self._code_chunks))
            if code:
                self.blocks.append(DocBlock(kind="code", text=code))
            self._in_pre = False
            self._code_chunks = []
        elif tag in {"th", "td"} and self._current_cell is not None:
            cell_text = _normalize_whitespace("".join(self._current_cell))
            self._current_row.append(cell_text)
            self._current_cell = None
        elif tag == "tr" and self._current_row:
            if self._current_row_has_header and not self._table_headers:
                self._table_headers = self._current_row
            else:
                self._table_rows.append(self._current_row)
            self._current_row = []
            self._current_row_has_header = False
        elif tag == "table":
            if self._table_headers or self._table_rows:
                self.blocks.append(
                    DocBlock(
                        kind="table",
                        headers=self._table_headers[:],
                        rows=[row[:] for row in self._table_rows],
                    )
                )
            self._table_headers = []
            self._table_rows = []

    def handle_data(self, data: str) -> None:
        if self._current_cell is not None:
            self._current_cell.append(data)
            return
        if self._in_pre:
            self._code_chunks.append(data)
            return
        if self._text_tag is not None:
            self._text_chunks.append(data)

    def _start_text(self, tag: str) -> None:
        if self._text_tag is not None:
            self._flush_text(kind="blockquote" if self._text_tag == "blockquote" else "text")
        self._text_tag = tag
        self._text_chunks = []

    def _flush_text(self, kind: str) -> None:
        text = _normalize_block_text("".join(self._text_chunks))
        if text:
            self.blocks.append(DocBlock(kind=kind, text=text))
        self._text_tag = None
        self._text_chunks = []


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
    menu_tree_file: Path | None,
) -> list[str]:
    seeds = list(explicit_seeds)

    if seed_file and seed_file.exists():
        for line in seed_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                seeds.append(line)

    if menu_tree_file and menu_tree_file.exists():
        try:
            import json
            tree_data = json.loads(menu_tree_file.read_text(encoding="utf-8"))
            for item in tree_data:
                if item.get("type") != 1:
                    continue
                if "id" in item:
                    seeds.append(f"{DOC_PATH_PREFIX}{item['id']}")
        except Exception as e:
            logger.warning(f"Failed to parse menu tree: {e}")

    if not seeds:
        seeds = [f"{DOC_PATH_PREFIX}90665"]

    # keep order + dedupe
    return list(dict.fromkeys(seeds))


def fetch_html(url: str, timeout: float = 15.0, cookie: str | None = None) -> str:
    headers: dict[str, str] = {
        "User-Agent": "wecom-cli-catalog-discovery/1.0",
        "Accept": "text/html,application/xhtml+xml",
    }
    if cookie:
        headers["Cookie"] = cookie
    req = Request(url, headers=headers)
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


def _extract_title(html: str) -> str | None:
    match = TITLE_RE.search(html)
    if not match:
        return None
    return _strip_title_suffix(match.group(1))


def _extract_request_basics(html: str) -> tuple[str | None, str | None]:
    plain_text = _normalize_whitespace(unescape(re.sub(r"<[^>]+>", " ", html)))
    method_match = METHOD_RE.search(plain_text)
    request_url_match = REQUEST_URL_RE.search(plain_text)
    method = method_match.group(1).upper() if method_match else None
    request_url = request_url_match.group(1) if request_url_match else None
    return method, request_url


def _parse_doc_blocks(html: str) -> list[DocBlock]:
    parser = DocBlockParser()
    parser.feed(html)
    return parser.blocks


def _heading_type(text: str) -> str | None:
    normalized = _normalize_whitespace(text).rstrip("：:")
    if normalized.startswith("参数说明"):
        return "params"
    if normalized.startswith("请求示例"):
        return "request_example"
    if normalized.startswith("返回示例") or normalized.startswith("返回结果"):
        return "response_example"
    if normalized.startswith("权限说明"):
        return "permissions"
    return None


def _table_to_fields(block: DocBlock) -> tuple[DiscoveredField, ...]:
    headers = block.headers or []
    rows = block.rows or []
    normalized_headers = [_normalize_whitespace(h) for h in headers]

    def _find_index(patterns: tuple[str, ...]) -> int | None:
        for index, header in enumerate(normalized_headers):
            if any(pattern in header for pattern in patterns):
                return index
        return None

    name_index = _find_index(("参数", "字段", "名称", "属性"))
    required_index = _find_index(("必须", "是否必须", "必填", "required"))
    description_index = _find_index(("说明", "描述", "含义"))
    type_index = _find_index(("类型", "type"))

    fields: list[DiscoveredField] = []
    for row in rows:
        if name_index is None or name_index >= len(row):
            continue
        name = _strip_tree_prefix(row[name_index])
        if not name:
            continue
        required = None
        if required_index is not None and required_index < len(row):
            required = _bool_from_required(row[required_index])
        description = row[description_index].strip() if description_index is not None and description_index < len(row) else None
        field_type = row[type_index].strip() if type_index is not None and type_index < len(row) else None
        fields.append(
            DiscoveredField(
                name=name,
                required=required,
                description=description or None,
                type=field_type or None,
            )
        )
    return tuple(fields)


def _parse_json_example(text: str) -> object | None:
    text = text.strip()
    if not text:
        return None
    start = min((idx for idx in (text.find("{"), text.find("[")) if idx != -1), default=-1)
    if start == -1:
        return None
    candidate = text[start:]
    end_object = candidate.rfind("}")
    end_array = candidate.rfind("]")
    end = max(end_object, end_array)
    if end == -1:
        return None
    candidate = candidate[: end + 1]
    try:
        return json.loads(candidate)
    except json.JSONDecodeError:
        return None


def _extract_doc_details(
    html: str,
) -> tuple[
    tuple[DiscoveredField, ...],
    tuple[DiscoveredField, ...],
    str | None,
    object | None,
    str | None,
    object | None,
    tuple[str, ...],
    tuple[str, ...],
]:
    blocks = _parse_doc_blocks(html)
    request_params: tuple[DiscoveredField, ...] = ()
    response_params: tuple[DiscoveredField, ...] = ()
    request_example_text: str | None = None
    response_example_text: str | None = None
    permissions: list[str] = []
    notes: list[str] = []
    active_section: str | None = None
    response_seen = False

    for block in blocks:
        if block.kind == "text":
            heading = _heading_type(block.text)
            if heading == "params":
                active_section = "response_params" if response_seen and response_example_text else "request_params"
                continue
            if heading == "request_example":
                active_section = "request_example"
                continue
            if heading == "response_example":
                active_section = "response_example"
                response_seen = True
                continue
            if heading == "permissions":
                active_section = "permissions"
                continue
            if active_section == "permissions":
                permissions.append(block.text)
            continue

        if block.kind == "blockquote":
            notes.append(block.text)
            continue

        if block.kind == "table":
            if active_section == "request_params" and not request_params:
                request_params = _table_to_fields(block)
            elif active_section == "response_params" and not response_params:
                response_params = _table_to_fields(block)
            continue

        if block.kind == "code":
            if active_section == "request_example" and request_example_text is None:
                request_example_text = block.text
            elif active_section == "response_example" and response_example_text is None:
                response_example_text = block.text
            elif response_seen and response_example_text is None:
                response_example_text = block.text
            elif not response_seen and request_example_text is None:
                request_example_text = block.text

    return (
        request_params,
        response_params,
        request_example_text,
        _parse_json_example(request_example_text) if request_example_text else None,
        response_example_text,
        _parse_json_example(response_example_text) if response_example_text else None,
        tuple(permissions),
        tuple(notes),
    )


def extract_operations(source_url: str, html: str) -> list[DiscoveredOperation]:
    title = _extract_title(html)
    method, request_url = _extract_request_basics(html)
    (
        request_params,
        response_params,
        request_example_text,
        request_example_json,
        response_example_text,
        response_example_json,
        permissions,
        notes,
    ) = _extract_doc_details(html)

    endpoints: list[str] = []
    if request_url:
        parsed = urlparse(request_url)
        if parsed.path.startswith("/cgi-bin/"):
            endpoints.append(parsed.path)
    if not endpoints:
        if not any((method, request_params, response_params, request_example_text, response_example_text)):
            return []
        endpoints = sorted(set(ENDPOINT_RE.findall(html)))

    return [
        DiscoveredOperation(
            endpoint=endpoint,
            method=method,
            source_url=source_url,
            title=title,
            request_url=request_url,
            request_params=request_params,
            response_params=response_params,
            request_example_text=request_example_text,
            request_example_json=request_example_json,
            response_example_text=response_example_text,
            response_example_json=response_example_json,
            permissions=permissions,
            notes=notes,
        )
        for endpoint in endpoints
    ]


def _load_empty_pages(path: Path | None) -> set[str]:
    if not path or not path.exists():
        return set()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return set(data)
    except Exception as e:
        logger.warning(f"Failed to load empty pages cache: {e}")
    return set()


def _save_empty_pages(path: Path | None, empty_set: set[str]) -> None:
    if not path:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(sorted(empty_set), ensure_ascii=False, indent=2), encoding="utf-8")


def crawl(
    seed_urls: Iterable[str],
    max_pages: int,
    seed_only: bool = False,
    delay_min: float = 1.0,
    delay_max: float = 3.0,
    empty_pages_file: Path | None = None,
    cookie: str | None = None,
) -> CrawlReport:
    seeds = list(seed_urls)
    seed_set: set[str] = set(seeds)
    q: deque[str] = deque(seeds)
    seen: set[str] = set()
    discovered: dict[tuple[str, str | None], DiscoveredOperation] = {}
    failures: list[CrawlFailure] = []
    new_empty: set[str] = set()

    known_empty = _load_empty_pages(empty_pages_file)
    skipped_empty = 0
    blocked_count = 0
    consecutive_blocks = 0

    total_expected = min(len(seeds), max_pages) if seed_only else max_pages
    logger.info(
        f"Starting crawl: {len(seeds)} seeds, max_pages={max_pages}, "
        f"seed_only={seed_only}, cached_empty={len(known_empty)}"
    )

    while q and len(seen) < max_pages:
        url = q.popleft()
        if url in seen:
            continue

        if url in known_empty:
            logger.debug(f"Skipping cached-empty: {url}")
            seen.add(url)
            skipped_empty += 1
            continue

        seen.add(url)

        curr_idx = len(seen) + skipped_empty
        percent = (curr_idx / total_expected) * 100 if total_expected > 0 else 0
        progress_prefix = f"[{curr_idx}/{total_expected}] {percent:5.1f}%"

        logger.debug(f"Fetching: {url}")
        time.sleep(random.uniform(delay_min, delay_max))
        try:
            html = fetch_html(url, cookie=cookie)
        except Exception as exc:
            logger.error(f"{progress_prefix} | FAILED | {url} | Error: {exc}")
            failures.append(CrawlFailure(url=url, error=str(exc)))
            consecutive_blocks = 0
            continue

        if _is_captcha_block(html):
            blocked_count += 1
            consecutive_blocks += 1
            logger.warning(
                f"{progress_prefix} | BLOCKED  | Anti-bot page ({len(html)} bytes)"
                + (f" | {consecutive_blocks} consecutive — will abort at {CAPTCHA_CONSECUTIVE_LIMIT}"
                   if consecutive_blocks >= CAPTCHA_CONSECUTIVE_LIMIT - 2 else "")
            )
            if consecutive_blocks >= CAPTCHA_CONSECUTIVE_LIMIT:
                logger.error(
                    f"Aborting: {consecutive_blocks} consecutive CAPTCHA blocks. "
                    "Server is rate-limiting. Increase --delay-min/--delay-max or wait and retry."
                )
                break
            continue

        consecutive_blocks = 0

        ops = extract_operations(url, html)
        if ops:
            for op in ops:
                key = (op.endpoint, op.method)
                discovered[key] = op
            op_names = ", ".join(f"{op.method or '??'} {op.endpoint}" for op in ops)
            logger.info(f"{progress_prefix} | FOUND {len(ops):2d} | {op_names}")
        else:
            logger.info(f"{progress_prefix} | EMPTY    | No API found on page")
            new_empty.add(url)

        if not seed_only:
            for child in extract_links(url, html):
                if child not in seen:
                    q.append(child)
        else:
            for child in extract_links(url, html):
                if child in seed_set and child not in seen:
                    q.append(child)

    if new_empty and empty_pages_file:
        merged = known_empty | new_empty
        _save_empty_pages(empty_pages_file, merged)
        logger.info(f"Cached {len(new_empty)} new empty pages ({len(merged)} total)")

    if blocked_count:
        logger.warning(f"Crawl blocked {blocked_count} times by anti-bot protection")

    return CrawlReport(
        operations=sorted(discovered.values(), key=lambda x: (x.endpoint, x.method or "")),
        visited_pages=len(seen),
        failed_pages=len(failures),
        blocked_pages=blocked_count,
        failures=failures,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Discover WeCom APIs from doc pages")
    parser.add_argument("--seed", action="append", default=[], help="Seed doc URLs")
    parser.add_argument("--seed-file", type=Path, help="File containing seed URLs, one per line")
    parser.add_argument("--menu-tree-file", type=Path, default=Path("specs/wecom/menu_tree.json"), help="Menu tree JSON file")
    parser.add_argument("--max-pages", type=int, default=300)
    parser.add_argument("--delay-min", type=float, default=1.0,
                        help="Minimum delay between page fetches in seconds")
    parser.add_argument("--delay-max", type=float, default=3.0,
                        help="Maximum delay between page fetches in seconds")
    parser.add_argument("--output", type=Path, default=Path("artifacts/catalog.discovery.yaml"))
    parser.add_argument("--log-file", type=Path, default=Path("artifacts/discovery.log"), help="Path to log file")
    parser.add_argument("--empty-pages-file", type=Path, default=Path("specs/wecom/empty_pages.json"),
                        help="Cache file for known-empty pages (skips on re-crawl)")
    parser.add_argument("--cookie", default=None,
                        help="Cookie header to send with each request (bypasses CAPTCHA)")
    args = parser.parse_args()

    setup_logging(args.log_file)

    seeds = build_seed_urls(
        explicit_seeds=list(args.seed),
        seed_file=args.seed_file,
        menu_tree_file=args.menu_tree_file,
    )

    start_time = time.time()
    # When using menu_tree_file, the seeds already cover all known pages.
    # Disable free link-following to avoid unbounded crawl expansion.
    seed_only = args.menu_tree_file is not None and args.menu_tree_file.exists()
    crawl_report = crawl(
        seeds, args.max_pages,
        seed_only=seed_only,
        delay_min=args.delay_min,
        delay_max=args.delay_max,
        empty_pages_file=args.empty_pages_file,
        cookie=args.cookie,
    )
    duration = time.time() - start_time

    payload = {
        "snapshot_date": "2026-04-23",
        "source": ALLOWED_HOST,
        "seed_urls": seeds,
        "crawl": {
            "visited_pages": crawl_report.visited_pages,
            "failed_pages": crawl_report.failed_pages,
            "blocked_pages": crawl_report.blocked_pages,
            "failures": [asdict(item) for item in crawl_report.failures],
            "duration_seconds": round(duration, 2),
        },
        "operations": [asdict(op) for op in crawl_report.operations],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    
    logger.info("-" * 40)
    logger.info(f"Discovery completed in {duration/60:.1f} minutes")
    logger.info(
        "Summary: "
        f"{len(crawl_report.operations)} operations found "
        f"(visited={crawl_report.visited_pages}, failed={crawl_report.failed_pages}, "
        f"blocked={crawl_report.blocked_pages}) "
    )
    logger.info(f"Output saved to: {args.output}")
    if args.log_file:
        logger.info(f"Full logs available at: {args.log_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
