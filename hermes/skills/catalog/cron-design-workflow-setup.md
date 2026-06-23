---
title: Cron Design Workflow Setup Guide
description: Deploy a reusable Hermes Agent skill for designing cron jobs, scheduled automations, and recurring alerts — Context → Office Hour → Brainstorming → Grill Me → Docs → Execute
---

# Cron Design Workflow

**Source:** [lovenps85/hermes-cron-design-workflow-skill](https://github.com/lovenps85/hermes-cron-design-workflow-skill)
**Stars:** 0 ⭐ | **License:** MIT
**Created:** June 23, 2026

## Overview

A reusable workflow for designing and improving Hermes Agent cron jobs, scheduled automations, and recurring alerts. Adapts battle-tested patterns from Superpowers (brainstorming, writing-plans), Matt Pocock (grill-me, domain-modeling), and GSTACK (office-hours) into a structured 6-phase pipeline.

## Workflow

```
Context → Office Hour → Brainstorming → Grill Me → Docs → Execute / Verify
```

### Phase 1: Context
Agent gathers current state — existing crons, schedule conflicts, resource usage, failure history. No design yet; just data.

### Phase 2: Office Hour
Structured Q&A session. Agent asks clarifying questions about the cron's purpose, frequency, failure tolerance, notification targets, and dependencies.

### Phase 3: Brainstorming
Agent proposes 3-5 design options with trade-offs: schedule variants, error handling strategies, notification routing, and resource budgets.

### Phase 4: Grill Me
Adversarial review of the chosen design. Agent stress-tests: "What if the API is down?" "What if the previous run is still executing?" "What happens at DST boundary?"

### Phase 5: Docs
Agent generates: cron command, schedule rationale, failure modes, rollback plan, and monitoring checklist.

### Phase 6: Execute / Verify
Agent creates the cron, runs it once dry, verifies output, and confirms delivery to notification targets.

## Prerequisites

- Hermes Agent with cron management (`hermes cron create/list/logs`)
- Access to target notification channels (Telegram, email, etc.)
- Understanding of the task being automated

## Installation

```bash
git clone https://github.com/lovenps85/hermes-cron-design-workflow-skill.git
mkdir -p ~/.hermes/skills/devops
cp -a hermes-cron-design-workflow-skill/cron-design-workflow ~/.hermes/skills/devops/
```

Load the skill in a Hermes session:

```bash
hermes -s cron-design-workflow
```

Or invoke from within an active session:

```
/skill cron-design-workflow
```

## CLI Reference

```bash
# Start a new cron design session
hermes -s cron-design-workflow "design a daily report cron at 6 PM"

# Review an existing cron
hermes -s cron-design-workflow "audit the skills-monitor cron"

# Skip to a specific phase
hermes -s cron-design-workflow "grill-me on the video generation cron"
```

## Capabilities

| Phase | Tool Support | Output |
|-------|-------------|--------|
| Context | `hermes cron list`, `hermes cron logs`, system resource check | Current state report |
| Office Hour | Structured Q&A template | Clarified requirements doc |
| Brainstorming | Design pattern library from Superpowers + Matt Pocock | 3-5 options with trade-offs |
| Grill Me | Failure mode catalog, edge case library | Risk assessment + mitigations |
| Docs | Auto-generated from design decisions | Cron spec + runbook |
| Execute | `hermes cron create`, dry-run, verification | Live cron + delivery confirmation |

## CorpusIQ Use Cases

| Use Case | Why This Workflow |
|----------|-------------------|
| **New Daily Report Cron** | Ensures 6 PM delivery with fallback, verification, and Telegram delivery confirmation |
| **Skills Sweep Automation** | Designs for API failures, rate limits, concurrent-run prevention, and catalog update conflicts |
| **Video Generation Pipeline** | Handles HeyGen API timeouts, queue management, and multi-platform posting verification |
| **Email Monitor Refactoring** | Optimizes polling intervals, dual-account handling, and token refresh failure modes |
| **Platform Comment Checking** | Designs for per-platform rate limits, session expiry, and fallback paths |

## Troubleshooting

### Skill not found

```bash
# Verify installation
ls ~/.hermes/skills/devops/cron-design-workflow/

# If missing, re-clone
git clone https://github.com/lovenps85/hermes-cron-design-workflow-skill.git /tmp/cdw
cp -a /tmp/cdw/cron-design-workflow ~/.hermes/skills/devops/
```

### "Grill Me" phase produces too many edge cases

The adversarial review is intentionally thorough. Focus on the top 5 highest-impact failure modes and defer the rest to the Docs phase as "known limitations."

### Cron verification fails on first run

Common causes: environment variables not set in cron context, working directory mismatch, or Python path issues. The Docs phase generates a `cron.env` file — ensure it's sourced in the cron command.

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace Home](/hermes/skills/marketplace/) →*
