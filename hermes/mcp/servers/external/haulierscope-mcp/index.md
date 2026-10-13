---
title: "HaulierScope MCP - GB Operator Licence Data for Agents"
description: "Look up any GB goods-vehicle or bus operator licence from DVSA open data, with Companies House, earned-recognition and Traffic Commissioner context."
category: Logistics
stars: n/a (new listing)
added: 2026-10-12
source: "mcpservers.org /all (Oct 12, 2026 evening sweep)"
relevance: ★★
tags: [logistics, transport, compliance, dvsa, operator-licence, uk, government-data, remote-mcp]
---

# HaulierScope MCP

**Remote MCP server (Streamable HTTP, free, no key, read-only)** - the GB operator licence register as a set of tools: search any goods vehicle (HGV) or bus and coach (PSV) operator by company name, licence number or company number, read the licence and its conditions, and follow the change feed the Traffic Commissioners publish - new applications, grants, endings, public inquiries and decisions - on top of the DVSA open data file.

```
Server type: Remote (Streamable HTTP)
Auth: none; all tools are read-only
Endpoint: https://haulierscope.co.uk/mcp (server card at /mcp/server-card)
Tools: 15 (search_operators, get_licence, get_company, area_stats, recent_changes, upcoming_public_inquiries, insolvency_watch, filing_watch, new_licences, licences_ended, tc_decisions, biggest_operators, data_status)
Pricing: free
Category: Logistics / Compliance
Built by: HaulierScope (haulierscope.co.uk, hosted service)
Data: DVSA operator licence open data (Open Government Licence v3.0), file dated 7 October 2026, refreshed as DVSA publishes
Listing: mcpservers.org /all (Oct 12, 2026 evening sweep)
```

## Why This Matters for Operators

Anyone who moves goods or people in Great Britain touches the operator licence system: who holds a licence, which vehicles and trailers are authorised, what conditions and undertakings apply, and whether the operator is in front of a Traffic Commissioner. The checks that depend on it - onboarding a haulier, vetting a subcontractor, screening a carrier before a contract, watching a competitor - are usually done by hand on a public register.

HaulierScope makes that register callable and keeps the provenance visible: every result carries the DVSA file date it came from, and the service layers Companies House data and earned-recognition status where it can. A dispatcher can ask whether a carrier's licence is current before a load is assigned; a compliance team can pull the change feed for the region they operate in; a risk team can watch for insolvency signals on the carriers they depend on.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Lookups | search_operators, get_licence, get_company: find an operator by name, licence number or company number and read the full record |
| Market view | area_stats, biggest_operators: licence and fleet statistics by area, and the largest operators |
| Change feed | recent_changes, new_licences, licences_ended, tc_decisions, upcoming_public_inquiries: what is moving in the register |
| Watch tools | insolvency_watch, filing_watch: Companies House insolvency and filing signals on operators |
| Meta | data_status, search, fetch: the DVSA file date, and raw search/fetch access |

## Installation

```bash
claude mcp add --transport http haulierscope https://haulierscope.co.uk/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "haulierscope": {
      "type": "http",
      "url": "https://haulierscope.co.uk/mcp"
    }
  }
}
```

## Business Relevance

- **Freight and logistics teams** can verify a carrier before a contract or a load: licence status, authorised vehicles, conditions and earned recognition in one call.
- **Compliance and transport managers** can follow the change feed for their operating area instead of monitoring a public site.
- **Procurement and finance teams** get insolvency and filing signals on the carriers they depend on, alongside the licence record.
- **Competitive and market research** can size operators by licence and fleet data for a region.

## Integration with CorpusIQ

CorpusIQ answers from the operational systems; HaulierScope vets the counterparties. Connect a QuickBooks or Airtable source and ask which carriers on the vendor list have licences with conditions attached, or which depend on a single licence that is up for a public inquiry; the assistant reads the actual supplier records from the source of record and checks each one against the licence register, returning the register's own file date with every answer.

## Limitations

- Great Britain coverage (goods vehicles and public service vehicles); Northern Ireland and other jurisdictions are out of scope.
- The data follows the DVSA publication cycle (weekly in practice); the file date travels with every result, so recent changes can lag the live register.
- Read-only by design; it is a register view, not a filing system.

## FAQ

### Is it really free and keyless?

Yes. The MCP endpoint answers without authentication, all tools are read-only, and the vendor publishes the same records on its own website from the same DVSA file.

### How current is the data?

It tracks the DVSA operator licence open data file; the service states the file is re-read each time DVSA publishes (usually weekly), and every result carries the file date so you can judge freshness yourself.

### What can I check about a specific company?

Search by company name, licence number (two letters plus seven digits) or company number, then read the licence record - authorised vehicles, conditions and undertakings - plus Companies House and earned-recognition context where available.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
