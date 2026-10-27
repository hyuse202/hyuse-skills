---
name: hyuse-landing
description: "Complete system for building high converting landing pages with a pure paper aesthetic (opaque surfaces, no glass, blur, or translucency) that only starts once an approved brand kit exists in brand/BRAND.md: brand kit gate, intake questions, page structure, layout selection, conversion copywriting, SEO, strict visual rules for typography, spacing, corner radius, backgrounds, hero layout, icons, and motion, plus a brand review before delivery. Use this skill whenever building, editing, styling, reviewing, or writing copy for a landing page, marketing site, or one of its sections, even when the user does not mention design, conversion, or tokens."
---

# Landing Page Design

A landing page is not a homepage. A homepage serves multiple intents. A landing page wins one intent:

**one offer → one audience → one primary action.**

This skill has three parts. **Part A** decides what the page says and how it is structured. **Part B** is the non negotiable visual system. **Part C** reviews the page against the brand before delivery. Work through A before touching B.

## Scope

Apply to landing pages, marketing sites, and their sections. When a rule here conflicts with a framework default, this file wins. When the user's explicit prompt conflicts with a rule, the user wins.

**Companion skill.** `hyuse-brand` builds the brand kit this skill requires. When the kit is missing or incomplete, hand over to it.

---

# PART A — Strategy and structure

## A0. Brand kit gate

Do not design, write copy, or build anything until an approved brand kit is in hand.

Look for `brand/BRAND.md` and `brand/tokens.css` at the project root, or at the path the user gives. The kit passes only when all of these hold:

- [ ] Both files exist
- [ ] BRAND.md front matter says `status: approved`
- [ ] No `[ASSUMPTION]` or `TODO` remains anywhere in BRAND.md
- [ ] Section 11, Open questions, lists only "None"
- [ ] Sections 1 to 9 are filled: brand core, color roles with computed contrast, typography with its hierarchy, paper material, logo, icons, imagery, voice, signature rules
- [ ] Every logo file listed in section 5 exists, except print files marked pending from the designer

If any check fails, list exactly which ones failed, tell the user to finish the kit with `hyuse-brand`, and stop. Never invent brand values and never fall back to defaults. This is the one exception to the "do not stall" rule in A1.

Once the kit passes:

- Import `brand/tokens.css` into the page. Components use component or semantic tokens only, never primitives and never raw hex.
- Fonts, colors, icons, material, logo, and voice come from the kit. The kit wins over every default in Part B.
- The positioning sentence and key messages in BRAND.md section 1 are the starting point for the headline in A5 and the proof in A4.
- The signature rules in BRAND.md section 9 are checked in Part C alongside this file's rules.

## A1. Intake

Gather these before designing or writing. Ask only for what is missing, and ask in one batch rather than one question at a time.

**Purpose**
- What is the ONE primary action? (trial, demo, buy, waitlist, download)
- What is the offer, exactly what do they get?
- What counts as a conversion? (click, signup, purchase)

**Audience and context**
- Who is the ICP?
- What problem are they trying to solve?
- Top three objections, meaning why they do not convert today
- Traffic source: ads, search, social, email
- What do visitors already know when they land?

**Proof and assets**
- Proof points: logos, testimonials, numbers, case studies
- Screenshots, demo video, product GIFs
- Guarantees, refund terms, cancellation terms

**Constraints**
- Mobile priority?

Visual direction and brand voice are not asked here. They come from the brand kit (A0).

If the user cannot answer, make a reasonable assumption, state it in one line, and continue. Do not stall the build.

## A2. Page structure

**Above the fold (required)**
1. Headline, outcome plus audience
2. Subheadline, clarifies how and adds specificity
3. Primary CTA, clear verb plus what they get
4. One proof signal, logo strip, stat, or short testimonial
5. Hero visual, product screenshot or video, or a strong illustration

**Mid page (the argument)**
6. Problem to solution, one section
7. Benefits, three to five, outcome driven
8. How it works, three steps
9. Social proof, testimonials or a case study

**Bottom (objection handling)**
10. FAQ, six to twelve questions
11. Risk reversal, trial, cancel anytime, guarantee
12. Final CTA, identical to the top

## A3. Layout selection

Pick one and say why.

| Type | Use when |
|---|---|
| **A. Classic hero plus sections** | The product is understandable from a hero screenshot. Most common. |
| **B. Long form story** | You need to educate and overcome skepticism. |
| **C. Minimal conversion page** | High intent traffic (email to known users), or a short offer like a download or waitlist. |
| **D. Comparison page** | Search intent includes alternatives ("X vs Y", "best for"). Usually paired with SEO pages. |

## A4. Conversion rules

**Match message to source.** If traffic comes from ads, mirror the ad headline in the hero and keep the same promise and visual tone.

