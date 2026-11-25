---
title: "RTK CLI Proxy - Token Reduction Skills Setup"
description: "rtk-ai/rtk - 12.8K combined installs: Rust skills for TDD, triage, code simplification and design patterns from the RTK token-reduction CLI proxy."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/rtk-ai-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "rust", "token reduction", "tdd", "code quality"]
---

# RTK CLI Proxy - Setup Guide

**Source:** [rtk-ai/rtk](https://www.skills.sh/rtk-ai/rtk) via skills.sh - 12.8K combined installs across 8 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 morning sweep)
**GitHub:** [rtk-ai/rtk](https://github.com/rtk-ai/rtk) - 87,780 stars, Apache-2.0, last pushed Nov 25, 2026, develop branch (not main); eight indexed skill directories under .claude/skills/<name>/SKILL.md inside the RTK token-reduction CLI repository.
**Category:** Rust Development / Code Quality
**Quality Tier:** 🟡 Yellow - 5 of 8 sampled skills pass all three checks; rtk-triage, pr-triage and issue-triage carry a Snyk Warn.

rtk-ai/rtk publishes RTK (Rust Token Killer), a single Rust binary CLI proxy that compresses command output before an agent reads it, cutting LLM token consumption 60-90% on common dev commands. The repository also ships eight agent skills that encode the maintainers' Rust workflow: test-driven development, PR and issue triage, code simplification, and design patterns, each as a self-contained SKILL.md under .claude/skills/.

The skills.sh index lists 8 listings at 12.8K combined installs, all with a matching .claude/skills/<name>/ directory in the current tree. The tree also carries four additional skills without indexed listings: pr-review, repo-recap, security-guardian, and ship.

## Installation

Install the RTK CLI first, then plug it into your agent:

```bash
brew install rtk                                  # macOS, or Linux with Homebrew
winget install rtk-ai.rtk                         # Windows
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/develop/install.sh | sh   # Linux, macOS, WSL, Git Bash
```

```bash
rtk init -g                                       # Claude Code
rtk init --agent hermes                           # Hermes (plugin)
```

The eight indexed skills live in the repository under .claude/skills/<name>/SKILL.md. To use them standalone, copy that directory into your agent's skills folder. The repository also carries .claude/ agents, commands and hooks plus a CLAUDE.md for Claude Code.

## What It Provides

skills.sh publishes per-skill descriptions for all 8 indexed listings, and each has a matching .claude/skills/<name>/ directory in the current tree.

| Skill | Installs | Use For |
|---|---|---|
| rtk-tdd | 2,362 | enforces TDD (Red-Green-Refactor) for Rust development |
| code-simplifier | 2,337 | reviews RTK Rust code for idiomatic simplification |
| design-patterns | 2,022 | Rust design patterns for new modules and refactors |
| tdd-rust | 1,539 | TDD workflow for RTK filter development with fixtures and snapshot tests |
| rtk-triage | 1,531 | runs issue-triage and pr-triage in parallel, then cross-checks |
| pr-triage | 1,500 | audits open PRs, deep reviews selected ones, drafts review comments |
| issue-triage | 1,461 | audits open issues, categorizes, detects duplicates, risk assessment |

The remaining 1 indexed listing is performance (86 installs), CLI performance optimization for startup time, memory usage and token-saving benchmarks.

## Why This Matters for Hermes Agents

RTK is one of the most-starred Rust tooling projects on GitHub, and this suite turns the maintainers' own development discipline into agent-readable skills. For a builder running Hermes agents on Rust work, the TDD and triage skills turn a vague instruction like "tighten up the PR workflow" into the repo's actual conventions: Red-Green-Refactor loops, issue and PR triage with risk assessment, and Rust-idiomatic simplifications. The skills are short and focused, so an agent can load one without pulling in the whole repository. Every sampled skill passes the Gen Agent Trust Hub and Socket checks, with only three Snyk warnings in the sample. Adoption is trivial through the existing RTK install, and the skills sit alongside the CLI rather than requiring a separate marketplace. The main caveat is scope: these skills encode RTK's own Rust practices, not a general-purpose Rust curriculum.

## Usage

| You say | What happens |
|---|---|
| Add a failing test before I implement this | Uses rtk-tdd for a Red-Green-Refactor cycle with Rust-idiomatic patterns |
| Review the open PRs on this repo | Uses pr-triage to audit, deep review and draft review comments |
| Triage the open issues | Uses issue-triage to categorize, detect duplicates and assess risk |
| Run a full triage pass | Uses rtk-triage to run issue and PR triage in parallel and cross-check |
| Simplify this over-engineered function | Uses code-simplifier to apply Rust idioms without changing behavior |
| What pattern fits this new module | Uses design-patterns to pick a newtype, builder or state machine approach |
| Add a snapshot test for this filter | Uses tdd-rust for fixtures, token-savings assertions and insta snapshots |

## Verification

Confirm the README and a representative skill body resolve on the develop branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/rtk-ai/rtk/develop/README.md | head -40
curl -sL https://raw.githubusercontent.com/rtk-ai/rtk/develop/.claude/skills/rtk-tdd/SKILL.md | head -40
```

Both URLs return 200. The default branch is develop, not main, so use develop in raw GitHub URLs. After installing, review each .claude/skills/<name>/SKILL.md before relying on it.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| rtk-tdd | Pass | Pass | Pass |
| code-simplifier | Pass | Pass | Pass |
| design-patterns | Pass | Pass | Pass |
| tdd-rust | Pass | Pass | Pass |
| rtk-triage | Pass | Pass | Warn |
| pr-triage | Pass | Pass | Warn |
| issue-triage | Pass | Pass | Warn |
| performance | Pass | Pass | Pass |

All 8 sampled skills pass the Gen Agent Trust Hub and Socket checks; rtk-triage, pr-triage and issue-triage carry a Snyk Warn. All 8 indexed listings were sampled.

## Limitations

- Snapshot data, verified Nov 25, 2026: 12,838 combined installs across 8 indexed listings; 87,780 GitHub stars; Apache-2.0; last pushed Nov 25, 2026. Counts drift over time.
- The default branch is develop, not main; use develop in raw GitHub URLs.
- The tree ships 12 skills, but only 8 have indexed listings; pr-review, repo-recap, security-guardian and ship are not indexed on skills.sh.
- The skills encode RTK's own Rust workflow, so the Use For cells reflect the maintainers' repo rather than a general-purpose Rust toolkit.
- The rtk CLI is Apache-2.0, but the repository also contains rtk-engine and rtk-proxy under BUSL-1.1; the skills themselves live under the Apache-2.0 CLI.

## Related

[OpenClaw Token Optimizer Skills Setup](/hermes/skills/catalog/openclaw-token-optimizer-setup) | [Context Engineering Skills Setup](/hermes/skills/catalog/context-engineering-skills-setup) | [Actionbook Rust Skills - Rust Guidelines Setup](/hermes/skills/catalog/actionbook-rust-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install with brew install rtk, then rtk init -g (or rtk init --agent hermes) to wire the hook into your agent.
- Read CLAUDE.md and the .claude/agents and .claude/commands directories for the repo's full agent conventions beyond the eight skills.
- Remember the default branch is develop: use develop, not main, in any raw GitHub URL.
- Copy only the skills you need from .claude/skills/ into your agent's skills directory to avoid loading the whole repository.
- Pair rtk-triage (or issue-triage and pr-triage) with code-simplifier for a review pass that both triages and simplifies.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
