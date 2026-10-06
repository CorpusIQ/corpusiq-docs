---
title: "exascale.build MCP - Cited US Energy and Buildout Data"
description: "US ISO interconnection queues, EIA power data, ERCOT prices and cited AI-infra filings with source-row hash verification over MCP."
category: Data & Analytics
stars: n/a (new listing)
added: 2026-10-06
source: "mcpservers.org /all"
relevance: ★★
tags: [energy, data, citations, power, interconnection, ai-infrastructure, remote-mcp]
---

# exascale.build MCP

**Remote MCP server (Streamable HTTP, keyless to start)** - cited US energy and buildout data for agents. exascale.build turns EIA, FERC, ERCOT, Census, Fed and FCC sources into 25 live data capabilities with a discover, describe, query, verify loop, and every number carries a citation you can re-hash. Point an agent at the discovery card and it gets the whole map in one request.

```
Server type: Remote (Streamable HTTP) - REST twin on the same contract
Auth: None for the 25 free queries; API key for historical as_of views
Endpoint: https://api.exascale.build/mcp
Capabilities: 25 live data points (power, natural gas, interconnection queues, AI infrastructure, robotics, space)
Pricing: 25 free queries, then $49/mo or $490/yr
Built by: exascale.build
```

## Why This Matters for Operators

Energy is the quiet constraint on every physical buildout: data centers wait in interconnection queues, industrial sites price power by the balancing authority, and supply chains run on natural gas, chips and equipment that all have public data nobody has time to collect. exascale.build packages that data for agents, with the one property analysts actually need: verifiability.

**Every figure carries its source file and a SHA-256 hash, and `get_source_evidence` re-opens the raw file, re-hashes it and returns the literal source cell.** The query loop also declares what each capability will not answer - capacity is MW, not generation MWh - so the agent declines out-of-scope questions instead of fabricating an answer. For operators, that means an energy or siting question can go from a conversation to a cited number without a research analyst in between.

Coverage spans the buildout story end to end: operating, planned and retired generator capacity (EIA-860M); generation and fuel (EIA-923); FERC Form 1 plant costs with ERCOT's partial coverage stated; Henry Hub and state power prices; hourly demand by balancing authority (EIA-930); ERCOT day-ahead prices; all seven ISO interconnection queues (MISO, PJM, CAISO, NYISO, ISO-NE, ERCOT, SPP); data-center and fab construction spend (Census C30); chip and equipment imports; semiconductor production (Fed G.17); robotics adoption and robot imports; and the FCC satellite dockets.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `list_capabilities_v1` | Every data point and how they join (county_fips, state, balancing_authority_code, eia_plant_id) |
| Schema / describe tools | Each capability's exact filters, group-bys, measures and what it does not answer |
| Query tools | Filters plus group_by, server-side order_by and top_n, returning cited rows and a summary |
| `get_source_evidence_v1` | Re-opens the raw source file, re-hashes it and returns the literal cell as proof |

## Installation

```bash
claude mcp add --transport http exascale https://api.exascale.build/mcp
```

Discovery surfaces: `GET /.well-known/mcp` for the tool map, `GET /v1/capabilities` for the machine-readable reference, `GET /v1/health` for data freshness.

## Configuration

```json
{
  "mcpServers": {
    "exascale": {
      "url": "https://api.exascale.build/mcp"
    }
  }
}
```

The REST twin lives on the same contract, so scripts and agents share one truth: what MCP exposes, REST exposes.

## Business Relevance

- **Energy and industrial operators** size siting decisions against queue positions, prices and demand by balancing authority.
- **AI infrastructure watchers** track data-center construction spend, chip imports and fab output in one citation chain.
- **Consultants and agencies** deliver sourced answers - each figure re-hashable - instead of screenshot proof.
- **Investors and analysts** join supply, demand and buildout data without assembling five dashboards.

## Integration with CorpusIQ

CorpusIQ answers from inside the business: QuickBooks, Stripe, GA4 and the 40+ connectors stay read-only and source-cited. exascale.build answers from outside it, with the same discipline - every number tied to its source file. An operator weighing an energy-heavy decision can pull demand and price data with citations next to their own financials, and the two halves are both verifiable before anyone commits capital.

## Limitations

- US-only and mostly current-fleet defaults; historical as_of views need a paid key.
- ERCOT and some sources carry explicitly partial coverage; the tools say so.
- 25 free queries, then $49/mo or $490/yr; rate limits return a `retry_after`.
- Satellite filing intake changes at the FCC's ICFS cutover; recent filings come from the weekly notices series.
- Brand new listing: no track record from this catalog yet.

## FAQ

### Can I verify a number the agent reports?

Yes. Pass the `verify` object from a query to `get_source_evidence_v1` and the response re-hashes the raw file and returns the literal source row with `hash_verified: true`.

### Does it need an API key?

No for the 25 free queries and current views; a paid key unlocks historical `as_of` snapshots. The health and capabilities endpoints are open.

### What does it not answer?

Each capability declares its own limits - for example, capacity is MW and not generation MWh - so agents decline out-of-scope questions instead of guessing.

### Is REST available too?

Yes. The MCP server and the REST API share one contract; call it from agents or scripts and get identical, cited JSON.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [WaitingForPower MCP - US Energy Permitting Tracker for Agents](/hermes/mcp/servers/external/waitingforpower-mcp/)