**Make the next step obvious.** One primary CTA. Never place competing CTAs above the fold.

**Write benefit first.** Features are what it does. Benefits are what that means for them.

**Be specific.**
- ❌ "Save time and streamline"
- ✅ "Cut your weekly reporting from 4 hours to 15 minutes"

**Reduce risk.** Pick at least one: free trial, free plan, no credit card, cancel anytime, money back guarantee.

**Treat objections as a section, not a footnote.** Move the FAQ earlier for high friction offers. Put proof directly beside the claim it supports.

## A5. Copywriting

All copy follows the voice in BRAND.md section 8: its attributes, form of address, sentence rules, and lexicon.

**Headline formulas**
- "{Outcome} without {pain}"
- "The {category} for {audience}"
- "Ship {result} in {time}"

**Subheadline.** One or two sentences. Clarify what it is and who it is for.

**CTA.** Verb plus what they get. Never "Learn more" or "Submit". Use "Start free trial", "Book a demo", "Get the checklist".

**Benefit bullets.** Bold benefit, then the proof or detail. Example: **Faster iteration** — generate three layout variants in one click.

Note: the copy rules in B1 still apply. No hyphens used as dashes, no orphaned words.

## A6. Build order

Work section by section, in this order:

1. Hero
2. Benefits
3. How it works
4. Proof
5. FAQ
6. Final CTA

Never rebuild the whole page on each iteration. Section by section keeps control and keeps diffs reviewable.

## A7. SEO and AEO

**Do not index** ad only campaign pages or highly time bound offers. Use `noindex` or keep them behind a non indexed path.

**Do index** evergreen offers and pages where search intent matches the promise. Add a clear title and meta description, internal links from the homepage and feature pages, and the FAQ in plain question and answer form for AEO. Add FAQ schema if appropriate.

## A8. Pitfalls

- Too many CTAs above the fold
- Vague value prop: "streamline", "optimize"
- A large feature list with no outcomes
- Proof buried at the bottom
- Mobile layout that breaks readability
- No clear next step

---

# PART B — Visual system

Every visual value must resolve through the brand kit and these rules instead of being invented ad hoc.

## B1. Typography

### Fonts

- Use only the families in BRAND.md section 3, in the roles given there: display for headings, text for body and UI.
- When the kit's display or text family is a mono, use it everywhere that role applies. A separate extra mono is only for code, data, or numeric UI.
- Italic only where the kit allows it, and only for the purpose it names.
- **Never use ultra bold weights** (900 / black). Cap at semibold or bold.

### Copy rules

**No hyphens as dashes.** Do not use `-` to join clauses or as a stand in for a dash in body copy, headings, or labels. Rewrite the phrase instead. Hyphens that belong to a word or a compound ("e-commerce", "seven-person") are fine.

**No orphaned words.** A single word must never sit alone on the last line. Apply `text-wrap: balance` for headings and `text-wrap: pretty` for body copy.

### Type scale

Use the hierarchy table in BRAND.md section 3 for every heading, lead, body, caption, and button. The rules below apply to anything the table does not cover.

Always resolve font sizes to Tailwind's default type scale. Never leave arbitrary values in place, including `text-[19px]`, `font-size: 22px`, or `1.4rem`.

If an existing size does not land exactly on a step, snap it to the **closest step below**, taking both the size and its paired line height.

| Class | Size | Line height |
|---|---|---|
| `text-xs` | 12px (0.75rem) | 16px |
| `text-sm` | 14px (0.875rem) | 20px |
| `text-base` | 16px (1rem) | 24px |
| `text-lg` | 18px (1.125rem) | 28px |
| `text-xl` | 20px (1.25rem) | 28px |
| `text-2xl` | 24px (1.5rem) | 32px |
| `text-3xl` | 30px (1.875rem) | 36px |
| `text-4xl` | 36px (2.25rem) | 40px |
| `text-5xl` | 48px (3rem) | 1 |
| `text-6xl` | 60px (3.75rem) | 1 |
| `text-7xl` | 72px (4.5rem) | 1 |
| `text-8xl` | 96px (6rem) | 1 |
| `text-9xl` | 128px (8rem) | 1 |

Do not combine scale snapping with independently set custom line heights elsewhere in an audit. Tracking and line height may only be adjusted **within** the value the matched step already provides, so the two rules never fight each other.

For Vietnamese copy, normalise every string to NFC before it reaches the page (at the CMS or with `String.prototype.normalize("NFC")`), and check that stacked diacritics in headings with a line height of `1` are not clipped. If they are, use the next step's line height rather than an arbitrary value.

### Button type

- Main buttons: `text-base` (16px), semibold.
- Smaller header buttons: `text-sm` (14px), semibold.

## B2. Spacing

Only these values. Nothing between them, nothing outside them.

