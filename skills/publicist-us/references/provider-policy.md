# Provider acquisition policy

Read current terms before production use. Platform policy can change after this document is released. Use official API or MCP access only when the account and contract authorize the intended data and automation.

| Provider | Allowed route | Boundary |
|---|---|---|
| Featured | Official OAuth MCP or human product use | No unauthorized bots, harvesting, redistribution, fabricated experts or quotations, or spam. Qualified human review is required before AI PR content is sent or published. |
| Qwoted | Human on-platform discovery and human-authored commentary | No scraping or contact harvesting. Its Community Guidelines prohibit AI/LLM-generated commentary. Do not draft or submit a Qwoted response, contact reporters off-platform, or follow up unless the reporter replies. |
| Source of Sources | Human use unless written permission expressly covers AI processing | Do not ingest, copy, redistribute, scrape, retransmit, or recirculate Queries or query emails. |
| MentionMatch | Official arranged or paid API/webhook after authorization; otherwise human use | No unauthorized automated access, systematic retrieval, scraping, robots, or offline readers. Verified Sender status does not verify the underlying request. |
| JournoFinder | Official OAuth MCP or licensed UI/export | External MCP access requires an eligible paid account and browser OAuth. Never request an API key; preserve provider/article evidence and verify current role and fit independently. |

## Licensed request content

Authorized access to a source request permits task processing, not automatic redistribution. Keep the minimum audit record needed: provider, request ID, canonical URL where available, retrieval time, text hash and terms status. Do not place full private/licensed query text into public fixtures, issues, logs or repository artifacts. Source of Sources is stricter: its terms restrict copying, redistribution, scraping, retransmission and recirculation of Queries/service content.

## General acquisition rules

- `robots.txt` describes crawler preferences; it does not grant contractual, privacy, copyright, or account authorization.
- Never bypass authentication, rate limits, CAPTCHAs, access controls, or technical barriers.
- A public page does not automatically authorize bulk collection, enrichment, reuse, or outreach.
- Preserve platform, request ID, canonical URL, retrieval time, text hash, access route, and terms status.
- Keep licensed exports within their contractual scope and retention period.
- When authorization is uncertain, stop collection and return `permission-required` or `manual-only`.

## Primary sources

- Featured: <https://featured.com/terms> and <https://featured.com/acceptable-use>
- Qwoted: <https://app.qwoted.com/terms_of_service> and <https://www.qwoted.com/qwoted-community-guidelines/>
- Source of Sources: <https://www.sourceofsources.com/universal-terms-of-service/>
- MentionMatch: <https://mentionmatch.com/terms> and <https://mentionmatch.com/api>
- JournoFinder: <https://help.journofinder.com/en/articles/9410893-terms-of-service> and <https://journofinder.com/mcp>
