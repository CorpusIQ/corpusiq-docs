---
title: "Dutch Vehicle Context MCP - Netherlands Vehicle Reports by Plate"
description: "Free keyless remote MCP server returning one verified vehicle report per Dutch licence plate from eleven official registers: MOT (APK) history, per-inspection defects, odometer verdict, full recall chain with risk and remedy, and severity-sorted buyer signals"
category: Commerce & E-Commerce
stars: n/a (new listing)
added: 2026-08-20
source: "mcpservers.org (tradebrite-nl-vehicle-context)"
relevance: ★★
tags: [netherlands, vehicle-data, used-cars, mot, apk, recalls, odometer, remote-mcp, keyless]
---

# Dutch Vehicle Context MCP

**One licence plate in, one verified vehicle report out — from eleven official Dutch registers.** Dutch Vehicle Context answers "is this a sensible buy" without an agent stitching datasets together: APK (MOT) history with readable defect descriptions per inspection, the official odometer verdict, and the full recall chain — including what can break, how dangerous it is, and what the remedy is — returned as one ~10 kB JSON answer with severity-sorted signals.

```
Server type: Hosted remote (Streamable HTTP) + plain HTTPS API
Endpoint: https://vehicle-context.tradebrite.nl/mcp
Auth: None (free, no key, no registration)
Tools: 1 (get_verified_vehicle_context)
License: MIT
Built by: TradeBrite NL (rleefers)
```

## Why This Matters for Operators

All the underlying data is public and free; the problem is fragmentation. The answer to a normal question sits across eleven datasets and two code tables, and the most valuable conclusions exist in none of them: a recall flagged simply as `Yes` in the base register, a recurring defect that only appears when you group inspection rounds, a re-inspection after repair that shares the same defects and would raise a false alarm if you counted dates. This layer computes those conclusions and labels them.

`signals` are observations, never established defects, sorted by severity, each with a recommendation and its basis. Theft status is deliberately absent — it is not provided as open data, and every answer says so explicitly, so a clean-looking report can never be misread as "not stolen".

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `get_verified_vehicle_context` | Returns one JSON answer with `identity`, `technical`, `fuel`, `inspection`, `defects`, `odometer`, `recalls`, `status_flags`, `value`, `signals`, and `provenance` blocks |

Key signals: `open_recall` (with defect, danger, and remedy), `recurring_defect` (same defect across multiple inspection rounds), `odometer_illogical`, `odometer_no_judgement` (no verdict is not the same as an approval), `imported_vehicle` (pre-import history missing), `emission_zone_restricted` (diesel below EURO 5), `apk_expired`, `not_insured`, `exported`, and `taxi_history`.

## Installation

```json
{
  "mcpServers": {
    "vehicle-context": {
      "type": "http",
      "url": "https://vehicle-context.tradebrite.nl/mcp"
    }
  }
}
```

```bash
claude mcp add --transport http vehicle-context https://vehicle-context.tradebrite.nl/mcp
```

A plain HTTPS API (`GET /v1/vehicle/context?plate=...`) serves the same data without MCP. Documentation at tradebrite.nl/vehicle-context/.

## Configuration

No keys, no registration. The server is hosted and free. MIT licensed; the source is public at github.com/rleefers/dutch-vehicle-context.

## Business Relevance

- **Used-car dealers and importers** screen plates before purchase or trade-in
- **Leasing and fleet operators** monitor APK expiry, recalls, and emission-zone status across fleets
- **Insurance and finance teams** verify odometer and inspection history per vehicle
- **Agent builders** ground vehicle questions in verified registers instead of web guesses

## Integration with CorpusIQ

Dutch Vehicle Context delivers the Dutch vehicle-data layer, which CorpusIQ's connectors do not cover. In one agent session, a dealer can screen every plate through Dutch Vehicle Context while CorpusIQ handles the commercial layer: QuickBooks for the books, Stripe for payments, and email for purchase correspondence — joined on licence plate. The explicit no-theft-verdict design fits CorpusIQ's no-fabrication data doctrine.

## Limitations

- Netherlands only; no theft status by design (not open data)
- Not purchase or safety advice; signals are observations, not established defects
- New listing (Aug 2026), zero-star repository, single maintainer
- One tool surface — no bulk endpoints

## See Also

- [Dutch Property Context MCP — Netherlands Property Reports by Address](/hermes/mcp/servers/external/dutch-property-context/)
- [RE Data Refinery MCP — Pay-Per-Query Real Estate Intelligence](/hermes/mcp/servers/external/re-data-refinery-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