| Token | Value |
|---|---|
| Spacing-0 | 0 |
| Spacing-25 | 2px |
| Spacing-50 | 4px |
| Spacing-75 | 8px |
| Spacing-100 | 12px |
| Spacing-200 | 16px |
| Spacing-300 | 24px |
| Spacing-400 | 32px |
| Spacing-500 | 40px |
| Spacing-600 | 48px |
| Spacing-700 | 64px |
| Spacing-800 | 80px |
| Spacing-900 | 96px |

**Main buttons:** 8px vertical padding, 12px horizontal padding.

## B3. Corner radius

Only use Tailwind's radius values, starting from the base radius in BRAND.md section 4. Keep square any element the kit says must stay square.

**Nested radius formula.** When a shape sits inside another shape and the gap between them is **less than 32px**:

```
inner radius = outer radius − gap
```

Apply this only when the result is **greater than 2**. Below that, leave the inner shape square or unchanged.

Example: an outer card at `rounded-2xl` (16px) with 8px of internal padding gives an inner element an 8px radius (`rounded-lg`).

## B4. Paper, borders, and backgrounds

### Paper, never glass

Every surface is opaque paper. Nothing is see through and nothing is frosted.

- Never use `backdrop-blur`, `blur`, or any CSS `filter: blur()` on surfaces or content.
- Never use translucent surfaces such as `bg-white/80`, `bg-black/60`, or `rgba()` fills over content. Overlays, menus, and sticky bars use a solid `--paper` or `--paper-alt`.
- Never use glow, neon, glossy highlights, or reflections.
- Depth comes from a change of stock (`--paper` to `--paper-alt`), a rule line, or the kit's single `--shadow-paper` token. If the kit says `none`, there is no shadow anywhere.
- Texture only if the kit defines one, placed under the content as an image, never over it.

### Borders and backgrounds

- **Never apply a border to only one side of a card.** Borders go all the way around or not at all. Rule lines between sections are dividers, not card borders, and use `--rule-width` and `--rule`.
- **Never use gradients** in backgrounds or on text. Backgrounds are flat.
- Colors come from tokens only. No hex values in components.
- Dark mode only if BRAND.md defines a dark palette, applied through `[data-theme="dark"]`. Otherwise the page is light only.

## B5. Hero section

- Heading text is a single flat color, `--ink`. **Never apply a gradient to text.**
- Heading and subheading both get a **max width of 680px**.
- Read the heading copy and insert line breaks at **meaningful** points.
- Never break a line in a way that cuts a phrase awkwardly or makes the sentence harder to read. Break where the thought breaks.

## B6. Icons

Use only the icon set in BRAND.md section 6, at the weights and grid it gives: the weight mapped to body text beside body text, the one mapped to headings beside headings, and the active weight for selected or inverted states. Never mix sets.

## B7. Motion

### Interaction timing

Hover, press, and focus transitions run 150 to 300ms with an ease out curve. Animate only `transform`, `opacity`, `color`, `background-color`, and `border-color`.

### Navigation

**Hamburger morph.** On click, the hamburger lines fluidly rotate and translate into a perfect X using `rotate-45` and `-rotate-45` with absolute positioning. They must never simply disappear.

**Menu panel.** The open menu is a solid `--paper` panel. No blur, no see through backdrop.

**Staggered mask reveal.** Nav links inside the expanded state fade in and slide up from an invisible box, `translate-y-12 opacity-0` resolving to `translate-y-0 opacity-100`, staggered per item with `delay-100`, `delay-150`, `delay-200`, and so on.

### Scroll interpolation

Elements never appear statically on load. As they enter the viewport they execute a gentle, heavy fade up, with no blur:

```
translate-y-16 opacity-0  →  translate-y-0 opacity-100
```

over 800ms or longer.

For JavaScript driven reveals use `IntersectionObserver` or Framer Motion's `whileInView`. **Never use `window.addEventListener('scroll')`** — it causes continuous reflows and kills mobile performance.

`prefers-reduced-motion: reduce` shows every element in its final state with no movement.

---

## B8. Content realism

Never ship filler. These are the tells that a page was generated rather than made.

- **No Lorem Ipsum.** Write real draft copy.
- **No "John Doe".** Use diverse, realistic names.
- **No placeholder brands** like "Acme Corp", "Nexus", or "SmartFlow". Invent contextual, believable names.
- **No round fake numbers** like `99.99%`, `50%`, `$100.00`. Use organic data: `47.2%`, `$99.00`, `+1 (312) 847-1928`.
- **No AI cliches.** Never use any word on the never list in BRAND.md section 8.
- **Sentence case headers**, not Title Case On Everything.
- **Active voice.** "We could not save your changes", not "Mistakes were made".
- **No exclamation marks in success messages**, and no "Oops!" in errors. Be direct: "Connection failed. Please try again."
- **Unique avatars** per person, and varied blog post dates.

