---
title: "Wyatt Walsh Agents — Skill Governance and Orchestration Suite Setup"
description: "wyattowalsh/agents — 85 skills, 2.1K installs: the skills.sh founder's personal agent toolkit covering orchestration, skill lifecycle governance, code conventions, and agent team management."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/wyattowalsh-agents-setup/"
robots: "index,follow"
last_updated: "2026-08-18"
tags: ["hermes skill", "agent skill", "skill setup", "orchestration", "skill governance", "agent teams"]
---

# Wyatt Walsh Agents — Setup Guide

**Source:** [wyattowalsh/agents](https://skills.sh/wyattowalsh/agents)
**GitHub:** [wyattowalsh/agents](https://github.com/wyattowalsh/agents)
**Skills:** 85 skills · 2.1K total installs
**Category:** Agent Operations
**First Seen:** February 23, 2026 (catalogued August 18, 2026 sweep)
**Quality Tier:** 🟢 Production — Gen Agent Trust Hub Pass, Socket Pass, and Snyk Pass on the orchestrator flagship; published by Wyatt Walsh, founder of skills.sh itself

This is the personal agent toolkit of Wyatt Walsh, the founder of skills.sh — the platform this catalog documents. The 85 skills span four families: orchestration (subagent dispatch patterns, tier selection, recovery ladders, wargames), role personas (prompt-engineer, database-architect, devops-engineer, security-scanner, api-designer, frontend-designer), code conventions (python, javascript, shell), and a unique skill-lifecycle governance suite (skill-token-budget-linter, skill-compat-matrix, skill-quality-dashboard, skill-lifecycle-manager, skill-install-dry-run-planner, cross-agent-install-smoke, skill-signing-verifier, skill-tag-taxonomist, skill-registry-lock). The orchestrator skill applies classification and decomposition gates to every parallelization decision, with a canonical vocabulary and a recovery ladder for failed dispatches.

---

## Installation

```bash
npx skills add wyattowalsh/agents
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/wyattowalsh/agents --skill orchestrator
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Multi-agent environment** | Orchestration skills assume an agent runtime that supports subagent dispatch |

## What It Provides

| Skill Group | Examples | Purpose |
|---|---|---|
| Orchestration | orchestrator, reasoning-router, event-driven-architect, release-pipeline-architect, data-pipeline-architect | Parallel execution patterns, tier selection, and recovery rules |
| Role personas | prompt-engineer, database-architect, devops-engineer, security-scanner, api-designer, test-architect | Specialist role loading for agent teams |
| Code conventions | python-conventions, javascript-conventions, shell-conventions, git-workflow | Language and workflow standards |
| Skill governance | skill-token-budget-linter, skill-compat-matrix, skill-quality-dashboard, skill-lifecycle-manager, skill-registry-lock, skill-signing-verifier | The only dedicated skill-lifecycle tooling suite on skills.sh |
| Skill installation QA | skill-install-dry-run-planner, cross-agent-install-smoke, skill-package-manifest-enricher, skill-trace-debugger | Pre-install planning and cross-agent verification |
| Media and data | yt-dlp, ffmpeg, trafilatura, docling-graph, data-wizard | Agent-side media and data extraction |

Top skills by installs: orchestrator (89), skill-creator (88), wargame (63), prompt-engineer (63), email-whiz (63).

## Quick Start

1. Install: `npx skills add wyattowalsh/agents`
2. Load orchestrator before any parallelization decision — it applies the classification and decomposition gates
3. For skill operations, use skill-token-budget-linter and skill-compat-matrix when maintaining a skill collection

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Skill collection maintenance** | The governance suite (budget linter, compat matrix, quality dashboard) is purpose-built for maintaining large skill sets like ours |
| **Subagent orchestration** | orchestrator's dispatch patterns map directly to multi-agent workflows |
| **Skill install QA** | cross-agent-install-smoke and dry-run planning match our verify-before-assertion discipline |
| **Platform-founder provenance** | Authored by the skills.sh founder — the platform's own operator patterns, documented for our readers |

## Limitations / Verification

- Security audits on the orchestrator flagship: Gen Agent Trust Hub Pass, Socket Pass, Snyk Pass
- Publisher-page total verified (2.1K across 85 skills); 5 GitHub stars as of the sweep
- Below the 20K install guide bar — drafted on platform-founder authority (the skills.sh founder's own toolkit) and the unique skill-lifecycle governance category it covers
- Personal toolkit rather than a vendor product; conventions reflect one experienced operator's patterns, not a formal standard

```bash
npx skills add wyattowalsh/agents   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
