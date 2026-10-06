"""index.html から、WordPress の固定ページ「車の持ち方診断」(/carmotikata/) の
カスタムHTMLブロックに貼る中身（wp_block.html）を作る。
<html>・<head>・<body> の外枠を外す（由美さんが WP に貼ったときと同じ形）。
    python3 build_wp.py
"""
import sys
from pathlib import Path

here = Path(__file__).parent


def build(src: str) -> str:
    start = src.index("  <style>")
    head_end = src.index("</head>")
    body_start = src.index("<body>\n") + len("<body>\n")
    body_end = src.index("</body>")
    return src[start:head_end] + src[body_start:body_end]


if __name__ == "__main__":
    src = sys.stdin.read() if "-" in sys.argv[1:] else (here / "index.html").read_text(encoding="utf-8")
    out = build(src)
    if "-" in sys.argv[1:]:
        sys.stdout.write(out)
    else:
        (here / "wp_block.html").write_text(out, encoding="utf-8")
        print("wrote wp_block.html", len(out))
