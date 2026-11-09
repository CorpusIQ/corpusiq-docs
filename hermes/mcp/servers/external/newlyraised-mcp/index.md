---
title: "newlyraised MCP - SEC Form D and SBA Raise Leads"
description: "Find new SEC Form D raises and $1M+ SBA buyout loans by metro, for fractional CFOs and search firms, each row linked to its record."
category: Finance
stars: "n/a (hosted; OAuth 2.1, trial from the consent screen)"
added: 2026-11-09
source: "chatmcp/mcpso submission #6975 filed 2026-11-09T06:51:37Z; the official MCP registry record com.newlyraised/newlyraised 1.0.0; the connector documentation at newlyraised.com/docs/mcp; the data-sources page; and the endpoint itself, where a keyless initialize answered 401 with a protected-resource document"
relevance: ★★★
tags: [finance, funding, sec-form-d, sba, private-equity, executive-search, government-data, remote-mcp]
last_updated: "2026-11-09"
---

# newlyraised MCP

**Two people ask the same question every Monday: which companies just raised money, and which ones just changed hands. Both answers are already filed with the US government, one in the SEC's daily Form D index and one in the SBA's quarterly loan file, and neither arrives as a list a principal can work from.** newlyraised turns both into a searchable list for six US metros, with every row pointing at the filing it came from.

```text
Server type: Remote (Streamable HTTP)
Endpoint:    https://app.newlyraised.com/mcp
Auth:        OAuth 2.1, authorization code with PKCE (S256), DCR and Client ID Metadata Documents
Tools:       5, read-only
Registry:    com.newlyraised/newlyraised 1.0.0
Docs:        newlyraised.com/docs/mcp
Metros:      Houston, Dallas-Fort Worth, Austin, San Antonio, Denver, Atlanta
```

## What the endpoint says about itself

A keyless `initialize` is refused rather than silently redirected:

```text
POST https://app.newlyraised.com/mcp   ->   401
{"jsonrpc":"2.0","error":{"code":-32001,"message":"Authentication required"},"id":null}
```

The protected-resource document names the resource, the authorization server and the single scope `newlyraised`, and the authorization-server document publishes an authorization endpoint, a token endpoint, a `registration_endpoint` for dynamic client registration, a revocation endpoint and `S256` as the only challenge method. That is the tier this entry rests on: **live, gated, documented by the vendor, not driven.** There is no key to paste and no free keyless path, so nothing below is a claim about data quality from a live call.

## The five tools

| Tool | What it answers |
|---|---|
| `list_metros` | Which metros the connector covers and how many records each one holds. |
| `new_raises` | New and updated Form D raises by metro, window, amount, industry and finance-title status. |
| `sba_loans` | SBA 7(a) and 504 approvals of $1 million or more by metro, buyout status, lender and industry. |
| `lender_activity` | Which lenders carry the most SBA buyout activity in a metro. |
| `get_record` | One public finding by id, with the source record behind it. |

Every result is bounded, carries the public source link and a link to the same view inside the web app. The vendor's own examples are the use case stated plainly: new raises in Houston this week that list no CFO, and SBA loans of a million dollars or more that went to buying an existing business in Dallas-Fort Worth this quarter.

## How fresh the data is, and what each source proves

The data-sources page is unusually specific, and it is the reason this entry reads as a research tool rather than a CRM export:

- **SEC Form D.** The newest daily index covered filings posted Nov 2 to Nov 6, 2026, fetched the morning of Nov 7. The weekly list is those five business days; the four-week list covers Oct 13 to Nov 6. Every item links to the SEC filing.
- **SBA 7(a) and 504.** Data as of Sep 30, 2026, from CSV files dated Oct 30, using only approvals dated July to September. The vendor states that SBA republishes the whole file each quarter and that the next one is expected around the end of January 2027. SBA publishes no page per loan, so the row is cited by file and row number, which the vendor says out loud.
- **Census geography.** Static 2020 ZIP-to-county files and the July 2023 metro delineation list place each record in a metro, so a metro filter is a real boundary rather than a guess from a city name.

The page carries an engine run stamp beside the figures, so a reader can see when the list behind the answer was rebuilt rather than when the page was edited.

## Why this matters for operators

A fractional CFO or an executive search firm does not need a database of every company. They need the twenty companies in their metro that just crossed a threshold: a first institutional round that has no finance hire yet, or an acquisition financed with an SBA loan where the new owner is about to inherit a bookkeeping mess. Both of those are public events with dates.

The difference from a general search assistant is the provenance and the boundary. A model asked to name recent raises in Austin will produce a plausible paragraph, mixing funding rounds reported in press with rounds that were never filed. This connector answers from the filing, links the filing, and returns nothing outside the six metros instead of silently widening the search.

## The class it enters, with the owners named

Three neighbours here cover adjacent slices and none covers this one. [Mamba Funding Investor Record](/hermes/mcp/servers/external/mamba-funding-investor-record/) builds a 32-field funding record for one named company from Form D and UK Companies House, which is a record lookup rather than a list. [AllClear Lending](/hermes/mcp/servers/external/allclear-lending-mcp/) works the borrower's side of commercial credit, naming lenders and programs for a business that wants money. [SpendQuery](/hermes/mcp/servers/external/spendquery-mcp/) runs query plans over federal award data. newlyraised is the acquisition side of the SBA file, read as a market: who bought a business, which lender financed it, and which advisory firms are one call away from the new owner.

## Limits, stated as limits

Six metros, not the country. Read-only with no write path, so nothing can be marked, assigned or followed up inside the connector. Results are bounded on purpose, which means a wide question returns a truncated answer rather than a full export, and the export path is the web app. The trial is started from the consent screen, so connecting also starts a clock, and after it lapses the connector returns a sample view instead of the full data.

## Frequently asked questions

### What can an assistant answer with this connector?

New Form D raises and SBA loan approvals of a million dollars or more inside six US metros, filtered by window, amount, industry, lender and finance-title status, with a source link on every row. Both source files are public and neither is a product data set, so the answers are as current as the government file behind them.

### Is it read-only?

Yes. All five tools read. There is no way to write a note, move a record or push anything back into the vendor's system, which makes it safe beside an assistant that only asks questions.

### Can it find companies that raised money and have no CFO?

That is the vendor's own worked example: `new_raises` filtered by finance-title status returns raises where no finance title is listed, which is the list a fractional CFO works from. The filter is stated by the vendor, so treat the first answer as the thing to verify against the linked filing rather than a settled fact.

### How far back does the data go?

The connector advertises week and four-week windows over the Form D daily index, and a quarterly SBA file. It is a recent-activity tool, not an archive, so a question about last year belongs in a different system.
