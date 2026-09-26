# Publicist Skills

<p align="center">
  <a href="../../README.md">English</a> ·
  <a href="README.de.md">Deutsch</a> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.pt-BR.md">Português</a>
</p>

<p align="center">
  <img src="../../assets/repository-hero.de.png" alt="Publicist-Wortmarke für Publicist Skills: Skills für Medienrecherche und Pitch-Strategie in fünf Märkten">
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

Publicist Skills ist eine Familie aus 49 Agent Skills. Fünf Länder-Skills decken die USA, Deutschland, Festlandchina, Japan und Brasilien ab; 36 optionale Plattform-Skills ergänzen die Tiefe einzelner Kanäle; fünf marktübergreifende Marketing-Skills decken Conversion, Launch-Ökonomie, Pricing, Signup und Social Content ab; drei PR-Workflow-Skills decken Monitoring, Nachrichtenwert und die erneute Ansprache derselben Redaktion ab. Lade nur, was du brauchst.

Ich habe Publicist entwickelt, weil die meisten Marketing- und Medien-Skills entweder sehr allgemein waren oder sich auf Social-Media-Plattformen konzentrierten. Earned Media ist lokal: Redaktionsgepflogenheiten, Kontaktwege, Gesetze und seriöse Pitching-Praktiken unterscheiden sich von Markt zu Markt. Ein schlecht ausgerichteter Pitch verschwendet mehr als Zeit und Tokens; er kann dem Ruf des Absenders schaden. Deshalb sind diese Skills bewusst ausführlich.

Sie enthalten keine geheime Journalistenliste und sind kein Massenmailer. Aus redaktionellen Belegen und verbundenen Recherchewerkzeugen entstehen eine kurze, geprüfte Medienliste, Themenwinkel und Entwürfe zur Freigabe.

## So funktioniert es

