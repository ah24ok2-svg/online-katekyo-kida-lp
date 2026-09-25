#!/usr/bin/env python3
"""プレビュー用サイトを組み立てる。

index.html などのソースには {{ }} をそのまま残しておき、
このスクリプトが出力先にコピーする過程でだけ仮データを流し込む。
併せて noindex とプレビュー告知バーを入れるので、
公開中のプレビューが検索に載ったり、仮の金額が本物に見えたりしない。

  使い方: python3 preview/build.py _site
"""
import json
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
VALUES = json.loads((ROOT / "preview" / "values.json").read_text(encoding="utf-8"))

# 出力しないもの（プレビューの成果物に混ぜる必要がない）
EXCLUDE_DIRS = {".git", ".github", "preview", "_site", "node_modules"}
EXCLUDE_FILES = {"README.md", ".gitignore"}

BANNER = """<div class="preview-bar">
  <p>これは公開前の<strong>確認用プレビュー</strong>です。検索エンジンには表示されません。</p>
</div>
"""

BANNER_CSS = """<style>
/* プレビュー告知バー。preview/build.py が挿入する。本番ビルドには入らない */
.preview-bar {
  background: #F2EFE8;
  border-bottom: 1px solid #DFDCD4;
}
.preview-bar p {
  max-width: 44em;
  margin: 0 auto;
  padding: 0.75rem 1.5rem;
  color: #5A5A56;
  font-size: 0.8125rem;
  line-height: 1.7;
}
.preview-bar strong { color: #1A1A1A; font-weight: 500; }
</style>
"""

NOINDEX = '<meta name="robots" content="noindex, nofollow">'


def fill(text: str) -> str:
    """{{キー}} を仮データに置換する。未知のキーは残して後で気付けるようにする。"""
    def repl(m):
        key = m.group(1)
        if key not in VALUES:
            print(f"  !! 仮データ未定義: {{{{{key}}}}}", file=sys.stderr)
            return m.group(0)
        return VALUES[key]

    return re.sub(r"\{\{([^}]+)\}\}", repl, text)


def localize_cta(html: str) -> str:
    """仮の問い合わせ先がページ内アンカーのとき、新規タブ指定を外す。

    本番の Google フォーム URL は別タブで開く仕様なので、ソース側の
    target="_blank" はそのまま。プレビューで同じページが新規タブに
    開くのを避けるための処理に限る。
    """
    if not VALUES.get("問い合わせ先", "").startswith("#"):
        return html
    return re.sub(r'(<a class="btn" href="#[^"]*")\s+target="_blank"\s+rel="noopener"', r"\1", html)


def decorate(html: str) -> str:
    """noindex と告知バーを差し込む。"""
    if not re.search(r'<meta\s+name="robots"', html):
        html = html.replace("</head>", f"{NOINDEX}\n</head>", 1)
    html = html.replace("</head>", f"{BANNER_CSS}</head>", 1)
    html = html.replace("<body>", f"<body>\n\n{BANNER}", 1)
    return html


def main() -> int:
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    for src in sorted(ROOT.rglob("*")):
        rel = src.relative_to(ROOT)
        if set(rel.parts) & EXCLUDE_DIRS or rel.name in EXCLUDE_FILES:
            continue
        if src.is_dir():
            continue

        dst = out / rel
        dst.parent.mkdir(parents=True, exist_ok=True)

        if src.suffix == ".html":
            dst.write_text(decorate(localize_cta(fill(src.read_text(encoding="utf-8")))), encoding="utf-8")
        elif src.name == "robots.txt":
            # プレビューの間は全ページをクロール対象外にする
            dst.write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
        else:
            shutil.copy2(src, dst)
        print(f"  {rel}")

    remaining = sum(
        len(re.findall(r"\{\{[^}]+\}\}", p.read_text(encoding="utf-8")))
        for p in out.rglob("*.html")
    )
    print(f"\n出力: {out}／未置換のプレースホルダ: {remaining}")
    return 1 if remaining else 0


if __name__ == "__main__":
    raise SystemExit(main())
