---
title: "Sentimony Skills - Dev Workflow & Review Gates Setup"
description: "Setup guide for sentimony/skills - 28.3K combined installs. 25 dev-workflow skills: TypeScript, testing, debugging, plan crafting, and review gates."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sentimony-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "dev workflow", "agent discipline", "testing"]
---

# Sentimony Skills - Setup Guide

**Source:** [sentimony/skills](https://www.skills.sh/sentimony/skills) via skills.sh - 28.3K combined installs across 25 indexed listings; first seen Aug 18, 2026 (evening sweep); converted Oct 10, 2026 (zero-catalog audit)
**GitHub:** [sentimony/skills](https://github.com/sentimony/skills) (6 stars, MIT license; pushed Oct 10, 2026; `plugins/<plugin>/skills/<name>/SKILL.md` layout)
**Category:** Dev Workflow / Agent Discipline
**Quality Tier:** 🟡 Beta - 25-skill dev-workflow suite; plugin layout; mixed sampled verdicts - see Security

Sentimony's skills repo packages developer discipline for coding agents into five plugins: devflow (14 skills), skills (9), writing (3), echarts, and skill-crafting. It has drawn 28.3K combined installs, and its busiest entries are the daily utilities: typescript (2,595), web-debug (2,361), vitest (2,347), and echarts (2,294). Underneath sits an opinionated loop: scope-triage classifies a request before design work, plan-crafting turns settled requirements into a TDD-oriented plan, inline-plan-dev or subagent-plan-dev executes it, review-request and review-resolution carry the review loop, and branch-finish closes verified work.

Skills live at `plugins/<plugin>/skills/<name>/SKILL.md`, and they install either individually through the skills CLI or as Claude Code and Codex plugins. Plugin skills are namespaced by their plugin (`/devflow:scope-triage`), and the workflow is composable rather than mandatory-linear: steps like debugging, git-worktree-isolation, and parallel-agents are reached when the work calls for them.

---

## Installation

Prerequisites: Node.js for the skills CLI, or Claude Code / Codex for the plugin route.

```bash
# Install everything for Codex and Claude Code
npx skills add sentimony/skills -a codex claude-code -y

# Install a single skill
npx skills add sentimony/skills -s typescript -a codex claude-code -y
```

Or install as plugins, which namespaces every skill:

```bash
# Claude Code
claude plugin marketplace add sentimony/skills
claude plugin install devflow@sentimony

# Codex
codex plugin marketplace add sentimony/skills
codex plugin add devflow@sentimony
```

Other plugins in the set: writing, skill-crafting, echarts, and skills.

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| typescript | 2,595 | Configure tsconfig, diagnose compiler behavior, and audit or migrate TypeScript projects |
| web-debug | 2,361 | Debug and verify local web apps via Playwright |
| vitest | 2,347 | Configure, write, debug, run, migrate, and audit Vitest tests |
| echarts | 2,294 | Build, audit, style, debug, and optimize Apache ECharts visualizations |
| plan-crafting | 2,051 | Turn an approved design into a bite-sized, TDD-oriented implementation plan |
| scope-triage | 2,050 | Classify request scope before design work and route to the right process |
| dashfix | 1,919 | Replace typographic dashes with the plain hyphen and audit a project per occurrence |
| negafix | 1,910 | Ban negative parallelism, audit prose for it, and score it 0-100 |
| commit-all | 1,671 | Gather the working tree into one commit per repository the session changed |
| maintaining-agent-context | 1,527 | Audit and maintain a repo's agent instruction architecture for Claude Code and Codex |
| frontend-crafting | 1,200 | Create, redesign, review, and polish interfaces with a verifiable quality gate |
| review-request | 627 | Prepare and dispatch independent code review against requirements, scope, and the diff |
| tdd | 625 | Drive behavior changes through valid RED, sufficient GREEN, and evidence-backed refactoring |
| parallel-agents | 625 | Prove work units independent and dispatch one bounded parallel wave |
| subagent-plan-dev | 623 | Execute a plan through scoped subagents with risk-based dispatch and verification |
| review-resolution | 623 | Validate and resolve review findings with evidence and explicit dispositions |
| inline-plan-dev | 623 | Execute a plan inline in the current session with reconciliation and durable resume |
| git-worktree-isolation | 623 | Select, detect, or create a safe isolated workspace with explicit ownership |
| debugging | 623 | Investigate bugs with a root-cause-first evidence workflow |
| branch-finish | 622 | Decide, execute, and report the integration outcome for verified work |

The remaining 5 indexed listings range from 85 to 330 installs, led by prose-crafting (330) and secret-hygiene (132).

## Why This Matters for Hermes Agents

Most agent failures are process failures: work that was never scoped, plans that drifted from reality, reviews that rubber-stamped a diff, branches merged without a verification pass. This suite encodes the countermeasures as skills a Hermes agent can reach for at each stage, from scope-triage at the front to branch-finish at the end, with review loops that demand evidence instead of assertions. The utilities stand alone as well: typescript, vitest, and web-debug cover the daily TypeScript and browser work, while dashfix and negafix police prose quality. Because everything ships per-skill and per-plugin, adoption can be gradual: start with scope-triage and commit-all, then add the review loop when the team is ready. The plugin namespacing pattern is also a clean model for Hermes skill authors building their own multi-plugin distributions.

## Usage

| You say | What happens |
|---|---|
| "Is this change small enough to just do?" | scope-triage classifies scope and routes to direct work, a light spec, or a full design cycle |
| "Turn this spec into an implementation plan" | plan-crafting produces a bite-sized, TDD-oriented plan |
| "Execute the plan in this session" | inline-plan-dev works through the plan with plan-reality reconciliation and durable resume |
| "Run this plan through subagents" | subagent-plan-dev dispatches scoped subagents with risk-based verification |
| "Get an independent review of this diff" | review-request prepares and dispatches review against requirements and the actual diff |
| "Debug why the settings page fails to load" | web-debug drives Playwright to reproduce the issue and gather browser evidence |
| "Commit everything I changed today" | commit-all gathers the working tree into one commit per changed repository |

## Verification

```bash
# Confirm the install through the skills CLI
npx skills list | grep -i sentimony

# Or check the plugin layout in a checkout of the repo
ls plugins/devflow/skills/

# Review the typescript skill from GitHub before installing
curl -sL https://raw.githubusercontent.com/sentimony/skills/main/plugins/skills/skills/typescript/SKILL.md | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| typescript | Pass | Pass | Pass |
| web-debug | Pass | Pass | Warn |
| vitest | Pass | Pass | Pass |

## Limitations

- Small repository: 6 GitHub stars and an independent publisher; the workflow suite is opinionated and young.
- Mixed sampled verdicts: web-debug carries a Snyk Warn, and coverage is partial across the 25 listings.
- Plugin migration caveat: from v1.56.0 the skills@sentimony plugin carries nine skills; the other 19 moved to devflow, writing, skill-crafting, and echarts, so install the plugins whose skills you use.
- The README lists 28 skills across five plugins while this snapshot indexes 25 listings; the experimental scope-check and webapp-debugger sit outside the index, so verify names when scripting installs.
- Snapshot data, verified Oct 10, 2026: 28,260 combined installs across 25 indexed listings; 6 GitHub stars; MIT; last pushed Oct 10, 2026. Counts drift over time.

## Related

- [Meticulous Agent Skills - Visual Regression Testing Setup](/hermes/skills/catalog/meticulous-agent-skills-setup) - visual regression checks to pair with frontend-crafting and web-debug
- [Skill Vetter - Security Audit for Hermes Skills Setup](/hermes/skills/catalog/skill-vetter-setup) - vet any skill's security before you install it
- [TanStack Skills - React Server State & Router Suite Setup](/hermes/skills/catalog/tanstack-skills-setup) - frontend stack skills that complement the typescript and vitest workflow
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with scope-triage: it is the documented entry point, and every step after it is reached on a condition rather than in sequence.
- Prefer plugin installs in Claude Code or Codex to get namespaced commands like `/devflow:scope-triage`.
- Pair plan-crafting with inline-plan-dev for solo work; switch to subagent-plan-dev when the work parallelizes.
- dashfix and negafix are cheap prose gates; run them over docs and PR descriptions before review.
- Install single utilities with `-s` (for example `-s vitest`) when you do not want the full workflow surface.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
