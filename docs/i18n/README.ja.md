# Publicist Skills

<p align="center">
  <a href="../../README.md">English</a> ·
  <a href="README.de.md">Deutsch</a> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.pt-BR.md">Português</a>
</p>

<p align="center">
  <img src="../../assets/repository-hero.ja.png" alt="Publicist Skills：5つの市場に対応するメディア調査・企画提案スキル">
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

Publicist Skills は49個の Agent Skill ファミリーです。5つの国別スキルが米国、ドイツ、中国本土、日本、ブラジルに対応し、36個の任意のプラットフォームスキルがチャネルごとの詳しい情報を追加します。5個の市場横断マーケティングスキルはコンバージョン、ローンチ経済性、料金設定、サインアップ、ソーシャルコンテンツを扱い、3個の広報ワークフロースキルはモニタリング、ニュース価値、同じ媒体への再アプローチを扱います。必要なものだけを読み込めます。

Publicistを作ったのは、マーケティングやメディア向けのスキルの多くが広すぎるか、ソーシャルプラットフォーム中心だったからです。アーンドメディアは地域ごとに異なります。編集部の慣習、連絡方法、法律、信頼できるピッチの進め方は市場によって変わります。的外れなピッチは時間とトークンを無駄にするだけでなく、送信者の評判を傷つけることもあります。そのため、これらのスキルは必要な詳細を意図的に含めています。

非公開の記者リストを提供するものでも、一斉送信ツールでもありません。報道の根拠と接続済みの調査ツールを使い、確認済みの短い媒体リスト、企画の切り口、確認用の連絡文案をまとめます。

## 仕組み

