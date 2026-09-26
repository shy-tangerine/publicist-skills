# Publicist Germany, platform skills index

**Parent**. `publicist-germany` (core workflow)
**Purpose**. Modular platform/functional skills for Germany earned media. Load only what you need.

---

## Platform/Channel skills (distribution & access)

| Skill | Channel | Use When |
|---|---|---|
| `publicist-germany-pressclub` | Presseclubs (BPK, Landes-PK, Fachclubs) | Targeting German press clubs for accreditation, press conferences, venue hire |
| `publicist-germany-wireservice` | Wire services (dpa/ots, zimpel, PR-Gateway) | Distributing press releases via Germany's wire services |
| `publicist-germany-pressrelease` | Service selection guide | Choosing among dpa/ots, news aktuell/zimpel, PR-Gateway, PRNewswire, Business Wire |

---

## Compliance skills (mandatory gates)

| Skill | Regulation | Trigger |
|---|---|---|
| `publicist-germany-compliance` | UWG §7, GDPR/ePrivacy, DDG §5, Pressekodex, DSK Werbung, TDDDG, Abmahnung, CJEU C-654/23 | **Every** Germany earned media activity, mandatory compliance gate |
| `publicist-germany-business-culture` | German business etiquette | Communicating with German journalists, editors, media professionals |

---

## Loading guidance

```python
# Minimal: Core workflow only
$publicist-germany

# Wire distribution + compliance
$publicist-germany + $publicist-germany-wireservice + $publicist-germany-compliance

# Press club route + compliance
$publicist-germany + $publicist-germany-pressclub + $publicist-germany-compliance

# Full campaign (wire + club + direct)
$publicist-germany + $publicist-germany-wireservice + $publicist-germany-pressclub + $publicist-germany-business-culture + $publicist-germany-compliance

# Service selection help
$publicist-germany + $publicist-germany-pressrelease
```

## Reference docs (in parent skill `references/`)
- `contact-providers.md`, zimpel, published routes, secondary enrichment, minimum output
- `law-and-ethics.md`, UWG §7, GDPR, DDG §5, Pressekodex, DSK Werbung, provider uncertainty
- `strategy.md`, Channel selection, startup positioning, timing, criticism resilience
- `sources.md`, UWG §7, DDG §5, Pressekodex, DSK Werbung, DSGVO, DJV, IVW, zimpel
- `provider-adapters.md`, provider wizard runbook
- `companion-wiki.md`, pointer to wiki deep-dives

## What stays in parent skill (`publicist-germany/SKILL.md`)
- Core workflow (assignment → discover → verify → qualify → contact → angle → draft → check → return)
- Decision gates (REJECT/NEEDS_REVIEW/DRAFT_ALLOWED)
- Output schema
- Provider-specific decisions (zimpel primary, published routes, secondary enrichment)
- Tool scope boundaries

## What moved to platform skills
- **Press clubs.** Membership, PR access, protocols, accreditation, and comparison with Japan
- **Wire Services**. 7-service comparison matrix, decision tree, dpa/ots/zimpel/PR-Gateway detail, Drei-Säulen
- **Business Culture**. Du/Sie, Titel, Betreffzeile, E-Mail-Knigge, Timing, Follow-up, Absage, XING/LinkedIn, Presskits, Messen
- **Compliance (Appliance)**. UWG §7/CJEU C-654/23, GDPR cross-border, DDG §5, Pressekodex/DSK, Abmahnung, Checklist
- **Press Release Services**. Service comparison, decision tree, dpa/ots/zimpel/PR-Gateway detail, Drei-Säulen

## What stays as reference only (no skill)
- dpa/ots/zimpel official UIs, no automation
- BPK/Landes-PK accreditation portals, manual
- Journalist contact databases, verify per outlet
- Pressekodex/DSK PDFs, source documents
