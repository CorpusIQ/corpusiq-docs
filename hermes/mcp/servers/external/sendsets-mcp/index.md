---
title: Sendsets MCP - Programmable Cold Email for AI Agents
description: "Sendsets gives agents programmable cold email: warm mailboxes, launch campaigns, manage leads and answer replies behind a policy engine."
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-09-27
source: "mcpservers.org + github.com/AddisonHoff/sendsets"
relevance: ★★★
tags: [cold-email, mailbox-warmup, email-campaigns, deliverability, lead-management, reply-triage, oauth, remote-mcp]
---

# Sendsets MCP

**A cold email service built API-first for agents, with an approval layer operators can trust.** Sendsets exposes a remote MCP server at `https://api.sendsetsapi.com/v1/mcp` plus a CLI and REST API over the same service layer. Agents connect sending mailboxes, warm them up, build and launch outbound campaigns, add leads, and read and answer replies. Every send-class action passes a credential-bound policy and returns `executed`, `awaiting_approval` (a person approves in the dashboard within 30 minutes) or `blocked`, and approval can never override a missing opt-out, a suppression or a mailbox health check.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (RFC 9728 metadata, dynamic client registration) or ssk_ API key
Endpoint: https://api.sendsetsapi.com/v1/mcp
Tools: campaigns, leads, mailboxes, inbox, runs, suppressions, analytics
Pricing: free for up to 10 mailboxes
Category: Sales & Outreach / Cold Email
Built by: Sendsets (sendsetsapi.com; repo github.com/AddisonHoff/sendsets)
```

## Why This Matters for Operators

Cold email tooling usually forces a choice: a dashboard you babysit, or an API with no guardrails. Sendsets splits the difference. The agent does the mechanical work, and the policy engine enforces the invariants that keep domains alive, opt-outs honored, suppressions respected and mailbox health checked before any send.

The run model is the second operator win: campaigns launch through durable, idempotent, preflighted runs (`create_run`, `get_run`, `list_runs`, `cancel_run`), so a retried request cannot double-send, and a campaign can be stopped cleanly mid-flight.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Campaigns | Draft, edit sequence steps, pick sender mailboxes, start and stop |
| Leads | Add, search, tag, bulk edit, manage segments and timelines |
| Mailboxes | Connect, inspect, adjust limits, toggle warmup, check warmup standing |
| Inbox | List and read threads, draft and send replies, label and snooze |
| Runs | Durable, idempotent, preflighted campaign runs |
| Suppressions | Manage the do-not-contact list |
| Analytics | Read dashboard analytics and manage signed webhooks |

## Installation

```bash
claude mcp add --transport http sendsets https://api.sendsetsapi.com/v1/mcp
```

A Claude Code plugin installs the server plus bundled agent skills together via the plugin marketplace (`AddisonHoff/sendsets`). Claude desktop and claude.ai users add the URL under Settings > Connectors.

## Configuration

```json
{
  "mcpServers": {
    "sendsets": {
      "type": "http",
      "url": "https://api.sendsetsapi.com/v1/mcp"
    }
  }
}
```

OAuth clients register dynamically and sign in through the browser with no key to paste; a static `ssk_` key from the dashboard works for scripts and key-only clients.

## Business Relevance

- **Founders** get a cold email stack with a free tier of up to 10 mailboxes
- **SDR teams** get replies triaged and drafted without leaving the chat
- **Agencies** get per-credential scopes so each client surface stays separated
- **Ops-minded senders** get a policy engine that cannot be overridden by the agent

## Integration with CorpusIQ

Sendsets complements CorpusIQ's email connectors: Gmail handles the human inbox while Sendsets runs the outbound program, and campaign stats can be pulled into CorpusIQ recaps alongside Klaviyo email revenue to compare inbound and outbound channel performance. Suppression lists from Sendsets should be kept in sync with the CRM unsubscribe state tracked through the CorpusIQ CRM connector.

## Limitations

- Approval window for send-class tools is 30 minutes before auto-expiry
- Cold email outcome still depends on domain reputation and warmup patience
- Cloud-only; no self-hosted option published
- New listing with a short public track record

## FAQ

### What stops the agent from sending something bad?

A credential-bound policy engine returns executed, awaiting_approval or blocked, and approval can never override an opt-out, suppression or mailbox health check.

### Are campaign runs idempotent?

Yes. Runs are durable, idempotent and preflighted, so a retried request cannot double-send.

### What does the free tier include?

Up to 10 mailboxes.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
