---
title: "Unipile MCP - LinkedIn, WhatsApp and Email for Agents"
description: "LinkedIn Sales Navigator, Recruiter, WhatsApp, Instagram, Telegram and email over one Streamable HTTP endpoint for coding agents and sales teams."
category: Sales & Outreach
stars: n/a (no public repo)
added: 2026-09-29
source: "mcp.so server page (developer.unipile.com)"
relevance: ★★★
tags: [linkedin, whatsapp, email, sales-navigator, outreach, remote-mcp, streamable-http]
---

# Unipile MCP

**One hosted endpoint for the channels sales teams actually use.** Unipile puts LinkedIn (Sales Navigator and Recruiter), WhatsApp, Instagram, Telegram and email behind a single Streamable HTTP MCP server, so a coding agent or MCP client can build lead search, conversation sync and threaded email flows without stitching together per-channel APIs.

```
Server type: Remote (Streamable HTTP)
Auth: API key (Unipile account)
Endpoint: https://developer.unipile.com/mcp?branch=v2.0
Tools: capability set from the vendor's published use cases (live tool list is served from the endpoint)
Pricing: account-based (vendor API plans)
Category: Sales & Outreach
Built by: Unipile (unipile.com)
```

## Why This Matters for Operators

Multichannel outreach usually means one integration per channel. Unipile collapses LinkedIn, WhatsApp, Instagram, Telegram and email into one endpoint, with the vendor's documented use cases covering the exact workflows an operator runs: building Sales Navigator lead search screens, syncing conversations into an inbox with webhooks for new messages, and sending email sequences with replies threaded under the original message.

Because the server is hosted, there is no local install and no credential plumbing beyond the Unipile API key. The listing does not publish a static tool table, so the capabilities below are drawn from the vendor's own use cases and documentation rather than a live tools/list export.

## Tools & Capabilities

| Capability | What it covers |
|---|---|
| LinkedIn Sales Navigator search | Lead search screens with seniority and headcount filters |
| LinkedIn Recruiter access | Recruiter workflows through the same connection |
| Conversation sync | WhatsApp and LinkedIn conversations synced into your inbox, webhook on new messages |
| Email sending | Gmail, Outlook and IMAP sending with replies threaded under the original email |
| Calendar | Calendar access alongside messaging |
| Instagram and Telegram | Direct messaging over the same endpoint |

The live tool list is served from the endpoint itself; the vendor's use cases above are the published capability set.

## Installation

```bash
claude mcp add unipile --transport http https://developer.unipile.com/mcp?branch=v2.0
```

## Configuration

```json
{
  "mcpServers": {
    "unipile": {
      "type": "http",
      "url": "https://developer.unipile.com/mcp?branch=v2.0"
    }
  }
}
```

Attach the Unipile API key as the authorization header (Bearer scheme) per the vendor's documentation. The same endpoint works from Cursor, Codex and any client that supports remote MCP servers.

## Business Relevance

- **Sales operators** run Sales Navigator lead search and multichannel follow-up from one connection
- **Agencies** sync client conversations into a unified inbox with new-message webhooks
- **Founders** thread email sends (Gmail, Outlook, IMAP) into sequences without a separate email integration
- **Revops teams** replace per-channel API glue with a single documented endpoint

## Integration with CorpusIQ

Unipile executes the outreach that CorpusIQ data selects. A composed workflow: CorpusIQ pulls the audience from Shopify, Stripe or HubSpot, the assistant drafts the follow-up, and Unipile handles the LinkedIn and email sends with replies threaded back for review. The approval point stays with the operator.

## Limitations

- Listing does not publish a static tool table; verify the live tool list from the endpoint before production use
- Requires a Unipile account and API key; no anonymous or keyless mode
- Channel coverage depends on the vendor's platform plans
- Hosted endpoint means vendor uptime and data residency policies apply

## FAQ

### Which channels does Unipile cover?

LinkedIn (Sales Navigator and Recruiter), WhatsApp, Instagram, Telegram and email over Gmail, Outlook and IMAP, plus calendar access.

### Does Unipile require authentication?

Yes. Unipile requires an API key from your developer account, attached to the MCP connection per the vendor's documentation.

### Which transport does the server use?

Streamable HTTP, the transport used by remote MCP servers and supported by all major MCP clients.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [HeyLead MCP - LinkedIn Outreach from Your Own Account](/hermes/mcp/servers/external/heylead-mcp/)
- [Odichat MCP - WhatsApp, Instagram and Facebook Inbox for Agents](/hermes/mcp/servers/external/odichat-mcp/)
