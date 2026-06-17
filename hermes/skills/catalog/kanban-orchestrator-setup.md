---
title: Kanban Orchestrator — Full Setup Guide for Hermes Agents
description: Install, configure, and use the kanban-orchestrator skill from nousresearch/hermes-agent. Decompose growth ops into parallel workstreams.
---

# Kanban Orchestrator — Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/kanban-orchestrator) (133 installs)
**Category:** Productivity

A decomposition playbook with anti-temptation rules for an orchestrator profile routing work through Kanban. The core rule: "don't do the work yourself." Break complex growth operations into parallel tasks, assign them to subagents, and track progress through a Kanban board.

---

## Installation

```bash
npx skills add nousresearch/hermes-agent@kanban-orchestrator -y
```

This is a prompt/instruction module. It changes how the agent thinks about work decomposition — no new tools or APIs.

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Any version |
| **delegate_task tool** | Must be enabled in Hermes config for subagent delegation |
| **Kanban board (optional)** | GitHub Projects, Notion, or any visual tracker — the skill works with any |

---

## Key Capabilities

### Core Features

| Capability | How to Trigger | Notes |
|---|---|---|
| **Work decomposition** | Agent breaks a complex goal into parallel tasks automatically | "Don't do the work yourself" rule enforced |
| **Anti-temptation guard** | Prevents orchestrator from diving into execution | Keeps the agent in coordinator role |
| **Parallel task dispatch** | Routes decomposed tasks to subagents | Maximizes throughput on multi-step ops |
| **Status tracking** | Agent maintains Kanban columns: Backlog → In Progress → Review → Done | Works with any board or mental model |

### CLI Command Reference

No CLI commands — this is a behavior-modifying skill. Load it into an orchestrator profile and the agent automatically decomposes work.

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Daily growth sweep** | Decompose into: (1) Reddit mining, (2) HN monitoring, (3) Discord engagement, (4) lead response — run all 4 in parallel |
| **Product launch checklist** | Break into: social posts, email blast, docs update, changelog, competitor monitoring — dispatch each to a subagent |
| **Weekly competitive research** | Parallel tasks: scrape 5 competitor sites, analyze pricing changes, summarize feature updates, draft positioning response |
| **Lead qualification pipeline** | Decompose: email classification → domain research → response drafting → send — each step a separate task |
| **Content calendar execution** | Break monthly calendar into weekly batches, dispatch each week's posts as parallel tasks |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| **Orchestrator agent tries to execute** | Remind: "You're the orchestrator — delegate, don't do." The skill reinforces this. |
| **Subagents return incomplete work** | Add verification step to each task: "Return URL, file path, or HTTP status as proof" |
| **Too many parallel tasks** | Limit to 3 concurrent subagents (config.yaml: `delegation.max_concurrent_children: 3`) |
| **Kanban board out of sync** | Run a sync pass: "Audit all tasks, update board to match reality" |

## Verification

```bash
# Verify skill installed
hermes skills list | grep kanban-orchestrator

# Test decomposition (describe a complex goal to your orchestrator agent)
# Example: "Plan the CorpusIQ June product update. Decompose into parallel tasks."
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 15 Discovery](/hermes/skills/marketplace/new-june15-2026/) →*

*Powered by CorpusIQ*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
