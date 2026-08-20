---
title: "Analytics Legends MCP - SAP Analytics Market Intelligence"
description: "Hosted read-only MCP server delivering SAP analytics market intelligence with citations: consulting firm directory, day-rate benchmarks by geography and seniority, contract radar, and curated market news for agents that answer SAP questions with records instead of guesses"
category: Content & Research
stars: n/a (new listing)
added: 2026-08-20
source: "mcp.so GitHub issue #3651"
relevance: ★★
tags: [sap, market-intelligence, consulting-rates, research, business-intelligence, remote-mcp, day-rates, sap-analytics-cloud]
---

# Analytics Legends MCP

**Hosted read-only market intelligence for the SAP analytics services market, with a citation URL on every row.** Analytics Legends MCP exists so an assistant answering a question about SAP Datasphere, Business Data Cloud, SAP Analytics Cloud, BW/4HANA or Databricks can cite a record instead of guessing. 20 tools cover the consulting firm directory, published day-rate benchmarks, contract openings, stack vocabulary, study metadata, and a curated market-news corpus — and every response states the size of the population it was drawn from.

```
Server type: Hosted remote (Streamable HTTP)
Endpoint: https://analyticslegends.ai/mcp
Auth: None for 14 tools, subscriber key for 6 premium tools
Tools: 20 (read-only)
License: MIT
Registry: ai.analyticslegends/sap-analytics (v1.0.6)
Built by: Analytics Legends
```

## Why This Matters for Operators

Companies that run SAP analytics stacks buy two things constantly: consulting capacity and current market knowledge. Both are normally assembled from recruiter calls, forum threads, and gut feel. Analytics Legends turns that into an agent-callable surface where every answer carries its source: day rates come with basis, sample size, and the population they were drawn from, and firm records link to a citation page.

The honesty mechanics are the differentiator. A `sample_size` of null is stated as such rather than implied away, and each response reports the size of the population it was queried against — so an agent knows the difference between a one-observation rate and a market-wide band.

## Tools & Capabilities

| Capability | What it returns |
|---|---|
| Firm directory | SAP consulting, ESN, recruitment and vendor organisations, searchable by country, kind and declared SAP module, with per-firm profiles and an aggregate count tool |
| Day-rate benchmarks | Published P25/P50/P75 bands by geography, stack and seniority, each served with its basis, sample and source |
| Contract radar | Publicly published SAP analytics openings, each with its own page, filterable by employment type |
| Concepts and studies | Stack vocabulary, deep-research study metadata, and the Academy module catalogue |
| Market news | Curated corpus carrying both the Analytics Legends citation URL and the upstream publisher link |

14 tools answer with no credential; 6 require a subscriber key.

## Installation

```json
{
  "mcpServers": {
    "sap-analytics": {
      "type": "http",
      "url": "https://analyticslegends.ai/mcp"
    }
  }
}
```

```bash
claude mcp add --transport http sap-analytics https://analyticslegends.ai/mcp
```

Nothing to install or self-host: the server is a hosted streamable-HTTP endpoint. Documentation lives at analyticslegends.ai/mcp-server/.

## Configuration

No configuration for the free tier. Subscriber tools require a key issued through the Analytics Legends site; the registry entry `ai.analyticslegends/sap-analytics` tracks the official MCP Registry release (v1.0.6, `isLatest`). MIT licensed.

## Business Relevance

- **Buyers of SAP services** benchmark day rates by geography and seniority before negotiating
- **SAP consultancies and recruiters** find the firms and open contract roles in their module
- **Analysts** ground SAP-stack research in citable records with population sizes
- **Agent builders** fold SAP market context into sourcing, budgeting, and vendor-selection workflows

## Integration with CorpusIQ

Analytics Legends supplies the SAP-services market layer — a domain none of CorpusIQ's connectors cover. In one agent session, a finance leader can pull day-rate benchmarks and firm shortlists through Analytics Legends while CorpusIQ handles the money side: QuickBooks for budgets, Stripe for invoices to the chosen firm, and email for the engagement thread — then join the two on vendor name or contract value. The read-only, citation-first design matches CorpusIQ's source-declared reporting discipline.

## Limitations

- SAP analytics services market only — not product usage telemetry or system access
- 6 of 20 tools require a paid subscription
- New listing (Aug 2026), zero-star repository, single vendor
- Read-only by design; no write path to any SAP system

## See Also

- [SYNTHORA MCP — Verified Multi-Source Intelligence Mesh](/hermes/mcp/servers/external/synthora-mcp/)
- [Profitelligence MCP — Financial Intelligence from First-Party SEC Data](/hermes/mcp/servers/external/profitelligence-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
