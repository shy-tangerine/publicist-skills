#!/usr/bin/env python3
"""Impressum (Germany) provider wizard."""
from __future__ import annotations
import argparse, json, sys

PROVIDER = {"name": "Impressum", "market": "Germany", "class": "public-web lookup", "status": "supported", "url": "https://www.gesetze-im-internet.de/ddg/__5.html", "guide": "impressum"}

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--setup", action="store_true", help="Show setup guide")
    p.add_argument("--check", action="store_true", help="Check access status")
    args = p.parse_args()

    guide_url = "https://github.com/shy-tangerine/publicist-skills/blob/main/wiki/public-relations/providers/impressum.md"

    if args.setup:
        out = {
            "wizard": "publicist.provider-guidance.v1",
            "country": "Germany",
            "provider": PROVIDER["name"],
            "guide": "references/provider-adapters.md",
            "guide_url": guide_url,
            "official_fallback": PROVIDER["url"],
            "status": PROVIDER["status"],
            "class": PROVIDER["class"],
            "access_state": "not_checked",
            "next": "Read the guide, then follow the provider's official setup or manual route; this selector does not inspect or configure access."
        }
    else:
        out = {
            "wizard": "publicist.provider-guidance.v1",
            "country": "Germany",
            "provider": PROVIDER["name"],
            "guide": "references/provider-adapters.md",
            "guide_url": guide_url,
            "official_fallback": PROVIDER["url"],
            "status": PROVIDER["status"],
            "class": PROVIDER["class"],
            "access_state": "not_checked",
            "next": "Choose this provider to print its guide and official fallback. Access remains not_checked."
        }

    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
    return 0

if __name__ == "__main__":
    sys.exit(main())

