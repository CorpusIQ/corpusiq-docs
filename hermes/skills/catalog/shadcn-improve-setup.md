---
title: "shadcn Improve - Codebase Audit to Plan Setup"
description: "shadcn's improve skill: 37.5K combined installs. Audit a codebase with your best model, then hand self-contained plans to cheaper agents to execute."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/shadcn-improve-setup/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skill setup", "code audit", "planning", "shadcn"]
---

# shadcn Improve - Setup Guide

**Source:** [shadcn/improve](https://www.skills.sh/shadcn/improve) via skills.sh - 37.5K combined installs across 1 indexed listing; new to this catalog in the Oct 24, 2026 evening sweep

**GitHub:** [shadcn/improve](https://github.com/shadcn/improve) - 9,259 stars, MIT, last pushed 2026-09-12, branch main, single skill at `skills/improve/SKILL.md`

**Category:** Code Review / Planning and Delegation

**Quality Tier:** 🟢 Production - single purpose skill from the shadcn organization, MIT licensed, read-only on source code by design, all three auditors passing, and 37,531 installs on one listing

Most agent skills help a model write code. This one refuses to. `improve` surveys a repository as a senior advisor, produces a findings table with evidence, and writes implementation plans that a smaller, cheaper model can execute without ever seeing the advisory session. The author states the intent directly: spend the capable model on the part where judgment compounds, which is understanding the codebase and writing the spec, then hand execution to something cheap. The plans are the product.

The mechanism is what makes the claim credible. Reconciliation maps the repo's stack, conventions and the exact build, test and lint commands, and those commands become the verification gates inside every plan. The audit fans out across nine categories with `file:line` evidence per finding, and a vetting pass re-reads every cited location before anything is shown, so false positives are dropped and rejected findings are recorded with a reason. Findings then sort by leverage, and the ones you choose become self-contained files under `plans/`, each stamped with the commit it was written against, each with STOP conditions for when reality does not match.

## Installation

One command, from the README:

```bash
npx skills add shadcn/improve
```

The skill is a single directory with no dependencies and no scripts of its own. It works in any agent that reads the Agent Skills format, and the plans it writes are plain markdown, so the executor can be a different agent or a human.

Install it at the project level rather than globally. The skill reads the repository it runs in, and a global install invites it to audit whatever directory happens to be open.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| improve | 37,531 | A read-only codebase audit that returns a prioritized findings table and writes self-contained implementation plans into `plans/` for other models to execute. |

No indexed listings fall below the threshold; the single listing appears above.

The commands are the interface, and each one is a mode of the same skill. `/improve` runs a full audit. `/improve quick` is the cheap pass with hotspots and top findings only, `/improve deep` is exhaustive across every package and category, and `/improve security`, `/improve perf`, `/improve tests` and `/improve bugs` narrow the audit to one category. `/improve branch` audits only what the current branch changes, `/improve next` suggests where to take the project, `/improve plan <description>` skips the audit and specs one thing, `/improve review-plan <file>` critiques an existing plan, `/improve execute <plan>` dispatches a cheaper executor, and `/improve reconcile` refreshes the backlog.

## Why This Matters for Hermes Agents

The economics of agent work are lopsided. A capable model reading a whole repository to find the five things worth doing is expensive, and the same capable model typing out the fixes is expensive again. `improve` splits those two jobs deliberately, and the artifact that crosses the split is a markdown plan detailed enough for a weak executor: exact paths, current-state code excerpts, the repo's own verification commands, out-of-scope lists and stop conditions.

For a Hermes agent that orchestrates subagents, that artifact is the missing interface. Instead of passing a vague instruction to a cheaper worker and hoping, you pass a plan whose every step ends in a command with an expected output, so the worker never has to judge whether it succeeded.

The write boundary is the second reason to trust it. The skill never edits source, never runs commands that mutate the working tree, and never reproduces a secret value, only locations and credential types with a rotation recommendation. `execute` runs the executor in a disposable git worktree and reviews the diff against the plan, and merging stays with you. That is a reviewable loop rather than an autonomous one.

The honest cost is model quality in and token spend out. A shallow audit produces shallow plans, and `execute` plus `reconcile` are two more model sessions on top of the audit. Budget for the loop, not the single command.

## Usage

| You say | What happens |
|---|---|
| "Audit this codebase and tell me what to fix first" | Runs the full audit, maps the repo, fans out the nine categories, vets every citation and returns a findings table ordered by leverage. |
| "Do a quick pass, I only want the top issues" | `/improve quick` runs the cheap audit and returns hotspots and top findings without the exhaustive sweep. |
| "Plan items 1, 3 and 5" | Writes one plan file per finding into `plans/` with an index, priority order, dependency graph and verification gates. |
| "Audit just what this branch changes" | `/improve branch` scopes the audit to the diff, which is the pre pull request case. |
| "Implement plan 001" | `execute` spawns a cheaper executor in an isolated worktree, hands it the plan, re-runs every done criterion and returns a verdict. |
| "Publish these plans as issues" | `--issues` creates GitHub issues with the self-contained plan body so any agent or human can pick them up. |
| "Clean up the backlog" | `reconcile` verifies finished plans still hold, rewrites blocked ones around the obstacle and retires findings that were fixed independently. |

## Verification

The skill lives at one path on main. Confirm it before installing:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/shadcn/improve/main/skills/improve/SKILL.md
```

Read the procedure before the first run, because it documents the hard rules you are relying on:

- https://raw.githubusercontent.com/shadcn/improve/main/skills/improve/SKILL.md

After install, run it on a repository you know well before you run it on one you do not. The output shape is a findings table followed by a prompt for which items to plan, so a first run on familiar code tells you whether the evidence and the effort estimates are calibrated for your stack. Check that `plans/` is either gitignored or committed deliberately, since the files are meant to be read and reviewed.

## Security

skills.sh verdicts for sampled skills (verified October 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| improve | Pass | Pass | Pass |

A clean verdict is easy here because the skill's own design is restrictive. It reads source, searches, and writes only to `plans/`. It does not execute fix commands, does not mutate the working tree and does not copy secret values into the plan, and the repository states those as hard rules rather than preferences.

The authority that needs your attention is `execute`, which dispatches a second model into a git worktree and runs the repository's own verification commands. Those commands run code from the repository, so treat executors like any other build agent: sandboxed working directory, no production credentials in the environment, and a human reading the diff before merge.

## Limitations

- Snapshot data, verified October 24, 2026: 37,531 combined installs across 1 indexed listing; 9,259 GitHub stars; MIT; last pushed 2026-09-12. Counts drift over time.
- The repository has not been pushed since 2026-09-12. The rules it writes are stable, but new framework idioms will not appear in its guidance until it is updated.
- Plan quality tracks the model that ran the audit. A cheap advisor produces plans a cheap executor can follow but you would not want to ship.
- Nine audit categories fan out as parallel subagents, so a full run on a large monorepo is a real token spend before any plan exists.
- `execute` and `reconcile` are separate model sessions on top of the audit. The cheap execution half only pays off if you use the plans.
- Plans trust the repository's own build, test and lint commands. A repository with no working verification commands gets plans with weak gates.

## Related

- [Writing Plans Subagent Development Setup](/hermes/skills/catalog/writing-plans-subagent-development-setup)
- [Plan Mode - Plan-Only Execution Mode Setup](/hermes/skills/catalog/plan-mode-setup)
- [AccessLint Skills - WCAG 2.2 Accessibility Audit Suite Setup](/hermes/skills/catalog/accesslint-skills-setup)

## Pro Tips

- Run `/improve quick` first on any repository over a few thousand files. It costs a fraction of the deep pass and usually names the same top three findings.
- Commit the intent documents the skill reads (`docs/adr/`, `CONTEXT.md`, `DESIGN.md`, `PRODUCT.md`) if you have them. The reconciliation step uses them to avoid re-flagging decided tradeoffs.
- Keep `plans/` in version control during a migration. The commit stamp in each plan is what lets an executor detect drift before it edits.
- Use `--issues` when more than one agent or person will execute. The issue body is the same self-contained plan, so the queue and the work live in one place.
- Feed `review-plan` a plan you wrote by hand before trusting the generated ones. The critique mode is a cheap way to see the standard the skill is holding itself to.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
