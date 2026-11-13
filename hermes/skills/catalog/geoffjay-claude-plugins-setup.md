---
title: "Geoffjay Claude Plugins - Language and Ops Setup"
description: "geoffjay/claude-plugins: 3.5K combined installs across 25 listings of Go, Rust, Tokio, Ruby and Git skills in a Claude Code marketplace"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/geoffjay-claude-plugins-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "golang", "rust", "claude code"]
---

# Geoffjay Claude Plugins - Setup Guide

**Source:** [geoffjay/claude-plugins](https://www.skills.sh/geoffjay/claude-plugins) via skills.sh - 3.5K combined installs across 25 indexed listings; first seen Nov 11, 2026
**GitHub:** 8 stars, MIT, `main` branch, last pushed 2025-11-04, 25 `SKILL.md` files under `plugins/<plugin>/skills/<name>/` against 25 indexed listings, 102 files in total
**Category:** Language and operations skills for Go, Rust, Ruby and Git, packaged as a Claude Code plugin marketplace
**Quality Tier:** 🟡 Established - a 25-for-25 tree across nine language plugins, held back by a last push in November 2025 and a small star count.

The repository describes itself as an experimental Claude Code plugin marketplace, and the README is frank about it: a place to try out plugins rather than a supported product. What it does have is breadth. Twenty-five skills spread across Go development, Rust CLI work, Rust GPUI desktop UI, Tokio async patterns, Ruby with Sinatra, Git operations and repository maintenance.

The layout is the marketplace convention rather than the flat `skills/` folder most packs use: `plugins/<plugin>/skills/<name>/SKILL.md`, with each plugin's agents, commands and skills installed together. The README argues for that granularity, claiming an average of 3.4 components per plugin and full coverage of its agents across plugins, so installing `golang-development` loads the Go surface and nothing else.

The retrieval pattern is progressive disclosure in three tiers: metadata always loaded, instructions loaded when a skill activates, resources loaded on demand. For an agent with a context budget, that is the design that makes a 25-skill marketplace usable rather than a permanent tax.

## Installation

The documented path is the Claude Code plugin marketplace, in two steps:

```bash
/plugin marketplace add geoffjay/claude-plugins
```

```text
/plugin
/plugin install golang-development
```

Adding the marketplace makes all plugins available without loading anything into context. Installing a plugin loads only its own agents, commands and skills, so a Go project can take `golang-development` and a Rust service can take `rust-cli-developer` without either seeing the other.

The individual listings are also indexed on skills.sh, which is where the install counts below come from. If you are installing into a non-Claude target, check that listing for the current install form rather than assuming the marketplace commands apply.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| documentation-update | 1,788 | Regenerating a plugin repo's own `agents.md`, `agent-skills.md`, `plugins.md` and `usage.md` from marketplace data. |
| git-troubleshooting | 346 | Recovering lost commits, fixing merge conflicts and resolving detached HEAD states. |
| git-advanced | 324 | Complex rebase strategies, interactive staging, commit surgery and history rewriting. |
| tokio-patterns | 124 | Core Tokio idioms: worker pools, request-response channels and task supervision. |
| tokio-concurrency | 75 | Fan-out and fan-in, pipeline processing and rate limiting in async services. |
| git-repository | 65 | Branch strategies (Git Flow, GitHub Flow, trunk-based) and monorepo layout decisions. |
| tokio-troubleshooting | 64 | Debugging async services with tokio-console, detecting deadlocks and tracing memory growth. |
| gpui-performance | 56 | GPUI rendering and layout performance, plus the memory profile of a Rust UI. |
| tokio-networking | 54 | HTTP services, gRPC and middleware composition with Hyper, Tonic and Tower. |
| gpui-patterns | 50 | GPUI component composition, state management, event handling and actions. |
| rust-ui-architecture | 49 | Structuring a Rust UI application: code organisation and GPUI-specific architecture. |
| git-conventions | 43 | Conventional Commits, branch naming and commit message standards. |

The remaining 13 indexed listings range from 33 to 42 installs.

The tail is where the bulk of the language coverage sits: the three Go skills (`go-patterns`, `go-concurrency`, `go-optimization`), the three Rust CLI skills (`clap-patterns`, `cli-configuration`, `cli-distribution`), the four Sinatra and Rack skills (`sinatra-patterns`, `sinatra-security`, `ruby-patterns`, `rack-middleware`), plus `gpui-styling` and `cli-ux-patterns`.

## Why This Matters for Hermes Agents

Language skills are usually the ones an agent gets wrong, because the model's default advice is a few years behind the language. `go-patterns` is scoped to Go 1.18 and later, and the Tokio skills are written around the current runtime rather than the pre-1.0 idioms that still dominate training data. That gap is exactly where an agent sounds confident and produces code that will not compile.

The Git pair is the most immediately useful part of the pack. `git-troubleshooting` covers the situations where an operation went wrong: lost commits, conflicted merges, a detached HEAD with work on it. Those are the moments when an agent with a wrong instruction does more damage than an agent with no instruction, so a skill that names the recovery sequence is worth more than its install count suggests.

The two repository-maintenance skills are a pattern worth copying. `documentation-update` and `marketplace-update` regenerate the repo's own metadata from its contents, which is how a marketplace of 25 skills stays internally consistent when plugins are added or removed.

The trade-off is age. A last push in November 2025 means the version-sensitive advice has had a year to drift, and the Tokio and GPUI ecosystems move faster than that.

## Usage

| You say | What happens |
|---|---|
| "I lost a commit after a bad rebase, get it back" | Runs `git-troubleshooting` and walks the reflog recovery path before touching the branch. |
| "Squash these twelve commits into one clean commit" | Runs `git-advanced` for an interactive rebase plan with the conflict steps called out. |
| "Write a worker pool in Go with bounded concurrency" | Runs `go-concurrency` and returns the goroutine, channel and context pattern. |
| "This Tokio service stops responding under load, find the deadlock" | Runs `tokio-troubleshooting` with the tokio-console workflow and the suspect await points. |
| "Set up the argument parser for this Rust CLI" | Runs `clap-patterns` and returns the derive structures plus validation. |
| "What branch strategy fits a three-person team shipping weekly" | Runs `git-repository` and compares Git Flow, GitHub Flow and trunk-based for that cadence. |
| "Write the commit message standard for this repo" | Runs `git-conventions` and returns the Conventional Commits rules and examples. |

## Verification

The tree is `plugins/<plugin>/skills/<name>/SKILL.md` on `main`, which is deeper than the usual `skills/` layout. Both probes returned 200 when this guide was written:

```bash
curl -fsSL https://raw.githubusercontent.com/geoffjay/claude-plugins/main/plugins/golang-development/skills/go-patterns/SKILL.md | head -8
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/geoffjay/claude-plugins/main/plugins/utilities/git/skills/git-advanced/SKILL.md
```

After install, confirm the plugin you asked for is the plugin that landed. Because the marketplace installs per plugin, a partial install is normal: you may have `golang-development` present and `rust-tokio-expert` absent, and the agent will not announce the difference.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| documentation-update | Warn | Pass | Pass |
| git-troubleshooting | Pass | Pass | Pass |
| git-advanced | Pass | Pass | Pass |
| tokio-patterns | Pass | Pass | Pass |

The other 21 indexed listings carry no published verdicts. The one warning sits on `documentation-update`, which rewrites files inside its own repository from marketplace data, so the warning fits the behaviour: a skill that regenerates documentation can overwrite whatever is there. The sampled skills are instruction files for local development work, and none of the four fetches data or handles credentials.

## Limitations

- Snapshot data, verified 2026-11-13: 3,515 combined installs across 25 indexed listings; 8 GitHub stars; MIT; last pushed 2025-11-04. Counts drift over time.
- The last push was November 2025. Advice about Tokio, GPUI and Clap versions has had a year to age, so check a version-specific claim against current documentation before applying it.
- `documentation-update` and `marketplace-update` are maintenance for this repository, not general work. They produce the metadata files that make this marketplace consistent, which is of little use in your own project.
- The install band is flat. Apart from documentation-update at 1,788 and the two Git skills at 346 and 324, every listing sits between 33 and 124 installs, which reads as a marketplace installed as a unit rather than skills chosen individually.
- Eight stars on 3,515 installs means the pack is being installed far more than it is being read or reviewed in public, and the README calls the project experimental rather than supported.
- Installing through the marketplace loads agents and commands as well as skills, so the context cost per plugin is larger than a single `SKILL.md`.

## Related

- [Laurigates Claude Plugins - Python and Ops Suite](/hermes/skills/catalog/laurigates-claude-plugins-setup)
- [Vinta Django AI Plugins - Django and Celery Setup](/hermes/skills/catalog/vintasoftware-django-ai-plugins-setup)
- [Astral Plugins - Python uv, ruff and ty Setup](/hermes/skills/catalog/astral-sh-claude-code-plugins-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install per plugin, not the whole marketplace. The point of the layout is that a Go repository never pays for the Tokio and Sinatra skills.
- Start with the Git pair. `git-troubleshooting` is useful on any repository, in any language, and it is the skill most likely to save work you have already done.
- Ask for the recovery plan before the recovery. The Git skills are strongest at naming the safe sequence, and a wrong rebase against a real branch is expensive to rehearse.
- Treat version claims as dated. The Go, Rust and Tokio advice was current in late 2025; for anything that has shipped since, use the skill for the pattern and the language docs for the syntax.
- Read the plugin's agents and commands alongside the skills. The pack installs all three, and the commands are the fast path to the workflow the skills describe.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
