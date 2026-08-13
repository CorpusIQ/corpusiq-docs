---
title: Oh-My-Hermes Workflow — Agent Orchestration Framework Setup Guide
description: Install and configure the Oh-My-Hermes workflow framework that provides opinionated patterns for Hermes agent task orchestration, session management, and tool chaining.
publisher: aradotso/hermes-skills
installs: 182
quality_tier: 🔵 Community
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/oh-my-hermes-workflow-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Oh-My-Hermes Workflow — Agent Orchestration Framework Setup Guide

Oh-My-Hermes Workflow is an opinionated workflow framework for Hermes Agent inspired by Oh-My-Zsh. It provides consistent patterns for task orchestration, session lifecycle management, and tool chaining — so every Hermes session follows proven, repeatable workflows.

**Publisher:** [aradotso/hermes-skills](https://github.com/aradotso/hermes-skills)  
**Source:** skills.sh  
**Quality Tier:** 🔵 Community

---

## What It Does

- **Workflow Templates:** Pre-built workflow patterns for common Hermes tasks
- **Session Management:** Structured session lifecycle (init → execute → verify → handoff)
- **Tool Chaining:** Declarative tool pipelines — define input/output contracts between tools
- **Context Preservation:** Automatic context saving and restoration across session boundaries
- **Convention Enforcement:** Ensures consistent patterns across all agent operations

---

## Prerequisites

| Requirement | Check |
|-------------|-------|
| Hermes Agent installed | `hermes --version` |
| Active profile | `hermes profile list` |
| `npx` available | `npx --version` |

---

## Installation

```bash
npx skills add https://github.com/aradotso/hermes-skills --skill oh-my-hermes-workflow
```

Verify:

```bash
hermes skills list | grep oh-my-hermes
```

---

## Built-in Workflow Templates

| Workflow | Trigger | What It Does |
|----------|---------|--------------|
| `session-start` | New session | Pre-flight checks, context recovery, skill loading |
| `task-execute` | Any task | Structured task → verify → report cycle |
| `session-handoff` | Session end | Context save, Honcho + GBrain handoff, cleanup |
| `error-recovery` | Error detected | Diagnostic collection, retry with fallback, escalation |
| `multi-agent-swarm` | Swarm dispatch | Parallel task distribution, result aggregation |
| `daily-briefing` | Morning cron | Overnight digest, priority queue, schedule prep |

---

## Usage

### Activate a Workflow

```bash
hermes skill invoke oh-my-hermes-workflow --workflow session-start
```

### Create a Custom Workflow

Workflows are defined in `~/.hermes/workflows/`:

```yaml
# ~/.hermes/workflows/corpusiq-growth-report.yaml
name: corpusiq-growth-report
description: Daily growth metrics collection and reporting
steps:
  - name: check-email
    tool: terminal
    command: "hermes skill invoke corpusiq-session-start --check-email"
  - name: pull-analytics
    tool: terminal
    command: "hermes skill invoke corpusiq-report-data-extraction"
  - name: social-sweep
    tool: terminal
    command: "hermes skill invoke corpusiq-organic-discovery --sweep"
  - name: generate-report
    tool: terminal
    command: "hermes skill invoke corpusiq-daily-html-reporting"
  - name: push-telegram
    tool: terminal
    command: "hermes skill invoke corpusiq-daily-html-reporting --deliver"
```

Run it:

```bash
hermes skill invoke oh-my-hermes-workflow --workflow corpusiq-growth-report
```

---

## Integration with CorpusIQ

Oh-My-Hermes Workflow is particularly useful for:

- **Standardizing Session Starts:** Replace ad-hoc session initiation with `session-start` template
- **Cron Job Reliability:** Wrap every cron in `task-execute` for automatic error handling
- **Multi-Agent Coordination:** Use `multi-agent-swarm` to parallelize research tasks
- **Session Handoff:** Standardize how sessions save state before shutdown

---

## Verification

```bash
# List available workflows
hermes skill invoke oh-my-hermes-workflow --list

# Run a dry-run
hermes skill invoke oh-my-hermes-workflow --workflow session-start --dry-run

# Check workflow history
hermes skill invoke oh-my-hermes-workflow --history
```

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| "No workflows found" | Workflow directory missing | `mkdir -p ~/.hermes/workflows` |
| Workflow step fails silently | No error handling in step | Add `on_error: continue|retry|abort` to step config |
| Slow execution | Steps running sequentially | Add `parallel: true` to independent steps |

---

## Related Skills

- [Hermes Agent Self-Evolution](/hermes/skills/catalog/hermes-agent-self-evolution-setup/)
- [Blueprint Orchestration](/hermes/skills/catalog/blueprint-orchestration-setup/)
- [CorpusIQ Session Handoff](/hermes/skills/catalog/gbrain-agent-operations-setup)

---

*Discovered July 31, 2026 · Published by aradotso/hermes-skills · 182 installs*
