---
title: "Jackin Dev Skills - Spec-Driven Workflow Orchestration"
description: "jackin-project/jackin-dev - 6.5K combined installs across 19 indexed listings: spec-driven feature, PR, research, and release workflow skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/jackin-dev-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "coding workflow", "release management"]
---

# Jackin Dev Skills - Setup Guide

**Source:** [jackin-project/jackin-dev](https://www.skills.sh/jackin-project/jackin-dev) via skills.sh - 6.5K combined installs across 19 indexed listings; first seen Nov 16, 2026 (Nov 16 evening sweep)
**GitHub:** 3 stars, Apache-2.0 license, `main` branch, last pushed 2026-11-16, eleven `skills/<name>/SKILL.md` files plus `.claude-plugin/`, `.codex-plugin/`, and `.kimi-plugin/` manifests at the repo root
**Category:** Coding workflow - spec-driven feature, PR, research, and release orchestration
**Quality Tier:** 🟡 Yellow - 7 of the 19 sampled skills carry a Snyk Warn; the rest pass all three scanners.

jackin-dev is a development-workflow plugin for the jackin project. It turns the repo's spec-driven workflow into eleven manual-only skills, one `SKILL.md` each, that sequence steps otherwise scattered across the repo's auto-loaded topic files such as PULL_REQUESTS.md and BRANCHING.md. Each skill names the governing rule instead of copying it, so a rule change in the repo keeps the skill pointing at the right place.

The suite walks a change from idea to release: propose a feature as a roadmap item plus an early PR, brainstorm it into design decisions, distill a goal prompt, create and refresh PRs, run the pre-merge gate and squash-merge, then check, note, and cut the release. Skills shell out to `cargo xtask` subcommands for the mechanical, exact steps and leave the judgment to the agent, which verifies the result.

## Installation

With the skills CLI:

```sh
npx skills add jackin-project/jackin-dev
```

Or a native plugin install per client (the README's plugin-first matrix):

| Client | Native plugin install |
|---|---|
| Claude Code | `claude plugin marketplace add jackin-project/jackin-dev`, then `claude plugin install jackin-dev@jackin-dev` |
| Codex CLI | `codex plugin marketplace add jackin-project/jackin-dev`, then `codex plugin add jackin-dev` |
| Grok Build | `grok plugin install jackin-project/jackin-dev --trust` |
| Kimi Code | `/plugins install https://github.com/jackin-project/jackin-dev`, then `/plugins reload` |

Do not copy these skills into `~/.agents/skills/` or a shared global skill tree; the README marks them manual-only and distributed only through native plugins.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| jackin-propose | 472 | Open a feature or idea as a roadmap item draft plus an early PR; never writes code. |
| jackin-goal-prompt | 470 | Distill a roadmap item, plus optional plan files, into a self-contained /goal prompt capped at 4000 characters. |
| jackin-checkout-pr | 470 | Switch the working repo onto a PR's branch via gh pr checkout, guarding the working tree first. |
| jackin-research | 469 | Produce a standalone multi-page research dossier on the docs site from web and codebase evidence. |
| jackin-release | 469 | Cut a release: run readiness gates, write the changelog, recommend a version, then execute cargo release on confirmation. |
| jackin-release-notes | 469 | Classify every PR merged since the last tag into Keep a Changelog categories and write the Unreleased section. |
| jackin-release-check | 469 | Run the release-readiness gates before a cut. |
| jackin-refresh-pr | 469 | Reconcile an open PR's title and body against the current diff. |
| jackin-merge-pr | 469 | Run the pre-merge gate, retire the roadmap item into docs, and squash-merge. |
| jackin-create-pr | 469 | Open a PR for a small fix with the correct body shape and auto-selected verify-locally blocks. |
| jackin-brainstorm | 469 | Turn a roadmap item's intent into concrete design decisions through freeform discussion. |

The remaining 8 indexed listings range from 160 to 164 installs.

## Why This Matters for Hermes Agents

The suite encodes a complete change lifecycle an agent can drive without a human relaying each step. jackin-propose scaffolds a roadmap item and opens an early PR but never writes code, so intent is captured before execution starts. jackin-brainstorm records design decisions into the roadmap item, and jackin-goal-prompt turns a finalized item into a self-contained /goal prompt an external spec-runner executes. PR mechanics are shared: jackin-propose and jackin-create-pr use the same pr body path, and jackin-refresh-pr reuses that binary to reconcile a drifted PR. jackin-merge-pr runs the pre-merge gate fail-closed: blast-radius confirm, CI polling, roadmap retirement, then squash-merge with trailers. The release skills run readiness gates, classify merged PRs into changelog categories, and cut the release. The division of labor matters for builders: cargo xtask binaries do the deterministic work and verify it, while the agent spends its effort on judgment only it can make. Manual-only enforcement via disable-model-invocation keeps the skills from firing on their own.

## Usage

| You say | What happens |
|---|---|
| "/jackin-dev:jackin-propose feature-name" | Scaffolds a roadmap item plus an early PR and stops; no code is written. |
| "/jackin-dev:jackin-brainstorm payments" | Discusses the item into concrete design decisions written into ## Design. |
| "/jackin-dev:jackin-goal-prompt <slug>" | Distills the roadmap item into a self-contained /goal prompt capped at 4000 characters. |
| "/jackin-dev:jackin-create-pr typo fix" | Opens a PR for a small fix with the correct body and verify-locally blocks. |
| "/jackin-dev:jackin-merge-pr 123" | Runs the pre-merge gate, retires the roadmap item, and squash-merges PR 123. |
| "/jackin-dev:jackin-release" | Runs readiness gates, writes the changelog, recommends a version, and cuts the release on confirmation. |

## Verification

Check the skill files before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/jackin-project/jackin-dev/main/skills/jackin-propose/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/jackin-project/jackin-dev/main/skills/jackin-release/SKILL.md | head -20
```

Each skill is one `SKILL.md` under `skills/<name>/`; confirm the path exists in the current tree before copying a specific skill.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| jackin-propose | Pass | Pass | Pass |
| jackin-goal-prompt | Pass | Pass | Pass |
| jackin-checkout-pr | Pass | Pass | Pass |
| jackin-research | Pass | Pass | Warn |
| jackin-release | Pass | Pass | Pass |
| jackin-release-notes | Pass | Pass | Warn |
| jackin-release-check | Pass | Pass | Pass |
| jackin-refresh-pr | Pass | Pass | Warn |
| jackin-merge-pr | Pass | Pass | Pass |
| jackin-create-pr | Pass | Pass | Pass |
| jackin-brainstorm | Pass | Pass | Pass |
| release-notes | Pass | Pass | Warn |
| release | Pass | Pass | Pass |
| release-check | Pass | Pass | Pass |
| research | Pass | Pass | Warn |
| propose | Pass | Pass | Pass |
| merge-pr | Pass | Pass | Warn |
| create-pr | Pass | Pass | Pass |
| brainstorm | Pass | Pass | Warn |

All 19 sampled skills pass the Gen Agent Trust Hub and Socket; 7 carry a Snyk Warn and none fail.

## Limitations

- Snapshot data, verified Nov 16, 2026: 6,453 combined installs across 19 indexed listings; 3 GitHub stars; Apache-2.0; last pushed 2026-11-16. Counts drift over time.
- Built for the jackin-project/jackin repository; expects `gh` authenticated, and the release skills additionally expect `cargo-release` plus a `.github/workflows/ci.yml`.
- Skills are manual-only and distributed only through native plugins; copying them into a shared skill tree is unsupported, and OpenCode is intentionally excluded.
- 7 of the 19 sampled skills carry a Snyk Warn (jackin-research, jackin-release-notes, jackin-refresh-pr, release-notes, research, merge-pr, brainstorm).
- The repository has 3 GitHub stars at snapshot, so it carries less community vetting than larger catalogs.

## Related

- [Fernando Skills](/hermes/skills/catalog/fernando-skills-setup)
- [OpenSpec Skills](/hermes/skills/catalog/fission-openspec-skills-setup)
- [Sentimony Agentic Workflow](/hermes/skills/catalog/sentimony-agentic-workflow-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use jackin-propose for feature work and jackin-create-pr for small fixes; the two are not interchangeable.
- Treat the repo's rule files as the source of truth; the skills name rules instead of copying them.
- Run jackin-refresh-pr on demand, not after every commit, to reconcile a drifted PR title and body.
- Confirm releases by hand; jackin-release runs cargo release only after explicit operator confirmation.
- Keep the plugin-first install and do not copy these skills into a shared global skill tree.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
