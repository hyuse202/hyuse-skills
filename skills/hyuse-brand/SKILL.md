---
name: hyuse-brand
description: "Builds, documents, or updates a complete brand kit with opaque 'paper, not glass' surfaces (no glass, blur, or translucency): brand core (mission, vision, values, positioning, tagline, story, key messages), color roles with computed contrast and print values, typography with a hierarchy and licenses, logo lockups and file set, icons, imagery, voice, signature rules, and application templates (business card, email signature, letterhead, social, slides, proposal, quotation). Writes brand/BRAND.md, brand/tokens.css, a brand board page, logo files, and templates. Use this skill whenever the user asks for a brand kit, brand board, brand identity, brand guidelines, color palette, font pairing, logo or logomark, voice guide, style guide, or brand templates, or when hyuse-landing stops because the brand kit is missing or incomplete."
---

# Brand Kit

A brand kit is a set of decisions, not a mood board. Every value has a job and a reason, and every other skill reads it instead of inventing its own.

**brief → brand core → direction → system → files → templates → owner approval.**

The output is consumed by `hyuse-landing`, which refuses to start until this kit is approved.

## Scope

Apply to creating a new brand, documenting an existing one, or updating a kit. When a rule here conflicts with a framework default, this file wins. When the brand owner's explicit choice conflicts with a rule, the owner wins, and the kit records that choice.

## Deliverables

All files go in `brand/` at the project root unless the user names another place.

| File | What it is |
|---|---|
| `brand/BRAND.md` | Source of truth, filled from `templates/BRAND.md` in this skill |
| `brand/tokens.css` | CSS custom properties in three layers, filled from `templates/tokens.css` |
| `brand/board.html` | One page brand board for review |
| `brand/logo/*.svg` | Every lockup and color variant listed in BRAND.md section 5 |
| `brand/logo/png/*.png` | Transparent PNGs at three widths, the favicon set, and the avatar |
| `brand/templates/*.html` | Application templates listed in BRAND.md section 10 |
| `brand/view/*.html` | Self-contained copies of the board and templates, for sharing |

`templates/` and `scripts/` paths are relative to this skill's own directory, not to the project.

---

# PART A — Brief, core, and direction

## A1. Pick the mode

| Mode | When | What changes |
|---|---|---|
| **Create** | No brand exists yet | Everything is designed here |
| **Document** | The brand exists as a logo, site, deck, or guide | Extract and record what exists. Never redesign what the owner already has. Only fill real gaps |
| **Update** | `brand/BRAND.md` exists | Change only what was asked, bump `version`, set `status: draft`, regenerate `tokens.css`, the board, and any affected template |

Document mode, when an asset is incomplete:

- **Logo only as a raster image.** Identify the typeface, rebuild the vector from its outlines, and overlay it on the raster until the difference is no more than 1px at the source size. Record that the files are rebuilt, and replace them when the designer's master arrives.
- **No mark or favicon.** Derive it from an element the logo already has, never from a new idea. Show the owner the candidates at 16, 24, and 32px.
- **Facts on the owner's site conflict with each other or with the brief.** List each conflict with its sources and ask. Never pick one silently.

## A2. Brief

Ask in one batch, only for what is missing.

- Brand name, and what it sells or does
- Audience: who, and what they care about
- Three competitors or references, and what to stay away from
- Three brand attributes (for example: precise, warm, unhurried)
- Existing mission, vision, values, tagline, or story, if any
- Existing assets: logo, colors, fonts, site, past materials
- Brand family: is there a parent company or product brands with their own identity?
- Languages the brand writes in
- Fixed constraints: licensed fonts, colors that cannot change
- Print needs: business cards, stationery, signage, and whether a print shop needs Pantone values
- Which application templates are needed first

Unlike a page build, a brand kit may move forward on assumptions, but every assumed or invented value is written as `[ASSUMPTION] value` in BRAND.md and listed in the final report. An assumption is never silent. When the owner asks you to fill the gaps creatively, still mark what you wrote, so they can approve it line by line.

## A3. Brand core

Fill BRAND.md section 1 before any visual work.

