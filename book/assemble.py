#!/usr/bin/env python3
"""
Assemble a directory of chapter .md files (title/part/status frontmatter,
the booklet-new-design-commons convention) into one pandoc-ready Markdown
file: title page, table of contents, part-divider pages, and chapters —
each chapter wrapped in a <section> carrying procedural attributes
(data-mood, data-density) computed from that chapter's own prose, plus
cross-reference links for ideas that recur across chapters.

    python3 assemble.py CHAPTERS_DIR TITLE AUTHOR OUTPUT.md

See book/README.md for what "procedural" means here and why.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
THEMES_FILE = HERE / "themes.txt"

CHAPTER_RE = re.compile(r'^(\d+)-.*\.md$')
FRONTMATTER_RE = re.compile(r'^---\n(.*?)\n---\n', re.S)
TODO_BLOCK_RE = re.compile(r'\n<!--\s*\nTO DO.*\Z', re.S)


# --------------------------------------------------------------- frontmatter

def parse_frontmatter(raw):
    """Flat top-level `key: value` pairs only — enough for title/part/status/
    canonical. Indented list items (e.g. under `sources:`) are ignored."""
    m = FRONTMATTER_RE.match(raw)
    meta = {}
    if not m:
        return meta, raw
    for line in m.group(1).splitlines():
        if line.startswith((" ", "\t")) or not line.strip():
            continue
        key, _, val = line.partition(":")
        if _:
            meta[key.strip()] = val.strip()
    body = raw[m.end():]
    return meta, body


FOOTNOTE_LABEL_RE = re.compile(r'\[\^([\w-]+)\]')


def namespace_footnotes(body, chapter_id):
    """Each chapter file was drafted standalone, so short footnote labels
    like [^a] or [^keedy] repeat across chapters. Concatenated into one
    document those collide — pandoc keeps only the first definition and
    silently reuses it for every later reference of the same label
    (surfaces as a 'Duplicate note reference' warning, not an error, so
    it's easy to ship wrong footnotes without noticing). Prefixing every
    label with the chapter id keeps each chapter's footnotes scoped to
    itself."""
    return FOOTNOTE_LABEL_RE.sub(rf'[^{chapter_id}-\1]', body)


def strip_todo_block(body):
    """Drop a trailing HTML-comment TO DO block. Pandoc would drop it from
    the rendered output anyway (HTML comments don't render), but stripping
    it here keeps it out of the word/sentence counts that drive mood and
    density — a chapter's editorial notes-to-self shouldn't shape its own
    typography."""
    return TODO_BLOCK_RE.sub("", body).rstrip() + "\n"


# ----------------------------------------------------------- text analysis

WORD_RE = re.compile(r"[A-Za-z']+")
SENTENCE_SPLIT_RE = re.compile(r'(?<=[.!?])\s+')
SECOND_PERSON_RE = re.compile(r"\b(you|your|yours|yourself|you're|youre)\b", re.I)


def analyze(body):
    """Two procedural parameters, both computed from the chapter's own
    prose rather than assigned by hand:

    mood    — "lecture" (direct address, spoken cadence) or "essay"
              (written register), from second-person pronoun density and
              question-mark density. Calibrated against this booklet's own
              nine chapters: the polished introduction and a not-yet-drafted
              placeholder read as "essay"; everything still carrying its
              lecture-delivery voice reads as "lecture."
    density — "brisk" / "measured" / "dense", from average sentence length.

    Thresholds are fixed constants tuned once against real chapter text
    (see book/README.md) rather than exposed as options — the point is
    that the *content* decides, not a knob a person turns per chapter.
    """
    words = WORD_RE.findall(body)
    word_count = len(words) or 1
    sentences = [s for s in SENTENCE_SPLIT_RE.split(body) if s.strip()]
    sentence_count = len(sentences) or 1

    avg_sentence_len = word_count / sentence_count
    second_person_pct = 100 * len(SECOND_PERSON_RE.findall(body)) / word_count
    question_pct = 100 * body.count("?") / sentence_count

    direct_address_score = second_person_pct + question_pct
    mood = "lecture" if direct_address_score >= 2.0 else "essay"

    if avg_sentence_len < 13:
        density = "brisk"
    elif avg_sentence_len >= 16:
        density = "dense"
    else:
        density = "measured"

    return {
        "mood": mood,
        "density": density,
        "word_count": len(words),
        "avg_sentence_len": round(avg_sentence_len, 1),
        "direct_address_score": round(direct_address_score, 2),
    }


# ----------------------------------------------------------- cross-references

def load_themes():
    if not THEMES_FILE.exists():
        return []
    lines = [
        l.strip() for l in THEMES_FILE.read_text().splitlines()
        if l.strip() and not l.strip().startswith("#")
    ]
    return sorted(set(lines), key=len, reverse=True)


def tag_recurrences(body, chapter_id, themes, first_seen):
    """Mutates `first_seen` ({theme_lower: chapter_id}) in place. Returns the
    body with at most one link-ified recurrence per theme per chapter,
    pointing back at the chapter where that theme first appeared. The
    origin chapter's own occurrence is left untouched."""
    for theme in themes:
        pattern = re.compile(r'\b' + re.escape(theme) + r'\b', re.I)
        key = theme.lower()
        if key not in first_seen:
            if pattern.search(body):
                first_seen[key] = chapter_id
            continue
        origin = first_seen[key]
        if origin == chapter_id:
            continue

        def link_once(m, origin=origin):
            return f"[{m.group(0)}](#{origin})"

        body = pattern.sub(link_once, body, count=1)
    return body


# --------------------------------------------------------------- assembly

def section(tag_open, title_line, body):
    return f"{tag_open}\n\n{title_line}\n\n{body}\n\n</section>\n\n"


def build(chapters_dir, title, author, out_path):
    files = sorted(
        (p for p in chapters_dir.glob("*.md") if CHAPTER_RE.match(p.name)),
        key=lambda p: int(CHAPTER_RE.match(p.name).group(1)),
    )
    if not files:
        sys.exit(f"assemble.py: no NN-title.md chapter files found in {chapters_dir}")

    themes = load_themes()
    first_seen = {}
    chapters = []

    for path in files:
        num = CHAPTER_RE.match(path.name).group(1)
        chapter_id = f"ch-{num}"
        meta, raw_body = parse_frontmatter(path.read_text(encoding="utf-8"))
        body = strip_todo_block(raw_body)
        body = namespace_footnotes(body, chapter_id)
        chapter_title = meta.get("title", path.stem)
        part = meta.get("part", "")
        status = meta.get("status", "")

        # Strip the chapter's own leading `# Title` line — assemble.py
        # regenerates it with an explicit {#id} so cross-refs have an anchor.
        body = re.sub(r'^\s*#\s+.*\n', '', body, count=1)

        if status.startswith("canonical") or status == "empty":
            stats = {"mood": "essay", "density": "measured",
                      "word_count": 0, "avg_sentence_len": 0,
                      "direct_address_score": 0}
            canonical = meta.get("canonical", "")
            body = (
                f"*This chapter's finished prose lives at "
                f"`{canonical or 'a canonical source noted in its own frontmatter'}` "
                f"and has not been folded into this build yet "
                f"(status: {status}).*\n"
            )
        else:
            stats = analyze(body)
            body = tag_recurrences(body, chapter_id, themes, first_seen)

        # pandoc only emits an <li> for a footnote that's both defined AND
        # referenced — an orphaned definition (defined, never cited in the
        # prose) produces just a warning, no list item, so it has to be
        # excluded here too or this count drifts from pandoc's actual output.
        defined = set(re.findall(rf'^\[\^({re.escape(chapter_id)}-[\w-]+)\]:', body, re.M))
        referenced = set(re.findall(rf'\[\^({re.escape(chapter_id)}-[\w-]+)\](?!:)', body))
        note_count = len(defined & referenced)

        chapters.append({
            "id": chapter_id, "num": num, "title": chapter_title,
            "part": part, "status": status, "body": body,
            "note_count": note_count, **stats,
        })

    # ---- report (stderr): the procedural decisions, made visible ----
    print(f"{'chapter':<32} {'mood':<8} {'density':<10} words  avg-sent  score", file=sys.stderr)
    for c in chapters:
        print(f"{c['id']} {c['title']:<28} {c['mood']:<8} {c['density']:<10} "
              f"{c['word_count']:<6} {c['avg_sentence_len']:<9} {c['direct_address_score']}",
              file=sys.stderr)

    out = []
    out.append('<section class="titlepage">\n\n')
    out.append(f"# {title} {{.book-title}}\n\n")
    out.append(f"*{author}*\n\n")
    out.append("</section>\n\n")

    out.append('<nav class="toc">\n\n')
    out.append("## Contents {.toc-heading}\n\n")
    prev_part = None
    for c in chapters:
        if c["part"] != prev_part:
            out.append(f'<p class="toc-part">{c["part"]}</p>\n\n')
            prev_part = c["part"]
        out.append(f'- [{c["title"]}](#{c["id"]})\n')
    out.append("\n</nav>\n\n")

    prev_part = None
    for c in chapters:
        if c["part"] != prev_part:
            out.append(section(
                f'<section class="part-divider" data-part="{c["part"]}">',
                f'# {c["part"]} {{.part-title}}',
                "",
            ))
            prev_part = c["part"]

        kicker = f'<p class="kicker">{c["part"]} &middot; Chapter {c["num"]}</p>\n\n'
        heading = f'# {c["title"]} {{#{c["id"]}}}'
        out.append(section(
            f'<section class="chapter" data-mood="{c["mood"]}" '
            f'data-density="{c["density"]}" data-index="{c["num"]}">',
            kicker + heading,
            c["body"],
        ))

    out_path.write_text("".join(out), encoding="utf-8")
    print(f"-> {out_path}  ({len(chapters)} chapters)", file=sys.stderr)

    # Sidecar for group_footnotes.py: pandoc renumbers every footnote id to
    # a flat fn1, fn2, ... in its HTML output regardless of the label used
    # in Markdown, so there's no chapter marker left to key off of there.
    # This records how many footnote definitions each chapter contributed,
    # in chapter order, so the post-processor can split pandoc's one flat
    # endnotes list back into per-chapter sections by simply consuming that
    # many list items at a time.
    notes_path = out_path.with_suffix(out_path.suffix + ".notes.tsv")
    with notes_path.open("w", encoding="utf-8") as f:
        for c in chapters:
            f.write(f"{c['id']}\t{c['title']}\t{c['note_count']}\n")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit("usage: assemble.py CHAPTERS_DIR TITLE AUTHOR OUTPUT.md")
    build(Path(sys.argv[1]), sys.argv[2], sys.argv[3], Path(sys.argv[4]))
