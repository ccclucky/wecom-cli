from __future__ import annotations

from unittest.mock import patch

from scripts.discover_wecom_apis import (
    CAPTCHA_CONSECUTIVE_LIMIT,
    CrawlFailure,
    _is_captcha_block,
    _load_empty_pages,
    _save_empty_pages,
    _strip_tree_prefix,
    build_seed_urls,
    crawl,
    extract_links,
    extract_operations,
    fetch_html,
)


def test_extract_operations_from_html():
    html = """
    <html>
      <head><title>发送消息 - 文档 - 企业微信开发者中心</title></head>
      <body>
        <p><strong>请求方式：</strong>POST（<strong>HTTPS</strong>）<br><strong>请求地址：</strong>https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=ACCESS_TOKEN</p>
        <p><strong>参数说明：</strong></p>
        <table>
          <thead><tr><th>参数</th><th>是否必须</th><th>说明</th></tr></thead>
          <tbody>
            <tr><td>access_token</td><td>是</td><td>调用接口凭证</td></tr>
            <tr><td>touser</td><td>否</td><td>接收成员</td></tr>
          </tbody>
        </table>
        <p><strong>请求示例：</strong></p>
        <pre>{
  "touser": "zhangsan",
  "msgtype": "text"
}</pre>
        <p><strong>返回结果：</strong></p>
        <pre>{
  "errcode": 0,
  "errmsg": "ok"
}</pre>
        <p><strong>参数说明：</strong></p>
        <table>
          <thead><tr><th>参数</th><th>说明</th></tr></thead>
          <tbody>
            <tr><td>errcode</td><td>返回码</td></tr>
            <tr><td>errmsg</td><td>返回信息</td></tr>
          </tbody>
        </table>
        <blockquote>频率限制：每分钟 30 次</blockquote>
      </body>
    </html>
    """
    ops = extract_operations("https://developer.work.weixin.qq.com/document/path/1", html)
    assert len(ops) == 1
    op = ops[0]
    assert op.endpoint == "/cgi-bin/message/send"
    assert op.method == "POST"
    assert op.title == "发送消息"
    assert op.request_url == "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=ACCESS_TOKEN"
    assert [field.name for field in op.request_params] == ["access_token", "touser"]
    assert op.request_params[1].required is False
    assert op.request_example_json == {"touser": "zhangsan", "msgtype": "text"}
    assert op.response_example_json == {"errcode": 0, "errmsg": "ok"}
    assert [field.name for field in op.response_params] == ["errcode", "errmsg"]
    assert "频率限制" in op.notes[0]


def test_extract_links_filters_domain_and_path():
    html = """
    <a href="/document/path/123">ok</a>
    <a href="https://developer.work.weixin.qq.com/document/path/456">ok2</a>
    <a href="https://example.com/document/path/789">bad-domain</a>
    <a href="/other/path/1">bad-path</a>
    """
    links = extract_links("https://developer.work.weixin.qq.com/document/path/1", html)
    assert links == [
        "https://developer.work.weixin.qq.com/document/path/123",
        "https://developer.work.weixin.qq.com/document/path/456",
    ]


def test_build_seed_urls_supports_menu_tree_and_deduplicate(tmp_path):
    seed_file = tmp_path / "seeds.txt"
    seed_file.write_text(
        "https://developer.work.weixin.qq.com/document/path/90664\n",
        encoding="utf-8",
    )
    # Create a minimal menu_tree.json with type=1 (document) nodes
    menu_tree_file = tmp_path / "menu_tree.json"
    menu_tree_file.write_text(
        '[{"id": 90665, "type": 1}, {"id": 90666, "type": 1}]',
        encoding="utf-8",
    )
    seeds = build_seed_urls(
        explicit_seeds=["https://developer.work.weixin.qq.com/document/path/90664"],
        seed_file=seed_file,
        menu_tree_file=menu_tree_file,
    )
    assert "https://developer.work.weixin.qq.com/document/path/90664" in seeds
    assert "https://developer.work.weixin.qq.com/document/path/90665" in seeds
    assert "https://developer.work.weixin.qq.com/document/path/90666" in seeds
    assert len(seeds) == len(set(seeds))