## B9. States

Every interactive element ships with its full state set:

- **Hover** — background shift, slight scale, or translate
- **Active** — `scale(0.98)` or `translateY(1px)` for physical feedback
- **Focus** — a visible focus ring, `--focus-ring`. Accessibility requirement, not optional.
- **Loading** — skeleton loaders shaped like the real layout, not circular spinners
- **Empty** — a composed "getting started" view, never a blank panel
- **Error** — inline and specific, in `--danger`. Never `window.alert()`.

No dead links. A button pointing at `#` is either linked or visually disabled. The current page must be indicated in the navigation.

## B10. Ship requirements

Things that get forgotten and make a page feel unfinished:

- Privacy policy and terms links in the footer
- A custom, branded 404
- Client side form validation for email format and required fields
- A skip to content link for keyboard users
- Cookie consent where the jurisdiction requires it
- A favicon from the kit's logo files
- `<title>`, meta description, `og:image`, and social sharing tags
- Alt text on every meaningful image
- Semantic HTML: `<nav>`, `<main>`, `<article>`, `<aside>`, `<section>`
- A way back from every page

---

# PART C — Brand review

Run this on the finished page before delivery, and on any section rebuilt later.

## C1. Copy review

Check every piece of copy against BRAND.md section 8:

1. **Tone** matches the three voice attributes
2. **Vocabulary** uses the lexicon, and nothing from the never list
3. **Sentence rules** and form of address are followed
4. **Claims** are specific and backed by the proof the user gave. Flag any claim with legal risk (guarantees, "best", "number one", health or money promises)
5. **Disclaimers** the offer needs are present

## C2. Visual review

Search the page code for drift:

- Raw hex or `rgb()` values outside `tokens.css`
- Arbitrary values such as `text-[19px]`, `p-[13px]`, or `rounded-[10px]`
- Any `blur`, `backdrop-blur`, translucent fill (`/80`, `rgba(`), gradient, or glow
- Fonts, icons, or shadows not defined in the kit
- Missing states from B9

## C3. Report

Return one table, most severe first. Fix every 🔴 before delivery.

| Issue | Severity | Where | Original | Fix | Reason |
|---|---|---|---|---|---|

🔴 breaks the brand kit or a hard rule · 🟡 drifts from the voice or system · 🟢 polish

---

# Output format

When generating a landing page from scratch, return these in order before writing code:

0. **Brand kit check** — pass, or the list of failed A0 checks (and stop)
1. **Page outline** — sections and their order
2. **Hero copy** — headline, subheadline, CTA, proof line
3. **Benefits** — three to five outcome driven bullets
4. **How it works** — three steps
5. **FAQ** — six to twelve questions and answers
6. **SEO / AEO** — index or noindex recommendation, plus title and meta if indexed
7. **Layout recommendation** — A, B, C, or D, and why

Then build section by section per A6, and finish with the Part C report.

---

# Quick checklist

**Strategy**
- [ ] Brand kit passes every A0 check
- [ ] One offer, one audience, one primary action
- [ ] No competing CTAs above the fold
- [ ] Specific numbers instead of vague verbs
- [ ] At least one risk reversal
- [ ] Proof sits next to the claim it supports
- [ ] Layout type chosen deliberately

**Visual**
- [ ] Only the kit's fonts, italic only where the kit allows, no ultra bold
- [ ] No hyphens used as dashes, no orphaned words
- [ ] Every font size lands on a Tailwind scale step
- [ ] Every spacing value comes from the spacing table
- [ ] Nested radii follow the formula
- [ ] Colors from tokens only, no hex in components
- [ ] No single sided card borders, no gradients on backgrounds or text
- [ ] Paper only: no blur, no translucent surfaces, no glow
- [ ] Hero heading and subheading capped at 680px with meaningful line breaks
- [ ] Icons from the kit's set only
- [ ] Interactions 150 to 300ms, scroll reveals use IntersectionObserver, reduced motion respected

**Content and ship**
- [ ] No Lorem Ipsum, no placeholder brands, no never list words, no round fake numbers
- [ ] Hover, active, focus, loading, empty, and error states all present
- [ ] No dead links, current nav item indicated
- [ ] 404, legal links, form validation, favicon, meta tags, alt text
- [ ] Part C report delivered with no 🔴 left

---

# Credits

Adapted from `landing-page-design` in [elayadesign/ai-design-skills](https://github.com/elayadesign/ai-design-skills), MIT License, Copyright (c) 2026 Elaya. The brand review in Part C borrows its structure from Anthropic's brand review skill ([github.com/anthropics/skills](https://github.com/anthropics/skills)).
