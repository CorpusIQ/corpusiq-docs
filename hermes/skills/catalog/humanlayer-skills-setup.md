---
title: HumanLayer Skills — Human-in-the-Loop Patterns Setup Guide for Hermes Agents
description: Install the humanlayer/skills cluster (2.7K installs, 5 skills) — show-me, improve-claude-md, design-control-loop, build-iterated-agentic-loop for building agent systems with human approval gates.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/humanlayer-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# HumanLayer Skills — Setup Guide

**Source:** [humanlayer/skills](https://www.skills.sh/humanlayer/skills) (5 skills · 2.7K combined installs)
**Repo:** [github.com/humanlayer/skills](https://github.com/humanlayer/skills)
**Category:** Agent Infrastructure / Human-in-the-Loop
**First Seen:** August 13, 2026
**Quality Tier:** 🟡 Beta core (`show-me` at 2.0K installs, trending on the hot leaderboard)

HumanLayer is one of the leading human-in-the-loop (HITL) tooling companies, and this skill pack encodes their patterns for designing agent systems where humans approve critical actions. `show-me` teaches agents to render work for human review; `design-control-loop` and `build-iterated-agentic-loop` encode the architecture patterns behind approval gates. Directly relevant to governance-layer design for multi-agent deployments.

---

## Installation

```bash
# Full cluster
npx skills add humanlayer/skills

# Hermes: install individual skills by identifier
hermes skills install humanlayer/skills/show-me
hermes skills install humanlayer/skills/design-control-loop
```

---

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| `show-me` | 2.0K | Rendering agent work for human review and approval |
| `improve-claude-md` | 491 | Improving agent memory/context files |
| `design-control-loop` | 92 | Designing human approval loops around agent actions |
| `build-iterated-agentic-loop` | 74 | Building iterated agent execution with checkpoints |
| `narrow-react-prop-types` | 45 | Tightening React props for HITL UI components |

---

## Prerequisites

| Requirement | Details |
|---|---|
| Any agent runtime | Patterns are framework-agnostic |
| Node.js + npx | For the skills.sh CLI install path |
| An approval UI or channel | HumanLayer SDK, Slack, or custom review surface |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Commander approval gates** | `design-control-loop` patterns for the submit() review cycle |
| **Customer deployments** | HITL review surfaces for client Hermes installations |
| **Audit trails** | Human approval points as governance evidence |

---

## Limitations / Verification

- Cluster is small and beta-tier overall — `show-me` is the proven core
- HITL design needs a review surface to be meaningful; the skill supplies the pattern, not the UI
- Verify install: `npx skills list | grep -E 'show-me|control-loop'`

---

## Related

- [Agent Infrastructure category](/hermes/skills/catalog/)
- [Skills Catalog](/hermes/skills/catalog/)