def test_build_seed_urls_filters_menu_tree_type_zero(tmp_path):
    """Menu tree nodes with type != 1 (category/directory nodes) are skipped."""
    menu_tree_file = tmp_path / "menu_tree.json"
    menu_tree_file.write_text(
        '[{"id": 90000, "type": 0}, {"id": 90004, "type": 0}, {"id": 90200, "type": 1}]',
        encoding="utf-8",
    )
    seeds = build_seed_urls(
        explicit_seeds=[],
        seed_file=None,
        menu_tree_file=menu_tree_file,
    )
    # Only type=1 node included
    assert seeds == ["https://developer.work.weixin.qq.com/document/path/90200"]


def test_build_seed_urls_menu_tree_missing_type_field(tmp_path):
    """Nodes without a type field are skipped; fallback default seed not triggered when explicit_seeds provided."""
    menu_tree_file = tmp_path / "menu_tree.json"
    menu_tree_file.write_text(
        '[{"id": 90665}, {"id": 90666}]',
        encoding="utf-8",
    )
    seeds = build_seed_urls(
        explicit_seeds=["https://developer.work.weixin.qq.com/document/path/90200"],
        seed_file=None,
        menu_tree_file=menu_tree_file,
    )
    # Both menu tree nodes lack type=1 → skipped. Only explicit_seed remains.
    assert seeds == ["https://developer.work.weixin.qq.com/document/path/90200"]


# --- crawl() tests ---

SAMPLE_HTML_WITH_API = """
<html>
  <head><title>发送消息 - 文档 - 企业微信开发者中心</title></head>
  <body>
    <p><strong>请求方式：</strong>POST（<strong>HTTPS</strong>）<br>
    <strong>请求地址：</strong>https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=ACCESS_TOKEN</p>
  </body>
</html>
"""

SAMPLE_HTML_EMPTY = "<html><body><p>Some non-API page</p></body></html>"

SEED_A = "https://developer.work.weixin.qq.com/document/path/90001"
SEED_B = "https://developer.work.weixin.qq.com/document/path/90002"
SEED_C = "https://developer.work.weixin.qq.com/document/path/90003"


def test_crawl_visits_all_seeds():
    pages = {SEED_A: SAMPLE_HTML_WITH_API, SEED_B: SAMPLE_HTML_WITH_API, SEED_C: SAMPLE_HTML_EMPTY}
    with patch("scripts.discover_wecom_apis.fetch_html", side_effect=lambda u, **kw: pages[u]):
        report = crawl([SEED_A, SEED_B, SEED_C], max_pages=10, delay_min=0, delay_max=0)
    assert report.visited_pages == 3
    # SEED_A and SEED_B produce same endpoint/method → deduplicated to 1
    assert len(report.operations) == 1


def test_crawl_respects_max_pages():
    seeds = [f"https://developer.work.weixin.qq.com/document/path/9000{i}" for i in range(10)]
    pages = {u: SAMPLE_HTML_EMPTY for u in seeds}
    with patch("scripts.discover_wecom_apis.fetch_html", side_effect=lambda u, **kw: pages[u]):
        report = crawl(seeds, max_pages=3, delay_min=0, delay_max=0)
    assert report.visited_pages == 3


def test_crawl_records_failures():
    def fetch_fail(url):
        raise ConnectionError("timeout")

    with patch("scripts.discover_wecom_apis.fetch_html", side_effect=fetch_fail):
        report = crawl([SEED_A, SEED_B], max_pages=10, delay_min=0, delay_max=0)
    assert report.failed_pages == 2
    assert len(report.failures) == 2
    assert all(isinstance(f, CrawlFailure) for f in report.failures)
    assert report.visited_pages == 2


def test_crawl_deduplicates_urls():
    with patch("scripts.discover_wecom_apis.fetch_html", return_value=SAMPLE_HTML_EMPTY):
        report = crawl([SEED_A, SEED_A, SEED_A], max_pages=10, delay_min=0, delay_max=0)
    assert report.visited_pages == 1


def test_crawl_seed_only_mode_ignores_non_seed_links():
    html_with_link = SAMPLE_HTML_EMPTY.replace(
        "</body>",
        '<a href="https://developer.work.weixin.qq.com/document/path/99999">link</a></body>',
    )
    with patch("scripts.discover_wecom_apis.fetch_html", return_value=html_with_link):
        report = crawl([SEED_A], max_pages=100, seed_only=True, delay_min=0, delay_max=0)
    assert report.visited_pages == 1


