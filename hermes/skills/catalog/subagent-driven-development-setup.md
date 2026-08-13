---
title: Subagent-Driven Development — Skill Setup Guide
description: Install and configure subagent-driven-development, the official Hermes Agent skill for dispatching parallel subagents per task with systematic two-stage review — 88 installs.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/subagent-driven-development-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Subagent-Driven Development — Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/subagent-driven-development) (88 installs)
**Category:** Development / Workflow Automation
**License:** MIT · **Platforms:** Linux, macOS, Windows
**Dependencies:** Hermes Agent v0.20.0+, `delegate_task` tool access

Execute implementation plans by dispatching fresh subagents per task with systematic two-stage review. Each task gets a clean context, dedicated subagent, and automated spec-then-quality review between tasks. Ideal for complex multi-file projects where context isolation prevents subtle errors from creeping across task boundaries.

---

## What It Does

| Capability | How |
|-----------|-----|
| **Task dispatch** | Spawns fresh subagents per task — clean context, no pollution |
| **Two-stage review** | Spec compliance check then code quality review |
| **Parallel execution** | Independent tasks run concurrently via delegation |
| **Implementation plans** | Consumes output from the `plan` skill or user requirements |
| **Automated gating** | Failed review blocks next task until fix applied |

---

## How It Works

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Task Plan    │────▶│  Subagent 1  │────▶│ Spec Review  │
│  (from plan)  │     │  (isolated)  │     │   (Gate 1)   │
└──────────────┘     └──────────────┘     └──────┬───────┘
                                                 │ pass
┌──────────────┐     ┌──────────────┐     ┌──────▼───────┐
│  Dispatch 2   │◀────│  Subagent 2  │◀────│ Quality Rev  │
│  (next task)  │     │  (isolated)  │     │   (Gate 2)   │
└──────────────┘     └──────────────┘     └──────────────┘
```

The core principle is fresh subagent per task. Each subagent sees only its own task context — no cross-contamination from prior work. Reviews are automated between tasks so nothing slips through.

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill subagent-driven-development
```

### Direct from Hermes Agent Repo

```bash
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/development/subagent-driven-development ~/.hermes/skills/
```

---

## Prerequisites

1. **Hermes Agent v0.20.0+** — delegation subsystem required
2. **`delegate_task` tool** — must be enabled in your Hermes config
3. **Implementation plan** — from `plan` skill or documented requirements

---

## Basic Usage

Load the skill and trigger with an implementation plan:

```
> Load subagent-driven-development skill
> Here's my plan for the auth refactor:
>   1. Extract token logic to auth.ts
>   2. Add refresh token rotation
>   3. Update API client to use new auth
>   4. Write tests for all flows
> Execute this with subagent-driven-development
```

Hermes will:
1. Parse the plan into discrete tasks
2. Dispatch Task 1 to a fresh subagent
3. Run spec review on Task 1 output
4. Run code quality review on Task 1 output
5. Only proceed to Task 2 after both reviews pass
6. Repeat for all tasks

---

## Configuration

No additional configuration required. The skill uses Hermes' built-in delegation system. For optimal results:

- **Subagent model:** Set `delegation.model` in config.yaml to match your task complexity (Sonnet for routine, Opus for critical)
- **Max concurrent:** Set `delegation.max_concurrent_children` for independent task parallelism
- **Review strictness:** The two-stage review is opinionated — spec compliance then code quality. Adjust by editing the skill's review prompts if needed.

---

## When to Use vs When Not

| ✅ Use When | ❌ Don't Use When |
|------------|------------------|
| Multi-file, multi-task projects | Single file quick fixes |
| Tasks are mostly independent | Tasks have deep sequential dependencies |
| Quality/spec compliance critical | Exploratory/prototype work |
| Want automated review between steps | Tasks under 30 seconds each |

---

## Tips

- **Combine with `plan` skill:** Generate the implementation plan first, then feed it here
- **Review output lives in delegation logs:** Check `~/.hermes/cache/delegation/` for review results
- **Failed reviews produce actionable feedback:** The subagent gets specific fix instructions, not just "failed"
- **For sensitive work:** Use Opus routing for both the dispatcher and subagents

---

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| "No delegation tool" | delegate_task not enabled | `hermes config set delegation.enabled true` |
| Subagent model wrong | Config override | Check `delegation.model` in config.yaml |
| Reviews too strict/lenient | Prompt tuning needed | Edit skill review templates in `~/.hermes/skills/subagent-driven-development/` |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [nousresearch/hermes-agent on skills.sh](https://skills.sh/nousresearch/hermes-agent)*

*Powered by CorpusIQ*
