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
│       ├── kida-placeholder.svg   顔写真の仮置き
│       ├── kida.jpg               ← 顔写真（未配置）
│       └── ogp.jpg                ← OGP 画像 1200x630（未配置）
├── robots.txt
└── README.md
```

JS はありません。FAQ のアコーディオンは `<details>` で実装しています。

## 公開までにやること

### 1. プレースホルダを埋める

HTML 内に `{{ }}` の形で残しています。**全て埋めるまで公開しないでください。**

```sh
grep -rno '{{[^}]*}}' index.html legal/index.html privacy/index.html | sort -u -t: -k3
```

| プレースホルダ | 内容 | 使用箇所 |
|---|---|---|
| `{{指導歴}}` | 指導年数。**SNS・既存ポートフォリオと数字を必ず統一する**（既存は「11年」、SNS は「16年」を使用予定） | index（meta / ヒーロー / 講師について） |
| `{{料金}}` | 月額（税込表記） | index, legal |
| `{{対応学年}}` | 例：小6〜中3 | index（meta / ヒーロー） |
| `{{対応科目}}` | 例：英語・数学・国語 | index（ヒーロー / JSON-LD） |
| `{{授業時間}}` | 1回あたりの分数 | index, legal |
| `{{受付枠}}` | 現在の空き枠数 | index（ヒーロー / 申し込み） |
| `{{屋号}}` | 特商法表記に使う事業者名 | legal, privacy |
| `{{問い合わせ先}}` | Google フォームの URL（家庭教師用を新規作成する。AI 相談フォームは流用しない） | index（CTA 2箇所 / JSON-LD） |
| `{{所在地}}` | 特商法表記の所在地 | legal |
| `{{メールアドレス}}` | 連絡先メールアドレス | legal, privacy |
| `{{電話番号}}` | 連絡先電話番号 | legal |
| `{{支払方法}}` | 例：銀行振込 | index, legal |
| `{{支払時期}}` | 例：毎月末までに翌月分 | legal |
| `{{解約条件}}` | 例：1ヶ月前までにご連絡いただければ可 | index（料金 / FAQ）, legal |
| `{{返金条件}}` | 未実施分の扱い | legal |

Google フォームの項目は6つに絞る（保護者氏名 / メールアドレス / お子さんの学年 / 現在の学習状況 / ご相談内容 / 希望する連絡方法）。成績や志望校は相談時に聞く。

### 2. 画像を置く

- `assets/img/kida.jpg` — 顔写真（正面・明るい・私服可）。置いたら `index.html` のヒーローの `src` を `assets/img/kida-placeholder.svg` から差し替える。
- `assets/img/ogp.jpg` — 1200x630。meta タグは配置済みなので、ファイルを置くだけで有効になる。

### 3. URL を確認する

独自ドメインを設定する場合、`canonical` と `og:url` / `og:image` / `twitter:image` の絶対 URL（現在は `https://ah24ok2-svg.github.io/online-katekyo-kida-lp/`）を書き換える。サイト内のリンクは全て相対パスなので、そちらの変更は不要。

### 4. 特商法表記を確認する

記載内容は事業形態により異なります。個人事業で役務を継続提供し対価を受け取る場合、氏名・所在地・連絡先・料金・支払時期・解約条件などの表示が求められるのが一般的ですが、**最終的な記載内容は本人が確認すること。**

### 5. 自己紹介動画（後日）

`index.html` の「講師について」内に、60〜90秒の自己紹介動画を入れる枠をコメントで残してあります。撮影後、コメントを外して `iframe` の `src` を入れる。CSS（`.video`）は用意済み。

## 公開

GitHub Pages で `main` ブランチのルートを配信する。Settings → Pages → Source: Deploy from a branch → `main` / `(root)`。

## ローカル確認

```sh
python3 -m http.server 8000
```

## 書くときの原則（編集時も維持する）

- 断定表現を使わない（「必ず」「絶対に」）
- 緊急性を煽らない（「今だけ」「残りわずか」）
- 実績は数字で書くが、盛らない
- 生徒の個別事例に、学校名・地域・部活・家族構成を出さない
- マナリンク、および AI 事業（`new-portfolio.kentaro`）への言及・リンクは置かない
- CTA はヒーローと最終セクションの2箇所のみ。中間に散らさない
- 朱（`--vermil`）は CTA ボタンと重要な一文の下線のみに使う
