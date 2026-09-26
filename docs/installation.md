# Installation

The install commands below use the public repository; no GitHub authentication is required.

Publicist Skills contains five independent country skills for United States media in English, Germany, mainland China, Japan, and Brazil, 36 optional platform companions that add depth for a single market, and five independent cross-market marketing skills. The CLI method requires Node.js and `npx`.

## Install with the Skills CLI

Pick one command to install a country skill. Cross-market commands follow the country list.

```bash
npx skills add shy-tangerine/publicist-skills --skill publicist-us --global --yes
npx skills add shy-tangerine/publicist-skills --skill publicist-germany --global --yes
npx skills add shy-tangerine/publicist-skills --skill publicist-china --global --yes
npx skills add shy-tangerine/publicist-skills --skill publicist-japan --global --yes
npx skills add shy-tangerine/publicist-skills --skill publicist-brazil --global --yes

# Cross-market conversion, launch, pricing, signup, and social skills
npx skills add shy-tangerine/publicist-skills --skill cro --global --yes
npx skills add shy-tangerine/publicist-skills --skill launch-economics --global --yes
npx skills add shy-tangerine/publicist-skills --skill pricing --global --yes
npx skills add shy-tangerine/publicist-skills --skill signup --global --yes
npx skills add shy-tangerine/publicist-skills --skill social --global --yes
```

Start a new agent session after installation so the client refreshes skill discovery. To verify installation, ask the new session to use the installed skill by name and confirm it loads the matching market workflow before providing live data.

## Skill package and optional companion wiki

The installer copies only the selected skill directory: `SKILL.md`, `references/`, `scripts/`, `assets/`, and agent metadata. It does not copy the repository-level [`wiki/`](../wiki/), READMEs, or other project files.

The wiki is optional companion documentation. Each `SKILL.md` contains the complete core workflow; its installed references cover the market's providers, law and ethics, strategy, and source map. When deeper historical or comparative context would materially improve the work, the agent may use the companion-wiki pointer and available authenticated GitHub access to retrieve relevant articles. The normal workflow never depends on wiki access.

## Manual installation

Clients that discover Agent Skills from a local skills directory can use manual installation. Copy the complete package from [`skills/`](../skills/) into the skills directory documented by the client. Keep `SKILL.md`, `references/`, `scripts/`, `assets/` when present, and `agents/` together so conditional market references and metadata remain available.

## Choose a skill

| Work | Skill |
|---|---|
| United States media and source-request workflow | `$publicist-us` |
| Germany or German newsroom workflow | `$publicist-germany` |
| Mainland China or Simplified Chinese newsroom workflow | `$publicist-china` |
| Japan or Japanese newsroom workflow | `$publicist-japan` |
| Brazil or natural Brazilian Portuguese | `$publicist-brazil` |
| Conversion-rate optimization | `$cro` |
| Launch revenue and unit economics | `$launch-economics` |
| Pricing, packaging, and monetization | `$pricing` |
| Signup and registration-flow optimization | `$signup` |
| Social content, scheduling, and listening | `$social` |

For a supported country in a multi-market project, use the country skill for local research and drafting. The base skill is for the United States, not a general English-language or worldwide fallback. The five cross-market skills can be used independently for their named marketing workflows.

Platform skills such as `$publicist-us-wire-services` or `$publicist-brazil-whatsapp-pitch` are optional add-ons for one market. Install one only after its country skill; the index at `skills/publicist-<market>-platforms-index.md` lists the available companions.

## Tool compatibility

The core research and drafting instructions require no server, API key, database, or runtime. Web research tools, provider APIs, media databases, CRMs, email, messaging, and storage are optional integrations with separate authorization requirements. Installing a skill or connecting a tool does not authorize data acquisition or outreach.

Each country package adds local legal, platform, language, and newsroom checks to the shared safety boundary. Unresolved legal or policy questions return `NEEDS_REVIEW`; the skills do not provide legal advice.

## Update

Skills CLI users rerun the same `npx skills add` command to refresh the installed skill. Manual users pull or download the repository again and recopy the selected complete directory, including `scripts/`. Start a new agent session afterward.

## Client install and updates

Manual installs copy the complete selected directory from [`skills/`](../skills/) and keep `SKILL.md`, `references/`, `assets/`, `agents/`, and `scripts/` together. The scripts are optional helpers; core research and drafting need no runtime.

| Client | Install or update | Official guidance | Support |
|---|---|---|---|
| Skills CLI | `npx skills add shy-tangerine/publicist-skills --skill publicist-us --global --yes` (rerun to update) | [skills.sh](https://skills.sh/) | Verified convention |
| Claude Code | Copy the selected skill directory to `~/.claude/skills/<skill-name>/` (global) or `.claude/skills/<skill-name>/` (project) | [Supported agents](https://github.com/vercel-labs/skills#supported-agents) | Convention verified; runtime untested |
| Codex | Copy the selected skill directory to `~/.agents/skills/<skill-name>/` (user) or `.agents/skills/<skill-name>/` (project) | [Codex skills](https://learn.chatgpt.com/docs/build-skills) | Convention verified; runtime untested |

Use the selected directory name, such as `publicist-us`, in place of `<skill-name>`.

First run: install `$publicist-us` and provide this brief: “Organization: [organization]. Story/news change: [what happened]. Primary evidence: [URL]. Market: [US region/audience]. Output: three verified candidates with fit notes and source URLs; flag missing facts.” In a multi-market project, repeat with the country skills in this order: United States, Germany, mainland China, Japan, Brazil.