def test_crawl_free_mode_follows_discovered_links():
    html_a = SAMPLE_HTML_EMPTY.replace(
        "</body>",
        f'<a href="{SEED_B}">link</a></body>',
    )
    html_b = SAMPLE_HTML_WITH_API
    pages = {SEED_A: html_a, SEED_B: html_b}

    with patch("scripts.discover_wecom_apis.fetch_html", side_effect=lambda u, **kw: pages[u]):
        report = crawl([SEED_A], max_pages=10, seed_only=False, delay_min=0, delay_max=0)
    assert report.visited_pages == 2
    assert len(report.operations) == 1


def test_crawl_deduplicates_operations_by_endpoint_method():
    with patch("scripts.discover_wecom_apis.fetch_html", return_value=SAMPLE_HTML_WITH_API):
        report = crawl([SEED_A, SEED_B], max_pages=10, delay_min=0, delay_max=0)
    # Both pages produce same endpoint/method → deduplicated
    assert len(report.operations) == 1


# --- empty pages cache tests ---

EMPTY_CACHE_SEED = "https://developer.work.weixin.qq.com/document/path/91000"


def test_load_empty_pages_returns_set(tmp_path):
    cache_file = tmp_path / "empty.json"
    cache_file.write_text('["https://example.com/a", "https://example.com/b"]', encoding="utf-8")
    result = _load_empty_pages(cache_file)
    assert result == {"https://example.com/a", "https://example.com/b"}


def test_load_empty_pages_missing_file():
    result = _load_empty_pages(None)
    assert result == set()


def test_load_empty_pages_nonexistent_file(tmp_path):
    result = _load_empty_pages(tmp_path / "does_not_exist.json")
    assert result == set()


def test_save_empty_pages_writes_sorted(tmp_path):
    cache_file = tmp_path / "empty.json"
    _save_empty_pages(cache_file, {"https://example.com/b", "https://example.com/a"})
    data = cache_file.read_text(encoding="utf-8")
    assert data == '[\n  "https://example.com/a",\n  "https://example.com/b"\n]'


def test_save_empty_pages_none_is_noop():
    _save_empty_pages(None, {"https://example.com/a"})


def test_crawl_skips_cached_empty_pages(tmp_path):
    cache_file = tmp_path / "empty.json"
    cache_file.write_text('["https://developer.work.weixin.qq.com/document/path/91000"]', encoding="utf-8")

    with patch("scripts.discover_wecom_apis.fetch_html") as mock_fetch:
        mock_fetch.return_value = SAMPLE_HTML_WITH_API
        report = crawl(
            [EMPTY_CACHE_SEED], max_pages=10, delay_min=0, delay_max=0,
            empty_pages_file=cache_file,
        )
    # Cached-empty page must be skipped without fetching
    mock_fetch.assert_not_called()
    assert report.visited_pages == 1
    assert len(report.operations) == 0


def test_crawl_saves_new_empty_pages(tmp_path):
    cache_file = tmp_path / "empty.json"

    with patch("scripts.discover_wecom_apis.fetch_html", return_value=SAMPLE_HTML_EMPTY):
        report = crawl(
            [EMPTY_CACHE_SEED], max_pages=10, delay_min=0, delay_max=0,
            empty_pages_file=cache_file,
        )
    assert report.visited_pages == 1
    assert len(report.operations) == 0

    # Verify cache was written
    saved = _load_empty_pages(cache_file)
    assert EMPTY_CACHE_SEED in saved


def test_crawl_empty_cache_merges_with_existing(tmp_path):
    cache_file = tmp_path / "empty.json"
    cache_file.write_text('["https://developer.work.weixin.qq.com/document/path/99999"]', encoding="utf-8")

    with patch("scripts.discover_wecom_apis.fetch_html", return_value=SAMPLE_HTML_EMPTY):
        crawl(
            [EMPTY_CACHE_SEED], max_pages=10, delay_min=0, delay_max=0,
            empty_pages_file=cache_file,
        )

    saved = _load_empty_pages(cache_file)
    assert EMPTY_CACHE_SEED in saved
    assert "https://developer.work.weixin.qq.com/document/path/99999" in saved
    assert len(saved) == 2


