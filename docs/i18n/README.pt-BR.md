# Publicist Skills

<p align="center">
  <a href="../../README.md">English</a> ·
  <a href="README.de.md">Deutsch</a> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.pt-BR.md">Português</a>
</p>

<p align="center">
  <img src="../../assets/repository-hero.pt-BR.png" alt="Publicist Skills: Skills para pesquisa de mídia e estratégia de pautas em cinco mercados">
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

Publicist Skills reúne uma família de 49 Agent Skills. Cinco skills de país cobrem Estados Unidos, Alemanha, China continental, Japão e Brasil; 36 skills de plataforma opcionais adicionam profundidade por canal; cinco skills de marketing cross-market cobrem conversão, economia de lançamentos, preços, cadastro e conteúdo social; e três skills de fluxo de trabalho de relações públicas cobrem monitoramento, noticiabilidade e novos contatos com o mesmo veículo. Você carrega apenas o que precisa.

Criei o Publicist depois de perceber que a maioria dos skills de marketing e mídia era ampla demais ou centrada em plataformas sociais. Earned media é local: costumes das redações, canais de contato, leis e boas práticas de pitch mudam de um mercado para outro. Um pitch mal direcionado desperdiça mais do que tempo e tokens; também pode prejudicar a reputação de quem envia. Por isso, estes skills são detalhados de propósito.

Eles não contêm uma lista secreta de jornalistas nem funcionam como disparador em massa. A partir de evidências editoriais e ferramentas de pesquisa conectadas, produzem uma lista curta de contatos verificados, ângulos de pauta e mensagens prontas para revisão.

## Como funciona

