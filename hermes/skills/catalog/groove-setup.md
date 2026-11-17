---
title: "Groove - Compound Engineering Workflow"
description: "andreadellacorte/groove - 24.2K combined installs across 54 indexed listings: compound engineering workflow for AI productivity."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/groove-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "engineering workflow", "task tracking", "memory logs"]
---

# Groove - Setup Guide

**Source:** [andreadellacorte/groove](https://www.skills.sh/andreadellacorte/groove) via skills.sh - 24.2K combined installs across 54 indexed listings; first seen Nov 16, 2026 (Nov 16 evening sweep)
**GitHub:** 6 stars, MIT license, `main` branch, last pushed 2026-07-24, skills under `skills/<name>/SKILL.md` plus companions under `.agents/skills/`
**Category:** Engineering workflow - daily rhythm, task tracking, memory logs, and a compound engineering loop
**Quality Tier:** 🟡 Yellow - of 24 sampled skills, 6 carry a Snyk Warn and 2 carry a Gen Agent Trust Hub Warn on the daily start and end skills; none fail.

Groove packages an engineering cadence into one installable skill set. A single `/groove` router dispatches an intent to the right skill, backed by daily, work, task, memory, and admin handlers plus three companions (`find-skills`, `agent-browser`, `pdf-to-markdown`). Configuration lives in `.groove/index.md` frontmatter, and two hook layers run advisory markdown actions plus deterministic native hooks for Claude Code and Cursor.

The loop is explicit: brainstorm, plan, execute, review, then compound lessons back into rules, templates, and docs. Memory rolls up daily, weekly, and monthly, and `groove-utilities-prime` reloads workflow context, identity, and pending captures at the start of every session.

## Installation

With the skills CLI:

```sh
npx skills add andreadellacorte/groove --all
```

Then bootstrap the backends with `/groove-admin-install`.

Or by hand: copy the skills under `skills/<name>/` (and the companions under `.agents/skills/`) into your agent's skills directory, for example `.claude/skills/`. Copy the whole set; the skills route through the top-level `/groove` entry point.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| groove | 633 | Top-level router that dispatches `/groove` intents to the right skill. |
| groove-utilities-task-analyse | 590 | Analyse task status and distribution across the backend. |
| groove-utilities-memory-install | 587 | Set up the memory backend and configuration. |
| groove-admin-install | 586 | Install backends, companions, and the AGENTS.md bootstrap once per repo. |
| groove-utilities-memory-log-daily | 583 | Write the daily memory log entry at end of day. |
| groove-utilities-task-install | 582 | Set up the task backend and configuration. |
| groove-admin-config | 581 | Create or update `.groove/index.md` config interactively. |
| groove-utilities-task-list | 579 | List active tasks in the configured backend. |
| groove-daily-start | 573 | Start the day: review yesterday, create daily memory, load tasks. |
| groove-admin-doctor | 573 | Run all health checks: config, backends, companions, AGENTS.md. |
| groove-daily-end | 559 | End the day: write memory, analyse tasks, run the end hook. |
| groove-utilities-memory-doctor | 555 | Check memory backend health and configuration. |
| groove-work-brainstorm | 552 | Clarify scope through dialogue and surface open questions. |
| groove-utilities-task-doctor | 552 | Check task backend health and connectivity. |
| groove-work-review | 546 | Evaluate output, identify lessons, decide accept or rework. |
| groove-work-plan | 546 | Research the codebase and write a concrete plan. |
| groove-utilities-task-update | 546 | Update an existing task in the backend. |
| groove-utilities-memory-log-weekly | 545 | Roll up the weekly memory log from daily entries. |
| groove-admin-help | 544 | Show all skills and commands with live config values. |
| groove-work-spec | 543 | Create an outcome spec: overview, decisions, steps, edge cases. |
| groove-utilities-task-create | 543 | Create a new task in the backend. |
| groove-work-compound | 541 | Document lessons and update rules, templates, and docs. |
| groove-work-audit | 541 | Review the branch for blindspots: fix now, needs spec, create issues. |
| groove-utilities-prime | 540 | Load groove workflow context into the conversation. |
| groove-utilities-memory-log-git | 539 | Record git activity in memory. |
| groove-utilities-memory-log-monthly | 538 | Roll up the monthly memory log from weekly entries. |
| groove-utilities-check | 538 | Check whether a newer groove version is available. |
| groove-work-exec | 537 | Execute the plan. |
| groove-utilities-task-config | 534 | Configure the task backend. |
| groove-utilities-task-archive | 533 | Archive a completed task. |
| groove-admin-claude-hooks | 531 | Install Claude Code native shell hooks into `.claude/settings.json`. |
| groove-utilities-memory-mistakes | 530 | Log and resolve workflow mistakes. |
| groove-admin-update | 529 | Pull the latest version and apply migrations. |
| groove-work-doc | 519 | Document how a component works. |
| groove-utilities-memory-promises | 519 | Capture and resolve deferred items. |
| groove-admin-cursor-hooks | 519 | Install Cursor native hooks into `.cursor/hooks.json`. |
| groove-utilities-memory-retrospective | 517 | Analyse ratings, mistakes, and learnings. |
| groove-utilities-memory-graduate | 511 | Promote a stable lesson to AGENTS.md permanently. |
| groove-groovebook-review | 508 | Browse and review open Groovebook learning PRs. |
| groove-groovebook-publish | 507 | Publish a workflow learning to the shared commons. |
| groove-utilities-onboard | 506 | Generate a GROOVE.md contributor onboarding guide. |
| groove-admin-claude-statusline | 502 | Wire groove state into the Claude Code statusline. |

The remaining 12 indexed listings range from 1 to 293 installs.

## Why This Matters for Hermes Agents

Groove gives a Hermes agent a daily rhythm and a compound-engineering loop instead of ad hoc sessions. The `/groove` router means the agent does not need to memorise command names; it types an intent and the top-level skill routes to a daily, work, task, memory, or admin handler. The compound loop is explicit: brainstorm, plan, execute, review, then fold lessons back into rules, templates, and docs. Memory is a first-class citizen with daily, weekly, and monthly roll-ups plus git activity capture, so context survives across sessions. The prime skill reloads workflow context, identity, and pending captures at the start of every session, which is exactly what a long-running agent needs after compaction. Deterministic native hooks run outside the model for version checks, daily-end reminders, and git commit capture, so the loop does not depend on the model remembering. Health is scripted through doctor skills for config, backends, and companions, so failures surface as a checklist rather than a silent break. For a builder, this is a ready-made operating cadence to bolt onto a coding agent.

## Usage

| You say | What happens |
|---|---|
| `/groove start my day` | Routes to groove-daily-start, which reviews yesterday, creates today's memory, and loads tasks. |
| `/groove plan the auth refactor` | Routes to groove-work-plan after brainstorming, researching the codebase and writing a plan. |
| `/groove-utilities-task-list` | Lists active tasks in the configured backend. |
| `/groove-utilities-memory-log-daily` | Writes the daily memory log entry for the work done. |
| `/groove-work-review` | Evaluates output, identifies lessons, and decides accept or rework. |
| `/groove-admin-doctor` | Runs all health checks across config, backends, companions, and AGENTS.md. |
| `/groove-utilities-prime` | Loads groove workflow context into the conversation at session start. |

## Verification

Check the skill files before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/andreadellacorte/groove/main/skills/groove/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/andreadellacorte/groove/main/skills/groove-admin-doctor/SKILL.md | head -20
npx skills add andreadellacorte/groove --all
```

Each skill is one `SKILL.md` under `skills/<name>/`; confirm the path exists in the current tree before copying a specific skill.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| groove | Pass | Pass | Pass |
| groove-utilities-task-analyse | Pass | Pass | Warn |
| groove-utilities-memory-install | Pass | Pass | Pass |
| groove-admin-install | Pass | Pass | Warn |
| groove-utilities-memory-log-daily | Pass | Pass | Pass |
| groove-utilities-task-install | Pass | Pass | Warn |
| groove-admin-config | Pass | Pass | Pass |
| groove-utilities-task-list | Pass | Pass | Warn |
| groove-daily-start | Warn | Pass | Pass |
| groove-admin-doctor | Pass | Pass | Pass |
| groove-daily-end | Warn | Pass | Pass |
| groove-utilities-memory-doctor | Pass | Pass | Pass |
| groove-work-brainstorm | Pass | Pass | Pass |
| groove-utilities-task-doctor | Pass | Pass | Warn |
| groove-work-review | Pass | Pass | Pass |
| groove-work-plan | Pass | Pass | Pass |
| groove-utilities-task-update | Pass | Pass | Warn |
| groove-utilities-memory-log-weekly | Pass | Pass | Pass |
| groove-admin-help | Pass | Pass | Pass |
| groove-work-spec | Pass | Pass | Pass |
| groove-utilities-task-create | Pass | Pass | Pass |
| groove-work-compound | Pass | Pass | Pass |
| groove-work-audit | Pass | Pass | Pass |
| groove-utilities-prime | Pass | Pass | Pass |

Of 24 sampled skills, 16 pass all three scanners, 6 carry a Snyk Warn, and 2 carry a Gen Agent Trust Hub Warn on the daily start and end skills; none fail.

## Limitations

- Snapshot data, verified Nov 16, 2026: 24,171 combined installs across 54 indexed listings; 6 GitHub stars; MIT; last pushed 2026-07-24. Counts drift over time.
- Groove targets Claude Code and Cursor; session bootstrap and deterministic behaviour rely on native platform hooks those two platforms support.
- 12 of the 54 indexed listings sit under 300 installs, including the companions (pdf-to-markdown, agent-browser, find-skills), groove-utilities-stats, and several short-name aliases.
- The repository has 6 GitHub stars at snapshot, so the workflow carries less community vetting than larger catalogs.
- Memory paths (`.groove/memory/`) and specs paths are hardcoded, not configurable.

## Related

- [Context Engineering Kit](/hermes/skills/catalog/context-engineering-kit-setup)
- [Obra Superpowers](/hermes/skills/catalog/obra-superpowers-setup)
- [Plannotator](/hermes/skills/catalog/plannotator-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install with the full set so the companions (find-skills, agent-browser, pdf-to-markdown) land too.
- Create a `.groove/IDENTITY.md` with mission, goals, and active projects; groove-utilities-prime injects it into every session.
- Run `/groove-admin-doctor` after setup to confirm config, backends, and companions are healthy.
- Use `/groove-utilities-memory-graduate` to promote a stable lesson into AGENTS.md so it survives the session.
- Keep the whole set together; the skills route through the `/groove` entry point and a partial install loses the router.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
