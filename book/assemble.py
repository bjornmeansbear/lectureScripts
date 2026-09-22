#!/usr/bin/env python3
"""
Assemble a directory of chapter .md files (title/part/status frontmatter,
the booklet-new-design-commons convention) into one pandoc-ready Markdown
file: title page, table of contents, part-divider pages, and chapters —
each chapter wrapped in a <section> assigned one of two real, named
typesetting systems (Manutius/Aldine or Brockmann/Swiss, see
compute_visual_params) based on its own prose, plus continuous
content-derived CSS custom properties that modulate within whichever
system it gets, plus cross-reference links for ideas that recur across
chapters.

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


BOLD_LEAD_RE = re.compile(r'^\*\*[^*]+\*\*', re.M)
BLOCKQUOTE_LINE_RE = re.compile(r'^>\s?(.*)$', re.M)


def analyze(body):
    """Raw, per-chapter metrics — all computed from the chapter's own prose,
    none hand-assigned. `build()` normalizes these across the whole book
    (corpus min/max) and turns them into the actual visual parameters; see
    book/README.md for the full list and what each one drives.

    register        — "SPOKEN" or "WRITTEN": a fixed-threshold label for the
                       running head only (a label needs *a* cutoff to be
                       readable at all). The typesetting itself uses the
                       corpus-relative, continuous version of this same
                       score (direct_address_score) instead of the label.
    word_count           — chapter length.
    avg_sentence_len     — sentence rhythm.
    direct_address_score — second-person pronoun density + question density:
                            spoken/direct-address register vs. written.
    bold_lead_per_1000   — paragraphs opening `**Bolded like a label.**`,
                            per 1000 words: chapters built out of labeled,
                            enumerable moves (ch. 08's "Require libre
                            fonts.", "Constrain the image sources.") read as
                            instructional; flowing narrative has none.
    blockquote_pct       — share of the chapter's characters inside a `>`
                            blockquote.
    """
    words = WORD_RE.findall(body)
    word_count = len(words) or 1
    sentences = [s for s in SENTENCE_SPLIT_RE.split(body) if s.strip()]
    sentence_count = len(sentences) or 1

    avg_sentence_len = word_count / sentence_count
    second_person_pct = 100 * len(SECOND_PERSON_RE.findall(body)) / word_count
    question_pct = 100 * body.count("?") / sentence_count
    direct_address_score = second_person_pct + question_pct

    bold_lead_per_1000 = 1000 * len(BOLD_LEAD_RE.findall(body)) / word_count
    bq_chars = sum(len(m) for m in BLOCKQUOTE_LINE_RE.findall(body))
    blockquote_pct = 100 * bq_chars / max(len(body), 1)

    return {
        "register": "SPOKEN" if direct_address_score >= 2.0 else "WRITTEN",
        "word_count": len(words),
        "avg_sentence_len": round(avg_sentence_len, 1),
        "direct_address_score": round(direct_address_score, 2),
        "bold_lead_per_1000": round(bold_lead_per_1000, 2),
        "blockquote_pct": round(blockquote_pct, 2),
    }


# ------------------------------------------------------ visual parameters

def lerp(a, b, t):
    t = max(0.0, min(1.0, t))
    return a + (b - a) * t


def lerp_color(c1, c2, t):
    t = max(0.0, min(1.0, t))
    return tuple(round(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))


def normalize(x, lo, hi):
    if hi - lo < 1e-9:
        return 0.5
    return (x - lo) / (hi - lo)


BROWN_6 = (88, 81, 78)
PINK_7 = (116, 0, 37)


def compute_visual_params(chapters):
    """Second pass, after every chapter's raw metrics are known.

    Earlier version of this function blended five metrics continuously
    within *one* template — every chapter got its own leading/margin/
    indent numbers, but a dial only ever produces dial-sized differences.
    Turning a knob doesn't make a different machine. What actually reads
    as "different and meaningful" is a different *system*: different
    grid logic, different alignment, different relationship between type
    and page. So the top-level decision here is now discrete, and it
    picks between two real, named, historically-grounded templates
    (built out in book.css) rather than a continuously blended default:

    - **Brockmann** (Swiss International Typographic Style, Emil Ruder /
      Josef Müller-Brockmann): strict grid, flush-left ragged-right, no
      justification or hyphenation, sans-serif only, hierarchy from
      weight alone, a big grid-module numeral instead of ornament.
      Chosen when a chapter is more instructional/enumerable than it is
      quotation-or-citation-laden — ch. 08's "Require libre fonts.",
      "Constrain the image sources." is the clear case.
    - **Manutius** (the Aldine press, Venice, 1490s-1510s): justified,
      hyphenated, tight, serif, a single narrow column, a rubricated
      (pink) initial standing in for the hand-colored capitals Aldus's
      printers left space for. Chosen for chapters that lean on quotation
      and citation — the discursive-essay default for this booklet.

    The five metrics don't disappear; they still modulate *within*
    whichever template gets picked (see below), which is where the
    "content decides the details" idea from the first version still
    holds. What changed is that they no longer decide the system itself.

    Every number below is final and literal — no calc()/mix() relied on
    in book.css, just var() lookups — so what you see in the PDF is
    exactly what got computed here, checkable straight from this function.
    """
    reals = [c for c in chapters if c["word_count"] > 0]
    bounds = {
        key: (min(c[key] for c in reals), max(c[key] for c in reals))
        for key in ("word_count", "avg_sentence_len", "direct_address_score",
                    "bold_lead_per_1000")
    }
    apparatus_scores = {
        c["id"]: c["note_count"] * 1000 / c["word_count"] + c["blockquote_pct"]
        for c in reals
    }
    lo_ap, hi_ap = min(apparatus_scores.values()), max(apparatus_scores.values())

    for c in chapters:
        placeholder = c["word_count"] == 0
        if placeholder:
            da_t = sr_t = len_t = instr_t = appar_t = 0.5
        else:
            lo, hi = bounds["direct_address_score"]
            da_t = normalize(c["direct_address_score"], lo, hi)
            lo, hi = bounds["avg_sentence_len"]
            sr_t = normalize(c["avg_sentence_len"], lo, hi)
            lo, hi = bounds["word_count"]
            len_t = normalize(c["word_count"], lo, hi)
            lo, hi = bounds["bold_lead_per_1000"]
            instr_t = normalize(c["bold_lead_per_1000"], lo, hi)
            appar_t = normalize(apparatus_scores[c["id"]], lo_ap, hi_ap)

        # The one discrete decision: more instructional-enumerable than
        # citation/quotation-laden -> Brockmann; otherwise Manutius, the
        # default register for this booklet's discursive essays. Ties
        # (both scores 0, e.g. a chapter with no bold-leads and no
        # apparatus at all) fall to Manutius, the safer default.
        template = "brockmann" if instr_t > appar_t else "manutius"

        label_color = lerp_color(BROWN_6, PINK_7, instr_t)

        if template == "manutius":
            dropcap_em = lerp(2.3, 1.0, da_t) * lerp(1.15, 0.95, len_t)
            vis = {
                "leading": round(lerp(1.30, 1.14, sr_t), 3),
                "indent_em": round(lerp(1.25, 0.0, da_t), 3),
                "para_gap_em": round(lerp(0.0, 1.0, da_t) * lerp(0.7, 1.3, sr_t), 3),
                "rule_pt": round(lerp(3.0, 1.0, da_t), 2),
                "dropcap_em": round(max(1.0, min(2.6, dropcap_em)), 3),
                "h1_size_rem": round(2.1 * lerp(1.18, 1.0, len_t), 3),
                "outer_margin_in": round(lerp(0.55, 1.15, appar_t), 3),
                "columns": 1,
            }
        else:  # brockmann
            vis = {
                # Swiss setting is tight and consistent regardless of
                # content — the grid imposes the rhythm, not the prose —
                # so this range is deliberately narrower than Manutius's.
                "leading": round(lerp(1.28, 1.18, sr_t), 3),
                "indent_em": 0.0,
                "para_gap_em": round(lerp(0.5, 0.8, sr_t), 3),
                "rule_pt": 0.0,
                "dropcap_em": 1.0,
                "h1_size_rem": round(1.9 * lerp(1.12, 1.0, len_t), 3),
                # Grid margins are structural, not content-driven: equal
                # left/right within the gutter constraint, not scaled by
                # apparatus (a Brockmann chapter is low-apparatus by
                # construction, so there's nothing for a wide margin to
                # reserve space for anyway).
                "outer_margin_in": 0.6,
                "columns": 2,
            }

        vis["template"] = template
        vis["label_color"] = "rgb(%d,%d,%d)" % label_color
        vis["label_border_pt"] = round(lerp(0.0, 3.0, instr_t), 2)
        c["vis"] = vis


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
            stats = {"register": "WRITTEN", "word_count": 0,
                     "avg_sentence_len": 0, "direct_address_score": 0,
                     "bold_lead_per_1000": 0, "blockquote_pct": 0}
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

    compute_visual_params(chapters)

    # ---- report (stderr): the procedural decisions, made visible ----
    print(f"{'chapter':<32} {'template':<10} words  avg-sent  da-score  "
          f"instr/1k  apparatus  leading  h1-rem", file=sys.stderr)
    for c in chapters:
        v = c["vis"]
        print(f"{c['id']} {c['title']:<28} {v['template']:<10} "
              f"{c['word_count']:<6} {c['avg_sentence_len']:<9} "
              f"{c['direct_address_score']:<9} {c['bold_lead_per_1000']:<9} "
              f"{v['leading']:<8} {v['h1_size_rem']}",
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
        # data-index repeats on the h1 itself (not just the section) so
        # book.css's Brockmann grid-numeral rule can read it via attr() —
        # attr() only sees the attribute of the element the rule targets,
        # no ancestor lookup without :has(), which WeasyPrint doesn't have.
        heading = f'# {c["title"]} {{#{c["id"]} data-index="{c["num"]}"}}'
        v = c["vis"]
        style = (
            f'--leading:{v["leading"]}; --indent:{v["indent_em"]}em; '
            f'--para-gap:{v["para_gap_em"]}em; --rule-weight:{v["rule_pt"]}pt; '
            f'--dropcap-size:{v["dropcap_em"]}em; --h1-size:{v["h1_size_rem"]}rem; '
            f'--label-color:{v["label_color"]}; --label-border:{v["label_border_pt"]}pt;'
        )
        out.append(section(
            f'<section class="chapter" data-template="{v["template"]}" '
            f'data-register="{c["register"]}" data-index="{c["num"]}" '
            f'style="{style}">',
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

    # Per-chapter page margins: a CSS custom property on the section can't
    # reach @page (margins are a page-box property, not an element one), so
    # apparatus density's effect on margin width needs one named @page per
    # chapter instead. book.css keeps the fixed inner/gutter, top, and
    # bottom margins (binding safety, consistent vertical rhythm); only the
    # outer margin — the side that would hold marginalia — varies here.
    pages_path = out_path.with_suffix(out_path.suffix + ".pages.css")
    with pages_path.open("w", encoding="utf-8") as f:
        for c in chapters:
            outer = c["vis"]["outer_margin_in"]
            f.write(
                f'@page ch-page-{c["num"]} {{}}\n'
                f'@page ch-page-{c["num"]}:right {{ margin-right: {outer}in; }}\n'
                f'@page ch-page-{c["num"]}:left  {{ margin-left: {outer}in; }}\n'
                f'section.chapter[data-index="{c["num"]}"] {{ page: ch-page-{c["num"]}; }}\n\n'
            )


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit("usage: assemble.py CHAPTERS_DIR TITLE AUTHOR OUTPUT.md")
    build(Path(sys.argv[1]), sys.argv[2], sys.argv[3], Path(sys.argv[4]))
