---
title: "Hercules MCP - US Property Records and Investor Leads"
description: "NYC and nationwide US property records for investors and lenders: owners, LLC lookups, mortgages, pre-foreclosures and owner contact searches."
category: Real Estate Data
stars: n/a (new listing)
added: 2026-10-12
source: "chatmcp/mcpso issue #5215 (Oct 12, 2026 evening sweep)"
relevance: ★★
tags: [real-estate, property-data, owners, llc, foreclosure, mortgages, investor-leads, remote-mcp]
last_updated: "2026-10-24"
---

# Hercules MCP

**Remote MCP server (Streamable HTTP, keyless initialize and tool listing)** - NYC and nationwide US property records for real estate investors, brokers and lenders: property facts and owners, LLC owner lookups, owner portfolios, mortgages, NYC pre-foreclosure cases, active-investor and investor-firm searches, and owner phone and email contacts. Searches and quotes are free; full reports use workspace credits.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in for reports; searches and quotes run without a key
Endpoint: https://app.hercules.properties/mcp
Tools: 21 (NYC property and owner tools, pre-foreclosure search, national property search, LLC owner lookup, investor and investor-firm search, credit balance)
Pricing: searches and quotes free; reports use workspace credits
Category: Real Estate / Data
Built by: Hercules (hercules.properties, hosted service)
Website: hercules.properties/integrations/mcp
Listing: chatmcp/mcpso issue #5215 (Oct 12, 2026 evening sweep)
```

## Why This Matters for Operators

Property records answer two different questions, and most tools only answer one. The first is due diligence: who owns this building, what is the mortgage, is it in pre-foreclosure. The second is prospecting: which owners hold portfolios worth approaching, which LLCs own what, and how to reach them. Hercules puts both behind one server, with the NYC market covered deeply (pre-foreclosure cases are their own tool group) alongside nationwide searches.

For operators in real estate adjacent businesses - lenders screening collateral, brokers sourcing inventory, service businesses targeting property owners - the practical change is that a lead list becomes a conversation. Ask which active investors in a city hold more than a set number of properties, pull the owner portfolio behind one address, or check a pre-foreclosure case before a call.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| NYC property and owners | find_nyc_property, get_nyc_property, search_nyc_owners, get_nyc_owner_portfolio, unlock_nyc_property_report, unlock_nyc_owner_contacts: parcel-level facts, ownership and contacts |
| NYC pre-foreclosure | search_nyc_preforeclosures, run_nyc_preforeclosure_search, get_nyc_preforeclosure_detail: case search and detail |
| National search | quote_national_property_search, run_national_property_search, get_property_detail: US-wide property records |
| Investor targeting | quote_active_investor_search, run_active_investor_search, quote_investor_firm_search, run_investor_firm_search, quote_llc_owner_lookup, run_llc_owner_lookup: find owners and firms by activity |
| Account | get_hercules_overview, get_credit_balance, buy_credits |

## Installation

```bash
claude mcp add --transport http hercules https://app.hercules.properties/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "hercules": {
      "type": "http",
      "url": "https://app.hercules.properties/mcp"
    }
  }
}
```

## Business Relevance

- **Real estate investors** can screen pre-foreclosure cases and build target lists of active investors and their portfolios.
- **Brokers and agents** can pull owner detail and contacts for a property or a neighborhood before outreach.
- **Lenders and servicers** can verify ownership and mortgage context on collateral across the US.
- **Property service businesses** can build owner-targeted lists by LLC and activity instead of buying static lists.

## Integration with CorpusIQ

CorpusIQ answers from the business systems; Hercules answers the property question. Connect a CRM or spreadsheet source that holds your pipeline, then ask which owners in the pipeline match active-investor signals, or reconcile a list of owned properties against the county records behind each address. The catalog's Placestack entry covers parcel, zoning and permit due diligence; Hercules adds the ownership, portfolio, pre-foreclosure and contact layers that outreach and lending workflows need.

## Limitations

- Deep coverage is strongest in the NYC market (its own tool set); nationwide coverage runs through quote-and-run searches with credits.
- Full reports and contact unlocks consume workspace credits after free searches and quotes.
- OAuth sign-in is the vendor's intended path for report access; the endpoint answers keyless initialize and lists all 21 tools so capability is verifiable before signing up.

## FAQ

### What does a free search return?

Searches and quotes run without credits: they resolve the property or owner and quote what a full report would cost. Unlocking reports and contacts consumes workspace credits.

### Is this the same coverage as the catalog's other property entries?

It complements them. Placestack focuses on parcel, zoning, permit and assessment due diligence; Hercules focuses on ownership, portfolios, pre-foreclosure and owner contacts for investors, brokers and lenders.

### Do I need the vendor's account?

Yes for reports: the flow is OAuth sign-in through the client, and credits live in the workspace. No key is copied around, which keeps report access tied to the account.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
