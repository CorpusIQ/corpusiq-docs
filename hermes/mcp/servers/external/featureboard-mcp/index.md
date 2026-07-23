---
title: FeatureBoard MCP Server
subtitle: Agentic governance, management, orchestration, task planning for AI agents
source: mcpservers.org
github: https://github.com/valentil/featureboard-mcp
created: 2026-07-22
category: AI Operations
stars: 0
tags: [agent-orchestration, governance, task-management, productivity, ai-operations]
---

# FeatureBoard MCP Server

MCP server for **automatic agentic governance, management, orchestration, task planning, and tracking**. Designed for operators running multiple AI agents — gives you visibility and control over what your agents are doing, planning, and completing.

## What It Does

- **Task Planning** — AI agents can create, assign, and track tasks programmatically
- **Orchestration** — Coordinate work across multiple agents with dependency tracking
- **Governance** — Monitor agent activity, enforce policies, audit decisions
- **Management Dashboard** — Central view of all agent workstreams

## Business Operator Use Cases

| Use Case | Value |
|----------|-------|
| **Multi-Agent Oversight** | "Show me everything the growth agent worked on today" — single dashboard |
| **Task Dependency Management** | "Don't start the email campaign until the landing page is approved" |
| **Agent Audit Trail** | "Why did the pricing agent change our subscription tiers?" → decision history |
| **Workload Balancing** | "Reassign the SEO audit to agent-3 while agent-2 finishes the competitor analysis" |

## Installation

```bash
git clone https://github.com/valentil/featureboard-mcp
cd featureboard-mcp
npm install
```

## Configuration

Add to your MCP client config:

```json
{
  "mcpServers": {
    "featureboard": {
      "command": "node",
      "args": ["path/to/featureboard-mcp/index.js"],
      "env": {
        "FEATUREBOARD_API_KEY": "your-api-key"
      }
    }
  }
}
```

## Tools Provided

- `create_task` — Create new tasks with priority, assignee, and dependencies
- `list_tasks` — Query tasks by status, agent, project
- `update_task` — Change status, reassign, add notes
- `get_audit_log` — Retrieve decision history for governance
- `orchestrate_workflow` — Define multi-step workflows with dependency chains

## Limitations

- **0 stars, brand new** — Created July 22, 2026. Experimental.
- **API key required** — FeatureBoard appears to be a SaaS product requiring an account.
- **Unclear pricing** — No public pricing page found. May be free tier or paid.
- **No agent framework integration yet** — Not yet integrated with popular agent frameworks (CrewAI, AutoGen, etc.).

## Operator Verdict

★★★ **Directly relevant to CorpusIQ's multi-agent architecture.** This is one of the first MCP servers specifically targeting agent governance rather than data access. If FeatureBoard delivers on orchestration + audit trail, it could become the control plane for agent operations. Monitor closely.
