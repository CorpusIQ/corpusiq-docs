---
title: Ruflo — Multi-Agent Orchestration Platform for Hermes Agents
description: Install and configure Ruflo (65K+ GitHub stars), the leading agent meta-harness with native Hermes support, 314+ MCP tools, 30+ plugins, and 267 skills for multi-agent swarms, memory, intelligence pipelines, and autonomous workflows.
---

# Ruflo — Setup Guide

**Source:** [ruvnet/ruflo](https://skills.sh/ruvnet/ruflo) (5.8K+ combined installs across skills)
**GitHub:** [ruvnet/ruflo](https://github.com/ruvnet/ruflo) — 65,762 ★ | MIT License | TypeScript
**Category:** Agent Infrastructure / Orchestration
**Quality Tier:** 🟢 Production (65K+ GitHub stars, v3.31.0 stable, active development)

Ruflo is the leading agent meta-harness — a cross-agent orchestration layer that works natively with **Hermes**, Claude Code, Codex, Cursor, Copilot, Gemini, Amp, and 12+ other coding agents. It ships as three npm packages and provides 314+ MCP tools for memory (HNSW vector search), multi-agent swarms (hierarchical/mesh with anti-drift), task lifecycle management, self-learning intelligence pipelines, hooks, routing, and 30+ optional plugins. With 65,762 GitHub stars and active development (822 open issues as of July 2026), it's the most popular agent orchestration framework in the ecosystem.

---

## Installation

### Via skills.sh (Recommended)

```bash
# Core ruflo skill only
npx skills add ruvnet/ruflo --skill ruflo --yes

# Full catalog — 267 skills across all 30+ plugins
npx skills add ruvnet/ruflo --all
```

### Via npm

```bash
npm install -g ruflo
# or
npm install -g @claude-flow/cli
```

### Initialize in a Project

```bash
# In your Hermes project root:
npx ruflo init

# Creates .claude/ directory, MCP config, hooks, and memory backend
# Auto-detects which agent you're using (Hermes, Codex, Claude Code, etc.)
```

---

## Included Skills (Core)

| Skill | Installs | Purpose |
|---|---|---|
| **ruflo** | 2.0K | Core orchestration — swarms, memory, hooks, task lifecycle |
| **agent-workflow** | 1.3K | Multi-agent workflow coordination with hierarchical swarms |
| **security-audit** | 1.2K | Codebase security scans, CVE checks, adversarial testing |
| **workflow-automation** | 1.2K | Custom multi-step pipeline execution |
| **memory-management** | 1.1K | HNSW-indexed semantic search, hybrid SQLite+AgentDB backend |

## 30+ Plugins (Highlights)

| Plugin | Purpose |
|---|---|
| `ruflo-goals` | Deep research + goal-oriented action planning |
| `ruflo-cost-tracker` | Session cost telemetry, budgets, burn tracking |
| `ruflo-metaharness` | Harness scoring, MCP security scans, red/blue testing |
| `ruflo-browser` | Session-recorded browser automation with RVF replay |
| `ruflo-jujutsu` | Git diff risk analysis + PR lifecycle management |
| `ruflo-security-audit` | Codebase scans + CVE vulnerability checks |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | 20+ (verified by `npx ruflo doctor`) |
| **npm** | 9+ |
| **MCP Server** | Auto-configured by `npx ruflo init` |
| **API Keys** | Model provider keys as needed (Anthropic, OpenAI, etc.) |

---

## Key Capabilities

### 1. Multi-Agent Swarms

Ruflo enables coordinated multi-agent execution with two topology modes:

- **Hierarchical** — orchestrator spawns and manages worker agents with anti-drift coordination
- **Mesh** — peer-to-peer agent communication with distributed task routing

```bash
# Initialize a swarm in the current project
npx ruflo init

# Spawn specialized agents via MCP
# mcp__claude-flow__agent_spawn — 55+ agent types (coder, reviewer, tester, security-architect, etc.)
```

### 2. Persistent Memory (HNSW Vector Search)

- Hybrid backend: SQLite + AgentDB
- HNSW-indexed semantic search across sessions
- Survives context window resets and model switches

```bash
# Store → Search → Retrieve pattern
# mcp__claude-flow__memory_store
# mcp__claude-flow__memory_search
# mcp__claude-flow__memory_retrieve
```

### 3. Self-Learning Intelligence Pipeline

4-step pipeline that runs continuously:

```
RETRIEVE → JUDGE → DISTILL → CONSOLIDATE
```

Captures patterns, learns from decisions, and improves agent selection over time.

### 4. Hooks & Observability

- Pre/post-edit hooks
- Session lifecycle events
- 12 built-in background workers
- Pattern-based agent selection
- 3-tier model routing (deterministic → Haiku → Sonnet/Opus)

### 5. Task Lifecycle Management

```bash
# mcp__claude-flow__task_create
# mcp__claude-flow__task_assign
# mcp__claude-flow__task_complete
# mcp__claude-flow__task_summary
```

---

## Quick Start

```bash
# 1. Install globally
npm install -g ruflo

# 2. Initialize in your project
cd ~/your-hermes-project
npx ruflo init

# 3. Health check
npx ruflo doctor --fix

# 4. Discover matching plugins
npx ruflo discover-plugins

# 5. List all available MCP tools
npx ruflo mcp list

# 6. Check available plugins
npx ruflo plugins list
```

---

## Verification

```bash
# Check version
npx ruflo --version
# Expected: 3.31.0+

# Health check
npx ruflo doctor

# Verify MCP tools registered
npx ruflo mcp list | head -20

# Check skills.sh install
npx skills list | grep ruflo
```

---

## Hermes Integration Notes

- Ruflo auto-detects Hermes during `npx ruflo init` and configures MCP accordingly
- All 314+ MCP tools become available in Hermes as `mcp__claude-flow__*`
- Memory persistence survives Hermes context window resets
- SPARC methodology support for complex multi-step workflows
- GAIA benchmark runs for agent evaluation

---

## Notes

- **Production-grade**: 65K GitHub stars, MIT license, v3.31.0 stable — not experimental
- **Active**: 822 open issues indicates heavy usage and rapid iteration
- **Cross-agent**: Works with 15+ coding agents, not locked to any single ecosystem
- **When NOT to use**: One-shot edits, simple bug fixes, single-agent tasks — the orchestration overhead isn't worth it for simple work
- **Full docs**: [github.com/ruvnet/ruflo](https://github.com/ruvnet/ruflo)
- **Related**: See also [Hermes Agent Setup](/hermes/skills/catalog/hermes-agent-setup/) for native Hermes orchestration
