---
title: Plan Mode — Hermes Skill Setup Guide
description: Install and configure plan, the official Hermes Agent skill for plan-only execution mode — generates structured markdown plans without executing code — 309 installs.
---

# Plan Mode — Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/plan) (309 installs)
**Category:** Development / Workflow
**License:** MIT · **Platforms:** Linux, macOS, Windows
**Dependencies:** None

Plan Mode switches Hermes into a planning-only execution mode. When active, the agent generates concrete, actionable markdown plans but does NOT implement code, run mutating commands, or perform external actions. Plans are saved to `.hermes/plans/` in the active workspace.

---

## What It Does

| Capability | How |
|-----------|-----|
| **Plan-only mode** | Agent generates plans but does not execute |
| **Structured output** | Plans saved as markdown in `.hermes/plans/` |
| **Read-only inspection** | Agent can inspect repos/context but not modify |
| **Actionable plans** | Concrete steps, not vague descriptions |
| **Workspace integration** | Plans live alongside project code for review |

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill plan
```

### Direct from Hermes Agent Repo

```bash
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/development/plan ~/.hermes/skills/
```

---

## Behavior Rules

When Plan Mode is active:

| Action | Allowed? |
|--------|----------|
| Read files / inspect repos | ✅ Yes |
| Read-only terminal commands | ✅ Yes |
| Implement code | ❌ No |
| Edit project files | ❌ No (except plan file) |
| Run mutating commands | ❌ No |
| Commit / push | ❌ No |
| External API calls | ❌ No |

---

## Usage

### Activating Plan Mode

```
Hermes, plan the refactoring of the authentication module
Hermes, create a plan for adding WebSocket support
Hermes, I need a plan — not execution — for migrating to PostgreSQL
```

### Plan Output Location

Plans are saved to:

```
.hermes/plans/<timestamp>-<plan-name>.md
```

---

## Plan Template

Generated plans follow this structure:

```markdown
# [Plan Title]

## Overview
[One-paragraph summary of the goal]

## Prerequisites
- [Dependency/requirement check]

## Steps
1. [Concrete, actionable step]
2. [Concrete, actionable step]
...

## Risks
- [Identified risk] → [Mitigation]

## Estimated Effort
[Time/complexity estimate]

## Success Criteria
- [Measurable outcome]
```

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.20.0+ |
| Workspace | Must be inside a project directory (for `.hermes/plans/` output) |

---

## Verification

After install, test with:

```
Hermes, plan how to add dark mode support to a React application.
```

The agent should respond with a structured markdown plan but should NOT create any files or run any code.

---

## Pitfalls

- **Not a gate:** Plan Mode is a skill, not a system-level guard. The agent can still execute if the skill is not explicitly invoked.
- **Plan quality varies:** The skill provides structure but plan quality depends on the agent's understanding of the domain.
- **Workspace required:** Plans save to `.hermes/plans/` which requires a project directory context. Outside a workspace, plans are output inline only.
- **One turn only:** Plan mode applies to the current turn. Future turns may execute unless plan mode is re-invoked.

---

**Installed via:** `npx skills add nousresearch/hermes-agent --skill plan`
