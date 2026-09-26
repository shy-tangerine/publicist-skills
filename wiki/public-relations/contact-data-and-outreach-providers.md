# Contact-data and outreach providers for journalist research

> Sources: Hunter, Clay, and Apollo official documentation and policies (publication dates not stated unless shown on the linked page; accessed 2026-09-12)
> References: [Hunter API v2](https://hunter.io/api-documentation/v2); [Hunter Content Policy](https://hunter.io/transparency/content-policy); [Hunter Terms of Service](https://hunter.io/terms-of-service); [Hunter MCP](https://hunter.io/mcp); [Hunter unsubscriptions](https://help.hunter.io/en/articles/8486539-manage-unsubscriptions-in-sequences); [Clay Work Email waterfall](https://university.clay.com/docs/work-email-waterfall); [Clay waterfalls](https://university.clay.com/docs/building-a-data-waterfall); [Clay email sequencer](https://university.clay.com/docs/email-sequencer); [Clay MCP security and privacy](https://university.clay.com/docs/mcp-security-privacy); [Clay Terms of Service](https://www.clay.com/terms-of-service); [Clay Privacy Center](https://www.clay.com/privacy); [Apollo People Enrichment API](https://docs.apollo.io/reference/people-enrichment); [Apollo add contacts to sequence API](https://docs.apollo.io/reference/add-contacts-to-sequence); [Apollo MCP](https://docs.apollo.io/docs/apollo-mcp); [Apollo Privacy Policy](https://www.apollo.io/privacy-policy); [Apollo Terms of Service](https://www.apollo.io/terms-of-service); [Apollo unsubscribe settings](https://knowledge.apollo.io/hc/en-us/articles/4409140379661-Configure-Your-Email-Unsubscribe-Link)
> Updated: 2026-09-12

## Overview

Hunter, Clay, and Apollo can help complete or verify professional contact records, but none is a substitute for editorial research. The publicist workflow must first establish that a person covers the subject, that the outlet is appropriate, and that an official contact route does not already exist. Only then may an authorized provider be used to look for a missing professional address. Every result must retain one of these provenance classes: published, provider-supplied, or inferred. It must also pass the target market's privacy and outreach rules before it becomes a draft recipient.

## Three kinds of contact evidence

| Class | What it means | How the workflow treats it |
|---|---|---|
| Published editorial route | An address, form, newsroom directory entry, masthead, author profile, or request reply route published by the outlet or journalist | Preferred. Record the source URL and confirm that the route is intended for pitches, tips, or professional contact. |
| Provider-supplied or enriched address | A professional contact field returned from a licensed database or enrichment vendor | Secondary. Record provider, query date, match confidence or verification status, and the lawful-use decision. Never describe it as published by the journalist. |
| Inferred or guessed address | An address constructed from a name and domain pattern, whether by a provider or locally | Weakest. A successful SMTP-style validation can indicate deliverability; it does not prove identity, consent, editorial purpose, or willingness to receive a pitch. Label it inferred and use only where the market workflow and the user's policy permit it. |

The same email can move between these classes only when new evidence supports the change. Finding an inferred address and later locating the same address on an official author page permits the record to cite the official page as published evidence; the enrichment result alone does not.

## Provider comparison

| Provider | Discovery and verification | Provenance | Access modes | Outreach capability | Geographic position |
|---|---|---|---|---|---|
| Hunter | Domain Search lists professional-domain addresses; Email Finder returns the most likely address for a named person and domain; Email Verifier checks a supplied address. API responses can include confidence, source URLs, and whether an address is public or inferred. | Hunter says its database contains professional contact data, excludes consumer-domain personal addresses, and labels records public or inferred. It may infer address patterns and performs SMTP verification. | Licensed web product, API v2, and official remote MCP. | Email Sequences can send one-off or automated emails through a connected mailbox and maintain a team-wide unsubscription list. | The API supports country/location and language filters in relevant discovery endpoints, but the official material reviewed does not promise equal coverage by country. Validate record-by-record. |
| Clay | Work Email waterfall calls multiple data providers in order and can validate results. Its optional Infer Email step constructs an address from name, company domain, and a pattern before paid providers run. | Clay orchestrates other providers; provenance and terms follow each selected provider. Enable the successful-provider output and keep intermediate evidence needed for audit. A Clay result is not a claim that Clay found the address on an official page. | Licensed web product and OAuth-scoped official MCP. The workspace admin chooses which MCP functions are exposed. | Clay Sequencer sends campaigns through connected Gmail, Outlook, SMTP, or uploaded mailboxes; it tracks sends, bounces, replies, and blocklist events. | Coverage is the union of the configured providers, not a universal Clay guarantee. Check each provider's supported markets and contract. |
| Apollo | People Enrichment matches a supplied person against Apollo data and can reveal professional contact fields; optional waterfall enrichment checks connected third-party sources. Match confidence concerns identity matching and does not prove permission to contact. | Apollo says its Contributor Database draws from public websites, professional directories, public regulatory and government sources, vetted third-party providers, customer/user contributions, and derived or inferred data. | Licensed web product, API/API keys or OAuth scopes, and official MCP subject to account permissions. | Apollo Sequences can send from connected email accounts; APIs can add existing contacts to sequences. Paid plans can append unsubscribe links and supported mailboxes can add one-click unsubscribe headers. | Search supports location filters, but the official material reviewed does not establish uniform global accuracy. Treat geography as a filter, not a coverage warranty. |

## Hunter: appropriate use in a publicist workflow

Use Hunter after verifying the journalist's identity, outlet, role, and relevant recent work from editorial sources. Domain Search is useful when the outlet domain is known; Email Finder is useful when both the journalist's name and professional domain are known; Email Verifier is useful when the workflow already has an address to check. Retain Hunter's source URLs, confidence, verification date/status, and public-versus-inferred label where returned.

Hunter's Content Policy permits professional B2B prospecting, CRM enrichment, and internal research, but prohibits consumer contact, spam or bulk unsolicited email, and automated mass sequences without individualized relevance. Hunter also states that users are independent data controllers responsible for lawful basis, transparency, opt-out suppression, minimization, and accuracy. Its Terms incorporate a data-processing agreement and make the customer responsible for compliance with applicable law.

The official remote MCP and API are suitable automation routes only when the user's Hunter account and current plan authorize them. Do not scrape the web interface or expose an API key in a prompt, log, wiki, or output. Hunter Sequences is a sending tool, not an implicit permission to send: the publicist skill may prepare an exact message and recipient record, but sending requires the user's explicit authorization for that message and the market workflow's legal gate.

## Clay: appropriate use in a publicist workflow

Clay is best understood as an orchestration layer. Its waterfall runs providers in a chosen order and stops according to configured validation rules. The Work Email waterfall can expose which provider succeeded, but that output is optional; turn it on for publicist work. Do not hide the provenance needed to explain where an address came from.

Keep **Infer Email** off by default for journalists. When a user explicitly permits inferred professional addresses and the market workflow allows them, label the output inferred even if validation succeeds. Clay's Conservative, Balanced, and Aggressive validation modes express delivery risk, not consent, relevance, or legal permission. A valid or catch-all result is not an editorial invitation.

Each third-party enrichment selected inside Clay remains governed by that provider's terms and the user's account rights. Clay's Terms place responsibility for uploaded content and lawful use on the customer and direct users to review third-party service terms. Its MCP uses browser OAuth, is scoped to one user and workspace, and exposes only functions enabled by an administrator; viewers can still trigger runs, so workspace role alone is not a sufficient control. Use function allow-lists, user-level spend limits, and a dedicated approved workflow.

Clay Sequencer connects to real mailboxes and starts sending when a campaign launches. Because launch is consequential, the skill should stop at a campaign-ready draft unless the user explicitly authorizes launch. Keep unsubscribe/blocklist handling enabled, pause a lead immediately on an objection, and do not convert a one-to-one journalist pitch into an always-on sales sequence.

## Apollo: appropriate use in a publicist workflow

Apollo is a B2B contact database and engagement platform, not a journalism directory. Use editorial evidence first to identify a journalist, then use People Enrichment only to complete a known person's professional record. Supply enough identity evidence, such as name, outlet, and domain, to reduce false matches. Accept only an appropriately strong match and retain the match-confidence value, returned data type, source/provider class, and lookup date.

Apollo's privacy policy says the Contributor Database can contain business emails, phone numbers, employment history, job titles, and social-profile URLs. Its sources include public sites and directories, government sources, vetted third parties, customer contributions, and generated inferences. Consequently, an Apollo result cannot be called public, journalist-published, or consented unless a separate first-party page proves that claim. Data subjects can request access, correction, deletion, or opt-out; Apollo may retain suppression data so removed records are not re-added.

Apollo's Terms license professional B2B communication but prohibit spam, unlawful marketing, unauthorized scraping or bots, redistribution of the database, and uses that violate data-subject rights. They require the customer to verify both accuracy and legal compliance before acting. API and MCP access therefore require an authorized account, current scopes, and compliance with rate, credit, export, and downstream-use limits.

Apollo Sequences is a real sending system. Adding contacts through the API requires an existing sequence and contacts in the team's Apollo database. An unsubscribe link or one-click header helps process objections but does not create a lawful basis for the first message. Keep those controls enabled and show the exact recipients and copy immediately before enrollment or launch.

## Recommended decision sequence

1. **Qualify editorial relevance.** Confirm the journalist, outlet, beat, recent bylines, and why the proposed story fits.
2. **Prefer first-party contact routes.** Check the byline, author page, masthead, newsroom directory, tip page, contact form, and the request platform where the opportunity originated.
3. **Apply the market gate.** Determine whether enrichment and unsolicited professional outreach are permitted for this purpose in the recipient's jurisdiction. Use the country skill's law and data-handling reference; uncertainty stops enrichment.
4. **Use one authorized provider.** Start with the narrowest lookup that can complete the known record. Do not bulk-search an outlet merely because the tool supports it.
5. **Preserve provenance.** Store the provider, source URL where supplied, lookup date, public/provider/inferred class, confidence or validation status, and account/contract basis.
6. **Verify independently.** Re-check role and outlet on current editorial pages. Treat catch-all, deliverable, and high-confidence labels as technical signals only.
7. **Draft one relevant pitch.** Tie the message to a specific recent article, request, or beat. Do not generate a mass sequence from a database export.
8. **Confirm the external action.** Present recipient, address provenance, channel, exact copy, attachments or links, and compliance notes immediately before sending or enrollment.
9. **Honor objections everywhere.** Stop follow-ups, update the suppression list, and propagate the opt-out to every authorized sending system.

## Market cautions

- **United States workflow.** Hunter and Apollo are B2B-oriented and can support targeted professional research, but the sender still owns CAN-SPAM and other applicable obligations. Database access never replaces editorial relevance.
- **Brazil.** Apply the LGPD purpose, necessity, transparency, rights, and legitimate-interest review before enrichment. Prefer outlet-published routes and minimize retained fields.
- **Germany.** Apply the UWG and GDPR workflow before any lookup or message. A professional address in a database does not establish the prior consent generally required for advertising email; prefer explicit requests, consented contacts, and official editorial submission routes.
- **Japan.** Apply APPI and unsolicited-email review and prefer official editorial forms, PR wires, or established introductions. Do not infer that a verified address accepts pitches.
- **Mainland China.** Apply PIPL purpose, consent/legal-basis, localization, and cross-border-transfer checks before sending personal data to an overseas enrichment provider. Prefer verified outlet submission channels and locally authorized workflows.

## Operational rule

Contact enrichment is optional. When the user lacks an authorized provider account, the market gate is unresolved, provenance cannot be retained, or an official editorial route exists, the skill should continue with the official route or return a research dossier with the contact field unresolved. It should never guess an address silently.

## See also

- [Localized media-contact infrastructure](localized-media-contact-infrastructure.md)
- [Brazil data handling and LGPD](brazil-data-and-lgpd.md)
- [Germany legal outreach](germany-legal-outreach.md)
- [Germany data handling](germany-data-handling.md)
- [Japan personal data and email law](japan-personal-data-and-email-law.md)
- [China data and cross-border](china-data-and-cross-border.md)
