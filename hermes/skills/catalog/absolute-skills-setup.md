---
title: "Absolute Skills - AI Coding Workflow Engine Setup Guide"
description: "dhruvjainin/absolute: an 11-skill development workflow engine for AI coding agents - 15.3K combined installs across 96 listings."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/absolute-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "ai coding", "sdlc workflow", "spec-driven development"]
---

# Absolute Skills - Setup Guide

**Source:** [dhruvjainin/absolute](https://www.skills.sh/dhruvjainin/absolute) via skills.sh - 15.3K combined installs across 96 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 morning sweep)
**GitHub:** [dhruvjainin/absolute](https://github.com/dhruvjainin/absolute) - 225 stars, MIT license, main branch, last pushed Oct 26, 2026. Eleven skills live under `skills/<name>/SKILL.md` (103 files in the tree).
**Category:** AI Coding Workflow
**Quality Tier:** 🟠 Orange - 9 Fail among 20 sampled verdicts (Snyk: docker-kubernetes, frontend-developer, financial-reporting, figma-to-code, backend-engineering, vite-plus, game-balancing, clean-architecture, api-design; vite-plus also Fail on Gen Agent Trust Hub), 5 Warn (Socket: absolute-brainstorm, code-review-mastery, crm-management, internal-docs; Snyk: absolute-work), 6 all Pass. MIT license.

Absolute is a development workflow engine for AI coding agents: eleven opinionated skills spanning a one-time setup interview, a daily build loop (think, spec, plan, build, polish, document), and a five-skill engineering-health family that keeps the codebase maintained. Each skill installs independently and works with any agent that reads the SKILL.md format: Claude Code, Gemini CLI, OpenAI Codex, Cursor, and 40+ more.

The skills.sh page for dhruvjainin/absolute aggregates 96 indexed listings totaling 15,314 combined installs, but the repository itself holds only the eleven absolute skills. The remaining listings (docker-kubernetes, frontend-developer, financial-reporting and many others) are index-only rows with no counterpart in the current tree. Install commands in the README use the author's earlier GitHub username maddhruv, which GitHub resolves to dhruvjainin.

## Installation

Install with the `skills` CLI via `npx`. Install all eleven skills at once, or pick only what you need:

```bash
# Install all eleven skills
npx skills add maddhruv/absolute-init maddhruv/absolute-work maddhruv/absolute-spec \
  maddhruv/absolute-ui maddhruv/absolute-simplify maddhruv/absolute-docs \
  maddhruv/absolute-upgrade maddhruv/absolute-audit maddhruv/absolute-prune \
  maddhruv/absolute-debt maddhruv/absolute-deflake

# Or install individually
npx skills add maddhruv/absolute-work
npx skills add maddhruv/absolute-ui
```

Then invoke each skill by name (for example `/absolute-work`) and reload your agent if needed. Scope flags:

```bash
# Globally, available across all projects
npx skills add maddhruv/absolute-work -g

# To a specific agent
npx skills add maddhruv/absolute-work -a claude-code

# Non-interactive (CI/CD friendly)
npx skills add maddhruv/absolute-work -g -a claude-code -y
```

Managing installs:

```bash
npx skills list                      # list installed skills
npx skills check                     # check for updates
npx skills update                    # update everything
npx skills remove absolute-work      # remove a skill
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| absolute-audit | 589 | Defensive vulnerability and security scan of your own repo: dependency CVEs plus risky code patterns (secrets, injection, weak authz), triaged and remediated without suppressing findings |
| absolute-ui | 382 | Polished, intentional UIs with concrete CSS/Tailwind values: typography, color, layout, spacing, dark mode, accessibility, animations and components |
| absolute-simplify | 336 | Simplifying staged or unstaged git changes: reduce complexity, flatten nesting, remove redundancy and dead code, then run tests to prove nothing broke |
| docker-kubernetes | 273 | Docker and Kubernetes guidance; no counterpart in the current repo tree |
| frontend-developer | 210 | Frontend development guidance; no counterpart in the current repo tree |
| financial-reporting | 209 | Financial reporting guidance; no counterpart in the current repo tree |
| absolute-work | 202 | End-to-end, phase-gated SDLC: design interview, reviewed spec, dependency-graphed task board, safe-wave TDD execution, verification and converge |
| figma-to-code | 202 | Figma-to-code conversion guidance; no counterpart in the current repo tree |
| backend-engineering | 200 | Backend engineering guidance; no counterpart in the current repo tree |

The remaining 87 indexed listings range from 87 to 194 installs, led by vite-plus and second-brain (194 each), game-balancing (191) and clean-architecture (190). Most of these carry no counterpart in the current repo tree.

## Why This Matters for Hermes Agents

The absolute family targets the exact failure mode that trips coding agents: they start writing before the design is settled, ship UIs that look machine-made, leave the diff messier than it needed to be, and let docs drift from the code. absolute-work enforces a phase-gated loop (interview, spec, plan, safe-wave TDD execution, verify, converge) with hard gates so an agent does not run ahead. absolute-ui encodes concrete CSS/Tailwind values, which is the difference between "make it clean" and an actual spacing, color and type system. The engineering-health family (upgrade, audit, prune, debt, deflake) turns standing maintenance into risk-ranked, gated scan-and-fix passes that never cheat the checker. Every skill writes files and reports but never auto-commits, so the human stays in control at each gate. For Hermes builders this is a drop-in SDLC discipline that works across any SKILL.md-compatible harness.

## Usage

| You say | What happens |
|---|---|
| /absolute-init | Interviews you for output style, autonomy and TDD strictness, detects the stack once, then writes .absolute.config.json that every other skill reads |
| /absolute-work "Add OAuth2 login with Google and GitHub" | Plans it, builds it and verifies it through the phase-gated SDLC |
| /absolute-spec "Design a commenting system" | Writes a reviewed design doc to docs/plans/ and stops without building |
| /absolute-ui "Design a pricing page" | Makes the UI look intentional, not generated, with concrete CSS/Tailwind values |
| /absolute-simplify | Cleans up your working git diff before you commit |
| /absolute-audit | Scans dependencies and code for CVEs and risky patterns, then triages and remediates |
| /absolute-deflake | Fixes the tests that fail randomly, without retry, skip or sleep |

## Verification

```bash
# confirm what is installed
npx skills list
# review the flagship SKILL.md before relying on it
curl -sL https://raw.githubusercontent.com/dhruvjainin/absolute/main/skills/absolute-work/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| absolute-audit | Pass | Pass | Pass |
| absolute-ui | Pass | Pass | Pass |
| absolute-simplify | Pass | Pass | Pass |
| docker-kubernetes | Pass | Warn | Fail |
| frontend-developer | Pass | Warn | Fail |
| financial-reporting | Warn | Pass | Fail |
| absolute-work | Pass | Pass | Warn |
| figma-to-code | Pass | Pass | Fail |
| backend-engineering | Pass | Pass | Fail |
| vite-plus | Fail | Warn | Fail |
| second-brain | Pass | Pass | Pass |
| game-balancing | Pass | Warn | Fail |
| clean-architecture | Pass | Pass | Fail |
| absolute-brainstorm | Pass | Warn | Pass |
| code-review-mastery | Pass | Warn | Pass |
| budgeting-planning | Pass | Pass | Pass |
| crm-management | Pass | Warn | Pass |
| api-design | Pass | Pass | Fail |
| absolute-spec | Pass | Pass | Pass |
| internal-docs | Pass | Warn | Pass |

## Limitations

- Snapshot data, verified Nov 20, 2026: 15,314 combined installs across 96 indexed listings; 225 GitHub stars; MIT license; last pushed Oct 26, 2026. Counts drift over time.
- Only 20 of 96 listings carry skills.sh verdicts; the other 76 are unverified on that platform.
- The repo tree holds eleven absolute skills; the other 85 indexed listings (docker-kubernetes, frontend-developer, financial-reporting and the rest) have no counterpart in the current tree, so install commands and paths for them are unverified here.
- The README installs skills under the author's earlier GitHub username maddhruv (maddhruv/absolute-<name>), which GitHub resolves to dhruvjainin; the skills.sh page lists the same skills under dhruvjainin/absolute.
- The README documents the eleven-skill workflow but not the broader listing set, so anything beyond the absolute family should be reviewed skill by skill before install.

## Related

- [Warp Common Skills - Spec-Driven Development Workflow Setup](/hermes/skills/catalog/warpdotdev-common-skills-setup)
- [OpenSpec Skills - Spec-Driven Development Suite Setup](/hermes/skills/catalog/fission-openspec-skills-setup)
- [Simplify Code - Parallel Review & Cleanup Setup](/hermes/skills/catalog/simplify-code-setup)
- [Uizze UI Skills - Anti-UI-Slop Design Quality Setup](/hermes/skills/catalog/uizze-ui-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run absolute-init once per repo first; every other skill reads its config instead of re-detecting the stack.
- Let absolute-work run the full loop for anything beyond a single-file change; its hard gates keep the agent from running ahead of the design.
- Use absolute-ui before shipping any new screen: it replaces vague advice with concrete CSS/Tailwind values.
- Run the five engineering-health skills (upgrade, audit, prune, debt, deflake) on green main, not mid-feature.
- The skills never auto-commit; review the files each skill writes and commit yourself.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
