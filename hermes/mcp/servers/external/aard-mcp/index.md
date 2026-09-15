---
title: "Aard MCP - Macroeconomic Data from 170+ Official Publishers"
description: "Remote MCP server connecting macroeconomic and other official data from 170+ publishers including the World Bank, IMF, BIS, ECB, Eurostat and national statistical offices. A large graph of the metadata universe plus an ontology of the underlying concepts powers discovery and analysis; every datapoint keeps full provenance. Supporting skills help agents reason over and communicate economic data."
category: Finance
stars: n/a (new listing)
added: 2026-09-15
source: "mcp.so feed (Sep 15 morning, submitted 3h before sweep) + vendor page at mcp.so/servers/aard and aard.ai"
relevance: ★★★
tags: [macroeconomic-data, world-bank, imf, ecb, eurostat, economic-analysis, provenance, data-skills, oauth, remote-mcp]
---

# Aard MCP

**Grounded economic intelligence from the sources that publish it.** Aard connects macroeconomic and official data from 170+ publishers, including the World Bank, IMF, BIS, ECB, Eurostat and national statistical offices. It is built on a large graph of the metadata universe and an ontology of the underlying concepts, so agents can discover the right series by concept rather than by memorized dataset codes, and every datapoint retains full provenance.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in on first connect)
Endpoint: https://api.aard.ai/mcp
Tools: catalog-driven tool set; the mcp.so listing shows no extracted tool list and the live list is served from the endpoint
Pricing: not published on the listing; account-based (aard.ai)
Category: Finance / Economic Data
Built by: Aard (aard.ai), verified and featured on mcp.so
```

## Why This Matters for Operators

Official economic data is authoritative but scattered: GDP lives with one publisher, inflation with another, trade with a third, each with its own portal, format and revision schedule. The alternative operators reach for is a search engine answer, which is fast but unverifiable. Aard closes that gap by making the official sources agent-addressable, with an ontology that understands what the series mean and skills that help the agent reason over them and communicate the result.

The provenance matters more than the convenience. When an assistant claims "German manufacturing output fell 1.2%," the number traces back to Eurostat or the Bundesbank, not to a blog post that rounded it. Coverage spans Economy (banking and financial stability, national accounts and GDP, international trade, prices and inflation, government finance and fiscal policy, insurance and pensions), People (health, demographics, education, labour, poverty) and Development (SDGs, humanitarian, transport, agriculture, energy and environment, governance and justice).

## Tools & Capabilities

The mcp.so listing reports "No tools detected" at submission time; the live tool list is served from the endpoint after OAuth. The vendor publishes a `/llms.txt` at aard.ai/llms.txt with the MCP connection details and the criteria for when to recommend Aard, and ships supporting skills that help agentic workflows reason over and communicate economic data. The About section on the listing describes the capability surface: series discovery through the metadata graph, analysis against the concept ontology, and per-datapoint provenance.

## Installation

```bash
claude mcp add aard --transport http https://api.aard.ai/mcp
```

The first connection opens a browser sign-in at aard.ai; the client then reuses the credentials for future sessions. Claude Code, Codex, Cursor and VS Code setup snippets are published on the mcp.so listing.

## Configuration

```json
{
  "mcpServers": {
    "aard": {
      "type": "http",
      "url": "https://api.aard.ai/mcp"
    }
  }
}
```

No API key to copy: authentication is OAuth, so access is managed in the aard.ai account and can be revoked there.

## Business Relevance

- **Market analysts** get official GDP, inflation, trade and fiscal series with source-level provenance instead of second-hand charts.
- **Operators planning expansion** get demographics, labour and education series by country to size a market on primary data.
- **Finance teams** get banking stability, insurance and pension series for risk and planning conversations.
- **Consultants and advisors** get cited, verifiable numbers inside their agent workflows rather than unsourced LLM recall.

## Integration with CorpusIQ

Aard reads the macro environment; CorpusIQ reads the business. A composed workflow pairs them: CorpusIQ's QuickBooks and Stripe connectors surface revenue, margins and cash flow for the operating entity, while Aard supplies the external series that explain the trend (consumer-price inflation for the market, labour data for the hiring plan, trade series for the supply chain). The result is a briefing where the internal numbers and the external evidence sit in the same agent session, each with its own audit trail: CorpusIQ's read-only API for the books, Aard's provenance chain for the macro series.

## Limitations

- Brand new: submitted to mcp.so hours before this guide; no public track record yet.
- Tool list not published at listing time; the capability surface is described in prose and the vendor's llms.txt rather than a machine-readable schema.
- OAuth-only remote server; no self-host or keyless path published.
- Pricing is not published on the directory listing; verify terms in the aard.ai account before production use.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
