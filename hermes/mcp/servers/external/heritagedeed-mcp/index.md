---
title: "HeritageDeed MCP - US Title Reports on Demand"
description: "58 keyless tools for US property due diligence: order a $49 title report and read flood, radon, Superfund and sale lists for free."
category: Real Estate Data
stars: ★★★ (keyless, 58 tools)
added: 2026-11-01
source: "the mcpservers.org /all newest page on 2026-11-01 under the slug heritagedeed-com-developers, its detail page read through the r.jina.ai reader proxy, and a keyless JSON-RPC session against https://heritagedeed.com/mcp/public returning HTTP 200 on initialize with serverInfo heritagedeed 1.30.0, 58 tools listed, and live answers from list_coverage, flood_zone_lookup and property_tax_rates_by_state"
relevance: ★★★
tags: [real-estate, title-search, property-data, due-diligence, environmental, tax-sale, surplus-funds, keyless, remote-mcp]
last_updated: "2026-11-01"
---

# HeritageDeed MCP

**Half of property due diligence is free public data that nobody assembles, and the other half is one paid document that takes a title company three days to produce. HeritageDeed puts both behind one keyless endpoint, and lets an agent order the document.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://heritagedeed.com/mcp/public
Auth:        none for lookups, key only for the REST API
Tools:       58 measured
Reports:     title $49, environmental $29, tax appeal $49
Coverage:    title search in 43 counties, environmental anywhere in the US
```

## What it does

Two products and a very wide set of free lookups around them.

The paid documents are ordered, not looked up. `order_title_search` places a **Current Owner Search** in one of **43 counties across 14 states** and returns a PDF plus JSON: the owner of record and the vesting deed, every deed, mortgage and release the county index returns with each mortgage matched to its release and anything unreleased flagged open, recorded liens, lis pendens and UCC fixture filings, federal and bankruptcy court records matched to the owner, property tax status, and in New York City also HPD, DOB and ECB violations and water charges, a FEMA flood zone and EPA-listed sites near the parcel, and a plain-English summary with a risk score. The **Environmental Records Report** runs at any US street address for **$29**. The **Property Tax Appeal Evidence Pack** runs in covered counties for **$49**.

Everything else is free and keyless, and this is the part that changes an operator's week:

- **Land and title context:** `property_history_lookup` for what has been recorded against a parcel, `recent_sales` for sale dates and prices from open data, `zoning_lookup` for New York City, Chicago and Philadelphia, `hoa_lookup`, `llc_owner_lookup`, `ucc_lien_search`, and `nyc_landlord_lookup` off the city's own HPD registration.
- **Environmental screening by address:** `flood_zone_lookup` on FEMA's National Flood Hazard Layer, `radon_lookup` by address or ZIP with the county's EPA radon zone, `superfund_sites_near_address` on the EPA NPL and SEMS lists, `fault_lines_near_address` on USGS mapping within five miles, and `power_lines_near_address` for transmission lines at 100 kV and above.
- **Money:** `title_insurance_premium` from the official Texas rate schedule, `transfer_tax` from the statutes, `seller_net_sheet` for proceeds and buyer closing costs in Florida, Texas, New York City and New York, `property_tax_rate_by_county`, `property_tax_rate_by_zip`, `property_tax_rates_by_state`, `county_loan_limits` across the 3,144 counties for FHFA, FHA and VA, `national_loan_limits`, `fair_market_rent_by_county` and `fair_market_rent_by_zip` from HUD, and `usda_eligibility_lookup`.
- **Distress and lists:** `upcoming_auction_sales` for tax and sheriff sales in the next 21 days, `tax_sale_search` and `tax_sale_summary`, `surplus_funds_search` and `surplus_funds_summary` over excess proceeds still on official lists, `start_tax_sale_due_diligence` for a per-parcel flag sheet of debts that outlive the sale, `tax_appeal_deadlines` with the free filing route, and `property_watch_coverage` plus `create_property_watch` for a watched parcel.
- **Before you spend anything:** `list_coverage`, `check_coverage`, `check_address`, `get_sample_report`, `get_terms` and `list_products`, so an agent can confirm a county is covered and read a finished sample report before an order exists.

## What this pass measured

A keyless `initialize` on `https://heritagedeed.com/mcp/public` returned **HTTP 200**, `serverInfo` `heritagedeed` **1.30.0** with `websiteUrl` `https://heritagedeed.com/developers`, and `tools/list` returned **58** tools with schemas.

`list_coverage` answered with the whole coverage table and the price sheet in one response: **43** counties, with the counties grouped by state and their main cities (Maricopa in Arizona carrying Phoenix, Mesa, Chandler, Scottsdale, Glendale, Gilbert and Tempe), the eight things a title search includes, and the four it does not, naming title insurance, title commitments, an attorney's opinion of title, a survey, payoff balances and any document recorded before the county's online index begins.

