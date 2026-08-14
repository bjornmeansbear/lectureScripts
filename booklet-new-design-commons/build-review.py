#!/usr/bin/env python3
"""
Build a single printable HTML review document from the booklet drafts.

    python3 build-review.py && open review.html

Then Cmd+P in the browser and "Save as PDF".

Why this exists rather than just printing the .md files: the TO DO blocks in each
draft are HTML comments, so every normal Markdown renderer hides them. Those notes
are the whole point of a review pass, so this script turns them into visible boxes.

No dependencies. Handles the Markdown subset these drafts actually use.
"""

import re
import html
from pathlib import Path

HERE = Path(__file__).parent
ORDER = ["OUTLINE.md"] + sorted(
    p.name for p in HERE.glob("0*.md")
)
OUT = HERE / "review.html"


# ---------------------------------------------------------------- markdown

def inline(t):
    """Inline markup. Order matters: code first so its contents stay literal."""
    out, codes = [], []

    def stash(m):
        codes.append(m.group(1))
        return f"\x00{len(codes)-1}\x00"

    t = re.sub(r"`([^`]+)`", stash, t)
    t = html.escape(t, quote=False)

    t = re.sub(r"\[\^([\w-]+)\]", r'<sup class="fn">\1</sup>', t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"&lt;(https?://[^&\s]+)&gt;", r'<a href="\1">\1</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)

    for i, c in enumerate(codes):
        t = t.replace(f"\x00{i}\x00", f"<code>{html.escape(c)}</code>")
    return t


def convert(md):
    lines, out = md.split("\n"), []
    i, n = 0, len(md.split("\n"))
    para, listbuf, listtag, quote = [], [], None, []

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def flush_list():
        nonlocal listtag
        if listbuf:
            out.append(f"<{listtag}>" + "".join(listbuf) + f"</{listtag}>")
            listbuf.clear()
            listtag = None

    def flush_quote():
        if quote:
            body = "".join(f"<p>{inline(q)}</p>" for q in quote if q.strip())
            out.append(f"<blockquote>{body}</blockquote>")
            quote.clear()

    def flush_all():
        flush_para(); flush_list(); flush_quote()

    while i < n:
        ln = lines[i]

        # TO DO comment blocks -> visible review boxes
        if ln.strip().startswith("<!--"):
            flush_all()
            block = []
            if "-->" in ln:
                block.append(ln.strip()[4:].replace("-->", ""))
            else:
                i += 1
                while i < n and "-->" not in lines[i]:
                    block.append(lines[i]); i += 1
            text = "\n".join(block).strip()
            head = "Notes"
            if text.upper().startswith("TO DO"):
                head, text = "To do", text[5:].lstrip(":").strip()
            elif text.upper().startswith("STATUS"):
                head = "Status"
            items = [x.strip() for x in re.split(r"\n\s*-\s+", "\n" + text) if x.strip()]
            body = "".join(f"<li>{inline(re.sub(r'\\s+', ' ', it))}</li>" for it in items)
            out.append(f'<aside class="todo"><h4>{head}</h4><ul>{body}</ul></aside>')
            i += 1
            continue

        if ln.startswith("#"):
            flush_all()
            lvl = len(ln) - len(ln.lstrip("#"))
            out.append(f"<h{lvl}>{inline(ln[lvl:].strip())}</h{lvl}>")
        elif ln.strip() in ("---", "***"):
            flush_all()
            out.append("<hr>")
        elif ln.startswith(">"):
            flush_para(); flush_list()
            quote.append(ln.lstrip(">").strip())
        elif re.match(r"^\s*[-*]\s+", ln):
            flush_para(); flush_quote()
            if listtag == "ol":
                flush_list()
            listtag = "ul"
            listbuf.append(f"<li>{inline(re.sub(r'^\s*[-*]\s+', '', ln))}</li>")
        elif re.match(r"^\s*\d+\.\s+", ln):
            flush_para(); flush_quote()
            if listtag == "ul":
                flush_list()
            listtag = "ol"
            listbuf.append(f"<li>{inline(re.sub(r'^\s*\d+\.\s+', '', ln))}</li>")
        elif ln.startswith("|"):
            flush_all()
            rows = []
            while i < n and lines[i].startswith("|"):
                rows.append(lines[i]); i += 1
            cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows]
            cells = [c for c in cells if not all(re.fullmatch(r":?-+:?", x) for x in c)]
            thead = "".join(f"<th>{inline(c)}</th>" for c in cells[0])
            tbody = "".join(
                "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>"
                for row in cells[1:]
            )
            out.append(f"<table><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table>")
            continue
        elif not ln.strip():
            flush_all()
        else:
            flush_quote()
            para.append(ln.strip())
        i += 1

    flush_all()
    return "\n".join(out)


def split_frontmatter(md):
    if not md.startswith("---"):
        return {}, md
    end = md.find("\n---", 3)
    if end == -1:
        return {}, md
    raw, body = md[3:end], md[end + 4:]
    meta = {}
    for line in raw.split("\n"):
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m and m.group(2).strip():
            meta[m.group(1)] = m.group(2).strip()
    return meta, body


