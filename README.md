# Publicist Skills

<p align="center">
  <a href="README.md">English</a> ·
  <a href="docs/i18n/README.de.md">Deutsch</a> ·
  <a href="docs/i18n/README.zh-CN.md">简体中文</a> ·
  <a href="docs/i18n/README.ja.md">日本語</a> ·
  <a href="docs/i18n/README.pt-BR.md">Português</a>
</p>

<p align="center">
  <img src="assets/repository-hero.png" alt="Publicist hero artwork for Publicist Skills on bright newsprint">
</p>

<p align="center">
  <a href="skills/publicist-us/SKILL.md"><img alt="49 Agent Skills" src="https://img.shields.io/badge/Agent_Skills-49-102235?style=flat-square&labelColor=111111"></a>
  <a href="wiki/index.md"><img alt="45 wiki articles" src="https://img.shields.io/badge/Wiki-45_articles-102235?style=flat-square&labelColor=111111"></a>
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-8B5CF6?style=flat-square&labelColor=111111"></a>
  <a href="https://github.com/sponsors/shy-tangerine"><img alt="Sponsor" src="https://img.shields.io/badge/Sponsor-%E2%99%A5-EC4899?style=flat-square&labelColor=111111&logo=githubsponsors&logoColor=white"></a>
</p>

<p align="center">
  <a href="https://github.com/shy-tangerine/publicist-skills"><img alt="GitHub: public" src="https://img.shields.io/badge/Repository-public-2E8B57?style=flat-square&labelColor=111111"></a>
</p>

Publicist Skills is a family of 49 Agent Skills. Five country skills cover the United States, Germany, mainland China, Japan, and Brazil; 36 optional platform skills add per-channel depth; five cross-market marketing skills cover conversion, launch economics, pricing, signup, and social content; and three public-relations workflow skills cover monitoring, newsworthiness, and repeat outreach to the same outlet. Load only what you need.

I built Publicist after finding that most marketing and media skills were either broad or centered on social platforms. Earned media is local: newsroom norms, contact routes, laws, and credible pitching practices change by market. A poorly targeted pitch wastes more than time and tokens; it can damage the sender's reputation, so these skills are detailed by design.

They do not contain a secret journalist list or act as a bulk mailer. They turn newsroom evidence and connected research tools into a short, verified media list, story angles, and outreach ready for review.

## How it works

