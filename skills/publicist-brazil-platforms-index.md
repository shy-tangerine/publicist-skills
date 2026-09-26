# Publicist Brazil, platform skills index

**Parent**. `publicist-brazil` (core workflow)
**Purpose**. Modular platform/functional skills for Brazil earned media. Load only what you need.

---

## Platform/Channel skills (distribution & access)

| Skill | Channel | Use When |
|---|---|---|
| `publicist-brazil-regional-media` | 27 states + DF media matrix | Targeting specific Brazilian states/regions |
| `publicist-brazil-wire-services` | Wire services (DCI, PrNewswire, agencies) | Choosing distribution service for Brazil |
| `publicist-brazil-whatsapp-pitch` | WhatsApp communication | Pitching/following up with Brazilian journalists via WhatsApp |
| `publicist-brazil-assessoria-culture` | Agency intermediary model | Working with/as Brazilian PR agency |

---

## Compliance skills (mandatory gates)

| Skill | Regulation | Trigger |
|---|---|---|
| `publicist-brazil-lgpd-compliance` | LGPD, ANPD, Marco Civil, CDC | **Every** Brazil earned media activity, mandatory compliance gate |

---

## Loading guidance

```python
# Minimal: Core workflow only
$publicist-brazil

# Regional targeting + compliance
$publicist-brazil + $publicist-brazil-regional-media + $publicist-brazil-lgpd-compliance

# Wire distribution + compliance
$publicist-brazil + $publicist-brazil-wire-services + $publicist-brazil-lgpd-compliance

# Full campaign (regional + wire + WhatsApp + assessoria + compliance)
$publicist-brazil + $publicist-brazil-regional-media + $publicist-brazil-wire-services + $publicist-brazil-whatsapp-pitch + $publicist-brazil-assessoria-culture + $publicist-brazil-lgpd-compliance

# Agency partnership
$publicist-brazil + $publicist-brazil-assessoria-culture + $publicist-brazil-lgpd-compliance
```

## Reference docs (in parent skill `references/`)
- `contact-providers.md`, DCI, In Press, Primeiro Plano, PrNewswire, assessoria agencies
- `law-and-ethics.md`, LGPD, Marco Civil, CDC, ANPD, Marco Civil data retention
- `strategy.md`, Regional approach, assessoria model, WhatsApp cadence, crisis
- `sources.md`, ANPD, LGPD, Marco Civil, CDC, FENAJ, ABRAPCOM, CONRERP
- `provider-adapters.md`, provider wizard runbook
- `companion-wiki.md`, pointer to wiki deep-dives

## What stays in parent skill (`publicist-brazil/SKILL.md`)
- Core workflow (assignment → discover → verify → qualify → contact → angle → draft → check → return)
- Decision gates (REJECT/NEEDS_REVIEW/DRAFT_ALLOWED)
- Output schema
- Provider-specific decisions (DCI primary, published routes, assessoria agencies)
- Portuguese search query templates
- Tool scope boundaries

## What moved to platform skills
- **Regional Media**. 27 states + DF matrix, top outlets, pauta emails, editorial calendars, WhatsApp contacts
- **Wire Services**. 6-service comparison (DCI, agencies, PrNewswire, Business Wire, GlobeNewswire, budget), decision tree
- **WhatsApp Pitch**. Etiquette, áudio vs texto, follow-up cadence, LGPD opt-out, scheduling, crisis
- **Assessoria Culture**. Agency model, briefing templates, follow-up cadence, crisis coordination, billing
- **LGPD Compliance**. LGPD/ANPD gate, cross-border triggers, SCC/TIA, ANPD enforcement, local-first principle

## What stays as reference only (no skill)
- DCI/PrNewswire/agency official UIs, no automation
- Journalist contact databases, verify per outlet
- ANPD official guides, source documents
- LGPD/SCC PDFs, source documents
