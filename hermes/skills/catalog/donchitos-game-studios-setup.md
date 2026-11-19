---
title: "Claude Code Game Studios - Game Dev Agent Suite Setup"
description: "donchitos/claude-code-game-studios: 49.8K combined installs across 79 listings; a game dev studio that turns Claude Code into a game-making workflow."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/donchitos-game-studios-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "game development", "claude code", "game design"]
---

# Claude Code Game Studios - Setup Guide

**Source:** [donchitos/claude-code-game-studios](https://www.skills.sh/donchitos/claude-code-game-studios) via skills.sh - 49.8K combined installs across 79 indexed listings; first seen Nov 18, 2026 (Nov 18, 2026 evening sweep)
**GitHub:** 40,093 stars, MIT licence, `main` branch, last pushed 2026-11-09. Skills are one `SKILL.md` per directory under `.claude/skills/`, with 49 studio agents under `.claude/agents/` and supporting hooks, rules, and docs under `.claude/`.
**Category:** Game development and studio workflow
**Quality Tier:** 🟡 Yellow - 2 Warns among 12 sampled verdicts (brainstorm, design-review); MIT licence.

Claude Code Game Studios turns Claude Code into a game development studio. Describe a game, answer a few questions, and it writes a one-page brief and builds a playable browser game, then grows and finishes it one step at a time. The repo mirrors a real studio hierarchy: 49 agent roles spanning creative direction, production, programming, and engine specialism, coordinated by workflow skills, hooks, and rules.

The skills.sh index carries 79 skill listings covering concept work, design documents, prototyping, QA, sprint and release process, and engine setup for web, Godot, Unity, and Unreal. Installation is a clone-and-open flow rather than a one-line installer: you clone the template, open Claude Code in the project root, and start with `/start` or `/prototype`.

## Installation

The README's setup is a clone-and-open flow. The repository is a Claude Code project template:

```bash
git clone https://github.com/Donchitos/Claude-Code-Game-Studios.git my-game
cd my-game
claude
```

Open Claude Code in the project root (the folder holding `CLAUDE.md` and `project.yaml`), then run `/start`, which asks where you are and routes you to the right workflow, or jump straight in with `/prototype` and your game idea. `/setup-engine godot 4.7` configures an engine if you already know you want one. Each skill is a plain `SKILL.md` under `.claude/skills/`, so a harness that loads skill files can use them directly even though the end-to-end flow targets Claude Code.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| balance-check | 1,062 | Find balance outliers, broken progressions, degenerate strategies, and economy imbalances in formulas and data. |
| playtest-report | 857 | Turn playtest notes into a structured playtest report, or fill the report template with reproduction steps and severity. |
| brainstorm | 827 | Guide the user toward a game concept, from a game jam idea to dropping the current idea and starting over. |
| art-bible | 808 | Author the Art Bible that sets visual identity and gates asset production, run before map-systems. |
| team-narrative | 774 | Orchestrate the narrative team for story, world lore, and narrative-driven levels. |
| design-review | 771 | Review one design document for completeness, internal consistency, implementability, and design standards. |
| design-system | 727 | Section-by-section game design document authoring for one system, cross-referencing dependencies. |
| ux-review | 718 | Validate a UX spec, HUD design, or pattern library for accessibility, GDD alignment, and readiness. |
| map-systems | 710 | Decompose a concept into systems, map dependencies, prioritize design order, and create the systems index. |
| estimate | 702 | Estimate task effort from complexity, dependencies, velocity, and risk with confidence levels. |
| scope-check | 700 | Check current scope against the original plan, flag additions, quantify bloat, and recommend cuts. |
| bug-report | 699 | Write a structured bug report from a description, or analyze code for potential bugs with reproduction steps. |
| asset-audit | 699 | Audit assets against naming conventions, file size budgets, and format standards, finding orphaned assets and missing references. |
| team-ui | 694 | Orchestrate the UI team through authoring, visual design, implementation, review, and polish using ux-design and ux-review. |

The remaining 65 indexed listings range from 3 to 689 installs.

## Why This Matters for Hermes Agents

For an agent that builds games, the default failure mode is plausible output that is not actually playable or not actually what the user asked for. These skills replace that with a staged studio process: concept, brief, prototype, grow, and finish, with checks between stages. The director gates and review skills such as design-review, scope-check, and consistency-check act as validation steps that catch drift before code ships.

The skills are plain SKILL.md files with structured references, so a harness that loads skill files, including Hermes, can adopt the review and estimation skills directly even though the end-to-end studio flow assumes Claude Code hooks and agents. The design and QA skills name real standards, such as a design document's required sections and explicit balance and scope checks, rather than a model's defaults.

## Usage

| You say | What happens |
|---|---|
| "/prototype a fishing game where the rare fish only bite at dusk" | A few questions, then a one-page brief and a first playable browser build, checked in a headless browser before handover. |
| "/start" | The skill asks where you are and routes you to the right workflow: make me a game, an idea, clear design, or existing work. |
| "Check my game for scope creep" | scope-check flags additions against the original plan, quantifies bloat, and recommends cuts. |
| "Turn these playtest notes into a report" | playtest-report converts the notes into a structured report with reproduction steps and severity. |
| "Review my design doc before the programmers get it" | design-review checks completeness, consistency, implementability, and design standards. |
| "/setup-engine godot 4.7" | setup-engine pins the engine version and writes the Godot reference docs into the project. |
| "Audit our assets" | asset-audit checks naming conventions, file size budgets, and formats, and finds orphaned assets and missing references. |

## Verification

Probe one skill on the `main` branch before cloning. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/Donchitos/Claude-Code-Game-Studios/main/.claude/skills/balance-check/SKILL.md
```

Then clone and open:

```bash
git clone https://github.com/Donchitos/Claude-Code-Game-Studios.git my-game
cd my-game
claude
```

Run `/start`, then confirm the skills appear in the agent's skills directory under `.claude/skills/`.

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| balance-check | Pass | Pass | Pass |
| playtest-report | Pass | Pass | Pass |
| brainstorm | Pass | Pass | Warn |
| art-bible | Pass | Pass | Pass |
| team-narrative | Pass | Pass | Pass |
| design-review | Warn | Pass | Pass |
| design-system | Pass | Pass | Pass |
| ux-review | Pass | Pass | Pass |
| map-systems | Pass | Pass | Pass |
| estimate | Pass | Pass | Pass |
| scope-check | Pass | Pass | Pass |
| bug-report | Pass | Pass | Pass |

The sample covers 12 of the 79 indexed listings; brainstorm carries a Snyk Warn and design-review a Gen Agent Trust Hub Warn, and every other cell passes.

## Limitations

- Snapshot data, verified Nov 18, 2026: 49,825 combined installs across 79 indexed listings; 40,093 GitHub stars; MIT licence; last pushed 2026-11-09. Counts drift over time.
- Installation is a clone-and-open flow, not a one-line installer: you clone the template and open Claude Code in the project root, and the skills live as SKILL.md files under .claude/skills/.
- The README describes 75 workflow skills while the skills.sh index carries 79 listings, so a few indexed listings do not map one-to-one to the README's workflow count.
- The set is Claude-Code-centric: agents, hooks, and rules assume Claude Code, and Python 3 plus Bash are required for hooks and project.yaml parsing.
- Engine work (Godot, Unity, Unreal) and the one-shot web prototypes are built and pass the framework's own checks, but are not yet validated by the same kind of comparison test the browser-game workflow received.

## Related

- [Awesome GameDev Skills - 77 Game Engine Agent Suite](/hermes/skills/catalog/awesome-gamedev-agent-skills-setup)
- [Unreal Engine Skills - Game Dev Suite for Agents](/hermes/skills/catalog/unreal-engine-skills-setup)
- [Unity AI Skills - Official Unity 29-Skill Game Dev Suite Setup](/hermes/skills/catalog/unity-ai-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with /start rather than /prototype if you are unsure which workflow fits; it routes you and writes project.yaml.
- Keep rigor at minimal until the project outgrows it; /next-step and /gate-check suggest raising it when the signs appear.
- Run scope-check and design-review before handing a design document to programmers.
- Copy a single SKILL.md (for example .claude/skills/balance-check/SKILL.md) into your harness if you only want one skill.
- Hooks need Bash and Python 3; without them validation silently falls back to defaults.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
