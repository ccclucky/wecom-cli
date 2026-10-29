"""Report whether WECOM_DOC_COOKIE still authenticates against the doc site.

Every doc page embeds its own session state as

    "_userinfo":{"profile":{},"isLogin":false}

so one page fetch is enough to tell a working cookie from an expired one. The
crawl does not depend on this, but a valid cookie is the difference between
being cut off after ~25 minutes and finishing a sweep in one pass.

Exit codes:
  0  the cookie authenticates
  1  no cookie was supplied
  2  the cookie was supplied but the site treated the request as anonymous
  3  the marker could not be found, so the result is unknown
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from discover_wecom_apis import fetch_html

PROBE_URL = "https://developer.work.weixin.qq.com/document/path/90200"
USERINFO_RE = re.compile(r'"_userinfo":\{"profile":(\{.*?\}),"isLogin":(true|false)\}', re.S)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check whether the WeCom doc cookie still works")
    parser.add_argument("--cookie", default=None, help="Cookie header value to test")
    parser.add_argument("--probe-url", default=PROBE_URL, help="Page to probe")
    parser.add_argument("--output", type=Path, default=None, help="Optional JSON result path")
    args = parser.parse_args()

    result: dict[str, object] = {"probe_url": args.probe_url, "cookie_supplied": bool(args.cookie)}

    if not args.cookie:
        result["status"] = "missing"
        print("No cookie supplied; the crawl will run unauthenticated.")
        _write(args.output, result)
        return 1

    try:
        html = fetch_html(args.probe_url, cookie=args.cookie)
    except Exception as exc:  # noqa: BLE001 - the probe must never crash the workflow
        result["status"] = "error"
        result["error"] = str(exc)
        print(f"Probe failed: {exc}")
        _write(args.output, result)
        return 3

    match = USERINFO_RE.search(html)
    if not match:
        result["status"] = "unknown"
        print("Could not locate the _userinfo marker; the page layout may have changed.")
        _write(args.output, result)
        return 3

    profile = json.loads(match.group(1))
    logged_in = match.group(2) == "true"
    result.update(
        {
            "status": "valid" if logged_in else "expired",
            "is_login": logged_in,
            "profile_keys": sorted(profile),
            "response_bytes": len(html),
        }
    )
    _write(args.output, result)

    if logged_in:
        print(f"Cookie is valid (isLogin=true, profile fields: {', '.join(sorted(profile)) or 'none'}).")
        return 0
    print("Cookie is no longer valid: the site returned isLogin=false for an authenticated request.")
    return 2


def _write(path: Path | None, payload: dict[str, object]) -> None:
    if not path:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
