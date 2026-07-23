---
title: Knowledge Work Plugins — Anthropic's Official Productivity Skills for Hermes
description: Data visualization, documentation, code review, dashboards, task management, and memory management from Anthropic. 43K+ combined installs across 6 official Anthropic skills.
---

# Knowledge Work Plugins — Setup Guide

**Source:** [anthropics/knowledge-work-plugins](https://skills.sh/anthropics/knowledge-work-plugins) (43K+ combined installs)
**Category:** Agent Infrastructure / Productivity
**Quality Tier:** 🟢 Production

Anthropic's official knowledge work plugins — a suite of productivity skills for data visualization, technical documentation, code review, dashboard building, task management, and memory management. These are the skills Anthropic ships for Claude's knowledge work capabilities, directly applicable to Hermes agents.

---

## Installation

```bash
npx skills add anthropics/knowledge-work-plugins --skill data-visualization
npx skills add anthropics/knowledge-work-plugins --skill documentation
npx skills add anthropics/knowledge-work-plugins --skill code-review
npx skills add anthropics/knowledge-work-plugins --skill build-dashboard
npx skills add anthropics/knowledge-work-plugins --skill task-management
npx skills add anthropics/knowledge-work-plugins --skill memory-management
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **data-visualization** | 10.1K | Generate charts, graphs, and data stories from raw data |
| **documentation** | 7.5K | Write technical docs, API references, and architecture decisions |
| **code-review** | 7.3K | Structured code review with security, performance, and style checks |
| **build-dashboard** | 6.6K | Build interactive dashboards with real-time data binding |
| **task-management** | 6.0K | Kanban, sprint planning, and task decomposition workflows |
| **memory-management** | 5.9K | Agent memory strategies — what to store, when to retrieve, when to forget |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Data access** | CSV, JSON, or database connection for visualization and dashboards |
| **Code repository** | Git access for code review skill |
| **Project context** | Task descriptions or sprint goals for task management |

---

## Key Capabilities

### Data Visualization
Transform raw datasets into publication-ready charts: line, bar, scatter, heatmap, Sankey, and geospatial. Supports Matplotlib, D3.js, Vega-Lite, and Observable Plot. Auto-detects chart type based on data structure and analysis goal.

### Technical Documentation
Write and maintain technical documentation: API references with OpenAPI, architecture decision records (ADRs), onboarding guides, and changelogs. Enforces consistent voice and structure.

### Code Review (Knowledge Work)
Anthropic's own code review methodology — different from the community `git-pr-reviewer` skill. Focuses on knowledge transfer: explains why patterns work, suggests improvements with rationale, and links to relevant documentation.

### Dashboard Building
Build operational dashboards: KPIs, trend lines, alert thresholds, and drill-down capabilities. Supports React/Vue components or standalone HTML with real-time WebSocket data binding.

### Task Management
Decompose large projects into manageable tasks, estimate complexity, identify dependencies, and track progress. Compatible with Linear, Jira, GitHub Projects, and plain Markdown.

### Memory Management
Strategies for agent memory systems: classification of what to persist (user preferences, project context, learned patterns), retrieval triggers, staleness detection, and compaction policies.

---

## Quick Start

```bash
# Analyze and visualize data
npx skills use anthropics/knowledge-work-plugins@data-visualization

# Write or update documentation
npx skills use anthropics/knowledge-work-plugins@documentation

# Review code with knowledge-transfer mindset
npx skills use anthropics/knowledge-work-plugins@code-review

# Manage complex multi-step tasks
npx skills use anthropics/knowledge-work-plugins@task-management
```

---

## Verification

```bash
npx skills list | grep knowledge-work
```

---

## Notes

- Official Anthropic-maintained skills — highest quality tier
- `code-review` skill complements the community `git-pr-reviewer` (onewave-ai, 239 installs) and `git-pr-review` (sickn33, 34 installs) — use Anthropic's for knowledge transfer, community ones for checklist-driven review
- `memory-management` is particularly valuable for long-running Hermes agents with persistent memory
- `build-dashboard` integrates with the `data-visualization` skill for full data→insight→dashboard pipelines
- Quality tier 🟢 Production: 43K+ combined installs, Anthropic-maintained
