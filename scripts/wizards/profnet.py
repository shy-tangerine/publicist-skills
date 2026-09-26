#!/usr/bin/env python3
"""ProfNet (Mainland China) provider wizard."""
from __future__ import annotations
import argparse, json, sys

PROVIDER = {"name": "ProfNet", "market": "Mainland China", "class": "browser-only", "status": "manual-only", "url": "https://www.prnewswire.com/profnet/", "guide": "profnet"}

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--setup", action="store_true", help="Show setup guide")
    p.add_argument("--check", action="store_true", help="Check access status")
    args = p.parse_args()

    guide_url = "https://github.com/shy-tangerine/publicist-skills/blob/main/wiki/public-relations/providers/profnet.md"

    if args.setup:
        out = {
            "wizard": "publicist.provider-guidance.v1",
            "country": "Mainland China",
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
            "country": "Mainland China",
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

