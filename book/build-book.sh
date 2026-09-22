#!/usr/bin/env bash
# build-book.sh — chapter directory of .md files -> one print-ready book PDF.
#
#   ./build-book.sh CHAPTERS_DIR "Book Title" "Author Name" [output.pdf]
#
# Example:
#   ./build-book.sh ../booklet-new-design-commons "A New Design Commons" \
#       "Kristian Bjornard"
#
# CHAPTERS_DIR must hold NN-slug.md files with the frontmatter this repo's
# essay directories already use (title/part/status, optionally canonical).
# assemble.py does the real work: computes each chapter's mood/density from
# its own prose, tags cross-references, and builds part dividers, a TOC,
# and a title page around the chapters. This script just wires pandoc and
# weasyprint around that.
#
# Requires pandoc and weasyprint (see ~/Code/color-system-and-guidelines
# print/md2pdf.sh — same toolchain, same reasoning: plain text in git,
# diffable, rebuilds without a browser).
set -euo pipefail

CHAPTERS_DIR="${1:?usage: build-book.sh CHAPTERS_DIR \"Title\" \"Author\" [output.pdf]}"
TITLE="${2:?usage: build-book.sh CHAPTERS_DIR \"Title\" \"Author\" [output.pdf]}"
AUTHOR="${3:?usage: build-book.sh CHAPTERS_DIR \"Title\" \"Author\" [output.pdf]}"
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHAPTERS_DIR="$(cd "$CHAPTERS_DIR" && pwd)"

SLUG="$(basename "$CHAPTERS_DIR")"
OUT="${4:-$DIR/output/$SLUG.pdf}"
mkdir -p "$(dirname "$OUT")"

MD="$(mktemp "${TMPDIR:-/tmp}/book.XXXXXX.md")"
HTML="$(mktemp "${TMPDIR:-/tmp}/book.XXXXXX.html")"
NOTES="$MD.notes.tsv"
trap 'rm -f "$MD" "$HTML" "$NOTES"' EXIT

python3 "$DIR/assemble.py" "$CHAPTERS_DIR" "$TITLE" "$AUTHOR" "$MD"

pandoc "$MD" \
  --from=markdown+pipe_tables+hard_line_breaks+autolink_bare_uris+smart \
  --to=html5 \
  --standalone \
  --template="$DIR/book-template.html" \
  --metadata pagetitle="$TITLE" \
  --output "$HTML"

python3 "$DIR/group_footnotes.py" "$HTML" "$NOTES"

weasyprint --stylesheet "$DIR/book.css" "$HTML" "$OUT"
echo "-> $OUT  ($(pdfinfo "$OUT" 2>/dev/null | awk '/^Pages/{print $2}') pages)"
