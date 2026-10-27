# hyuse skills

Design skills for AI coding tools with one point of view: **pages are paper, not glass**, and **nothing gets designed before the brand is decided**.

Opaque surfaces, flat ink, rule lines, real copy. No blur, no translucency, no glow, no gradient text. Paper here means opaque and flat; it can be warm cream or pure black on white.

## Skills

| Skill | What it does |
|---|---|
| [`hyuse-brand`](./skills/hyuse-brand/SKILL.md) | Builds, documents, or updates a full brand kit: brand core (positioning, mission, vision, values, tagline, story, key messages), color roles with computed contrast and print values, typography with a hierarchy, logo lockups and file set, icons, imagery, voice, signature rules, and application templates (business card, email signature, letterhead, envelope, social, slides, proposal, quotation). Writes `brand/BRAND.md`, `brand/tokens.css`, a brand board, logo files, templates, and self-contained copies for sharing, then waits for the owner's approval |
| [`hyuse-landing`](./skills/hyuse-landing/SKILL.md) | Builds a landing page from an approved brand kit: intake, page structure, conversion copy, SEO, a strict paper visual system, and a brand review before delivery. Refuses to start without an approved kit |

They work as a pair:

```
hyuse-brand  →  brand/BRAND.md (status: approved)  →  hyuse-landing
```

## What a kit contains

```
brand/
├── BRAND.md            source of truth, 11 sections
├── tokens.css          primitive → semantic → component tokens
├── board.html          brand board for review
├── logo/               SVG lockups and variants, logo/png/ at three widths, favicons, avatar
├── templates/          business card, email signature, letterhead, envelope, social, slides, proposal, quotation
└── view/               self-contained copies with CSS, logos, and fonts inlined
```

## Install

### Claude Code

```bash
git clone https://github.com/hyuse202/hyuse-skills.git /tmp/hyuse-skills
mkdir -p ~/.claude/skills
cp -r /tmp/hyuse-skills/skills/hyuse-brand /tmp/hyuse-skills/skills/hyuse-landing ~/.claude/skills/
```

Copy into `.claude/skills/` inside a project instead to scope them to that project.

### Other tools

Copy a skill's `SKILL.md` into your tool's rules file (`AGENTS.md`, `.cursor/rules/`, `.windsurfrules`, `.clinerules`). `hyuse-brand` also needs its `templates/` and `scripts/` folders next to it.

## Scripts

Both need Python 3 and nothing else.

| Script | What it does |
|---|---|
| `hyuse-brand/scripts/contrast.py` | WCAG contrast for color pairs, in HEX or `oklch()` |
| `hyuse-brand/scripts/bundle.py` | Inlines CSS, logos, and (with `--embed-fonts`) web fonts into each brand page, so it renders the same on any device, offline included |

## Notes for Vietnamese brands

- Check that the page really renders the chosen font before judging its diacritics: a web font that fails to load falls back silently, and the fallback is the usual cause of broken marks.
- Store and show text as NFC. Decomposed text (NFD) breaks mark placement in every font.

## Credits

`hyuse-landing` is adapted from `landing-page-design` in [elayadesign/ai-design-skills](https://github.com/elayadesign/ai-design-skills) (MIT). Ideas in `hyuse-brand` and the brand review step come from Anthropic's skills ([anthropics/skills](https://github.com/anthropics/skills)) and the Brandkit skill curated by [Collective Brain](https://collectivebrain.de), rewritten in our own words.

## License

MIT. See [LICENSE](./LICENSE).
