---
title: Matt Pocock Agent Workflow Suite - 20-Skill Setup Guide for Hermes Agents
description: Install and configure 20 previously uncatalogued Matt Pocock skills (11.4M+ combined installs) - grill-me (1.1M), grill-with-docs (941K), tdd (873K), handoff (774K), triage (760K), teach (626K), domain-modeling (603K), code-review (521K) and more.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mattpocock-agent-workflow-suite-setup/"
robots: "index,follow"
last_updated: "2026-09-09"
tags: ["hermes skill", "agent skill", "skill setup", "matt pocock", "workflow"]
---

# Matt Pocock Agent Workflow Suite - Setup Guide

**Source:** [mattpocock/skills](https://skills.sh/mattpocock/skills) (20 skills, 11.4M+ combined installs)
**Category:** Software Engineering / Agent Workflow / Product Management
**First Seen:** Sep 9, 2026

This guide covers 20 Matt Pocock skills that were **not** included in the earlier [Mattpocock Skills Setup](/docs/hermes/skills/catalog/mattpocock-skills-setup) (19 skills) or [Engineering Skills](/docs/hermes/skills/catalog/matt-pocock-engineering-setup) (5 skills) guides. Together they form the interrogation-and-execution layer of the Pocock methodology: grilling plans, TDD loops, domain modeling, triage, handoffs between agent sessions, and spec-to-ticket pipelines. Combined installs: **11,400,000+**.

---

## Installation

Install all 20 at once:

```bash
# Interrogation layer
npx skills add mattpocock/skills --skill grill-me
npx skills add mattpocock/skills --skill grill-with-docs
npx skills add mattpocock/skills --skill loop-me
npx skills add mattpocock/skills --skill wait-what

# Engineering layer
npx skills add mattpocock/skills --skill tdd
npx skills add mattpocock/skills --skill code-review
npx skills add mattpocock/skills --skill diagnosing-bugs
npx skills add mattpocock/skills --skill domain-modeling
npx skills add mattpocock/skills --skill research
npx skills add mattpocock/skills --skill setup-ts-deep-modules

# Planning-to-tickets layer
npx skills add mattpocock/skills --skill to-spec
npx skills add mattpocock/skills --skill to-tickets
npx skills add mattpocock/skills --skill to-questionnaire
npx skills add mattpocock/skills --skill wayfinder
npx skills add mattpocock/skills --skill wizard

# Session and collaboration layer
npx skills add mattpocock/skills --skill handoff
npx skills add mattpocock/skills --skill triage
npx skills add mattpocock/skills --skill teach
npx skills add mattpocock/skills --skill writing-for-agents
npx skills add mattpocock/skills --skill retro
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Any recent version with skill support |
| **Node.js 18+** | For the `npx skills` CLI |
| **GitHub repo with Issues enabled** | For triage, to-spec, to-tickets, wayfinder output |
| **GitHub PAT with `repo` scope** | For issue/ticket creation |

---

## Capabilities

### Interrogation Layer

| Skill | Installs | What It Does |
|---|---|---|
| **grill-me** | 1,103,281 | A relentless interview to sharpen a plan or design. Dispatches to `grilling`. The flagship skill of the suite |
| **grill-with-docs** | 941,573 | The grilling interview that also creates docs (ADRs and glossary) as it goes |
| **loop-me** | 277,934 | Grill me about specs for the workflows I want to build, within this workspace |
| **wait-what** | 224,639 | "Stop. That last message did not land: re-pitch it." - clarity catch |

### Engineering Layer

| Skill | Installs | What It Does |
|---|---|---|
| **tdd** | 873,338 | Red-green-refactor loop reference: what a good test is, where tests go, anti-patterns, loop rules. Reads CONTEXT.md and ADRs |
| **code-review** | 521,103 | Reviews changes since a fixed point along two axes: Standards (repo's documented coding standards) and Spec (does the code match what was asked) |
| **diagnosing-bugs** | 574,167 | Diagnosis loop for hard bugs and performance regressions |
| **domain-modeling** | 603,161 | Build and sharpen a project's domain model; writes/edits CONTEXT.md and ADRs |
| **research** | 476,454 | Investigates a question against high-trust primary sources, captures findings as a Markdown file in the repo |
| **setup-ts-deep-modules** | 211,966 | Wires dependency-cruiser into a TypeScript repo so each package is a deep module (implementation hidden, reachable only through entry points) |

### Planning-to-Tickets Layer

| Skill | Installs | What It Does |
|---|---|---|
| **to-spec** | 474,307 | Turns the current conversation into a spec and publishes it to the issue tracker - no interview, just synthesis |
| **to-tickets** | 466,073 | Breaks a plan/spec/conversation into tracer-bullet tickets, each declaring blocking edges, published to the configured tracker |
| **to-questionnaire** | 282,849 | Turns a decision you can't fully answer into a questionnaire for someone else |
| **wayfinder** | 483,129 | Plans work too big for one agent session as a shared map of decision tickets, resolved one at a time |
| **wizard** | 335,511 | Generates an interactive bash wizard for steps only a human can perform (infrastructure, credentials, CI secrets, third-party dashboards) |

### Session and Collaboration Layer

| Skill | Installs | What It Does |
|---|---|---|
| **handoff** | 774,587 | Compacts the current conversation into a handoff document for another agent to pick up |
| **triage** | 760,099 | Moves issues and external PRs through a state machine of triage roles: categorise, verify, grill if needed, write agent-ready briefs |
| **teach** | 626,663 | Teaches the user a new skill or concept, within this workspace |
| **writing-for-agents** | 233,014 | Writing documents for agents: creating/editing skills, AGENTS.md, CLAUDE.md |
| **retro** | 72,735 | Conducts a retrospective on a coding session |

---

## Quick Start

1. Install the interrogation layer first: `npx skills add mattpocock/skills --skill grill-me`
2. Grill a plan before building: invoke `grill-me` (or `grill-with-docs` if you want ADRs and a glossary as output)
3. Build with `tdd`, review with `code-review`, diagnose failures with `diagnosing-bugs`
4. Convert the finished conversation to specs and tickets: `to-spec` then `to-tickets` (or `wayfinder` for multi-session work)
5. End each session with `handoff` so the next agent session picks up without re-reading the transcript

**Typical workflow:** grill-me -> tdd -> code-review -> to-spec -> to-tickets -> handoff

---

## Limitations / Verification

```bash
# Verify skills installed
hermes skills list | grep -E "grill-me|tdd|handoff|triage|to-spec"

# Functional test
# "Grill me about this plan" -> invokes grill-me -> dispatches to grilling
```

- `grill-me` sets `disable-model-invocation: true` - it is invoked via the Skill tool, not by the model directly
- `loop-me`, `retro`, `setup-ts-deep-modules` live in the repo's `in-progress` directory - stable but evolving
- Marketplace-only siblings (listed on skills.sh, no SKILL.md in the repo main branch yet): `qa` (205K), `diagnose` (238K), `obsidian-vault` (201K), `review` (94K), `batch-grill-me` (64K)

## Security

- [skills.sh publisher page](https://skills.sh/mattpocock/skills) - Pass
- [GitHub repo](https://github.com/mattpocock/skills) - Pass
- [Publisher](https://github.com/mattpocock) - Pass (146K+ stars)

## Related

- [codebase-design Setup](/docs/hermes/skills/catalog/codebase-design-setup)
- [Resolving Merge Conflicts Setup](/docs/hermes/skills/catalog/resolving-merge-conflicts-setup)
- [Matt Pocock Engineering Skills Setup](/docs/hermes/skills/catalog/matt-pocock-engineering-setup)
- [Mattpocock Skills Setup](/docs/hermes/skills/catalog/mattpocock-skills-setup)
