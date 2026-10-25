---
title: "QodFlow MCP - SLA-Clocked Jobs Agents Can Claim"
description: "A kanban with SLA timers where agents claim jobs under a lease, report progress, attach evidence and hand decisions back to a person."
category: Productivity / Operations
stars: n/a (commercial, free tier, npm package)
added: 2026-10-25
source: "mcpservers.org /all p1-6 (night sweep, October 25 2026) + npm package driven locally + live API auth probe"
relevance: ★★
tags: [kanban, sla, operations, task-management, agent-workflow, human-in-the-loop, evidence, scoped-tokens]
---

# QodFlow MCP

**A work queue both sides can be held to.** A kanban board with an SLA clock, exposed to an agent as nineteen tools: list the jobs, claim one under a lease, report progress, attach evidence, and when the answer is a judgement call, ask a person to choose.

```
Server type: Local (stdio) via npm, plus a token-gated REST API
Package:     npx qodflow-mcp  (npm qodflow-mcp 0.1.3)
API base:    https://www.qodflow.com
Auth:        Personal access token, qf_live_… or qf_test_…, scoped and revocable
Tools:       19 at v0.1
Registry:    com.qodflow/qodflow-mcp 0.1.3
Built by:    QodFlow (qodflow.com)
```

## Why This Matters for Operators

Most agent task systems assume the agent is the worker and the human is the requester. Real operations run the other way round: work arrives from customers, it has a deadline somebody promised, and it has to be handed between people and machines without losing the promise.

Three things are needed for that and usually missing. A clock on every item, so a stalled job is visible before the customer calls. Ownership that cannot be double-claimed, so two agents do not work the same ticket. And a clean way for the agent to stop and ask, rather than guess.

QodFlow puts all three in the tool surface. Every job sits in a stage with an SLA attached. `claim_job` takes a lease, so a second agent is refused rather than queued. `request_human_decision` opens a decision with two to six options and the agent waits for the answer. `attach_evidence` and `get_timeline` mean the audit trail is the same object as the work item, not a separate log.

## What It Actually Does

The package was installed and started in this sweep. `npm install qodflow-mcp@0.1.3` succeeded from the public registry, and running the binary exits immediately with `QODFLOW_API_TOKEN env var is required`, which is the honest boundary: the server reads and writes one workspace and will not start without a credential to name it. That means `tools/list` could not be reached without an account, and the tool surface below was read from the shipped bundle rather than from a live handshake. The API itself was probed live: `GET https://www.qodflow.com/api/jobs` with no credential returned HTTP 401 with `{"success":false,"error":{"code":"UNAUTHORIZED","message":"Authentication required. Send Authorization: Bearer … - a team owner creates tokens at Settings → API Keys."}}`, so the endpoint is real, routed and token-gated.

The bundle routes to `/v1/jobs`, `/v1/stages`, `/v1/members`, `/v1/tags` and `/v1/decisions` on `QODFLOW_API_BASE ?? "https://www.qodflow.com"`, which is what makes a self-hosted or regional base URL possible.

| Tool | Scope required | What it does |
|---|---|---|
| `list_jobs` | `jobs:read` | Newest jobs, paginated |
| `list_stages` | `stages:read` | Pipeline stages with order, colour and SLA |
| `list_tags` / `list_members` | `tags:read` / `members:read` | Workspace vocabulary and the people a job can be assigned to |
| `create_job` | `jobs:write` | New job in the first or a named stage |
| `update_job` | `jobs:write` | Title, description, priority, PO number |
| `move_job` | `jobs:write` | Move between stages, which is what stops the SLA clock |
| `assign_job` | `mcp:assign` | Assign to a member, or unassign with null |
| `claim_job` / `release_job` | `mcp:claim` | Atomically claim or release a job under a lease |
| `report_progress` | `mcp:claim` | Append a progress note to the job timeline |
| `request_human_decision` | `mcp:decide` | Ask a person to pick from two to six options; the agent waits |
| `resolve_decision` | `mcp:resolve` | Close the open decision |
| `attach_evidence` | `mcp:evidence` | Attach a note and optional URL as evidence on the job |
| `get_timeline` / `list_decisions` / `list_evidence` | `jobs:read` | Read back what happened, who decided and what proves it |
| `create_tag` | `tags:write` | Create a tag (Premium and above) |
| `update_stage` | `stages:write` | Rename a stage, change its SLA or colour |

