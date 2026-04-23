from __future__ import annotations

from scripts.discover_wecom_apis import extract_links, extract_operations


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
