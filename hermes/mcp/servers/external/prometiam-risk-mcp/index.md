---
title: "Prometiam Risk MCP - European Company Registries"
description: "Registry lookups, officers, financial statements, insolvency notices and sanctions screening across 13 European countries."
category: Business Operations
stars: n/a (new listing)
added: 2026-10-07
source: "chatmcp/mcpso issue #4912 (Oct 7, 2026 midday-supplement sweep)"
relevance: ★★★
tags: [company-data, company-registry, kyb, due-diligence, compliance, europe, sanctions-screening, self-hosted]
---

# Prometiam Risk MCP

**Local MCP server (stdio via npx) that puts official European company registries inside your agent** - one install covers company data across 13 countries: lookups by name, registration number or VAT, officers and directors, corporate events, insolvency notices from twelve markets, sanctions screening (beta) and VIES or GLEIF validation, as 35 native tools.

```
Server type: Local (stdio via npx prometiam-risk-mcp)
Auth: Shared demo key works with no setup; set PROMETIAM_API_KEY for your own free trial key
API docs: https://www.prometiam.com/risk-api/docs (the REST API every tool wraps)
Tools: 35 across company data, people, events, insolvency, screening, validation, monitoring and procurement
Pricing: No key needed to start; free trial 1,000 calls over 14 days, no card; paid scopes from EUR 9.99/month
Category: Business Operations
Built by: Prometiam (MIT package, commercial API hosted in the EU)
```

## Why This Matters for Operators

Due diligence is a copy-paste tax: every new supplier, customer or counterparty means another registry site, in another language, with another format and login. Prometiam normalizes all of it behind one tool surface. Ask for a company by name, get its registry coordinates, officers, filed accounts and any insolvency notices; screen a counterparty list against sanctions lists in batch; validate a VAT number without leaving the chat.

The economics matter too. **The shared demo key answers immediately after `npx`, so an operator can try every tool before deciding anything.** A free trial key (1,000 calls over 14 days, no card) then covers a real evaluation, and paid plans start at EUR 9.99/month - below the cost of pulling even a handful of official filings by hand.

## Tools & Capabilities

| Tool | What the agent can do |
|---|---|
| `companies_search` | Search by name or identifier - NIF, SIREN/SIRET, company number, organisation number |
| `company_detail` | Full profile by Prometiam ID: officers, registry coordinates, capital, status |
| `companies_lookup` | Resolve up to 100 companies in one call, by identifier or fuzzy name |
| `company_financials` | Annual accounts as filed (GB, FR, DK, SE, NO; listed companies only in ES, PL, HR, BE) |
| `people_search` / `person_detail` | Search officers, directors and shareholders; one person's full appointment history |
| `directors_network` | People appointed to many companies (nominee and hub detection, ES) |
| `events_search` / `events_timeline` / `event_detail` | Capital changes, director changes, dissolutions and mergers, normalized and dateable |
| `insolvency_search` | Insolvency and risk notices by company name or identifier, including Spain's concursal proceedings |
| `insolvency_notices_search` / `insolvency_check` / `insolvency_record` | Gazette notices across twelve markets; check up to 100 counterparties in one call |
| `sanctions_screen` / `sanctions_screen_batch` | Fuzzy-match names against sanctions and export-control lists with confidence scores (beta) |
| `sanctions_entity` / `sanctions_changes` | One sanctions entity in full; additions, removals and amendments on the lists |
| `sanctions_watch` / `sanctions_unwatch` / `sanctions_watchlist` | Re-screened watchlists for your names, with recent hits |
| `vat_validate` | Validate an EU VAT number against VIES (27 member states plus XI) |
| `lei_lookup` / `lei_search` / `lei_relationships` | GLEIF register lookups, name-to-LEI resolution and Level-2 ownership chains |
| `monitor_list` / `monitor_get` / `monitor_subscribe` / `monitor_stop` | Ongoing daily monitoring with signed webhooks (ten markets) |
| `procurement_awards` / `procurement_buyer` / `procurement_buyers` / `procurement_relationship` | Public-contract awards and scored buyer risk profiles (beta) |
| `coverage` / `account` | Per-country dataset coverage and freshness; your plan, quota and scopes |

