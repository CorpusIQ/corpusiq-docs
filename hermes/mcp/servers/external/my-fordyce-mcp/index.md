---
title: "My Fordyce MCP - Shared Backlog for Agent Teams"
description: "Remote MCP that puts multiple AI agents on one ticket backlog with leases, heartbeats and evidence, so concurrent work never forks the truth."
category: "Business Operations"
stars: n/a (hosted platform, fordycecg.com)
added: 2026-10-03
source: "mcpservers.org server page (fordycecg-com-products-myfordyce-mcp)"
relevance: ★★★
tags: [project-management, backlog, multi-agent, orchestration, tracking, remote-mcp]
---

# My Fordyce MCP

**Remote MCP server (Streamable HTTP, OAuth or API key)** - My Fordyce is a control plane over a shared backlog, built for the case where more than one AI agent works the same queue. The agent writing code, the one you think out loud with and the one that reviews all connect to `https://myfordyce.fordycecg.com/mcp` and work from a single ticket list, so the work does not fork into three versions of the truth.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in) or API key
Endpoint: https://myfordyce.fordycecg.com/mcp
Tools: Backlog tools incl. request_work, claim, heartbeat, add_evidence, release
Pricing: Fordyce account (see fordycecg.com)
Category: Business Operations
Built by: Fordyce Consulting Group (fordycecg.com)
```

## Why This Matters for Operators

The moment a team runs more than one agent, the hard problem stops being intelligence and becomes coordination: two agents grab the same ticket, one overwrites the other's work, and nobody can tell which attempt is the real one. My Fordyce treats every work hand-out as a lease. One agent gets one ticket, the lease is renewable while it works, and the attempt record survives so the next holder reads what already happened instead of starting over.

**The differentiator is that coordination is built into the protocol, not bolted on.** Concurrency is refused by design: a second claim loses with a 409 that names the current holder, and a write carries the version it read so a concurrent change is rejected with the current value of every field rather than merged by guess. Abandoned and lapsed leases return the ticket to the pool with the attempt attached.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `request_work` | Hands one agent one ready ticket and reserves it, so two agents asking at once get different work |
| `claim` | Takes a specific ticket; exactly one caller wins, the rest get a 409 naming the holder |
| `heartbeat` | Renews the lease while an agent is still working, so a long stretch never costs it the ticket |
| `add_evidence` | Appends what the agent actually did (a note, a branch, test output) so a lapsed lease is not re-run blind |
| `release` | Ends the lease; done sends the work to review, abandon returns it to the pool with the hand-off attached |

Every tool the server exposes is listed in the app, and the client reads the current list when it connects. The full reference is in the Fordyce Help Center.

The ticket lifecycle runs `available → claimed → in_use → awaiting_review → done`, with **abandoned**, **lapsed**, **draft** (fails field gates, not dispatchable) and **duplicate** (near-match filed to a human triage lane) as first-class states.

## Installation

```bash
claude mcp add --transport http my-fordyce \
  https://myfordyce.fordycecg.com/mcp
```

In Claude or Claude Code, add the HTTP server then use `/mcp` to sign in. In ChatGPT, add the URL as a connector and complete the browser sign-in.

## Configuration

```json
{
  "mcpServers": {
    "my-fordyce": {
      "type": "http",
      "url": "https://myfordyce.fordycecg.com/mcp"
    }
  }
}
```

Any client that supports sign-in (OAuth) connects with one URL and a browser sign-in. A client without it connects with an API key and one config block; keys and connection management live under **Connect your agent**, and authorized apps can be reviewed or disconnected under **Connected apps**. Identity is presented, not assumed: `agent_id` is a stable name the agent supplies when claiming work.

## Business Relevance

- **Engineering teams running multiple coding agents** keep them on one backlog so two agents never edit the same ticket.
- **Operators orchestrating a mixed fleet** (a coder, a researcher, a reviewer) share one queue instead of three private lists.
- **Team leads** get review as an explicit state, so agent output lands in a lane a human settles rather than shipping itself.
- **Anyone auditing agent work** reads the attempt record attached to every ticket, which survives an abandoned or lapsed lease.
- **Consultancies and agencies** give each client project a governed queue that shows what was done and by which agent.
