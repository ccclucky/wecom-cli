"""Script to automatically fetch and update the WeCom API menu tree."""

import argparse
import json
import re
import urllib.request
from pathlib import Path


def update_menu_tree(output_path: Path, cookie: str | None = None) -> int:
    url = "https://developer.work.weixin.qq.com/document/path/90665"
    headers: dict[str, str] = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    if cookie:
        headers["Cookie"] = cookie
    req = urllib.request.Request(url, headers=headers)

    print(f"Fetching latest menu tree from {url} ...")
    try:
        response = urllib.request.urlopen(req, timeout=15)
        html = response.read().decode("utf-8")
    except Exception as e:
        print(f"Failed to fetch document page: {e}. Falling back to existing menu tree.")
        return 0

    m = re.search(r"window\.categories\s*=\s*(\[.*?\])(?:;|\n|</script>)", html, re.DOTALL)
    if not m:
        print(
            "Could not find 'window.categories' in the HTML (possible CAPTCHA block). Falling back to existing menu tree."
        )
        return 0

    try:
        categories = json.loads(m.group(1))
    except Exception as e:
        print(f"Failed to parse JSON: {e}. Falling back to existing menu tree.")
        return 0

    if not categories:
        print("Fetched categories are empty. Falling back to existing menu tree.")
        return 0

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(categories, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Successfully updated menu tree with {len(categories)} nodes at {output_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Update WeCom menu tree")
    parser.add_argument("--output", type=Path, default=Path("specs/wecom/menu_tree.json"))
    parser.add_argument("--cookie", default=None, help="Cookie header for request (bypasses CAPTCHA)")
    args = parser.parse_args()
    return update_menu_tree(args.output, cookie=args.cookie)


if __name__ == "__main__":
    raise SystemExit(main())
