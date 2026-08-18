---
title: "AwardCast MCP - CorpusIQ Docs - CorpusIQ Docs"
description: "US federal contracting data for AI agents: SAM.gov solicitations, agency buying profiles, award history, and recompete forecasts via MCP"
category: Analytics & Business Intelligence
stars: n/a (new listing)
added: 2026-08-17
source: "mcp.so GitHub issue #3609"
relevance: ★★★
tags: [govcon, federal-contracting, sam-gov, usaspending, procurement, public-data, remote-mcp, no-auth]
---

# AwardCast MCP

**Remote MCP server (Streamable HTTP, no auth) serving public US federal contracting data to AI agents.** Eight tools cover open solicitations from SAM.gov, buying profiles for federal agencies, award history for contractors, contracts heading to recompete with the incumbent, historical closing-price ranges by agency and NAICS code, and a forecast accuracy scorecard. Data comes from USASpending/FPDS and SAM.gov.

```
Server type: Remote (Streamable HTTP)
Auth: None (public data)
Endpoint: https://awardcast.ai/mcp
Tools: 8 (search, fetch, solicitations, buying profiles, award history, recompete radar, price ranges, forecast scorecard)
Pricing: Free
Category: Government Contracting Data
Built by: AwardCast (awardcast.ai), repo ChosingDept/awardcast-mcp
```

## Why This Matters for Operators

Federal contracting is a data war. Incumbents defend renewals, challengers hunt recompetes, and every player needs to know what agencies actually pay for a given NAICS code. That research normally means sitting inside SAM.gov and USASpending with their clunky interfaces. AwardCast compresses it into eight tools an agent can call directly.

The `search` and `fetch` tools follow the deep-research contract: results carry citable URLs, so a bid team gets an evidence trail, not a summary. The recompete radar is the standout: contracts approaching recompete are flagged with the incumbent named, which converts "we should look at gov work" into a concrete target list.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| `search` / `fetch` | Deep-research style queries with citable source URLs on every result |
| Open solicitations | Active SAM.gov opportunities, filterable for pipeline building |
| Agency buying profiles | How a given federal agency buys: volumes, NAICS mix, preferred vehicles |
| Award history | Historical awards by contractor, for incumbent analysis and past-performance research |
| Recompete radar | Contracts heading to recompete, with the incumbent identified |
| Closing-price ranges | Historical price ranges by agency and NAICS, for bid calibration |
| Forecast scorecard | Accuracy tracking of the platform's own forecasts, disclosed openly |

## Installation

```bash
claude mcp add --transport http awardcast https://awardcast.ai/mcp
```

No account or key required. The surface is read-only public data.

## Configuration

```json
{
  "mcpServers": {
    "awardcast": {
      "type": "http",
      "url": "https://awardcast.ai/mcp"
    }
  }
}
```

## Business Relevance

- **Government contractors** build bid pipelines from open solicitations and recompete flags without a dedicated research analyst
- **Bid teams** calibrate pricing against historical closing ranges by agency and NAICS
- **Business development leads** get named incumbents on every recompete target, which shapes capture strategy
- **Agencies and primes** research contractor award histories for past performance and teaming decisions
- **Analysts** track forecast accuracy against outcomes because the scorecard is published with the data

## Integration with CorpusIQ

CorpusIQ's QuickBooks and Stripe connectors answer the money side of a government services business: invoicing, payment timing, and receivables. AwardCast answers the pipeline side those connectors cannot: which contracts exist, who holds them, and what they are worth. A GovCon operator runs AwardCast for opportunity discovery and CorpusIQ for the financial reconciliation of the work they win, in the same agent session.

## Limitations

- Brand new listing (Aug 17, 2026), no track record yet
- Public contracting data only: no classified or restricted procurements
- Covers US federal awards; no state, local, or international contracting data
- No auth means no personalized pipeline state: pair with a CRM for tracking
- Hosted-only: no self-host option published

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
