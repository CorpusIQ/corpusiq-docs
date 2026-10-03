---
title: "SendNow MCP - Trackable Document Sharing for Agents"
description: "OAuth remote MCP that shares documents as secure trackable links: data rooms, NDA gates, watermarks and per-viewer read analytics."
category: "Business Operations"
stars: n/a (hosted platform, sendnow.live)
added: 2026-10-02
source: "mcpservers.org server page (sendnow-live)"
relevance: ★★★
tags: [documents, proposals, data-room, e-signature, analytics, sales-enablement, remote-mcp]
---

# SendNow MCP

**Remote MCP server (Streamable HTTP, OAuth)** - SendNow shares documents as secure trackable links and reports who opened them, which pages they read and when to follow up, so an agent can send a proposal and then act on the engagement signal it produces.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth
Endpoint: https://share.sendnow.live/mcp
Tools: document sharing, data rooms, access controls and viewer analytics
Pricing: SendNow account required
Category: Business Operations
Built by: SendNow (sendnow.live)
```

## Why This Matters for Operators

Sending a proposal as an email attachment is sending it blind. SendNow turns each document into a link with engagement telemetry, so the sender learns which sections a reader returned to and when to follow up. The MCP server lets an agent send, control and read that telemetry without a human opening the SendNow app.

**The access controls are the operator feature.** Email verification, NDA gates, download blocking, watermarks and expiry all travel with the link, which is what makes it usable for pitch decks, financial reports and data rooms rather than only internal sharing.

## Tools & Capabilities

| Capability | Purpose |
|---|---|
| Share documents | Turn a document into a secure, trackable link |
| Build data rooms | Group documents with shared access rules |
| Access controls | Email verification, NDA gates, download blocking, watermarks, expiry |
| Viewer analytics | See who viewed what, page-by-page, with per-viewer reporting |
| Activity feed | Follow opens, re-opens and time spent per section |

## Installation

```bash
claude mcp add sendnow --transport http https://share.sendnow.live/mcp
```

Sign in with the browser on first connect.

## Configuration

```json
{
  "mcpServers": {
    "sendnow": {
      "type": "http",
      "url": "https://share.sendnow.live/mcp"
    }
  }
}
```

OAuth handles authorization; a SendNow account is required.

## Business Relevance

- **Sales teams** send pitch decks and proposals, then follow up when the buyer actually returns to a page.
- **Founders** run investor data rooms with NDA gates and watermarking for sensitive documents.
- **Finance teams** share reports with full visibility into who read which sections.
- **Agencies** send client deliverables and report engagement back in the same workflow.
- **Any operator** who needs proof a document was opened, not just sent.

## Integration with CorpusIQ

SendNow closes the loop that most outreach leaves open. A HubSpot deal stage tells an agent who to send to, CorpusIQ pulls the figures for the document from Stripe, QuickBooks or Shopify, and SendNow delivers it with telemetry the agent then writes back to the CRM. The operator sees not only that a proposal went out but whether the buyer read the pricing page, and the CRM record carries the signal without anyone pasting screenshots.

## Limitations

- Brand new, no track record yet.
- Requires a SendNow account and runs as a hosted cloud service.
- Analytics depend on recipient behavior and email-open quirks.
- Data rooms and NDA gating are commercial features behind the account.
- Document format support follows what SendNow accepts for sharing.

## FAQ

### What does SendNow MCP actually add over email?

Engagement telemetry and access controls. Each shared document is a link that reports opens, page-level attention and return visits, with optional NDA gates, watermarks and expiry.

### Does it need an API key?

No. It uses browser OAuth at `https://share.sendnow.live/mcp`.

### Can an agent act on the view data?

Yes. The analytics surface is available to the agent, so it can follow up when a document is opened or re-opened.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
