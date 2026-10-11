---
title: "DataBazaar MCP - Dataset Marketplace for Agents"
description: "Search, sample and retrieve datasets from an agent-first marketplace, with quality scores, one-click purchases and data bounties sellers can fill."
category: Data & Analytics
stars: n/a (new listing)
added: 2026-10-10
source: "chatmcp/mcpso issue #5093 (submission) + vendor site databazaar.io/integrations; catalogued at the October 10, 2026 evening sweep"
relevance: ★★★
tags: [datasets, data-marketplace, data-discovery, bounties, analytics, remote-mcp]
---

# DataBazaar MCP

**The marketplace where agents buy data** - search datasets by plain-language query, inspect bounded samples with schema and quality scores, and retrieve or purchase the full data, all from the assistant. Discovery and samples are public and keyless; full retrieval works through an account. The data-platform find of the October 10 evening sweep, catalogued with the public endpoint probed live (initialize returns 200, `databazaar` v1.2.0, and `tools/list` returns the three public tools with full schemas).

```
Server type: Remote (Streamable HTTP at https://api.databazaar.io/mcp/public, keyless; https://api.databazaar.io/mcp with account auth) or local stdio via npx databazaar-mcp
Auth: None for the public discovery endpoint; account API key for retrieval, purchases and account tools
Tools: 3 public (search_datasets, get_dataset, preview_sample) and 27 total on the full server with 5 resources
Category: Data & Analytics
Built by: DataBazaar (databazaar.io; repo github.com/shagarwal/databazaar-mcp, MIT server code)
```

## Why This Matters for Operators

Data work starts with finding the right data, and that step usually happens outside the tools people actually use: browser tabs, sample downloads, spreadsheets of links. DataBazaar puts the marketplace inside the conversation - the agent searches listings with filters for category, price, quality and pricing type, pulls a sample to verify the columns and format before anyone commits, and hands back a checkout link for the one-click human purchase. Listings carry assessed quality scores with a published rubric, and when the data does not exist, a bounty can be posted to signal demand to sellers.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `search_datasets` | Natural-language search across the marketplace with filters: category (geographic, pricing, sensor, images, text, financial, scientific, social, retail, other), max price, minimum quality score, pricing type (buy it now, auction, hybrid, free) |
| `get_dataset` | Full metadata: schema, column counts, quality score, price anchoring, a checkout URL for human purchase and a forwardable pitch |
| `preview_sample` | About 50 sample rows plus the schema via a signed URL, with an optional question answered from the sample (for example an average or a count) - no purchase needed |

The authenticated server adds retrieval, publishing, bounty and account tools (27 tools and five resources on the full surface). Discovery, samples and bounty browsing work without credentials.

## Installation

```json
{
  "mcpServers": {
    "databazaar": {
      "url": "https://api.databazaar.io/mcp/public"
    }
  }
}
```

Local stdio with account tools: `npx -y databazaar-mcp` after `npx -y databazaar-mcp auth login`, or configure an account API key as documented in the repository. Coding agents can also install the marketplace skill: `npx skills add shagarwal/databazaar-plugin --skill databazaar-marketplace`. Framework clients use the `databazaar-agent-tools` package (Vercel AI SDK 7 and LangChain examples are published).

## Configuration and Safety

- Public endpoint: discovery and samples only, no authentication, three read-only tools. Purchases and account mutations live on the authenticated endpoint.
- Full downloads, including free datasets, require an account. An issued download URL is not a completed download; the docs walk through retrieval for both a benchmark dataset and historical stock bars.
- Purchases require your authorization: the flow hands back a checkout URL, and paid actions are not taken by the public tools.
- Only send the DataBazaar credential to the DataBazaar API. Storage download URLs carry their own authorization - do not attach the API key to them.

## Business Relevance

- **Analytics and BI teams**: find and verify a dataset before buying it - sample first, check the quality score and schema, then retrieve the CSV for the warehouse.
- **AI and data engineering**: agent-first access means a pipeline can source its own inputs; the maintained LangChain and AI SDK packages fit existing frameworks.
- **Marketplace sellers**: browse open bounties and fulfil data requests, or list your own datasets where agent traffic already is.

## Integration with CorpusIQ

Market data answers "what does the world look like"; CorpusIQ answers "what does my business look like". Find an external benchmark or industry dataset through DataBazaar, then ask CorpusIQ for your own comparable numbers from the connectors you already run - Shopify orders, QuickBooks spend, Stripe revenue - and put the two side by side in one conversation, each side traceable to its source.

## Limitations

- The public endpoint is discovery-only; retrieval needs an account even for free datasets.
- Quality scores come from sample structure analysis with a published rubric and limitations page; unassessed listings are excluded when you filter on the score.
- Purchases, refunds and download issues run through the marketplace account, not through the MCP tools on the public side.
- Listings vary in depth: some are raw files, some include schemas and samples; verify with `preview_sample` before buying.

## FAQ

### Do I need an account to try it?

No for search, metadata and samples - the public endpoint is keyless and the three tools work immediately. An account is required to retrieve full datasets, including free ones, and to buy, publish or fulfil bounties.

### How do I check a dataset before buying?

Call `preview_sample` with the dataset id. You get about 50 rows, the schema and a signed download URL, plus an optional synthesized answer (for example "average price in 2024") computed from the sample. Nothing is purchased.

### Can my agent spend money on its own?

Not through the public tools - purchases surface as a checkout URL for the human to complete. Account-level mutations run under your authenticated credentials, and the docs' example clients explicitly cannot purchase or post bounties with the default tool set.

## See Also

- [Monitly MCP - Official Statistics for Your Agent](/hermes/mcp/servers/external/monitly-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
