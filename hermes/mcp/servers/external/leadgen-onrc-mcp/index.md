---
title: "Leadgen ONRC MCP - Romanian Company Registry for Agents"
description: "Keyless access to Romania's 4.2 million company registry with financial filings, VIES checks and public contracts, driven on Dedeman."
category: "Business Data"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-26
source: "chatmcp submission queue #8179 filed 2026-11-26T16:35:19Z (com.adrianhomelab/leadgen-onrc); keyless initialize 200 as `leadgen` 2.7.2 on https://leadgen-mcp.adrianhomelab.com/mcp with a 21-tool tools/list and seven tools/call requests driven on 2026-11-26 (lookup_business on Dedeman, find_company_by_domain on dedeman.ro, check_vat, company_contracts, lookup_by_category on software in Cluj, lookup_financials and lookup_financial_ratios)"
relevance: "★★"
tags: [romania, company-registry, kyb, business-data, vies, procurement, financials, keyless, remote-mcp]
last_updated: "2026-11-26"
---

# Leadgen ONRC MCP

**Romania is a market where a company check usually means a web form, a captcha and a payment, and the answer comes back without the field that decides the deal.** This server answers with the ONRC registry record, the Ministry of Finance filing for the latest year, a VIES validity check on the VAT number, and the company's public procurement contracts, all from one endpoint and all without a key. It holds 4.2 million companies, and its twenty-one tools go past lookup into director search, domain-to-company matching, category search and a watchlist.

```
Server type:  Remote (Streamable HTTP)
Endpoint:     https://leadgen-mcp.adrianhomelab.com/mcp?src=mcp-registry
Registry:     com.adrianhomelab/leadgen-onrc
Server name:  leadgen 2.7.2
              title "Leadgen MCP - Romanian Business Data (ONRC)"
Tools:        21, read from a keyless tools/list, seven driven
Sources:      ONRC registry, Ministry of Finance filings, ANAF, EU VIES, SEAP
Auth:         none; free key mentioned by the vendor for higher limits
```

The `instructions` block does the routing the tool names do not: `lookup_business` first for a company by name or CUI, `lookup_director` when the only thing known is a person, `lookup_by_category` to find companies by what they do, `extract_contacts` or `lookup_domain` for a website, `lookup_financials` and `lookup_financial_ratios` for money, and `enrich_company` for one company in a single call.

## The twenty-one tools

| Group | Tools | Notes |
| --- | --- | --- |
| Lookup | `lookup_business`, `lookup_companies`, `find_company_by_domain`, `match_companies`, `lookup_by_category`, `lookup_director`, `company_history` | `lookup_companies` takes up to 100 CUIs in one call, `match_companies` up to 500 records |
| Enrichment | `extract_contacts`, `enrich_company`, `lookup_domain` | the last one adds WHOIS, DNS and an SPF and DMARC audit |
| Money | `lookup_financials`, `lookup_financial_ratios`, `check_vat`, `company_contracts` | filings, ratios, VIES and SEAP |
| Monitoring | `watch_company`, `watch_caen`, `poll_watchlist`, `list_watches`, `unwatch` | a stored fingerprint of the registry record |
| Account | `get_usage`, `report_issue` | usage counters and a defect channel |

## Dedeman, read end to end

`lookup_business` with `query: "Dedeman"` returned four matches and the first is the retailer every Romanian business answer will name:

- **DEDEMAN SRL**, CUI **2816464**, registration **J1992002621040**, registered **05/11/1992**, EUID `ROONRC.J1992002621040`
- **Address:** Municipiul Bacau, Str. ALEXEI TOLSTOI 8, 600093
- **Main activity:** CAEN **4752**, retail sale of hardware, paints and glass in specialised stores, with a further nine secondary codes on the record
- **Directors and administrators:** PAVAL I. DRAGOS and PAVAL ADRIAN, both listed as administrator
- **Latest financials, fiscal 2025, source `mfp`:** revenue **13,157,835,535 RON**, net result **1,635,337,205 RON**, **12,702** employees
- **As of:** registry **2026-11-04**, financial year **2025**

The two derived figures a credit or sales answer will want reproduce by hand. Revenue per employee is **1,035,886.91 RON**, or about **86,323.91 RON a month**, and the net margin is **12.429 percent**. Both are arithmetic on the payload, not vendor opinion, and a client should show them as derived.