The country skills follow the inspectable sequence in the [shared prompts](prompts/shared.md#core-sequence), with market-specific rules and completion gates in each `SKILL.md`:

1. Turn your approved facts, evidence, exclusions, and spokesperson availability into a brief.
2. Research candidates through current bylines, official newsroom routes, source requests, and any provider you have connected.
3. Record the evidence and return `REJECT`, `NEEDS_REVIEW`, or `DRAFT_ALLOWED`; the [US output contract](skills/publicist-us/SKILL.md#output) shows the required fields, and the optional [JSON Schema](schemas/opportunity-record.schema.json) formalizes source-request records.
4. Draft a market-appropriate angle or pitch only after the evidence gate passes. Sending and publishing remain separate actions under the [safety model](docs/safety-model.md#external-action-boundary).

## Tools and boundaries

Official newsroom pages and recent work come first. The services below are optional; their accounts, access rules, and costs remain separate from these skills.

Research or drafting never authorizes outreach.

| Task | Tools |
|---|---|
| Find source requests and expert opportunities | [Featured](https://featured.com/), [Qwoted](https://www.qwoted.com/), [Source of Sources](https://www.sourceofsources.com/), and [MentionMatch](https://mentionmatch.com/) in the US; [PR Newswire Asia/Cision ProfNet](https://www.prnasia.com/products/media-database/) in mainland China; [Ajor's source-bank directory](https://ajor.org.br/sete-bancos-de-fontes-gratuitos-para-jornalistas/) in Brazil |
| Find outlets and journalists | [JournoFinder](https://journofinder.com/) in the US; [news aktuell zimpel](https://www.newsaktuell.de/zimpel/) in Germany; [Niumedia](https://niumedia.cn/) in mainland China; [PRONE/PRM](https://prone.jp/prm) and [Foreign Press Center Japan](https://fpcj.jp/en/assistance/fpregcard/) in Japan; [Knewin/Comunique-se Mailing](https://www.knewin.com/mailing-de-imprensa/) in Brazil; plus official staff pages, recent bylines, newsroom directories, and submission pages |
| Check reach, beat, and local access rules | [IVW](https://www.ivw.de/) and the [Germany discovery guide](wiki/public-relations/germany-media-discovery.md); the [mainland China discovery guide](wiki/public-relations/china-media-discovery.md); [Nihon Shinbun Kyokai's press-club guidelines](https://pressnet.or.jp/english/about/guideline/) and [Foreign Press Center Japan](https://fpcj.jp/en/assistance/fpregcard/); the [Brazil discovery guide](wiki/public-relations/brazil-media-discovery.md) |
| Find professional contact details | [Hunter](https://hunter.io/), [Clay](https://www.clay.com/), and [Apollo](https://www.apollo.io/) as secondary US enrichment; [news aktuell zimpel](https://www.newsaktuell.de/zimpel/) in Germany; [PR Newswire Asia/Cision](https://www.prnasia.com/products/media-database/) in mainland China; [PRONE/PRM](https://prone.jp/prm) in Japan; [Knewin/Comunique-se Mailing](https://www.knewin.com/mailing-de-imprensa/) in Brazil; official newsroom routes first in every market |

The [localized-provider wiki](wiki/public-relations/localized-media-contact-infrastructure.md) explains what each system contains and where its evidence stops. The skills check contact provenance and provider rules; services such as Qwoted require human-written replies. For a country not listed here, research the local media system before outreach. The US skill is not a worldwide fallback.

## Install

Install one skill with the current Skills CLI syntax:

```bash
npx skills add shy-tangerine/publicist-skills \
  --skill publicist-us --global --yes
```

Replace `publicist-us` with the package you need:

| Scope | Skill names |
|---|---|
| Country | `publicist-us`, `publicist-germany`, `publicist-china`, `publicist-japan`, `publicist-brazil` |
| Cross-market | `cro`, `launch-economics`, `pricing`, `signup`, `social` |

Each skill works on its own. Optional platform companions and manual/client-specific setup are covered in [installation and compatibility](docs/installation.md).

### Provider setup wizard

At first use, the agent offers a wizard for providers in your market. Pick one to get setup and usage guidance for its official tools or website. You can skip this step.

From a repository checkout:

```bash
python3 scripts/provider_wizard.py germany --setup 'news aktuell zimpel'
```

The wizard points to instructions; it doesn't connect accounts. See the [provider setup guide](docs/provider-adapters.md) for details.

## Example

**Short fictional example.** The organization, journalist, outlet, and URLs below are invented; the fields follow the real [output contract](skills/publicist-us/SKILL.md#completion-check).

**Input:** Fernbrook Analytics is releasing an open-source firmware-security dataset. Use only the published device count and scan results; exclude breach framing and competitor claims. Find one relevant US journalist and prepare, but do not send, a pitch.

| Field | Value |
|---|---|
| `decision` | `DRAFT_ALLOWED` |
| `journalist_name` | Dana Okafor |
| `recent_work_url` | `example.com/vtl/sbom-gaps` (observed 2026-09-01) |
| `route_provenance` | Official byline page → `dokafor@vtl.example` |
| Claim gate | Device count verified; broad competitor claim removed |
| External action | Draft stored; nothing sent |

The [prompt library](prompts/README.md) contains reusable briefs for research, verification, drafting, follow-up, and correction work.

## Repository contents

| Path | Contents |
|---|---|
| [`skills/`](skills/) | Five self-contained country skills, 36 optional platform companions, five cross-market marketing skills, and three public-relations workflow skills |
| [`wiki/`](wiki/) | Detailed market and provider research with citations to original public sources |
| [`schemas/`](schemas/) | Optional opportunity-record schema and fictional example |
| [`docs/`](docs/) | Installation, safety, translations, and sponsorship |
| [`prompts/`](prompts/) | Reusable prompts for research, verification, angles, and review |
| [`scripts/`](scripts/) | Optional offline provider setup wizard and inventory |

The wiki favors laws, regulators, press councils, professional associations, platform rules, and original newsroom guidance. Check the linked source and its current version before relying on a legal or platform claim.

## Security audits

NVIDIA SkillSpector: **Warn** (static-only, 2026-09-21, revision `b5457eb`). Twenty-four findings across 13 packages were reviewed individually as false positives; unresolved path-like references leave 45 package reports partial, so the aggregate remains `CAUTION`. The scan covers the 46 packages present at that revision: five country skills, 36 platform companions, and five cross-market skills. It predates the three public-relations workflow skills. See the [audit report](docs/security-audit.md) for scope and limitations.

## Credits

- [Original Instagram reel](https://www.instagram.com/p/DblOuOGxU1A/): project inspiration.
- [Writing for Agents](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md): used for the skills.
- [Karpathy's LLM wiki document](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): used for the wiki.
- [Wizard](https://github.com/mattpocock/skills/blob/main/skills/engineering/wizard/SKILL.md): used for provider setup.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a new source, market workflow, prompt, or policy correction. Report vulnerabilities through GitHub private vulnerability reporting as described in [SECURITY.md](SECURITY.md).

## Sponsorship

For logo placement inquiries, email [shy-tangerine@mailbox.org](mailto:shy-tangerine@mailbox.org).

Sponsorship funds source monitoring, country-workflow maintenance, compatibility testing, and new market research. See [sponsorship](docs/SPONSORS.md) or [sponsor shy-tangerine](https://github.com/sponsors/shy-tangerine).

## License

MIT. See [LICENSE](LICENSE).

Python tooling: use `uv lock --check`, `uv sync --locked`, and `uv run python scripts/<script>.py` for repository scripts. The Python tools are not the published app.
