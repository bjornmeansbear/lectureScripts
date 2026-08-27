#!/usr/bin/env python3
"""Split a markdown lecture/essay into TiddlyWiki chunk tiddlers plus an assembly tiddler.

Follows the pattern Kristian already established in
`Lecture: What Is Sustainable Graphic design? (April 2021)`:
  - one tiddler per `##` section, tagged with the parent lecture title
  - a parent tiddler that is pure assembly — `list:` field plus `{{transclusions}}`

Usage:
  md-to-tiddlers.py <file.md> --title "Lecture: Foo" [--tags "Lecture Bar"] [--write]

Without --write it prints what it would create and stops. Never overwrites.
"""
import argparse, datetime, os, re, sys

TIDDLERS = os.path.expanduser("~/Code/sentence-a-day/sad2021tw/tiddlers")


def stamp(offset=0):
    t = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(milliseconds=offset)
    return t.strftime("%Y%m%d%H%M%S") + f"{t.microsecond // 1000:03d}"


def fname(title):
    # TiddlyWiki's file-title escaping: / \ : ? " < > | * -> _
    return re.sub(r'[\\/:?"<>|*]', "_", title) + ".tid"


def to_tw(md):
    """Markdown -> TiddlyWiki markup."""
    out, in_quote = [], False
    for line in md.split("\n"):
        if line.startswith("> "):
            if not in_quote:
                out.append("<<<"); in_quote = True
            out.append(line[2:])
            continue
        if in_quote and not line.startswith(">"):
            out.append("<<<"); in_quote = False
        line = re.sub(r"^###### ", "!!!!!! ", line)
        line = re.sub(r"^##### ", "!!!!! ", line)
        line = re.sub(r"^#### ", "!!!! ", line)
        line = re.sub(r"^### ", "!!! ", line)
        line = re.sub(r"^## ", "!! ", line)
        line = re.sub(r"^# ", "! ", line)
        line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"[[\1|\2]]", line)
        line = re.sub(r"\*\*([^*]+)\*\*", r"''\1''", line)
        line = re.sub(r"(?<![*\w])\*([^*\n]+)\*(?!\*)", r"//\1//", line)
        line = re.sub(r"^(\s*)- ", lambda m: m.group(1) + "* ", line)
        out.append(line)
    if in_quote:
        out.append("<<<")
    return "\n".join(out).strip()


def split_sections(md):
    """Yield (heading, body) for each ## section. Text before the first ## is the intro."""
    md = re.sub(r"(?s)^---\n.*?\n---\n", "", md)          # strip yaml frontmatter
    md = re.sub(r"(?s)<!--.*?-->", "", md)                 # strip html comments
    parts = re.split(r"(?m)^##\s+(.+)$", md)
    intro = parts[0].strip()
    intro = re.sub(r"(?m)^#\s+.*$", "", intro).strip()     # drop the h1
    intro = re.sub(r"(?m)^>\s*Working title.*$", "", intro).strip()
    secs = []
    for i in range(1, len(parts), 2):
        head, body = parts[i].strip(), parts[i + 1].strip()
        body = re.sub(r"(?m)^---\s*$", "", body).strip()
        if body:
            secs.append((head, body))
    return intro, secs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--title", required=True, help='parent tiddler title, e.g. "Lecture: Foo"')
    ap.add_argument("--tags", default="Lecture", help="tags for the parent tiddler")
    ap.add_argument("--prefix", default="", help="optional prefix for chunk titles")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()

    md = open(a.source, encoding="utf-8").read()
    intro, secs = split_sections(md)
    if not secs:
        sys.exit("No ## sections found.")

    planned, collisions = [], []
    for head, body in secs:
        title = (a.prefix + head).strip()
        path = os.path.join(TIDDLERS, fname(title))
        if os.path.exists(path):
            collisions.append(title)
        planned.append((title, path, to_tw(body)))

    parent_path = os.path.join(TIDDLERS, fname(a.title))
    if os.path.exists(parent_path):
        collisions.append(a.title)

    print(f"source : {a.source}")
    print(f"parent : {a.title}   ({a.tags})")
    print(f"chunks : {len(planned)}\n")
    for title, _, body in planned:
        print(f"  {len(body.split()):>4}w  {title}")
    if collisions:
        print("\nCOLLISIONS — these already exist and will NOT be touched:")
        for c in collisions:
            print("  !", c)
    if not a.write:
        print("\n(dry run — pass --write to create)")
        return

    made = 0
    for i, (title, path, body) in enumerate(planned):
        if os.path.exists(path):
            continue
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(f"created: {stamp(i)}\nmodified: {stamp(i)}\n"
                     f"tags: [[{a.title}]]\ntitle: {title}\ntype: text/vnd.tiddlywiki\n\n{body}\n")
        made += 1

    if not os.path.exists(parent_path):
        listed = " ".join(f"[[{t}]]" for t, _, _ in planned)
        lines = [to_tw(intro), ""] if intro else []
        for title, _, _ in planned:
            lines += [f"!! {title}", "", "{{" + title + "}}", ""]
        with open(parent_path, "w", encoding="utf-8") as fh:
            fh.write(f"created: {stamp()}\nlist: {listed}\nmodified: {stamp()}\n"
                     f"tags: {a.tags}\ntitle: {a.title}\ntype: text/vnd.tiddlywiki\n\n"
                     + "\n".join(lines).strip() + "\n")
        made += 1
    print(f"\nwrote {made} tiddlers")


if __name__ == "__main__":
    main()
