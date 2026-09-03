#!/usr/bin/env python3
"""Dump a Figma slide deck to markdown — frame order, names, and on-slide text.

Why this exists: several lectures in this repo have a finished deck and no script
(lecture-some-semiotics is the clearest case). For those, the deck IS the only
record of the argument, and it is locked inside Figma where nothing can grep it,
diff it, or cross-reference it from SHARED-COMPONENTS.md. This pulls it out.

Hidden frames are marked `[hidden]` rather than dropped. Hiding a frame is how
a slide gets benched from the current cut of a talk while staying in the file,
so the dump shows what is on the bench alongside what is in — the Design for
the Future deck keeps finished Clarke and Dator slides that way.

The output is a dated snapshot. Figma stays source of truth. Regenerate, don't edit.

Setup:
  1. Get a personal access token: Figma → Settings → Security → personal access
     tokens. It needs the `file_content:read` scope.
  2. Put it in .env at the repo root (already gitignored):
         FIGMA_TOKEN=your_token_here
  3. Pass any URL that names a page (a /design/ or /proto/ link with node-id):

     python3 scripts/figma-slides.py "https://figma.com/design/KEY/Name?node-id=1082-2"
     python3 scripts/figma-slides.py "<url>" -o lecture-some-semiotics/slides.md

Docs: https://www.figma.com/developers/api#get-file-nodes-endpoint
"""

import argparse
import datetime
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.figma.com"
RETRIES = 4  # Figma throttles a burst of page requests; a loop over a whole file hits it


def fetch(url, token, what):
    """GET with backoff on throttling and transient server errors."""
    req = urllib.request.Request(url, headers={
        "X-Figma-Token": token, "Accept": "application/json"})
    for attempt in range(RETRIES):
        try:
            with urllib.request.urlopen(req) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503, 504) and attempt < RETRIES - 1:
                wait = 2 ** attempt
                print(f"  {exc.code} on {what}, retrying in {wait}s…", file=sys.stderr)
                time.sleep(wait)
                continue
            body = exc.read().decode("utf-8", "replace")[:400]
            hint = ""
            if exc.code == 403:
                hint = ("\nA 403 usually means the token lacks file_content:read, "
                        "or you can't see this file.")
            sys.exit(f"HTTP {exc.code} on {what}\n{body}{hint}")


