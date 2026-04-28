from __future__ import annotations

from unittest.mock import patch

from scripts.discover_wecom_apis import (
    CrawlFailure,
    CrawlReport,
    DiscoveredOperation,
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
    # Create a minimal menu_tree.json with two nodes
    menu_tree_file = tmp_path / "menu_tree.json"
    menu_tree_file.write_text(
        '[{"id": 90665}, {"id": 90666}]',
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
    with patch("scripts.discover_wecom_apis.fetch_html", side_effect=lambda u: pages[u]):
        report = crawl([SEED_A, SEED_B, SEED_C], max_pages=10, delay_min=0, delay_max=0)
    assert report.visited_pages == 3
    # SEED_A and SEED_B produce same endpoint/method → deduplicated to 1
    assert len(report.operations) == 1


def test_crawl_respects_max_pages():
    seeds = [f"https://developer.work.weixin.qq.com/document/path/9000{i}" for i in range(10)]
    pages = {u: SAMPLE_HTML_EMPTY for u in seeds}
    with patch("scripts.discover_wecom_apis.fetch_html", side_effect=lambda u: pages[u]):
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
        f'<a href="https://developer.work.weixin.qq.com/document/path/99999">link</a></body>',
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

    with patch("scripts.discover_wecom_apis.fetch_html", side_effect=lambda u: pages[u]):
        report = crawl([SEED_A], max_pages=10, seed_only=False, delay_min=0, delay_max=0)
    assert report.visited_pages == 2
    assert len(report.operations) == 1


def test_crawl_deduplicates_operations_by_endpoint_method():
    with patch("scripts.discover_wecom_apis.fetch_html", return_value=SAMPLE_HTML_WITH_API):
        report = crawl([SEED_A, SEED_B], max_pages=10, delay_min=0, delay_max=0)
    # Both pages produce same endpoint/method → deduplicated
    assert len(report.operations) == 1


# --- fetch_html() tests ---

def test_fetch_html_success():
    with patch("scripts.discover_wecom_apis.urlopen") as mock_urlopen:
        mock_resp = mock_urlopen.return_value.__enter__.return_value
        mock_resp.read.return_value = b"<html>ok</html>"
        result = fetch_html("https://example.com")
    assert result == "<html>ok</html>"


def test_fetch_html_timeout_raises():
    import socket
    with patch("scripts.discover_wecom_apis.urlopen", side_effect=socket.timeout("timed out")):
        try:
            fetch_html("https://example.com", timeout=1)
        except socket.timeout:
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
