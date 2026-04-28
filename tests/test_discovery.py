from __future__ import annotations

from scripts.discover_wecom_apis import build_seed_urls, extract_links, extract_operations


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
