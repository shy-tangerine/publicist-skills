# Publicist Skills

<p align="center">
  <a href="../../README.md">English</a> ·
  <a href="README.de.md">Deutsch</a> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.pt-BR.md">Português</a>
</p>

<p align="center">
  <img src="../../assets/repository-hero.zh-CN.png" alt="Publicist Skills：面向五个市场的媒体研究与选题提案技能">
</p>

<p align="center">
  <a href="../../skills/publicist-us/SKILL.md"><img alt="49 Agent Skills" src="https://img.shields.io/badge/Agent_Skills-49-102235?style=flat-square&labelColor=111111"></a>
  <a href="../../wiki/index.md"><img alt="45 wiki articles" src="https://img.shields.io/badge/Wiki-45_articles-102235?style=flat-square&labelColor=111111"></a>
  <a href="../../LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-8B5CF6?style=flat-square&labelColor=111111"></a>
  <a href="https://github.com/sponsors/shy-tangerine"><img alt="Sponsor" src="https://img.shields.io/badge/Sponsor-%E2%99%A5-EC4899?style=flat-square&labelColor=111111&logo=githubsponsors&logoColor=white"></a>
</p>

<p align="center">
  <a href="https://github.com/shy-tangerine/publicist-skills"><img alt="GitHub: private preview, authentication required" src="https://img.shields.io/badge/Repository-private%20preview-6B7280?style=flat-square&labelColor=111111"></a>
</p>

Publicist Skills 提供由 49 个 Agent Skill 组成的技能家族。五个国家技能覆盖美国、德国、中国大陆、日本和巴西；36 个可选的平台技能提供单一渠道的深度内容；五个跨市场营销技能覆盖转化率、发布经济学、定价、注册和社交内容；三个公关工作流技能覆盖监测、新闻价值判断和同一媒体的重复联系。按需加载即可。

我开发 Publicist，是因为大多数营销和媒体技能要么过于宽泛，要么集中在社交平台。赢得媒体报道是一项本地化工作：编辑部惯例、联系渠道、法律和可靠的提案方式因市场而异。目标不准的提案浪费的不只是时间和 token，还可能损害发送者的声誉，因此这些技能在设计上保留了必要的细节。

这些技能不包含秘密记者名单，也不是群发工具。它们结合新闻报道证据与已连接的研究工具，整理出简短且经过核验的媒体名单、选题角度和待审核的联系文案。

## 工作方式

