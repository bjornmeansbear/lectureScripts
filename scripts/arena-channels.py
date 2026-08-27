#!/usr/bin/env python3
"""List your Are.na channels, formatted for SURFACES.md.

Why this exists: several are.na channels are named out loud in workshop
transcripts with no URL recorded anywhere (see SURFACES.md). This recovers them.

Setup:
  1. Get a personal access token at https://www.are.na/settings/oauth
  2. Put it in .env at the repo root (already gitignored):
         ARENA_TOKEN=your_token_here
  3. python3 scripts/arena-channels.py            # all channels
     python3 scripts/arena-channels.py type      # only titles/slugs matching "type"

Spec: Are.na v3 OpenAPI, https://api.are.na/v3/openapi
A local copy lives at ~/Code/sentence-a-day/openapi
"""

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.are.na"


def load_token():
    for var in ("ARENA_TOKEN", "ARENA_ACCESS_TOKEN", "ARENA_API_TOKEN"):
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
                if key.strip() in ("ARENA_TOKEN", "ARENA_ACCESS_TOKEN", "ARENA_API_TOKEN"):
                    return val.strip().strip("'\"")
    sys.exit(
        "No token found. Add ARENA_TOKEN=... to .env, or export it.\n"
        "Get one at https://www.are.na/settings/oauth"
    )


def get(path, token, **params):
    url = f"{API}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        # Cloudflare in front of api.are.na rejects urllib's default UA (error 1010)
        "User-Agent": "lectureScripts-arena-channels/1.0 (+https://github.com/bjornmeansbear/lectureScripts)",
    })
    try:
        with urllib.request.urlopen(req) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")[:300]
        sys.exit(f"HTTP {exc.code} on {path}\n{body}")


FILTER = (sys.argv[1].lower() if len(sys.argv) > 1 else "")


def main():
    token = load_token()

    me = get("/v3/me", token)
    user = me.get("user") or me
    uid = user.get("id")
    slug = user.get("slug") or ""
    print(f"# Are.na channels — {user.get('username') or slug}\n", file=sys.stderr)

    channels, page = [], 1
    while True:
        data = get(f"/v3/users/{uid}/contents", token,
                   type="Channel", per=100, page=page, sort="created_at_asc")
        items = data.get("contents") or data.get("data") or []
        if not items:
            break
        channels.extend(items)
        if len(items) < 100:
            break
        page += 1

    print(f"{len(channels)} channels\n", file=sys.stderr)

    for ch in channels:
        cslug = ch.get("slug") or ch.get("id")
        title = ch.get("title") or "(untitled)"
        counts = ch.get("counts") or {}
        count = ch.get("length")
        if count is None:
            count = counts.get("contents", counts.get("blocks"))
        vis = ch.get("visibility") or ch.get("status") or ""
        bits = []
        if count is not None:
            bits.append(f"{count} blocks")
        if vis and vis != "public":
            bits.append(vis)
        tail = " — " + ", ".join(bits) if bits else ""
        if not FILTER or FILTER in title.lower() or FILTER in str(cslug).lower():
            print(f"- [{title}](https://www.are.na/{slug}/{cslug}){tail}")


if __name__ == "__main__":
    main()
