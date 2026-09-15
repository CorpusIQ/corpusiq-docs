---
title: "Radicado Uno MCP - Colombian Company Due Diligence for Agents"
description: "Read-only MCP server exposing verified Colombian company data by tax ID (NIT): public procurement from SECOP II since 2000, the RUES business registry, NIIF financial statements, and sanctions with OFAC and UN lists. Six tools return every fact linked to its official source document and capture date. Bearer key at mcp.radicadouno.co/mcp; Business plan with 7-day trial."
category: Compliance
stars: n/a (new listing)
added: 2026-09-14
source: "mcp.so feed (radicado-uno) + vendor page radicadouno.co/precios"
relevance: ★★
tags: [kyb, compliance, colombia, company-data, due-diligence, procurement, ofac, remote-mcp]
---

# Radicado Uno MCP

**Remote MCP server (Streamable HTTP, API key)** - read-only, source-linked company intelligence for Colombia. Given a company name or a NIT (tax ID), an assistant can pull the business registry record, public procurement history back to 2000, NIIF financial statements, sanctions signals and the procurement network around the company, with every fact carrying its official source URL and capture date. The endpoint answers an anonymous initialize with HTTP 401, confirming a live, key-gated server.

```
Server type: Remote (Streamable HTTP)
Auth: API key (rduno_...; the same key opens the REST API)
Endpoint: https://mcp.radicadouno.co/mcp
Tools: 6 (search, profile, contracts, risk signals, network graph, source freshness)
Pricing: Business plan with 7-day free trial; key issued instantly by email
Category: Compliance
Built by: Radicado Uno (radicadouno.co)
```

## Why This Matters for Operators

Colombian counterparty checks normally mean crawling SECOP II, RUES and sanctions lists by hand and stitching screenshots into a memo. Radicado Uno packs the same records into six tools that return structured data with provenance built in - the source document and its capture date travel with every fact, which is what makes the output usable in a compliance file rather than a research note. The procurement network view is the piece spreadsheets miss: it shows which companies compete for the same public buyers, the two-hop graph that makes concentration and co-bidding patterns visible before a contract is signed.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `radicado-uno_buscar_empresa` | search by company name prefix or exact NIT |
| `radicado-uno_perfil_empresa` | full company profile: registry status, provider record, procurement summary |
| `radicado-uno_contratos_empresa` | public contracts by NIT, linked to the official file, filterable by year and status |
| `radicado-uno_senales_empresa` | objective risk signals: public-client concentration, single-bid wins, sanctions, latest financials (not a credit score) |
| `radicado-uno_red_empresa` | two-hop procurement network graph: which companies compete for the same public buyers |
| `radicado-uno_estado_fuentes` | freshness status per source table |

## Installation

```bash
claude mcp add radicado-uno --transport http https://mcp.radicadouno.co/mcp --header "Authorization: Bearer rduno_..._key"
```

Subscribe on the Business plan (7-day free trial) and the API key arrives by email; the same key opens both the REST API and the MCP server.

## Configuration

```json
{
  "mcpServers": {
    "radicado-uno": {
      "type": "http",
      "url": "https://mcp.radicadouno.co/mcp",
      "headers": {
        "Authorization": "Bearer rduno_..._key"
      }
    }
  }
}
```

## Business Relevance

- **Procurement and supply-chain teams** vet Colombian suppliers before onboarding: registry status, contract history, public-client concentration.
- **Compliance officers** assemble source-linked counterparty files with capture dates on every fact.
- **Finance teams** check sanctions exposure (OFAC and UN lists) and financial-statement currency before payment.
- **Sales and partnerships** research prospective Colombian customers or partners from the same assistant they plan in.

## Integration with CorpusIQ

Radicado Uno extends the same due-diligence pattern CorpusIQ runs on internal business data: read the spend and vendor records (QuickBooks bills, expense data) through CorpusIQ, then verify the Colombian counterparties against SECOP II, RUES and sanctions through Radicado Uno in the same session. It pairs naturally with the CN Evidence guide for cross-border supplier checks - different jurisdictions, the same source-linked evidence model an agent can cite in a review.

## Limitations

- Colombia only: no other Latin American jurisdictions.
- Read-only by design; there is no write path to any registry.
- Tool names are in Spanish, matching the source registries.
- Business plan required for tool calls (7-day trial available); brand new listing with no track record yet.
- "Risk signals" are objective indicators, not a credit score or an audit opinion.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [CN Evidence MCP - China Supplier Due Diligence for Agents](/docs/hermes/mcp/servers/external/cn-evidence-mcp)
- [Recordwire MCP - US Business Registry Data for Agents](/docs/hermes/mcp/servers/external/recordwire-mcp)
