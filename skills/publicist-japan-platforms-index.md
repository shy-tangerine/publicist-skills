# Publicist Japan, platform skills index

**Parent**. `publicist-japan` (core workflow)
**Purpose**. Modular platform/functional skills for Japan earned media. Load only what you need.

---

## Platform/Channel skills (distribution & access)

| Skill | Channel | Use When |
|---|---|---|
| `publicist-japan-kishaclub` | 記者クラブ (Press Clubs) | Targeting Japanese press clubs for 投げ込み, レク付き配布, 記者会見 |
| `publicist-japan-prwire` | 共同通信PRワイヤー (Kyodo News PR Wire) | Distributing press releases via Japan's premier wire service |
| `publicist-japan-fpcj` | 外国人記者センター (FPCJ) | Foreign company needs official Japan media access |
| `publicist-japan-pressrelease` | Domestic wire services comparison | Choosing among PR TIMES, @Press, ValuePress, 共同通信PRワイヤー, Dream News, Digital PR Platform |

---

## Compliance skills (mandatory gates)

| Skill | Regulation | Trigger |
|---|---|---|
| `publicist-japan-compliance` | APPI, 特定電子メール法, 景品表示法, 業法, PRSJ指針, 日本心理学会指針 | **Every** Japan earned media activity, mandatory compliance gate |
| `publicist-japan-business-culture` | Japanese business etiquette | Communicating with Japanese journalists, editors, media professionals |

---

## Loading guidance

```python
# Minimal: Core workflow only
$publicist-japan

# Wire distribution + compliance
$publicist-japan + $publicist-japan-prwire + $publicist-japan-compliance

# Press club route + compliance
$publicist-japan + $publicist-japan-kishaclub + $publicist-japan-compliance

# Foreign company entry
$publicist-japan + $publicist-japan-fpcj + $publicist-japan-business-culture + $publicist-japan-compliance

# Full campaign (wire + club + direct)
$publicist-japan + $publicist-japan-prwire + $publicist-japan-kishaclub + $publicist-japan-business-culture + $publicist-japan-compliance

# Service selection help
$publicist-japan + $publicist-japan-pressrelease
```

## Reference docs (in parent skill `references/`)
- `contact-providers.md`, PRONE/PRM, what's not established, minimum output
- `law-and-ethics.md`, APPI, email/platform rules, transparency, escalation points
- `strategy.md`, media system, relationship-first, foreign startups, timing, anti-patterns
- `sources.md`, 日本新聞協会, 外務省, PPC, APPI, 特定電子メール法, 共同通信PRワイヤー, PRONE, 日本心理学会, JETRO
- `provider-adapters.md`, provider wizard runbook
- `companion-wiki.md`, pointer to wiki deep-dives

## What stays in parent skill (`publicist-japan/SKILL.md`)
- Core workflow (classify target → discover → verify identity/scope → qualify fit → handle contacts → develop angle → draft Japanese → check platform/data → return)
- Decision gates (REJECT/NEEDS_REVIEW/DRAFT_ALLOWED)
- Output schema
- Provider-specific decisions (PRONE, contact providers, provider adapters)
- 日本語検索クエリテンプレート
- Tool scope boundaries

## What moved to platform skills
- **Kisha Club**. Club types, 投げ込み手順, 幹事社协调, レク付き配布, 記者会見, アクセス制限
- **PR Wire**. 共同通信PRワイヤー料金/審査/チャネル, ワイヤーvsクラブvs直接の使い分け
- **FPCJ**. 外国記者登録証, 取材アレンジ, プレスツアー, 会見支援, 外企エントリーポイント
- **Press Release Services**. 6社比較マトリクス, 決定木, スタートアップ特典, 三位一体戦略
- **Business Culture**. 名刺交換, アポイント, メール件名/本文/タイミング, フォローアップ, 断り方, お礼, 季節挨拶, 禁忌
- **Compliance (Appliance)**. APPI越境トリガー/最省力経路, 特定電子メール法実務テンプレート, 景品表示法クレーム検証, 業法クイックリファレンス, PRSJ/心理学会指針, 差分チェックリスト

## What stays as reference only (no skill)
- MediaCrawler等クローラー, 研究のみ、法的グレーゾーン
- PRONE/PRM 公式UI, 自動化なし
- 外国記者登録証申請, 企業が記者をスポンサー
- 記者クラブ会員名簿, クラブごとに確認
