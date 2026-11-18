---
title: "Specsfy Skills - Spec-Driven Development Suite Setup"
description: "promovaweb/specsfy: 21.2K combined installs across 66 listings; a spec-driven development suite that turns an idea into tested software."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/specsfy-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "spec-driven development", "requirements", "cli"]
---

# Specsfy Skills - Setup Guide

**Source:** [promovaweb/specsfy](https://www.skills.sh/promovaweb/specsfy) via skills.sh - 21.2K combined installs across 66 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 90 stars, AGPL-3.0 license, `main` branch, last pushed 2026-11-16. The numbered pipeline skills live in `skills/`, the per-stack specialists in `specialists/`, with a published copy under `example/.agents/skills/`.
**Category:** Spec-driven development / requirements to tested software
**Quality Tier:** 🟡 Yellow - 52 Pass and 8 Warn across the 20 sampled listings; no Fail. AGPL-3.0 copyleft licence.

Specsfy is a Brazilian project from Promovaweb. Its README and skill descriptions are written in Portuguese, and this guide translates them. It is an executable methodology for turning an idea into tested software from a single specification: you talk to the agent, and the skills organize requirements, tests, and tasks into one spec file, with each step producing a checkable result before the next runs.

The suite splits into a numbered pipeline (inbox, backlog, specify, validate, tasks, tdd-bdd, implement, plus setup, progress, and documentation helpers) and per-stack specialists for data modeling, software architecture, domain modeling, and UI work. A companion CLI, `specsfy`, installs the skills into a project, checks its state, and drives gates from the terminal or CI.

## Installation

The README requires Node.js 22.20 or newer plus npm, then installs the CLI:

```bash
npm install --global @promovaweb/specsfy
specsfy --version
```

On first run, npm downloads and verifies the platform binary. To install without npm, fetch the Node.js launcher from `get.specsfy.dev`, which does the same download on first run:

```bash
mkdir -p "$HOME/.local/bin"
curl -fL get.specsfy.dev -o "$HOME/.local/bin/specsfy"
chmod +x "$HOME/.local/bin/specsfy"
```

Then install the skills into a project:

```bash
cd path/to/project
specsfy doctor --project .
specsfy install --project .
specsfy skills list
specsfy progress --project .
```

`doctor` checks the runtime, terminal, config, Git, the skills CLI, and the project GitHub token. `install` publishes the base skills into `.agents/skills/`, writes `.specsfy/Spec.md`, and reconciles the managed blocks in `AGENTS.md` and `CLAUDE.md`. To update, `specsfy upgrade` replaces the binary and `specsfy update --project .` updates skills, templates, and managed blocks.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| specsfy-aux-stack | 1,151 | Build or update .specsfy/STACK.md additively from manifests, lockfiles, and config, tracking framework, language, runtime, test tooling, and persistence. |
| specsfy-specialist-data-modeling | 570 | Model data, entities, relationships, lifecycles, quality, and persistent contracts before implementing changes. |
| specsfy-specialist-software-architecture | 553 | Analyze and evolve architecture: boundaries, dependency direction, quality attributes, ADRs, migration, and trade-offs. |
| specsfy-specialist-domain-modeling | 540 | Discover and refine domain language, invariants, events, aggregates, and bounded contexts from concrete scenarios. |
| specsfy-specialist-reui | 525 | Build React and Tailwind CSS interfaces with the free ReUI components. |
| specsfy-specialist-shadcn-ui | 502 | Install, compose, and adapt shadcn/ui with registry, Radix, theming, forms, tables, charts, and sidebars. |
| specsfy-setup | 485 | Prepare and reconcile persistent project context (PROJECT.md, STACK, RULES, DATABASE, USER-PROFILE), install detected specialists, and preserve GitHub Spec Kit projects. |

The remaining 59 indexed listings range from 15 to 479 installs.

## Why This Matters for Hermes Agents

The core idea is a single normative spec file that carries requirements, tasks, tests, and gate records, so an agent never scatters project state across many files. Each pipeline skill owns one transition (capture, backlog, specify, validate, tasks, tdd-bdd, implement), and each gate must pass before the next transition runs.

The CLI exposes the same state to scripts and CI with read-only commands such as `specsfy progress --project . --json` and `specsfy gate spec 0001`, so a build can enforce the same gates an agent would. If you already run GitHub Spec Kit, `$specsfy-setup` reads the constitution and specs and publishes a read bridge in `.specsfy/SPECKIT.md` rather than migrating your artifacts.

Specialists install per stack and only after you confirm, so an agent recommendation does not silently pull in domain experts for stacks you are not using.

## Usage

| You say | What happens |
|---|---|
| "Use $specsfy-setup to prepare this project" | Reads the project, records the interaction profile in .specsfy/USER-PROFILE.md, and installs detected specialists. |
| "Use $specsfy-01-inbox to capture: create a welcome page" | Saves the capture into specs/inbox/ as a timestamped file with no questions asked. |
| "specsfy doctor --project ." | Checks the runtime, terminal, config, Git, the skills CLI, and the GitHub token. |
| "specsfy progress --project . --watch" | Projects specs, gates, tasks, and checklists without editing the spec. |
| "specsfy gate spec 0001" | Approves the spec gate (exit 0) or rejects it (exit 10). |
| "specsfy skills install specsfy-specialist-laravel --project ." | Installs the Laravel specialist after you confirm the install. |

## Verification

Probe two skills on the `main` branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/promovaweb/specsfy/main/skills/specsfy-setup/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/promovaweb/specsfy/main/skills/specsfy-aux-stack/SKILL.md
```

Then confirm the CLI installed and see the base skills:

```bash
specsfy --version
specsfy skills list
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| specsfy-aux-stack | Pass | Pass | Pass |
| specsfy-specialist-data-modeling | Pass | Pass | Pass |
| specsfy-specialist-software-architecture | Pass | Pass | Pass |
| specsfy-specialist-domain-modeling | Pass | Pass | Pass |
| specsfy-specialist-reui | Pass | Pass | Warn |
| specsfy-specialist-shadcn-ui | Pass | Pass | Warn |
| specsfy-setup | Pass | Pass | Warn |
| specsfy-03-specify | Pass | Pass | Warn |
| specsfy-roadmap-milestone-interviewer | Pass | Pass | Pass |
| specsfy-interviewer | Pass | Pass | Pass |
| specsfy-milestone-governor | Pass | Pass | Pass |
| specsfy-07-implement | Pass | Pass | Warn |
| specsfy-05-tasks | Warn | Pass | Pass |
| specsfy-01-inbox | Pass | Pass | Pass |
| specsfy-06-tdd-bdd | Pass | Pass | Pass |
| specsfy-04-validate | Pass | Pass | Warn |
| specsfy-02-backlog | Pass | Pass | Warn |
| specsfy-mvp-milestone-interviewer | Pass | Pass | Pass |
| specsfy-progress | Pass | Pass | Pass |
| specsfy-documentator | Pass | Pass | Pass |

The sample covers 20 of the 66 indexed listings; the eight Warn cells are one Gen Agent Trust Hub flag (specsfy-05-tasks) and seven Snyk flags. No Fail.

## Limitations

- Snapshot data, verified 2026-11-17: 21,220 combined installs across 66 indexed listings; 90 GitHub stars; AGPL-3.0; last pushed 2026-11-16. Counts drift over time.
- The README and skill descriptions are written in Portuguese; this guide translates them. Working in the repository itself means reading Portuguese SKILL.md files and docs.
- The repository is licensed AGPL-3.0, a copyleft license; review its obligations before using the skills in closed or hosted deployments. The license does not grant use of the Specsfy or Promovaweb name and logo.
- The seven skills shown above carry most of the install volume; the other 59 indexed listings sit between 15 and 479 installs and are long-tail.
- Installing the skills requires the `specsfy` CLI, so a Node.js 22.20 or newer toolchain is a prerequisite even though the compiled binary itself has no Node dependency.

## Related

- [Spec Kit Skills - Specify, Plan, Implement](/hermes/skills/catalog/speckit-agent-skills-setup)
- [OpenSpec Skills - Spec-Driven Development Suite Setup](/hermes/skills/catalog/fission-openspec-skills-setup)
- [Warp Common Skills - Spec-Driven Development Workflow Setup](/hermes/skills/catalog/warpdotdev-common-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start every spec with `$specsfy-setup`, then capture with `$specsfy-01-inbox`; the setup skill reads the project before asking and records USER-PROFILE.md.
- Run `specsfy doctor --project .` before `install`; it catches Git and GitHub-token problems that would otherwise surface mid-spec.
- Prefer `specsfy progress --project . --json` for scripts and CI; it is read-only and never edits the spec.
- Install specialists only when you confirm them; an agent recommendation does not install a specialist on its own.
- For GitHub Spec Kit projects, let `$specsfy-setup` publish the read bridge instead of migrating artifacts by hand.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
