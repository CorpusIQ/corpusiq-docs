---
title: "Knowledge Work Plugins — Anthropic Official Productivity Skills for Hermes"
description: "14 production-grade skills from Anthropic: data viz, docs, code review, dashboards, tasks, memory, Slack, content creation, knowledge synthesis, search"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/knowledge-work-plugins-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Knowledge Work Plugins — Setup Guide

**Source:** [anthropics/knowledge-work-plugins](https://skills.sh/anthropics/knowledge-work-plugins) (66K+ combined installs across 14 skills)
**Category:** Agent Infrastructure / Productivity
**Quality Tier:** 🟢 Production

Anthropic official knowledge work plugins — a comprehensive suite of productivity, communication, research, and knowledge synthesis skills. These are the skills Anthropic ships for Claude knowledge work capabilities, directly applicable to Hermes agents. Updated July 28, 2026 to include 8 newly discovered skills (23.5K additional installs).

---

## Installation

```bash
# Core productivity (6 skills)
npx skills add anthropics/knowledge-work-plugins --skill data-visualization
npx skills add anthropics/knowledge-work-plugins --skill documentation
npx skills add anthropics/knowledge-work-plugins --skill code-review
npx skills add anthropics/knowledge-work-plugins --skill build-dashboard
npx skills add anthropics/knowledge-work-plugins --skill task-management
npx skills add anthropics/knowledge-work-plugins --skill memory-management

# Communication & content (3 skills)
npx skills add anthropics/knowledge-work-plugins --skill slack-messaging
npx skills add anthropics/knowledge-work-plugins --skill slack-search
npx skills add anthropics/knowledge-work-plugins --skill content-creation

# Research & synthesis (2 skills)
npx skills add anthropics/knowledge-work-plugins --skill knowledge-synthesis
npx skills add anthropics/knowledge-work-plugins --skill search-strategy

# Integration & tooling (3 skills)
npx skills add anthropics/knowledge-work-plugins --skill design-mcp-workflow
npx skills add anthropics/knowledge-work-plugins --skill build-zoom-rest-api-app
npx skills add anthropics/knowledge-work-plugins --skill scribe
```

---

## Included Skills

### Core Productivity

| Skill | Installs | Purpose |
|---|---|---|
| **data-visualization** | 10.1K | Generate charts, graphs, and data stories from raw data |
| **documentation** | 7.5K | Write technical docs, API references, and architecture decisions |
| **code-review** | 7.3K | Structured code review with security, performance, and style checks |
| **build-dashboard** | 6.8K | Build interactive dashboards with real-time data binding |
| **task-management** | 6.0K | Kanban, sprint planning, and task decomposition workflows |
| **memory-management** | 6.1K | Agent memory strategies — what to store, when to retrieve, when to forget |

### 🆕 Communication & Content

| Skill | Installs | Purpose |
|---|---|---|
| **content-creation** | 3.9K | Blog posts, emails, landing pages, social — with voice and channel templates |
| **slack-messaging** | 3.2K | Compose formatted Slack messages with mrkdwn, thread etiquette, and tone |
| **slack-search** | 2.5K | Search Slack with modifiers, natural language queries, and source filtering |

### 🆕 Research & Synthesis

| Skill | Installs | Purpose |
|---|---|---|
| **knowledge-synthesis** | 5.2K | Merge overlapping info from multiple sources, deduplicate, and produce unified narratives |
| **search-strategy** | 4.4K | Decompose queries, translate across source-specific syntax, rank results |

### 🆕 Integration & Tooling

| Skill | Installs | Purpose |
|---|---|---|
| **design-mcp-workflow** | 1.5K | Assess MCP fit, design server architecture, and implement MCP integrations |
| **build-zoom-rest-api-app** | 1.4K | Build apps using Zoom REST API — meetings, webinars, recordings, reports |
| **scribe** | 1.4K | Transcribe uploaded/stored media into structured text with timestamps |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Data access** | CSV, JSON, or database connection for visualization and dashboards |
| **Code repository** | Git access for code review skill |
| **Slack workspace** | Slack API token for messaging and search skills |
| **Zoom account** | Zoom OAuth app for REST API skill |

---

## Key Capabilities

### Core Productivity

**Data Visualization:** Transform raw datasets into publication-ready charts: line, bar, scatter, heatmap, Sankey, and geospatial. Supports Matplotlib, D3.js, Vega-Lite, and Observable Plot. Auto-detects chart type based on data structure and analysis goal.

**Technical Documentation:** Write and maintain technical documentation: API references with OpenAPI, architecture decision records (ADRs), onboarding guides, and changelogs. Enforces consistent voice and structure.

**Code Review:** Anthropic own code review methodology — focuses on knowledge transfer: explains why patterns work, suggests improvements with rationale, and links to relevant documentation.

**Dashboard Building:** Build operational dashboards: KPIs, trend lines, alert thresholds, and drill-down capabilities. Supports React/Vue components or standalone HTML with real-time WebSocket data binding.

**Task Management:** Decompose large projects into manageable tasks, estimate complexity, identify dependencies, and track progress. Compatible with Linear, Jira, GitHub Projects, and plain Markdown.

**Memory Management:** Strategies for agent memory systems: classification of what to persist (user preferences, project context, learned patterns), retrieval triggers, staleness detection, and compaction policies.

### 🆕 Communication & Content

**Content Creation:** Multi-channel content templates with platform-specific best practices:
- **Blog posts:** Hook → body → CTA structure, SEO optimization
- **Emails:** Subject lines under 50 chars, preview text, scannable body sections, one CTA per email
- **Landing pages:** Headline (under 10 words), subheadline, hero section, 3-4 value propositions
- **Social media:** Platform-specific formats with voice preservation

**Slack Messaging:** Compose professional Slack messages with correct mrkdwn formatting (`*bold*` not `**bold**`, `<url|text>` not `[text](url)`). Enforces message structure guidelines (lead with the point, keep it short, use line breaks), thread vs. channel etiquette, and tone appropriate to audience.

**Slack Search:** Advanced Slack search with:
- Natural language queries ("What is the deadline for project X?")
- Keyword search with channel/user/date modifiers (`in:#channel`, `from:@user`, `after:`, `before:`)
- Multi-pass strategy: search topic → search people → search specific channels
- Deduplication of results across multiple searches

### 🆕 Research & Synthesis

**Knowledge Synthesis:** Merge overlapping information from multiple sources (chat threads, emails, docs, project trackers) into unified narratives. Deduplicates by content similarity, author, timestamps, and cross-references. Produces single narrative items with full source attribution.

**Search Strategy:** Query decomposition framework — extracts keywords, entities, intent signals, constraints, and negations from user questions. Translates natural language queries into source-specific syntax (Slack modifiers, GitHub search, file system grep patterns). Ranks results by relevance and source authority.

### 🆕 Integration & Tooling

**Design MCP Workflow:** Structured workflow for MCP (Model Context Protocol) design — assesses fit for MCP integration, designs server architecture (resources, tools, prompts), and implements with proper error handling and authentication.

**Build Zoom REST API App:** End-to-end guide for building Zoom REST API applications — covers meetings, webinars, cloud recordings, dashboards/reports, and OAuth authentication flow.

**Scribe:** Media transcription routing guardrail — detects when uploaded or stored media needs transcription, routes to appropriate transcription tooling, and returns structured text output with timestamps.

---

## Quick Start

```bash
# Analyze and visualize data
npx skills use anthropics/knowledge-work-plugins@data-visualization

# Compose a Slack message
npx skills use anthropics/knowledge-work-plugins@slack-messaging

# Synthesize information from multiple sources
npx skills use anthropics/knowledge-work-plugins@knowledge-synthesis

# Design an MCP integration
npx skills use anthropics/knowledge-work-plugins@design-mcp-workflow
```

---

## Verification

```bash
npx skills list | grep knowledge-work
```

---

## Notes

- Official Anthropic-maintained skills — highest quality tier, 🟢 Production
- Updated July 28, 2026: expanded from 6 skills (43K) to 14 skills (66K+) — 8 new skills discovered via skills.sh marketplace sweep
- **New for Hermes agents:** `slack-messaging` and `slack-search` enable Hermes agents to interact professionally in Slack workspaces; `knowledge-synthesis` and `search-strategy` provide research capabilities directly applicable to agent reasoning loops
- `code-review` skill complements the community `git-pr-reviewer` — use Anthropic for knowledge transfer, community ones for checklist-driven review
- `memory-management` is particularly valuable for long-running Hermes agents with persistent memory
- `design-mcp-workflow` is relevant for any Hermes agent building or consuming MCP servers