# ---------------------------------------------------------------- assemble

CSS = """
:root{
  --ink:#2b2118; --rule:#2b2118; --muted:#6b5d4f;
  --accent:#c0356c; --paper:#fffdf8; --note:#f3ece0;
  --measure:34em;
}
*{box-sizing:border-box}
body{
  margin:0; background:var(--paper); color:var(--ink);
  font:16px/1.55 ui-serif,Charter,Georgia,"Times New Roman",serif;
  -webkit-font-smoothing:antialiased;
}
.sheet{max-width:52em; margin:0 auto; padding:4rem 3rem 6rem}
/* wide right gutter: leave room to write */
h1,h2,h3,h4,p,ul,ol,blockquote,table,hr{max-width:var(--measure)}

h1{font-size:1.9rem; line-height:1.15; margin:0 0 .25rem; letter-spacing:-.01em}
h2{font-size:1.15rem; margin:2.4rem 0 .6rem; border-bottom:1px solid var(--rule); padding-bottom:.2rem}
h3{font-size:1rem; margin:1.8rem 0 .4rem; font-style:italic; font-weight:600}
h4{font-size:.75rem; margin:0 0 .4rem; text-transform:uppercase; letter-spacing:.09em}
p{margin:0 0 .85rem; hyphens:auto}
ul,ol{margin:0 0 .9rem; padding-left:1.2rem}
li{margin:.2rem 0}
blockquote{
  margin:1rem 0 1.1rem; padding:.1rem 0 .1rem 1rem;
  border-left:2px solid var(--accent); color:var(--muted); font-style:italic;
}
blockquote p{margin:.2rem 0}
code{font:.85em/1 ui-monospace,SFMono-Regular,Menlo,monospace; background:var(--note); padding:.1em .3em}
a{color:inherit; text-decoration:none; border-bottom:1px solid var(--accent)}
sup.fn{color:var(--accent); font-size:.65em; vertical-align:super; margin-left:.1em}
sup.fn::before{content:"["} sup.fn::after{content:"]"}
hr{border:0; border-top:1px solid var(--rule); margin:2rem 0; opacity:.35}
table{border-collapse:collapse; font-size:.82rem; max-width:100%; width:100%}
th,td{border:1px solid var(--rule); padding:.35rem .5rem; text-align:left; vertical-align:top}
th{background:var(--note)}

/* review apparatus */
.meta{font-size:.72rem; text-transform:uppercase; letter-spacing:.1em; color:var(--muted); margin:0 0 2rem}
.meta .status{border:1px solid var(--accent); color:var(--accent); padding:.1em .5em; margin-left:.5em}
.todo{
  max-width:var(--measure); margin:1.6rem 0; padding:.9rem 1rem;
  background:var(--note); border-left:3px solid var(--accent);
  font-family:ui-sans-serif,system-ui,sans-serif; font-size:.78rem; line-height:1.45;
}
.todo h4{color:var(--accent); margin-bottom:.3rem}
.todo ul{padding-left:1.1rem; margin:0}
.essay{page-break-before:always; padding-top:1rem}
.essay:first-of-type{page-break-before:avoid}
.notespace{height:0}

@media print{
  @page{ size:letter; margin:0.85in 2.1in 0.9in 0.9in; }
  body{font-size:10.5pt; background:#fff}
  .sheet{padding:0; max-width:none}
  :root{--measure:100%}
  a{border-bottom:none}
  a[href^="http"]::after{content:" (" attr(href) ")"; font-size:.75em; color:var(--muted); word-break:break-all}
  .todo{background:#f2f2f2; -webkit-print-color-adjust:exact; print-color-adjust:exact; break-inside:avoid}
  blockquote{break-inside:avoid}
  h2,h3{break-after:avoid}
  .notespace{height:1.2in}   /* breathing room at the end of each essay */
}
"""

def main():
    parts = []
    for name in ORDER:
        p = HERE / name
        if not p.exists():
            continue
        meta, body = split_frontmatter(p.read_text())
        bits = []
        if meta.get("part"):
            bits.append(meta["part"])
        if meta.get("status"):
            bits.append(f'<span class="status">{html.escape(meta["status"])}</span>')
        header = f'<p class="meta">{" · ".join(bits)}</p>' if bits else ""
        parts.append(
            f'<section class="essay"><!-- {name} -->\n'
            f'{convert(body).split("</h1>")[0]}</h1>\n{header}'
            f'{"</h1>".join(convert(body).split("</h1>")[1:])}'
            f'<div class="notespace"></div></section>'
            if "</h1>" in convert(body)
            else f'<section class="essay">{header}{convert(body)}<div class="notespace"></div></section>'
        )

    doc = (
        "<!doctype html><html lang='en'><head><meta charset='utf-8'>"
        "<title>A New Design Commons — review draft</title>"
        f"<style>{CSS}</style></head><body><div class='sheet'>"
        + "\n".join(parts)
        + "</div></body></html>"
    )
    OUT.write_text(doc)
    print(f"wrote {OUT}  ({len(ORDER)} files)")
    print("open review.html  →  Cmd+P  →  Save as PDF")


if __name__ == "__main__":
    main()
