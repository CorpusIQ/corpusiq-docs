---
title: "Faivelo MCP - Business Email for AI Agents"
description: "Faivelo gives AI agents business email on your own domain: read, search and send mail, manage mailboxes and aliases, and set up DNS."
category: Communication & Email
stars: n/a (new listing)
added: 2026-09-28
source: "mcp.so server page (faivelo.com)"
relevance: ★★
tags: [email, mailboxes, dns, aliases, business-email, communication, remote-mcp]
---

# Faivelo MCP

**Business email on your own domain, operated by AI agents.** Faivelo provides email infrastructure for AI agents: read, search and send mail, manage mailboxes and aliases, and configure DNS automatically, with unlimited mailboxes on one flat plan. The hosted endpoint is `https://faivelo.com/api/mcp`.

```
Server type: Remote (Streamable HTTP)
Auth: account auth (docs at faivelo.com/docs)
Endpoint: https://faivelo.com/api/mcp
Tools: read, search, send, mailboxes, aliases, DNS setup
Pricing: flat plan, unlimited mailboxes (faivelo.com/pricing)
Category: Communication & Email
Built by: Faivelo (faivelo.com, github.com/ethannschwartz/faivelo-mcp)
```

## Why This Matters for Operators

Giving an agent a Gmail login means sharing a human identity and fighting Google's limits. Faivelo inverts that: the agent gets its own addresses on your domain, so campaign mail, transactional mail and agent-originated mail stay separate from the founder's inbox, with DNS records configured automatically.

The flat plan with unlimited mailboxes matters for operators who run many parallel campaigns or per-project addresses. Provisioning a new mailbox becomes one agent command instead of a support ticket.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Mailboxes and aliases | Create and manage addresses on your own domain |
| Read and search | Read and search mail across mailboxes |
| Send | Send mail from any managed address |
| DNS setup | Configure SPF, DKIM and MX records automatically |

Tool names are served from the endpoint; the table reflects the vendor's published capability set.

## Installation

```bash
claude mcp add faivelo --transport http https://faivelo.com/api/mcp
```

Per-client setup walkthroughs, including Claude connectors, are published at faivelo.com/docs.

## Configuration

```json
{
  "mcpServers": {
    "faivelo": {
      "type": "http",
      "url": "https://faivelo.com/api/mcp"
    }
  }
}
```

## Business Relevance

- **Founders** keep agent mail on their domain without sharing the human inbox
- **Growth operators** spin up per-campaign addresses on demand
- **Agencies** provision client mailboxes without DNS tickets
- **Ops teams** give each workflow its own address for clean routing

## Integration with CorpusIQ

Faivelo complements the CorpusIQ Gmail and Outlook email connectors: human inboxes stay on Gmail while agent-originated campaigns run through Faivelo addresses on the same domain, keeping deliverability and identity clean.

For the full outbound loop, pair Faivelo addresses with CorpusIQ HubSpot contacts and Klaviyo or ActiveCampaign sends: the agent drafts and sends through Faivelo while the CRM records the contact and the campaign tool reports engagement.

## Limitations

- New listing from an independent developer, no track record yet
- Tool names are not published; live catalog is served from the endpoint
- DNS features depend on domain access
- No deliverability analytics disclosed on the listing

## FAQ

### Why not just give the agent a Gmail inbox?

Shared credentials blur the line between human and agent identity. Dedicated addresses on your domain keep agent mail auditable and separate.

### Does it handle DNS for me?

Yes. Mailbox creation includes automatic DNS configuration for the domain, which is the step most setups get wrong.

### What is the MCP endpoint?

https://faivelo.com/api/mcp with Streamable HTTP transport and account authorization on first connect.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
