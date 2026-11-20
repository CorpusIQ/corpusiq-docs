---
title: "Agile Delivery Skills - Sprint Planning and Delivery Setup"
description: "Setup guide for djalmajr/skills: 3.3K combined installs across 61 listings; agile delivery management from intake to sprint planning and TDD."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/djalmajr-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "agile", "project management", "tdd"]
---

# Agile Delivery Skills - Setup Guide

**Source:** [djalmajr/skills](https://www.skills.sh/djalmajr/skills) via skills.sh - 3.3K combined installs across 61 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 evening sweep)
**GitHub:** 4 stars, no LICENSE file, `main` branch, last pushed 2026-11-19. Twenty-one skills under `skills/` (the README documents 14 agile skills plus design, media, planning, and UX), each a SKILL.md with `templates/` or `references/`; docs, samples, a presentation directory, and a validation script sit alongside.
**Category:** Agile delivery management for AI agents
**Quality Tier:** 🟠 Orange - no LICENSE file; 1 Fail and 2 Warn among the 16 sampled skills.sh verdicts (aim-init fails the Gen Agent Trust Hub).

djalmajr/skills is an agile delivery management suite for AI agents. It covers the full delivery loop: intake, roadmap, epic, story, sprint, status, review, and retrospective, with TDD, prototyping, and onboarding alongside. Around the agile core sit design workflow, Excalidraw diagramming, UX flow and persona skills, audio and video creation, and a goal-planning skill.

The suite defines an explicit flow, intake to roadmap to epic to story to execution to status to retrospective, with refinement checking planning artifacts and code at each handoff. An agile-router skill points to the right agile skill when context is ambiguous. The skills follow the shared Agent Skills convention and target Claude Code, OpenCode, and Codex. The install index is much wider than the repository tree: 61 indexed listings against 21 in-tree skill directories, so many listed names are older or external.

## Installation

`bunx` is preferred in this environment; `npx` also works. Install all skills, specific skills, or explicit target agents:

```bash
# All skills
bunx skills add djalmajr/skills --skill '*'

# Specific skills
bunx skills add djalmajr/skills --skill agile-epic --skill agile-story

# Explicit target agents
bunx skills add djalmajr/skills --agent claude-code --agent opencode --agent codex --skill '*'
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| agile-sprint | 129 | Plan a sprint by selecting items from the backlog, defining the objective, capacity, and execution order. |
| agile-review | 128 | Prepare the sprint review and demo of deliveries for stakeholders, including the sprint's quantitative metrics. |
| agile-tdd | 122 | Guide the TDD workflow, testing strategy, and the project's VALIDATION.md contract; triggers on "TDD" and "red-green-refactor". |
| agile-proto | 120 | Create static, browser-based UI prototypes with a zero-build stack (z-proto, HTM UI, Tailwind v4, Preact/htm, preact-iso). |
| agile-metrics | 118 | Listed on skills.sh with no directory in the current tree, so its behavior is not documented in the repository. |
| agile-retro | 115 | Conduct a retrospective with learnings and improvement actions at the end of a cycle, sprint, or delivery. |
| agile-epic | 115 | Structure large initiatives into a decomposed backlog with roadmap, dependencies, and verification, plus story files with tasks. |
| agile-router | 114 | Route to the right agile skill based on context: planning, ceremonies, tracking, prototypes, TDD, or onboarding. |
| agile-roadmap | 114 | Map multi-phase trajectories with dependencies into clear, sequenced roadmaps for any duration. |
| agile-onboarding | 114 | Onboard new team members to how planning, execution, and tracking work with AI agents in the agile flow. |
| agile-story | 113 | Create an execution plan with tasks for a single story or a localized standalone change. |
| agile-status | 110 | Track delivery progress in three modes: checkpoint (daily), consolidation (period report), and closure (post-implementation). |
| agile-refinement | 109 | Validate planning artifacts and review code for quality, consistency, and completeness. |
| agile-intake | 109 | Structure new and vague problems into clear intake documents before they reach the backlog. |
| agile-skill-feedback | 98 | Listed on skills.sh with no directory in the current tree, so its behavior is not documented in the repository. |
| aim-init | 89 | Listed on skills.sh with no directory in the current tree, so its behavior is not documented in the repository. |
| aim-write | 73 | Listed on skills.sh with no directory in the current tree, so its behavior is not documented in the repository. |
| aim-query | 72 | Listed on skills.sh with no directory in the current tree, so its behavior is not documented in the repository. |

The remaining 43 indexed listings range from 1 to 69 installs.

## Why This Matters for Hermes Agents

An agent that jumps straight from a request to an edit skips the planning that keeps a delivery coherent. This suite forces the opposite: intake captures the vague problem, roadmap sequences phases, epic decomposes into stories, story details each task, and refinement validates the artifacts and the code before and after each step. Following the flow keeps a Hermes agent's work traceable from idea to delivered increment.

The ceremony skills make the loop measurable. agile-status records checkpoints, consolidations, and closures; agile-review prepares the stakeholder demo with quantitative metrics; agile-retro converts what worked and what did not into improvement actions. An agent that can run these ceremonies produces not just code but a governed delivery record.

agile-tdd and agile-proto round out the practical ends: TDD ties each change to a validation contract, and the zero-build prototype stack turns an idea into a clickable browser mockup without a backend or build pipeline. Together they cover the two highest-leverage feedback loops in delivery: proving the code works and proving the concept is worth building.

## Usage

| You say | What happens |
|---|---|
| "Turn this vague idea into a plan" | agile-intake structures the problem into an intake document before it reaches the backlog. |
| "Break this initiative into stories with dependencies" | agile-epic produces a roadmap plus individual story files with tasks and verification. |
| "Plan this sprint from the backlog" | agile-sprint selects items, defines the objective and capacity, and orders execution. |
| "Implement this feature with tests" | agile-tdd guides red-green-refactor and the project's VALIDATION.md contract. |
| "Build a clickable prototype for the demo" | agile-proto creates a static, zero-build browser prototype with HTM UI and Tailwind. |
| "Which agile skill should I use here?" | agile-router points to the right skill for planning, ceremonies, tracking, prototypes, or TDD. |
| "Run our sprint retrospective" | agile-retro captures learnings and produces improvement actions for the next cycle. |

## Verification

Confirm skills landed in the agent skills directory after install, and probe one SKILL.md on the `main` branch before reviewing (returns 200):

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/djalmajr/skills/main/skills/agile-epic/SKILL.md
```

Claude Code loads installed skills from `.claude/skills/<name>/SKILL.md` or `~/.claude/skills/<name>/SKILL.md`; OpenCode reads `.opencode/skills`, `.claude/skills`, or `.agents/skills`.

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

One of the 16 sampled skills carries a Fail cell (aim-init on the Gen Agent Trust Hub), and agile-proto carries Socket and Snyk Warn cells, so review those pages before relying on the skills in production.

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| agile-sprint | Pass | Pass | Pass |
| agile-review | Pass | Pass | Pass |
| agile-tdd | Pass | Pass | Pass |
| agile-proto | Pass | Warn | Warn |
| agile-metrics | Pass | Pass | Pass |
| agile-retro | Pass | Pass | Pass |
| agile-epic | Pass | Pass | Pass |
| agile-router | Pass | Pass | Pass |
| agile-roadmap | Pass | Pass | Pass |
| agile-onboarding | Pass | Pass | Pass |
| agile-story | Pass | Pass | Pass |
| agile-status | Pass | Pass | Pass |
| agile-refinement | Pass | Pass | Pass |
| agile-intake | Pass | Pass | Pass |
| agile-skill-feedback | Pass | Pass | Pass |
| aim-init | Fail | Pass | Pass |

The sample covers 16 of the 61 indexed listings; the remaining listings carry no published verdict in this snapshot.

## Limitations

- Snapshot data, verified Nov 19, 2026: 3,298 combined installs across 61 indexed listings; 4 GitHub stars; no LICENSE file; last pushed 2026-11-19. Counts drift over time.
- There is no LICENSE file, so treat the repository as all-rights-reserved rather than open source until terms are confirmed with the owner.
- The install index outruns the tree: 61 indexed listings against 21 in-tree skill directories, so most listed names have no SKILL.md in the repository (notably agile-metrics, agile-skill-feedback, aim-init, aim-write, and aim-query among the higher-install rows).
- Many indexed names (work-*, wiki-*, aim-*, figma-capture, shadcn, minions, and others) are not part of the shipped 21-skill package.
- The herdr-agents listing points to a skill moved to djalmajr/herdr-soho; install that package separately rather than from this repository.
- One sampled verdict carries a Fail cell (aim-init on the Gen Agent Trust Hub), so review that skill before production use.

## Related

- [Planning With Files - Agent Planning Methodology Setup](/hermes/skills/catalog/planning-with-files-setup)
- [Linear Integration - Issue & Project Management Setup](/hermes/skills/catalog/linear-setup)
- [PM Skills - Product Management Lifecycle Suite Setup](/hermes/skills/catalog/pm-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `/agile-router` when unsure which skill fits; it knows the agile-* family and routes by context.
- Follow the flow (intake to roadmap to epic to story) and let refinement check artifacts and code at each handoff.
- Keep templates self-contained: each skill references its own `templates/` with relative paths, never global locations.
- Use `bunx skills add djalmajr/skills --agent claude-code --agent opencode --agent codex --skill '*'` to target all three agents at once.
- Install herdr-soho from djalmajr/herdr-soho instead of the old herdr-agents listing.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
