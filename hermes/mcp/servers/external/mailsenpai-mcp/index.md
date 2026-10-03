---
title: "MailSenpai MCP - Email Marketing for Agents"
description: "OAuth remote MCP over MailSenpai email marketing: manage lists, subscribers, templates and campaigns from any AI assistant."
category: "Marketing"
stars: n/a (hosted platform, mailsenpai.com)
added: 2026-10-02
source: "mcpservers.org server page (mcp-mailsenpai-com)"
relevance: ★★
tags: [email-marketing, campaigns, newsletters, subscribers, crm, eu-hosting, remote-mcp]
---

# MailSenpai MCP

**Remote MCP server (Streamable HTTP, OAuth)** - MailSenpai MCP manages an email marketing account from an assistant: lists, subscribers, templates and campaigns, on a server hosted in the European Union.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (server-side)
Endpoint: https://mcp.mailsenpai.com/mcp
Tools: lists, subscribers, templates and campaign management
Pricing: MailSenpai account required
Category: Marketing
Built by: MailSenpai (mailsenpai.com)
```

## Why This Matters for Operators

Newsletter and campaign work is repetitive: the same list hygiene, template edits and campaign sends on a schedule. Putting it behind MCP means an agent can draft a campaign, check the list it will go to and manage the send from the same place the operator plans it, instead of bouncing between a CRM, a template editor and the marketing app.

**EU hosting is the differentiator for regulated teams.** For operators with data-residency constraints, a European-hosted email marketing server is a materially easier approval than a US-only alternative.

## Tools & Capabilities

| Capability | Purpose |
|---|---|
| Lists | Create and manage subscriber lists |
| Subscribers | Add, update and inspect subscribers |
| Templates | Manage and edit email templates |
| Campaigns | Create and manage campaigns across the account |

## Installation

```bash
npx add-mcp 'https://mcp.mailsenpai.com/mcp'
```

Or add the URL as a remote MCP server in any client and complete the OAuth sign-in.

## Configuration

```json
{
  "mcpServers": {
    "mailsenpai": {
      "type": "http",
      "url": "https://mcp.mailsenpai.com/mcp"
    }
  }
}
```

OAuth handles authorization; a MailSenpai account is required.

## Business Relevance

- **Marketing teams** draft and manage campaigns without leaving the assistant.
- **Founders** run newsletters with the list and the template in one agent surface.
- **Agencies** manage several client lists under one account.
- **EU-based or regulated operators** get an email marketing server hosted in Europe.

## Integration with CorpusIQ

MailSenpai runs the outbound while CorpusIQ supplies the targeting and the result. An agent pulls a customer segment from Shopify or a lead list from HubSpot, builds the MailSenpai campaign against that audience, and afterwards reads GA4 or Stripe to see whether the campaign converted. CorpusIQ answers "who and what did they do", MailSenpai answers "what did we send them", and the pair closes the loop from send to revenue.

## Limitations

- Brand new, no track record yet.
- Requires a MailSenpai account; runs as a hosted cloud service.
- Email marketing category is well covered by other servers, so the EU-hosting angle is the differentiator.
- Deliverability and compliance remain the operator's responsibility.
- Tool-level detail beyond the four capability areas is documented on the vendor site rather than in the directory listing.

## FAQ

### Where is MailSenpai hosted?

The server is hosted in the European Union, which matters for teams with data-residency requirements.

### Does it need an API key?

No. It uses OAuth, so clients add `https://mcp.mailsenpai.com/mcp` and sign in.

### What can an agent manage through it?

Lists, subscribers, templates and campaigns.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
