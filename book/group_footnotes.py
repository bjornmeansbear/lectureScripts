#!/usr/bin/env python3
"""
Post-process pandoc's HTML output: pandoc collects every footnote from the
whole assembled document into one flat, unlabeled <ol> at the very end,
with ids renumbered fn1, fn2, ... in document order — it discards whatever
label the Markdown used, so there's no chapter marker left on the <li>
itself to key off of. For a ten-chapter book that flat list reads as one
undifferentiated wall of notes with no indication of which chapter each
belongs to — exactly the buried structure this pipeline is trying to
avoid for cross-references generally.

assemble.py writes a sidecar (chapter_id, title, footnote_count) per
chapter in reading order next to its output Markdown. Since pandoc's flat
list is in that same document order, this just consumes that many <li>s
at a time per chapter, wraps each run in its own <ol> continuing the
global count (global numbering preserved), and labels it with an <h3>.

Numbering continuation uses `style="counter-reset: list-item N"` rather
than the HTML `start` attribute — WeasyPrint 70 silently ignores `start`
on <ol> (verified directly: every list restarts at 1 regardless), but
does honor the CSS counter it's supposed to be shorthand for.

    python3 group_footnotes.py FILE.html FILE.md.notes.tsv
"""
import re
import sys

FOOTNOTES_ASIDE_RE = re.compile(
    r'<aside id="footnotes"[^>]*>.*?<ol>(.*?)</ol>\s*</aside>', re.S)
LI_RE = re.compile(r'<li id="fn\d+".*?</li>', re.S)


def run(html_path, notes_path):
    html = open(html_path, encoding="utf-8").read()

    chapters = []
    with open(notes_path, encoding="utf-8") as f:
        for line in f:
            chapter_id, title, count = line.rstrip("\n").split("\t")
            chapters.append((chapter_id, title, int(count)))

    m = FOOTNOTES_ASIDE_RE.search(html)
    if not m:
        return  # no footnotes in this book — nothing to do

    lis = LI_RE.findall(m.group(1))
    if not lis:
        return

    out = ['<h2 class="notes-heading">Notes</h2>']
    i, n = 0, 0
    for chapter_id, title, count in chapters:
        if count == 0:
            continue
        group, i = lis[i:i + count], i + count
        out.append(f'<h3 class="notes-chapter">{title}</h3>')
        out.append(f'<ol style="counter-reset: list-item {n}">')
        out.extend(group)
        out.append('</ol>')
        n += len(group)

    if i != len(lis):
        sys.exit(f"group_footnotes.py: sidecar accounts for {i} footnotes "
                  f"but the document has {len(lis)} — assemble.py's count "
                  f"and pandoc's output have drifted apart.")

    replacement = (
        '<aside id="footnotes" class="footnotes footnotes-end-of-document" '
        'role="doc-endnotes">' + "".join(out) + '</aside>'
    )
    html = html[:m.start()] + replacement + html[m.end():]
    open(html_path, "w", encoding="utf-8").write(html)
    print(f"   grouped {n} footnote(s) into per-chapter sections", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: group_footnotes.py FILE.html FILE.md.notes.tsv")
    run(sys.argv[1], sys.argv[2])
