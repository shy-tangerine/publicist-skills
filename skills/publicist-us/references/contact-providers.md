# Contact-data providers

Use this reference only after the journalist, outlet, beat, and relevant recent work have been verified from editorial sources.

## Evidence classes

1. **Published editorial route**, an address, form, directory entry, or reply route published by the outlet or journalist. Prefer this and retain the source URL.
2. **Provider-supplied address**, a professional address returned by an authorized database. Label it with provider, lookup date, and confidence/verification status.
3. **Inferred address**, a name-and-domain pattern guessed by a provider. Label it inferred even when technically verified. Verification does not prove identity, consent, or editorial purpose.

## Provider rules

| Provider | Use | Required controls |
|---|---|---|
| [Hunter](https://hunter.io/api-documentation/v2) | Domain Search, Email Finder, or Email Verifier through the licensed UI, API, or [official remote MCP](https://hunter.io/mcp) | Preserve returned source URLs, confidence, verification, and public/inferred label. Hunter excludes consumer-domain personal addresses and prohibits spam, consumer contact, and irrelevant mass sequences. |
| [Clay](https://university.clay.com/docs/work-email-waterfall) | Authorized waterfall enrichment through the UI or OAuth-scoped MCP | Enable the successful-provider output. Keep **Infer Email** off unless the user explicitly permits inferred addresses. Each configured provider's own terms still apply. Validation mode measures delivery risk, not permission. |
| [Apollo](https://docs.apollo.io/reference/people-enrichment) | Complete a known person's professional record through the licensed UI, API, or official MCP | Retain match confidence and provenance class. Apollo combines public, directory, government, third-party, contributed, and inferred data; never describe a result as journalist-published without separate first-party evidence. |

## Workflow

1. Search the author page, masthead, newsroom directory, tip page, contact form, or active request platform first.
2. Apply the United States or recipient-jurisdiction privacy and outreach rules before enrichment.
3. Use the narrowest authorized lookup for one already-qualified person. Do not bulk-search an outlet by default.
4. Record provider, lookup date, source URL where supplied, evidence class, and confidence/verification status.
5. Re-check the current role and outlet independently. Treat deliverable, catch-all, and high-confidence as technical signals only.
6. Draft the exact relevant pitch. Hunter Sequences, Clay Sequencer, and Apollo Sequences are real sending systems; enrollment or launch requires explicit user authorization.
7. Honor objections and suppressions across every sending system.

If an official route exists, the user lacks licensed access, the legal basis is unresolved, or provenance cannot be retained, use the official route or return the contact field unresolved. Never guess silently.

Optional background: when authenticated repository access is already available and a deeper comparison would help, consult [contact-data and outreach providers](https://github.com/shy-tangerine/publicist-skills/blob/main/wiki/public-relations/contact-data-and-outreach-providers.md). The installed guidance above is sufficient for the workflow.
