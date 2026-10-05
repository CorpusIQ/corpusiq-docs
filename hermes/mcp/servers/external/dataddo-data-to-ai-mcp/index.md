---
title: Dataddo Data to AI MCP - Semantic Layer for Business Data
description: "Semantic layer over 400+ business data sources: 12 tools for models, entities, blessed metrics, queries, freshness, known gaps and masking."
category: Data & Analytics
stars: n/a (new listing)
added: 2026-10-05
source: mcp.so feed (Oct 5, 2026 midday sweep)
relevance: ★★★
tags: [business-data, semantic-layer, analytics, data-integration, freshness, masking, remote-mcp, oauth]
---

# Dataddo Data to AI MCP

**Remote MCP server (Streamable HTTP, OAuth)** - Data to AI from Dataddo, the server that connects AI assistants to a company's business tools through a semantic layer. Dataddo extracts from 400+ sources - CRMs, ad platforms, ERPs, payment processors, databases and SaaS apps - keeps the data fresh in SmartCache, and this server answers questions against it with business entities and blessed metrics instead of SQL.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 with dynamic client registration (Dataddo account)
Endpoint: https://headless.dataddo.com/mcp-data
Tools: 12 (list_flows, describe_flow, list_models, list_entities, describe_entity, search, sample_values, query, data_status, known_gaps, refresh, report_problem)
Pricing: free during private pre-release
Clients: Claude, ChatGPT, Cursor, Gemini CLI, Le Chat and other MCP clients
```

## Why This Matters for Operators

Cross-tool questions are the expensive kind. Marketing performance lives in GA4, Google Ads and Meta Ads; financial questions need the CRM, payroll, the payment processor and the ERP. Answering "did the campaign pay for itself" usually means exporting and joining spreadsheets by hand.

This server closes that gap without a warehouse project: the agent asks the semantic layer for business nouns (customer, invoice, deal, revenue) rather than tables, and Dataddo never accepts SQL from the model - queries stay inside what the data model defines. Two design details matter more than the tool count: every answer can carry its data freshness, and the agent is told to check a known-gaps list before answering anything involving trends or forecasts, so "we cannot answer that" is a supported outcome instead of an approximation.

## Tools & Capabilities

| Group | Tools | What they do |
|---|---|---|
| Discovery | `list_flows`, `describe_flow`, `list_models`, `list_entities`, `describe_entity`, `search`, `sample_values` | Start at the flows the account is connected to, then the entities and blessed metrics one model can actually answer; `search` finds fields and metrics by keyword; `sample_values` shows how a categorical field is really spelled before filtering |
| Querying | `query` | Select fields by name, traverse declared relationships with dots, group, order and filter; metrics encode which definition of revenue is correct; `dry_run` compiles and returns the SQL without executing it |
| Trust | `data_status`, `known_gaps` | Freshness, last write time and row counts before presenting figures someone will act on; the hand-written inventory of questions the data cannot answer |
| Feedback | `refresh`, `report_problem` | Ask the source for fresh data; record an answer that a person says is wrong, with what is known about the entity often explaining why |

## Installation

```bash
claude mcp add dataddo-data-to-ai --transport http https://headless.dataddo.com/mcp-data
```

OAuth 2.1 with dynamic client registration on first connect. You need a Dataddo account with Data to AI access; the product is free during private pre-release and pricing is announced at launch. Learn more at dataddo.com/products/data-to-ai.

## Business Relevance

- **One question, many systems**: marketing, finance and operations answers from the same conversation, without exporting and joining by hand.
- **Grounding over guessing**: freshness on every entity and a known-gaps check before trends or forecasts - fewer confidently wrong answers.
- **Control over exposure**: only data attached to an AI destination or AI Model is reachable, and personal or sensitive fields can be hashed or excluded before they ever reach the model.
- **No warehouse requirement**: Dataddo handles extraction and freshness; users query through the semantic layer instead of logging in to each tool.

## Integration with CorpusIQ

Both layers attack the same problem from opposite ends: CorpusIQ connects an agent to the systems a business already runs, read-only, and answers with source-cited figures. Dataddo's Data to AI models those systems into a governed semantic layer with masking and a pre-release free tier. An operator with both can compare a direct connector read against a modelled metric when a number needs a second opinion, with each answer stating where it came from and how fresh it is.

## Limitations

- Requires a Dataddo account with Data to AI access; free during private pre-release, priced at launch.
- Answers are scoped to what has been modelled: a flow with columns listed but `queryable=false` is connected and inspectable, not answerable.
- Not every account question is answerable - gaps are written by hand, and an empty gap list is not evidence there are none.
- The server never accepts SQL; queries stay within the declared entities, fields, relationships and metrics.
- Hosted by Dataddo and governed by its terms; a live POST initialize returns 401 unauthenticated (Missing bearer token), confirming it is auth-gated.

## FAQ

### What is Dataddo Data to AI?

A semantic layer between AI assistants and a company's business tools: Dataddo extracts from 400+ sources and keeps them fresh, and the MCP server exposes entities and blessed metrics so assistants answer grounded questions instead of querying raw tables.

### Can the model write SQL?

No. Dataddo never accepts SQL from the model - the agent selects entities, fields and pre-defined metrics by name, so queries stay inside what the data model defines.

### How does it handle sensitive data?

Only data attached to an AI destination or AI Model is reachable, and personal or sensitive fields can be hashed or excluded before they reach the model.

### How much does it cost?

Free during private pre-release; pricing is announced at launch. You need a Dataddo account with Data to AI access.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
