# Publicist China, platform skills index

**Parent**. `publicist-china` (core workflow)
**Purpose**. Modular platform-specific skills for mainland China earned media. Load only what you need.

---

## Platform skills (commercial/editorial engagement)

| Skill | Platform | Use When |
|---|---|---|
| `publicist-china-wechat` | 微信公众号 | Targeting WeChat accounts for editorial/企业供稿/付费合作/分发 |
| `publicist-china-xiaohongshu` | 小红书 | Targeting 小红书 for editorial or commercial placement |
| `publicist-china-zhihu` | 知乎 | Targeting 知乎 for expert positioning or editorial |
| `publicist-china-douyin` | 抖音 | Targeting 抖音 for commercial/editorial video |
| `publicist-china-bilibili` | B站 | Targeting B站 for long-form commercial/editorial |

---

## Infrastructure skills (cross-platform)

| Skill | Purpose | Use When |
|---|---|---|
| `publicist-china-prnasia` | 美通社/Cision/ProfNet | Distributing press releases, accessing media DB, ProfNet China |
| `publicist-china-distribution` | Wechatsync multi-platform sync | Syncing drafted content to 29+ CN platforms via Chrome/CLI/MCP |
| `publicist-china-guanxi` | 关系/人情 operational protocols | Building journalist relationships: WeChat etiquette, meetings, gifts, face |

---

## Compliance skills (mandatory gates)

| Skill | Regulation | Trigger |
|---|---|---|
| `publicist-china-ai-compliance` | AI标识办法 (2025-09-01) | Any pitch/content contains AI-generated segments |
| `publicist-china-pipl` | PIPL 跨境传输 | Journalist/contact data leaves China or enters overseas CRM/model |

---

## Loading guidance

```python
# Minimal: Core workflow only
$publicist-china

# Target WeChat + compliance
$publicist-china + $publicist-china-wechat + $publicist-china-ai-compliance + $publicist-china-pipl

# Full commercial campaign
$publicist-china + $publicist-china-wechat + $publicist-china-xiaohongshu + $publicist-china-douyin + $publicist-china-distribution + $publicist-china-guanxi + $publicist-china-ai-compliance + $publicist-china-pipl

# PR wire distribution
$publicist-china + $publicist-china-prnasia
```

## Reference docs (in parent skill `references/`)
- `contact-providers.md`, all channel rules (updated 2024-25)
- `law-and-ethics.md`, PIPL, advertising, platform rules, sensitive sectors
- `strategy.md`, narrative scenarios, launch paths, expert strategy, WeChat strategy
- `sources.md`, government/legal sources + platform commercial rules (to update)
- `provider-adapters.md`, runbook for provider wizard
- `companion-wiki.md`, pointer to wiki deep-dives

## What stays in parent skill (`publicist-china/SKILL.md`)
- Core workflow (8 steps: Discover → Verify → Qualify → Contact → Angle → Draft → Check → Return)
- Decision gates (REJECT/NEEDS_REVIEW/DRAFT_ALLOWED)
- Output schema
- Provider policy references
- Tool scope boundaries

## What moved to platform skills
- Platform-specific commercial rules (互选/蒲公英/知+/星图/花火)
- Platform-specific pitch protocols (WeChat-first, 蒲公英报备, 知乎禁引流, etc.)
- Platform-specific content formats
- Platform-specific compliance checklists

## What stays as reference only (no skill)
- MediaCrawler / NanmiCoder, study only, legal gray zone
- 美通社/牛媒数据 official UIs, no automation
- 记者证查询 `press.nppa.gov.cn`, manual verification step
