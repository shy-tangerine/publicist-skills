# Publicist documentation

This directory contains the public documentation for the Publicist Skills packages.

## Structure

```
docs/
├── README.md                    # This file
├── installation.md              # Installation guide
├── provider-adapters.md         # Provider adapter reference
├── safety-model.md              # Safety model documentation
├── security-audit.md            # Security audit documentation
├── i18n/                        # Internationalization
│   ├── README.de.md             # German
│   ├── README.ja.md             # Japanese
│   ├── README.zh-CN.md          # Chinese
│   └── README.pt-BR.md          # Portuguese (Brazil)
└── SPONSORS.md                  # Sponsors
```

## Skills

The repository ships 46 packages: five self-contained country skills, 36 optional single-market platform companions, and five cross-market marketing skills.

| Market | Country skill | Platform companions | Index |
|---|---|---|---|
| United States | `publicist-us` | 10 | [`skills/publicist-us-platforms-index.md`](../skills/publicist-us-platforms-index.md) |
| Germany | `publicist-germany` | 5 | [`skills/publicist-germany-platforms-index.md`](../skills/publicist-germany-platforms-index.md) |
| Mainland China | `publicist-china` | 10 | [`skills/publicist-china-platforms-index.md`](../skills/publicist-china-platforms-index.md) |
| Japan | `publicist-japan` | 6 | [`skills/publicist-japan-platforms-index.md`](../skills/publicist-japan-platforms-index.md) |
| Brazil | `publicist-brazil` | 5 | [`skills/publicist-brazil-platforms-index.md`](../skills/publicist-brazil-platforms-index.md) |

Each country skill carries the complete default workflow in its `SKILL.md` plus conditional references for providers, law and ethics, strategy, and source maps. Platform companions are single-file reference skills; install one only after its country skill, and only when its channel matters to you.

### Cross-market packages

These packages are independent of the country and platform skills:

| Package | Focus |
|---|---|
| `cro` | Conversion-rate optimization |
| `launch-economics` | Launch revenue and unit economics |
| `pricing` | Pricing, packaging, and monetization |
| `signup` | Signup and registration-flow optimization |
| `social` | Social content, scheduling, and listening |

## Provider documentation

Provider guides live in `wiki/public-relations/providers/`:

- US: featured.md, qwoted.md, source-of-sources.md, mentionmatch.md, journofinder.md
- Germany: zimpel.md, ivw.md, impressum.md
- China: pr-newswire-asia.md, cision.md, profnet.md, niumedia.md, wechat.md
- Japan: prone.md, fpcj.md, kyodo-news-pr-wire.md
- Brazil: knewin.md, comunique-se.md, ajor.md, whatsapp-professional-routes.md
- Cross-market: hunter.md, clay.md, apollo.md

## Provider setup wizard

Each provider above has an offline wizard script in [`scripts/wizards/`](../scripts/wizards/) that points to the provider's own setup and usage guidance:

```sh
python3 scripts/provider_wizard.py us --setup Qwoted
```

The wizard points to instructions; it does not connect accounts. See [provider-adapters.md](provider-adapters.md) for the selector contract and boundaries.

## Market research

The companion wiki in [`wiki/`](../wiki/index.md) holds dated articles with direct links to original sources:

- United States: [outreach workflow](../wiki/public-relations/us-outreach-workflow.md)
- Germany: [media discovery](../wiki/public-relations/germany-media-discovery.md), [legal outreach](../wiki/public-relations/germany-legal-outreach.md), [data handling](../wiki/public-relations/germany-data-handling.md), [newsroom ethics](../wiki/public-relations/germany-newsroom-ethics.md), [pitch workflow](../wiki/public-relations/germany-pitch-workflow.md)
- Mainland China: [media discovery](../wiki/public-relations/china-media-discovery.md), [advertising and WeChat](../wiki/public-relations/china-advertising-and-wechat.md), [data and cross-border](../wiki/public-relations/china-data-and-cross-border.md), [outreach workflow](../wiki/public-relations/china-outreach-workflow.md)
- Japan: [press clubs and foreign access](../wiki/public-relations/japan-press-clubs-and-foreign-access.md), [media ethics and disclosure](../wiki/public-relations/japan-media-ethics-and-disclosure.md), [personal data and email law](../wiki/public-relations/japan-personal-data-and-email-law.md), [PR wire and release quality](../wiki/public-relations/japan-pr-wire-and-release-quality.md), [outreach workflow](../wiki/public-relations/japan-outreach-workflow.md)
- Brazil: [media discovery](../wiki/public-relations/brazil-media-discovery.md), [data and LGPD](../wiki/public-relations/brazil-data-and-lgpd.md), [newsroom ethics](../wiki/public-relations/brazil-newsroom-ethics.md), [outreach workflow](../wiki/public-relations/brazil-outreach-workflow.md)
- Cross-market: [localized media contact infrastructure](../wiki/public-relations/localized-media-contact-infrastructure.md), [contact data and outreach providers](../wiki/public-relations/contact-data-and-outreach-providers.md), [media environment comparison](../wiki/public-relations/media-environment-comparison.md)

## License

MIT. See [LICENSE](../LICENSE).