People, corporate events, sanctions screening and procurement are paid scopes from Starter (EUR 9.99/month); company financials need Scale. Every other tool works on the free tier.

## Installation

```bash
npx -y prometiam-risk-mcp   # one-shot run, no install needed
```

Works with Claude Desktop, Claude Code, Cursor, VS Code and any other MCP-over-stdio client. The server answers on the shared demo key right away; add your own key when you want a private quota.

## Configuration

```json
{
  "mcpServers": {
    "prometiam-risk": {
      "command": "npx",
      "args": ["-y", "prometiam-risk-mcp"],
      "env": { "PROMETIAM_API_KEY": "rk_live_your_key_here" }
    }
  }
}
```

Get a free trial key at prometiam.com/signup (1,000 calls over 14 days, no card). VS Code uses a `servers` key instead of `mcpServers`; the vendor's MCP page has per-client snippets for each client.

## Business Relevance

- **Founders and finance teams:** run KYB on a new customer or supplier in minutes - registration data, officers, accounts and insolvency notices in one conversation.
- **Agencies and consultancies:** batch-resolve a client's counterparty list and screen it for insolvency and sanctions exposure before advising.
- **Accountants and bookkeepers:** verify a client's EU VAT number and pull filed financial statements without registry-site hopping.
- **Procurement and compliance teams:** monitor key counterparties daily with webhook alerts and check public-buyer risk scores.
- **Sales teams:** enrich an account list with registry facts and director networks before an approach.

## Integration with CorpusIQ

CorpusIQ reads your business - Stripe, QuickBooks, HubSpot, GA4, Shopify - and keeps those answers consistent across AI clients. Prometiam covers the other side of the table: the companies outside your walls. Read your own pipeline through CorpusIQ, then check a counterparty's registry record, officers and insolvency history through Prometiam in the same conversation. For regulated workflows, combine the two: your numbers from CorpusIQ, their verified identity from Prometiam.

## Limitations

- Brand new - no track record yet; the package is at 0.4.x with active releases and CI watching four publish surfaces.
- Sanctions screening is beta; PEP screening is Spain-only and a hit is a prompt to review, not a determination.
- Coverage varies by country: Ireland and Poland are company-level only (no officers); Finland, Sweden, Croatia, Belgium, Denmark, Estonia and Slovakia are company records without officer tools.
- Monitoring works in ten markets; insolvency notices cover twelve markets and are corporate only.
- Mutating tools are limited to `monitor_subscribe` and `monitor_stop`; everything else is read-only.
- One request per tool call counts against quota, so batch tools are cheaper than loops.

## FAQ

### Does it really work without an API key?

Yes. The server ships with a shared demo key (30 requests a minute, 2,000 a day, used by everyone without their own key), so the first tool call answers right after `npx`. When that shared quota is spent, the error explains how to get a free key.

### What does the free trial include?

A free trial key is 1,000 calls over 14 days with no credit card. Paid scopes (people, corporate events, sanctions screening, procurement) and company financials start at Starter (EUR 9.99/month) and Scale tiers respectively.

### Which countries are covered?

Company lookups span Spain, France, the UK, Ireland, Poland, Norway, Finland, Sweden, Belgium, Croatia, Denmark, Estonia and Slovakia; insolvency notices cover twelve markets; monitoring covers ten. The `coverage` tool reports dataset coverage and freshness per country.

### Can the agent change anything?

Only `monitor_subscribe` and `monitor_stop` create or delete a monitoring subscription. Every other tool is read-only, and requests run against the EU-hosted Prometiam Risk API with no telemetry added by the package.

## See Also

- [UK Companies House MCP - KYB Packs for Agents](/hermes/mcp/servers/external/uk-companies-house-mcp/)
- [The Company Atlas MCP - Trade Data and Company Registries](/hermes/mcp/servers/external/company-atlas-mcp/)
- [Korea Business Verify MCP - Live KYB Checks for Korean Companies](/hermes/mcp/servers/external/korea-business-verify)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
