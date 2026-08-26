# Deck background images

Drop files here with these exact names and they appear behind the section-opener
slides in `../di200-wk1-deck.html`:

| file | section |
|---|---|
| `beat-history.jpg` | §2 Where it came from |
| `beat-critique.jpg` | §3 The case, and the critique |
| `beat-ethics.jpg` | §5 Ethics |
| `beat-ethnography.jpg` | §6 Looking, writing it down |
| `beat-fieldwork.jpg` | §7 You cannot code a vibe |

Missing files are fine — the slide falls back to a flat dark ground and still reads.

Each beat slide carries a commented-out credit line in the HTML. When you drop a real image
in, uncomment it and write the actual attribution:

```html
<p class="credit">Farm Security Administration, Library of Congress, 1939. Public domain.</p>
```

Until then it stays hidden, so no placeholder text shows on the projected slide.

## Contrast

Each beat lays a `brown-8` scrim over the image at `--scrim: 0.80`. Computed
against the worst case (a pure-white photo under the tint):

- `gray-0` display text — **9.03:1**, AAA at any size
- `gray-1` eyebrow/credit — **7.98:1**, AAA at any size
- `pink-2` accent — **5.20:1**, AAA large (≥24px, or ≥18.7px bold)

Real photographs sit darker than white, so actual contrast runs higher. For an
already-dark photo, dial the scrim down on that slide only:

```html
<section class="slide s-eth opener beat" style="--img:url('images/beat-ethics.jpg'); --scrim:0.70">
```

At 0.70 the numbers drop to 6.29 / 3.62 — AA, not AAA. 0.75 holds AAA for the
white text (7.50) but not the pink accent (4.32).

## Where to get them

All public domain or CC0:

- **Library of Congress, FSA/OWI collection** — Depression-era and wartime federal
  photography. Deep on labor, service work, kitchens, hotels, ordinary interiors.
  loc.gov/collections/fsa-owi-black-and-white-negatives/
- **Smithsonian Open Access** — 4M+ items, CC0. si.edu/openaccess
- **RawPixel public domain** — rawpixel.com/public-domain
- **Flickr Commons** — flickr.com/commons
- **Public Domain Review** — publicdomainreview.org

Full annotated list, with the gratis/libre distinction, lives in
`../../workshop-semiotic-commons/copyright-and-the-commons.md`.
