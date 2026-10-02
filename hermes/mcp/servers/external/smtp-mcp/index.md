---
title: "smtp-mcp - Guardrailed Outbound Email over SMTP for Agents"
description: "smtp-mcp is the outbound half of the ni-c email suite: an MCP client can send, reply to and forward mail from one configured address over plain SMTP submission, gated by a required recipient allowlist, a default-off send switch and per-message human approval through MCP elicitation. TypeScript stdio server, MIT."
category: Communication & Email
stars: 0
added: 2026-09-07
source: "chatmcp/mcpso issue #3956"
relevance: ★★★
tags: [email, smtp, outbound, human-approval, allowlist, stdio, communication]
---

# smtp-mcp - Guardrailed Outbound Email over SMTP for Agents

**Local stdio MCP server (TypeScript, MIT)** - smtp-mcp is the deliberately outbound counterpart to imap-mcp: where imap-mcp reads a mailbox and cannot send, smtp-mcp sends, replies and forwards from one configured address over plain SMTP submission, so it works with whatever mail account the operator already has. Because sending is the dangerous direction, the channel is narrowed at four independent points.

```
Server type: Local (stdio, Node.js 22+); Docker image on ghcr.io/ni-c/smtp-mcp
Auth: SMTP account credentials held by the operator; no vendor API
Install: npx @ni-c/smtp-mcp
Tools: 7 ceiling; SMTP_ALLOW_TOOLS=essential registers a curated 5
Pricing: Free software
Category: Communication & Email
Built by: ni-c (github.com/ni-c/smtp-mcp)
```

## Why This Matters for Operators

Inbound agent email is a solved problem; outbound is where the risk concentrates. A model that can send mail can leak, spam or misrepresent the sender. smtp-mcp's design answers each failure mode with a mechanism: sending is off until the operator enables it, every recipient in To, Cc and Bcc must match an explicit allowlist, every message passes a human approval step via MCP elicitation, and the sender address cannot be chosen by the model - so a prompt-injected "send this to a different address" fails before a connection is ever opened.

**The four-point narrowing is the guide's headline: default-off registration, recipient allowlist, per-message human approval, fixed sender. An agent workflow that survives all four is safe by construction, not by prompt discipline.**

## Tools & Capabilities

| Group | What the agent does |
|---|---|
| Sending | Sends, replies to and forwards mail from the configured address |
| Recipient control | Every To, Cc and Bcc address checked against SMTP_ALLOWED_RECIPIENTS before a connection opens |
| Human approval | Each message goes to the client as an MCP elicitation with recipients, subject and Bcc on labelled lines |
| Transport safety | SMTP_TLS=starttls default with mandatory upgrade; stripped STARTTLS fails the connection |

## Installation

```bash
npx @ni-c/smtp-mcp
```

## Configuration

```json
{
  "mcpServers": {
    "smtp": {
      "command": "npx",
      "args": ["@ni-c/smtp-mcp"],
      "env": {
        "SMTP_HOST": "smtp.example.com",
        "SMTP_USER": "ops@example.com",
        "SMTP_ALLOW_SEND": "true",
        "SMTP_ALLOWED_RECIPIENTS": "finance@example.com,founder@example.com"
      }
    }
  }
}
```

Sending tools are not registered at all until SMTP_ALLOW_SEND is set, and SMTP_ALLOWED_RECIPIENTS is required to turn sending on. There is no from parameter by design; the sender is fixed at configuration time.

## Business Relevance

- **Founders** let the agent draft and send routine mail through an approval gate instead of a free hand.
- **Ops teams** pair smtp-mcp with imap-mcp for a full read-and-send mailbox workflow with split credentials.
- **Finance teams** use the allowlist to keep agent mail inside a named recipient circle.
- **Security-conscious teams** get STARTTLS enforcement and a fixed sender as audit properties.

## Integration with CorpusIQ

CorpusIQ reads the business; smtp-mcp speaks on its behalf under supervision. A composed workflow: the agent pulls receivables data from CorpusIQ's Stripe and QuickBooks connectors, drafts a payment reminder, and smtp-mcp routes it to the allowlisted finance recipient only after the human approves the elicitation.

## Limitations

- Brand new listing (issue #3956, Sep 5, 2026); repo and package are days old (0 stars).
- One configured sender address per server instance.
- Human approval requires a client that supports MCP elicitation.
- SMTP submission only; no calendar or contact tools (see the sibling caldav-mcp and carddav-mcp).

## See Also

- [imap-mcp - Read-Only IMAP Mailbox Operations for Agents](/hermes/mcp/servers/external/imap-mcp)
- [AssistantMail MCP - Managed Mailboxes for AI Agents](/hermes/mcp/servers/external/assistantmail-mcp)
- [BusyMail MCP - Human-Approval Email over MCP](/hermes/mcp/servers/external/busymail-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
