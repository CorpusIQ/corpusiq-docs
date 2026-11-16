---
title: "Pwguler Skills - Triple Debt Engineering Suite"
description: "pwguler/skills - 15.2K combined installs across 47 indexed listings: test-first engineering loop with specs, ADRs and review checks."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pwguler-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skill setup", "engineering", "tdd", "specs"]
---

# Pwguler Skills - Setup Guide

**Source:** [pwguler/skills](https://www.skills.sh/pwguler/skills) via skills.sh - 15.2K combined installs across 47 indexed listings; first seen Nov 15, 2026 (Nov 15 evening sweep)
**GitHub:** 10 stars, MIT license, `main` branch, last pushed 2026-10-16, fifteen `SKILL.md` files under `skills/`
**Category:** Engineering workflow and test-first delivery
**Quality Tier:** 🟡 Yellow - the 15 sampled skills pass the Gen Agent Trust Hub and Socket; three carry a Snyk warn.

This suite works against the three debts of the Triple Debt Model (Storey, [arXiv:2603.22106](https://arxiv.org/abs/2603.22106)): technical debt in the code, cognitive debt in the people, and intent debt in what nobody wrote down. Each debt maps to a set of skills, and the base suite forms one loop: drill, then implement, then verify, then land.

The loop has a bounded goal and a maker/checker cycle. A quality claim that no command can settle goes to rubric, where a judge who did not make the work decides it. Before work with a spec lands, the rubric defect pass sends the diff to two fresh reviewers. On a fast path, an obvious task skips the interview; if verify fails twice on a fast-path task, the task goes back through drill.

Twenty-four engineering principles, such as "fix root causes" and "explain the number", are folded into the skill whose step they detail, so a session reads a principle only when it reaches that step.

## Installation

Install the whole suite with `npx skills`; it asks which agents get it:

```bash
npx skills add pwguler/skills
```

Update with:

```bash
npx skills update
```

Start a new session to load the new version. If a skill is missing after an update, install the suite again.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| implement | 1,034 | Build code test-first in thin slices. |
| land | 1,023 | Send a finished branch through fresh reviewers, then merge or open a PR. |
| drill | 1,023 | Settle a plan into a spec and hard-to-undo decisions into ADRs. |
| verify | 1,020 | Prove a result against evidence before saying done. |
| debug | 1,010 | Fix a bug at its root cause. |
| research | 1,009 | Find why code has its shape, or read a library or standard before a subagent handoff. |
| core-interview | 1,006 | Settle a topic through questions, one decision at a time. |
| parallel | 1,004 | Run independent tasks or competing attempts in parallel. |
| write-skill | 1,000 | Write a document an agent reads, or encode a mistake corrected twice. |
| rubric | 978 | Have fresh reviewers judge a change or a quality no command can settle. |
| tldr | 975 | Report results, not transcripts, for a finished task or a catch-up. |
| prototype | 975 | Build a throwaway to react to a design decision. |
| recall | 920 | Rebuild where work stands from past sessions. |
| reflect | 902 | Turn session lessons into checks, skills or project files. |
| perf | 897 | Measure before changing code for speed; read a profile or trace. |

The remaining 32 indexed listings range from 3 to 105 installs.

## Why This Matters for Hermes Agents

The Triple Debt Model is the useful part here: it names the failure modes an agent hits when it ships code faster than people can follow it. Technical debt is in the code, cognitive debt is in the shared understanding of the system, and intent debt is in the reasons, goals and constraints nobody wrote down. A generic model treats all three as "write more code"; this suite gives each a distinct skill and a distinct artifact.

The maker/checker cycle matters for agents that run unattended. verify rejects by default and quotes evidence for every acceptance criterion, and rubric hands quality judgments to a judge who did not make the work. That structure is exactly what a solo agent with no human in the loop needs to avoid declaring victory too early.

The principle files are a good example of context discipline. Instead of a giant prompt stuffed into every session, each principle opens only at the step it adds detail to, which keeps the context window bounded without losing the guidance.

## Usage

| You say | What happens |
|---|---|
| "Plan this feature end to end" | drill writes the goal, non-goals and acceptance criteria into a spec, and hard decisions into ADRs. |
| "Implement this spec" | implement builds the change test-first in thin slices, then verify checks each criterion against evidence. |
| "Fix this bug" | debug finds the root cause instead of patching the symptom. |
| "Why does this code look like this" | research reads the owning source or standard and returns the reason. |
| "Is this actually done" | verify rejects by default and quotes the evidence for each acceptance criterion. |
| "Run these five checks at once" | parallel fans the independent tasks out and joins the results. |
| "Catch me up on this session" | tldr reports results, not a transcript. |

## Verification

Check the skill files before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/pwguler/skills/main/skills/implement/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/pwguler/skills/main/skills/drill/SKILL.md | head -20
npx skills add pwguler/skills --list
```

The suite runs in any coding agent that reads Agent Skills; confirm your host can load `skills/<name>/SKILL.md` before relying on the loop.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-15) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| implement | Pass | Pass | Pass |
| land | Pass | Pass | Pass |
| drill | Pass | Pass | Pass |
| verify | Pass | Pass | Pass |
| debug | Pass | Pass | Pass |
| research | Pass | Pass | Warn |
| core-interview | Pass | Pass | Pass |
| parallel | Pass | Pass | Pass |
| write-skill | Pass | Pass | Pass |
| rubric | Pass | Pass | Pass |
| tldr | Pass | Pass | Pass |
| prototype | Pass | Pass | Warn |
| recall | Pass | Pass | Warn |
| reflect | Pass | Pass | Pass |
| perf | Pass | Pass | Pass |

Every sampled skill passes the Gen Agent Trust Hub; the only non-Pass cells are Snyk warns on research, prototype and recall.

## Limitations

- Snapshot data, verified 2026-11-15: 15,161 combined installs across 47 indexed listings; 10 GitHub stars; MIT; last pushed 2026-10-16. Counts drift over time.
- The install index outruns the tree: 47 indexed listings against 15 `SKILL.md` directories. The 32 listings without a matching directory are the 24 `principle-*` listings at 3 installs each plus 8 lower-install skills (architecture, deep, teach, spawn, bro, pecut, which-skill, huh).
- The 24 engineering principles are folded into the skill whose step they detail, so they surface only when that step runs; there is no standalone index of all of them.
- The base loop is opinionated and heavier than a plain ask-and-code skill for small, one-off edits.
- Installation is via `npx skills` only; the README carries no Claude Code plugin or zip bundle.

## Related

- [Stark AI Agent Skills - Engineering Workflow Kit](/hermes/skills/catalog/stark-ai-agent-skills-setup)
- [Sentimony Agentic Workflow - Spec to PR Setup](/hermes/skills/catalog/sentimony-agentic-workflow-setup)
- [OpenSpec Skills - Spec-Driven Development Suite Setup](/hermes/skills/catalog/fission-openspec-skills-setup)
- [Spec Kit Skills - Specify, Plan, Implement](/hermes/skills/catalog/speckit-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the whole suite once rather than a subset; the loop skills reference each other.
- Fast path: a one-sentence plan skips the drill interview; if verify fails twice, the task was not obvious, so send it back through drill.
- Subtraction first: in each file a slice or fix changes, the dead code goes before anything new comes in.
- Start a new session after `npx skills update`, or the new version will not load.
- Keep the spec after the branch lands, so the branch records why the code looks the way it does.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
