---
title: "Retasc MCP — Integration Guide"
description: "The issue tracker for AI agents over MCP. Atomic claims, dependency-aware dispatch, parallel swarms, and cross-runtime handoffs for agent orchestration."
category: mcp
tags: [mcp-server, agent-orchestration, task-management, multi-agent, issue-tracker, claude-code, hermes-agent]
last_updated: 2026-07-28
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/retasc-mcp/"
robots: "index,follow"

---

# Retasc MCP — AI Agent Task Orchestration for Hermes Agent

Retasc is the MCP server AI coding agents pull work from. It replaces traditional issue trackers with atomic claims, dependency-aware dispatch, and parallel swarm execution — purpose-built for agentic workflows, not human project management.

## What It Does

Retasc transforms how AI agents consume and complete work:

- **Atomic claims with lease/TTL** — Agents claim individual work items with per-claim tokens and expiration. No double-work, no orphaned tasks.
- **next_batch wave dispatch** — Parallel agent swarms pull the next ready batch based on dependency resolution and effective priority.
- **Dependency-graph scheduling** — Tasks blocked on incomplete dependencies never surface. When a blocker completes, dependents become available automatically.
- **Resumable handoffs** — Any runtime (Claude Code, Codex, Cursor) resumes from the last checkpoint. Cross-runtime handoffs are native, not bolted on.
- **Deadline-aware dispatch** — `dueAt` SLA pressure: a breach outranks an urgent-priority task.
- **Inbound intake webhooks** — GitHub and GitLab issues sync in; done-items sync back to the source.
- **Outbound notifications** — Slack, Discord, and Telegram DMs on done, assigned, review, or canceled.
- **Human principal binding** — Every claim and edit is traceable to the signed-in human who authorized the agent.

### Why It Matters for Operators

If you're running multiple AI agents on a project, traditional issue trackers (Jira, Linear, GitHub Issues) break down. Agents need atomic work claims, not assignment fields. They need dependency-aware dispatch, not manual backlog grooming. Retasc is the first MCP-native work queue built for how agents actually operate.

## Quick Setup

### Prerequisites
- **Retasc account:** Sign up at [retasc.com](https://retasc.com)
- **MCP-compatible client:** Claude Code, Codex, Cursor, or any HTTP MCP client

### Connection Details

| Field | Value |
|-------|-------|
| **Transport** | Streamable HTTP (Remote) |
| **Endpoint** | `https://api.retasc.com/mcp` |
| **Authentication** | API key (generated in Retasc dashboard) |
| **Tools** | 33 (claim, release, complete, next_batch, create_issue, dependencies, notifications, etc.) |

### Add to Hermes Agent

```json
{
  "mcpServers": {
    "retasc": {
      "transport": "http",
      "url": "https://api.retasc.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_RETASC_API_KEY"
      }
    }
  }
}
```

### Claude Code Setup

```bash
claude mcp add retasc --transport http https://api.retasc.com/mcp
# First connection prompts for API key
```

## Key Tools

| Tool | Purpose |
|------|---------|
| `claim_issue` | Atomically claim next available work item with lease TTL |
| `release_issue` | Release a claim (agent blocked, context lost, reprioritized) |
| `complete_issue` | Mark work done; triggers dependency resolution for dependents |
| `next_batch` | Fetch next batch of claimable items based on priority + dependency graph |
| `create_issue` | Create new work items with dependencies, deadlines, and priority |
| `add_dependency` | Link an issue as blocked on another |
| `get_status` | Query current state of any issue or batch |
| `notify` | Send human notifications (Slack, Discord, Telegram) on status changes |

## Use Cases for CorpusIQ

### Agent Swarm Product Development
Feed Retasc with feature specs. Multiple Claude Code agents claim tasks in parallel, each with a lease. When one finishes, its dependents unlock automatically. You review PRs while agents orchestrate themselves.

### Content Pipeline with Deadlines
Create content tasks with `dueAt` timestamps. Retasc's deadline-aware dispatch ensures time-sensitive posts surface above non-urgent work. Agents check `next_batch` and always pull what matters most.

### Cross-runtime Handoffs
Start a research task in Claude Code, checkpoint it. Resume from Codex or Cursor. Retasc handles the context handoff — same claim, same state, different runtime.

## Pricing

- **Free tier:** First $10 of metered usage included
- **Pay-per-action:** After free tier; Retasc reports their own busiest agent runs ~$9/month
- **No per-seat:** Pay for what agents consume, not how many humans have accounts

## Limitations

- **MCP-native only:** No traditional web UI for human task management — this is purpose-built for agents
- **Early stage:** New product, ecosystem integrations growing
- **API key auth:** Not OAuth; key management is manual
- **Dependency on MCP client support:** Requires clients that support Streamable HTTP transport

## Verdict

Retasc is the most significant agent orchestration MCP we've seen this month. It solves the fundamental mismatch between human-centric issue trackers and agent workflows. For operators running multiple AI coding agents, this replaces the Jira/Linear API + custom dispatch scripts pattern with a single MCP endpoint. Strong recommend for any multi-agent workflow.

**Rating: ★★★ — Essential for multi-agent operators**
