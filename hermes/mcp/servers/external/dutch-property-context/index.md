---
title: "Dutch Property Context MCP - Netherlands Property Reports by Address"
description: "Free keyless remote MCP server that returns one verified property report per Dutch address, linking nine official open sources (BAG construction year and floor area, energy label, CBS neighbourhood statistics, noise and air quality, monument status, schools) with match-confidence signals"
category: Real Estate
stars: n/a (new listing)
added: 2026-08-20
source: "mcpservers.org (tradebrite-nl-property-context)"
relevance: ★★
tags: [netherlands, real-estate, property-data, open-data, bag, energy-label, remote-mcp, keyless]
---

# Dutch Property Context MCP

**One address in, one verified property report out — from nine official Dutch open sources.** Dutch Property Context answers "what should I know about this address before I view it" without sending the agent to hunt the web: construction year and floor area from the BAG, the registered energy label, CBS neighbourhood statistics, environmental noise and air quality, national-monument status, protected townscape, and nearby schools — linked, deduplicated, and returned as one ~11 kB JSON answer with explicit match confidence.

```
Server type: Hosted remote (Streamable HTTP) + plain HTTPS API
Endpoint: https://property-context.tradebrite.nl/mcp
Auth: None (free, no key, no registration)
Tools: 1 (get_verified_property_context)
License: MIT
Built by: TradeBrite NL (rleefers)
```

## Why This Matters for Operators

Ask an AI agent about a Dutch address and it will browse the web and return an answer that looks right and is sometimes wrong — the underlying data is public and reliable, but it lives in nine registers with their own keys, formats, and quirks. The hard part is linking, and this layer takes that over: it publishes how certain it is that it matched the right building, and when the match is ambiguous it lists every equally good candidate.

`signals` are observations, never established defects. A construction year of 1921 does not mean lead pipes — it means that is worth checking. A source that did not respond is reported as unknown, not as empty.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `get_verified_property_context` | Returns one JSON answer with `identity`, `building`, `energy`, `location`, `neighbourhood`, `environment`, `heritage`, `protected_area`, `schools`, `signals`, and `provenance` blocks |

Read `identity.match_verified` first: when false, the requested address was not verified and the rest of the answer may describe a different building; `match_ambiguous` lists the equal candidates. Key signals: `conflicting_construction_year` (two registers disagree, both shown), `energy_label_expiring` / `no_energy_label`, `protected_townscape` / `world_heritage_area` (permit consequences), and `source_unavailable` (a source did not answer).

## Installation

```json
{
  "mcpServers": {
    "property-context": {
      "type": "http",
      "url": "https://property-context.tradebrite.nl/mcp"
    }
  }
}
```

```bash
claude mcp add --transport http property-context https://property-context.tradebrite.nl/mcp
```

A plain HTTPS API (`GET /v1/property/context?address=...`) serves the same data without MCP. Documentation at tradebrite.nl/property-context/.

## Configuration

No keys, no registration. The server is hosted and free. MIT licensed; the source is public at github.com/rleefers/dutch-property-context.

## Business Relevance

- **Dutch real estate investors and buyers** screen addresses before viewings
- **Property managers** pull energy-label and protected-area status per address
- **Relocation and rental platforms** enrich listings with official neighbourhood data
- **Agent builders** ground address questions in verified registers instead of web guesses

## Integration with CorpusIQ

Dutch Property Context delivers the Dutch property-data layer, which CorpusIQ's connectors do not cover. In one agent session, a Netherlands-focused investor can pull verified property context per address while CorpusIQ handles the commercial layer: QuickBooks for the books, Stripe for payments, and email for deal correspondence — joined on address. The explicit match-confidence field fits CorpusIQ's no-fabrication data doctrine.

## Limitations

- Netherlands only; no valuations, asking prices, ground-lease terms, or ownership history (not freely available)
- Not legal, construction, or investment advice; signals are observations, not established defects
- New listing (Aug 2026), zero-star repository, single maintainer
- One tool surface — no bulk endpoints

## See Also

- [Dutch Vehicle Context MCP — Netherlands Vehicle Reports by Plate](/hermes/mcp/servers/external/dutch-vehicle-context/)
- [Austin MLS MCP — Live Austin Real Estate Listings for AI Assistants](/hermes/mcp/servers/external/austin-mls-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
