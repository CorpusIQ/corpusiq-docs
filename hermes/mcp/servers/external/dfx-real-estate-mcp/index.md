---
title: DFX Real Estate Intelligence MCP - US Property, Parcel
description: "Remote, no-key MCP with 9 tools for US commercial and multifamily real estate: property and parcel lookups, ownership, recorded sales, measured coverage and near-term commercial debt timing. Endpoint live-verified (dfx-real-estate v0.2.0)."
category: Finance
stars: "n/a (hosted service)"
added: 2026-08-31
source: "chatmcp/mcpso issue #3862 (Aug 31, 2026)"
relevance: ★★★
tags: [mcp-server, real-estate, property, parcels, ownership, commercial-debt]
---

# DFX Real Estate Intelligence MCP

**US real estate intelligence, callable directly.** DFX exposes nine tools over US commercial and multifamily real estate: property and parcel resolution, ownership records, recorded sales, coverage measurement, and near-term commercial debt timing. No API key, no signup, no OAuth for eight of the nine tools. A plain GET on the endpoint returns the full tool schemas and a worked example, so a client can evaluate the server before calling anything.

```
Server type: Hosted, remote (Streamable HTTP)
Endpoint: https://exchange-production-9123.up.railway.app/mcp
Auth: none for 8 of 9 tools (no key, no signup, no OAuth)
Registry: io.github.Capital-W-Holdings/us-property-parcel-real-estate-debt (v0.7.0)
Tools: 9 (what_can_dfx_answer, dfx_coverage, resolve_address, ownership, recorded sales, debt timing, ...)
Built by: DFX (dfxintel.com)
```

## Why This Matters for Operators

Real estate diligence is scattered across county recorders, assessor sites and data vendors. DFX packages the machine-callable core.

First, **self-describing.** `what_can_dfx_answer` tells the agent whether DFX can help with an objective, which tool to call, and returns a free sample. `dfx_coverage` reports measured coverage and known gaps, so the agent knows what it does not know.

Second, **debt timing is the differentiator.** Near-term commercial debt timing is exactly what operators miss when they only look at ownership and sales records.

Third, **evaluation before commitment.** The plain-GET schema dump means a developer or agent can inspect the full surface before calling any tool.

## Tools and Capabilities

| Tool | What it returns |
|------|-----------------|
| `what_can_dfx_answer` | Whether DFX can help with an objective, which tool to call, and a free sample |
| `dfx_coverage` | Measured coverage, served sources, object types, known gaps |
| `resolve_address` | A US street address resolved to parcel and property |
| Ownership and sales tools | Recorded sales, ownership and parcel records |
| Debt timing | Near-term commercial and multifamily debt maturity context |

## Verification (Aug 31, 2026)

- **Live JSON-RPC initialize verified**: POST to the endpoint returned `dfx-real-estate v0.2.0` with tools capability and instructions describing US commercial and multifamily intelligence with no key required.
- Submission (#3862) documents 9 tools, the no-auth posture, and the official registry record.
