# Earned-media preflight

Use this card after discovery and before treating outreach as draft-ready. It summarizes the existing hard gates; it does not replace market-specific law, provider, or language guidance.

| Gate | PASS requires |
|---|---|
| Identity | Current journalist/desk/account identity is verified from a first-party or authorized source |
| Editorial fit | Recent relevant work or an explicit live request supports the beat/format fit |
| Geography | The target and story satisfy every geographic requirement |
| Timing | Deadline and timezone are known and still actionable |
| Route | A professional route is known and its provenance is recorded |
| Hard requirements | Every stated must-have passes |
| Claims | Every material claim maps to supplied or verified evidence |
| Disclosure | Representation, commercial interest, paid/distributed status and embargo are clear where applicable |
| Data/contact permission | Collection/use is within the published route, provider terms and market-specific gate |
| Language/channel | The draft can follow the recipient's language, naming, honorific and channel conventions |
| Legal/provider uncertainty | No unresolved issue materially blocks the requested action |

Decision rules are deliberately non-numeric:

- Any confirmed failed hard requirement → `REJECT`.
- Any material unknown in a required gate → `NEEDS_REVIEW`.
- All required gates pass → `DRAFT_ALLOWED`.
- `DRAFT_ALLOWED` authorizes drafting only. Sending/publishing remains a separate external action.

Suggested machine-readable card:

```json
{"decision":"NEEDS_REVIEW","gates":{"identity":"PASS","editorial_fit":"PASS","geography":"PASS","timing":"PASS","route":"UNKNOWN","hard_requirements":"PASS","claims":"PASS","disclosure":"PASS","data_contact_permission":"UNKNOWN","language_channel":"PASS","legal_provider_uncertainty":"UNKNOWN"},"missing":["published route","contact-use permission"]}
```