`flood_zone_lookup` on a live address returned a parsed FEMA result rather than a link: the matched address and its coordinates, the county, `mapped: false`, `sfha: false`, category `no_mapped_hazard`, an explanation that the layer is also empty where FEMA has published no digital map so the official panel should still be checked, the insurance consequence, the sources, a disclaimer that this is free screening and not an official determination, and the page to confirm it on.

`property_tax_rates_by_state` returned the Census ACS **2020-2024** survey period with a US effective rate of **0.94 percent**, median real estate taxes of **$3,119**, a median home value of **$332,700** across **84,210,142** owner-occupied homes.

## Pricing, read from the server

The lookups are free and need no account. Reports are paid per report: **$49** for a title search, **$29** for an Environmental Records Report, **$49** for a tax appeal pack. Report credits are **$25** a report or **$250** for a pack of ten, and credits make an order start immediately instead of returning a checkout link. Plans are **Pro at $39 a month**, **Pro Reports at $199 a month** with ten reports a month, and **Property Watch at $9.99 a month per property**. A **County List Pass** is **$19 one time for 30 days**. Payments run through Creem as merchant of record.

The REST API v1 sits beside the MCP server for the batch work: up to **50 orders in one submission** as JSON or CSV with a per-row status and a results CSV, an `Idempotency-Key` header so a retried request never orders twice, webhooks with a signing secret, and a white-label company name on the account.

## Where it sits in this catalogue

[Hercules MCP](/hermes/mcp/servers/external/hercules-property-mcp/) is the nearest entry and the split is clean. Hercules is owner and prospecting data: property facts, LLC owners, mortgages, New York City pre-foreclosure cases and investor leads, aimed at finding who to call. HeritageDeed is due diligence: what is recorded against the parcel, what the ground and the air around it carry, what the sale actually nets, what a tax sale would leave behind, and the ordered title report at the end of it.

[Fonciq MCP](/hermes/mcp/servers/external/fonciq-mcp/) covers Quebec flood zones with the land registry, [UK Land Registry MCP](/hermes/mcp/servers/external/uk-land-registry-mcp/) covers sold price packs, and [Dutch Property Context MCP](/hermes/mcp/servers/external/dutch-property-context/) covers Netherlands reports. All three are single-country, and none of them orders a report.

## What this pass did not establish

No report was ordered, so the title search, the environmental report and the tax appeal pack are documented from the server's own coverage and terms rather than from a delivered document. The free lookups were exercised on a handful of addresses, not across all 43 counties, so a specific county's index depth is unverified. The reports are public-records searches, and the server says so itself: they are not title insurance, not a title commitment, not an attorney's opinion of title, and they exclude documents recorded before the county's online index begins and any payoff balances. The batch endpoint, the webhooks and the white-label field are documented in the server's own REST instructions and were not driven. Data freshness per source is unknown, since each lookup reads a different federal or county dataset on its own schedule.

## FAQ

### Do I need a key to use the MCP server?

No. The MCP endpoint answered `initialize` and `tools/list` without a credential, and the free lookups ran without one. A key is needed only for the REST API and for ordering a report against an account.

### What does a title report cost and where does it work?

**$49** per report, or **$25** from a prepaid credit, in **43 counties across 14 states**. `check_coverage` confirms a county and `check_address` validates the address before an order is placed.

### Is this the same as title insurance?

No, and the server says so in its own terms. It is a public-records search that shows what the county index returns with the mortgages matched to their releases. Title insurance, a title commitment and an attorney's opinion of title are explicitly outside it.

### Can an agent screen a property for environmental risk for free?

Yes: FEMA flood zone, EPA radon zone, EPA Superfund sites near the address, USGS fault lines within five miles and high-voltage transmission lines are all free by address. The $29 Environmental Records Report is the paid, fuller version of the same question.

### What is a surplus funds list?

Money left over after a tax deed or foreclosure sale that is still held on an official list. `surplus_funds_search` and `surplus_funds_summary` search it per county with row counts and totals, and Pro opens every county's full list.

### Can it run a batch across many properties?

Yes, through the REST API rather than the MCP tools: up to 50 orders in one submission, each row with its own status, a results CSV, and webhooks signed with the account's secret.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the full catalogue this entry belongs to
- [Hercules MCP - US Property Records and Investor Leads](/hermes/mcp/servers/external/hercules-property-mcp/) - owners, mortgages and investor prospecting rather than due diligence
- [Fonciq MCP - Quebec Flood Zones and Land Registry](/hermes/mcp/servers/external/fonciq-mcp/) - the same flood and registry question for Quebec
- [UK Land Registry MCP - Sold Price Packs for Agents](/hermes/mcp/servers/external/uk-land-registry-mcp/) - the UK equivalent for sold prices
