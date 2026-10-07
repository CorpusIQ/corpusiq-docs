---
title: "Mamba Reporting Window Finder MCP - Earnings Dates"
description: "Resolve a listed company and read its fiscal year end, reporting cadence, next events and an outreach window you define, with US timing rows."
category: Finance
stars: n/a (npm package, MIT)
added: 2026-10-07
source: "chatmcp/mcpso issue #4887 (Oct 7, 2026 morning sweep)"
relevance: ★★
tags: [earnings, public-companies, sec, finance, reporting, outreach-timing, apify, local-mcp]
---

# Mamba Reporting Window Finder MCP

**Local MCP server (stdio, npm) - when a public company reports** and when to reach out around it: fiscal year end, reporting cadence, the next reporting date, days to event, and the open and close of an outreach window you define.

```
Server type: Local (stdio), TypeScript, Node 18+
Auth: Your own Apify API token (APIFY_TOKEN)
Package: @mambalabsdev/mcp-public-company-reporting-window-finder (npm, MIT, v1.1.0)
Tools: 5 (resolve_company, qualify_company, get_reporting_timing, build_company_universe, get_reporting_season)
Registry: com.mambabuilt/mcp-public-company-reporting-window-finder
Pricing: Apify, per row returned (resolved $0.006, timing $0.012, season $0.05; volume discounts on paid Apify plans)
Coverage: timing rows are US companies; identity, venue and classification resolve worldwide
Built by: Mamba Labs (part of the Mamba Labs GTM Suite)
```

## Why This Matters for Operators

Every listed company runs on a reporting calendar, and that calendar is a selling window: budgets open before results, announcements go quiet around them. This server resolves a company from a domain, ticker, ISIN, LEI, CIK or name and returns fiscal year end, cadence, the next reporting events and an outreach window you define (default: opens 70 days before, closes 42 days before the event). A `include_constrained_period` flag even emits the period in which a listed company is constrained in what it can announce, which is exactly the calculus behind campaign timing.

The honesty layer is unusual and welcome: predicted dates are labelled (`next_event_is_estimate`), confidence is computed on the weakest link in the chain, and a company whose filing history is too short or irregular returns a null cadence with a stated reason instead of an invented date.

## Tools & Capabilities

| Tool | What the agent can do |
|---|---|
| `resolve_company` | Identity and venue from identifiers (44 fields) |
| `qualify_company` | A listed status verdict (with filters to keep or remove proven-listed companies) |
| `get_reporting_timing` | Fiscal year end, cadence, next event, the outreach window (75 fields) |
| `build_company_universe` | Build a company list from filters (set `limit`; billed per row) |
| `get_reporting_season` | Reporting load per week or month, optionally split by sector, country or exchange |

You never pass a mode; each tool sets its own and exposes only the inputs it uses. Identifiers: domain(s), tickers, ISINs, LEIs, CIKs and names. Filters: exchange codes (18 venues), countries, regions, sectors, security types, public float bands, fiscal year end months, cadences, operating-company-only, SPAC exclusion, foreign private issuer status and provenance controls.

## Installation

```bash
npm i @mambalabsdev/mcp-public-company-reporting-window-finder
```

Or run it without installing via `npx` using the configuration below.

## Configuration

```json
{
  "mcpServers": {
    "mamba-public-company-reporting-window-finder": {
      "command": "npx",
      "args": ["-y", "@mambalabsdev/mcp-public-company-reporting-window-finder"],
      "env": { "APIFY_TOKEN": "your-apify-token" }
    }
  }
}
```

Get a token at console.apify.com/account/integrations. The server lists its tools without a token; the token is needed to run a lookup. The same tools also ship in the umbrella `@mambalabsdev/mcp-gtm-suite` package.

## Business Relevance

- **IR and corp dev:** know when your own and peer reporting windows sit before scheduling outreach or announcements.
- **B2B sales into public companies:** open the conversation while budgets are still open, avoid the quiet period.
- **Analysts and agencies:** build a reporting-load calendar by week or month and plan capacity.
- **List building:** filter the publishable universe by venue, country, sector, float band, cadence and fiscal year end.

## Integration with CorpusIQ

CorpusIQ keeps the operator's own numbers consistent across their systems; the Reporting Window Finder adds the calendar of the companies around them. Pair it with a pipeline in CorpusIQ: enrich each account with its next reporting event and outreach window, then work the list while the window is open.

## Limitations

- Timing rows cover US companies only; a non-US company resolves fully and returns a stated reason rather than a guessed date (and is still charged as a timing row because the lookup ran).
- Dates are predicted from US SEC filing history, not announced; read `confidence_band`, `confidence_effective` and `next_event_is_estimate`.
- `build_company_universe` and `get_reporting_season` default to a 1000-row limit and are billed per row returned; set limits deliberately.
- Sector is populated on roughly 65 percent of the universe; fiscal year end is effectively a US field. Use `min_provenance_confidence: high` and `exclude_name_only_matches` where a wrong identity link matters.

## FAQ

### Which companies are covered?

Identity, venue and classification resolve worldwide across the publishable universe, but reporting dates come from US SEC filing history and exist for US companies only.

### What is the outreach window?

A window you define around each reporting event (default: opens 70 days before, closes 42 days before) so campaigns land while budgets are still open. `window_status` tells you whether it is open, not yet, or passed.

### Are the dates guaranteed?

No. They are predictions from filing history with confidence bands, and an unknown cadence is refused with a reason instead of guessed.

### How is it priced?

Per row returned on Apify: $0.006 per resolved company, $0.012 per timing row, $0.05 per season aggregate, with volume discounts on paid Apify plans.

## See Also

- [ETFIQ MCP - US ETF Data for Model Portfolios](/hermes/mcp/servers/external/etfiq-mcp/)
- [Silicon Floor MCP - AI and Chip Stock Research](/hermes/mcp/servers/external/silicon-floor-mcp/)
- [AdvisorIQ MCP - Advisor CE and RIA Firm Data](/hermes/mcp/servers/external/advisoriq-mcp/)
- [Mamba Funding Investor Record MCP - SEC and UK Filings](/hermes/mcp/servers/external/mamba-funding-investor-record/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
