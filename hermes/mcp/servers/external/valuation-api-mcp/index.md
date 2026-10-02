---
title: "Valuation API MCP - Deterministic Finance Math for Agents"
description: "Deterministic finance calculation engine exposed as an MCP server: IRR, NPV, MOIC, DCF, WACC and IRR sensitivity analysis as six typed tools wrapping pure mathematical functions. No LLM generation, no randomness. Live-probed keyless endpoint built and operated by Prospect Capital Labs for investment analysis and due diligence workflows."
category: Finance
stars: 0
added: 2026-09-02
source: "mcp.so GitHub issue #3900"
relevance: ★★
tags: [valuation, dcf, irr, npv, wacc, financial-modeling, investing]
---

# Valuation API MCP - Deterministic Finance Math for Agents

**Hosted Streamable HTTP MCP server** - six deterministic finance tools (IRR, NPV, MOIC, DCF, WACC, IRR sensitivity) wrapping pure mathematical functions. Verified live with a keyless probe: serverInfo valuation-api v0.3.0 and all six tools returned.

## Spec Block

| Field | Value |
|---|---|
| Server name | valuation-api |
| Endpoint | https://api.finance-tools.io/mcp |
| Transport | Streamable HTTP (JSON-RPC 2.0) |
| Auth | none observed (keyless probe succeeded) |
| Repo | github.com/johnbehar1500-ux/valuation-api |
| Operator | Prospect Capital Labs (prospectcapital.com) |
| License | MIT |
| Stars | 0 (brand new) |

## Why This Matters for Operators

The classic agent failure mode in finance is confidently wrong arithmetic. This server removes that: IRR, NPV, MOIC, DCF and WACC are computed by deterministic typed functions rather than an LLM doing mental math, so investment memos, cap-table analyses and due-diligence outputs carry numbers an analyst can reproduce.

## Tools & Capabilities (6 tools)

| Tool | Description |
|---|---|
| calculate_irr | Internal rate of return from a cash-flow schedule |
| calculate_npv | Net present value at a given discount rate |
| calculate_moic | Multiple on invested capital |
| calculate_dcf | Discounted cash-flow valuation |
| calculate_wacc | Weighted average cost of capital |
| irr_sensitivity | IRR sensitivity analysis across input ranges |

## Installation

Add as a remote MCP server with the endpoint URL. No API key was required at probe time; treat keyless availability as current but confirm on the homepage if the service changes.

## Configuration

No configuration observed. Endpoint accepts standard Streamable HTTP MCP initialize and tools/list calls.

## Business Relevance

Useful for: private-equity and VC analysts running quick DCF and MOIC checks, founders modelling round economics, and agents assembling investment memos where the math must be reproducible and defensible.

## Integration with CorpusIQ

Pairs with CorpusIQ's finance and company-data connectors: an agent can pull company financials through CorpusIQ, then hand the figures to Valuation API for deterministic DCF, IRR and WACC computation in the same workflow.

## Limitations

Brand new listing (repo created Sep 2, 2026, zero stars). Calculation-only surface: no market data feeds or company fundamentals included. Treat outputs as computation, not investment advice.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [FinBridge MCP - Korean and US Market Data for Agents](/hermes/mcp/servers/external/finbridge-mcp)
- [Fruit Stand Fund Returns MCP - US Fund and ETF Performance Data](/hermes/mcp/servers/external/fruitstand-fund-returns-mcp)
