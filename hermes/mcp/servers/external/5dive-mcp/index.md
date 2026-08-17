---
title: 5dive MCP
description: Agent-fleet operations over MCP — file tasks, message agents and read daily digests from a fleet of autonomous coding agents through the 5dive CLI.
category: Development
stars: n/a (new listing)
added: 2026-08-17
source: mcpservers.org
relevance: ★★
tags: [agent-fleet, coding-agents, task-queue, agent-ops, digests, cli-adapter, node, self-hosted]
---

# 5dive MCP

**MCP server (stdio, local CLI adapter)** — exposes the 5dive agent-fleet CLI as MCP tools: file tasks in the shared queue, inspect and message agents, and read the fleet's daily standup digest, directly from inside a model context. 5dive itself is the CLI plus control plane for running a fleet of autonomous coding agents as a self-governing company.

```
Server type: stdio (npx @5dive/mcp)
Auth: inherited from the local 5dive CLI (no secrets handled by the server)
Endpoint: local — requires the 5dive CLI on PATH
Tools: 6 (task_create, task_show, task_list, agent_send, agent_list, digest_get)
Pricing: free package (MIT); 5dive platform per 5dive.ai
Category: Development
Built by: 5dive AI (5dive.ai) — npm @5dive/mcp
```

## Why This Matters for Operators

Running a fleet of coding agents means someone has to run the fleet: queueing work, checking who is alive, reading what got done, and getting messages between agents. That operator role is exactly what this server hands to an MCP client.

**The design is an honest adapter**: every tool shells out to the local `5dive` binary's machine-readable `--json` surface and returns the result, so the server inherits the CLI's auth, permissions, and audit log for free and never handles secrets itself. Arguments are passed as an argv array with no shell, so tool input can never be interpreted as shell syntax. `task_list` filters by status or assignee, `agent_list` shows every agent's type, channels, model, and live state, and `digest_get` returns the fleet standup for the day or the week.

## Tools & Capabilities

| Tool | Wraps | Purpose |
|---|---|---|
| `task_create` | `5dive task add` | File a task in the shared queue (title, body, priority, assignee, parent) |
| `task_show` | `5dive task show` | Full detail for one task — status, body, result, subtasks, blockers |
| `task_list` | `5dive task ls` | List tasks, open by default, filterable by status or assignee |
| `agent_send` | `5dive agent send` | Message another agent on the fleet |
| `agent_list` | `5dive agent list` | Every agent: type, channels, model, live state |
| `digest_get` | `5dive digest` | Daily standup digest; `window: "7d"` for the weekly view |

## Installation

```bash
# 1. Install the 5dive CLI (Node 18+)
curl https://install.5dive.ai | sudo bash

# 2. Run the MCP server
npx @5dive/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "5dive": {
      "command": "npx",
      "args": ["-y", "@5dive/mcp"],
      "env": { "FIVEDIVE_SUDO": "1" }
    }
  }
}
```

`FIVEDIVE_SUDO=1` prefixes calls with sudo for managed boxes that require root; `FIVEDIVE_BIN` overrides the binary path; `FIVEDIVE_TIMEOUT_MS` sets the per-call timeout (default 30s).

## Business Relevance

- **Agent-fleet operators** get task filing, agent status, and digests from any MCP client
- **Engineering leads** can read the daily standup without opening a dashboard
- **Multi-agent teams** get a message path between agents through the CLI's own channels
- **Dev-ops builders** get a CLI-scoped adapter that inherits audit logging for free

## Integration with CorpusIQ

5dive composes with the CorpusIQ multi-agent operations stack as the fleet-work surface. Ledgenter holds the shared project office; 5dive runs the coding fleet — an operator agent working through the CorpusIQ connectors can file a 5dive task for the build work, read the digest to see what shipped, and log the outcome in Ledgenter with the decision trail intact. CorpusIQ Slack notifications can carry the digest summary to the human channel, so the fleet's standup reaches the team that funds it. The pattern is the CorpusIQ doctrine at the code level: the agent proposes the task, the CLI's permissions decide what runs, and the audit log records what happened.

## Limitations

- Brand new — no track record yet; listed August 17, 2026
- Requires the 5dive CLI installed and authenticated on the same box — no remote fleet control
- Curated slice of the CLI surface (tasks, agents, digest) — full CLI still needed for the rest
- stdio only — no hosted endpoint; the client launches the process
- Fleet value depends entirely on the 5dive platform's own capabilities

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
