---
brand: "{Brand name}"
version: 1.0
status: draft # draft | approved. Only the brand owner sets approved.
updated: YYYY-MM-DD
---

# {Brand name} brand kit

Source of truth for every visual and verbal decision. `tokens.css` is generated from this file and must match it.

## 1. Brand core

**Positioning:** For {audience}, {brand} is the {category} that {differentiator}.

**Mission:** {what the brand does every day, and for whom}

**Vision:** {where it is going, with a horizon}

**Values**

| Value | Behavior it produces |
|---|---|
| | |

**Tagline:** {under eight words}

**Story:** {under 120 words: origin, turning point, what it does now}

**Key messages**

| Message | Proof |
|---|---|
| | |

**Attributes:** {attribute 1}, {attribute 2}, {attribute 3}

**Direction:** {chosen paper direction, one line} — {why, one sentence}

**Brand family:** {`single brand`, or how this brand relates to its parent or product brands: which kit governs each, and how one appears on the other's materials}

## 2. Color

**Neutrals:** `pure` (true white, black, and grays) or `tinted toward {hue}`. Every neutral follows the same choice.

### Roles

| Token | HEX | RGB | CMYK | Job |
|---|---|---|---|---|
| `--paper` | `#` | | | Page background |
| `--paper-alt` | `#` | | | Raised or alternate surface (cards, bands) |
| `--ink` | `#` | | | Body text and headings |
| `--ink-muted` | `#` | | | Secondary text, captions |
| `--rule` | `#` | | | Borders, dividers, rule lines |
| `--accent` | `#` | | | {the one job of the accent} |
| `--on-accent` | `#` | | | Text and icons placed on accent |
| `--success` | `#` | | | Positive state |
| `--warning` | `#` | | | Caution state |
| `--danger` | `#` | | | Error and destructive state |
| `--info` | `#` | | | Neutral notice |

At most six brand roles (paper through accent). State colors do not count toward the limit.

### Tonal steps

Lighter or darker steps of the brand hues. They do not count as roles.

| Primitive | HEX | Job |
|---|---|---|
| | | |

### Print

| Role | CMYK | Pantone (closest, confirm with the print shop) |
|---|---|---|
| | | |

### Usage ratio

{paper} {n}% · {ink} {n}% · {others} {n}%

### Contrast

Computed with `scripts/contrast.py`, never estimated. Body text needs 4.5:1, large text and UI parts (including form field borders) need 3:1.

| Foreground | Background | Ratio | Pass |
|---|---|---|---|
| `--ink` | `--paper` | | |
| `--ink` | `--paper-alt` | | |
| `--ink-muted` | `--paper` | | |
| `--on-accent` | `--accent` | | |
| `--accent` | `--paper` | | |
| Form field border | `--paper` | | |
| `--danger` | `--paper` | | |

### Dark mode

`none` or a separate table with the same roles. Designed on its own, never an inversion of the light palette, with its own contrast table.

## 3. Typography

| Role | Family | Weights | License | Fallback stack |
|---|---|---|---|---|
| Display (headings) | | | | |
| Text (body, UI) | | | | |
| Mono (code, data only, optional) | | | | |

At most two families. One family may fill both display and text. The extra mono row is only for a separate code or data face.

**Italic:** `not allowed` or `allowed for {where}`

**Weights in use:** {list}. Never 900 or black.

### Hierarchy

Sizes are Tailwind type scale steps.

| Level | Mobile | Desktop | Weight | Line height | Tracking |
|---|---|---|---|---|---|
| Display | | | | | |
| H1 | | | | | |
| H2 | | | | | |
| H3 | | | | | |
| Lead | | | | | |
| Body | | | | | |
| Small | | | | | |
| Caption | | | | | |
| Button | | | | | |

**Language support:** confirm the families render every character the copy needs (for Vietnamese: full diacritics, including stacked marks).

## 4. Paper material

| Property | Value |
|---|---|
| Shadow | `none` or one token, drawn from the ink color |
| Texture | `none` or `{path to grain asset}` with its strength |
| Pattern | `none` or `{pattern built from a logo element}`, where it may appear |
| Rule lines | {width} in `--rule` |
| Base radius | {Tailwind step}, plus where square corners are required |

Never glass: no blur, no translucent surfaces, no glow.

## 5. Logo

**Lockups**

| Lockup | File | Use | Minimum size |
|---|---|---|---|
| Horizontal (primary) | `logo/primary.svg` | Default everywhere | {px} / {mm} |
| Vertical | `logo/vertical.svg` | Square and narrow spaces | {px} / {mm} |
| Logomark | `logo/mark-square.svg` | Avatars, app icons | {px} |
| Favicon | `logo/favicon.svg` | Browser tabs, legible at 24px | 16px |

**Color variants:** `-inverted` (on dark) and `-mono` (`currentColor`) for each lockup.

**PNG:** `logo/png/`, transparent, at 480, 1200, and 2400px wide; favicon at 16, 32, 48, 180px; avatar on a solid background.

**Print files:** PDF, AI, EPS — {available, or pending from the designer}

**Clear space:** {rule in a unit taken from the logo}, which is {px} at the minimum size.

**Don'ts:**
1. {misuse}
2. {misuse}
3. {misuse}
4. {misuse}
5. {misuse}

## 6. Icons

**Set:** {library or custom}

**Weights:** {which weight beside body text, beside headings, for active states}

**Grid:** {size grid}

## 7. Imagery

**Photography:** {subject, light, color treatment}

**Processing:** {allowed crops and ratios, conversions}. No filter, overlay, tint, or vignette.

**Illustration:** {style, line weight, palette roles used}

**Never:** {what to avoid}

## 8. Voice

**Attributes**

1. {X}, not {Y}
2. {X}, not {Y}
3. {X}, not {Y}

**Languages:** {primary language}, {others}

**Form of address:** {how the brand refers to itself and the reader, e.g. "chúng tôi / bạn"}

**Sentence rules:** {length, active voice, punctuation habits}

**Tone by context**

| Context | Tone |
|---|---|
| Website | |
| Social | |
| Email | |
| Sales documents | |

**Lexicon**

| Use | Never use |
|---|---|
| | |

**Sounds like us**

1. "{example}"
2. "{example}"
3. "{example}"

**Not us**

1. "{example}" — {why it misses}
2. "{example}" — {why it misses}
3. "{example}" — {why it misses}

## 9. Signature rules

1. **{Rule name}.** {one sentence} Most likely break: {how}.
2. **{Rule name}.** {one sentence} Most likely break: {how}.
3. **{Rule name}.** {one sentence} Most likely break: {how}.

## 10. Applications

| Template | File | Size | Status |
|---|---|---|---|
| | `templates/{name}.html` | | |

## 11. Open questions

- None
