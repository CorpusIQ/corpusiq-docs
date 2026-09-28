---
title: Databar.ai MCP - B2B Data Enrichment for AI Agents
description: "Databar.ai gives agents one MCP server over 100+ B2B data providers: enrichment, email waterfalls and ICP prospect search."
category: Data & Analytics
stars: n/a (new listing)
added: 2026-09-27
source: "mcp.so server page (mcp.databar.ai)"
relevance: ★★★
tags: [data-enrichment, b2b-data, email-waterfall, prospect-search, technographics, company-signals, remote-mcp]
---

# Databar.ai MCP

**One interface for over a hundred data providers, with waterfalls instead of single lookups.** Databar.ai exposes a single MCP server at `https://mcp.databar.ai/mcp` that fronts 100-plus third-party data providers: company and contact enrichment, email and phone waterfalls, LinkedIn profiles, technographics, funding data, SEO metrics, email verification and prospect search with ICP filters. Instead of wiring and paying for a dozen vendor APIs, the agent searches the provider catalog at runtime, picks a provider, runs it and writes results into a persistent table.

```
Server type: Remote
Auth: Databar.ai account
Endpoint: https://mcp.databar.ai/mcp
Tools: 12 (enrichments, waterfalls, data sources)
Pricing: credit-based; per-provider prices queryable up front
Category: Data & Analytics
Built by: Databar.ai (databar.ai)
```

## Why This Matters for Operators

Enrichment stacks fail in two ways: single-vendor lookups that miss, and multi-vendor setups that leak cost. Databar addresses both. Email and phone waterfalls try providers in sequence until one hits, with optional verification on the result, which beats any single vendor's match rate. Cost is transparent: every provider exposes its parameters, response fields and credit price before a run, the balance is checkable before and after, and results are cached for 24 hours so repeat lookups are free.

Persistent tables are the operator-friendly detail: results land in a spreadsheet-like workspace rather than a transient tool response, so enrichment of a lead list survives the conversation.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Enrichments | search_enrichments, get_enrichment_details, get_param_choices, run_enrichment, run_bulk_enrichment |
| Waterfalls | search_waterfalls, run_waterfall, run_bulk_waterfall |
| Data sources | search_data_sources, add_table_source, run_table_source, get_table_sources |

## Installation

```bash
claude mcp add databar-ai --transport http https://mcp.databar.ai/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "databar": {
      "type": "http",
      "url": "https://mcp.databar.ai/mcp"
    }
  }
}
```

## Business Relevance

- **RevOps** builds prospect lists from ICP filters and pushes them to the CRM
- **Sales teams** get verified work emails through waterfalls instead of single lookups
- **Founders** research accounts across providers as one merged record
- **Data teams** keep continuously enriched account tables

## Integration with CorpusIQ

Databar feeds the CorpusIQ CRM connector: enriched companies and contacts land in HubSpot or LeadConnector, where CorpusIQ reads them for pipeline recaps. CorpusIQ's inbound-lead analysis can route new leads through Databar enrichment for domain-first qualification before the response is personalized.

## Limitations

- Credit-based pricing; heavy enrichment volume costs credits
- Provider depth depends on the Databar catalog at query time
- Live tool list is served from the endpoint after authentication
- New listing; the platform's agent-native surface is recent

## FAQ

### How many providers sit behind the server?

More than one hundred, searchable at runtime with parameters, response fields and credit price exposed up front.

### What is a waterfall?

A sequence of providers tried in order until one hits, with optional verification on the result.

### Are repeat lookups free?

Results are cached for 24 hours, so repeat enrichments of the same inputs cost nothing.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
