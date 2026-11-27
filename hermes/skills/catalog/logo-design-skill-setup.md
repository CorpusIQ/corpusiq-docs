---
title: "Logo Design Skill - Brand Mark Generation Framework"
description: "kaankiziltug/logo-design-skill: 3.9K combined installs. Logo and brand-mark design from brief to production SVG, with a 1,400+ logo reference library."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/logo-design-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "logo design", "brand identity", "svg", "design"]
---

# Logo Design Skill - Setup Guide

**Source:** [kaankiziltug/logo-design-skill](https://www.skills.sh/kaankiziltug/logo-design-skill) via skills.sh - 3.9K combined installs across 1 indexed listing; first documented 2026-11-27 (morning sweep)

**GitHub:** [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill) - 7,915 stars, MIT, branch main, last pushed 2026-11-13; the skill is a single folder `skills/logo-design/` holding `SKILL.md`, a `references/` set of topic guides, `scripts/` of dependency-free Python tools, `templates/` and an `assets/library/` of 1,400+ real-world SVG logos

**Category:** Logo and brand-mark design: briefs, concepting, SVG craft, testing, delivery and identity systems

**Quality Tier:** 🟢 Green - the single sampled listing passes Gen Agent Trust Hub, Socket and Snyk, and the repository is Markdown plus dependency-free Python

The logo-design skill turns Claude, or any agent supporting the open Agent Skills format, into a disciplined identity designer, from the first brief through production-ready SVG files and brand guidelines. One listing is indexed on skills.sh, so the single row below is the whole set.

It ships a searchable library of 1,400+ real-world SVG logos classified by mark type, technique, geometry, subject, typography, mood and industry, plus Python tools that audit SVGs, build test sheets and presentation boards, and export favicon and app-icon sets. The library is for studying construction, mapping category conventions and avoiding look-alikes; the skill is explicit that it is never to be copied from.

## Installation

The README documents four install routes. The Claude Code plugin marketplace is recommended:

```text
/plugin marketplace add kaankiziltug/logo-design-skill
/plugin install logo-design@logo-design-skill
```

The manual route is a clone plus a copy into the skills directory:

```bash
git clone https://github.com/kaankiziltug/logo-design-skill.git
cp -r logo-design-skill/skills/logo-design ~/.claude/skills/logo-design
```

For Gemini CLI and Codex CLI the same clone-then-copy pattern points at each agent's skills folder:

```bash
git clone https://github.com/kaankiziltug/logo-design-skill.git
cp -r logo-design-skill/skills/logo-design ~/.gemini/skills/logo-design
cp -r logo-design-skill/skills/logo-design ~/.codex/skills/logo-design
```

For Claude.ai or Claude Desktop, download `logo-design.zip` from the Releases page (or run `python3 tools/package_skill.py`) and upload it under Settings, Capabilities, Skills; if your upload has a size limit, use `logo-design-lite.zip`, which omits the SVG files themselves. The skill works best with a vision-capable model, because it renders its own drafts to PNG and checks them before showing anything.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| logo-design | 3,877 | End-to-end logo and brand-mark design: discovery and the brief, concept generation, choosing a mark type, clean geometric SVG, optical refinement, colour and typography, testing, client presentation, delivery variants and brand guidelines. |

All 1 indexed listing appears in the table above.

The workflow always stops at a checkpoint: it shows the concepts as one overview image with a recommendation, then offers the full kit, and nothing else is produced until you choose a direction. The test sheet puts options side by side at 96 and 32 px, in one colour and reversed, then walks each down a size ladder to 16 px, and the `svg_audit.py` script turns craft rules into checks for structure, colours, complexity, near-miss angles, tiny details and centring.

## Why This Matters for Hermes Agents

Logo design is a task where a general agent's first answer is usually wrong: a plausible mark that fails at small sizes, in one colour, or next to a competitor. This skill encodes the craft rules as checks the agent runs rather than vibes it trusts, which is exactly the difference between a decoration and a production mark.

The checkpoint discipline is the design worth copying. By stopping after concepts and asking for a direction, the skill spends the expensive work (colour, lockups, mockups, guidelines) only on an approved idea, and the examples show real briefs where the client picked a different concept than the recommendation and the skill refined that choice instead.

The 1,400+ SVG library is a grounding asset, not a generation source. An agent that can query real logos by technique and industry can map category conventions and avoid look-alikes, and the skill's own guidance is to use it for study, never to copy. The tools are standard-library Python, so they run anywhere a Hermes agent can run Python, with no dependency install.

## Usage

| You say | What happens |
|---|---|
| "Design a logo for Harbor, a savings app for first-time savers. It should feel calm and safe." | It runs the brief, maps words, generates 8-12 concepts, builds three in SVG, then stops at the checkpoint with a recommendation. |
| "Here's our current logo (logo.svg) - critique it and suggest a refresh." | It runs the audit and the critique reference, then proposes a refresh direction. |
| "Give me three wordmark directions for a specialty coffee roaster called Kiln." | It constrains concepting to wordmarks and presents three directions at the checkpoint. |
| "Turn this symbol into favicon, app icon and one-colour versions, plus a one-page usage guide." | It runs the export variants tool and the brand-guidelines template. |
| "Show me negative-space marks in the fintech category." | It queries the library with filters and returns matching real-world examples. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/kaankiziltug/logo-design-skill/main/skills/logo-design/SKILL.md
```

After a clone, confirm the folder layout and that the library and tools are real:

```bash
git clone --depth 1 https://github.com/kaankiziltug/logo-design-skill.git /tmp/logo-design-skill
ls /tmp/logo-design-skill/skills/logo-design
ls /tmp/logo-design-skill/skills/logo-design/assets/library/svg | wc -l
head -3 /tmp/logo-design-skill/skills/logo-design/SKILL.md
```

The SVG count should print more than 1,400, and `head` should show the skill's `name` and `description` fields. The tools run on Python 3.8+ with the standard library only.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| logo-design | Pass | Pass | Pass |

All three scanners pass, which is why this guide is green. The repository is Markdown plus standard-library Python: no third-party Python dependencies, no install script, no network calls, and nothing runs when the skill loads beyond reading Markdown and the tools you invoke explicitly.

One caveat is licensing, not security. The MIT license covers the skill text, scripts, templates and catalog data, but the SVG files in `assets/library/svg/` are trademarks of their respective owners, included for reference and education only and explicitly not covered by the MIT license (see `TRADEMARKS.md`). The example brands in the README are fictional briefs created to demonstrate the skill.

## Limitations

- Snapshot data, verified 2026-11-27: 3,877 combined installs across 1 indexed listing; 7,915 GitHub stars; MIT; last pushed 2026-11-13. Counts drift over time.
- The MIT license covers skill text, scripts, templates and catalog data only; the 1,400+ SVG logos in `assets/library/svg/` are trademarks of their owners and are not redistributable under MIT.
- The skill works best with a vision-capable model, since it renders its own drafts to PNG and checks them before showing you anything.
- PNG and ICO export depends on an external renderer (cairosvg, rsvg-convert, Inkscape, a Chromium-based browser or macOS Quick Look); the Python tools themselves need only the standard library.
- The skill always stops at the checkpoint, so nothing beyond concepts is produced until a direction is chosen.

## Related

- [RKnall Claude Skills - SVG Logo & GitLab Stack Setup](/hermes/skills/catalog/rknall-claude-skills-setup)
- [Brand Building Skills - Brand Strategy Suite Setup](/hermes/skills/catalog/arnabbagxd-brand-building-skills-setup)
- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Let it reach the checkpoint before asking for a full kit; the kit is most of the work and only makes sense for an approved idea.
- Name what to avoid in the brief ("no forks, chef hats, scooters") - the skill treats forbidden cliches as hard constraints.
- Run `search_library.py` before concepting to map category conventions and dodge look-alikes in the sector you are designing for.
- Audit before presenting: `svg_audit.py` catches off-grid angles, tiny details and over-complex paths the eye misses.
- Keep a vision-capable model selected; the self-check renders PNGs and reads them, so a text-only model will skip the visual review.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