国別スキルは[共通プロンプト](../../prompts/shared.md#core-sequence)の検証可能な手順に従い、市場固有のルールと完了条件は各 `SKILL.md` に記載されています。

1. 承認済みの事実、証拠、除外事項、取材対応者の予定をブリーフにまとめます。
2. 最近の署名記事、編集部の公式窓口、取材募集、接続済みサービスから候補を調査します。
3. 証拠を記録し、`REJECT`、`NEEDS_REVIEW`、`DRAFT_ALLOWED` のいずれかを返します。[米国スキルの出力規約](../../skills/publicist-us/SKILL.md#output)に必須項目を示し、任意の [JSON Schema](../../schemas/opportunity-record.schema.json)で取材募集レコードを形式化できます。
4. 証拠ゲートを通過してから、市場に合った切り口や文案を作成します。[安全方針](../../docs/safety-model.md#external-action-boundary)により、送信と公開は常に別の操作です。

## ツールと境界

編集部の公式ページと最近の記事を優先します。以下のサービスは任意で、アカウント、アクセス規則、費用はスキルとは別です。調査や文案作成が送信を許可することはありません。

| 作業 | 使用するツール |
|---|---|
| 取材募集や専門家への依頼を探す | 米国では [Featured](https://featured.com/)、[Qwoted](https://www.qwoted.com/)、[Source of Sources](https://www.sourceofsources.com/)、[MentionMatch](https://mentionmatch.com/)、中国本土では [PR Newswire Asia/Cision ProfNet](https://www.prnasia.com/products/media-database/)、ブラジルでは [Ajor の情報源データベース一覧](https://ajor.org.br/sete-bancos-de-fontes-gratuitos-para-jornalistas/) |
| 媒体と記者を探す | 米国では [JournoFinder](https://journofinder.com/)、ドイツでは [news aktuell zimpel](https://www.newsaktuell.de/zimpel/)、中国本土では [Niumedia](https://niumedia.cn/)、日本では [PRONE/PRM](https://prone.jp/prm) と [Foreign Press Center Japan](https://fpcj.jp/en/assistance/fpregcard/)、ブラジルでは [Knewin/Comunique-se Mailing](https://www.knewin.com/mailing-de-imprensa/)。加えて公式スタッフページ、最近の署名記事、編集部一覧、投稿窓口 |
| リーチ、担当分野、地域のアクセス条件を確認する | [IVW](https://www.ivw.de/) と [ドイツの媒体調査ガイド](../../wiki/public-relations/germany-media-discovery.md)、[中国本土の媒体調査ガイド](../../wiki/public-relations/china-media-discovery.md)、[日本新聞協会の記者クラブに関する見解](https://pressnet.or.jp/english/about/guideline/) と [Foreign Press Center Japan](https://fpcj.jp/en/assistance/fpregcard/)、[ブラジルの媒体調査ガイド](../../wiki/public-relations/brazil-media-discovery.md) |
| 業務用の連絡先を探す | 米国では [Hunter](https://hunter.io/)、[Clay](https://www.clay.com/)、[Apollo](https://www.apollo.io/) を補助的な連絡先補完に使用。ドイツでは [news aktuell zimpel](https://www.newsaktuell.de/zimpel/)、中国本土では [PR Newswire Asia/Cision](https://www.prnasia.com/products/media-database/)、日本では [PRONE/PRM](https://prone.jp/prm)、ブラジルでは [Knewin/Comunique-se Mailing](https://www.knewin.com/mailing-de-imprensa/)。どの市場でも編集部の公式窓口を優先 |

[地域別サービスのWiki](../../wiki/public-relations/localized-media-contact-infrastructure.md)では、各サービスが提供する情報と根拠の限界を説明しています。スキルは連絡先の出典とサービス規則を確認し、Qwoted などでは人が書いた回答が必要です。対象外の国では先に現地のメディア環境を調べてください。米国スキルは世界共通の代替ではありません。

## インストール

現在の Skills CLI 構文でスキルを1つインストールします。

```bash
npx skills add shy-tangerine/publicist-skills \
  --skill publicist-us --global --yes
```

`publicist-us` を必要なパッケージに置き換えます。

| 対象 | スキル名 |
|---|---|
| 国別 | `publicist-us`、`publicist-germany`、`publicist-china`、`publicist-japan`、`publicist-brazil` |
| 市場横断 | `cro`、`launch-economics`、`pricing`、`signup`、`social` |

各スキルは単独で動作します。任意のプラットフォームスキル、手動設定、クライアント別手順は[インストールと互換性](../../docs/installation.md)を参照してください。

### サービス設定ウィザード

初回利用時に、対象市場のサービスを選ぶウィザードをエージェントが案内します。サービスを選ぶと、公式ツールやウェブサイトの設定・利用手順を確認できます。この手順は省略できます。

リポジトリのローカルコピーから実行する例：

```bash
python3 scripts/provider_wizard.py germany --setup 'news aktuell zimpel'
```

ウィザードは手順を案内するもので、アカウントには接続しません。詳しくは[サービス設定ガイド](../../docs/provider-adapters.md)を参照してください。

## 例

**短い架空の例。** 以下の組織、記者、媒体、URLは架空で、フィールドは実際の[出力規約](../../skills/publicist-us/SKILL.md#completion-check)に従います。

**入力:** Fernbrook Analytics がオープンソースのファームウェアセキュリティデータセットを公開します。公開済みの端末数とスキャン結果だけを使い、侵害を示す表現や競合他社への主張は除外します。関連する米国の記者を1人探し、送信せずに文案を準備します。

| フィールド | 値 |
|---|---|
| `decision` | `DRAFT_ALLOWED` |
| `journalist_name` | Dana Okafor |
| `recent_work_url` | `example.com/vtl/sbom-gaps`（2026-09-01 確認） |
| `route_provenance` | 公式署名ページ → `dokafor@vtl.example` |
| 主張ゲート | 端末数を検証済み、広すぎる競合他社への主張を削除 |
| 外部操作 | 文案を保存、未送信 |

[プロンプト集](../../prompts/README.md)には、調査、検証、文案、フォローアップ、訂正用の再利用可能なブリーフがあります。

## リポジトリの内容

| パス | 内容 |
|---|---|
| [`skills/`](../../skills/) | 5つの独立した国別スキル、36個の任意のプラットフォームスキル、5個の市場横断マーケティングスキル、3個の広報ワークフロースキル |
| [`wiki/`](../../wiki/) | 市場・サービスの詳しい調査と、公開された原典への引用 |
| [`schemas/`](../../schemas/) | 任意の案件記録スキーマと架空のサンプル |
| [`docs/`](../../docs/) | インストール、安全方針、翻訳、スポンサーの説明 |
| [`prompts/`](../../prompts/) | 調査、確認、切り口の検討、レビュー用の再利用可能なプロンプト |
| [`scripts/`](../../scripts/) | 任意のサービス設定ウィザードと提供元一覧 |

Wiki は、法律、規制当局、報道評議会、職業団体、プラットフォーム規則、編集部による原文の案内を優先します。法律やプラットフォームについての記述に依拠する前に、リンク先とその最新版を確認してください。

## セキュリティ監査

NVIDIA SkillSpector：**Warn**（静的解析のみ、2026-09-21、リビジョン `b5457eb`）。13パッケージの24件の指摘を個別に確認し、すべて誤検出と判断しました。パス形式の未解決参照により45パッケージのレポートが不完全なため、集計結果は `CAUTION` です。この解析は当時の46パッケージ（国別5、プラットフォーム36、市場横断5）を対象としており、後から追加された3個の広報ワークフロースキルは含みません。範囲と制限は[監査報告](../security-audit.md)を参照してください。

## クレジット

- [着想の元となったInstagramリール](https://www.instagram.com/p/DblOuOGxU1A/)：プロジェクトの着想。
- [Writing for Agents](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md)：スキルの作成に使用。
- [KarpathyのLLM Wiki文書](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)：Wiki の作成に使用。
- [Wizard](https://github.com/mattpocock/skills/blob/main/skills/engineering/wizard/SKILL.md)：サービス設定の設計に使用。

## 貢献するには

新しい出典、市場の手順、プロンプト、規則の修正を提案する前に [CONTRIBUTING.md](../../CONTRIBUTING.md) をお読みください。脆弱性は [SECURITY.md](../../SECURITY.md) の説明に従い、GitHub の非公開報告機能からお知らせください。

## スポンサー

ロゴ掲載についてのお問い合わせは、[shy-tangerine@mailbox.org](mailto:shy-tangerine@mailbox.org) までご連絡ください。

スポンサーの支援は、出典の監視、国別手順の保守、互換性テスト、新市場の調査に充てられます。[スポンサーの説明](../../docs/SPONSORS.md)をご覧いただくか、[shy-tangerine のスポンサーになる](https://github.com/sponsors/shy-tangerine)からご支援ください。

## ライセンス

MIT。[LICENSE](../../LICENSE) を参照してください。
