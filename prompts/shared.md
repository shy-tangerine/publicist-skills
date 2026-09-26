# Shared brief and workflows

[Prompt library](README.md)

## Shared brief

Paste this block first for substantial assignments:

For repeated or substantial work, the user may instead supply the optional local/user-owned campaign context described in [campaign context](../docs/campaign-context.md). Reuse only supported, unexpired fields; apply exclusions and prior-contact suppression before ranking; flag conflicts as `NEEDS_REVIEW`. Never require this artifact for a one-off task, upload real campaign context to the repository, or treat it as authorization to contact anyone.

> **Brief**
> - Organization and represented interests: [name, commercial relationship, disclosure required]
> - News peg and deadline: [what changed, when, timezone, embargo]
> - Audience and geography: [who needs to know, country/region]
> - Approved facts and source links: [fact -> URL or supplied document]
> - Methodology and limitations: [sample, period, definitions, uncertainty]
> - Spokesperson: [name, role, credentials, languages, availability]
> - Useful assets: [dataset, document, image rights, demo, customer/independent source and permission]
> - Exclusions and prior outreach: [claims, outlets, people, dates, replies]
> - Desired deliverable: [research, angle, draft, follow-up, correction, or results review]

Ask for `REJECT`, `NEEDS_REVIEW`, or `DRAFT_ALLOWED`, plus a claim-to-source table, `needs_confirmation`, contact-route provenance, observation date, and next action. `DRAFT_ALLOWED` means the evidence and route gates passed; it does not mean a message was sent.

## Core sequence

### Qualify an opportunity

> Using the brief below, classify this as a source request, proactive pitch, newsjacking, launch, expert placement, or distribution task. Verify the opportunity, current outlet or journalist role, deadline and timezone, requirements, requested channel, editorial versus paid status, and every hard constraint. Read up to five recent relevant pieces and explain the recurring question this story would help answer. Return a small ranked list, evidence URLs and dates, contact route and provenance, `decision`, failed or unresolved gates, and a reason to exclude weaker candidates. Keep employment verified separate from beat inferred. Do not draft or contact anyone until the qualification table is complete.

### Develop angles from evidence

> From the approved facts, create three materially different angles for the qualified target. For each, provide: one-sentence thesis; why it is timely; audience or public value; two or more supporting sources; a counterpoint; methodology and limitation; a named useful asset or spokesperson; the exact connection to the target's recent work; and what new reporting the journalist could do. Reject angles that require an unsupported market-size claim, invented customer, fabricated local presence, or company background in place of news. Recommend one angle and state what evidence would change the choice.

### Draft and quality-check one pitch

> Draft one message for the verified route and channel. Put the news and its consequence in the subject and first two sentences. Tie the approach to one specific recent article, request, or verified beat, with URL and publication date in the working notes. Offer one useful asset or source, explain the limitation, disclose representation or commercial interest, and make one small concrete ask with availability and timezone. Use only facts in the brief or verified sources. Then run a hard edit: remove generic praise, biography before relevance, hype, false exclusivity, attachment dumping, unexplained acronyms, and asks the recipient cannot act on. Return subject, body, channel choice, claim map, missing facts, and a pass/fail checklist.

### Plan a disciplined follow-up

> Given the sent-or-ready pitch and the recipient's timezone, propose at most one follow-up after [market-appropriate interval]. It must add one genuinely useful new fact, asset, deadline clarification, or correction; it must not repeat the pitch or ask whether it was seen. Show the exact follow-up, evidence for its new information, stop conditions (no response, opt-out, complaint, changed deadline, or correction needed), and the date after which no further contact is proposed. Keep sending as a separate user-authorized action.

### Correct a published or circulated error

> Compare the published statement with the source record below. Identify the smallest material error, its impact, and the evidence that proves it. Draft a calm correction to the responsible desk or author that quotes the relevant wording, supplies corrected wording and primary source, explains remaining uncertainty, and offers a reachable human for questions. Do not conceal a client interest or demand favorable framing. Mark urgency, route, and whether legal or editorial review is needed. Do not send it.

### Assess results without claiming coverage

> Review this outreach log: [messages, routes, dates, replies, published URLs, referral sources]. Separate delivered, opened, replied, declined, opted out, published, syndicated, paid/distributed, and independently reported outcomes. Attribute each result to evidence and date; never count a wire hit as independent editorial coverage. Explain which angle, asset, route, timing, or unresolved gate likely affected the result, with uncertainty labeled. Recommend up to three changes for the next experiment and one thing to stop.

## Language and channel checks

Add this instruction whenever the recipient language or channel matters:

> Treat the recipient's published language, format, and route as evidence. Draft
> idiomatic copy for that channel rather than translating an English template.
> If a phrase, honorific, editorial convention, or disclosure term cannot be
> supported by a first-party example or the installed market guidance, mark
> `NEEDS_LANGUAGE_REVIEW` and show the exact uncertainty. Keep that flag narrow:
> do not use it as a substitute for checking the source.

## Earned-media preflight

Before treating a result as draft-ready, apply the shared [earned-media preflight](../docs/earned-media-preflight.md). Hard failures remain `REJECT`; material unknowns remain `NEEDS_REVIEW`. Never average a failed gate into a numeric score.

## Experiment learning

For repeated campaigns, use the [experiment-learning record](../docs/experiment-learning.md) to change one material variable when practical and distinguish replies, declines, source-request acceptance, independent reporting, syndication, and paid/distributed outcomes. Keep real campaign records local/user-owned.

## Final review card

Before returning a pitch, require every answer to these questions:

- Can a reader verify the news peg, date, method, scope, and limitation?
- Is the target's current role and recent work evidenced by a first-party route?
- Does the first paragraph explain why this recipient's audience benefits now?
- Is there one useful asset or source and one concrete, low-friction ask?
- Are representation, paid/distributed status, embargo, and uncertainty clear?
- Is the language, honorific, timezone, channel, and follow-up cadence native to the selected market?
- Are contact provenance and every material claim recorded?
- Is the artifact still a draft awaiting the user's explicit external-action authorization?
