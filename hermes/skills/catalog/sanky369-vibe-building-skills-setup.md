---
title: "Vibe Building Skills - Design and Marketing Setup Guide"
description: "sanky369/vibe-building-skills: 40 agent skills for design, brand, marketing and product video work - 4.5K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sanky369-vibe-building-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "design", "marketing", "creative"]
---

# Vibe Building Skills - Design and Marketing Setup Guide

**Source:** [sanky369/vibe-building-skills](https://www.skills.sh/sanky369/vibe-building-skills) via skills.sh - 4.5K combined installs across 40 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 evening sweep)
**GitHub:** [sanky369/vibe-building-skills](https://github.com/sanky369/vibe-building-skills) - 39 stars, MIT license, main branch, last pushed Jul 12, 2026; 40 standalone skills under `skills/<category>/<name>/SKILL.md` across five category trees (product-strategy, product-design, marketing, creative, frontend-design), plus a Python asset-generation layer under `docs/`.
**Category:** Design, Brand and Marketing
**Quality Tier:** 🟡 Yellow - sampled skills.sh verdicts are mostly Pass with Snyk Warn cells on tweet-writer, remotion-script-writer, brand-voice and content-atomizer; no Fails.

`vibe-building-skills` is a 40-skill Agent Skills library from sanky369 that spans the full product lifecycle: product strategy, product design, marketing, creative asset generation, and frontend design. Each skill ships as a standalone SKILL.md with trigger phrases, an agent-addressed workflow, required output formats, and a quality bar, per the repo's `docs/SKILL_SPEC.md` authoring standard. The creative skills also carry a Python automation layer (`docs/creative_cli.py` plus `docs/fal_api.py`) that generates images through FAL.ai nanobanana pro when a `FAL_API_KEY` is set.

The library is organized into five category trees, with the 13 frontend design skills forming the largest group and the 12 marketing skills close behind. Install paths are per-skill (upload a SKILL.md into Claude), per-category, or the whole repo, and the entry skill in each category sequences the remaining skills in that category. First seen in the Nov 20, 2026 catalog update.

## Installation

```bash
git clone https://github.com/sanky369/vibe-building-skills.git
cd vibe-building-skills
```

Each skill is a standalone SKILL.md file. Install an individual skill by uploading its SKILL.md in Claude (Settings > Capabilities > Skills > Add Skill), install the whole set by zipping the `skills` directory and uploading it, or install by category using the repo's per-category globs:

```text
skills/product-strategy/*/SKILL.md
skills/product-design/*/SKILL.md
skills/marketing/*/SKILL.md
skills/creative/*/SKILL.md
skills/frontend-design/*/SKILL.md
```

Start with `foundation-sprint` when the product direction is still open, or with the entry skill for your category when the direction is already clear. From there, follow the sequence the entry skill recommends and use Claude Code for implementation.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| social-graphics | 651 | platform-correct social media graphics with the repo's FAL.ai image pipeline |
| direct-response-copy | 415 | landing, sales, opt-in and ad copy built on an eight-part direct-response architecture |
| tweet-writer | 325 | high-engagement tweets and X/Twitter threads grounded in live niche research |
| typography-system | 264 | modular type scale, font choice, hierarchy and fluid sizing as Tailwind or CSS-variable tokens |
| remotion-script-writer | 228 | render-ready Remotion video scripts as structured JSON (scenes, assets and technical requirements) |
| product-video | 218 | end-to-end animated product video planning with beat sheets and keyframe prompts |
| color-system | 156 | brand and neutral ramps, semantic color tokens, dark mode and contrast verification |
| image-generation | 113 | generation-ready image prompt specs via the fal-ai/nano-banana-pro model |
| brand-asset | 111 | logo concepts, icon sets, patterns and brand illustrations as prompt specs |
| product-photography | 108 | AI product photography (e-commerce, hero and macro shots) as prompt specs |

The remaining 30 indexed listings range from 19 to 98 installs.

## Why This Matters for Hermes Agents

The skills in this library give an agent a complete product-building workflow instead of isolated one-off helpers. Product strategy skills shape and pressure-test an idea before code is written, the product design skill turns a prototype or live product into a prioritized review, and the marketing skills cover direct response, SEO, email, content and X/Twitter writing. The creative skills produce generation-ready prompt specs and, with a FAL_API_KEY, actual image files through the repo's FAL.ai automation, so an agent can go from prompt to asset without leaving the workflow. The frontend design group is the largest at 13 skills and spans the full design-system lifecycle: tokens, layout, typography, color, components, interaction, loading and error states, performance and accessibility. Because every skill is a standalone SKILL.md with trigger phrases and required output formats, an agent can load only the category it needs and still get consistent, specification-driven output. The creative automation runs through `docs/creative_cli.py`, which the skills call only when a FAL_API_KEY is present, so image generation stays opt-in rather than a hard dependency.

## Usage

| You say | What happens |
|---|---|
| "Generate a hero image for my SaaS landing page" | image-generation writes a prompt spec (subject, style, composition, lighting, mood, aspect ratio, negative constraints) and generates the file when FAL_API_KEY is set |
| "Make our product shots look consistent across the store" | product-photography produces a shot list with lighting, background and composition specs plus naming conventions |
| "Write a landing page that actually converts" | direct-response-copy drafts hook, problem, mechanism, solution, proof, objections, CTA and urgency sections with a conversion checklist |
| "Turn my blog post into a week of social content" | content-atomizer builds per-platform posts: LinkedIn posts, an X thread, a newsletter item and short-video scripts |
| "Our colors clash and we need dark mode" | color-system extracts the current palette, consolidates drift into ramps and verifies WCAG AA contrast on every pairing |
| "Audit this dashboard for accessibility issues" | accessibility-excellence returns a prioritized audit of WCAG failures with the implemented fixes |

## Verification

```bash
# after cloning, confirm the standalone SKILL.md files are present
ls skills/creative/social-graphics/SKILL.md
# review one skill before relying on it
curl -sL https://raw.githubusercontent.com/sanky369/vibe-building-skills/main/skills/creative/social-graphics/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200. Skills live under `skills/<category>/<name>/SKILL.md` across the five category trees, and each is a standalone file that can be uploaded to Claude or Claude Code directly.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| social-graphics | Pass | Pass | Pass |
| direct-response-copy | Pass | Pass | Pass |
| tweet-writer | Pass | Pass | Warn |
| typography-system | Pass | Pass | Pass |
| remotion-script-writer | Pass | Pass | Warn |
| product-video | Pass | Pass | Pass |
| color-system | Pass | Pass | Pass |
| image-generation | Pass | Pass | Pass |
| brand-asset | Pass | Pass | Pass |
| product-photography | Pass | Pass | Pass |
| layout-system | Pass | Pass | Pass |
| interaction-physics | Pass | Pass | Pass |
| visual-hierarchy-refactoring | Pass | Pass | Pass |
| brand-voice | Pass | Pass | Warn |
| creative-strategist | Pass | Pass | Pass |
| loading-states | Pass | Pass | Pass |
| design-foundation | Pass | Pass | Pass |
| lead-magnet | Pass | Pass | Pass |
| content-atomizer | Pass | Pass | Warn |
| accessibility-excellence | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 20, 2026: 4,518 combined installs across 40 indexed listings; 39 GitHub stars; MIT license; last pushed Jul 12, 2026. Counts drift over time.
- The repository was last pushed Jul 12, 2026, so install counts and skills.sh listings reflect a mid-2026 snapshot and may lag newer activity.
- Only 20 of the 40 indexed listings carry skills.sh security verdicts in the sample; the other 20 are unverified on that platform.
- One in-tree skill directory name differs from its skills.sh indexed name (the creative category entry skill is indexed with a category prefix that its directory omits); the 40 in-tree SKILL.md files otherwise map one-to-one to the 40 indexed listings.
- The creative automation requires a FAL_API_KEY and the `docs/requirements.txt` dependencies; without it, the creative skills return prompt specs only, not generated image files.

## Related

- [Better Web UI - Frontend Design Skills Setup](/hermes/skills/catalog/aladicf-better-web-ui-setup)
- [Uizze UI Skills - Anti-UI-Slop Design Quality Setup](/hermes/skills/catalog/uizze-ui-skills-setup)
- [Better UI Skills - Interface Polish Suite Setup](/hermes/skills/catalog/better-ui-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Clone the repo once and install per category with the `skills/<category>/*/SKILL.md` globs so you load only the skills your current project needs.
- Start with `foundation-sprint` when the product direction is open, or the category entry skill when it is already set.
- Set `FAL_API_KEY` only when you want the creative skills to emit actual image files; without it they still return generation-ready prompt specs.
- Read `docs/SKILL_SPEC.md` to understand the authoring standard every skill meets before writing your own additions.
- Review a single SKILL.md before relying on it, since each skill carries its own trigger phrases and output formats.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
