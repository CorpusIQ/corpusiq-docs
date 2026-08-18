---
title: "Moltline Studio MCP - CorpusIQ Docs - CorpusIQ Docs"
description: "A suite of 14 audited remote MCP servers for business operations - merchant math, CSV analytics, business-day math and agent governance"
category: Business Operations
stars: n/a (new listing)
added: 2026-08-18
source: mcp.so GitHub issues
relevance: ★★
tags: [business-math, analytics, csv, invoices, sla, governance, remote-mcp, suite]
---

# Moltline Studio MCP Suite

**A suite of 14 remote MCP servers from Moltline Studio — streamable-HTTP endpoints independently audited A/A+ on MCPize Verified, each serving a machine-readable server card at `/.well-known/mcp/server-card.json`.** The flagship set covers merchant math, paste-your-data analytics, business-day arithmetic, and agent governance; eight additional servers (humanizer, business, personal, creator, research, outbound, educator, skillmd-lint) round out the catalog. Anonymous free tier; premium tools unlock by license.

```
Server type: Remote (Streamable HTTP, session management, JSON-RPC-compliant errors)
Auth: Anonymous-open free tier; license for premium tools
Endpoints: https://mcp.moltlinestudio.com/{catalog,codereview,data,timeops,merchant,govern,...}
Tools: Suite-wide, per-endpoint schemas in server cards
Pricing: Free tier (no key); premium via license
Category: Business Operations / Analytics
Built by: Moltline Studio (moltlinestudio.com, GitHub: GarphenGate)
```

## Why This Matters for Operators

Most MCP servers answer a data question; these answer a math question. Operators constantly re-derive the same deterministic numbers — processor fees on a charge, net after fees, discount stacking, proration, installments, business-day deadlines, SLA windows, timezone overlaps — and usually by hand in a spreadsheet. Moltline's flagship servers compute them in code, deterministically, no external calls, with audit-grade reproducibility.

**The governance server is the outlier worth noting.** It audits MCP configurations, scores tool blast radius, and scans skill-file injection — the same hygiene CorpusIQ's own ecosystem increasingly demands as agent tool counts grow.

## Tools & Capabilities

| Endpoint | What it does |
|---|---|
| `/merchant` | Processor fees, charge-to-net, invoices, discount stacking, proration, installments |
| `/data` | Paste-your-data analytics: CSV profiling, A/B z-tests, funnels, cohorts, forecasts |
| `/timeops` | Business-day, deadline, SLA, and timezone-overlap math, deterministic |
| `/govern` | MCP config audits, tool blast-radius scoring, skill-file injection scans |
| `/catalog` | Search/load 138 agent persona and skill products; gateway skills free |
| `/codereview` | Diff triage, AI-code-smell scan, complexity and secret location reports |
| `/business`, `/research`, `/outbound`, `/creator`, `/humanizer`, `/personal`, `/educator`, `/skillmd-lint` | Supporting suite servers, same protocol and standard |

All endpoints speak MCP protocol 2025-06-18 with session management and JSON-RPC-compliant errors. Machine-readable server cards publish full tool schemas per endpoint.

## Installation

```json
{
  "mcpServers": {
    "moltline-merchant": {
      "type": "http",
      "url": "https://mcp.moltlinestudio.com/merchant"
    },
    "moltline-data": {
      "type": "http",
      "url": "https://mcp.moltlinestudio.com/data"
    }
  }
}
```

Add only the endpoints your workflow needs — each server is independent. The free tier is anonymous-open (no key needed to try); premium tools require a license.

## Configuration

No local state. Each endpoint can be attached to a client independently, which keeps the agent's tool surface lean. Fetch `https://mcp.moltlinestudio.com/<name>/.well-known/mcp/server-card.json` for a server's complete tool schema before wiring it in.

## Business Relevance

- **Finance operators** get charge-to-net and fee math without spreadsheet drift
- **Growth teams** run A/B z-tests, funnels, cohorts, and forecasts on pasted CSVs in chat
- **Ops managers** compute SLA and business-day deadlines deterministically across timezones
- **Agent-platform operators** audit their own MCP configs and tool blast radius with `/govern`
- **Agencies** license premium tools while the free tier covers evaluation

## Integration with CorpusIQ

CorpusIQ answers "what is the data" — connected, live, multi-source. Moltline answers "what is the math" — deterministic computation over numbers, whether they came from CorpusIQ, a CSV, or a conversation.

The composed workflow: CorpusIQ pulls live revenue and ad spend into the session; Moltline's merchant and data endpoints compute net-of-fees, run the A/B test, or project the cohort — the derived number is reproducible in code, not recomputed by hand. CorpusIQ's read-only retrieval model and Moltline's deterministic math are complementary halves of operator analytics.

## Limitations

- Suite model means multiple endpoints to manage — no single unified surface
- Free tier is anonymous; premium pricing is license-based and unpublished in the listing
- Newer publisher (submitted Aug 16, 2026) with no long track record
- Merchant-math and timeops tools assume operator-provided inputs; no data connectors included
- A/A+ audit covers protocol compliance, not business-data quality
