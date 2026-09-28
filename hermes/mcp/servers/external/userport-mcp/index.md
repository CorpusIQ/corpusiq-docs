---
title: Userport MCP - Support Inbox and Outbound Messaging for SaaS
description: "Userport connects an agent to the SaaS support inbox and outbound messaging: triage, draft answers and write sequences."
category: Business Operations
stars: n/a (new listing)
added: 2026-09-27
source: "mcpservers.org + userport.io"
relevance: ★★★
tags: [customer-support, inbox-triage, onboarding-sequences, outbound-messaging, saas, drop-off-analysis, remote-mcp]
---

# Userport MCP

**The support inbox and outbound engine, operated from a conversation.** Userport is a customer support and outbound messaging platform for SaaS founders, with a remote MCP server at `https://mcp.userport.io/mcp`. An agent connected to it sees who is waiting, reads threads, drafts and sends answers, closes what is done, writes onboarding and outbound sequences, and reports where users drop off. Streamable HTTP with OAuth 2.1: sign in with a Userport account, no API key, and it works on every plan including the free one.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (browser sign-in, no API key)
Endpoint: https://mcp.userport.io/mcp
Tools: inbox, threads, replies, sequences, analytics
Pricing: all plans including free (userport.io/pricing)
Category: Business Operations / Support
Built by: Userport (userport.io)
```

## Why This Matters for Operators

Support backlogs and onboarding gaps are the same disease: conversations that need an answer, and sequences that need writing, both starved for attention. Userport turns both into outcomes the agent can deliver: list who is still waiting oldest first, summarize unread threads and draft answers, close what is answered, and then write the three-email sequence for people who never installed the widget, with a test send before it goes live.

The compound questions are where the platform earns its keep: which onboarding step loses the most people, and how did outbound do this month versus last, answered from the same connected data.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Inbox triage | List waiting conversations, summarize and draft answers |
| Replies | Send answers and close resolved threads |
| Sequences | Write onboarding and outbound sequences with test sends |
| Analytics | Drop-off analysis by step, month-over-month outbound reports |
| Connection control | Per-account sign-in with revocable connections |

## Installation

```bash
claude mcp add --transport http userport https://mcp.userport.io/mcp
```

Then run `/mcp` and sign in. Claude desktop and claude.ai users add the URL under Settings > Connectors > Add custom connector.

## Configuration

```json
{
  "mcpServers": {
    "userport": {
      "type": "http",
      "url": "https://mcp.userport.io/mcp"
    }
  }
}
```

The client registers itself, the operator signs in and chooses what to allow, and connections can be revoked in Settings > Connect.

## Business Relevance

- **SaaS founders** clear support backlogs and onboarding gaps in one surface
- **Support teams** triage by outcome, not by clicking threads
- **Growth operators** find the onboarding step losing the most users
- **Small teams** get the whole motion on the free plan

## Integration with CorpusIQ

Userport pairs with CorpusIQ's email connectors: Gmail handles the founder's inbox while Userport handles customer conversations, and CorpusIQ can recap support volume alongside GA4 sessions to connect activation and support load. Onboarding drop-off data from Userport joins CorpusIQ's PostHog funnels to confirm where activation actually breaks.

## Limitations

- Built for SaaS support and outbound; not a general helpdesk
- Hosted by the vendor; no self-hosted option published
- Sequence performance depends on list and offer quality
- New listing with a short public track record

## FAQ

### Is there a free plan?

Yes. The MCP connection works on every plan including the free one, with OAuth and no API key.

### What outcomes can the agent deliver?

Triage and answer support threads, write and test sequences, and report drop-off by onboarding step.

### Can connections be revoked?

Yes, from Settings then Connect in the Userport app.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