def load_token():
    for var in ("FIGMA_TOKEN", "FIGMA_ACCESS_TOKEN", "FIGMA_PAT"):
        if os.environ.get(var):
            return os.environ[var]
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    envfile = os.path.join(here, ".env")
    if os.path.exists(envfile):
        with open(envfile, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, val = line.partition("=")
                if key.strip() in ("FIGMA_TOKEN", "FIGMA_ACCESS_TOKEN", "FIGMA_PAT"):
                    return val.strip().strip("'\"")
    sys.exit(
        "No token found. Add FIGMA_TOKEN=... to .env, or export it.\n"
        "Get one at Figma → Settings → Security → personal access tokens "
        "(scope: file_content:read)."
    )


def parse_target(target):
    """Accept a Figma URL or a bare 'KEY NODE' pair. Returns (file_key, node_id)."""
    if target.startswith("http"):
        # /design/KEY/Name, /proto/KEY/Name, /file/KEY/Name, /board/KEY/Name,
        # and branch URLs /design/KEY/branch/BRANCHKEY/Name (branch key wins).
        m = re.search(r"/(?:design|proto|file|board|slides)/([0-9A-Za-z]{22,128})", target)
        if not m:
            sys.exit(f"Could not find a file key in: {target}")
        key = m.group(1)
        branch = re.search(r"/branch/([0-9A-Za-z]{22,128})", target)
        if branch:
            key = branch.group(1)
        q = urllib.parse.parse_qs(urllib.parse.urlparse(target).query)
        # A /proto/ link's node-id is whichever slide the prototype starts on;
        # its page-id is the deck. For every other URL shape, node-id is the target.
        if "/proto/" in target:
            node = (q.get("page-id") or q.get("node-id") or [None])[0]
        else:
            node = (q.get("node-id") or q.get("page-id") or [None])[0]
        return key, (node.replace("-", ":") if node else None)
    parts = target.split()
    if len(parts) == 1:
        return parts[0], None
    if len(parts) != 2:
        sys.exit("Pass a Figma URL, or 'FILEKEY NODEID'.")
    return parts[0], parts[1].replace("-", ":")


def get_nodes(key, node, token):
    url = f"{API}/v1/files/{key}/nodes?" + urllib.parse.urlencode({"ids": node})
    return fetch(url, token, f"{node} in {key}")


def get_pages(key, token):
    """Top-level canvases only — depth=1 keeps this cheap on a big file."""
    doc = fetch(f"{API}/v1/files/{key}?depth=1", token, f"page list for {key}")
    return doc.get("name"), (doc.get("document") or {}).get("children") or []


def walk_text(node, out, max_text):
    """Collect every TEXT node's characters, in document order."""
    if node.get("type") == "TEXT":
        chars = (node.get("characters") or "").strip()
        chars = re.sub(r"\s+", " ", chars)
        if chars:
            if max_text and len(chars) > max_text:
                chars = chars[:max_text].rstrip() + "…"
            out.append((chars, node.get("visible", True)))
    for kid in node.get("children") or []:
        walk_text(kid, out, max_text)
    return out


def main():
    ap = argparse.ArgumentParser(
        description="Dump a Figma page's frames and on-slide text to markdown.")
    ap.add_argument("target", help="Figma URL with a node-id, or 'FILEKEY NODEID'")
    ap.add_argument("-o", "--out", help="write here instead of stdout")
    ap.add_argument("--list-pages", action="store_true",
                    help="list every page in the file and exit — one per line, "
                         "'NODEID<tab>NAME', so a shell loop can dump them all")
    ap.add_argument("--min-width", type=float, default=1000.0,
                    help="ignore frames narrower than this (default 1000, "
                         "which drops scratch groups and keeps 1920px slides)")
    ap.add_argument("--all", action="store_true",
                    help="keep every top-level child, whatever its size")
    ap.add_argument("--max-text", type=int, default=500,
                    help="truncate any single text run past this (0 = never)")
    ap.add_argument("--full", action="store_true",
                    help="print every text run on every frame. Off by default: "
                         "these decks build by duplication, so a frame repeats "
                         "its predecessor plus one new thing, and printing the "
                         "carried-over lines every time buries the build")
    ap.add_argument("--row-tolerance", type=float, default=200.0,
                    help="frames within this many px vertically are one section row")
    args = ap.parse_args()

    key, node_id = parse_target(args.target)
    token = load_token()

    if args.list_pages:
        fname, pages = get_pages(key, token)
        print(f"{fname} — {len(pages)} pages", file=sys.stderr)
        for pg in pages:
            print(f"{pg.get('id')}\t{pg.get('name')}")
        return

    if not node_id:
        sys.exit("No node-id in that URL. Use --list-pages to see what's in the "
                 "file, or copy a page-specific link from Figma.")

    print(f"fetching {node_id} from {key}…", file=sys.stderr)
    data = get_nodes(key, node_id, token)
    entry = (data.get("nodes") or {}).get(node_id)
    if not entry:
        sys.exit(f"Node {node_id} not in the response. Wrong page id?")
    page = entry["document"]

    frames = []
    for child in page.get("children") or []:
        box = child.get("absoluteBoundingBox") or {}
        w = box.get("width") or 0
        if not args.all and w < args.min_width:
            continue
        texts = walk_text(child, [], args.max_text)
        frames.append({
            "name": child.get("name") or "(unnamed)",
            "x": box.get("x") or 0,
            "y": box.get("y") or 0,
            "w": w,
            "h": box.get("height") or 0,
            "hidden": not child.get("visible", True),
            "texts": texts,
        })
    frames.sort(key=lambda f: (f["y"], f["x"]))
    print(f"{len(frames)} frames", file=sys.stderr)

    deck_url = f"https://www.figma.com/design/{key}/?node-id={node_id.replace(':', '-')}"
    lines = [
        "---",
        f"what: slide inventory for \"{page.get('name')}\", generated from Figma",
        f"generated: {datetime.date.today().isoformat()}",
        f"deck: {deck_url}",
        "note: snapshot — Figma is source of truth. Regenerate with scripts/figma-slides.py, don't edit.",
        "---",
        "",
        f"# {page.get('name')}",
        "",
        f"{len(frames)} frames. Rows are sections; frames run left to right within a row.",
        "",
    ]

    row_y = None
    prev_texts = set()
    for f in frames:
        if row_y is None or abs(f["y"] - row_y) > args.row_tolerance:
            row_y = f["y"]
            row = [g for g in frames if abs(g["y"] - row_y) <= args.row_tolerance]
            lines += ["", f"## y={int(row_y)} — {len(row)} frames", ""]
        flag = "  `[hidden]`" if f["hidden"] else ""
        lines.append(f"### {f['name']}{flag}")
        lines.append(f"<sub>{int(f['w'])}×{int(f['h'])} at x={int(f['x'])}</sub>")
        lines.append("")
        if f["texts"]:
            carried = 0
            for chars, vis in f["texts"]:
                if not args.full and chars in prev_texts:
                    carried += 1
                    continue
                mark = " `[hidden]`" if not vis else ""
                lines.append(f"- {chars}{mark}")
            if carried:
                lines.append(f"- *(+{carried} carried from the previous frame)*")
        else:
            lines.append("- *(no text — image or drawing only)*")
        prev_texts = {c for c, _ in f["texts"]}
        lines.append("")

    out = "\n".join(lines).rstrip() + "\n"
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(out)
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(out)


if __name__ == "__main__":
    main()