各国家技能遵循[共享提示词](../../prompts/shared.md#core-sequence)中的可检查流程；每个 `SKILL.md` 另有本地规则和完成门槛：

1. 将已批准的事实、证据、排除事项和受访者可用时间整理为简报。
2. 通过近期署名报道、编辑部官方渠道、采访需求和已连接的服务商研究候选对象。
3. 记录证据，并返回 `REJECT`、`NEEDS_REVIEW` 或 `DRAFT_ALLOWED`。[美国技能输出约定](../../skills/publicist-us/SKILL.md#output)列出必需字段；可选的 [JSON Schema](../../schemas/opportunity-record.schema.json)用于规范采访需求记录。
4. 只有证据门槛通过后，才起草符合当地市场的角度或提案。根据[安全说明](../../docs/safety-model.md#external-action-boundary)，发送和发布始终是单独操作。

## 工具与边界

优先使用编辑部官方页面和近期作品。以下服务均为可选项；其账户、访问规则和费用与技能本身分开。研究或起草绝不等于授权发送。

| 任务 | 工具 |
|---|---|
| 寻找采访需求和专家供稿机会 | 美国的 [Featured](https://featured.com/)、[Qwoted](https://www.qwoted.com/)、[Source of Sources](https://www.sourceofsources.com/) 和 [MentionMatch](https://mentionmatch.com/)；中国大陆的 [PR Newswire Asia/Cision ProfNet](https://www.prnasia.com/products/media-database/)；巴西的 [Ajor 信息源库目录](https://ajor.org.br/sete-bancos-de-fontes-gratuitos-para-jornalistas/) |
| 寻找媒体和记者 | 美国的 [JournoFinder](https://journofinder.com/)；德国的 [news aktuell zimpel](https://www.newsaktuell.de/zimpel/)；中国大陆的 [Niumedia](https://niumedia.cn/)；日本的 [PRONE/PRM](https://prone.jp/prm) 和 [Foreign Press Center Japan](https://fpcj.jp/en/assistance/fpregcard/)；巴西的 [Knewin/Comunique-se Mailing](https://www.knewin.com/mailing-de-imprensa/)；以及官方团队页面、近期署名报道、编辑部目录和投稿页面 |
| 核实影响范围、报道领域和当地准入规则 | [IVW](https://www.ivw.de/) 和 [德国媒体发现指南](../../wiki/public-relations/germany-media-discovery.md)；[中国大陆媒体发现指南](../../wiki/public-relations/china-media-discovery.md)；[日本新闻协会记者俱乐部指南](https://pressnet.or.jp/english/about/guideline/) 和 [Foreign Press Center Japan](https://fpcj.jp/en/assistance/fpregcard/)；[巴西媒体发现指南](../../wiki/public-relations/brazil-media-discovery.md) |
| 寻找专业联系信息 | [Hunter](https://hunter.io/)、[Clay](https://www.clay.com/) 和 [Apollo](https://www.apollo.io/) 用于美国市场的辅助联系信息补充；德国使用 [news aktuell zimpel](https://www.newsaktuell.de/zimpel/)；中国大陆使用 [PR Newswire Asia/Cision](https://www.prnasia.com/products/media-database/)；日本使用 [PRONE/PRM](https://prone.jp/prm)；巴西使用 [Knewin/Comunique-se Mailing](https://www.knewin.com/mailing-de-imprensa/)；所有市场均优先采用编辑部官方渠道 |

[本地服务提供商 Wiki](../../wiki/public-relations/localized-media-contact-infrastructure.md)说明各系统包含的信息及其证据边界。技能会核实联系信息来源及平台规则；Qwoted 等服务要求回复由人撰写。对于未列出的国家，应先研究当地媒体体系。美国技能不是全球市场的通用替代方案。

## 安装

使用当前 Skills CLI 语法安装一个技能：

```bash
npx skills add shy-tangerine/publicist-skills \
  --skill publicist-us --global --yes
```

将 `publicist-us` 替换为所需软件包：

| 范围 | 技能名称 |
|---|---|
| 国家 | `publicist-us`、`publicist-germany`、`publicist-china`、`publicist-japan`、`publicist-brazil` |
| 跨市场 | `cro`、`launch-economics`、`pricing`、`signup`、`social` |

每个技能均可独立使用。可选平台技能、手动设置和客户端说明见[安装与兼容性](../../docs/installation.md)。

### 服务提供商设置向导

首次使用时，智能体会提供适用于目标市场的服务选择向导。选择一个服务，即可查阅其官方工具或网站的设置和使用说明。此步骤可以跳过。

在仓库的本地副本中运行：

```bash
python3 scripts/provider_wizard.py germany --setup 'news aktuell zimpel'
```

向导只提供说明，不会连接账户。详见[服务设置指南](../../docs/provider-adapters.md)。

## 示例

**简短虚构示例。** 以下组织、记者、媒体和 URL 均为虚构；字段遵循真实的[输出约定](../../skills/publicist-us/SKILL.md#completion-check)。

**输入：** Fernbrook Analytics 将发布一个开源固件安全数据集。仅使用已发布的设备数量和扫描结果；排除入侵叙事及竞品陈述。寻找一位相关的美国记者，并准备提案，但不要发送。

| 字段 | 值 |
|---|---|
| `decision` | `DRAFT_ALLOWED` |
| `journalist_name` | Dana Okafor |
| `recent_work_url` | `example.com/vtl/sbom-gaps`（2026-09-01 查证） |
| `route_provenance` | 官方署名页 → `dokafor@vtl.example` |
| 陈述门槛 | 设备数量已核验；宽泛竞品陈述已删除 |
| 外部操作 | 草稿已保存；未发送任何内容 |

[提示词库](../../prompts/README.md)提供可复用的研究、核验、起草、跟进和更正简报。

## 仓库内容

| 路径 | 内容 |
|---|---|
| [`skills/`](../../skills/) | 五个独立的国家技能、36 个可选的平台技能、五个跨市场营销技能，以及三个公关工作流技能 |
| [`wiki/`](../../wiki/) | 详细的市场和服务提供商研究，附公共原始来源引用 |
| [`schemas/`](../../schemas/) | 可选的机会记录 JSON Schema 及虚构示例 |
| [`docs/`](../../docs/) | 安装、安全、翻译和赞助说明 |
| [`prompts/`](../../prompts/) | 用于研究、核验、选题角度设计和审核的可复用提示词 |
| [`scripts/`](../../scripts/) | 可选的服务提供商设置向导和清单 |

Wiki 优先采用法律、监管机构、新闻评议组织、行业协会、平台规则和编辑部原始指南。在依赖法律或平台相关陈述前，请核对链接来源及其当前版本。

## 安全审计

NVIDIA SkillSpector：**Warn**（仅静态分析，2026-09-21，版本 `b5457eb`）。13 个软件包中的 24 项发现均已逐项审核并判定为误报；未解析的路径样引用使 45 个软件包报告保持不完整，因此汇总结果为 `CAUTION`。扫描覆盖该版本中的 46 个软件包：5 个国家技能、36 个平台伴随技能和 5 个跨市场技能。三个公关工作流技能是在此后加入的。范围与限制见[审计报告](../security-audit.md)。

## 致谢

- [最初的 Instagram 视频](https://www.instagram.com/p/DblOuOGxU1A/)：项目灵感。
- [Writing for Agents](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md)：用于编写技能。
- [Karpathy 的 LLM Wiki 文档](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)：用于构建 Wiki。
- [Wizard](https://github.com/mattpocock/skills/blob/main/skills/engineering/wizard/SKILL.md)：用于设计服务设置流程。

## 参与贡献

在建议新来源、市场流程、提示词或规则修正前，请阅读 [CONTRIBUTING.md](../../CONTRIBUTING.md)。漏洞请按 [SECURITY.md](../../SECURITY.md) 中的说明通过 GitHub 私密漏洞报告渠道提交。

## 赞助

如需洽谈赞助商标志展示，请联系 [shy-tangerine@mailbox.org](mailto:shy-tangerine@mailbox.org)。

赞助用于跟踪来源变化、维护各国流程、兼容性测试和新市场研究。查看[赞助说明](../../docs/SPONSORS.md)，或[赞助 shy-tangerine](https://github.com/sponsors/shy-tangerine)。

## 许可证

MIT。详见 [LICENSE](../../LICENSE)。
