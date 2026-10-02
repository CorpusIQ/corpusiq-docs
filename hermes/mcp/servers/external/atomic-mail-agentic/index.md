---
title: "Atomic Mail MCP - Programmable Inbox for AI Agents"
description: "Programmable email inbox platform for AI agents: JMAP-based stdio MCP server with hands-free proof-of-work signup, custom-domain sending behind a human dashboard control plane, and a 255-star MIT repo; agents read, send and react to email autonomously."
category: Communication & Email
stars: "255 (Atomic-Mail/atomic-mail-agentic)"
added: 2026-08-31
source: "mcpservers.org /all page 1 (Aug 31 afternoon catch-up sweep)"
relevance: ★★
tags: [mcp-server, email, jmap, inbox, automation, stdio, agents]
---

# Atomic Mail MCP

**A programmable email inbox built for agents, not humans clicking through setup.** Atomic Mail gives an agent its own mailbox - register an `@atomicmail.ai` address hands-free through proof-of-work signup, send and receive mail, and keep threads going - through a local stdio MCP proxy that speaks JMAP. For company domains, a human dashboard acts as the control plane: verify `support@yourcompany.com` once, and the agent sends with a domain-aligned From address from then on.

```
Server type: Local stdio proxy (npx) over a hosted JMAP backend
Package: @atomicmail/mcp-github (npm, v0.3.26)
Registry: "Atomic Mail" on registry.modelcontextprotocol.io (v0.3.14)
Repo: github.com/Atomic-Mail/atomic-mail-agentic (MIT, 255 stars)
Website: atomicmail.ai · Dashboard: dashboard.atomicmail.ai
Auth: Proof-of-work signup for default inboxes; API key or OAuth for custom domains
Transport: JMAP under the hood; embedded docs and presets ship with the CLI
```

## Why This Matters for Operators

The standard email-assistant failure mode is the assistant touching your personal mailbox. Atomic Mail inverts it: the agent gets its own inbox and the operator stays out of the blast radius.

First, **dedicated agent inboxes isolate risk.** Newsletter digests, outbound campaigns and survey follow-ups run from an `@atomicmail.ai` address, never the operator's personal mail, and inbound mail is treated as untrusted input by design.

Second, **custom domains keep the operator in control.** Sending from your own domain requires a human to add and verify DNS records in the dashboard - a deliberate control plane separated from the agent flow - after which each inbox gets its own API key with domain-aligned sending.

Third, **the agent owns the workflow end to end.** The platform is designed to be driven by an agent: describe a workflow in plain language, and the agent registers the inbox, sends, receives and keeps the thread going. A `help` tool ships embedded docs, presets and troubleshooting.

## Tools and Capabilities

The MCP surface is JMAP-shaped with bundled presets:

| Capability | What the agent can do |
|-----------|-----------------------|
| `jmap_request` | Full JMAP request surface with bundled JSON presets for common operations |
| `list_inbox` | List mailbox contents via the standard preset flow |
| `send_mail` | Send from the agent's inbox (or a domain-aligned address after dashboard setup) |
| `help` | Embedded docs, presets, cron guidance and troubleshooting hints |

Example workflows from the project: a newsletter digest inbox that subscribes, reads and summarizes; a support inbox that replies from your docs and escalates only when it cannot answer; an interview survey inbox that sends questions and tracks responses.

## Installation

```bash
npx -y @atomicmail/mcp-github
```

MCP host config:

```json
{
  "mcpServers": {
    "atomicmail": {
      "command": "npx",
      "args": ["-y", "@atomicmail/mcp-github"]
    }
  }
}
```

A ready prompt for any agent is published at atomicmail.ai; ClawHub and Hermes skill installs are also available.

## Configuration

Default inboxes are created hands-free through proof-of-work signup during the agent's first session. For custom domains: add and verify the domain in the dashboard (TXT ownership plus MX records), create an inbox, then connect with its API key (`atomicmail register --api-key`) or OAuth. Local credentials are written with mode 0600; the project recommends installing only from the `@atomicmail` npm scope.

## Business Relevance

- **Support teams** hand a dedicated inbox to an agent that answers from documentation and escalates edge cases.
- **Marketing operators** run newsletter digests and survey outreach from disposable agent inboxes.
- **Companies with domain reputation concerns** keep agent mail on domain-aligned addresses with a human-controlled DNS gate.

## Integration with CorpusIQ

Atomic Mail and CorpusIQ occupy complementary halves of email operations. CorpusIQ's Gmail connectors read business inboxes and feed CRM and analytics pipelines with cited data, while Atomic Mail gives agents their own sending and receiving surface for outbound workflows like surveys and digests. An operator can run both: CorpusIQ monitors and measures, Atomic Mail executes the conversational outbound loop - with the domain control plane keeping the sending identity under human governance.

## Limitations

- stdio transport only for MCP; a REST API exists for custom connectors and advanced logic.
- No built-in approval queue: an agent with send permission can send, so scope inboxes and keys per workflow (BusyMail's human-approval model is the stricter alternative).
- Default inboxes live on @atomicmail.ai; custom-domain sending requires the dashboard setup with DNS changes.
- Catch-up cataloguing: the project has been live since May 2026; this guide reflects v0.3.x.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [BusyMail MCP - Human-Approval Email over MCP](/hermes/mcp/servers/external/busymail-mcp)
- [imap-mcp - Read-Only IMAP Mailbox Operations for Agents](/hermes/mcp/servers/external/imap-mcp)