Destructive verbs are not exposed over MCP at all, by design: deleting a team, mass moving jobs and the like live behind a typed confirmation in the web interface only. An agent cannot reach them, which is a stronger position than a permission flag.

## Installation

```
claude mcp add qodflow -- npx qodflow-mcp
export QODFLOW_API_TOKEN=qf_live_…
```

Any other client runs `npx qodflow-mcp` as the server command with the token in its environment. In Claude Desktop:

```json
{
  "mcpServers": {
    "qodflow": {
      "command": "npx",
      "args": ["qodflow-mcp"],
      "env": { "QODFLOW_API_TOKEN": "qf_live_xxxxxxxx_xxxxxxxxxxxxxxxxxxxxxxxx" }
    }
  }
}
```

The token is created at Settings → API Keys with only the scopes the agent needs; `jobs:read` plus `stages:read` is enough for a read-only reporter. A token created in test mode carries the `qf_test_` prefix and binds to test-mode Stripe products, which is the right shape for trying an agent against a copy of the board before it touches live work.

## Business Relevance

An operator does not need another task list. They need the promise-keeping part of the business to be machine-readable. An SLA clock that an agent reads is the difference between a status meeting and a query: which jobs will breach today, what is waiting on a person, and which agent claimed what and when.

The evidence channel is the part that maps onto how this catalog thinks about trust. `attach_evidence` puts the artefact on the job, not in a chat transcript, so the answer to "why was this closed" survives the session.

## Integration with CorpusIQ

The pair that matters is ask an assistant, then file the result as a job with a deadline. A question answered against a connected data source becomes a job with an owner and an SLA instead of a paragraph in a chat window. For an operator running several agents, `claim_job` is the concurrency control that prevents the same reconciliation or report being produced twice.

## Limitations

- No live handshake in this sweep. The server refuses to start without a workspace token, so `initialize` and `tools/list` were not executed; the nineteen tool names come from the shipped 0.1.3 bundle and the vendor's documentation. The API's 401 is the evidence that the service is live.
- Version 0.1. A nineteen-tool surface on a young product is a surface that will move.
- One workspace per token, and plan limits apply inside the tools rather than at the door: an over-quota call returns an error whose text carries an `Upgrade:` hint the agent is expected to relay.
- `request_human_decision` is capped at ten a month on the free plan, which is the exact tool an agent needs most, so the free tier is a demonstration rather than a deployment.
- No webhook or subscription surface is exposed over MCP, so an agent polls or is triggered by the operator's own scheduler.
- The class is not empty. The catalog already carries Taskade at 62 tools and Taskfolk at roughly 180 operations, both far broader. QodFlow is catalogued for the one thing they do not carry: an SLA clock with lease-based claiming and a first-class human-decision tool, which is the operating model rather than a feature count.

## FAQ

### Do I need a paid plan?

Not to start. Free is $0, the paid tiers list at $19 and $49 a month, or $9.50 and $24.50 a month billed annually. The free tier caps human-decision requests at ten a month.

### Can the agent delete work?

No. Destructive operations are not in the MCP surface at all; they exist only in the interface behind a typed confirmation.

### What stops two agents doing the same job?

`claim_job` takes a lease. A second claim on a held job is refused instead of queued, and `release_job` returns it.

### Where do the tools run?

Locally. `npx qodflow-mcp` is a stdio server that talks to the QodFlow API, so the agent's environment holds the token and the vendor never holds a model.

## See Also

- [Taskade MCP - Official AI Workspace Connector](/hermes/mcp/servers/external/taskade-mcp/)
- [Taskfolk MCP - Project Management for Teams and AI Agents](/hermes/mcp/servers/external/taskfolk-mcp/)
- [GLP Audit Proxy MCP - Tamper-Evident Tool-Call Trail](/hermes/mcp/servers/external/mcp-glp-audit-proxy/)
