---
title: Fundz Agent API MCP - SEC-Filing-Linked Sales Triggers
description: "Hosted sales trigger intelligence that gives agents the reason to reach out and the proof behind it. Four tools surface dated funding and SEC 8-K events for companies matching an ideal-customer profile, each evidence item linked to the SEC filing or announcement it came from, with watchlist polling and an explicitly-labelled experimental forecast."
category: Sales
stars: n/a (new listing)
added: 2026-09-07
source: mcp.so feed
relevance: ★★★
tags: [sales-intelligence, gtm, sec-filings, trigger-events, prospecting, icp, watchlist, remote-mcp]
---

# Fundz Agent API MCP - SEC-Filing-Linked Sales Triggers

**Remote MCP server (Streamable HTTP, API key)** - a hosted sales trigger intelligence endpoint from Fundz LLC (fundz.net) that answers the hardest outbound question - why reach out to this company, today - with dated evidence where every item links back to the SEC filing or announcement it came from. The agent gets a reason to call and the proof behind it, so a rep can open the source before anything is sent.

```
Server type: Remote (Streamable HTTP)
Auth: API key via X-Fundz-Key header (Authorization Bearer and X-Api-Key also accepted); initialize and tools/list are keyless
Endpoint: https://api.fundz.net/v1/agent/mcp
Tools: 4 (why_now, events_for_icp, watchlist_diff, predicted_next)
Pricing: Metered at $0.06 per unit with a $25/month minimum; Platform tiers at 50k / 150k / 400k units
Category: Sales
Built by: Fundz LLC (app.fundz.net)
```

## Why This Matters for Operators

Outbound teams burn hours hunting for a reason to reach out, then send generic emails that read like every other vendor's. Fundz inverts that: the agent starts from dated evidence - a fresh Form D funding round, an 8-K event - and every item carries a `source_kind` label (`sec_filing` or `press_or_news`) plus the link to the filing itself. A rep can open the primary source before a single word is sent.

**The honesty contract is the differentiator: when there is no event in your window, the server returns an empty answer instead of inventing a reason to call**, and `last_event` tells you when the most recent one actually was. It also does not touch contact or people data - no scraped emails, no guessed names - which keeps the tool compliant with the way modern outbound stacks are built.

Coverage is funding (SEC Form D parsed from EDGAR, plus announcements) and SEC 8-K filings. `events_for_icp` builds a list from scratch against an ideal-customer profile, and `watchlist_diff` polls up to 400 of your own domains so a long-running agent only hears about what moved.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `why_now` | One company's dated evidence, each item linked to its source filing or announcement. Costs 1 unit. |
| `events_for_icp` | Companies matching an ideal-customer profile that have had recent funding or 8-K events, ranked with evidence. `min_signals` filters for companies with several signals at once. Hard-capped at 100 rows per call, cursor-paged. |
| `watchlist_diff` | A book of up to 400 domains and a cursor - returns only what moved since. The endpoint to poll. 0.1 units per company checked. |
| `predicted_next` | FundzScore v3 forecast of what a company may do next (raise, be acquired, acquire, hire an executive). Explicitly experimental: treat `lift` as a ranking aid, not a validated rate. |

The live tool list was probe-verified keyless: `events_for_icp` carries `readOnlyHint`, `idempotentHint` and `openWorldHint` annotations, and accepts industries, states, employee-band, `lookback_days` (default 90) and `min_signals` filters.

## Installation

```bash
claude mcp add fundz-agent-api --transport http https://api.fundz.net/v1/agent/mcp --header "X-Fundz-Key: YOUR_KEY"
```

Discovery is keyless - `initialize` and `tools/list` need no credential, so a client can inspect the server before a key is handed over. Only `tools/call` requires the key.

## Configuration

```json
{
  "mcpServers": {
    "fundz-agent-api": {
      "type": "http",
      "url": "https://api.fundz.net/v1/agent/mcp",
      "headers": {
        "X-Fundz-Key": "YOUR_KEY"
      }
    }
  }
}
```

Keys come from the quickstart at app.fundz.net/agent-api. Docs live at github.com/Fund-z/agent-api-docs with runnable examples at github.com/Fund-z/agent-examples.

## Business Relevance

- **SDR and AE teams** get a why-now reason with a primary source link for every account they work, instead of stale intent-data scores.
- **Founders and GTM leaders** poll a 400-domain watchlist for funding and 8-K movement among their ICP and competitors.
- **Agencies running outbound for clients** swap generic sequences for trigger-anchored messaging that cites the actual filing.
- **Investor relations and BD teams** track portfolio-adjacent events without reading EDGAR by hand.

## Integration with CorpusIQ

Fundz feeds directly into CorpusIQ's lead pipeline: the lead tracker polls `watchlist_diff` on the domains already in the pipeline, and when a tracked company shows a new funding or 8-K event, the CorpusIQ-connected agent writes a trigger-anchored outreach note into the contact timeline before the first email is drafted. `events_for_icp` runs as a discovery sweep ahead of cold outreach campaigns, and its evidence links get pasted into the research dossier CorpusIQ builds for each prospect - so the SDR opens the conversation with the filing, not a template. The tool's no-contact-data stance means it complements the enrichment CorpusIQ already runs rather than duplicating it.

## Limitations

- Brand new listing (published Sep 2026) - no public track record yet.
- Metered pricing with a $25/month minimum; costs accrue per call and per company checked.
- Coverage is funding and 8-K only - no hiring, contact or people signals by design.
- `predicted_next` is explicitly experimental and labelled as such by the vendor.
- No self-host option - this is a hosted API only.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
