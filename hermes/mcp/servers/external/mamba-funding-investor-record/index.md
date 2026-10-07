---
title: "Mamba Funding Investor Record MCP - SEC and UK Filings"
description: "A company funding record from SEC Form D, UK Companies House and press, every amount labelled with its source of record and entity match."
category: Sales & Outreach
stars: n/a (npm package, MIT)
added: 2026-10-07
source: "chatmcp/mcpso issue #4872 (Oct 7, 2026 morning sweep)"
relevance: ★★★
tags: [funding, sec-form-d, companies-house, sales-signals, due-diligence, apify, local-mcp, npm]
---

# Mamba Funding Investor Record MCP

**Local MCP server (stdio, npm) - filing-backed funding records** for any company: SEC EDGAR Form D amounts with accession numbers, UK Companies House registration details, and press coverage of funding rounds, each labelled with the source it came from.

```
Server type: Local (stdio), TypeScript, Node 18+
Auth: Your own Apify API token (APIFY_TOKEN); optional free Companies House API key for the UK columns
Package: @mambalabsdev/mcp-funding-investor-record (npm, MIT, v1.1.1)
Tool: get_company_funding_record (single tool; 32 flat snake_case fields, one row per company)
Registry: com.mambabuilt/mcp-funding-investor-record
Pricing: Apify credits per lookup
Cache: 7-day result cache (skipCache to force a fresh fetch)
Built by: Mamba Labs (part of the Mamba Labs GTM Suite)
```

## Why This Matters for Operators

Funding events are buying signals and diligence anchors, but most datasets blend filings and press into one blurry number. This keeps them separate: every amount travels with a `source_of_record` saying whether it came from a legal filing or a press release, because those are not the same kind of fact. An entity gate compares each filing against the company name and rejects near matches; a differently named subsidiary goes to separate `related_entity` columns as a named lead and can never be summed into a total. `filings_rejected` reports exactly what the gate turned away.

The positioning is honest and worth repeating: this is not a resold database. It returns less than a database would, and what it returns has a filing behind it. For timing outreach around a raise, or checking a claim before a call, that trade is the right one.

## Tools & Capabilities

| Tool | What the agent can do |
|---|---|
| `get_company_funding_record` | One flat row per company: Form D filing status, date, entity name and accession number; UK company number, name, status and incorporation date; press amount, currency and URL; coverage and fetch status |

Key inputs:
- `company_domain` and `company_name` (the name is what every source is searched by and what the entity gate compares; a wrong or missing name is the largest source of wrong rows).
- `sources` - `all`, `regulatory`, `sec_only`, `uk_only` or `press_only`. Choose `regulatory` when a number has to be defensible.
- `lookbackMonths` - 12 to 120, default 36.
- `minAmountUsd` - sets `amount_meets_threshold` so material raises stand out; it never drops a row or changes an amount.
- `companiesHouseApiKey` - your own free key; without it the UK columns report `skipped` rather than guessing.

## Installation

```bash
npm i @mambalabsdev/mcp-funding-investor-record
```

Or run it without installing via `npx` using the configuration below.

## Configuration

```json
{
  "mcpServers": {
    "mamba-funding-investor-record": {
      "command": "npx",
      "args": ["-y", "@mambalabsdev/mcp-funding-investor-record"],
      "env": {
        "APIFY_TOKEN": "your-apify-token",
        "COMPANIES_HOUSE_API_KEY": "optional-free-key"
      }
    }
  }
}
```

Get an Apify token at console.apify.com/account/integrations and an optional Companies House key at developer.company-information.service.gov.uk. The server lists its tools without a token; the token is needed to run a lookup. The same tools also ship in the umbrella `@mambalabsdev/mcp-gtm-suite` package.

## Business Relevance

- **Sales teams:** time outreach to funding events with a defensible date and amount.
- **Due diligence:** check funding claims against primary sources before a deal or call.
- **UK and US market work:** Companies House records and SEC Form D filings in one row.
- **Investor research:** rejection accounting shows what the record deliberately left out, not just what it found.

## Integration with CorpusIQ

CorpusIQ answers from the operator's own systems; the Funding Investor Record adds the outside-in view of a company's financing history from primary sources. Pair it with a CRM pipeline: enrich every account with a filing-backed funding record while the pipeline numbers stay sourced from your own data.

## Limitations

- Strongest coverage is the US (SEC Form D) and UK (Companies House); other markets rely on press only.
- A near name match is deliberately excluded from totals; check the `related_entity` columns for named leads.
- A row that resolves nothing is still billed: the lookup ran to produce a real "no match" answer.
- Bring your own free Companies House API key for the UK columns; otherwise they report `skipped`.
- Press is labelled as press and never merged with filings; treat it as the least verified source.

## FAQ

### Where does the data come from?

SEC EDGAR Form D filings, UK Companies House records and press coverage, each labelled per number with its source of record. It is built from primary sources, not a resold database.

### What does filings_rejected mean?

The count of records the entity gate turned away because the match was not exact. Near matches surface as `related_entity` leads instead of being summed into the record.

### Can I limit it to filings only?

Yes. `sources: regulatory` keeps filings only, with `sec_only` and `uk_only` for one side of the Atlantic.

### Does it need a Companies House account?

Only for the UK columns. Without a key they report `skipped` and the SEC and press sources still run.

## See Also

- [UK Companies House MCP - KYB Packs for Agents](/hermes/mcp/servers/external/uk-companies-house-mcp/)
- [Builders in Fintech MCP - Fintech Funding Data](/hermes/mcp/servers/external/builders-in-fintech-mcp/)
- [Recordwire MCP - US Business Registry Data for Agents](/hermes/mcp/servers/external/recordwire-mcp/)
- [Mamba Reporting Window Finder MCP - Earnings Dates](/hermes/mcp/servers/external/mamba-reporting-window-finder/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
