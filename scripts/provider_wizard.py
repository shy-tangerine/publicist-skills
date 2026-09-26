#!/usr/bin/env python3
"""Offline country-scoped provider guidance selector."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from provider_adapters import PROVIDERS
COUNTRIES={'us':'US','germany':'Germany','china':'Mainland China','japan':'Japan','brazil':'Brazil'}
def main() -> None:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('country'); p.add_argument('--setup',metavar='PROVIDER'); a=p.parse_args()
    if a.country.casefold() not in COUNTRIES:
        print(json.dumps({'wizard':'publicist.provider-guidance.v1','error':{'code':'unknown_country','message':'Choose us, germany, china, japan, or brazil.'}},indent=2)); raise SystemExit(2)
    market=COUNTRIES[a.country.casefold()]
    choices=[dict(x) for x in PROVIDERS if x['market'] in (market,'cross-market')]
    if a.setup:
        found=next((x for x in choices if x['name'].casefold()==a.setup.casefold()),None)
        if found is None:
            print(json.dumps({'wizard':'publicist.provider-guidance.v1','country':market,'error':{'code':'provider_not_in_country','message':'Choose a provider listed for this country.'}},indent=2)); raise SystemExit(2)
        remote_guide=f"wiki/public-relations/providers/{found['guide']}.md"
        package_guide=remote_guide if (Path(__file__).resolve().parent.parent / remote_guide).exists() else 'references/provider-adapters.md'
        out={'wizard':'publicist.provider-guidance.v1','country':market,'provider':found['name'],'guide':package_guide,'guide_url':f"https://github.com/shy-tangerine/publicist-skills/blob/main/{remote_guide}",'official_fallback':found['url'],'status':found['status'],'class':found['class'],'access_state':'not_checked','next':"Read the guide, then follow the provider's official setup or manual route; this selector does not inspect or configure access."}
    else: out={'wizard':'publicist.provider-guidance.v1','country':market,'choices':choices,'next':'Choose one provider to print its guide and official fallback. Access remains not_checked.'}
    print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
if __name__=='__main__': main()
