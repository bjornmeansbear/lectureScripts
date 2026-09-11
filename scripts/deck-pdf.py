#!/usr/bin/env python3
"""Render an HTML slide deck in this repo to a one-slide-per-page PDF.

Why this exists: the decks in lecture-design-thinking/ are single-file HTML
presentations — slides are `<section class="slide">`, hidden except `.on`, laid
out with container-query units against a 16:9 `.stage`. Printing them directly
gives you one slide, because that is genuinely what is on screen.

This makes a temp copy next to the original (so relative image paths still
resolve), rewrites the DOM so every slide gets its own correctly-sized
container-query context, and drives headless Chrome to print it.

Usage:
    python3 scripts/deck-pdf.py lecture-design-thinking/di200-wk1-deck.html
    python3 scripts/deck-pdf.py lecture-design-thinking/*.html
    python3 scripts/deck-pdf.py <deck> -o ~/Desktop/week-one.pdf

Output goes to build/ at the repo root, mirroring the deck's path — these are
generated artifacts, and build/ is gitignored. PDFs do not delta-compress, so a
re-render commits a whole fresh megabyte every time. Use -o to put one somewhere
else, e.g. straight onto the Desktop for a Canvas upload.
"""

import argparse
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import time

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# 1280x720 CSS px = 13.333in x 7.5in at 96dpi — the standard 16:9 slide size,
# so the PDF opens at a familiar page size in Canvas/Preview/Acrobat.
W, H = 1280, 720
TIMEOUT = 300          # per deck; an 82-slide deck takes well under a minute


def _complete(pdf: pathlib.Path) -> bool:
    """A finished PDF ends with %%EOF — guards against reading a half-written file."""
    if not pdf.exists() or pdf.stat().st_size < 1024:
        return False
    with pdf.open("rb") as fh:
        fh.seek(-32, os.SEEK_END)
        return b"%%EOF" in fh.read()

INJECT = """
<style id="deck-pdf">
  @page { size: 13.333in 7.5in; margin: 0; }
  html, body {
    height: auto !important; overflow: visible !important;
    display: block !important; background: #fff !important; margin: 0 !important;
  }
  .nav, .deck-nav, [class*="nav"] { display: none !important; }
  .pdf-page {
    container-type: size;
    position: relative;
    width: %(W)dpx; height: %(H)dpx;
    overflow: hidden;
    break-after: page; page-break-after: always;
  }
  .pdf-page:last-child { break-after: auto; page-break-after: auto; }
  .pdf-page > .slide { display: flex !important; position: absolute; inset: 0; }
  * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
</style>
<script>
  window.addEventListener('load', function () {
    var slides = Array.prototype.slice.call(document.querySelectorAll('.slide'));
    var frag = document.createDocumentFragment();
    slides.forEach(function (s) {
      var page = document.createElement('div');
      page.className = 'pdf-page';
      s.classList.add('on');
      page.appendChild(s);
      frag.appendChild(page);
    });
    var stage = document.querySelector('.stage');
    if (stage && stage.parentNode) stage.parentNode.removeChild(stage);
    document.body.appendChild(frag);
    document.documentElement.setAttribute('data-pdf-ready', slides.length);
  });
</script>
""" % {"W": W, "H": H}


def build_path(src: pathlib.Path) -> pathlib.Path:
    """build/<path relative to repo root>.pdf — outside the tree git tracks."""
    src = src.resolve()
    root = next((p for p in src.parents if (p / ".git").exists()), src.parent)
    try:
        rel = src.relative_to(root)
    except ValueError:
        rel = pathlib.Path(src.name)
    out = root / "build" / rel.with_suffix(".pdf")
    out.parent.mkdir(parents=True, exist_ok=True)
    return out


def render(src: pathlib.Path, out: pathlib.Path) -> int:
    html = src.read_text(encoding="utf-8")
    # inject at the very end so it wins the cascade and runs after the deck's own script
    tmp = src.with_name(f".{src.stem}.pdftmp.html")
    tmp.write_text(html + INJECT, encoding="utf-8")
    profile = tempfile.mkdtemp(prefix="deckpdf-")
    out.unlink(missing_ok=True)
    proc = subprocess.Popen([
        CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
        f"--user-data-dir={profile}",
        "--virtual-time-budget=10000",     # let webfonts and images settle
        "--no-pdf-header-footer",
        f"--print-to-pdf={out}",
        tmp.resolve().as_uri(),
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        # Chrome 152 headless writes the PDF and then does not always exit, so
        # watch the file rather than the process: done when the size stops moving.
        deadline, last, stable = time.time() + TIMEOUT, -1, 0
        while time.time() < deadline:
            if proc.poll() is not None:
                break
            size = out.stat().st_size if out.exists() else 0
            if size and size == last:
                stable += 1
                if stable >= 3 and _complete(out):
                    break
            else:
                stable = 0
            last = size
            time.sleep(1)
        else:
            raise TimeoutError(f"Chrome did not finish {src.name} in {TIMEOUT}s")
    finally:
        if proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                proc.kill()
        tmp.unlink(missing_ok=True)
        shutil.rmtree(profile, ignore_errors=True)
    if not _complete(out):
        raise RuntimeError(f"{out} is truncated or was never written")
    return html.count('<section class="slide')


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("decks", nargs="+", type=pathlib.Path)
    ap.add_argument("-o", "--out", type=pathlib.Path,
                    help="output path (only valid with a single deck)")
    a = ap.parse_args()

    if not os.path.exists(CHROME):
        sys.exit(f"Google Chrome not found at {CHROME}")
    if a.out and len(a.decks) > 1:
        sys.exit("-o takes a single deck")

    for d in a.decks:
        if not d.exists():
            sys.exit(f"no such file: {d}")
        out = a.out or build_path(d)
        n = render(d, out)
        size = out.stat().st_size / 1_048_576
        print(f"{d.name}  →  {out}  ({n} slides, {size:.1f} MB)")


if __name__ == "__main__":
    main()
