# Campaign context

Use this optional, user-owned artifact for substantial or repeated PR assignments. It is a convenience layer, not a prerequisite for one-off work and never authorizes an external action.

## Privacy and retention boundary

Keep real campaign context outside this public repository. Store only the minimum information needed for the assignment, prefer professional/public contact details, and avoid private dossiers, sensitive personal data, credentials, or secrets. The user controls storage, retention, and deletion. Do not upload a real context artifact to Publicist issues, commits, fixtures, or examples.

Treat every value as evidence supplied by the user, not as permission to contact anyone. Re-verify time-sensitive claims, journalist roles, provider rules, deadlines, and routes at use time.

## Suggested format

A JSON object may contain:

- `organization`: approved public facts and representation/disclosure text.
- `approved_claims`: claim, evidence URL or local evidence reference, review date, and optional expiry date.
- `spokespeople`: approved public role, credentials, languages, availability, and topics; omit unnecessary personal details.
- `evidence`: primary/source URLs or user-owned document references.
- `exclusions`: prohibited claims, outlets, people, geographies, or conflicts.
- `embargo`: scope, timezone, release time, and who approved it.
- `prior_contact_suppression`: recipient/outlet, last contact date, outcome, opt-out state, and stop-until date.
- `market_permissions`: market-specific channels, disclosure requirements, legal/editorial review gates, and explicit prohibitions.
- `updated_at`: ISO date for the artifact itself.

Unknown fields stay unknown. Expired claims are not reusable until reviewed.

## How skills consume it

When a campaign-context artifact is supplied, load it before building the assignment fact pack. Use it to prefill only fields it actually supports. The current request overrides stale operational preferences, but it cannot turn an unsupported claim into an approved one or bypass a hard safety, provider, legal, editorial, or external-action gate.

For every reused claim, check its review/expiry state and evidence. Apply exclusions and prior-contact suppression before candidate ranking. Apply market permissions before selecting a channel. Flag conflicts between the artifact and current evidence as `NEEDS_REVIEW`.

Sending, publishing, enrolling contacts, or modifying an external system remains a separate user-authorized action.

## Example

See `examples/campaign-context.example.json`. It is fictional and intentionally contains no real campaign data.
