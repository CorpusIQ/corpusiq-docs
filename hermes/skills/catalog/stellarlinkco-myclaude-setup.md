---
title: "Stellarlink MyClaude - Multi-Agent Orchestration Setup"
description: "stellarlinkco/myclaude: 4.0K combined installs across 13 listings; multi-agent orchestration across Claude Code, Codex, Gemini, and OpenCode backends."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/stellarlinkco-myclaude-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "multi-agent", "orchestration", "workflow"]
---

# Stellarlink MyClaude - Setup Guide

**Source:** [stellarlinkco/myclaude](https://www.skills.sh/stellarlinkco/myclaude) via skills.sh - 4.0K combined installs across 13 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 morning sweep)
**GitHub:** 2,751 stars, AGPL-3.0 licence, `master` branch, last pushed 2026-05-04. Eleven skills under `skills/`, plus agents and commands under `agents/`, a Go codeagent-wrapper, and an interactive installer.
**Category:** Multi-agent orchestration
**Quality Tier:** 🟠 Orange - 1 Fail among 13 sampled skills (do); AGPL-3.0 licence.

Stellarlink MyClaude is a multi-agent orchestration system for Claude Code that runs work across Codex, Claude, Gemini, and OpenCode backends through a Go codeagent-wrapper. Claude Code orchestrates; the wrapper executes code edits and tests in parallel, with worktree isolation and structured output. Modules wrap the workflows: `/do` for five-phase feature development, `/omo` for multi-agent bug investigation, `/bmad-pilot` for the BMAD agile workflow, and `/sparv` for the Specify-Plan-Act-Review-Vault loop.

The install index reports 13 listings against 11 `skills/` directories: `codex` and `gemini` are listed as installable skills (direct Codex and Gemini backend execution) but have no `skills/<name>/SKILL.md` directory in the current tree.

## Installation

Run the interactive installer via npx:

```bash
npx github:stellarlinkco/myclaude
```

List installable items, update, or target a custom directory:

```bash
npx github:stellarlinkco/myclaude --list
npx github:stellarlinkco/myclaude --update
npx github:stellarlinkco/myclaude --install-dir ~/.claude --force
```

After install, `~/.claude/` holds the wrapper binary, commands, agents, skills, and hooks; edit `config.json` to enable or disable modules. The default feature-development workflow is `/do`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| product-requirements | 1,279 | Interactive Product Owner skill: requirements gathering, analysis, and PRD generation with quality scoring and iterative dialogue. |
| test-cases | 1,259 | Generate comprehensive test cases from PRDs or requirements: functional, edge case, error handling, and state transition scenarios. |
| prototype-prompt-generator | 365 | Generate structured prompts for UI/UX prototypes across design systems (WeChat Work, iOS Native, Material Design, Ant Design Mobile). |
| skill-install | 200 | Install Claude skills from GitHub with automated security scanning. |
| codeagent | 193 | Execute codeagent-wrapper for multi-backend AI code tasks with agent presets, skill injection, worktree isolation, and parallel execution. |
| browser | 183 | Browser automation via Chrome DevTools Protocol: launch, navigate, run JavaScript, screenshot, and select DOM elements with no MCP server. |
| harness | 135 | Multi-session autonomous work with progress checkpointing, failure recovery, and task dependency management. |
| omo | 75 | Multi-agent orchestration for code analysis, bug investigation, fix planning, and implementation with a minimal agent set. |
| dev | 74 | Lightweight end-to-end development workflow with requirements clarification and parallel codeagent execution. |
| do | 73 | Structured feature development: a five-phase Understand, Clarify, Design, Implement, Complete loop via codeagent-wrapper. |
| sparv | 71 | Minimal SPARV workflow (Specify, Plan, Act, Review, Vault) with a 10-point spec gate and EHRB risk detection. |
| codex | 37 | Direct Codex backend execution. |

The remaining 1 indexed listing is gemini (28 installs), direct Gemini backend execution.

## Why This Matters for Hermes Agents

The pattern worth borrowing is the split between orchestration and execution. Claude Code plans, gathers context, and verifies, while the codeagent-wrapper runs the actual edits and tests across Codex, Claude, Gemini, and OpenCode with worktree isolation and parallel execution. That separation lets one harness drive several backend CLIs through a single wrapper interface.

The `harness` skill generalizes the same idea: checkpointing, failure recovery, and task-dependency management for long-running, multi-session work. For a Hermes operator, these skills are a reference for how to persist progress across context windows and resume from partial state, synthesized from Anthropic and OpenAI engineering practice.

## Usage

| You say | What happens |
|---|---|
| "/do build a login flow" | do runs the five-phase feature loop, orchestrating code-explorer, code-architect, and code-reviewer agents in parallel. |
| "Investigate this bug" | omo picks a minimal agent set for code analysis, fix planning, and implementation. |
| "/product-requirements for a billing feature" | product-requirements gathers requirements and generates a scored PRD. |
| "Generate test cases from this PRD" | test-cases produces functional, edge case, error handling, and state transition cases. |
| "Install this skill from GitHub" | skill-install fetches the repo and runs an automated security scan before adding it. |
| "/sparv" | sparv starts the Specify, Plan, Act, Review, Vault loop with the 10-point spec gate. |

## Verification

Probe one skill on the `master` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/stellarlinkco/myclaude/master/skills/product-requirements/SKILL.md
```

Then run the installer with `--list` to confirm the modules and skills it detects, and check `~/.claude/installed_modules.json` after install.

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| product-requirements | Pass | Pass | Pass |
| test-cases | Pass | Pass | Pass |
| prototype-prompt-generator | Pass | Pass | Pass |
| skill-install | Pass | Warn | Warn |
| codeagent | Pass | Warn | Pass |
| browser | Pass | Warn | Warn |
| harness | Pass | Warn | Pass |
| omo | Pass | Warn | Warn |
| dev | Warn | Warn | Pass |
| do | Fail | Warn | Pass |
| sparv | Pass | Pass | Pass |
| codex | Pass | Pass | Pass |
| gemini | Pass | Pass | Pass |

The sample covers all 13 indexed listings; one carries a Fail (do) and several carry Warnings. The installer runs builds and scripts on your machine, and AGPL-3.0 applies to commercial use, so review the licence before distributing a derivative.

## Limitations

- Snapshot data, verified Nov 19, 2026: 3,972 combined installs across 13 indexed listings; 2,751 GitHub stars; AGPL-3.0 licence; last pushed 2026-05-04. Counts drift over time.
- The install index outruns the repo tree: 13 indexed listings against 11 `skills/` directories. codex and gemini are listed as installable skills (direct backend execution) with no `skills/<name>/SKILL.md` directory in the current tree.
- The repository uses the `master` branch, not `main`; keep `master` in any raw-file URL.
- AGPL-3.0 applies; the README points to a commercial licensing contact for use without AGPL obligations.
- The installer default is `~/.claude`; the `--update` path detects installed modules via `installed_modules.json`.

## Related

- [Claw Multi-Agent Skill Setup](/hermes/skills/catalog/claw-multi-agent-setup)
- [Subagent-Driven Development - Multi-Agent Task Dispatch Setup](/hermes/skills/catalog/subagent-driven-development-setup)
- [BMad Method Skills - Agile AI Development Suite Setup](/hermes/skills/catalog/bmad-method-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `/do` for feature work; it is the recommended default and orchestrates the parallel agents for you.
- Set the backend CLIs up first (`codex`, `claude`, `gemini`, `opencode`); the wrapper calls them and needs their stream-JSON and resume flags.
- Use `--list` before installing so you know which modules, skills, and the wrapper are available.
- If a module does not load, check `~/.claude/installed_modules.json` and re-run the installer with `--force`.
- For long multi-session jobs, reach for `/harness`; it is the checkpointing and recovery layer the other workflows can ride on.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
