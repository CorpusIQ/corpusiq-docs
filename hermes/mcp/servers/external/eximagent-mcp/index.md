---
title: "EximAgent MCP - Export-Import Sales and Trade Data"
description: "Hosted MCP server for global trade teams: buyer and supplier discovery, customs and bill-of-lading analytics, HS classification, duty and FTA checks, OFAC screening, and confirmed outreach - 81 tools over OAuth."
category: International Trade
stars: n/a (new listing)
added: 2026-10-08
source: "mcp.so feed (October 8, 2026 night sweep)"
relevance: ★★★
tags: [international-trade, export-import, customs, lead-generation, compliance, sanctions, logistics, sales]
---

# EximAgent MCP

**Hosted MCP server that gives your agent an export-import sales team** - buyer and supplier discovery, trade analytics over customs and bill-of-lading records, compliance checks from HS classification to sanctions screening, and outreach that waits for your confirmation. 81 tools on one OAuth endpoint.

```
Server type: Remote (Streamable HTTP at https://mcp.eximagent.ai/mcp)
Auth: OAuth (browser sign-in; resource metadata at /.well-known/oauth-protected-resource)
Docs: https://eximagent.ai/docs
Tools: 81 across buyer discovery, company intelligence, trade analytics, compliance, outreach and evidence
Coverage: 276M+ shipment records, 578K+ importers identified (vendor-reported)
Pricing: see https://eximagent.ai/pricing
Category: International Trade
Built by: EximAgent
```

## Why This Matters for Operators

Exporters, importers, manufacturers and trading companies run on data most CRMs never see: who actually ships what, between which countries, at what price, and how often. EximAgent puts that corpus behind an agent. Ask for the growing importers of an HS6 code into a market that do not yet buy from your region, and the same conversation can research each company, find the sourcing contact, verify the email, draft the outreach and hold it for your go-ahead. It is the workflow of a trade desk, not another dashboard.

## Tools & Capabilities

| Area | Tools |
|---|---|
| Buyer and supplier discovery | search runs with fit ranking, saved collections, lookalike sets (companies that trade like a seed account), compound lead queries (growing importers of an HS6 with deliverable emails) |
| Company intelligence | full trade fingerprints (HS basket, corridors, counterparties, recurrence), supplier and customer rankings, competitor and similar-company sets, shipment evidence with provenance, company resolution |
| Trade analytics | market size and momentum, price-per-kg trends and dispersion, new and lapsed importers, buyer recurrence cohorts, corridor and route signals, across-country comparisons |
| Compliance | HS code classification, duty and trade-remedy profiles, FTA utilization, landed-cost breakdowns, OFAC sanctions screening (advisory) |
| Outreach | decision-maker contacts with verification, personalized drafts with preview and confirm, collections and share links with PII redaction |
| Account | workspace profile, async run status and post-mortem summaries, hard cost caps per run |

## Installation

```bash
claude mcp add eximagent --transport http https://mcp.eximagent.ai/mcp
```

```json
{
  "mcpServers": {
    "eximagent": {
      "url": "https://mcp.eximagent.ai/mcp"
    }
  }
}
```

Sign in through the browser prompt when your client first connects.

## Configuration

Every data point carries a confidence label (verified, extracted, heuristic or inferred), and shipment answers state data completeness for the market and period. Outreach is preview-first: drafts render as a confirm card and nothing sends until an explicit confirmation, after sender, signature and OFAC checks. Bulk dispatches accept an idempotency key; tools that cost money expose cost caps.

Live probe: POST initialize returns 401 with the OAuth resource metadata, confirming the endpoint is live and auth-gated.

## Example Prompts

- "Find growing importers of specialty coffee into Germany who do not yet buy from Vietnam, with deliverable contact emails."
- "What is my supplier's customer concentration, and which of their buyers could trade with us instead?"
- "Classify this product into an HS code, then give me the duty, FTA rate and landed cost for shipping to the US."
- "Draft outreach to our shortlisted collection, referencing each company's actual shipment profile."

## Integration with CorpusIQ

CorpusIQ keeps your business numbers consistent across AI clients: revenue, orders and customers from Stripe, Shopify or your CRM arrive read-only, with every answer cited. EximAgent adds the trade lane on top of that - pair order and customer data from your own systems with the shipment-level picture EximAgent reads, in the same conversation, without leaving your client.

## Limitations

- OAuth-only; there is no anonymous or keyless lane.
- Sanctions screening is advisory - the vendor states final clearance stays with the founder and legal.
- Shipment data coverage varies by market and period; tools surface completeness flags instead of padding results.
- Paid product; current pricing is published on eximagent.ai.

## FAQ

### Does the agent email buyers without approval?

No. Email tools preview first, then send only after an explicit confirmation step that runs signature, sender and OFAC checks. Failed checks refuse the send.

### What data powers the trade analytics?

Customs filings and bills of lading (vendor-reported 276M+ shipment records across corridors), with record-level evidence available through provenance tools.

### Can it be used without CorpusIQ?

Yes - it is an independent hosted MCP server. CorpusIQ is one convenient way to combine trade data with your own business numbers in the same chat.

## See Also

- [Plain Freight MCP - China to US Freight Quotes for Agents](/hermes/mcp/servers/external/plainfreight-mcp/)
- [ProShip MCP - Fulfillment Operations for Agents](/hermes/mcp/servers/external/proship-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
