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
│       └── ogp.jpg                OGP 画像 1200x630（SNS・LINE で共有したときに表示）
├── robots.txt
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

現在、未入力のプレースホルダはありません（上の grep で 0 件になることを確認する）。

Google フォームの項目は4つ（保護者氏名 / メールアドレス / お子様の学年 / 現在の学習状況）。変えたら LP の申し込み欄とプライバシーポリシーの記載も合わせる。成績や志望校は相談時に聞く。

### 2. 画像を置く

- `assets/img/ogp.jpg` — 配置済み（見出し・名前・肩書き・顔写真）。見出しや肩書きを変えたら作り直す。

### 3. URL を確認する

独自ドメインを設定する場合、`canonical` と `og:url` / `og:image` / `twitter:image` の絶対 URL（現在は `https://ah24ok2-svg.github.io/online-katekyo-kida-lp/`）を書き換える。サイト内のリンクは全て相対パスなので、そちらの変更は不要。

### 4. 特商法表記を確認する

記載内容は事業形態により異なります。個人事業で役務を継続提供し対価を受け取る場合、氏名・所在地・連絡先・料金・支払時期・解約条件などの表示が求められるのが一般的ですが、**最終的な記載内容は本人が確認すること。**

### 5. 自己紹介動画（後日）

`index.html` の「講師について」内に、60〜90秒の自己紹介動画を入れる枠をコメントで残してあります。撮影後、コメントを外して `iframe` の `src` を入れる。CSS（`.video`）は用意済み。

## 公開設定

GitHub Pages で `claude/new-session-c1a0ms` ブランチのルートをそのまま配信しています（ビルドなし）。
push すると数分で反映されます。

- Settings → Pages → Build and deployment → Source：**Deploy from a branch** / `claude/new-session-c1a0ms` / `/(root)`
- URL：`https://ah24ok2-svg.github.io/online-katekyo-kida-lp/`
- 特商法表記・プライバシーポリシーは `noindex`、`robots.txt` でもクロール対象外にしている（LP 本体のみ検索対象）

### ローカルで確認する

```sh
python3 -m http.server 8000
```

## 確定済みの値

- 指導歴：16年（非常勤時代含む）。既存ポートフォリオは「11年」のままなので、こちらに揃える
- 受付枠：10名
- 対応学年・科目：中学生・全科目
- 授業時間：1回60分
- 料金（1回ごと・税込）：ワーク補助コース　中1・中2 2,000円／中3 3,000円（入試対策コースは廃止。中高一貫校の中3生もいるため、受験前提のコースは置かない）。授業の中身は随時相談して決める
- 支払方法：銀行振込、PayPay
- 受講回数：月ごとに自由（最低回数なし）
- 受講の終了：やめる月の15日までに連絡
- 支払時期：月末締め・翌月末払い（後払いのため返金は発生しない）
- 事業者名：木田健太郎／所在地：埼玉県（詳細は請求時に開示）
- 連絡先：ah24o.k2@gmail.com／080-4500-6412
- 問い合わせフォーム：https://docs.google.com/forms/d/e/1FAIpQLScOPqG9miC_g9i534J-79wYgB1RrjtzoHpHmGFj-Q4R5QNJWg/viewform

## 書くときの原則（編集時も維持する）

- 断定表現を使わない（「必ず」「絶対に」）
- 緊急性を煽らない（「今だけ」「残りわずか」）
- 実績は数字で書くが、盛らない
- 生徒の個別事例に、学校名・地域・部活・家族構成を出さない
- マナリンク、および AI 事業（`new-portfolio.kentaro`）への言及・リンクは置かない
- CTA はヒーローと最終セクションの2箇所のみ。中間に散らさない
- 朱（`--vermil`）は CTA ボタンと重要な一文の下線のみに使う
