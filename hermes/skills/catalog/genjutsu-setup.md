---
title: "Genjutsu - Front-End Craft Skills for Agents"
description: "athevon/genjutsu on skills.sh: 18.1K combined installs across 20 listings; front-end craft skills for motion, layout, canvases and design audits."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/genjutsu-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "front-end", "motion design", "design systems"]
---

# Genjutsu - Setup Guide

**Source:** [athevon/genjutsu](https://www.skills.sh/athevon/genjutsu) via skills.sh - 18.1K combined installs across 20 indexed listings; first documented November 4, 2026 (morning sweep)
**GitHub:** 741 stars, NOASSERTION licence (the repo root ships an MIT LICENSE file), last pushed 2026-11-03, 20 SKILL.md directories
**Category:** Front-end craft for agents: layout systems, motion, component polish and design review in one skill library
**Quality Tier:** 🟡 Yellow: paint draws Socket and Snyk Warns, and GitHub reports the licence as NOASSERTION even though the repository ships an MIT LICENSE file

Genjutsu is Adrien Thevon's creative coding library for Claude Code, claude.ai and Cowork. The 20 indexed skills cover web work (React, Vue, Svelte, Astro, vanilla CSS, Three.js and Canvas), Android (Jetpack Compose and Compose Multiplatform) and Apple (SwiftUI on iOS and macOS). It is one of the few packs in this catalog that treats motion, graphics and layout as one subject across three platforms.

Three listings are the entry points. `cast` casts an illusion on an existing UI: it scans the stack, proposes an interaction thesis and loads the sub-skills it needs. `paint` builds a visual universe from nothing: art direction, design system, implementation, audit. `bunshin` runs the whole pipeline for a site or app with parallel agents. Everything else is a sub-skill or an internal module that those three load on demand, which is why the lowest install counts here belong to the most specialised pieces.

## Installation

The README documents the skills CLI route first, and it is specific about the URL:

```bash
npx skills add https://genjutsu.athevon.dev -g
```

After that, describe the task in Claude Code or type `/genjutsu`. The README asks for the `-g` flag on updates too, and warns against the repository route because it installs the skills without their modules:

```bash
npx skills update -g
```

The Claude Code plugin route exposes three named commands:

```text
/plugin marketplace add AThevon/genjutsu
/plugin install genjutsu
```

That gives `/genjutsu:cast`, `/genjutsu:paint` and `/genjutsu:bunshin` inside a session. Project scope, the claude.ai and Cowork paths, and the extra pieces `bunshin` needs are documented on the project's install page. For Hermes, copy the `skills/` tree into the profile skills directory and keep the `_jutsu/` subdirectory intact, since `cast` and `paint` resolve their modules from there.

## What It Provides

The suite splits into three entry points, platform sub-skills and internal modules.

| Skill | Installs | Use For |
|---|---|---|
| paint | 1,421 | Art direction brainstorm, design system, implementation and audit in one anti-slop pipeline |
| cast | 1,421 | Scans the stack, proposes an interaction thesis, loads sub-skills and implements the motion |
| motion-principles | 1,135 | Timing, easing, enter and exit patterns, accessibility and performance budgets |
| css-native | 1,056 | Zero-dependency animation with scroll-driven CSS, View Transitions and @starting-style |
| threejs-r3f | 1,026 | Three.js and React Three Fiber scenes, shaders and postprocessing |
| design-audit | 1,023 | Checklist pass over motion gaps, accessibility, colour, responsive and performance |
| canvas-generative | 1,001 | Canvas 2D generative art: particles, flow fields, noise, fractals and L-systems |
| gsap | 999 | GSAP core, timelines, ScrollTrigger and plugins |
| framer-motion | 991 | AnimatePresence, layout animations, gestures and motion values |
| desktop-principles | 984 | Hover states, pointer precision, shortcuts, multi-window and focus management |
| mobile-principles | 973 | Touch targets, thumb zones, safe areas, gestures and mobile performance budgets |
| compose-multiplatform | 949 | expect/actual composables, density and font handling, iOS, Android and desktop interop |
| ui-ux-pro-max | 948 | Searchable design-system dataset of 84 styles and 192 palettes; loaded by cast and paint |
| compose-motion | 943 | animateAsState, AnimatedVisibility, Crossfade and shared element transitions |
| swiftui-motion | 942 | withAnimation, transitions, matchedGeometryEffect, PhaseAnimator and springs |
| swiftui-graphics | 939 | Metal shaders, visualEffect, Liquid Glass on iOS 26, Canvas and CRT effects |
| compose-graphics | 936 | Material 3 Expressive motion physics, AGSL shaders and DrawScope generative work |
| bunshin | 380 | Full site pipeline: real material, parallel builds, fix loops and a cold-eyes verdict |
| design-excellence | 2 | No directory in the current skills/ tree; the listing carries install history only |
| creative-excellence | 1 | The suite's former name per the changelog; no directory in the current tree |

All 20 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

Most design skill packs are prose about taste. This one is organised by platform, so a Hermes agent working on a SwiftUI screen and one working on a Compose screen load different sub-skills that share the same vocabulary.

The entry points force a decision before code. `cast` scans the stack and proposes an interaction thesis, and the internal `tells` module names the reflexes a model falls into when nothing asked for them: invented data, decorative filler, converged layouts, hollow copy. That is a review an agent cannot run on its own taste, and it is the part worth borrowing even if you never install the rest.

Platform depth is unusual for a library this size. Android and Apple each get their own motion skill, graphics skill and platform-principles skill, rather than a single mobile afterthought.

`ui-ux-pro-max` is worth having for its data alone: 84 styles, 192 palettes, 74 font pairings, 25 charts and 99 UX guidelines across 22 stacks, shipped as a searchable dataset plus a CLI. It is an internal module, loaded by `cast` and `paint` rather than invoked directly.

The last useful signal is honesty about results. The README publishes per-run receipts with cost, turn counts and what each run left unverified, and it says plainly that measured gains over a page built without genjutsu are modest. Treat the suite as craft scaffolding, not a guarantee.

## Usage

| You say | What happens |
|---|---|
| "Make this dashboard feel alive without new dependencies" | cast scans the stack, states an interaction thesis, then applies css-native timing and transitions |
| "Give this product a look of its own" | paint runs art direction, builds the design system, implements it and audits the result |
| "Build the whole landing site from our brand material" | bunshin harvests the material, builds in parallel and loops fixes to a verdict |
| "Why does this page feel generic?" | tells names the specific tells, and design-audit returns the checklist gaps |
| "Add a shader background to the hero" | threejs-r3f on web, swiftui-graphics on Apple |
| "Our Compose screen drops frames on scroll" | compose-motion and mobile-principles work the animation and the performance budget |
| "Check the motion for accessibility" | motion-principles covers reduced motion and the audit checks the same path |

## Verification

Confirm the skills landed in the agent skills directory:

```bash
ls ~/.claude/skills | sort
```

Then fetch one raw file before installing anything. This path is `skills/_jutsu/motion-principles/SKILL.md` on branch main and returned 200 when this guide was written:

```bash
curl -fsSL https://raw.githubusercontent.com/athevon/genjutsu/main/skills/_jutsu/motion-principles/SKILL.md | head -20
```

Frontmatter with a name and a description confirms the indexed listing is backed by a real file. Repeat with `skills/paint/SKILL.md` and `skills/bunshin/SKILL.md`, which sit outside the `_jutsu` directory. The install index itself is at https://www.skills.sh/athevon/genjutsu.

## Security

skills.sh verdicts for sampled skills (verified November 4, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| paint | Pass | Warn | Warn |
| design-audit | Pass | Pass | Pass |
| mobile-principles | Pass | Pass | Pass |
| swiftui-graphics | Pass | Pass | Pass |
| creative-excellence | Pass | Pass | Pass |

`paint` is the only flagged skill in the sample and carries two Warns. It is also the skill that writes most freely, since its job is to create a design system and implement it across a project, so scope it to a branch you can discard.

## Limitations

- Snapshot data, verified November 4, 2026: 18,070 combined installs across 20 indexed listings; 741 GitHub stars; NOASSERTION licence; last pushed 2026-11-03. Counts drift over time.
- GitHub reports the licence as NOASSERTION even though the root LICENSE file is the MIT text (Copyright (c) 2026 Adrien Thevon). Read the file before redistributing; do not rely on the badge alone.
- The install index and the tree do not fully agree. design-excellence and creative-excellence carry install counts but have no directory in the current `skills/` tree, while `orchestration` and `tells` are in the tree and carry no indexed listing. The README says creative-excellence was the suite's name up to version 2.
- `bunshin` is web only for now, per the README, and it depends on the modules the site-URL install provides; a repository-route install leaves it weaker.
- Several listings are internal modules. `ui-ux-pro-max`, `tells` and `orchestration` are loaded by `cast`, `paint` or `bunshin`, so installing them on their own buys little.
- Install counts cluster tightly: 17 of the 20 listings sit between 936 and 1,421 installs, so the order inside the suite carries little signal.

## Related

- [Frontend God Mode - Design Skills Bundle Setup](/hermes/skills/catalog/frontend-god-mode-setup)
- [UI/UX Pro Max - Design System Skill Pack Setup](/hermes/skills/catalog/ui-ux-pro-max-setup)
- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install from the site URL with `-g`, not from the repository name. The README warns that the repository route drops the modules.
- Load one entry point, not the whole set. `cast` and `paint` pull what they need; preloading all 20 spends context on platforms you are not touching.
- Ask for the interaction thesis in writing before implementation. It is the cheapest place to catch a direction you did not want.
- Run `design-audit` at the end of a build, not the start. It is a checklist over finished output, not a plan.
- Keep the eval receipts in view: the author reports modest gains over an unskilled control, so judge the page rather than the claim.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