- **Positioning:** one sentence. "For {audience}, {brand} is the {category} that {differentiator}." If the owner says positioning is deliberately undecided (for example during a fundraise), write a capability statement from verifiable facts instead, mark it, keep positioning as an open question, and carry on with everything else.
- **Mission:** what the brand does every day, and for whom. One sentence, no adjectives it cannot prove.
- **Vision:** where it is going, with a horizon if the owner has one. One sentence.
- **Values:** three to five. Each is a word plus one line describing the behavior it produces, so it can be checked. Merge overlapping values instead of listing six vague ones.
- **Tagline:** under eight words, in the brand's voice, true without footnotes. Give three options and recommend one.
- **Story:** under 120 words. Origin, turning point, what it does now. Facts only.
- **Key messages:** three to five, each a claim plus the proof that backs it. A message without proof is cut.

Every later decision must serve the positioning (or the capability statement). If a choice cannot be explained by it, drop the choice.

## A4. Direction

Propose two or three directions, all inside the paper family. Paper here means opaque and flat, not glass. It does not mean a warm, cream, or textured look; that is one direction among several. Examples of the range:

- **Monochrome** — pure black on pure white, one typeface, inversion as the only highlight
- **Editorial** — newsprint calm, strong type hierarchy, rule lines, generous margins
- **Stationery** — warm cream stock, quiet ink, one stamped accent
- **Print workshop** — risograph energy, flat spot colors, visible grid
- **Archive** — catalogue cards, labels, mono details, muted ink

For each give: two adjectives, a paper and ink pairing, a type idea, and one signature device (a rule line system, a stamp, a margin note style, a numbered index). Recommend one and say why in one sentence.

**Stop and let the owner pick** before building the system. In Document mode, skip this step and record the existing direction.

---

# PART B — The system

## B1. Paper, never glass

These hold for every part of the kit and every artifact made from it.

- Every surface is opaque. No `backdrop-blur`, no `filter: blur()`, no translucent fills over content.
- No glow, neon, glossy highlights, reflections, or gradients on text or backgrounds.
- Depth comes from paper itself: a change of stock (`--paper` to `--paper-alt`), a rule line, or at most one soft shadow token drawn from the ink color.

## B2. Color

- Fill every role in BRAND.md section 2. Each color gets a HEX value and a one line job. The job is written for this brand; the accent may mark the primary action, a seal, or something else, as long as it is one thing.
- Pure white and pure black are allowed. Whether paper, ink, and neutrals are pure or tinted is a choice of the direction; record it, and keep every neutral on the same side of that choice.
- One accent. The accent may be a color, or ink itself used as an inverted block.
- At most six brand roles, paper through accent. Lighter or darker steps of those same hues (hover, selection, recessed fields) go in the tonal steps table and do not count. State colors (success, warning, danger, info) are extra, and must stay distinct from each other and from the accent.
- **Usage ratio:** write the share of a typical page each color takes (for example 80 / 15 / 5), so templates and pages keep the same balance.
- **Print values:** for every brand role give RGB and CMYK. For black, give K100 for text and a rich black for large solid areas. Give Pantone only as the closest match, marked to be confirmed against a physical swatch book with the print shop.
- **Compute contrast, never estimate it.** Run `python3 scripts/contrast.py "<fg>:<bg>" ...` for every pair in the contrast table and paste the numbers. The script takes HEX or `oklch(L% C H)`. Body text needs 4.5:1, large text and UI parts need 3:1. Form field borders are UI parts and need 3:1 against the paper; a rule color below that is decorative only and must say so. Fix any failure before moving on.
- Dark mode only if the owner asks. Design it as its own palette with the same roles and its own contrast table. Never invert the light one.

## B3. Tokens

`tokens.css` has three layers, kept in this order:

1. **Primitive** — raw values named by what they are (`--cream-50`, `--rust-600`)
2. **Semantic** — named by job, matching BRAND.md roles (`--paper`, `--ink`, `--accent`)
3. **Component** — named by element (`--button-bg`, `--card-border`), built from semantic tokens only

Component tokens never reference primitives or raw hex. Names are kebab case. Every value in `tokens.css` must match BRAND.md exactly, including the type hierarchy.

## B4. Typography

