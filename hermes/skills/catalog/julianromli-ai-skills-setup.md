---
title: "Julianromli Skills - Frontend and Product Craft"
description: "julianromli/ai-skills on skills.sh: 5.1K combined installs across 43 listings; frontend design, motion polish, site cloning and Vercel deploy skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/julianromli-ai-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "frontend design", "ui polish", "react"]
---

# Julianromli Skills - Setup Guide

**Source:** [julianromli/ai-skills](https://www.skills.sh/julianromli/ai-skills) via skills.sh - 5.1K combined installs across 43 indexed listings; first seen 2026-11-07 (Nov 7, 2026 morning sweep)
**GitHub:** 214 stars, no LICENSE file in the repository root, branch `main`, last pushed 2026-10-26, 31 SKILL.md directories under `skills/`
**Category:** Frontend craft for agents: design engineering, motion, landing-page cloning, Convex data patterns and deployment to Vercel
**Quality Tier:** 🟡 Yellow - the sampled skills pass Gen Agent Trust Hub and Socket, two carry Snyk warnings, and the repository ships no LICENSE file at its root.

This is a personal collection rather than a publisher release. Julian Romli's repository holds 31 skill directories covering the work around a frontend build: design direction, interface polish, motion, site cloning, React and Next.js performance, Convex and Supabase data rules, code review discipline, deployment to Vercel, and a few small odd jobs like PDF handling and social copy. The README calls it "a curated collection of AI agent skills for coding, frontend, debugging, product thinking, and workflow automation", and each package is meant to be read straight from `skills/<name>/SKILL.md`.

The install distribution is extremely top-heavy. `clone-website` alone accounts for 2,238 of the 5,054 recorded installs, and the second entry sits at 342. That shape tells you something useful: people come for the site-cloning workflow and pick up the design skills beside it. The polish skills are the interesting part, because they encode specific design-engineering rules (concentric border radius, optical alignment, shadows over borders, interruptible transitions) that models otherwise approximate badly.

## Installation

The install route the skills.sh listing page shows:

```bash
npx skills add julianromli/ai-skills
```

That pulls the collection in one step. The repository README documents no per-skill flag, so the alternative it does describe is manual: browse `skills/`, open the directory you want, read its `SKILL.md`, and carry any supporting files with it. Clone and copy the directories you actually need:

```bash
git clone https://github.com/julianromli/ai-skills.git
mkdir -p .agents/skills
cp -r ai-skills/skills/make-interfaces-feel-better .agents/skills/
cp -r ai-skills/skills/clone-website .agents/skills/
```

Copy whole directories. Several skills keep topic pages beside `SKILL.md` (the polish skill references `typography.md`, `surfaces.md`, `animations.md` and `performance.md`), and a `SKILL.md`-only copy loses the detail the skill routes the agent toward.

`clone-website` is the one to read before installing. Its pre-flight assumes a Next.js project with shadcn/ui and Tailwind v4 already scaffolded, asks for a browser automation MCP tool (Chrome MCP preferred), and requires `npm run build` to pass before it starts.

## What It Provides

Six listings clear the 100-install threshold:

| Skill | Installs | Use For |
|---|---|---|
| clone-website | 2,238 | Website reverse-engineering: extracts assets, CSS and content section by section, then dispatches parallel builder agents in worktrees to rebuild it pixel-perfect |
| frontend-ui-animator | 342 | UI animation work by name, but no `skills/frontend-ui-animator` directory exists in the current tree, so check what the listing resolves to before relying on it |
| make-interfaces-feel-better | 187 | Design-engineering polish: concentric radius, optical over geometric alignment, layered shadows instead of borders, interruptible transitions and staggered enter animations |
| frontend-design | 180 | Distinctive production-grade interface direction with an explicit anti-slop rule set across typography, colour, motion, spatial composition and background texture |
| browser | 129 | Browser automation by name, with no matching directory in the tree; the tree ships `agent-browser` (53 installs) for that job instead |
| ui-ux-pro-max | 124 | Design intelligence database: 50+ styles, 161 colour palettes, 57 font pairings, 99 UX guidelines and 25 chart types across 10 stacks |

The remaining 37 indexed listings range from 1 to 83 installs.

The tail is where the working skills live, not the leftovers. `frontend-skill`, `web-design-guidelines`, `shadcn`, `refactor-clean`, `systematic-debugging`, `deploy-to-vercel`, `convex-best-practices`, `supabase-postgres-best-practices`, `vercel-react-best-practices` and the two code-review skills all sit between 40 and 83 installs, and each has a directory in the tree.

## Why This Matters for Hermes Agents

Generic models produce interfaces that pass at a glance and fail on inspection: nested elements with the outer radius equal to the inner one, icon buttons that look off-centre because they are geometrically centred, borders standing in for depth, and keyframe animations that cannot be interrupted. `make-interfaces-feel-better` states those as rules with reasoning, and the rules survive review because they are checkable.

The collection also covers the seams around a build rather than only the UI layer. `refactor-clean` for cleanup, `requesting-code-review` and `receiving-code-review` for the review handshake, `systematic-debugging` for failures, `deploy-to-vercel` for shipping. An agent moving through those phases has guidance at each step instead of one design skill and no process.

`ui-ux-pro-max` is the lookup table of the set: 50+ styles, 161 palettes, 57 font pairings, 99 UX guidelines, 25 chart types across 10 stacks. When a task needs a decision (which style, which pairing, which chart) an explicit catalogue beats interpolation, and the skill states when to skip itself, which is rare enough to be worth noting.

`clone-website` is the outlier in both installs and behaviour. It does not generate a lookalike from a screenshot; it walks the target page section by section, writes a specification per section, and hands each specification to a builder agent in a worktree. Treat it as a workflow with real side effects rather than a prompt.

## Usage

| You say | What happens |
|---|---|
| "Clone this landing page and rebuild it in my Next.js app" | `clone-website` runs its pre-flight (browser MCP, build check), extracts section specs, and dispatches parallel builders in worktrees |
| "The spacing in these cards feels off" | The polish skill applies the concentric radius rule and the optical alignment rule before touching colour or typography |
| "Make this dashboard feel more expensive" | `ui-ux-pro-max` picks a style and palette from its catalogue, then `make-interfaces-feel-better` refines motion and surfaces |
| "Add a page transition that doesn't fight the user" | The animation guidance prefers CSS transitions that can be interrupted mid-flight over keyframes for interactive state |
| "Review this component file for design sins" | `web-design-guidelines` and the polish skill produce a rule-by-rule pass, including fixed `dark:` variants and mismatched nesting radii |
| "Ship this to Vercel and give me the link" | `deploy-to-vercel` handles the preview deployment request and reports the URL back |
| "Clean up the dead code before I open a PR" | `refactor-clean` scopes the removal, then `requesting-code-review` prepares the change for review |

## Verification

Read the skill before installing it. These paths returned HTTP 200 on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/julianromli/ai-skills/main/skills/make-interfaces-feel-better/SKILL.md | head -40
curl -fsSL https://raw.githubusercontent.com/julianromli/ai-skills/main/skills/frontend-design/SKILL.md | head -40
curl -fsSL https://raw.githubusercontent.com/julianromli/ai-skills/main/skills/clone-website/SKILL.md | head -40
curl -fsSL https://raw.githubusercontent.com/julianromli/ai-skills/main/skills/ui-ux-pro-max/SKILL.md | head -20
```

The polish skill should open with a categories table pointing at `typography.md`, `surfaces.md`, `animations.md` and `performance.md`. If those companion files are not in the directory after install, the skill is incomplete.

Two listings in the table have no file to read at all. Confirm what you actually received before trusting either one:

```bash
ls .agents/skills | wc -l
curl -s -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/julianromli/ai-skills/main/skills/frontend-ui-animator/SKILL.md
```

The second command returns 404, which is why the row above says nothing about what that listing does.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| clone-website | Pass | Pass | Warn |
| vercel-react-view-transitions | Pass | Pass | Pass |
| agent-browser | Pass | Pass | Warn |
| convex-best-practices | Pass | Pass | Pass |
| collapsible-sidebar | Pass | Pass | Pass |

Two Snyk warnings land on the two skills that touch a browser and a live site, which is where you would expect caution anyway. `clone-website` drives a browser against an arbitrary URL and spawns builder agents that write files, so run it against sites you have the right to copy and inside a repository you can throw away. `agent-browser` is a browser automation CLI, so its blast radius is whatever credentials the browser session holds.

The repository has no LICENSE file at its root, which matters more than usual here because installs are copies of source you are expected to keep. One skill does carry its own terms: `frontend-design` ships a `LICENSE.txt` and its frontmatter points at it. Everything else relies on whatever the repository implies, which is nothing enforceable.

## Limitations

- Snapshot data, verified 2026-11-07: 5,054 combined installs across 43 indexed listings; 214 GitHub stars; no LICENSE file; last pushed 2026-10-26. Counts drift over time.
- No LICENSE file in the repository root, so reuse and redistribution terms are undefined for the collection as a whole. `skills/frontend-design/LICENSE.txt` exists and covers that one skill.
- The install index outruns the tree: 43 indexed listings against 31 SKILL.md directories. `frontend-ui-animator` (342 installs) and `browser` (129 installs) have no matching directory, so this guide describes them at name level only.
- Index names and directory names do not always match. The tree has `skills/composition-patterns`, `skills/react-best-practices`, `skills/react-view-transitions`, `skills/react-native-skills` and `skills/gpt-tasteskill`, while the install index lists `vercel-composition-patterns`, `vercel-react-best-practices`, `vercel-react-view-transitions`, `vercel-react-native-skills` and `gpt-taste`, so cross-referencing a row to a file takes care.
- Several skills are Claude Code shaped: `clone-website` declares `argument-hint`, `user-invocable: true` and consumes `$ARGUMENTS`, and `design-engineer-router` expects the separate `emil-*` skills, which the README says are not included.
- Quality varies by skill, and nothing enforces consistency. These are one author's working notes across 31 packages, with no tests and no linter.

## Related

- [Frontend God Mode - Design Skills Bundle Setup](/hermes/skills/catalog/frontend-god-mode-setup)
- [Better UI Skills - Interface Polish Suite Setup](/hermes/skills/catalog/better-ui-skills-setup)
- [shadcn Skill - shadcn/ui Component Workflows Setup](/hermes/skills/catalog/shadcn-ui-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install selectively. Six of 43 listings clear 100 installs and the useful design rules are concentrated in three or four directories, so a full clone mostly adds context noise.
- Pair the polish skill with a review request. Asking for a rule-by-rule pass ("check nested radii, optical alignment, shadow depth") gets concrete fixes where "make it nicer" gets repainting.
- Read `clone-website`'s out-of-scope list before running it. It clones what is visible at the URL and explicitly excludes backend, auth and real-time features.
- Treat `vercel-` prefixed listings as the packaged names for the plain directories. When a listing and a directory disagree, read the directory's `SKILL.md` before assuming they are different skills.
- Skip `design-engineer-router` unless you have the `emil-*` pack. The README states those skills are not included, so the router has nothing to route to on its own.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
