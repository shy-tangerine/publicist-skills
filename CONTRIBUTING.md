# Contributing

Contributions are welcome when they improve a market workflow, correct a source-backed claim, add a useful provider route, strengthen a user-facing example, or fix the public documentation.

## Before you contribute

Before opening an issue or pull request, search the open issues and pull requests for related work. This repository is agent-facing, so mandatory research helps prevent duplicate tracker items and conflicting changes.

Outside contributors must use a fork and open a pull request. Never push directly to `main`; review and merge remain with the owner/Codex.

Bug reports and small fixes may be opened directly. Features require an issue first; do not open drive-by feature pull requests.

There is no AI-disclosure requirement for contributors.

## Identity policy

All repository activity must be under `shy-tangerine`. Never use the repository owner's real name on issues, pull requests, commits, attribution, metadata, or any other surface.

## Sources and wiki articles

The public knowledge base contains synthesized articles with direct links to original sources. Keep scraped pages, downloaded source text, browser captures, search exports, research logs, and working notes outside the repository.

When adding or changing guidance:

1. Prefer a current law, regulator, press council, professional association, platform policy, or original newsroom guide.
2. Add the source name, direct URL, publisher, publication date when known, and review date to the relevant wiki article or skill source map.
3. Explain the operational consequence in your own words. Quote only when the exact wording is necessary, and keep the quotation short.
4. Record uncertainty and conflicting evidence. Operational guidance must not be presented as a legal conclusion.
5. Update [`wiki/index.md`](wiki/index.md) when you add or rename an article.

Translations and search snippets can help locate a source, but a precise claim must point to the original publication. Recheck policy and legal links whenever they affect a release.

## Skills

- Maintain exactly five top-level country packages and present them in this order: United States/English, Germany/German, mainland China/Simplified Chinese, Japan/Japanese, and Brazil/Brazilian Portuguese.
- Keep optional platform skills in `publicist-<market>-<topic>` directories, one `SKILL.md` each. A platform skill is reference depth for one market: it pairs with that market's country skill, carries its own dated sources, and never depends on another platform skill or the repository wiki.
- Keep cross-market marketing skills in short, standalone directories when their workflow is not market-specific. They may be used independently of country and platform companions.
- Keep the complete default workflow and market-specific decision points in each `SKILL.md`. Use bundled references only for conditional provider, legal, strategy, and source detail.
- Make every country skill independently usable. It must not depend on the US skill or repository wiki for ordinary work.
- Keep reusable prompts in user-facing documentation, not inside installable skill references.
- Treat the companion wiki as optional depth. A missing repository connection must never block the installed workflow.
- Preserve the safety boundary around data acquisition and external communication.
- Give each country package its own contact-provider guide, legal and ethics guide, source map, strategy, and metadata.
- Use fictional people, outlets, addresses, requests, and identifiers in examples and tests.

Only commit publication-ready material. Client dossiers, contact databases, private correspondence, credentials, tokens, internal plans, local paths, and unpublished research do not belong in the repository.

## Validate

```bash
for skill in skills/*; do
  python3 /path/to/skill-creator/scripts/quick_validate.py "$skill"
done
git diff --check
```

In a pull request, explain the user-visible change, the sources consulted, the risks, and the validation performed. Provider-policy and legal-source changes must include a review date. Update the platform-skill index for the market when you add or rename a platform skill.
