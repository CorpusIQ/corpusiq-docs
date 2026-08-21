---
title: "Signal Nodus SEC Filings MCP — Primary-Source SEC Intelligence for AI Agents"
description: "Hosted MCP server delivering primary-source US SEC intelligence over 27 tools: year-over-year filing diffs, 8-K material events, 13D/13G activist stakes, insider Form 4 trades, 13F holdings, IPO pipeline, full-text EDGAR search since 2001 and XBRL financials with numeric claim verification. Per-call pricing via prepaid key or x402 on Base; free lookup."
category: Finance
stars: n/a (new listing)
added: 2026-08-21
source: mcp.so
relevance: ★★★
tags: [sec, edgar, filings, insider-trading, 13f, x402, finance, research, remote-mcp]
---

# Signal Nodus SEC Filings MCP

**Primary-source SEC intelligence for AI agents, priced per call, with no account required to connect.** Signal Nodus points any MCP client at a hosted endpoint and exposes 27 tools over SEC EDGAR, USAspending.gov, Senate LDA disclosures, ECB and public chain data. The flagship is `compare_filings` — a sentence-level year-over-year diff of a 10-K or 10-Q item — and every numeric claim can be checked against as-reported XBRL with `verify_financial_claim`. US-listed companies and US federal data only; no news, no forecasts, no analyst opinion.

```
Server type: Remote (Streamable HTTP)
Auth: None at connect; per-call billing via prepaid Bearer key or x402 on Base
Endpoint: https://mcp.signalnodus.ai/
Tools: 27 (filings, insider/activist data, IPO pipeline, financials, federal awards)
Pricing: per-call; lookup_company is free
Category: Finance
Built by: 6Genix (github.com/hgenix20/signalnodus)
```

## Why This Matters for Operators

Filings are the ground truth of the US economy — everything an operator needs for supplier diligence, competitive intelligence or investment research is in EDGAR, but it takes an expert to know which form holds the answer and a day to diff last year's 10-K against this year's.

**Signal Nodus turns that research into tool calls.** An agent can ask "what changed in the revenue-recognition section between last year's 10-K and this one", "who just disclosed an activist stake in our competitor", or "did this vendor actually grow receivables, or just revenue" — and get sentence-level, source-cited answers from primary records.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `compare_filings` | Sentence-level year-over-year diff of a 10-K / 10-Q item (flagship) |
| `filing_events` | 8-K material events with decoded item codes |
| `activist_stakes` | 13D/13G filings naming a company |
| `insider_trades` | Form 4 transactions — who traded, role, shares, price |
| `institutional_holdings` / `who_holds` | 13F positions, and the inverse (which managers hold a stock) |
| `ipo_pipeline` | New S-1/F-1 registrations market-wide |
| `edgar_search` | Exact-phrase full-text search over every filing since 2001 |
| `company_financials` / `verify_financial_claim` | As-reported XBRL, plus a deterministic numeric-claim check |
| `government_contracts` / `lobbying` | US federal awards and Senate LDA disclosures |
| Plus | EVM reads, token prices, ECB FX, domain reports, prediction-market odds |

## Installation

```bash
claude mcp add signal-nodus-sec-filings --transport http https://mcp.signalnodus.ai/
```

No account is required to connect — the tools appear on first call. Paying works two ways: buy a prepaid credit and send `Authorization: Bearer <key>`, or let the endpoint answer HTTP 402 with an x402 challenge on Base that the same call settles per use. `lookup_company` is free, so an agent can prove the service before spending anything.

## Configuration

```json
{
  "mcpServers": {
    "signal-nodus-sec-filings": {
      "type": "http",
      "url": "https://mcp.signalnodus.ai/"
    }
  }
}
```

Add the `Authorization: Bearer <key>` header when using a prepaid key; omit it for per-call x402 settlement.

## Business Relevance

- **Founders and operators** run supplier and competitor diligence from primary filings instead of summaries
- **Finance teams** verify a counterparty's reported numbers against XBRL before signing
- **Investors and analysts** track insider trades, activist stakes and institutional holdings by ticker
- **Government-contract vendors** surface federal award and lobbying disclosures for bid intelligence

## Integration with CorpusIQ

Signal Nodus feeds the research layer that CorpusIQ's structured connectors complement. A diligence session can hold the target's books in QuickBooks and its web performance in GA4 through CorpusIQ while Signal Nodus supplies the EDGAR record — insider selling, receivables versus revenue in XBRL, pending 8-K events — so the agent can answer "what does the public record say about this company" and "what do their numbers say" in one pass. The per-call pricing means an idle CorpusIQ agent spends nothing on SEC data.

## Limitations

- US-listed companies and US federal data only — no international filings
- Per-call pricing on every data tool; costs scale with heavy research loops
- x402 settlement requires a Base wallet for the pay-per-call path
- Brand new (Aug 2026 listing), no track record yet
- No news, forecasts or analyst opinion — primary records only

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
