---
title: "Mies - Design Taste Skill for Interfaces Setup"
description: "Setup guide for deeflect/mies - 8.8K combined installs. A design-taste skill that strips what a UI does not need, then perfects what is left."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mies-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "design", "ui craft"]
---

# Mies - Setup Guide

**Source:** [deeflect/mies](https://www.skills.sh/deeflect/mies) via skills.sh - 8.8K combined installs across 1 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [deeflect/mies](https://github.com/deeflect/mies) (4 stars, MIT; pushed 2026-05-29; `skills/mies/SKILL.md` layout)
**Category:** Design / UI Craft
**Quality Tier:** 🟡 Beta - single-skill design-taste repo (mies.design); MIT; all sampled verdicts Pass

deeflect publishes mies, a single-skill design-taste repo with its home page at mies.design. The premise is one sentence long: remove what an interface does not need, then perfect what is left. The skill asks one question of every element - "why is this here?" - and anything that cannot answer gets cut, while the survivors are made exact across proportion, spacing, alignment, type, color, state, motion, and copy. The name nods to Mies van der Rohe, who spent a career taking things out, and the skill keeps his discipline: less is not cold when the small decisions are warm.

For new work the skill runs a Frame, Set, Compose flow: Frame decides what you are building and rejects the obvious version of it before any code, Set lays the foundation, and Compose finishes the surface. For a small fix, it tells you what it sees and gets on with it. Invoke it as `/mies` in Claude Code whenever you are making, redesigning, critiquing, or cutting back a screen people actually use.

---

## Installation

Prerequisites: Node.js for the `npx` skills CLI, and an agent terminal that loads skills (the README targets Claude Code).

```bash
npx skills add deeflect/mies
```

Or drop the repository into your agent's skills directory by hand. Once installed, type `/mies` in Claude Code to run the design pass on a screen.

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| mies | 8,774 | Design-taste pass over a screen: cut what cannot justify itself, then make proportion, spacing, alignment, type, color, state, motion, and copy exact |

The repo carries a single indexed listing and it clears the 500-install threshold, so the table above covers the entire catalog with no below-threshold tail.

## Why This Matters for Hermes Agents

Most UI feedback an agent gives is additive: more spacing, more states, more polish. mies inverts that, and for agent work the inversion matters twice. First, reduction is a cheap, high-signal review pass: a Hermes agent can run the skill over a screen it just generated and cut what cannot be justified before a human sees any of it. Second, the skill encodes concrete craft (proportion, spacing, alignment, type, color, state, motion, copy) instead of vague taste, so its output is actionable for an agent that applies changes step by step. The Frame step doubles as a planning gate: it forces a decision about what is being built before code, which maps cleanly onto how a Hermes agent should open a build task. The repo is MIT and tiny, so adopting the skill costs almost nothing.

## Usage

| You say | What happens |
|---|---|
| "This settings screen feels cluttered; strip it back" | mies questions each element, removes what cannot justify itself, and makes the survivors exact |
| "Critique this dashboard before I review it" | A quick pass: the skill says what it sees and gets on with the small fixes |
| "Tighten the type scale and spacing on this page" | Set-mode work on the foundation: proportion, spacing, alignment, and type |
| "The empty states are bland; improve the copy" | Copy is part of the pass: wording written for an actual person survives, filler does not |
| "Does this layout survive ugly data?" | State review: the screen has to hold together when the data turns messy |
| "Plan the redesign before we touch code" | Frame mode decides what you are building and rejects the obvious version first |

## Verification

```bash
# Confirm the install through the skills CLI
npx skills list | grep -i mies

# Or check the skills directory your agent scans
ls ~/.claude/skills/ | grep -i mies

# Review the skill straight from GitHub before installing
curl -sL https://raw.githubusercontent.com/deeflect/mies/main/skills/mies/SKILL.md | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| mies | Pass | Pass | Pass |

The catalog is a single skill deep, and the whole catalog was scored: all three engines pass.

## Limitations

- Single skill from a single author; there is no broader suite or framework to grow into.
- The repo is small (4 GitHub stars), so community review is thin.
- Last pushed 2026-05-29, so it is not tracking the newest agent-platform conventions.
- Verdicts are sampled on skills.sh; re-check the security pages before production use.
- Snapshot data, verified Oct 10, 2026: 8,774 combined installs across 1 indexed listings; 4 GitHub stars; MIT; last pushed 2026-05-29. Counts drift over time.

## Related

- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup) - the design-engineering counterpart to a design-taste skill
- [Design Judge Skills - Design Award Workflow Setup](/hermes/skills/catalog/design-judge-skills-setup) - run an award-style critique on the result
- [Better UI Skills - Interface Polish Suite Setup](/hermes/skills/catalog/better-ui-skills-setup) - a polish-focused pass over the same surfaces
- [design-review - Visual UI Audit & Fix Setup](/hermes/skills/catalog/design-review-setup) - audit a screen, then have mies cut it back
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run it on fresh output before review: removals are easier to argue early, when nobody is attached to the pixels yet.
- Give it a real screen with real data; the whole point is holding up when the data turns ugly.
- For a new build, let Frame run before any code exists; rejecting the obvious version early is cheaper than refactoring later.
- Land removals and exactness fixes in that order, so each change stays attributable in the diff.
- Pair it with a screenshot workflow so the agent can see before and after states of the same screen.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
