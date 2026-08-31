# Week 2 deck — image slots

`../di200-wk2-deck.html` declares slots rather than filenames. Each opener slide
carries `data-img` (the slot) and `data-img-brief` (what the image is *for*), and
the deck probes `images/<slot>.jpg` at load. If the file decodes, it gets painted
behind the scrim. If not, the slide falls back to its flat section ground.

**The working build is loud. The presentation build is silent.**
Press <kbd>D</kbd>, or open the deck at `#dev`, to show every unfilled slot's name
and brief on the slide. Without it the room sees nothing — no TODO ever projects.

## The six slots

| § | slot | file to drop in | brief |
|---|---|---|---|
| 2 | `beat-ground` | `beat-ground.jpg` | something built from the ground up out of many small parts — a dry-stone wall, a cairn, a nest. No plan imposed from above. |
| 3 | `beat-ethics` | `beat-ethics.jpg` | working people in their own workplace, absorbed, not posing for anyone. The room belongs to them. |
| 4 | `beat-fifty` | `beat-fifty.jpg` | someone taught to look — a lesson in progress, plain light, no rhetoric. Instruction as ordinary labour. |
| 5 | `beat-round` | `beat-round.jpg` | a threshold — people arriving somewhere, the moment before they know where to go. |
| 6 | `beat-make` | `beat-make.jpg` | many hands over one shared task — sorting, gathering, mending. Nobody doing it alone. |
| 6 | `beat-close` | `beat-close.jpg` | the ground before the work starts — prepared, waiting, nothing harvested yet. |

`beat-ground` is new as of 31 Aug — grounded theory moved to the front of the deck and
needed its own opener. Six slots now, not five.

The briefs are written in the deck's own words, not as search terms. Translating
them into the concrete nouns a keyword API will match is a separate step — keep
the two apart so the original doesn't get flattened.

## A declared axis, not five separate picks

Per RULES.md: pick **one** axis for the whole set and let everything else vary.
The obvious one here is **subject — people at attentive work**, which is what the
week is about and what all five briefs already circle.

Winslow Homer is worth checking first (he recurs across the 2026 decks, and this
week is squarely about attention and instruction):

- *Blackboard*, 1877 — instruction, a lesson mid-delivery → `beat-fifty`
- *The Country School*, 1871 — a room full of people being taught to look → `beat-fifty`
- *Mending the Nets*, 1882 — many hands, one shared repair → `beat-make`
- *The Veteran in a New Field*, 1865 — prepared ground, work not yet done → `beat-close`

`beat-ground` has no obvious Homer. A dry-stone wall or a stacked cairn is the image;
try the Met and Cleveland APIs on the concept rather than searching a named artist.

For a named artist or artwork go to **Wikimedia Commons** — the American museum
APIs can only return what they own, and searching them for a European painter
returns their own Homers every time. For a *concept* brief, go to the museum APIs
(Met, Art Institute, Cleveland), which have real subject indexing.

Filter to public domain and ≥2000px before anything reaches your eye. Upscale caps
at ~2.5×; a projector eats resolution.

## Credits

Write the credit line at pick time, not later. Add it to the slide as a
`data-img-credit` attribute and the deck renders it in the corner automatically
once the image loads:

```html
data-img-credit="Winslow Homer, Blackboard, 1877. National Gallery of Art. Public domain."
```

## Contrast

Same scrim as Week 1 — `brown-8` at `--scrim: 0.80`, computed against the worst
case of a pure-white photograph:

- `gray-0` display text — **9.04:1**, AAA at any size
- `gray-1` eyebrow/credit — **8.00:1**, AAA at any size
- `pink-2` accent — **5.21:1**, AAA large (≥24px, or ≥18.7px bold)

Real photographs run darker, so actual contrast only improves. For an already-dark
image, dial that one slide and recompute — `--scrim: 0.75` gives 7.53 / 6.66 / 4.33,
and `0.70` drops to 6.27 / 5.55 / 3.61, which is AA but not AAA.

```html
<section class="slide s-field opener beat" style="--scrim:0.75" data-img="beat-round" ...>
```

## Sourcing

See `README.md` in this folder for the full public-domain source list. Check the
are.na channel for the deck first, if one gets made — channel membership is
already the curation.