`find_company_by_domain` with `dedeman.ro` matched the same company on `registry_website`, returning one of one. That is the join that makes the tool set useful for a sales list: a domain in a CRM becomes a legal entity, a CAEN code and a filing.

## VIES, checked live, and the name it compares

`check_vat` on the same CUI answered at **2026-11-26T17:04:55Z**:

```
valid:        true
vatNumber:    RO2816464
name:         DEDEMAN SRL
address:      MUN. BACAU 600093 STR. ALEXEI TOLSTOI Nr. 8
registryName: DEDEMAN SRL
nameMismatch: false
source:       EU VIES
```

**`nameMismatch` is the field that earns the tool.** A VAT number can be valid while the entity claiming it is not the entity on the record, and this returns both names side by side with the comparison already made, against the European Commission's own service rather than a cached copy.

## Public procurement, and a total that sums

`company_contracts` on Dedeman returned three SEAP contracts worth **18,377,193 RON**, with the attribution line *Sursa: SEAP, date publicate de ADR pe data.gov.ro, licenta CC-BY 4.0*, as of 2026-11-12:

| Year | Contracts | Value (RON) | Note |
| --- | --- | --- | --- |
| 2025 | 1 | 18,186,803 | contract 287, 2025-05-07, CPV 44160000-9, with TRANSGAZ Medias |
| 2023 | 1 | 0 | unpriced |
| 2019 | 1 | 190,390 | with Universitatea Alexandru Ioan Cuza Iasi |

The total reproduces exactly: **18,186,803 + 190,390 = 18,377,193**, and TRANSGAZ alone is **98.96 percent** of the priced value. A listing tool that reported a company's public-sector revenue without flagging that one authority is almost the whole number would be misleading, and the payload's `top` array is what makes the concentration visible.

## Category search, filtered by county

`lookup_by_category` with `topic: "software"` and `county: "Cluj"` returned **10 of 10**, sorted newest first, led by **HAYSTACKPAWS S.R.L.**, CUI 55786763, registered 02/11/2026, CAEN 5829 for software publishing. The response carries the full filter block that was applied, including `activeOnly: true`, plus nulls for the filters that were not, which is the shape that lets an agent build a defensible list rather than a lucky one.

## Two empty responses, measured

1. **`lookup_financials` on CUI 14347466 returned an empty object `{}`.** No error, no `found: false`, no message. A client cannot tell a company with no filings from a CUI that does not exist.
2. **`lookup_financial_ratios` on Dedeman's own CUI returned no content block and no structured content at all**, while `lookup_business` for the same company returned a full 2025 filing. The ratios tool is empty for a company whose revenue and net result are on the record two calls away.

Both are worth reporting to the vendor before this is put in front of a client, and neither stops the other nineteen tools working.

## Where it fits a business-answer system

A company question about Romania currently produces a plausible paragraph and no evidence. This produces a registry number, a registration date, named directors, a filing with a year, a VIES verdict with a mismatch flag and a procurement total with attribution, which is the difference between an answer and a citation. For a business-answer system the join matters more than any single field: the same CUI ties the registry record, the filing, the VAT check and the contracts, so a cross-source answer can prove it is talking about one entity.

## Is a missing company the same as an inactive company?

No. Category searches default to `activeOnly: true` and the response reports `inactiveFilteredOut` separately, so a company absent from a filtered list has not been shown to be closed. Fetch it by CUI before drawing that conclusion.

## Does the free endpoint have a rate limit?

The vendor names a free key for higher limits, and the `get_usage` tool reports the counters for the current key. No limit was stated in the handshake, and none was hit across seven calls.

## Can the contract data be quoted?

Yes, with the attribution the payload returns. The source is SEAP, published on data.gov.ro under CC-BY 4.0, and the `asOf` field dates the snapshot, which was 2026-11-12 on the day of this read.

## Connecting it

Add `https://leadgen-mcp.adrianhomelab.com/mcp?src=mcp-registry` as a remote MCP server. Keep the query string: it is how the vendor attributes the registry listing. Nothing else is needed, and a client can start with `lookup_business` on a name and work outward.

## See also

- [Korea Business Verify](/hermes/mcp/servers/external/korea-business-verify/) for the same registry class in another market
- [UK Land Registry MCP](/hermes/mcp/servers/external/uk-land-registry-mcp/) for the property side of a company check
- [External MCP server catalog](/hermes/mcp/servers/external/index.md) for the rest of the business-data group
