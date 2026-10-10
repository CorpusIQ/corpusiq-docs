---
title: "Better UI Skills - Interface Polish Suite Setup Guide"
description: "jakubkrehel suite: 310.6K combined installs across three repos - better-ui, typography, colors, accessibility, and make-interfaces-feel-better."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/better-ui-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-09"
tags: ["hermes skill", "agent skill", "skill setup", "ui design", "typography", "accessibility", "design polish"]
---

# Better UI Skills - Setup Guide

**Source:** [jakubkrehel/skills](https://skills.sh/jakubkrehel/skills) + sibling repos [make-interfaces-feel-better](https://www.skills.sh/jakubkrehel/make-interfaces-feel-better/make-interfaces-feel-better) and [oklch-skill](https://www.skills.sh/jakubkrehel/oklch-skill/oklch-skill) - 310.6K combined installs across 20 indexed listings (Oct 9, 2026 refresh)
**GitHub:** [jakubkrehel/skills](https://github.com/jakubkrehel/skills) (7,659 stars, MIT, very active - pushed Oct 6, 2026) + [make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) (3,629 stars) + [oklch-skill](https://github.com/jakubkrehel/oklch-skill) (265 stars)
**Skills:** 15 across three repositories (13 in the main suite + make-interfaces-feel-better + oklch-skill) · 310.6K combined installs
**Category:** UI Design & Interface Polish / Design Engineering
**First Seen:** August 14, 2026 evening sweep
**Refreshed:** October 9, 2026 - full count refresh; sibling repositories added (51.3K to 310.6K, 6x growth)
**Quality Tier:** 🟢 Production (upgraded from Beta at the Oct 9, 2026 refresh: 7,659-star MIT repo, very active, heavy adoption; Gen Agent Trust Hub and Socket Pass on all 15 sampled skills, Snyk Pass on 11 of 15 - four single-Warns, see Security)

The Better UI suite encodes interface-polish discipline: take an existing UI and make it genuinely better across type, color, layout, accessibility, and copy. The family spans three repositories - the 13-skill [jakubkrehel/skills](https://github.com/jakubkrehel/skills) suite, the original single skill [make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) (62,520 installs - animations, typography, icons, hover states, optical alignment, shadows, hit areas; quick and full review modes), and [oklch-skill](https://github.com/jakubkrehel/oklch-skill) (4,228 installs - model-correct color work, palette generation, semantic tokens, and APCA/WCAG contrast in the OKLCH space). The author is Jakub Krehel, a design engineer whose writing on jakub.kr and the Interfaces magazine (interfaces.dev) is a reference for how modern product interfaces should feel.

The suite's flagship workflow goes from a single question - "why does this feel off?" - to specific fixes: concentric border radius (outer radius = inner radius + padding), optical alignment, layered shadows instead of fake borders, ~100ms stagger timing, scale(0.96) on press, tabular numbers, and motion restraint. Counts below are from the October 9, 2026 skills.sh snapshot.

---

## Installation

```bash
# The full 13-skill suite
npx skills add jakubkrehel/skills

# Sibling repositories
npx skills add jakubkrehel/make-interfaces-feel-better
npx skills add jakubkrehel/oklch-skill
```

Claude Code plugin marketplace: `/plugin marketplace add jakubkrehel/skills` then `/plugin install interfaces@interfaces`.

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the `skills add` installer |
| **A codebase or design to polish** | Skills apply to existing UI work |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| make-interfaces-feel-better | 62,520 | The original polish skill: exact values for radius, shadows, stagger, icon states, hit areas; quick and full review modes |
| better-ui | 33,763 | Surfaces, icons, and motion with exact values - border radius, optical alignment, shadows, icon states, animation |
| better-typography | 29,772 | Type scale, spacing, font features, wrapping, truncation, punctuation |
| better-colors | 28,234 | Palette generation, semantic token naming, format conversion, contrast measurement |
| better-layout | 26,495 | Grouping, alignment, reading order, responsive structure, room for translated text |
| better-interface | 25,973 | Umbrella review across accessibility, layout, writing, typography, color, and UI polish |
| better-accessibility | 25,492 | Keyboard and focus behavior, ARIA, accessible names, forms, screen-reader output, motion, zoom - WCAG 2.2 |
| better-writing | 25,099 | Interface copy: labels, errors, empty states, confirmations |
| interface-review | 14,944 | Structured review of a branch, PR, or uncommitted change (user-invoked) |
| variant | 11,245 | Build multiple variants of a component and iterate (user-invoked) |
| explain-interface | 10,963 | Explain how a site, effect, or animation was built, from a live URL or screenshot (user-invoked) |
| break | 10,470 | Stress test a chosen component under every reachable scenario on a temporary page (user-invoked) |
| oklch-skill | 4,228 | OKLCH color work: palettes, tokens, conversion, APCA/WCAG contrast fixes (sibling repo) |
| state-machine | 720 | Render every state of a component with mock data and a switcher (user-invoked) |
| build-design | 677 | Build UI from a Figma file or design image using the project's existing tokens |

## Quick Start

1. `npx skills add jakubkrehel/skills`
2. "Run better-typography on the docs.corpusiq.io landing page styles"
3. "Apply better-accessibility to the signup flow"
4. "Do an interface-review of the dashboard and list the top 10 fixes"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Docs site polish** | better-typography and better-colors on MkDocs theme overrides |
| **Frontend QA** | interface-review as a pre-deploy design pass on www.corpusiq.io |
| **Accessibility compliance** | better-accessibility for WCAG passes on public pages |
| **Marketing page copy** | better-writing for landing page microcopy |

## Verification

```bash
# Claude Code / skills-directory agents - confirm the skills landed
ls ~/.claude/skills/ | grep -iE "better-|interface-review|oklch|make-interfaces"
```

## Security

skills.sh verdicts for all 15 sampled skills (verified Oct 9, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| better-ui | Pass | Pass | Pass |
| better-typography | Pass | Pass | Pass |
| better-interface | Pass | Pass | Pass |
| better-colors | Pass | Pass | Pass |
| better-layout | Pass | Pass | Pass |
| better-accessibility | Pass | Pass | Pass |
| better-writing | Pass | Pass | Pass |
| variant | Pass | Pass | Pass |
| state-machine | Pass | Pass | Pass |
| make-interfaces-feel-better | Pass | Pass | Pass |
| oklch-skill | Pass | Pass | Pass |
| break | Warn | Pass | Pass |
| build-design | Pass | Pass | Warn |
| explain-interface | Pass | Pass | Warn |
| interface-review | Pass | Pass | Warn |

## Limitations

- Design guidance is opinionated: the skills encode a craft point of view, not automated tests - treat output as review feedback.
- Several skills are user-invoked (interface-review, explain-interface, break, state-machine, variant) - they act when you ask for them.
- Content overlap: make-interfaces-feel-better is the original doctrine and better-interface re-runs the better-* principles; installing both is fine, but do not expect them to disagree.
- Stray 1-3 install listings (great-typography, great-interfaces, oklch-colors) appear to be alternate or test listings - ignore them.
- Snapshot data, verified Oct 9, 2026: 310,603 combined installs across 20 indexed listings; 7,659 GitHub stars; MIT; last repo push Oct 6, 2026. Counts drift over time.

## Related

- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup) - the motion and interaction side of design engineering
- [UI Skills - Design Engineer Skill Registry Setup](/hermes/skills/catalog/ibelick-ui-skills-setup) - registry-based repair skills for motion, accessibility, and metadata
- [Uizze UI Skills - Anti-UI-Slop Design Quality Setup](/hermes/skills/catalog/uizze-ui-skills-setup) - screenshot-based slop detection and scoring
- [AccessLint Skills - WCAG 2.2 Accessibility Audit Suite Setup](/hermes/skills/catalog/accesslint-skills-setup) - full accessibility audit suite to pair with better-accessibility
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- The first rule worth internalizing: outerRadius = innerRadius + padding (concentric radius). Mismatched radii on nested elements is the most common "feels off" defect.
- Match the review depth to the moment: quick scan while building, full review before shipping. When reviewing motion, replay at 10% speed - what looks off at 10% is subtly wrong at full speed.
- The suite expresses fixes in your project's existing styling system (Tailwind, plain CSS, CSS-in-JS) - never let it introduce a second styling system.
- For color work, run oklch-skill before adding tokens: converting legacy HEX/HSL into OKLCH up front prevents the hue drift and contrast failures that surface later.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
