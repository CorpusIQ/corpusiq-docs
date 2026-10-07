---
title: PingRoom MCP - Human Decisions and Notifications for Agents
description: "Hosted MCP server that lets agents reach humans: mobile pings with locations and attachments, tappable questions, approval requests, handoffs and lock-screen live progress. 41 tools confirmed by live probe, OAuth 2.1 with PKCE and dynamic client registration, long-polling inbound channels, and an active official MCP registry entry."
category: Productivity
stars: n/a (hosted; client repo)
added: 2026-09-04
source: "mcp.so GitHub issue #3937"
relevance: ★★★
tags: [human-in-the-loop, approvals, notifications, handoffs, agent-ops, oauth, remote-mcp]
---

# PingRoom MCP

**Remote MCP server (Streamable HTTP)** - the channel between an agent and its human. Agents send pings with locations, links and small attachments, ask tappable questions, request approvals, hand off decisions and drive live progress cards on the human's lock screen. 41 tools confirmed by live probe in this sweep; the catalog surface is open, account operations require OAuth consent.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 with PKCE + dynamic client registration; user consent required for account operations
Endpoint: https://api.pingroom.io/api/agent/mcp
Tools: 41 (live-probed)
Registry: io.pingroom/pingroom (active, official MCP registry)
Client plugins: Claude Code, Grok Build, Cursor, OpenClaw + @pingroom/cli
```

## Why This Matters for Operators

Autonomous agents stall exactly where they need a human: a budget approval, a go/no-go decision, a login only a person can do. PingRoom turns those moments into a protocol instead of a Slack DM guessing game. **An agent requests an approval with tappable options and long-polls for the answer; the human answers from a push notification; the agent resumes with a recorded decision.** Questions, approvals and handoffs all have the same shape: ask, long-poll, receive the chosen option plus the responder's identity.

The live-status surface is the differentiator: agents stream progress to a lock-screen card (iOS Live Activity or Android live update), so long-running jobs stay visible to the operator without any check-in messages. Handoffs verify the recipient's current identity before transferring, and each agent can rotate its public handle as a kill-switch for a leaked one.

## Tools & Capabilities

41 tools live-probed. Core groups:

| Group | Tools |
|---|---|
| Pings | `broadcast`, `list_notifications`, `get_notification`, `wait_for_notification`, `upload_attachment` (about 90 KiB over MCP, Pro), `get_attachment` |
| Questions | `ask_question` (2-4 tappable options), `wait_for_answer`, `get_question`, `list_questions`, `cancel_question`, `wait_for_ack` |
| Approvals | `request_approval`, `wait_for_approval`, `get_approval` |
| Handoffs | `create_handoff` (acknowledgement or tappable question), `wait_for_handoff`, `get_handoff`, `list_handoffs` |
| Live status | `live_status` (start/update/end lock-screen card), `get_live_status` |
| Rooms | `list_rooms`, `get_room`, `create_room`, `create_public_room`, `join_room`, `set_avatar`, `rotate_handle` |
| Webhooks | `list_webhooks`, `create_webhook` (Pro, secret trigger URL), `update_webhook`, `delete_webhook` |
| Quick actions | `list_quick_actions`, `trigger_quick_action`, `update_quick_action`, `update_quick_actions` |

Plus `connection_info` (stable feed link + install URL) and `redeem_code` (Pro/promo code redemption). Free accounts may own up to five rooms.

## Installation

```bash
claude mcp add --transport http pingroom https://api.pingroom.io/api/agent/mcp
```

Then run `/mcp` to complete the OAuth sign-in in the browser. The person authorizing the connection chooses the account and the allowed rooms; the human must also install the PingRoom app and claim the pairing - installation is not consent.

## Configuration

```json
{
  "mcpServers": {
    "pingroom": {
      "url": "https://api.pingroom.io/api/agent/mcp"
    }
  }
}
```

Client plugins are on GitHub (pingroom/skills): `pingroom-mcp` and `pingroom-cli` for Claude Code and Grok Build, a Cursor manifest, and an OpenClaw skill (`@pingroom/pingroom` on ClawHub). The CLI (`@pingroom/cli`) adds shell and CI use: attachments up to 5 MiB and exit-code gates on human answers.

## Business Relevance

- **Agent operations teams** gate deployments, spend and destructive actions on human approval with a recorded trail.
- **Long-running jobs** stream lock-screen progress so operators see state without check-ins.
- **On-call and escalation** use handoffs and questions with expiry instead of unmonitored chat pings.
- **Client onboarding** uses the built-in onboarding question flow when a new human pairs.

## Integration with CorpusIQ

CorpusIQ's governance systems (approval gates, human-in-the-loop workflows) are exactly the pattern PingRoom productizes. A CorpusIQ-connected agent that needs a human decision - approving a report, a spend threshold, a customer escalation - can hand the decision to PingRoom and resume with the recorded answer, keeping the audit trail in one place alongside CorpusIQ's data.

## Limitations

- Hosted server implementation is private; the public repo is client plugins only (0 stars, MIT).
- Account operations require OAuth consent per connection; the catalog surface alone does nothing useful.
- Attachments over MCP are small (about 90 KiB, Pro accounts); larger files go through the CLI path.
- Mobile push requires the human to install the app and claim each pairing.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [Raposa Aval MCP - Human Approval Gates with Audit Chains](/hermes/mcp/servers/external/raposa-aval-mcp)
- [Watchgoose MCP - Cron Monitoring and Failure Forensics for Agents](/hermes/mcp/servers/external/watchgoose-mcp)
