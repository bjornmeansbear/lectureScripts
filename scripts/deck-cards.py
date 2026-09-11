#!/usr/bin/env python3
"""Print a deck as cut-up cards — one small card per slide, for reordering on a table.

Why this exists: when a deck's running order stops making sense, the fastest fix is
physical. Print, cut, shuffle, lay them out, read the new order off the table. This
makes the sheet: slide number, the part it currently sits in, its palette, and enough
text to recognise it — deliberately not the whole slide.

Printed light on white regardless of the deck's own palette. A dark deck would empty
a toner cartridge.

    python3 scripts/deck-cards.py lecture-design-thinking/di200-wk4-deck.html
    python3 scripts/deck-cards.py <deck> --per-page 6

Writes build/<path>-cards.pdf and prints the current order to stdout, so you can hand
the new order back as a list of numbers.
"""
import argparse, html, pathlib, re, subprocess, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import importlib.util
_spec = importlib.util.spec_from_file_location("dp", pathlib.Path(__file__).parent / "deck-pdf.py")
dp = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(dp)

def text(frag, limit=170):
    t = re.sub(r'<[^>]+>', ' ', frag or '')
    return re.sub(r'\s+', ' ', html.unescape(t)).strip()[:limit]

def parse(src: pathlib.Path):
    s = src.read_text(encoding="utf-8")
    body = s[s.index('<div class="stage"'):]
    part, cards = "", []
    for chunk in re.split(r'<!-- ═══ (.*?) ═══ -->', body):
        if not chunk.strip().startswith('<section') and '·' in chunk:
            part = chunk.split('·')[0].strip(); continue
        for cid, cls, inner in re.findall(
                r'<section(?:\s+data-card="([^"]*)")?\s*class="slide([^"]*)"[^>]*>(.*?)</section>',
                chunk, re.S):
            eb = re.search(r'class="eyebrow">(.*?)</div>', inner, re.S)
            h  = re.search(r'<h[123][^>]*>(.*?)</h[123]>', inner, re.S)
            h3 = re.search(r'<h3>(.*?)</h3>', inner, re.S)
            lead = re.search(r'class="lead[^"]*">(.*?)</p>', inner, re.S)
            lis = re.findall(r'<li>(.*?)</li>', inner, re.S)
            head = text(h.group(1) if h else (h3.group(1) if h3 else None), 90)
            rest = text(lead.group(1) if lead else (" · ".join(text(l, 60) for l in lis[:3]) if lis else None))
            cards.append(dict(n=len(cards)+1, cid=cid or "--", part=part, cls=cls.strip(),
                              eyebrow=text(eb.group(1) if eb else None, 60),
                              head=head, rest=rest))
    return cards

CSS = """
@page { size: letter portrait; margin: 0.45in; }
:root{--bg:rgb(247,248,238);--ink:rgb(25,21,19);--mut:rgb(52,51,42);--acc:rgb(164,0,65);}
*{box-sizing:border-box}
body{margin:0;background:#fff;color:var(--ink);
     font:11px/1.35 system-ui,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;}
.sheet{display:grid;grid-template-columns:repeat(2,1fr);gap:0;}
.card{border:1px dashed rgba(0,0,0,.45);padding:12px 13px;height:2.45in;
      background:var(--bg);display:flex;flex-direction:column;gap:5px;overflow:hidden;
      break-inside:avoid;}
.top{display:flex;align-items:baseline;gap:8px;border-bottom:1px solid var(--ink);padding-bottom:4px;}
.n{font-size:23px;font-weight:800;letter-spacing:-.02em;line-height:1;}
.meta{font-size:8.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--mut);}
.pal{margin-left:auto;font-size:8.5px;letter-spacing:.06em;color:var(--acc);}
.eb{font-size:9px;letter-spacing:.07em;text-transform:uppercase;color:var(--acc);}
.hd{font-size:14px;font-weight:700;line-height:1.2;}
.bd{font-size:9.5px;color:var(--mut);overflow:hidden;}
"""

def build(cards, per_page):
    rows = "".join(
        f'<div class="card"><div class="top"><span class="n">{c["cid"]}</span>'
        f'<span class="meta">now #{c["n"]} · {html.escape(c["part"] or "—")}</span>'
        f'<span class="pal">{html.escape(c["cls"].replace("s-","")) }</span></div>'
        + (f'<div class="eb">{html.escape(c["eyebrow"])}</div>' if c["eyebrow"] else "")
        + (f'<div class="hd">{html.escape(c["head"])}</div>' if c["head"] else "")
        + (f'<div class="bd">{html.escape(c["rest"])}</div>' if c["rest"] else "")
        + "</div>"
        for c in cards)
    return (f"<!doctype html><html lang=en><head><meta charset=utf-8>"
            f"<title>cards</title><style>{CSS}</style></head><body>"
            f'<div class="sheet">{rows}</div></body></html>')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck", type=pathlib.Path)
    ap.add_argument("--per-page", type=int, default=8)
    a = ap.parse_args()
    cards = parse(a.deck)
    out = dp.build_path(a.deck).with_name(a.deck.stem + "-cards.pdf")
    tmp = a.deck.with_name(f".{a.deck.stem}.cards.html")
    tmp.write_text(build(cards, a.per_page), encoding="utf-8")
    try:
        dp.render(tmp, out)
    finally:
        tmp.unlink(missing_ok=True)
    for c in cards:
        print(f'id {c["cid"]}  now#{c["n"]:<3} {c["part"][:7]:<8} {(c["eyebrow"] or c["head"])[:56]}')
    print(f"\n{len(cards)} cards → {out}")

if __name__ == "__main__":
    main()
