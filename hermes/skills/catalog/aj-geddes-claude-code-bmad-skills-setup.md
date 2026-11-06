---
title: "BMAD Planning and Orchestrator - Claude Code Plugin"
description: "aj-geddes/claude-code-bmad-skills on skills.sh: 5.5K combined installs across 5 listings; BMAD planning and orchestration as a Claude Code plugin."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/aj-geddes-claude-code-bmad-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "bmad", "planning", "claude code plugin"]
---

# BMAD Planning and Orchestrator - Setup Guide

**Source:** [aj-geddes/claude-code-bmad-skills](https://www.skills.sh/aj-geddes/claude-code-bmad-skills) via skills.sh - 5.5K combined installs across 5 indexed listings; first seen 2026-11-05 (Nov 5, 2026 evening sweep)
**GitHub:** 493 stars, MIT, last pushed 2026-06-19, one plugin containing 20 skills under `bmad-planning-orchestrator/skills/` plus a marketplace manifest at the repository root
**Category:** BMAD planning for agents: PRD, architecture, sprint planning and course correction shipped as a Claude Code plugin
**Quality Tier:** 🟡 Usable with review - two of the five sampled audits are not clean: business-analyst Failed Gen Agent Trust Hub and Warned on Snyk, and creative-intelligence Warned on Snyk. The plugin also ships shell hooks that run at session start and stop.

This repository is a Claude Code plugin marketplace that ships exactly one plugin, BMAD Planning & Orchestrator, a harness for the BMAD Method's planning and orchestration workflow. It deliberately stops before implementation: the last artifact it produces is a `ready-for-dev` story file plus a `handoff-manifest.json`, and the README states plainly that it does not write, run or review code. The `developer` skill, the `/dev-story` command and the lint and coverage helpers were removed, which `MIGRATION.md` documents.

Two naming layers exist and they need separating before you install anything. The skills.sh index lists five listings by BMAD agent role: business-analyst, product-manager, system-architect, ux-designer and creative-intelligence. None of those five has a directory in the current tree. The tree ships 20 `bmad-*` skills instead, and several of them name the older role as their upstream counterpart, for example `bmad-product-brief` records `bmad-business-analyst` and `bmad-ux` says it implements the spirit of `bmad-ux-designer`. The install counts therefore attach to the role named skills from the pre-plugin suite, while the thing you actually get is the 20 skill plugin.

## Installation

This is a plugin, not a skills.sh bundle, so the install is two slash commands inside Claude Code:

```text
/plugin marketplace add aj-geddes/claude-code-bmad-skills
/plugin install bmad-planning-orchestrator@bmad-method-harness
```

Then `/reload-plugins`, or restart Claude Code. The marketplace manifest lives at the repository root (`.claude-plugin/marketplace.json`), so `marketplace add` targets the whole repository rather than the `bmad-planning-orchestrator/` subdirectory.

For local development against a checkout, the plugin can be loaded directly:

```text
claude --plugin-dir ./bmad-planning-orchestrator
```

Skills are namespaced as `/bmad-planning-orchestrator:<skill>`, and most of them are auto-invoked by Claude based on what you are doing. Output folder (default `bmad-output/`), default track and maximum parallel workstreams are set at enable time through `userConfig`.

If you used the older skills installer, `MIGRATION.md` lists the three directories to remove under `~/.claude` (`skills/bmad`, `commands/bmad`, `config/bmad`) before installing the plugin.

## What It Provides

The five indexed listings, with the skill in the current tree that now owns the same work:

| Skill | Installs | Use For |
|---|---|---|
| business-analyst | 2,233 | Business analysis and product brief work; the current tree ships that role as bmad-product-brief, which names bmad-business-analyst as its upstream counterpart |
| product-manager | 1,183 | PRD and roadmap work; bmad-prd covers functional and non-functional requirements, epics and MoSCoW, and bmad-research routes competitive questions to product-manager |
| system-architect | 802 | Architecture decisions and non-functional coverage; bmad-architecture produces architecture.md plus ADRs and is the skill that prevents semantic conflicts |
| ux-designer | 717 | UX contracts; bmad-ux produces two documents, DESIGN.md with tokens and WCAG AA targets and EXPERIENCE.md with journeys |
| creative-intelligence | 589 | Research and ideation; bmad-research and bmad-brainstorm cover the work, and bmad-prfaq hands unresolved questions to creative-intelligence |

No indexed listings fall below the 500-install threshold; all five appear above. The plugin itself ships 20 skills, including bmad-help, bmad-init, bmad-prd, bmad-architecture, bmad-epics-and-stories, bmad-parallel-plan and bmad-handoff, none of which appear as separate skills.sh listings.

## Why This Matters for Hermes Agents

Parallel agent work fails on coordination far more often than on capability. Two agents build against different ideas of the API surface, or two stories touch the same file, and the merge becomes the expensive part. This plugin addresses exactly that layer: one architecture document so the agents share API style, data model, naming and security assumptions, and stories scoped to disjoint files, dependency ordered into waves.

The track mechanism is the useful part for a Hermes agent deciding how much process to run. Quick Flow covers 1 to 15 stories with a tech spec only, BMad Method covers 10 to 50 or more with a PRD and architecture, and Enterprise covers 30 or more with security and DevOps planning added. An agent can size the ceremony to the work instead of applying a fixed template.

The handoff contract is what makes the output portable. A `ready-for-dev` story carries acceptance criteria, source cited dev notes, a testing strategy, tasks, a dependency map and an owned file scope, with the first three marked locked so an implementer must build against them rather than rewrite them. That is a contract a second agent, in any harness, can consume without a conversation.

It also keeps the planning artifacts in the repository. `decision-log.md`, `project-context.md` and the per story files survive the session, so a Hermes agent picking the work up tomorrow reads state rather than reconstructing intent.

## Usage

| You say | What happens |
|---|---|
| "/bmad-planning-orchestrator:bmad-init" | Runs track selection and scaffolds the workspace, decision log and project context |
| "What do I run next?" | bmad-help reads the artifact state and names the next skill, skipping optional phases that are already answered |
| "Write a PRD for this feature set" | bmad-prd produces prd.md, an addendum and decision log entries, with requirements split into functional and non-functional |
| "Break this into stories that two agents can build in parallel" | bmad-epics-and-stories shards into epics and stories with owned file scope, then bmad-parallel-plan builds the dependency DAG and waves |
| "Is this ready to hand to a dev tool?" | bmad-readiness-check returns PASS, CONCERNS or FAIL before any story is marked ready-for-dev |
| "The scope changed, re-plan around it" | bmad-correct-course re-plans from the change without re-writing code |
| "Give me a handoff manifest for the next runner" | bmad-handoff emits handoff-manifest.json with each story's scope, wave and dependencies |

## Verification

Confirm the plugin payload before enabling it, starting with the router skill the whole flow depends on:

```bash
curl -fsSL https://raw.githubusercontent.com/aj-geddes/claude-code-bmad-skills/main/bmad-planning-orchestrator/skills/bmad-help/SKILL.md | head -5
```

It should open with `name: bmad-help`. Then confirm the skill count matches the catalog claim of 20, which is the number the plugin README states:

```bash
git clone --depth 1 https://github.com/aj-geddes/claude-code-bmad-skills.git
ls bmad-planning-orchestrator/skills | wc -l
```

The second command should print 20. Inspect the two things that execute, since they run inside your session:

```bash
cat bmad-planning-orchestrator/hooks/hooks.json
ls bmad-planning-orchestrator/hooks/scripts bmad-planning-orchestrator/scripts
```

After `/reload-plugins`, `/bmad-planning-orchestrator:bmad-help` should respond with the next step for an empty workspace rather than an unknown command error.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| business-analyst | Fail | Pass | Warn |
| product-manager | Pass | Pass | Pass |
| system-architect | Pass | Pass | Pass |
| ux-designer | Pass | Pass | Pass |
| creative-intelligence | Pass | Pass | Warn |

Unlike a markdown-only skill bundle, this plugin executes shell. `hooks/hooks.json` registers a `SessionStart` hook running `hooks/scripts/session-start.sh` and a `Stop` hook running `hooks/scripts/suggest-next.sh`, both with a 5 second timeout, and the plugin ships five more shell scripts under `scripts/` for phase checks, config loading, conflict checks, track selection and status updates. Read those files before enabling the plugin in a session that has repository write access.

The business-analyst listing is the one to look at closely: it is the most installed listing in the repository at 2,233 and it is the only sampled skill that Failed a trust hub verdict.

## Limitations

- Snapshot data, verified 2026-11-05: 5,524 combined installs across 5 indexed listings; 493 GitHub stars; MIT; last pushed 2026-06-19. Counts drift over time.
- The index and the tree disagree. The five listings are BMAD agent role names from the earlier skills suite, and none of them exists as a directory in the current plugin, which ships 20 `bmad-*` skills. Installing from Claude Code gives you the plugin, not the five named skills.
- It plans and orchestrates only. There is no code generation, no test running, no linting and no diff review, and the `developer` skill and `/dev-story` command were removed. A workflow that expects implementation from this plugin will stall at the handoff.
- The install path is Claude Code's plugin marketplace. There is no `npx skills add` route and no standalone SKILL.md bundle, so harnesses outside Claude Code need the files copied manually from `bmad-planning-orchestrator/skills/`.
- This is an independent harness for the BMAD Method, not an official BMAD product. The methodology and the name belong to the BMAD Code Organization, and the MIT license covers only the plugin implementation.
- Hooks and scripts run bash at session start and stop. In a sandboxed or audited environment, budget for reviewing them and for the session overhead.

## Related

- [BMad Method Skills - Agile AI Development Suite Setup](/hermes/skills/catalog/bmad-method-setup)
- [BMAD Labs Skills - Architecture and Delivery Toolkit](/hermes/skills/catalog/bmad-labs-skills-setup)
- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)

## Pro Tips

- Start with bmad-help on an existing repository. It reads what artifacts already exist and skips the phases you have effectively done, which is cheaper than running bmad-init blind.
- Pick the track honestly. Quick Flow with a tech spec is right for a small change, and forcing a PRD on a two story task produces documents nobody reads.
- Read `hooks/hooks.json` once. The stop hook nudges you toward the next step, which is helpful in an interactive session and noise in an automated one.
- Keep `bmad-output/` in version control. The decision log is the cheapest defense against an agent re-litigating a settled choice.
- Treat the `ready-for-dev` story as the interface to your coding agent, not as a prompt to rewrite. The acceptance criteria and dev notes are locked by design.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
