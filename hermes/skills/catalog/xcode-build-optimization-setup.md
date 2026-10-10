---
title: "Xcode Build Optimization - iOS Build Performance Setup"
description: "Setup guide for avdlee/xcode-build-optimization-agent-skill - 20.6K combined installs. 6 Xcode build diagnostics and optimization skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/xcode-build-optimization-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "ios development", "xcode", "build performance"]
---

# Xcode Build Optimization - Setup Guide

**Source:** [avdlee/xcode-build-optimization-agent-skill](https://www.skills.sh/avdlee/xcode-build-optimization-agent-skill) via skills.sh - 20.6K combined installs across 6 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [avdlee/xcode-build-optimization-agent-skill](https://github.com/avdlee/xcode-build-optimization-agent-skill) (1,254 stars, MIT; pushed 2026-09-14; branch `main`; skills under `skills/`, one directory per skill, e.g. `skills/xcode-build-fixer/SKILL.md`)
**Category:** iOS Development / Build Tooling
**Quality Tier:** 🟡 Beta - Antoine van der Lee; 1,254-star MIT repo; pushed Sep 2026; all sampled verdicts Pass

Xcode Build Optimization is an open-source Agent Skills suite by Antoine van der Lee (SwiftLee, RocketSim) for benchmarking and optimizing Xcode build performance. Six skills cover clean builds, incremental builds, compile hotspots, project settings, and Swift Package Manager overhead, with checks grounded in Apple documentation, WWDC sessions, and the SwiftLee build-performance workflow.

The suite is organized around an orchestrator that coordinates five specialist skills in a recommend-first loop: benchmark, analyze, prioritize, then apply only the changes you approve. The flagship entry point is `xcode-build-orchestrator`, which writes a prioritized optimization plan to `.build-benchmark/optimization-plan.md` without modifying a single project file until you sign off.

---

## Installation

### skills.sh

Install all six skills (the orchestrator needs the specialist skills to work):

```bash
npx skills add https://github.com/avdlee/xcode-build-optimization-agent-skill
```

Install a single skill for standalone use with the `--skill` flag:

```bash
npx skills add https://github.com/avdlee/xcode-build-optimization-agent-skill --skill xcode-project-analyzer
```

### Claude Code plugin

```bash
/plugin marketplace add AvdLee/Xcode-Build-Optimization-Agent-Skill
/plugin install xcode-build-skills@xcode-build-skills
```

### Codex and other agents

For OpenAI Codex and compatible tools, copy the skill folders into your skills directory:

```bash
cp -R skills/ "$CODEX_HOME/skills/"
```

A Cursor plugin is packaged but not yet live on the Cursor Marketplace. In every case, open your Xcode project folder in your AI coding tool so the skills can run against it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| xcode-build-fixer | 3,563 | Apply approved optimization changes and verify them with re-benchmarks |
| xcode-build-orchestrator | 3,537 | End-to-end workflow: benchmark, analyze, prioritize, approve, fix, re-benchmark |
| xcode-project-analyzer | 3,456 | Build settings, scheme, script phase, and target dependency auditing |
| xcode-compilation-analyzer | 3,366 | Swift compile hotspot analysis and source-level recommendations |
| xcode-build-benchmark | 3,336 | Repeatable clean and incremental build benchmarks with timestamped artifacts |
| spm-build-analysis | 3,334 | Package graph, plugin overhead, and module variant review |

No indexed listings fall below the threshold; all 6 appear above.

## Why This Matters for Hermes Agents

Build time is the tax on every change to an iOS or macOS codebase, and it compounds: a 1-second improvement on a 30-second incremental build is about 3.5 hours per developer per year at 50 builds a day. These skills give an agent the tooling to measure that cost instead of guessing at it, across clean builds, incremental builds, and the compile-hotspot level that neither CI dashboards nor stopwatch runs can see. The orchestrator encodes a safe operating pattern for autonomous work: analyze first, produce a prioritized plan, modify nothing until the plan is approved, then re-benchmark to prove the gain. The plan file is a diffable artifact, so a human can review an agent's reasoning in a PR. Because the checks follow Apple's guidance and the SwiftLee workflow, recommendations track mainstream Swift practice rather than folklore. And since the skills are plain SKILL.md folders, any coding agent that reads skill files can run them.

## Usage

| You say | What happens |
|---|---|
| Analyze why our incremental builds got slow | The orchestrator benchmarks clean and incremental builds, runs the specialist analyzers, and writes a prioritized plan to `.build-benchmark/optimization-plan.md` |
| Implement the approved items from the optimization plan | xcode-build-fixer applies only the approved changes and re-benchmarks to verify them |
| Find the compile hotspots in our Swift code | xcode-compilation-analyzer flags long type-checks and complex expressions with source-level recommendations |
| Audit our build settings against best practices | xcode-project-analyzer checks Debug and Release settings, schemes, script phases, and target dependencies |
| Review our Swift Package Manager overhead | spm-build-analysis inspects the package graph, plugin overhead, branch pins, and module variants |
| Benchmark the project before and after a dependency bump | xcode-build-benchmark produces repeatable, timestamped build measurements |

## Verification

Confirm the install from the CLI or the skills directory:

```bash
npx skills list | grep xcode
```

The skill run itself writes its evidence to `.build-benchmark/` in your project. Before installing, review the exact instructions the agent will read: fetch the build fixer skill file at `https://raw.githubusercontent.com/avdlee/xcode-build-optimization-agent-skill/main/skills/xcode-build-fixer/SKILL.md` (verified reachable Oct 10, 2026).

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| xcode-build-fixer | Pass | Pass | Pass |
| xcode-build-orchestrator | Pass | Pass | Pass |
| xcode-project-analyzer | Pass | Pass | Pass |

## Limitations

- Verdicts cover the three sampled skills only; xcode-compilation-analyzer, xcode-build-benchmark, and spm-build-analysis are unaudited here - re-check each skill's security page on skills.sh before production use.
- The orchestrator depends on the specialist skills; install all six together or the workflow breaks.
- The suite targets Xcode and Swift Package Manager projects, so non-Apple toolchains are out of scope.
- The Cursor plugin is packaged but not yet live on the marketplace; install via skills.sh or the manual copy path today.
- Enabling compilation caching can raise the first cold clean-build time; the gains show up on cached clean builds and incremental builds.
- MIT license per the repo; re-check the LICENSE and pin a revision when vendoring. Tracked as Beta (first seen on skills.sh Oct 9, 2026).

- Snapshot data, verified Oct 10, 2026: 20,592 combined installs across 6 indexed listings; 1,254 GitHub stars; MIT; last pushed 2026-09-14. Counts drift over time.

## Related

- [Macos Computer Use Setup](/hermes/skills/catalog/macos-computer-use-setup) - drive Xcode and the Simulator on a Mac from your agent
- [Hermes Agent Core - Official Skill Setup Guide](/hermes/skills/catalog/hermes-agent-setup) - the base Hermes skill layer this suite plugs into
- [Mosif16 Codex Skills - iOS Design Setup](/hermes/skills/catalog/mosif16-codex-skills-setup) - iOS-side companion for interface work
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the orchestrator: "Use the /xcode-build-orchestrator skill to analyze build performance and come up with a plan for improvements."
- Treat `.build-benchmark/optimization-plan.md` as the source of truth; it is shareable with teammates, reviewable in PRs, and diffable over time.
- Install all six even if you only ever invoke the orchestrator - the specialists are dependencies, not extras.
- Match the benchmark to the complaint: clean builds expose project-graph and package overhead, while incremental builds expose edit-loop and cache problems.
- Re-benchmark after every fix; the fixer verifies gains instead of assuming them.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
