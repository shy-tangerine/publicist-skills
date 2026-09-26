# Publicist US, platform skills index

**Parent**. `publicist-us` (core workflow)
**Purpose**. Modular platform/functional skills for US earned media. Load only what you need.

---

## Platform/Channel skills (distribution & access)

| Skill | Channel | Use When |
|---|---|---|
| `publicist-us-local-broadcast` | 210 DMAs, TV/radio assignment desks | Targeting local TV/radio for earned media |
| `publicist-us-regional-media` | 50 states + DC newspapers, business journals, TV/radio | Targeting specific US states/regions |
| `publicist-us-trade-verticals` | Top 20 B2B verticals, key publications | Targeting industry-specific earned media |
| `publicist-us-wire-services` | PR Newswire, Business Wire, GlobeNewswire, PRWeb, EIN, PR Underground | Choosing wire distribution service |
| `publicist-us-journalist-platforms` | Qwoted, HARO, SourceBottle, ProfNet, JournoRequests | Using source-request platforms |
| `publicist-us-freelancer-pitch` | Freelancer/contributor protocol (30-50% of bylines) | Targeting freelance journalists |
| `publicist-us-crisis-playbook` | US crisis cycle (Twitter → cable → wire → print) | Managing US earned media crises |
| `publicist-us-local-seo` | Google News, Publisher Center, Core Web Vitals, Discover | Optimizing earned media for search |
| `publicist-us-state-government` | 50 states + DC press offices, FOIA/FOIL, accreditation | Targeting state government earned media |

---

## Compliance skills (mandatory gates)

| Skill | Regulation | Trigger |
|---|---|---|
| `publicist-us-compliance` | CAN-SPAM, FTC, SEC Reg FD, state privacy (CCPA/CPRA, VCDPA, CPA, CTDPA, UCPA) | **Every** US earned media activity, mandatory compliance gate |

---

## Loading guidance

```python
# Minimal: Core workflow only
$publicist-us

# Wire distribution + compliance
$publicist-us + $publicist-us-wire-services + $publicist-us-compliance

# Local broadcast + compliance
$publicist-us + $publicist-us-local-broadcast + $publicist-us-compliance

# Regional targeting + compliance
$publicist-us + $publicist-us-regional-media + $publicist-us-compliance

# Trade verticals + compliance
$publicist-us + $publicist-us-trade-verticals + $publicist-us-compliance

# Journalist platforms + compliance
$publicist-us + $publicist-us-journalist-platforms + $publicist-us-compliance

# Full campaign (wire + local + regional + trade + freelancer + crisis + SEO + state gov + compliance)
$publicist-us + $publicist-us-wire-services + $publicist-us-local-broadcast + $publicist-us-regional-media + $publicist-us-trade-verticals + $publicist-us-journalist-platforms + $publicist-us-freelancer-pitch + $publicist-us-crisis-playbook + $publicist-us-local-seo + $publicist-us-state-government + $publicist-us-compliance

# State government relations
$publicist-us + $publicist-us-state-government + $publicist-us-compliance

# Crisis management
$publicist-us + $publicist-us-crisis-playbook + $publicist-us-compliance

# SEO optimization
$publicist-us + $publicist-us-local-seo + $publicist-us-compliance
```

## Reference docs (in parent skill `references/`)
- `contact-providers.md`, Hunter, Clay, Apollo, Featured, MentionMatch, Qwoted, ProfNet, JournoFinder
- `provider-policy.md`, Qwoted AI-ban, Featured, MentionMatch, Source of Sources, JournoFinder
- `provider-adapters.md`, provider wizard runbook
- `law-and-ethics.md`, CAN-SPAM, FTC, SEC Reg FD, state privacy, FCC
- `sources.md`, FTC, SEC, CAN-SPAM, IAPP state tracker, FCC
- `companion-wiki.md`, pointer to wiki deep-dives

## What stays in parent skill (`publicist-us/SKILL.md`)
- Core workflow (assignment → discover → verify → qualify → contact → angle → draft → check → return)
- Decision gates (REJECT/NEEDS_REVIEW/DRAFT_ALLOWED)
- Output schema
- Provider-specific decisions (Featured, Qwoted, MentionMatch, Source of Sources, JournoFinder)
- US pitch templates (`prompts/us.md`)
- Tool scope boundaries

## What moved to platform skills
- **Local Broadcast**. 210 DMAs, assignment desks, booking producers, morning/evening formats
- **Regional Media**. 50 states + DC matrix, top outlets, pauta emails, editorial calendars
- **Trade Verticals**. 20 verticals, key publications, pitch norms, editorial calendars
- **Wire Services**. 6-service comparison, decision tree, enterprise vs SEO tier, Drei-Säulen
- **Journalist Platforms**. Qwoted/HARO/SourceBottle/ProfNet/JournoRequests deep dive
- **Freelancer Pitch**. Freelancer model, pitch protocol, relationship management, rates
- **Crisis Playbook**. US crisis cycle, war room, holding statements, stakeholder matrix
- **Local SEO**. News schema, Publisher Center, CWV, Discover, local pack, GBP
- **State Government**. 50 states + DC press offices, FOIA/FOIL, accreditation, PIO networks
- **Compliance**. CAN-SPAM, FTC, SEC Reg FD, state privacy patchwork, CAN-SPAM template

## What stays as reference only (no skill)
- PR Newswire/Business Wire/GlobeNewswire official UIs, no automation
- Qwoted/HARO/SourceBottle/ProfNet/JournoRequests platforms, manual use
- FCC/SEC/FTC official guides, source documents
- CAN-SPAM/FTC/SEC official docs, source documents
