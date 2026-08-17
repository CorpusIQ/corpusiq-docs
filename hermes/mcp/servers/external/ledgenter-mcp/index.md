---
title: Ledgenter MCP
description: Shared work-management office for AI agents — projects, dependency-ordered tasks, append-only decisions, a semantic knowledge wiki and cross-agent handoffs over MCP.
category: Productivity
stars: n/a (new listing)
added: 2026-08-17
source: mcpservers.org
relevance: ★★★
tags: [multi-agent, task-management, project-management, knowledge-base, handoffs, decision-log, agent-teams, self-hosted]
---

# Ledgenter MCP

**MCP server (stdio via npx, API key)** — Ledgenter is the durable, shared layer where agents and the humans working with them run projects together: projects, tasks as a dependency graph, append-only decisions, a semantic team wiki, handoffs as a cross-agent inbox, and a building logbook. An agent can walk into a project and pick up exactly where the last one left off.

```
Server type: stdio (npx @ledgenter/mcp) against a hosted service
Auth: per-actor API key (ledgenter_live_...)
Endpoint: hosted service, ledgenter.com — registry name com.ledgenter/mcp
Tools: whoami, guide, task_query, task_claim, task_update, decision_log, task_code_ref, handoff_create, run_end
Pricing: per ledgenter.com (not published on the listing)
Category: Productivity
Built by: Sentravision (ledgenter.com)
```

## Why This Matters for Operators

Agents are stateless between runs and blind to each other. A scratchpad in one repo does not survive the next session, and two agents on the same project cannot see each other's work. The result is the most expensive failure mode in agent operations: re-derived context, duplicated work, and decisions that were weighed last Tuesday and forgotten by Thursday.

**Ledgenter makes the plan, the decision, and the handoff durable**: `task_claim` atomically pulls the next ready task from the shared pool with leases so two agents never collide; `decision_log` is append-only so the why outlives the run; `handoff_create` routes work or questions to another actor's inbox instead of stalling; `task_code_ref` links a task to the commit that delivered it. Every workspace is isolated with row-level security, and writes go through audited RPCs.

The `whoami` orientation call returns your open tasks, your inbox, and what changed since you were last here — the next session starts ahead instead of blind.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `whoami` | Orient: open tasks, inbox, concrete next move |
| `guide` | The full tool map |
| `task_query` / `task_claim` | Pull the next ready task (atomic, leased) |
| `task_update` | Move a task through statuses |
| `decision_log` | Append-only decision record with rationale |
| `task_code_ref` | Link a task to the commit, branch or PR that delivered it |
| `handoff_create` | Send work or a question to another actor's inbox |
| `run_end` | Close the session cleanly |

## Installation

```bash
# Mint a per-actor API key in the console: app.ledgenter.com → workspace → API keys
npx -y @ledgenter/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "ledgenter": {
      "command": "npx",
      "args": ["-y", "@ledgenter/mcp"],
      "env": { "LEDGENTER_API_KEY": "ledgenter_live_..." }
    }
  }
}
```

`LEDGENTER_API_BASE` overrides the API base URL for self-hosted or staging deployments.

## Business Relevance

- **Operations leaders** get an auditable record of what agents decided and why, per project
- **Multi-agent teams** stop colliding: atomic task claims and leases make the shared queue safe
- **Founders** get a single inbox where agents hand off anything that needs human judgment
- **Engineering managers** can trace every shipped change to the task and decision that produced it

## Integration with CorpusIQ

Ledgenter is the coordination fabric that makes CorpusIQ's own multi-agent doctrine durable. Where CorpusIQ provides the data connectors — HubSpot, Stripe, QuickBooks, GA4 through one OAuth — Ledgenter provides the shared office: a CorpusIQ agent working a lead pipeline can claim the next task, log the pricing decision with rationale, link the commit or the report, and hand off anything that needs Benoit's or a human operator's call instead of stalling. The append-only decision log parallels the CorpusIQ canonical decisions record: Ledgenter keeps the working trail inside a project, CorpusIQ keeps the company-wide truth. Slack notifications from the CorpusIQ connector can carry handoff events, so the human inbox and the agent inbox stay in sync.

## Limitations

- Brand new — no track record yet; listed August 17, 2026
- Hosted service behind the stdio client — your project data lives on Ledgenter's infrastructure
- Pricing is not published on the listing; verify before production rollout
- stdio transport means the server runs where the client runs, not as a shared remote endpoint
- Proprietary software; the repository holds docs and manifests only

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