- At most two families, display and text. One family may fill both roles, and a mono may be that family. A separate extra mono is allowed only for code or data.
- Every family needs a clear license: an open license such as OFL, or a license the owner already holds. Record it.
- Avoid generic defaults (Inter, Roboto, Arial, Open Sans, Helvetica) unless the owner insists. They erase the paper character.
- Write a full fallback stack for each family.
- Decide italic explicitly: `not allowed`, or allowed for a named purpose (for example, pull quotes in the display serif).
- Never 900 or black weights.
- **Hierarchy:** fill the table for display, H1, H2, H3, lead, body, small, caption, and button. Each level gets a size on Tailwind's type scale for mobile and for desktop, a weight, a line height, and tracking. `hyuse-landing` uses this table as is.
- Check language quality, not just coverage. Having the characters is not enough: a font can contain every Vietnamese letter and still place the marks badly. Before choosing, render "Ầm ầm ẩn ỗ ỘP ỨNG ữ · Quán quân Khởi nghiệp" in uppercase and lowercase, at heading size and body size, next to a font designed with Vietnamese in mind, and look at the double marks: the tone mark must sit clear of the circumflex or breve, not touch it or be squashed onto it. Also check that line heights of 1 do not clip the marks. Show the owner the comparison.
- Before blaming a font for bad marks, confirm the page is really rendering it (`document.fonts`, or the browser's computed font). A web font that failed to load falls back silently to a system face, and that fallback is the usual cause of broken Vietnamese marks. Load fonts from one known source (Google Fonts with the `vietnamese` subset) and embed them in shared files.
- Text must be stored as precomposed Unicode (NFC). Decomposed text (NFD, "Unicode tổ hợp" from some input methods) breaks mark placement in most fonts. Record in the kit that every page normalises copy with `String.prototype.normalize("NFC")` or at the CMS.

## B5. Paper material

Fill BRAND.md section 4.

- **Shadow:** `none` by default. If used, one token only, soft, low offset, drawn from the ink color.
- **Texture:** `none` by default. A grain or fiber texture is allowed as an image asset under the content, never as a blur or translucent overlay on top of it.
- **Pattern:** `none` by default. If the brand needs one for covers or backgrounds, build it from an element the logo already has, in brand colors only, and never put it behind body text.
- **Rule lines:** width and color token, used for dividers, card borders, and tables.
- **Radius:** one base step, and whether some elements must stay square.

## B6. Logo

In Document mode, record the existing logo and its rules. In Create mode:

- Make three to five concepts as SVG. Start with a wordmark. Add a symbol only if the idea earns it.
- Avoid industry cliches (lightbulb, gear, handshake, globe, rocket) unless the twist is deliberate.
- Test every concept in one color, inverted, and as a 24px favicon. Drop any that fail.
- Give each concept a one sentence rationale tied to the positioning.

In both modes, the finished logo system has:

- **Lockups:** horizontal (primary), vertical (stacked, for square and narrow spaces), and a logomark for avatars and favicons. If the logo is a wordmark, the horizontal lockup is the wordmark; say so.
- **Color variants** for each lockup: on light, on dark, and single color (`currentColor`).
- **Clear space:** the empty margin no text, image, or edge may enter. Define it in a unit taken from the logo itself (a letter height, a character cell, a stroke), and give the pixel value at the minimum size.
- **Minimum size** for each lockup, on screen in px and in print in mm.
- **Misuse:** five or six concrete don'ts (recolor, stretch, rotate, re-set in another font, add effects, crowd the clear space, use retired versions).
- **Files:** SVG for every variant; transparent PNG at 480, 1200, and 2400px wide; favicon at 16, 32, 48, and 180px plus SVG; an avatar PNG on a solid background. PDF, AI, and EPS for print come from the designer; list them as pending until they arrive.

## B7. Icons and imagery

- **Icons:** one set only. Record the set, its weights or stroke width, and the grid. Map icon weights to type weights (for example: regular beside body text, bold beside headings, fill for active states). Never Material Icons or Material Symbols.
- **Photography:** subject, light, color treatment. Processing rules: allowed crops and aspect ratios, whether photos are converted (for example to black and white), and that no filter, overlay, tint, or vignette is added. Photos sit on paper like prints.
- **Illustration:** style, line weight, which palette roles it uses.
- **Never:** what must not appear, including generated photos presented as real.

## B8. Voice

Fill BRAND.md section 8. Ground it in the owner's existing writing whenever there is any.

- **Three attributes**, each written as a tension: "{X}, not {Y}" (for example: "Warm, not chatty").
- **Form of address.** How the brand names itself and the reader. In Vietnamese this choice ("chúng tôi / bạn", "mình / bạn", "anh chị") shapes every sentence, so settle it here.
- **Sentence rules:** length, active voice, punctuation habits.
- **Tone by context:** one line each for the website, social posts, email, and sales documents (proposals, quotations).
- **Lexicon:** words to use and words never to use. The never list always includes these AI cliches: Elevate, Seamless, Unleash, Next gen, Game changer, Delve, Tapestry, In the world of, Nâng tầm, Đột phá, Kiến tạo, Trải nghiệm tuyệt vời, Giải pháp toàn diện.
- **Examples:** three lines that sound like the brand, and three that do not, each with why it misses.
- Anything the owner has not decided goes to section 11, Open questions, replacing "None". Do not guess voice.

## B9. Signature rules

Write three to six named rules that make this brand recognisable and that a generic system would not have (for example "The Inversion Rule: the only highlight is ink printed in reverse"). Each rule has a name, one sentence, and the most likely way to break it. These are what reviewers check first.

## B10. Application templates

Build the templates the owner needs from this list, in `brand/templates/`, one HTML file each, all importing `../tokens.css` and the logo files. Print templates set `@page` to the exact size.

| Template | Size |
|---|---|
| Business card, front and back | 90 × 55 mm |
| Email signature | HTML table with inline styles, at most 600px wide, logo as hosted PNG |
| Letterhead | A4, 210 × 297 mm |
| Envelope | DL, 220 × 110 mm |
| Social avatar | 1:1, from the logomark |
| Social covers | Facebook 1640 × 624, LinkedIn 1584 × 396 |
| Social posts | 1080 × 1080 and 1080 × 1350 |
| Slide deck | 16:9, with title, section, content, quote, data, and closing layouts |
| Proposal | A4, multi page |
| Quotation | A4, with a line item table and totals |
| Web UI basics | Button, link, form, card, nav, footer (on the brand board) |

Rules for every template:

- Only kit values: tokens, the type hierarchy, the logo files. Nothing invented per template.
- Placeholder content is written as `{field}` and never as fake names, numbers, or contact details. Real facts appear only when the owner supplied them.
- Respect clear space and minimum size.
- Add a `brand/templates/index.html` that links every template with its size.

---

# PART C — Files and approval

## C1. Write the files

1. Copy `templates/BRAND.md` and `templates/tokens.css` into `brand/` and fill every field.
2. Write `brand/board.html`: one self contained page that follows B1, using `tokens.css`. Show, in order: brand core, color roles with HEX, print values, usage ratio, and contrast numbers, the type hierarchy (with a Vietnamese sample if the brand writes Vietnamese), every logo lockup with clear space and the small size test, icons and imagery, a button, a card, and a form field, the voice examples, the signature rules, and a link to the templates.
3. Export logo files to `brand/logo/` and `brand/logo/png/`.
4. Build the application templates in `brand/templates/`.
5. Run `python3 scripts/bundle.py brand brand/view --embed-fonts` to write self-contained copies of the board and every template, with CSS, logos, and fonts inlined. Pages that load sibling files or web fonts do not render correctly when sent alone or opened in a viewer without network access; a missing font falls back to a system face and Vietnamese marks break. The copies in `brand/view/` carry everything. Send or share those.

## C2. Self check

- [ ] Brand core complete: positioning or a marked capability statement, mission, vision, values with behaviors, tagline, story, key messages with proof
- [ ] Every color has a HEX, RGB, CMYK, and a job; at most six brand roles; usage ratio written
- [ ] Neutrals are consistently pure or consistently tinted, as the direction says
- [ ] Every contrast pair computed with the script and passing, form borders included
- [ ] `tokens.css` has three layers and matches BRAND.md exactly
- [ ] At most two families, licenses recorded, italic decided, hierarchy table filled
- [ ] Logo lockups, color variants, clear space, minimum sizes, misuse, and files all present; small sizes tested
- [ ] One icon set with weights mapped to type
- [ ] Imagery has processing rules
- [ ] Voice has three attributes, form of address, tone by context, lexicon, three good and three bad examples
- [ ] Signature rules written
- [ ] Templates use only kit values and `{field}` placeholders
- [ ] No blur, no translucency, no glow, no gradients anywhere

## C3. Hand over for approval

- Leave `status: draft`. **Never set `status: approved` yourself.** Only the owner does that, by editing the file or by telling you in chat to set it.
- Report: what was decided, every `[ASSUMPTION]`, every open question, and every file still pending from the designer. The kit is not complete while any assumption or open question remains.
- Point the owner to `brand/board.html` and `brand/templates/index.html` for review.

---

# Credits

Ideas adapted, in our own words, from the Brandkit skill curated by Collective Brain (collectivebrain.de), and from Anthropic's theme factory, brand voice, and frontend design skills ([github.com/anthropics/skills](https://github.com/anthropics/skills)).
