---
title: Oh My Hermes (OMH) Suite — Multi-Agent Orchestration Skills Setup Guide for Hermes Agents
description: "witt3rd/oh-my-hermes — 9 Hermes-native multi-agent orchestration skills (~800 combined installs): consensus planning (ralplan), verified execution (ralph), Socratic requirements interviews, parallel deep research, backlog triage, and end-to-end autopilot. Native Hermes install via hermes skills tap."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/oh-my-hermes-omh-suite-setup/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes skill", "agent skill", "skill setup", "multi-agent", "orchestration"]
---

# Oh My Hermes (OMH) Suite — Setup Guide

**Source:** [witt3rd/oh-my-hermes](https://skills.sh/witt3rd/oh-my-hermes)
**GitHub:** [witt3rd/oh-my-hermes](https://github.com/witt3rd/oh-my-hermes) (255⭐)
**Skills:** 9 (omh-ralplan, omh-ralph, omh-deep-interview, omh-deep-research, omh-triage, omh-autopilot + 3 drivers)
**Category:** Agent Orchestration & Multi-Agent Workflows
**First Seen:** August 14, 2026 sweep
**Quality Tier:** 🟡 Beta

Oh My Hermes (OMH) is a multi-agent orchestration framework for Hermes Agent, inspired by oh-my-claudecode and rebuilt natively for Hermes primitives. It provides composable skills for consensus planning (Planner → Architect → Critic debate), Socratic requirements interviewing, parallel research with citation verification, and evidence-verified execution — plus an optional plugin adding hook-based role injection and atomic state management. Skills work standalone with zero dependencies.

**Note:** distinct from the earlier-documented `oh-my-hermes-workflow` skill (publisher `aradotso/hermes-skills`). This is a different, larger suite from publisher `witt3rd/oh-my-hermes`.

---

## Overview

| Skill | Installs | What It Does |
|---|---|---|
| `omh-ralplan` | 93 | Consensus implementation planning — Planner + Architect + Critic debate until agreement (≤3 rounds) |
| `omh-ralplan-driver` | 91 | Dispatcher's playbook for driving an `omh-ralplan` run — context package, rounds, distillation |
| `omh-ralph` | 91 | Verified execution — one task per call, evidence required, "iron law" of proof |
| `omh-ralph-driver` | 90 | Dispatcher's playbook for `omh-ralph` — parallel batching, evidence gathering, commit hygiene |
| `omh-ralph-task` | 90 | Executor's discipline for one `omh-ralph` task — file-scope rigidity, sibling isolation |
| `omh-deep-research` | 95 | Parallel web research — decompose → subagents → synthesis → citation verification |
| `omh-deep-interview` | 92 | Socratic requirements interview — clarifies vague or ambiguous goals with coverage tracking |
| `omh-triage` | 89 | Multi-role consensus triage of an issue backlog (v0.1) |
| `omh-triage-driver` | — | Dispatcher's playbook for `omh-triage` runs — pre-flight audit, role-pass dispatch |
| `omh-autopilot` | 96 | End-to-end pipeline composing all skills: interview → plan → execute → QA → verify (v2.0.0) |

Recommended composition pipeline for unfamiliar domains:

```
omh-deep-research → omh-deep-interview → omh-ralplan → omh-ralph
```

---

## Installation

Native Hermes install (preferred):

```bash
hermes skills tap add witt3rd/oh-my-hermes
hermes skills install omh-deep-research omh-ralplan omh-ralplan-driver omh-deep-interview omh-ralph omh-ralph-driver omh-ralph-task omh-triage omh-triage-driver omh-autopilot
```

Or via skills.sh:

```bash
npx skills add witt3rd/oh-my-hermes
```

Manual alternative: copy `skills/<name>/` to `~/.hermes/skills/omh/`.

Optional plugin (hook-based role injection, atomic state management): copy `plugins/omh/` to `~/.hermes/plugins/omh/` (requires Python 3.10+ and `pyyaml`).

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Recent version with `hermes skills tap` support |
| **Python 3.10+** | Only for the optional `omh` plugin (`pyyaml`) |
| **Terminal toolset** | `omh-autopilot` metadata requires the `terminal` + `omh` toolsets |
| **API keys (research)** | `omh-deep-research` uses your configured search/web tools — none extra |

## Key Capabilities

### Multi-Role Consensus (omh-ralplan + driver)

Trigger: "plan this", "make a plan", "consensus plan". Planner, Architect, and Critic roles debate the implementation plan until consensus (max 3 rounds). The driver provides context-package authoring (where plan quality is born), round dispatch, and final review.

### Verified Execution (omh-ralph + driver + task)

Trigger: "execute the plan", "implement this". One task per call, with evidence required for every claim — screenshots, logs, test output. The driver handles parallel batching and strike categorization; the task skill enforces file-scope rigidity and stash-verify-against-HEAD sibling isolation.

### Deep Research (omh-deep-research)

Trigger: "research this domain". Decomposes the topic, fans out to parallel subagent searches, synthesizes findings, and verifies every citation before presenting.

### Requirements Interview (omh-deep-interview)

Trigger: "what should we build", vague goals. Socratic questioning with coverage tracking until the requirements are unambiguous.

### Backlog Triage (omh-triage + driver)

Trigger: "triage these issues". Maintainer (code-anchored) + Skeptic (pruning) roles reach consensus on issue priority. v0.1 — more roles coming.

### End-to-End Autopilot (omh-autopilot)

Trigger: "autopilot", "build me", "handle it all". Composes all skills into a multi-session pipeline: idea → interview → plan → execute → QA → verify.

## Quick Start

1. `hermes skills tap add witt3rd/oh-my-hermes && hermes skills install omh-deep-research omh-ralplan omh-ralph omh-autopilot`
2. Start with `omh-deep-interview` when goals are vague — it forces the user to pin requirements
3. Run `omh-ralplan` to get a consensus plan before any non-trivial implementation
4. Execute with `omh-ralph` — every completed task requires evidence
5. For unfamiliar domains, prepend `omh-deep-research` to the pipeline

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Feature planning** | Use `omh-ralplan` consensus debates for CorpusIQ product specs instead of single-pass planning |
| **Growth research** | Use `omh-deep-research` for market/competitor research with citation verification before writing content |
| **Multi-agent task execution** | Use `omh-ralph` verified-execution discipline in CorpusIQ supervisor-agent waves (complements the existing `corpusiq-supervisor-agent` wave dispatch) |
| **Requirement extraction** | Use `omh-deep-interview` on vague founder requests to pin scope before build |
| **Backlog management** | Use `omh-triage` for issue backlog triage in corpusiq-docs and CorpusIQ repos |

## Limitations / Verification

- `omh-triage` is v0.1 — Maintainer + Skeptic roles only, more roles planned
- `omh-autopilot` is multi-session — not for single-session trivial edits
- Skills run standalone, but full behavior (role injection, state) needs the optional `omh` plugin

```bash
# Verify skills installed
hermes skills list | grep omh-

# Functional test — ask Hermes in session:
#   "omh-deep-interview: interview me about a vague idea for a landing page"
```

## Security

- [witt3rd/oh-my-hermes repo](https://github.com/witt3rd/oh-my-hermes) — review SKILL.md files before install (standard practice)
- [Hermes skills security](/hermes/best-practices/security/) — skill trust guidance
- [Hermes plugin docs](https://hermes-agent.nousresearch.com/docs) — plugin permission model

## Related

- [Blueprint Orchestration — Multi-Agent Methodology](/hermes/skills/catalog/) — CorpusIQ's complementary multi-agent framework
- [Oh-My-Hermes Workflow (aradotso) Setup](/hermes/skills/catalog/oh-my-hermes-workflow-setup/) — the separate aradotso-published workflow skill
- [Agent Infrastructure catalog section](/hermes/skills/catalog/)

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