Os skills de país seguem a sequência verificável dos [prompts compartilhados](../../prompts/shared.md#core-sequence), com regras locais e critérios de conclusão em cada `SKILL.md`:

1. Transformam fatos aprovados, evidências, exclusões e disponibilidade do porta-voz em um briefing.
2. Pesquisam candidatos em matérias recentes, canais oficiais das redações, pedidos de fontes e provedores conectados.
3. Registram as evidências e retornam `REJECT`, `NEEDS_REVIEW` ou `DRAFT_ALLOWED`. O [contrato de saída dos EUA](../../skills/publicist-us/SKILL.md#output) mostra os campos obrigatórios; o [JSON Schema](../../schemas/opportunity-record.schema.json) opcional formaliza registros de pedidos de fontes.
4. Só depois do gate de evidências redigem um ângulo ou pitch adequado ao mercado. Envio e publicação continuam sendo ações separadas pelo [modelo de segurança](../../docs/safety-model.md#external-action-boundary).

## Ferramentas e limites

Páginas oficiais das redações e trabalhos recentes vêm primeiro. Os serviços abaixo são opcionais; contas, regras de acesso e custos permanecem separados dos skills. Pesquisa ou redação nunca autorizam o envio.

| Tarefa | Ferramentas |
|---|---|
| Encontrar pedidos de fontes e oportunidades para especialistas | [Featured](https://featured.com/), [Qwoted](https://www.qwoted.com/), [Source of Sources](https://www.sourceofsources.com/) e [MentionMatch](https://mentionmatch.com/) nos EUA; [PR Newswire Asia/Cision ProfNet](https://www.prnasia.com/products/media-database/) na China continental; [diretório de bancos de fontes da Ajor](https://ajor.org.br/sete-bancos-de-fontes-gratuitos-para-jornalistas/) no Brasil |
| Encontrar veículos e jornalistas | [JournoFinder](https://journofinder.com/) nos EUA; [news aktuell zimpel](https://www.newsaktuell.de/zimpel/) na Alemanha; [Niumedia](https://niumedia.cn/) na China continental; [PRONE/PRM](https://prone.jp/prm) e [Foreign Press Center Japan](https://fpcj.jp/en/assistance/fpregcard/) no Japão; [Knewin/Comunique-se Mailing](https://www.knewin.com/mailing-de-imprensa/) no Brasil; além de páginas oficiais das equipes, matérias recentes, diretórios de redações e páginas de envio |
| Verificar alcance, editoria e regras locais de acesso | [IVW](https://www.ivw.de/) e [guia de pesquisa na Alemanha](../../wiki/public-relations/germany-media-discovery.md); [guia de pesquisa na China continental](../../wiki/public-relations/china-media-discovery.md); [diretrizes de clubes de imprensa da Nihon Shinbun Kyokai](https://pressnet.or.jp/english/about/guideline/) e [Foreign Press Center Japan](https://fpcj.jp/en/assistance/fpregcard/); [guia de pesquisa no Brasil](../../wiki/public-relations/brazil-media-discovery.md) |
| Encontrar contatos profissionais | [Hunter](https://hunter.io/), [Clay](https://www.clay.com/) e [Apollo](https://www.apollo.io/) como enriquecimento complementar nos EUA; [news aktuell zimpel](https://www.newsaktuell.de/zimpel/) na Alemanha; [PR Newswire Asia/Cision](https://www.prnasia.com/products/media-database/) na China continental; [PRONE/PRM](https://prone.jp/prm) no Japão; [Knewin/Comunique-se Mailing](https://www.knewin.com/mailing-de-imprensa/) no Brasil; os canais oficiais das redações vêm primeiro em todos os mercados |

A [wiki de provedores locais](../../wiki/public-relations/localized-media-contact-infrastructure.md) explica o que cada sistema contém e os limites das evidências. Os skills verificam a origem dos contatos e as regras dos provedores; serviços como Qwoted exigem respostas escritas por pessoas. Para outros países, pesquise primeiro o sistema de mídia local. O skill dos EUA não é uma alternativa mundial.

## Instalação

Instale um skill com a sintaxe atual da Skills CLI:

```bash
npx skills add shy-tangerine/publicist-skills \
  --skill publicist-us --global --yes
```

Troque `publicist-us` pelo pacote desejado:

| Escopo | Nomes dos skills |
|---|---|
| País | `publicist-us`, `publicist-germany`, `publicist-china`, `publicist-japan`, `publicist-brazil` |
| Cross-market | `cro`, `launch-economics`, `pricing`, `signup`, `social` |

Cada skill funciona sozinho. Os skills de plataforma opcionais e a configuração manual ou específica por cliente estão em [instalação e compatibilidade](../../docs/installation.md).

### Assistente de configuração de provedores

No primeiro uso, o agente oferece um assistente com provedores do seu mercado. Escolha um para consultar instruções de configuração e uso das ferramentas oficiais ou do site. Você pode pular esta etapa.

Em uma cópia local do repositório:

```bash
python3 scripts/provider_wizard.py germany --setup 'news aktuell zimpel'
```

O assistente aponta para as instruções; ele não conecta contas. Veja os detalhes no [guia de configuração de provedores](../../docs/provider-adapters.md).

## Exemplo

**Exemplo fictício curto.** A organização, a jornalista, o veículo e as URLs são inventados; os campos seguem o [contrato de saída](../../skills/publicist-us/SKILL.md#completion-check) real.

**Entrada:** A Fernbrook Analytics vai lançar um conjunto de dados aberto sobre segurança de firmware. Use apenas a contagem de dispositivos e os resultados publicados; exclua enquadramento de incidente e afirmações sobre concorrentes. Encontre uma jornalista relevante nos EUA e prepare, sem enviar, um pitch.

| Campo | Valor |
|---|---|
| `decision` | `DRAFT_ALLOWED` |
| `journalist_name` | Dana Okafor |
| `recent_work_url` | `example.com/vtl/sbom-gaps` (observada em 2026-09-01) |
| `route_provenance` | Página oficial de bylines → `dokafor@vtl.example` |
| Gate de afirmações | Contagem de dispositivos verificada; afirmação ampla sobre concorrentes removida |
| Ação externa | Rascunho salvo; nada enviado |

A [biblioteca de prompts](../../prompts/README.md) contém briefings reutilizáveis para pesquisa, verificação, redação, follow-up e correções.

## Conteúdo do repositório

| Caminho | Conteúdo |
|---|---|
| [`skills/`](../../skills/) | Cinco skills de país independentes, 36 skills de plataforma opcionais, cinco skills de marketing cross-market e três skills de fluxo de trabalho de relações públicas |
| [`wiki/`](../../wiki/) | Pesquisa detalhada por mercado e provedor, com links para fontes públicas originais |
| [`schemas/`](../../schemas/) | Schema opcional para registros de oportunidades e um exemplo fictício |
| [`docs/`](../../docs/) | Instalação, segurança, traduções e patrocínio |
| [`prompts/`](../../prompts/) | Prompts reutilizáveis para pesquisa, verificação, ângulos e revisão |
| [`scripts/`](../../scripts/) | Assistente opcional de configuração de provedores e inventário offline |

A wiki prioriza leis, órgãos reguladores, conselhos de imprensa, associações profissionais, regras de plataformas e orientações originais de redações. Confira a fonte vinculada e sua versão atual antes de se apoiar em uma afirmação jurídica ou sobre uma plataforma.

## Auditorias de segurança

NVIDIA SkillSpector: **Warn** (análise estática, 2026-09-21, revisão `b5457eb`). Os 24 apontamentos em 13 pacotes foram revisados individualmente e classificados como falsos positivos; referências semelhantes a caminhos que não foram resolvidas deixam 45 relatórios de pacotes parciais, portanto o resultado agregado permanece `CAUTION`. A análise cobre os 46 pacotes presentes naquela revisão: cinco skills de país, 36 companheiros de plataforma e cinco skills cross-market. Os três skills de fluxo de trabalho de relações públicas foram adicionados depois. Veja o escopo e as limitações no [relatório da auditoria](../security-audit.md).

## Créditos

- [Reel original no Instagram](https://www.instagram.com/p/DblOuOGxU1A/): inspiração do projeto.
- [Writing for Agents](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md): usado nos skills.
- [Documento de wiki com LLM de Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): usado na wiki.
- [Wizard](https://github.com/mattpocock/skills/blob/main/skills/engineering/wizard/SKILL.md): usado na configuração de provedores.

## Contribua

Leia [CONTRIBUTING.md](../../CONTRIBUTING.md) antes de propor uma fonte, um fluxo de mercado, um prompt ou uma correção de regras. Relate vulnerabilidades pelo canal privado do GitHub, conforme descrito em [SECURITY.md](../../SECURITY.md).

## Patrocínio

Para conversar sobre a exibição do seu logo, escreva para [shy-tangerine@mailbox.org](mailto:shy-tangerine@mailbox.org).

O patrocínio financia o acompanhamento de fontes, a manutenção dos fluxos por país, testes de compatibilidade e pesquisa de novos mercados. Veja [patrocínio](../../docs/SPONSORS.md) ou [patrocine shy-tangerine](https://github.com/sponsors/shy-tangerine).

## Licença

MIT. Veja [LICENSE](../../LICENSE).
