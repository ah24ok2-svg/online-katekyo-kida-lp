# online-katekyo-kida-lp

オンライン家庭教師 木田健太郎のランディングページ。素の HTML / CSS のみ。ビルド不要。

## 構成

```
/
├── index.html                LP 本体（1ページ）
├── legal/index.html          特定商取引法に基づく表記
├── privacy/index.html        プライバシーポリシー
├── assets/
│   ├── css/style.css
│   └── img/
│       ├── favicon.svg
│       ├── kida.jpg               顔写真
│       └── ogp.jpg                ← OGP 画像 1200x630（未配置）
├── robots.txt
├── preview/                  プレビュー専用（本番公開時に削除する）
│   ├── build.py                  {{ }} に仮データを流し込む
│   └── values.json               仮データの定義
├── .github/workflows/
│   └── preview-pages.yml     プレビューを Pages に自動デプロイ
└── README.md
```

`style.css` を変更したら、3つの HTML の `style.css?v=…` の値も書き換える（ブラウザに古い CSS が残って変更が反映されないのを防ぐため）。

JS はありません。FAQ のアコーディオンは `<details>` で実装しています。

## 公開までにやること

### 1. プレースホルダを埋める

HTML 内に `{{ }}` の形で残しています。**全て埋めるまで公開しないでください。**

```sh
grep -rno '{{[^}]*}}' index.html legal/index.html privacy/index.html | sort -u -t: -k3
```

| プレースホルダ | 内容 | 使用箇所 |
|---|---|---|
| `{{屋号}}` | 特商法表記に使う事業者名 | legal, privacy |
| `{{問い合わせ先}}` | Google フォームの URL（家庭教師用を新規作成する。AI 相談フォームは流用しない） | index（CTA 2箇所 / JSON-LD） |
| `{{所在地}}` | 特商法表記の所在地 | legal |
| `{{メールアドレス}}` | 連絡先メールアドレス | legal, privacy |
| `{{電話番号}}` | 連絡先電話番号 | legal |
| `{{支払時期}}` | 例：毎月末までに翌月分 | legal |
| `{{返金条件}}` | 未実施分の扱い | legal |

Google フォームの項目は6つに絞る（保護者氏名 / メールアドレス / お子様の学年 / 現在の学習状況 / ご相談内容 / 希望する連絡方法）。成績や志望校は相談時に聞く。

### 2. 画像を置く

- `assets/img/ogp.jpg` — 1200x630。meta タグは配置済みなので、ファイルを置くだけで有効になる。

### 3. URL を確認する

独自ドメインを設定する場合、`canonical` と `og:url` / `og:image` / `twitter:image` の絶対 URL（現在は `https://ah24ok2-svg.github.io/online-katekyo-kida-lp/`）を書き換える。サイト内のリンクは全て相対パスなので、そちらの変更は不要。

### 4. 特商法表記を確認する

記載内容は事業形態により異なります。個人事業で役務を継続提供し対価を受け取る場合、氏名・所在地・連絡先・料金・支払時期・解約条件などの表示が求められるのが一般的ですが、**最終的な記載内容は本人が確認すること。**

### 5. 自己紹介動画（後日）

`index.html` の「講師について」内に、60〜90秒の自己紹介動画を入れる枠をコメントで残してあります。撮影後、コメントを外して `iframe` の `src` を入れる。CSS（`.video`）は用意済み。

## プレビュー（現在の公開設定）

雰囲気を確認するため、GitHub Pages に**仮データ入りのプレビュー**を出しています。

`.github/workflows/preview-pages.yml` が push のたびに `preview/build.py` を実行し、
`{{ }}` に `preview/values.json` の仮データを流し込んだものを配信します。
**ソースの HTML は `{{ }}` のまま**なので、プレビュー用の値が本番に紛れ込むことはありません。

プレビュー版には次の2つが自動で入ります。

- 全ページに `noindex, nofollow`、`robots.txt` は `Disallow: /`（検索に載りません）
- ページ上部に「数値はすべて仮」と書いた告知バー

仮の値を変えたいときは `preview/values.json` を編集して push してください。

### 初回だけ必要な設定

GitHub Pages の有効化だけは Actions から自動化できません
（`GITHUB_TOKEN` に Pages サイトの新規作成権限がないため）。
**リポジトリの Settings → Pages → Build and deployment → Source を「GitHub Actions」に変更**してください。
一度設定すれば、以降は push のたびに自動でデプロイされます。

設定後、Actions タブの「Preview on GitHub Pages」から Re-run するか、何か push すると公開されます。
URL は `https://ah24ok2-svg.github.io/online-katekyo-kida-lp/` です。

### ローカルで同じものを見る

```sh
python3 preview/build.py _site
cd _site && python3 -m http.server 8000
```

`{{ }}` のまま（仮データなし）で見たいときは、リポジトリのルートで直接 `python3 -m http.server 8000`。

## 本番公開に切り替える

1. 上の「公開までにやること」を済ませる（`{{ }}` を実際の値で置換、画像を配置）
2. `preview/` と `.github/workflows/preview-pages.yml` を削除する
3. `main` ブランチにマージし、Settings → Pages → Source: **Deploy from a branch** → `main` / `(root)` に変更する

プレビュー用の仕組みを残したまま本番にすると、告知バーと `noindex` が付いたままになります。

## 確定済みの値

- 指導歴：16年（非常勤時代含む）。既存ポートフォリオは「11年」のままなので、こちらに揃える
- 受付枠：10名
- 対応学年・科目：中学生・全科目
- 授業時間：1回60分
- 料金（1回ごと・税込）：ワーク補助コース 2,000円／中3入試対策コース 3,000円
- 支払方法：銀行振込、PayPay
- 解約：解約希望月の15日までに連絡

## 書くときの原則（編集時も維持する）

- 断定表現を使わない（「必ず」「絶対に」）
- 緊急性を煽らない（「今だけ」「残りわずか」）
- 実績は数字で書くが、盛らない
- 生徒の個別事例に、学校名・地域・部活・家族構成を出さない
- マナリンク、および AI 事業（`new-portfolio.kentaro`）への言及・リンクは置かない
- CTA はヒーローと最終セクションの2箇所のみ。中間に散らさない
- 朱（`--vermil`）は CTA ボタンと重要な一文の下線のみに使う