Die Länder-Skills folgen der prüfbaren Abfolge in den [gemeinsamen Prompts](../../prompts/shared.md#core-sequence); marktspezifische Regeln und Abschlusskriterien stehen im jeweiligen `SKILL.md`:

1. Freigegebene Fakten, Belege, Ausschlüsse und Verfügbarkeit der Ansprechperson werden zu einem Briefing.
2. Kandidat:innen werden über aktuelle Autorenzeilen, offizielle Redaktionswege, Quellenanfragen und verbundene Anbieter recherchiert.
3. Die Belege werden dokumentiert und als `REJECT`, `NEEDS_REVIEW` oder `DRAFT_ALLOWED` bewertet. Der [US-Ausgabevertrag](../../skills/publicist-us/SKILL.md#output) zeigt die Pflichtfelder; das optionale [JSON Schema](../../schemas/opportunity-record.schema.json) formalisiert Quellenanfragen.
4. Erst nach bestandener Belegprüfung entsteht ein marktgerechter Aufhänger oder Pitch. Versand und Veröffentlichung bleiben gemäß [Sicherheitsmodell](../../docs/safety-model.md#external-action-boundary) separate Aktionen.

## Werkzeuge und Grenzen

Offizielle Redaktionsseiten und aktuelle Beiträge haben Vorrang. Die folgenden Dienste sind optional; Konten, Zugangsregeln und Kosten bleiben von den Skills getrennt. Recherche oder Entwurf erlauben niemals automatisch den Versand.

| Aufgabe | Werkzeuge |
|---|---|
| Quellenanfragen und Expertenbeiträge finden | [Featured](https://featured.com/), [Qwoted](https://www.qwoted.com/), [Source of Sources](https://www.sourceofsources.com/) und [MentionMatch](https://mentionmatch.com/) in den USA; [PR Newswire Asia/Cision ProfNet](https://www.prnasia.com/products/media-database/) in Festlandchina; [Ajors Verzeichnis von Quellenbanken](https://ajor.org.br/sete-bancos-de-fontes-gratuitos-para-jornalistas/) in Brasilien |
| Medien und Journalist:innen finden | [JournoFinder](https://journofinder.com/) in den USA; [news aktuell zimpel](https://www.newsaktuell.de/zimpel/) in Deutschland; [Niumedia](https://niumedia.cn/) in Festlandchina; [PRONE/PRM](https://prone.jp/prm) und [Foreign Press Center Japan](https://fpcj.jp/en/assistance/fpregcard/) in Japan; [Knewin/Comunique-se Mailing](https://www.knewin.com/mailing-de-imprensa/) in Brasilien; außerdem offizielle Teamseiten, aktuelle Autorenzeilen, Redaktionsverzeichnisse und Einreichungsseiten |
| Reichweite, Ressort und lokale Zugangsregeln prüfen | [IVW](https://www.ivw.de/) und [Rechercheleitfaden für Deutschland](../../wiki/public-relations/germany-media-discovery.md); [Rechercheleitfaden für Festlandchina](../../wiki/public-relations/china-media-discovery.md); [Presseclub-Leitlinien des Nihon Shinbun Kyokai](https://pressnet.or.jp/english/about/guideline/) und [Foreign Press Center Japan](https://fpcj.jp/en/assistance/fpregcard/); [Rechercheleitfaden für Brasilien](../../wiki/public-relations/brazil-media-discovery.md) |
| Berufliche Kontaktdaten finden | [Hunter](https://hunter.io/), [Clay](https://www.clay.com/) und [Apollo](https://www.apollo.io/) zur ergänzenden Kontaktanreicherung in den USA; [news aktuell zimpel](https://www.newsaktuell.de/zimpel/) in Deutschland; [PR Newswire Asia/Cision](https://www.prnasia.com/products/media-database/) in Festlandchina; [PRONE/PRM](https://prone.jp/prm) in Japan; [Knewin/Comunique-se Mailing](https://www.knewin.com/mailing-de-imprensa/) in Brasilien; offizielle Redaktionswege haben in jedem Markt Vorrang |

Das [Wiki zu lokalen Anbietern](../../wiki/public-relations/localized-media-contact-infrastructure.md) erklärt, was die Systeme enthalten und wo ihre Belege enden. Die Skills prüfen die Herkunft von Kontaktdaten und Anbieterregeln; Dienste wie Qwoted verlangen von Menschen verfasste Antworten. Recherchiere für andere Länder zuerst das lokale Mediensystem. Der US-Skill ist kein weltweiter Ersatz.

## Installation

Installiere einen Skill mit der aktuellen Syntax der Skills CLI:

```bash
npx skills add shy-tangerine/publicist-skills \
  --skill publicist-us --global --yes
```

Ersetze `publicist-us` durch das gewünschte Paket:

| Bereich | Skill-Namen |
|---|---|
| Länder | `publicist-us`, `publicist-germany`, `publicist-china`, `publicist-japan`, `publicist-brazil` |
| Marktübergreifend | `cro`, `launch-economics`, `pricing`, `signup`, `social` |

Jeder Skill funktioniert eigenständig. Optionale Plattform-Skills sowie manuelle und clientspezifische Einrichtung stehen unter [Installation und Kompatibilität](../../docs/installation.md).

### Anbieter-Assistent

Beim ersten Einsatz bietet der Agent einen Assistenten für Anbieter in deinem Markt an. Wähle einen Anbieter, um Anleitungen für dessen offizielle Werkzeuge oder Website zu erhalten. Du kannst diesen Schritt überspringen.

Aus einem Repository-Checkout:

```bash
python3 scripts/provider_wizard.py germany --setup 'news aktuell zimpel'
```

Der Assistent verweist auf Anleitungen; er verbindet keine Konten. Details stehen im [Anbieter-Leitfaden](../../docs/provider-adapters.md).

## Beispiel

**Kurzes fiktives Beispiel.** Organisation, Journalist, Medium und URLs sind erfunden; die Felder folgen dem echten [Ausgabevertrag](../../skills/publicist-us/SKILL.md#completion-check).

**Eingabe:** Fernbrook Analytics veröffentlicht einen Open-Source-Datensatz zur Firmware-Sicherheit. Verwende nur die veröffentlichte Gerätezahl und die Scan-Ergebnisse; keine Einbruchsdarstellung und keine Wettbewerberbehauptungen. Finde eine passende US-Journalistin und bereite einen Pitch vor, ohne ihn zu senden.

| Feld | Wert |
|---|---|
| `decision` | `DRAFT_ALLOWED` |
| `journalist_name` | Dana Okafor |
| `recent_work_url` | `example.com/vtl/sbom-gaps` (abgerufen 2026-09-01) |
| `route_provenance` | Offizielle Byline-Seite → `dokafor@vtl.example` |
| Claim-Gate | Gerätezahl verifiziert; breite Wettbewerberbehauptung entfernt |
| Externe Aktion | Entwurf gespeichert; nichts versendet |

Die [Prompt-Bibliothek](../../prompts/README.md) enthält wiederverwendbare Briefings für Recherche, Prüfung, Entwurf, Follow-up und Korrekturen.

## Repository-Inhalt

| Pfad | Inhalt |
|---|---|
| [`skills/`](../../skills/) | Fünf eigenständige Länder-Skills, 36 optionale Plattform-Skills, fünf marktübergreifende Marketing-Skills und drei PR-Workflow-Skills |
| [`wiki/`](../../wiki/) | Ausführliche Markt- und Anbieterrecherche mit Verweisen auf öffentliche Originalquellen |
| [`schemas/`](../../schemas/) | Optionales Schema für Opportunity-Datensätze und ein fiktives Beispiel |
| [`docs/`](../../docs/) | Installation, Sicherheit, Übersetzungen und Sponsoring |
| [`prompts/`](../../prompts/) | Wiederverwendbare Prompts für Recherche, Prüfung, Themenwinkel und Review |
| [`scripts/`](../../scripts/) | Optionaler Offline-Anbieter-Assistent und Anbieterübersicht |

Das Wiki bevorzugt Gesetze, Aufsichtsbehörden, Presseräte, Berufsverbände, Plattformregeln und originale Redaktionshinweise. Prüfe die verlinkte Quelle und ihren aktuellen Stand, bevor du dich auf eine Rechts- oder Plattformaussage verlässt.

## Sicherheitsaudits

NVIDIA SkillSpector: **Warn** (nur statische Analyse, 2026-09-21, Revision `b5457eb`). 24 Befunde in 13 Paketen wurden einzeln geprüft und als Fehlalarme bewertet; nicht aufgelöste pfadähnliche Referenzen lassen 45 Paketberichte unvollständig, daher bleibt die Gesamtbewertung `CAUTION`. Die Analyse deckt die 46 Pakete ab, die in dieser Revision enthalten waren: fünf Länder-Skills, 36 Plattform-Skills und fünf marktübergreifende Skills. Die drei PR-Workflow-Skills kamen später hinzu. Umfang und Grenzen stehen im [Auditbericht](../security-audit.md).

## Credits

- [Originales Instagram-Reel](https://www.instagram.com/p/DblOuOGxU1A/): Projektidee.
- [Writing for Agents](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md): für die Skills verwendet.
- [Karpathys LLM-Wiki-Dokument](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): für das Wiki verwendet.
- [Wizard](https://github.com/mattpocock/skills/blob/main/skills/engineering/wizard/SKILL.md): für die Anbietereinrichtung verwendet.

## Mitmachen

Lies [CONTRIBUTING.md](../../CONTRIBUTING.md), bevor du eine neue Quelle, einen Markt-Workflow, einen Prompt oder eine Regelkorrektur vorschlägst. Melde Sicherheitslücken vertraulich über GitHubs private Meldemöglichkeit, wie in [SECURITY.md](../../SECURITY.md) beschrieben.

## Sponsoring

Für Anfragen zur Logoplatzierung schreib an [shy-tangerine@mailbox.org](mailto:shy-tangerine@mailbox.org).

Sponsoring finanziert Quellenbeobachtung, Pflege der Länder-Workflows, Kompatibilitätstests und Recherchen zu neuen Märkten. Siehe [Sponsoring](../../docs/SPONSORS.md) oder [unterstütze shy-tangerine](https://github.com/sponsors/shy-tangerine).

## Lizenz

MIT. Siehe [LICENSE](../../LICENSE).
