---
title: "Sentimony Agentic Workflow - Spec to PR Setup"
description: "sentimony/agentic-workflow on skills.sh: 8.9K combined installs across 11 listings; spec, plan, implement, verify and review skills for coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sentimony-agentic-workflow-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "planning", "workflow"]
---

# Sentimony Agentic Workflow - Setup Guide

**Source:** [sentimony/agentic-workflow](https://www.skills.sh/sentimony/agentic-workflow) via skills.sh - 8.9K combined installs across 11 indexed listings; first seen 2026-11-05 (Nov 5, 2026 morning sweep)
**GitHub:** 4 stars, MIT, last pushed 2026-11-05, 9 SKILL.md directories under skills/
**Category:** Spec-to-PR delivery workflow for coding agents: specify, plan, implement, verify, review and finalize
**Quality Tier:** 🟡 Beta - Gen Agent Trust Hub Warn on session-learnings and Snyk Warns on cr-request and plan-craft; MIT; 4 stars.

Agentflow, published from `sentimony/agentic-workflow` at version v0.0.21, is a nine-skill workflow that covers one delivery chain: take a request or an issue, design it, plan it, implement it, verify it, review it, resolve the review, and decide how the branch leaves. Each skill owns one stage and is written with an explicit boundary about what it must not do.

The skills are installed as a single plugin rather than picked one by one. `resolve-issue` is the orchestrator, and without the `--auto` flag the workflow stops at each meaningful stage and asks for the next transition. The README documents the chain as `resolve-issue` into intake, `specify`, `plan-craft`, plan review, `implement`, `verify`, code review, `cr-received`, `verify`, then PR, ready, merge, deploy, evidence, cleanup and `session-learnings`.

Worth stating up front: the repository is candid that native installation, upgrade and rollback evidence is unverified under an owner-approved release exception, that production forge adapters remain unverified, and that its Python suites exercise local contracts and injected fixtures rather than live acceptance. Treat it as a well-specified workflow in active development, not a turnkey release.

## Installation

The plugin lives in the author's marketplace, and the README is explicit that this repository has no marketplace of its own. For Claude Code:

```bash
claude plugin marketplace add sentimony/marketplace
claude plugin install agentflow@sentimony
```

For Codex:

```bash
codex plugin marketplace add sentimony/marketplace
codex plugin add agentflow@sentimony
```

Any other agent can install the stage skills through skills.sh:

```bash
npx skills add sentimony/agentic-workflow -s specify plan-craft implement verify cr-request cr-received finalize session-learnings -a codex claude-code -y
```

Two migration notes from the README matter before a first install. The plugin was renamed from `aw` to `agentflow` in version 0.0.15, and installing both identities together conflicts because they expose the same skill names, so uninstall `aw` and remove the old `agentic-workflow` marketplace first. The README also lists the earlier `sentimony/skills` devflow skills that `agentflow` replaces (`scope-triage`, `plan-crafting`, `inline-plan-dev`, `subagent-plan-dev`, `verification-gate`, `branch-finish`, `review-request`, `review-resolution` and `cross-review`), and says to remove them from a workspace that installs `agentflow` or they will intercept the same requests.

## What It Provides

Nine indexed listings, all above the threshold.

| Skill | Installs | Use For |
|---|---|---|
| session-learnings | 1,203 | Recording reusable learnings from a session in gitignored notes, then triaging them into the right instruction file after approval |
| cr-request | 1,130 | Pinning an exact change, stating its intent and dispatching a read-only reviewer with a persistent full report |
| cr-received | 1,117 | Verifying each review finding against current code, deciding with evidence and fixing only what holds up |
| finalize | 1,021 | Guarding local readiness and strict merge eligibility, then handling branch and workspace disposal |
| implement | 974 | Executing a plan with resumable task evidence, directly or through subagents |
| plan-craft | 960 | Turning an approved spec into an ordered task plan with exact files, checks and commits |
| verify | 927 | Checking completion claims on the pinned tree and returning PASS, FAIL, INCOMPLETE or BLOCKED |
| specify | 926 | Triaging a request and writing an approved spec with checkable acceptance criteria |
| resolve-issue | 433 | Running issue intake through configured delivery with durable recovery and fresh host authority |

The remaining 2 indexed listings range from 3 to 169 installs (cross-cr at 169 and cr-receive at 3; the README records that version 0.0.3 renamed cr-receive to cr-received).

## Why This Matters for Hermes Agents

The usual failure mode for an agent that "finishes" a task is a confident claim with nothing behind it. `verify` exists to block exactly that: it runs before a merge, a pull request or a handoff report, checks the claims on the pinned tree, and returns one of four explicit verdicts rather than a paragraph of reassurance.

The review pair is the other half. `cr-request` pins the change and its intent before dispatching a reviewer, so the review has a fixed object to talk about, and `cr-received` verifies every finding against the current code before any fix is applied. That second step is what stops an agent from dutifully "fixing" a finding that was already wrong.

For Hermes agents running multi-step jobs, the resumable execution record in `implement` and the per-stage checkpoint boundaries are the practical win. An interrupted run resumes from the plan's record instead of re-deriving what it already did.

The honest caveat is maturity. With 4 GitHub stars and a README that flags unverified native install and production adapter paths, this is a workflow to adopt deliberately and test in a scratch repository before it touches a real delivery pipeline.

## Usage

| You say | What happens |
|---|---|
| "Take this GitHub issue through to a PR" | resolve-issue runs the stage chain and stops for approval at each transition unless `--auto` is passed |
| "Write a spec for this feature, then turn it into a task plan" | specify triages the request into an approved spec, then plan-craft produces the ordered plan with exact files, checks and commits |
| "Implement the plan" | implement executes the tasks and records resumable evidence per task |
| "Is this actually done?" | verify checks the completion claims on the pinned tree and returns PASS, FAIL, INCOMPLETE or BLOCKED |
| "Get an independent review of this branch" | cr-request pins the change, states intent and returns compact verdicts with a full report |
| "The reviewer left six comments, work through them" | cr-received verifies each finding, decides with evidence and fixes only the ones that hold |
| "Record what we learned this session" | session-learnings writes reusable notes and triages them into instruction files after approval |

## Verification

Read the skill files before installing, since the workflow stages are the product:

```bash
curl -fsSL https://raw.githubusercontent.com/sentimony/agentic-workflow/main/skills/specify/SKILL.md | head -8
```

It should open with `name: specify` and a description about triaging a request into a direct change, a short note or a full design. Each stage has the same shape, so spot-check `plan-craft`, `verify` and `cr-received` the same way. After a skills.sh install, confirm the directories landed:

```bash
ls ~/.claude/skills | grep -E 'specify|plan-craft|implement|verify'
```

Four entries should appear, and the remaining stages follow the same naming. A functional check is to ask for a spec on a small feature and confirm the response produces acceptance criteria that `verify` could later check, rather than jumping straight to code.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| session-learnings | Warn | Pass | Pass |
| cr-request | Pass | Pass | Warn |
| plan-craft | Pass | Pass | Warn |
| cr-receive | Pass | Pass | Warn |

Three Snyk Warns and one Gen Agent Trust Hub Warn, with Snyk passing on `session-learnings` and Socket passing everywhere. The verdict table uses the older `cr-receive` name, so match it to `cr-received` when you read the report. These skills are instruction files with helper scripts rather than a service, so the main review questions are what they write to disk (session notes in gitignored files, evidence under `~/.sentimony`) and what they can do to a repository when a merge or a branch deletion is authorised. The README's own security model section is the place to start.

## Limitations

- Snapshot data, verified 2026-11-05: 8,863 combined installs across 11 indexed listings; 4 GitHub stars; MIT; last pushed 2026-11-05. Counts drift over time.
- The install index counts 11 listings against 9 skill directories. `cross-cr` (169) has no directory in the current layout, and `cr-receive` (3) is the pre-0.0.3 name of `cr-received`.
- Maturity is explicitly unproven: the README states that native installation, upgrade and rollback evidence remains unverified, and that production adapters, real forge policy, write and readback, deployments and native agent evals remain unverified.
- Environment isolation is cooperative. The helpers provide no OS containment, so the skills rely on the host's own permission model.
- `specify` and `plan-craft` use the separately installed `doc-preview` skill for document previews. Without it they report that and continue with degraded previews.
- `resolve-issue` delivery needs a configured G3 host bridge, and unknown project contracts block its actions. The workflow is resumable, but saved state grants no new permission.

## Related

- [Superpowers - Agentic Skills Framework Setup](/hermes/skills/catalog/superpowers-setup)
- [Writing Plans Subagent Development Setup](/hermes/skills/catalog/writing-plans-subagent-development-setup)
- [CodeStable Skills - AI Coding Workflow Setup](/hermes/skills/catalog/codestable-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start without `--auto`. The stage-by-stage mode is where the workflow earns its keep, because you see the spec and the plan before any code exists.
- Install `doc-preview` if you plan to use `specify` or `plan-craft` heavily, otherwise every spec step reports a missing preview dependency.
- Keep `verify` and `cr-received` apart. One checks completion claims, the other checks review findings, and collapsing them loses the evidence trail that makes the workflow auditable.
- Test the install in a scratch repository first. The README's own caveat about unverified native install and upgrade paths is the reason.
- Use `session-learnings` at the end of long sessions. It writes reusable notes to gitignored project files and only promotes them into instruction files after approval.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
