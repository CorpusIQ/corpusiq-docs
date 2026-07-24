---
name: "TaskerArmy Agent MCP"
description: "Check pending Shopify theme optimization tasks from AI agents"
category: "Development"
source: "mcpservers.org"
discovered: "2026-07-23"
verified: true
remote_endpoint: "https://dashboard.taskerarmy.com/mcp"
---

# TaskerArmy Agent MCP — Shopify Optimization Tasks

TaskerArmy Agent is a remote MCP server that connects AI assistants to TaskerArmy's Shopify theme optimization platform. Agents can query pending tasks, check optimization status, and manage ecommerce workflows.

## What It Does

- **Task visibility** — Query what Shopify theme optimization tasks are pending on your store
- **Status tracking** — Check completion status of optimization jobs
- **Agent-driven workflows** — AI agents can identify, prioritize, and track optimization work
- **Remote endpoint** — No local install; connects over HTTP

## Quick Start

```bash
# Add to Hermes Agent
hermes mcp add taskerarmy --url https://dashboard.taskerarmy.com/mcp

# Or Claude Code
claude mcp add taskerarmy --url https://dashboard.taskerarmy.com/mcp
```

**Prerequisites:** A TaskerArmy account (taskerarmy.com). The MCP endpoint uses your account's authentication.

## Key Tools

| Tool | Description |
|------|-------------|
| `get_pending_tasks` | List all pending optimization tasks for your store |
| `get_task_status` | Check status of a specific task |
| `get_store_health` | Overview of store optimization health score |
| `prioritize_tasks` | Reorder tasks by impact/urgency |

## Use Cases

- **Daily store check** — Agent checks pending tasks each morning and reports to Slack
- **Optimization pipeline** — Agent identifies highest-impact tasks → delegates to developers → tracks completion
- **Ecommerce monitoring** — Agent monitors store health score and alerts on degradation
- **Multi-store management** — Agency manages optimization tasks across multiple client stores

## Hermes Agent Integration

```python
# Agent checks store status
tasks = mcp_taskerarmy_get_pending_tasks(store="my-store")
health = mcp_taskerarmy_get_store_health(store="my-store")
for task in tasks:
    if task.priority == "high":
        print(f"⚠️ High priority: {task.title} — impact: {task.estimated_impact}")
```

---

*Discovered via [mcpservers.org](https://mcpservers.org) sweep. Listed in the [CorpusIQ MCP Catalog](https://corpusiq-docs/hermes/mcp/).*
