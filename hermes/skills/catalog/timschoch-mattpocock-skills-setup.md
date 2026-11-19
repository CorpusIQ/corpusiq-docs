---
title: "Matt Pocock Skills - Engineering Workflows Setup"
description: "timschoch/mattpocock-skills: 20.0K combined installs across 52 listings; a mirror of Matt Pocock's TypeScript and AI-engineering skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/timschoch-mattpocock-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "typescript", "software engineering"]
---

# Matt Pocock Skills - Setup Guide

**Source:** [timschoch/mattpocock-skills](https://www.skills.sh/timschoch/mattpocock-skills) via skills.sh - 20.0K combined installs across 52 indexed listings; first seen Nov 18, 2026 (Nov 18, 2026 evening sweep)
**GitHub:** 0 stars, MIT licence, `main` branch, last pushed 2026-10-26. A fork of mattpocock/skills with local tweaks; skills live under `skills/engineering/`, `skills/productivity/`, and `skills/misc/`, one `SKILL.md` per directory.
**Category:** TypeScript and AI engineering workflows
**Quality Tier:** 🟡 Yellow - 3 Warns among 12 sampled verdicts (code-review, implement, improve-codebase-architecture); MIT licence.

This repo is a fork of Matt Pocock's skills collection, published under timschoch/mattpocock-skills with local tweaks. It mirrors the same body of TypeScript and AI-engineering work: skills for real engineering rather than vibe coding, covering code review, TDD, domain modeling, grilling sessions, and ticket-driven workflows. The README's fork banner points to this mirror as the copy to install.

The skills split into engineering and productivity sets, and further into user-invoked skills that orchestrate a workflow and model-invoked skills that hold reusable discipline. The catalog already covers other publishers of similar agent-skill material, and this guide does not claim those are identical to what this mirror carries.

## Installation

The fork banner points to this repo as the copy to install:

```bash
npx skills add timschoch/mattpocock-skills
```

Then run `/setup-matt-pocock-skills` once per repo. It asks which issue tracker you use, which labels you apply when triaging, and where to save generated docs. The repo also ships a Claude Code plugin manifest under `.claude-plugin/`. The README's per-agent plugin commands (`claude plugin install`, `codex plugin add`, `copilot plugin install`) reference the upstream `mattpocock/skills` marketplace rather than this mirror.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| code-review | 912 | Review changes since a fixed point along two axes, coding standards and spec fidelity, run in parallel sub-agents. |
| domain-modeling | 910 | Build and sharpen a project's domain model: challenge terms against a glossary, record ADRs, and update GLOSSARY.md. |
| codebase-design | 910 | Shared vocabulary for designing deep modules with a lot of behavior behind a small interface at a clean seam. |
| ask-matt | 910 | Route a request to the right skill or flow in this repo. |
| grilling | 908 | Interview the user relentlessly about a plan or decision until every branch of the design tree is resolved. |
| diagnosing-bugs | 907 | A disciplined diagnosis loop for hard bugs and performance regressions, gated phase by phase. |
| handoff | 901 | Compact the current conversation into a handoff document for another agent to pick up. |
| implement | 899 | Implement a piece of work based on a spec or set of tickets, driving TDD and closing with a code review. |
| improve-codebase-architecture | 891 | Scan a codebase for deepening opportunities, present them as an HTML report, and grill through one you pick. |
| prototype | 884 | Build a throwaway prototype to answer a design question, as a single HTML file or several UI variations. |
| research | 878 | Investigate a question against high-trust primary sources and capture findings as a cited Markdown file. |
| tdd | 871 | Test-driven development with a red-green-refactor loop, one vertical slice at a time. |
| triage | 848 | Move issues through a state machine of triage roles using labels. |
| to-spec | 846 | Turn the current conversation into a spec and publish it to the issue tracker, no interview. |
| to-tickets | 842 | Break a plan, spec, or conversation into tracer-bullet tickets that declare their blocking edges. |
| wayfinder | 817 | Plan a large piece of work as a shared map of decision tickets resolved one at a time. |
| to-questionnaire | 751 | Turn a decision you cannot answer alone into a Markdown questionnaire for the person who can. |
| wait-what | 726 | Re-pitch a message that did not land, in plain English using your GLOSSARY.md vocabulary. |
| wizard | 702 | Generate an interactive bash wizard that walks a human through steps only they can perform. |
| writing-for-agents | 683 | Write documents for agents: skills, AGENTS.md and CLAUDE.md files, and pointer-reached docs. |

The remaining 32 indexed listings range from 1 to 525 installs.

## Why This Matters for Hermes Agents

These skills target the failure modes agents actually have: misalignment with what the user wants, verbosity from missing shared vocabulary, code that does not work, and codebases that turn into mud. Each skill is a small, composable discipline rather than a process that owns your workflow, which is the point: they are designed to be adapted, not adopted wholesale.

For Hermes agents, the transferable pieces are the reusable disciplines: code-review's two-axis review, tdd's red-green-refactor loop, domain-modeling's glossary and ADR habit, and the grilling interview primitive that stress-tests a plan before code is written. The skills are plain SKILL.md files, so any harness that loads skill files can take the discipline directly.

## Usage

| You say | What happens |
|---|---|
| "Review this branch against the spec" | code-review runs the Standards and Spec reviews in parallel sub-agents and reports them side by side. |
| "Build this spec test-first" | implement drives tdd at the agreed seams and closes with a code review before committing. |
| "Grill me on this plan" | grilling interviews you relentlessly until every branch of the design tree is resolved. |
| "Diagnose this flaky bug" | diagnosing-bugs runs a loop of reproduce, minimize, hypothesize, instrument, fix, and regression-test. |
| "Turn this conversation into tickets" | to-tickets breaks the plan into tracer-bullet tickets, each declaring its blocking edges. |
| "Hand off this session" | handoff compacts the conversation into a handoff document for another agent to pick up. |
| "Plan something too big for one session" | wayfinder maps it as decision tickets on the issue tracker and resolves them one at a time. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/timschoch/mattpocock-skills/main/skills/engineering/code-review/SKILL.md
```

Then install and run the setup skill:

```bash
npx skills add timschoch/mattpocock-skills
```

Run `/setup-matt-pocock-skills` once per repo, then confirm the skills appear in your agent's skills directory.

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| code-review | Warn | Pass | Warn |
| domain-modeling | Pass | Pass | Pass |
| codebase-design | Pass | Pass | Pass |
| ask-matt | Pass | Pass | Pass |
| grilling | Pass | Pass | Pass |
| diagnosing-bugs | Pass | Pass | Pass |
| handoff | Pass | Pass | Pass |
| implement | Pass | Pass | Warn |
| improve-codebase-architecture | Pass | Pass | Warn |
| prototype | Pass | Pass | Pass |
| research | Pass | Pass | Pass |
| tdd | Pass | Pass | Pass |

The sample covers 12 of the 52 indexed listings; code-review carries Warns in Gen Agent Trust Hub and Snyk, and implement and improve-codebase-architecture each carry a Snyk Warn.

## Limitations

- Snapshot data, verified Nov 18, 2026: 20,006 combined installs across 52 indexed listings; 0 GitHub stars; MIT licence; last pushed 2026-10-26. Counts drift over time.
- This is a mirror: it forks Matt Pocock's skills with local tweaks, and the README's per-agent plugin commands reference the upstream mattpocock/skills marketplace rather than this fork.
- The fork banner command is npx skills add timschoch/mattpocock-skills, followed by /setup-matt-pocock-skills once per repo before the engineering skills.
- 20 of the 52 listings sit above the 600-install threshold; the remaining 32 are a long tail from 1 to 525 installs.
- The security sample flags a Warn on code-review, implement, and improve-codebase-architecture, so review those skills before production use.

## Related

- [Pedro Nauck Skills - Curated Agent Skill Library](/hermes/skills/catalog/pedronauck-skills-setup)
- [React Doctor - React Codebase Diagnostics Setup](/hermes/skills/catalog/react-doctor-setup)
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run /setup-matt-pocock-skills once per repo before the engineering skills, so the issue tracker and triage labels are configured.
- Use grilling (or grill-me) before every change; it is the repo's recommended alignment step.
- Run /improve-codebase-architecture every few days as a survey, not a rescue.
- Pick one install method per agent; installing both the plugin and the npx copy gives you every skill twice.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
