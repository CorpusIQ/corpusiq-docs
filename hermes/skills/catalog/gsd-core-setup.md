---
title: "GSD Core - Spec-Driven Development Workflow Skills"
description: "open-gsd/gsd-core: 72 spec-driven development skills driving a discuss-plan-execute-verify-ship loop for coding agents - 41.4K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gsd-core-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "spec-driven development", "engineering workflow", "coding agents"]
---

# GSD Core - Spec-Driven Development Workflow Skills

**Source:** [open-gsd/gsd-core](https://www.skills.sh/open-gsd/gsd-core) via skills.sh - 41.4K combined installs across 72 indexed listings; first seen Nov 21, 2026 (Nov 21, 2026 morning sweep)
**GitHub:** [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) - 11,745 stars, MIT license, next branch, last pushed Nov 21, 2026; a packaged meta-prompting and spec-driven development system where each skill ships twice, once under `skills/<name>/SKILL.md` and once under `pi/package-skills/<name>/SKILL.md`.
**Category:** Spec-Driven Development and Engineering Workflow
**Quality Tier:** 🟠 Orange - 20 of 72 skills sampled; 2 Fail cells (gsd-quick Snyk, gsd-progress Gen Agent Trust Hub) and 6 Warn cells.

GSD Core is a spec-driven development system from open-gsd that drives AI coding agents through a disciplined phase loop: Discuss, Plan, Execute, Verify, Ship. It is the largest publisher in the Nov 21, 2026 morning sweep by a wide margin, with 41.4K combined installs across 72 indexed listings and 11,745 GitHub stars. The stated goal is to fight context rot: heavy research, planning and execution run in fresh-context subagents while the main session stays lean, and structured artifacts such as STATE.md and CONTEXT.md survive session boundaries.

The skill set is one workflow, not a grab bag. Most of the 72 skills are single-purpose commands in the loop (gsd-plan-phase, gsd-execute-phase, gsd-verify-work) or lifecycle helpers (gsd-new-project, gsd-onboard, gsd-ship, gsd-pause-work), plus a family of namespace, memory and audit tools (gsd-ns-*, gsd-mempalace-*, gsd-audit-*). The repo ships every skill twice, once under skills/ and once under pi/package-skills/, with the plugin package carrying the installable surface.

## Installation

Install via the npm installer, which prompts for your runtime and whether to install globally or locally:

```bash
npx @opengsd/gsd-core@latest
```

The installer is required for cross-runtime compatibility, so do not copy files from the agents/ or commands/ directories by hand. Once installed, start a new project or onboard an existing repo:

```bash
/gsd-new-project   # greenfield project
/gsd-onboard       # existing codebase
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| gsd-code-review | 599 | reviewing the files a phase changed for bugs, security issues and code quality problems |
| gsd-execute-phase | 597 | running every plan in a phase with dependency-aware parallel waves |
| gsd-verify-work | 596 | walking through what was built and validating it conversationally |
| gsd-plan-phase | 596 | writing the phase plan (PLAN.md) and verifying it fits a fresh context window |
| gsd-help | 595 | listing the available GSD commands and their usage |
| gsd-discuss-phase | 592 | capturing implementation decisions through adaptive questioning before planning |
| gsd-new-project | 591 | initializing a new project with deep context gathering and PROJECT.md |
| gsd-map-codebase | 591 | mapping a codebase with parallel agents into .planning/codebase/ documents |

The remaining 64 indexed listings range from 342 to 588 installs.

## Why This Matters for Hermes Agents

Spec-driven development is a discipline problem for agents: without a loop, an agent drafts a plan, wanders off it, and declares done on whatever it produced. GSD Core pins the loop to five named phases so the agent always knows where it is and what comes next. Each phase has a dedicated skill, so a Hermes agent can be told to plan a phase or verify the work and route to the right procedure instead of improvising one.

The context-engineering angle is what makes it worth a closer look for operators running long sessions. Heavy work runs in fresh-context subagents, which means a phase plan is produced and executed without carrying the whole session's context bloat forward. The verify step is a walk-through, not a green checkmark: it validates what was actually built and files fix plans before a phase is declared done. For a Hermes agent, that maps to a pattern where the agent proposes, a subagent executes, and the main session confirms against the spec before shipping.

## Usage

| You say | What happens |
|---|---|
| Start a new project from scratch | Runs gsd-new-project, gathers context and writes PROJECT.md |
| Onboard this existing repo | Runs gsd-onboard to map the codebase and set up state |
| Plan the next milestone | Runs gsd-new-milestone and gsd-plan-phase to write ROADMAP.md and PLAN.md |
| Execute the phase | Runs gsd-execute-phase, which runs plans in parallel waves in fresh contexts |
| Verify what was built | Runs gsd-verify-work to walk through features conversationally and file fixes |
| Ship it | Runs gsd-ship to open the PR, run review and prepare for merge |
| I am pausing for the day | Runs gsd-pause-work to write a context handoff you can resume later |

## Verification

Review a skill's instructions before installing, and confirm the file resolves on the default next branch:

```bash
curl -sL https://raw.githubusercontent.com/open-gsd/gsd-core/next/skills/gsd-code-review/SKILL.md | head -40
```

After install, run /gsd-help to confirm the installer wired the skills into your runtime and to see the command list.

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gsd-code-review | Pass | Pass | Pass |
| gsd-execute-phase | Pass | Pass | Pass |
| gsd-verify-work | Pass | Warn | Pass |
| gsd-plan-phase | Pass | Pass | Warn |
| gsd-help | Pass | Pass | Pass |
| gsd-discuss-phase | Pass | Pass | Pass |
| gsd-new-project | Pass | Pass | Warn |
| gsd-map-codebase | Pass | Pass | Pass |
| gsd-debug | Pass | Pass | Pass |
| gsd-ui-phase | Pass | Pass | Pass |
| gsd-quick | Pass | Pass | Fail |
| gsd-new-milestone | Pass | Pass | Warn |
| gsd-ship | Pass | Warn | Pass |
| gsd-pause-work | Pass | Pass | Pass |
| gsd-ui-review | Pass | Pass | Pass |
| gsd-sketch | Pass | Pass | Warn |
| gsd-plan-review-convergence | Pass | Pass | Pass |
| gsd-progress | Fail | Pass | Pass |
| gsd-phase | Pass | Pass | Pass |
| gsd-config | Pass | Pass | Pass |

The gsd-quick and gsd-progress skills carry Fail cells, so review their instructions before relying on them in an unattended loop.

## Limitations

- Snapshot data, verified Nov 21, 2026: 41,394 combined installs across 72 indexed listings; 11,745 GitHub stars; MIT license; last pushed Nov 21, 2026. Counts drift over time.
- The install index and the repo tree agree at 72 listings, but the repo ships every skill twice (skills/ and pi/package-skills/), and only 20 of the 72 skills have a description in the pack.
- The security sample covers 20 of 72 listings; the other 52 carry no skills.sh verdict in this snapshot.
- The default branch is next, not main, so keep next in raw URLs and pinned commands.
- GSD Core is a heavyweight workflow system: installing it changes how an agent plans and ships, so trial it on one project before adopting it across a team.

## Related

- [Spec Kit Skills - Specify, Plan, Implement](/hermes/skills/catalog/speckit-agent-skills-setup)
- [Subagent-Driven Development - Multi-Agent Task Dispatch Setup](/hermes/skills/catalog/subagent-driven-development-setup)
- [Context Engineering Kit - Prompt and MCP Setup](/hermes/skills/catalog/context-engineering-kit-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with gsd-onboard on an existing repo before gsd-new-project; onboarding exercises the map and plan skills without the greenfield setup cost.
- Run /gsd-help first to see which commands your runtime actually wired, because the installer routes differently per runtime.
- Do not skip the verify step even when the plan looks done; it is the phase that catches a subagent's drift.
- Pin the installer version when you roll out to a team, and test on one project before spreading it wider.
- Remember the default branch is next, not main, when you pin skill files by URL.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