def test_strip_tree_prefix_removes_box_drawing_chars():
    assert _strip_tree_prefix("└ contents") == "contents"
    assert _strip_tree_prefix("└ └ control") == "control"
    assert _strip_tree_prefix("├─ name") == "name"
    assert _strip_tree_prefix("│  value") == "value"
    assert _strip_tree_prefix("normal_field") == "normal_field"
    assert _strip_tree_prefix("") == ""
    assert _strip_tree_prefix("process_list.node_list") == "process_list_node_list"
    assert _strip_tree_prefix("attachment_list[].file_name") == "attachment_list_file_name"


# --- CAPTCHA detection tests ---

CAPTCHA_HTML = '<html><body>TencentCaptcha</body></html>'
CAPTCHA_SEED = "https://developer.work.weixin.qq.com/document/path/92000"


def test_is_captcha_block_detects_short_captcha_html():
    assert _is_captcha_block(CAPTCHA_HTML) is True
    assert _is_captcha_block("<html>TencentCaptcha</html>") is True
    assert _is_captcha_block("<html>captcha</html>") is True
    assert _is_captcha_block("<html>/security/verify</html>") is True


def test_is_captcha_block_passes_real_html():
    assert _is_captcha_block(SAMPLE_HTML_WITH_API) is False
    assert _is_captcha_block(SAMPLE_HTML_EMPTY) is False


def test_crawl_aborts_after_consecutive_captcha_blocks():
    seeds = [f"https://developer.work.weixin.qq.com/document/path/9200{i}" for i in range(10)]
    with patch("scripts.discover_wecom_apis.fetch_html", return_value=CAPTCHA_HTML):
        report = crawl(seeds, max_pages=100, delay_min=0, delay_max=0)
    assert report.blocked_pages == CAPTCHA_CONSECUTIVE_LIMIT
    assert report.visited_pages == CAPTCHA_CONSECUTIVE_LIMIT


def test_crawl_does_not_cache_captcha_pages(tmp_path):
    cache_file = tmp_path / "empty.json"
    with patch("scripts.discover_wecom_apis.fetch_html", return_value=CAPTCHA_HTML):
        crawl(
            [CAPTCHA_SEED], max_pages=100, delay_min=0, delay_max=0,
            empty_pages_file=cache_file,
        )
    # CAPTCHA pages must NOT be cached as empty
    saved = _load_empty_pages(cache_file)
    assert CAPTCHA_SEED not in saved


def test_crawl_recovers_after_isolated_captcha():
    """Single CAPTCHA followed by real page — should not abort."""
    responses = [CAPTCHA_HTML, SAMPLE_HTML_WITH_API]
    with patch("scripts.discover_wecom_apis.fetch_html", side_effect=responses):
        report = crawl(
            [CAPTCHA_SEED, SEED_A], max_pages=10, delay_min=0, delay_max=0,
        )
    # One blocked page, but should continue and find the API
    assert report.blocked_pages == 1
    assert len(report.operations) >= 1


# --- fetch_html() tests ---

def test_fetch_html_success():
    with patch("scripts.discover_wecom_apis.urlopen") as mock_urlopen:
        mock_resp = mock_urlopen.return_value.__enter__.return_value
        mock_resp.read.return_value = b"<html>ok</html>"
        result = fetch_html("https://example.com")
    assert result == "<html>ok</html>"


def test_fetch_html_timeout_raises():
    with patch("scripts.discover_wecom_apis.urlopen", side_effect=TimeoutError("timed out")):
        try:
            fetch_html("https://example.com", timeout=1)
        except TimeoutError:
            pass
        else:
            raise AssertionError("Expected timeout to raise")


def test_fetch_html_sends_headers():
    with patch("scripts.discover_wecom_apis.urlopen") as mock_urlopen:
        mock_resp = mock_urlopen.return_value.__enter__.return_value
        mock_resp.read.return_value = b"<html></html>"
        fetch_html("https://example.com")
        req = mock_urlopen.call_args[0][0]
        assert req.get_header("User-agent") or req.get_header("User-Agent")
