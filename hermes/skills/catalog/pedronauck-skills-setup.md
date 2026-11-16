---
title: "Pedro Nauck Skills - Curated Agent Skill Library"
description: "pedronauck/skills - 32.0K combined installs across 96 indexed listings: React, TypeScript, and UI engineering skills plus QA and marketing workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pedronauck-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "react", "typescript", "qa"]
---

# Pedro Nauck Skills - Setup Guide

**Source:** [pedronauck/skills](https://www.skills.sh/pedronauck/skills) via skills.sh - 32.0K combined installs across 96 indexed listings; first seen Nov 16, 2026 (Nov 16 morning sweep)
**GitHub:** 655 stars, MIT license, `main` branch, last pushed 2026-11-16, `SKILL.md` files under `skills/mine/<name>/`, `skills/curated/<name>/`, and `skills/marketing/<name>/`
**Category:** Frontend engineering and business - React, TypeScript, UI, QA and marketing workflows
**Quality Tier:** 🟡 Yellow - all sampled skills pass the Gen Agent Trust Hub and Socket; qa-execution and agent-browser carry a Snyk Warn.

Pedro Nauck's skills repository is a curated collection of agent skills for Claude Code and compatible AI coding assistants, organized into three buckets: `skills/mine/` (43 original skills), `skills/curated/` (33 hand-picked community skills), and `skills/marketing/` (13 marketing and business skills). Each skill is a directory holding a `SKILL.md` plus optional references, examples, templates, scripts, and checklists.

The suite spans frontend engineering (React 19 under the React Compiler, Tailwind CSS v4, advanced TypeScript), QA (dogfooding through public interfaces and living QA docs), and business workflows (fundraising, sales methodology, and copywriting). Two indexed listings, motion-react and skill-best-practices, carry install counts but have no matching `SKILL.md` directory in the current tree.

## Installation

Install the whole repository into your agent skills directory with the `skills` CLI:

```bash
npx skills add https://github.com/pedronauck/skills
```

Install a single bucket with the `owner/repo/<subpath>` shorthand, or pin one skill:

```bash
# Only the original skills
npx skills add pedronauck/skills/skills/mine

# Only the curated skills
npx skills add pedronauck/skills/skills/curated

# Pin a specific skill from a bucket
npx skills add pedronauck/skills/skills/mine --skill react
```

Manual install by copying or symlinking into your Claude Code configuration:

```bash
# Copy a single skill
cp -r skills/mine/react ~/.claude/skills/react

# Or symlink an entire bucket
ln -s $(pwd)/skills/mine ~/.claude/skills/mine
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| motion-react | 1,208 | No counterpart SKILL.md in the current tree (indexed listing only). |
| tui-design | 626 | Design terminal UIs: layouts, color schemes, keyboard navigation, dashboards, and accessibility across TUI frameworks. |
| no-workarounds | 590 | Evaluate proposed fixes that suppress errors or symptoms; enforce root-cause fixes over workarounds and hacks. |
| typescript-advanced | 584 | Advanced TypeScript types, reusable type utilities, and compile-time contracts with generics, conditional and mapped types. |
| qa-execution | 564 | Run dogfooding through public product interfaces; plan with qa-report and record findings in living QA docs. |
| architectural-analysis | 552 | Audit architecture, dead code, duplication, type confusion, and code smells across a codebase. |
| qa-report | 547 | Own living QA docs: journey and scenario plans, persona session charters, and the durable bug registry. |
| tailwindcss | 480 | Style components with Tailwind CSS v4 and project design tokens. |
| react | 480 | Build React 19 components and hooks under React Compiler: state, Effects, memoization, Actions, and Vitest tests. |
| skill-best-practices | 476 | No counterpart SKILL.md in the current tree (indexed listing only). |
| agent-browser | 470 | Browser automation CLI for AI agents: navigate, fill forms, click, screenshot, extract data, and test web apps. |

The remaining 85 indexed listings range from 227 to 447 installs.

## Why This Matters for Hermes Agents

The strongest entries here treat quality as a repeatable process rather than an afterthought. no-workarounds forces root-cause fixes over symptom patches, while verification-before-completion requires confirming command output before a task is claimed done. Together they attack the two most common failure modes of a long-running agent: shipping a hack and declaring success without evidence.

The QA pair is a real workflow, not two loose skills. qa-report owns the durable bug registry, journey plans, and persona charters, while qa-execution runs the live dogfooding sessions and fix loops against public interfaces. For an agent that must validate its own changes before a release, this division is directly reusable.

The frontend stack is unusually deep for one repo: React 19 under the React Compiler, Tailwind CSS v4, advanced TypeScript types, and TanStack patterns all live here, so a single install covers most of a modern React toolchain.

## Usage

| You say | What happens |
|---|---|
| "Audit this codebase's architecture" | architectural-analysis reports dead code, duplication, type confusion, and code smells. |
| "Is this fix just masking the symptom?" | no-workarounds evaluates the proposed fix for suppressed errors or symptoms. |
| "Dogfood the release like a real user" | qa-execution runs dogfooding through public product interfaces and records findings. |
| "Build a React 19 component with hooks" | react applies React Compiler rules for state, Effects, memoization, and Actions. |
| "Style this with Tailwind" | tailwindcss applies Tailwind CSS v4 patterns and project design tokens. |
| "Write advanced TypeScript types" | typescript-advanced builds generics, conditional and mapped types, and template literals. |
| "Set up living QA docs" | qa-report owns journey and scenario plans, persona charters, and the bug registry. |

## Verification

Check the skill files before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/pedronauck/skills/main/skills/mine/react/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/pedronauck/skills/main/skills/curated/tui-design/SKILL.md | head -20
npx skills add pedronauck/skills/skills/mine --skill react
```

Skills live in three buckets (`skills/mine/`, `skills/curated/`, `skills/marketing/`); confirm the specific path exists in the current tree before installing an individual skill.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| motion-react | Pass | Pass | Pass |
| tui-design | Pass | Pass | Pass |
| no-workarounds | Pass | Pass | Pass |
| typescript-advanced | Pass | Pass | Pass |
| qa-execution | Pass | Pass | Warn |
| architectural-analysis | Pass | Pass | Pass |
| qa-report | Pass | Pass | Pass |
| tailwindcss | Pass | Pass | Pass |
| react | Pass | Pass | Pass |
| skill-best-practices | Pass | Pass | Pass |
| agent-browser | Pass | Pass | Warn |
| electron-builder | Pass | Pass | Pass |

The sample has no Gen Agent Trust Hub or Socket fails; the two Snyk Warns (qa-execution and agent-browser) flag dependency-level findings.

## Limitations

- Snapshot data, verified Nov 16, 2026: 32,017 combined installs across 96 indexed listings; 655 GitHub stars; MIT; last pushed 2026-11-16. Counts drift over time.
- Two indexed listings, motion-react and skill-best-practices, carry install counts but have no matching `SKILL.md` directory in the current tree.
- The README catalogs 89 skills while the index counts 96 listings, so a few indexed names are not described in the README.
- Only the original `skills/mine/` skills carry the MIT license; `skills/curated/` and `skills/marketing/` come from other authors and keep their upstream licenses (sources in `upstream/sources.json`).
- The repo targets Claude Code and compatible assistants; skills match on the `description` field in each `SKILL.md`, so an agent without skill discovery will not load them.

## Related

- [React Doctor](/hermes/skills/catalog/react-doctor-setup)
- [Matt Pocock TypeScript Developer Toolkit](/hermes/skills/catalog/mattpocock-skills-setup)
- [TanStack Skills](/hermes/skills/catalog/tanstack-skills-setup)
- [UI Craft](/hermes/skills/catalog/ui-craft-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install only the bucket you need (`mine`, `curated`, or `marketing`) rather than the whole repo to keep the agent's skill list lean.
- Pin individual skills with `--skill` when you want one skill from a bucket without the rest.
- Skills match on the `SKILL.md` description field, so keep descriptions concise when authoring your own skills in this layout.
- Track `curated/` and `marketing/` skills through `upstream/sources.json` so upstream updates stay attributable.
- For discipline skills like no-workarounds, baseline-test against an agent without the skill first to measure the difference.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
