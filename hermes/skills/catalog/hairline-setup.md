---
title: "Hairline Skills - Isometric Line Figure Setup"
description: "lucasmarkes/hairline: 33 isometric line figures that answer the pointer, for React and any DOM, plus two agent skills - 11.5K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hairline-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "react", "svg", "motion", "creative coding"]
---

# Hairline Skills - Setup Guide

**Source:** [lucasmarkes/hairline](https://www.skills.sh/lucasmarkes/hairline) via skills.sh - 11.5K combined installs across 2 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 morning sweep)
**GitHub:** [lucasmarkes/hairline](https://github.com/lucasmarkes/hairline) - 4,034 stars, MIT licence, main branch, last pushed Nov 13, 2026. Two skills live under `skills/<name>/SKILL.md` (hairline-create, hairline-adopt) alongside the library packages; 218 files in the tree.
**Category:** Design Engineering
**Quality Tier:** 🟡 Yellow - 1 Warn among 2 sampled verdicts (Snyk Warn on hairline-create; hairline-adopt all Pass); MIT licence.

Hairline is a library of thirty-three isometric line figures that answer the pointer, published by Lucas Markes for React and for anything with a DOM. Each figure is drawn in lines and responds to the pointer's position, height and clicks, with an intensity option that scales the response. The figures ship as dependency-free ESM functions plus a React component entry, and every figure on a page shares one requestAnimationFrame loop so pages can host many at once.

Alongside the library, the repository ships two coding-agent skills. hairline-create draws a new figure from an idea, and hairline-adopt reads an SVG and rebuilds it as a Hairline figure. These two listings cover the whole indexed surface on skills.sh, and the repo tree has 218 files.

## Installation

```bash
# the library
npm i @lucasmarkes/hairline

# or, with shadcn (adds the package and a theme-aware wrapper)
npx shadcn@latest add https://hairline.lucasmarkes.com/r/hairline.json
```

For the two coding-agent skills, install the skill package and then type the command with an idea:

```bash
npx skills add lucasmarkes/hairline
```

```text
/hairline-create a sales funnel
/hairline-adopt icons/deploy.svg
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| hairline-create | 7,586 | Draw a new isometric line figure from an idea, to Hairline's ten rules, as one self-contained HTML file |
| hairline-adopt | 3,885 | Read an SVG (an icon, a logo, an illustration) and rebuild it as a Hairline figure that answers the pointer |

Both indexed listings appear in the table above.

## Why This Matters for Hermes Agents

The figures give an agent a way to ship interactive, pointer-responsive visuals without pulling in an animation framework: the package is ESM-only with no dependencies, and the React entry needs React 18 or later only as an optional peer. For a coding agent, the real value is the two skills, which encode Hairline's ten drawing rules so a generated figure matches the library's style instead of approximating it. hairline-create hands over a single self-contained HTML file with no dependencies that opens from disk, so the output is reviewable and portable across any stack. hairline-adopt turns an existing SVG asset into a figure on the same engine, which is the faster path when the design already exists. Both skills run on any agent that reads skills, including Claude Code, Cursor and Codex. Because every figure on a page shares one requestAnimationFrame loop and at-rest figures do no work, an agent can drop several figures into a page without the usual animation-loop cost.

## Usage

| You say | What happens |
|---|---|
| Create a hairline figure of a sales funnel | hairline-create offers two or three concepts, draws the one you pick, checks it against the rules and in a browser, and hands over a `hairline-<name>.html` file |
| Adopt this SVG logo as a hairline figure | hairline-adopt reads the SVG, rebuilds its object with its proportions and parts, and proposes what the pointer does to it |
| Add an interactive terrain figure to my React page | Import `Terrain` from `@lucasmarkes/hairline/react` and render it; it fills its parent's width at a 5:4 aspect ratio |
| Draw a dot matrix that fades where the pointer paints | Use the phosphor figure; a stronger intensity makes the trail linger longer |
| Make a vault door whose dial the pointer turns | Use the vault figure; detents catch every ten and the bolts draw back on the combination |

## Verification

```bash
# after install, confirm the skill files landed
ls .skills/lucasmarkes/hairline/
# review a skill before relying on it
curl -sL https://raw.githubusercontent.com/lucasmarkes/hairline/main/skills/hairline-create/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| hairline-create | Pass | Pass | Warn |
| hairline-adopt | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 20, 2026: 11,471 combined installs across 2 indexed listings; 4,034 GitHub stars; MIT licence; last pushed Nov 13, 2026. Counts drift over time.
- The publisher's whole indexed surface is the two listings above; there are no other indexed listings, and the repo tree has 218 files.
- The security picture rests on those two sampled rows: hairline-create carries a Snyk Warn while hairline-adopt is clean across all three scanners, so review a generated figure's HTML with the same care you would give any code a skill produces.
- The package is ESM-only with no dependencies; the React entry needs React 18 or later as an optional peer, and the core functions need a DOM, so on the server a component renders as an empty 5:4 box and the functions must be called in an effect, onMount, or a script after the element.
- hairline-create and hairline-adopt are coding-agent skills, not installers of the library itself; the figures they produce are standalone HTML files that open from disk with no dependencies.

## Related

- [Anatomy Skill - Isometric SVG Explainer Setup](/hermes/skills/catalog/anatomy-skill-setup)
- [Vibe Motion Skills - SVG & Motion Renders Setup](/hermes/skills/catalog/vibe-motion-skills-setup)
- [Design Motion Principles Skill - Motion & Interaction Setup](/hermes/skills/catalog/design-motion-principles-skill-setup)
- [p5js - Creative Coding & Generative Art Setup](/hermes/skills/catalog/p5js-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use `npx skills add lucasmarkes/hairline` to get both skills; the slash commands run on any agent that reads skills, including Claude Code, Cursor and Codex.
- Set `--hairline-plate` to the page background so a plate hides what is drawn behind it; the figure's styles have no specificity, so your own CSS wins without `!important`.
- For React, import from `@lucasmarkes/hairline/react`; the entry is a client module, so a Server Component can render it with no `"use client"` of its own.
- Pass `play: true` to walk a figure through its answer in a loop; under `prefers-reduced-motion`, the figures that play on their own hold still and the rest still answer the pointer.
- Every figure shares one `requestAnimationFrame` loop, and off-screen or at-rest figures do no work, so several figures on a page stay cheap.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
