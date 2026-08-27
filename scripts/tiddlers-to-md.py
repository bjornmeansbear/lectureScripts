#!/usr/bin/env python3
"""Render a set of tiddlers into one readable markdown document.

The inverse of md-to-tiddlers.py, and the point of Pure Content: the tiddlers stay
canonical, this is a rendering. Re-run it whenever the tiddlers change; never edit
the output by hand.

  tiddlers-to-md.py --tag "Pure Content" --out lecture-pure-content/compiled.md
  tiddlers-to-md.py --titles "A" "B" --out foo.md --heading "Lecture: Foo"
"""
import argparse, os, re, sys

TIDDLERS = os.path.expanduser("~/Code/sentence-a-day/sad2021tw/tiddlers")


def read(path):
    raw = open(path, encoding="utf-8").read()
    head, _, body = raw.partition("\n\n")
    meta = {}
    for line in head.split("\n"):
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip()
    return meta, body.strip()


def all_tiddlers():
    out = {}
    for fn in os.listdir(TIDDLERS):
        if not fn.endswith(".tid"):
            continue
        try:
            meta, body = read(os.path.join(TIDDLERS, fn))
        except Exception:
            continue
        if meta.get("title"):
            out[meta["title"]] = (meta, body)
    return out


def to_md(tw):
    out, quote = [], False
    for line in tw.split("\n"):
        if line.strip() == "<<<":
            quote = not quote
            continue
        if re.match(r"^<<list-links", line.strip()):
            continue
        for n in range(6, 0, -1):                       # !!! headings (not # — that's a list in TW)
            line = re.sub(r"^!{%d} ?" % n, "#" * n + " ", line)
        line = re.sub(r"^(#+) ", lambda m: m.group(1) + " ", line)
        line = re.sub(r"^\*+ ", lambda m: "  " * (len(m.group(0).strip()) - 1) + "- ", line)
        line = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"[\1](\2)", line)   # [[text|url]]
        line = re.sub(r"''([^']+)''", r"**\1**", line)
        line = re.sub(r"//([^/\n]+)//", r"*\1*", line)
        out.append(("> " + line) if quote and line.strip() else line)
    return "\n".join(out).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag")
    ap.add_argument("--titles", nargs="*")
    ap.add_argument("--order", nargs="*", help="explicit title order; the rest follow, longest first")
    ap.add_argument("--out", required=True)
    ap.add_argument("--heading", default=None)
    a = ap.parse_args()

    db = all_tiddlers()
    if a.titles:
        sel = [t for t in a.titles if t in db]
    elif a.tag:
        sel = [t for t, (m, _) in db.items()
               if a.tag in re.findall(r"\[\[([^\]]+)\]\]|(\S+)", m.get("tags", "")) or
                  a.tag in [x for pair in re.findall(r"\[\[([^\]]+)\]\]|(\S+)", m.get("tags", "")) for x in pair if x]]
    else:
        sys.exit("need --tag or --titles")

    if a.order:
        head = [t for t in a.order if t in sel]
        sel = head + sorted([t for t in sel if t not in head],
                            key=lambda t: -len(db[t][1].split()))

    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    total = 0
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(f"# {a.heading or a.tag}\n\n")
        fh.write("> **Generated file — do not edit.** Rendered from tiddlers in "
                 "`~/Code/sentence-a-day/sad2021tw/tiddlers`, which are canonical. "
                 f"Regenerate with `scripts/tiddlers-to-md.py`.\n\n")
        fh.write(f"Source tiddlers, in order: {', '.join('`' + t + '`' for t in sel)}\n\n---\n\n")
        for t in sel:
            meta, body = db[t]
            md = to_md(body)
            if not md:
                continue
            total += len(md.split())
            fh.write(f"## {t}\n\n")
            bits = []
            if meta.get("tags"):     bits.append(f"tags: `{meta['tags']}`")
            if meta.get("url"):      bits.append(f"published: <{meta['url']}>")
            if meta.get("modified"): bits.append(f"modified: {meta['modified'][:8]}")
            if bits:
                fh.write("*" + " · ".join(bits) + "*\n\n")
            fh.write(md + "\n\n---\n\n")
    print(f"{a.out}: {len(sel)} tiddlers, {total} words")


if __name__ == "__main__":
    main()
