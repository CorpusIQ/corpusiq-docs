---
title: Deeplead MCP - Verified B2B Contacts for AI Agents
description: "Deeplead's hosted MCP server finds businesses, companies and decision makers with verified emails and phones for B2B outreach."
category: Lead Generation & Web Scraping
stars: n/a (new listing)
added: 2026-09-27
source: "mcpservers.org + github.com/JWPapi/deeplead-mcp"
relevance: ★★★
tags: [b2b-data, lead-generation, email-finder, phone-numbers, company-enrichment, decision-makers, remote-mcp]
---

# Deeplead MCP

**A hosted endpoint that turns an AI assistant into the front end of a B2B contact database.** Deeplead's MCP server at `https://www.deeplead.io/api/mcp` connects agents to business and people search, company enrichment, decision-maker identification and verified work emails and phone numbers for outreach. Transport is streamable HTTP with OAuth, or a Deeplead API key sent as a Bearer header for clients that cannot run a browser flow.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth or API key (Bearer header)
Endpoint: https://www.deeplead.io/api/mcp
Tools: business search, people search, company enrichment, decision makers, emails, phones
Pricing: paid service (see deeplead.io)
Category: Lead Generation & Web Scraping
Built by: Deeplead (deeplead.io; repo github.com/JWPapi/deeplead-mcp)
```

## Why This Matters for Operators

Finding a verified email and phone for the right person is the most boring, highest-leverage step in outbound sales, and the one most likely to be faked by cheap scrapers. Deeplead positions itself around verification: work emails and phone numbers for decision makers, with enrichment on the companies behind them. The MCP server removes the second-biggest tax, which is wiring the database into the workflow, because the agent calls the tools directly mid-conversation.

The RapidAPI caveat matters: a RapidAPI key for Deeplead does not authenticate this endpoint. Only the Deeplead account OAuth or a Deeplead API key works, so operators migrating from the RapidAPI listing must mint the right credential.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Local business search | Find businesses by area and category |
| People search | Locate decision makers at companies |
| Company enrichment | Pull firmographic detail on a company |
| Decision makers | Identify the right contacts for an account |
| Email and phone | Return verified work emails and phone numbers |

Exact tool names and input schemas are exposed by the server after authentication.

## Installation

```bash
npx add-mcp 'https://www.deeplead.io/api/mcp'
```

Installs into Claude Code, Codex, Cursor and other clients. In clients that support remote servers, add the URL and complete OAuth; API-key clients configure the Authorization header locally.

## Configuration

```json
{
  "mcpServers": {
    "deeplead": {
      "type": "http",
      "url": "https://www.deeplead.io/api/mcp"
    }
  }
}
```

Keep the API key out of repositories and use the OAuth flow where the client supports it.

## Business Relevance

- **SDRs and founders** build outreach lists from plain-language asks
- **Recruiters** get decision-maker paths into accounts
- **Agencies** enrich client lists before campaigns go out
- **RevOps** pushes verified contacts straight into the CRM

## Integration with CorpusIQ

Deeplead pairs with CorpusIQ's CRM connector: enriched companies and contacts land in HubSpot or LeadConnector, where CorpusIQ reads them back for pipeline recaps. The lead-pipeline operations can dedupe Deeplead results against existing CRM contacts before outreach, and inbound-response personalization can use Deeplead enrichment to research a prospect before drafting.

## Limitations

- Paid service; pricing lives on deeplead.io and is not in the MCP docs
- RapidAPI keys do not work against this endpoint
- Tool names are exposed only after authentication
- New listing; enrichment depth varies by market

## FAQ

### How does the agent authenticate?

OAuth through a Deeplead account, or a Deeplead API key sent as a Bearer header.

### Does a RapidAPI key work here?

No. A RapidAPI key does not authenticate the Deeplead MCP endpoint; only account OAuth or a Deeplead API key does.

### What data does it return?

Local businesses, companies, decision makers, and verified work emails and phone numbers.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
