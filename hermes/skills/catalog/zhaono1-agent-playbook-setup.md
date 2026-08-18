---
title: "Zhaono1 Agent Playbook — 24-Role Agent Workflow Suite Setup"
description: "zhaono1/agent-playbook — 24 skills, 50.4K installs: self-improving agent loop, planning, security audit, and full lifecycle roles from PRD to deployment."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/zhaono1-agent-playbook-setup/"
robots: "index,follow"
last_updated: "2026-08-17"
tags: ["hermes skill", "agent skill", "skill setup", "agent workflows", "self-improvement"]
---

# Zhaono1 Agent Playbook — Setup Guide

**Source:** [zhaono1/agent-playbook](https://skills.sh/zhaono1/agent-playbook)
**GitHub:** [zhaono1/agent-playbook](https://github.com/zhaono1/agent-playbook)
**Skills:** 24 skills · 50.4K total installs
**Category:** Agent Workflows
**First Seen:** catalogued August 17, 2026 evening sweep (self-improving-agent on skills.sh since January 22, 2026; queue re-verification promoted the cluster from stale API numbers)
**Quality Tier:** 🟡 Trusted — flagship self-improving-agent carries Gen Agent Trust Hub Warn and Socket Warn (Snyk Pass); both named in Limitations

A 24-role agent lifecycle suite: self-improving-agent (33.1K installs) implements a multi-memory feedback loop with hooks-based self-correction, and the rest of the pack covers the full build cycle from PRD planning through code review, testing, and deployment. The cluster had been parked on stale API-sum numbers (top skill presumed under 1.2K); its publisher page reads 50.4K total.

---

## Installation

```bash
npx skills add zhaono1/agent-playbook
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/zhaono1/agent-playbook --skill self-improving-agent
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Agent runtime** | Claude Code, Cursor, or any skills-compatible agent |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| self-improving-agent | 33.1K | Multi-memory (semantic + episodic + working) self-correction loop with hooks (before_start, after_complete, on_error) and evolution markers |
| planning-with-files | 1.1K | File-backed planning discipline |
| security-auditor | 1.0K | Security review of proposed changes |
| architecting-solutions | 851 | Solution architecture guidance |
| skill-router | 839 | Routing between skills by task |
| prd-planner / prd-implementation-precheck | 807 / 690 | PRD planning and pre-implementation checks |
| workflow-orchestrator | 798 | Multi-step workflow coordination |
| test-automator / qa-expert / debugger | 785 / 728 / 728 | Test automation, QA, and debugging roles |
| figma-designer | 784 | Design handoff interpretation |
| code-reviewer / refactoring-specialist | 723 / 716 | Review and refactoring roles |
| session-logger | 724 | Session capture for continuity |
| api-designer / api-documenter / documentation-engineer | 681 / 691 / 689 | API and docs roles |
| performance-engineer | 682 | Performance analysis |
| auto-trigger / commit-helper / create-pr / deployment-engineer / long-task-coordinator | 648-669 | Trigger automation, commit, PR, deploy, and long-task roles |

## Quick Start

1. Install: `npx skills add zhaono1/agent-playbook`
2. Ask: "set up the self-improving loop for this project's skills"
3. The skill wires hooks on skill events and logs evolution markers for every change

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Self-evolution** | The multi-memory feedback loop maps to our own skill-patching discipline |
| **Lifecycle coverage** | PRD planner through deployment engineer gives a full pipeline in one pack |
| **Session continuity** | session-logger and planning-with-files reinforce our handoff-page pattern |

## Limitations / Verification

- Security audits on self-improving-agent: Gen Agent Trust Hub Warn, Socket Warn, Snyk Pass — trusted with both warns named; the skill writes agent memory files, which drives the audit warnings
- Publisher-page total verified (50.4K across 24 skills); repo at 73 GitHub stars
- A sibling publisher's self-improving-agent is already guided separately (charon-fan/agent-playbook at 32.2K); this guide covers zhaono1's full 24-skill suite on its own publisher-page numbers
- 23 of 24 skills sit under 1.2K installs — the suite's weight is concentrated in self-improving-agent

```bash
npx skills add zhaono1/agent-playbook   # verify install works
```

## Related

- [Self-Improving Agent — charon-fan Edition](/hermes/skills/catalog/self-improving-agent-setup/)
- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
