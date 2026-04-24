from __future__ import annotations

from scripts.discover_wecom_apis import build_seed_urls, extract_links, extract_operations


def test_extract_operations_from_html():
    html = """
    <html><body>
      <h2>请求方式：POST</h2>
      <code>/cgi-bin/message/send</code>
      <code>/cgi-bin/user/simplelist</code>
    </body></html>
    """
    ops = extract_operations("https://developer.work.weixin.qq.com/document/path/1", html)
    assert len(ops) == 2
    assert {o.endpoint for o in ops} == {"/cgi-bin/message/send", "/cgi-bin/user/simplelist"}
    assert all(o.method == "POST" for o in ops)


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


def test_build_seed_urls_supports_range_and_deduplicate(tmp_path):
    seed_file = tmp_path / "seeds.txt"
    seed_file.write_text(
        "https://developer.work.weixin.qq.com/document/path/90664\n",
        encoding="utf-8",
    )
    seeds = build_seed_urls(
        explicit_seeds=["https://developer.work.weixin.qq.com/document/path/90664"],
        seed_file=seed_file,
        doc_id_from=90664,
        doc_id_to=90666,
    )
    assert seeds[0] == "https://developer.work.weixin.qq.com/document/path/90664"
    assert "https://developer.work.weixin.qq.com/document/path/90665" in seeds
    assert "https://developer.work.weixin.qq.com/document/path/90666" in seeds
    assert len(seeds) == len(set(seeds))
