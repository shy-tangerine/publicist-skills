#!/usr/bin/env python3
"""Offline provider guidance selector for Japan. Generated; do not edit."""
import argparse
import json

MARKET = 'Japan'
ROWS = [('PRONE/PRM', 'permission-required', 'authenticated dataset', 'https://prone.jp/prm', 'prone'), ('Foreign Press Center Japan', 'supported', 'public-web lookup', 'https://fpcj.jp/en/assistance/fpregcard/', 'fpcj'), ('Kyodo News PR Wire', 'manual-only', 'browser-only', 'https://kyodonewsprwire.jp/corp/domestic/service-en/', 'kyodo-news-pr-wire'), ('Hunter', 'permission-required', 'API-capable', 'https://hunter.io/api-documentation/v2', 'hunter'), ('Clay', 'permission-required', 'official OAuth MCP', 'https://api.clay.com/v3/mcp', 'clay'), ('Apollo', 'permission-required', 'API-capable', 'https://docs.apollo.io/reference/people-enrichment', 'apollo')]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--setup", metavar="PROVIDER")
    args = parser.parse_args()
    choices = [dict(name=n, market=MARKET, **{"status": s, "class": c, "url": u, "guide": g}) for n, s, c, u, g in ROWS]
    if args.setup:
        found = next((item for item in choices if item["name"].casefold() == args.setup.casefold()), None)
        if found is None:
            print(json.dumps({"wizard": "publicist.provider-guidance.v1", "country": MARKET, "error": {"code": "provider_not_in_country", "message": "Choose a provider listed for this country."}}, indent=2))
            raise SystemExit(2)
        remote_guide = f"wiki/public-relations/providers/{found['guide']}.md"
        output = {"wizard": "publicist.provider-guidance.v1", "country": MARKET, "provider": found["name"], "guide": "references/provider-adapters.md", "guide_url": f"https://github.com/shy-tangerine/publicist-skills/blob/main/{remote_guide}", "official_fallback": found["url"], "status": found["status"], "class": found["class"], "access_state": "not_checked", "next": "Read the guide, then follow the provider's official setup or manual route; this selector does not inspect or configure access."}
    else:
        output = {"wizard": "publicist.provider-guidance.v1", "country": MARKET, "choices": choices, "next": "Choose one provider to print its guide and official fallback. Access remains not_checked."}
    print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
