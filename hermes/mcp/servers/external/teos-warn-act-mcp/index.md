---
title: "TEOS WARN Act Layoff Intelligence MCP"
description: "Hosted MCP server for US WARN Act mass-layoff intelligence - 5,964 normalized layoff and plant-closing notices covering 545,647 workers across CA, TX, NY, IL and NC, refreshed every 12 hours from primary state sources with provenance back to the originating filing. For layoff tracking, corporate distress and alternative-data signals, employment-law research, and recruiting or outplacement lead generation."
category: Compliance
stars: n/a (hosted, no public repo)
added: 2026-08-23
source: "mcp.so feed (Aug 23) + tppflow.com/llms.txt"
relevance: ★★★
tags: [warn-act, layoffs, labor-market-data, corporate-distress, alternative-data, hr-compliance, remote-mcp]
last_updated: "2026-10-24"
---

# TEOS WARN Act Layoff Intelligence MCP

**US WARN Act mass-layoff intelligence as a hosted MCP server - 5,964 normalized layoff and plant-closing notices covering 545,647 affected workers across California, Texas, New York, Illinois and North Carolina, refreshed every 12 hours from primary state government sources with provenance back to the originating filing.** WARN notices are the legally mandated filings US employers submit before a mass layoff or plant closing. Each state publishes them differently (spreadsheets, PDFs, dashboards); TEOS normalizes them into one queryable schema.

```
Server type: Remote (Streamable HTTP, hosted)
Auth: API key (Bearer header)
Endpoint: https://mcp.tppflow.com/mcp
Coverage: 5,964 notices, 545,647 workers, 5 states (CA, TX, NY, IL, NC)
Refresh: every 12 hours from primary state sources
Pricing: API key required (check tppflow.com for plans)
Category: Compliance / Labor market data
Built by: TEOS (tppflow.com)
```

## Why This Matters for Operators

Layoff data is a leading indicator that moves faster than headlines: a supplier quietly filing a 400-worker WARN notice is a credit risk, a sales opportunity for outplacement services, and a talent-pool signal all at once. Normally that data is scattered across five state websites in incompatible formats, which means nobody checks it until a news story breaks. TEOS puts the normalized corpus inside the agent you are already using, so screening questions like "which Texas manufacturers filed notices over 100 workers in the last quarter" become one tool call with provenance back to the state filing.

The dataset carries the fields that matter for triage: employer name, workers impacted, headcount, effective date, notice filing date, county, and layoff type (layoff vs plant closing). Because every record traces back to the state's original artifact, the agent can cite the source instead of asserting a number it can not defend.

## Tools & Capabilities

The MCP tool list is served live from the endpoint (the directory listing shows no static tool names), and mirrors the documented REST surface. The documented capability set:

| Capability | What it returns |
|---|---|
| WARN notices query | Filter by state (2-letter), company (substring), effective-date range, location (substring), limit 1-1000 with offset |
| Corpus stats | Coverage by state with the latest effective date per state |

State coverage as published (llms.txt, Aug 23): California 1,730 notices (latest effective date 2027-02-01), Texas 2,358 (2026-09-30), New York 260 (2027-03-31), Illinois 1,380 (2028-02-01), North Carolina 236 (2027-12-31).

The same data is available as a plain REST API at `api.tppflow.com` (`GET /api/v1/warn/notices`, `GET /api/v1/warn/stats`) with an OpenAPI spec at `api.tppflow.com/.well-known/openapi.json`.

## Installation

```bash
claude mcp add teos-warn --transport http https://mcp.tppflow.com/mcp --header "Authorization: Bearer YOUR_API_KEY"
```

## Configuration

```json
{
  "mcpServers": {
    "teos-warn": {
      "type": "http",
      "url": "https://mcp.tppflow.com/mcp",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```

The API key is obtained from tppflow.com. Connection guides exist for Claude Code, Codex, Cursor and VS Code on the mcp.so listing page.

## Business Relevance

- **Recruiting and outplacement firms** get a live lead list of employers filing mass-layoff notices, filterable by state, date and headcount, before news coverage catches up.
- **Credit and supplier-risk analysts** can flag counterparties entering distress: a plant closing in the portfolio is an early warning with a legal paper trail.
- **HR and employment-law teams** research WARN compliance patterns and regional layoff trends from primary sources with citable provenance.
- **Alternative-data investors** get a 12-hour-fresh, normalized distress signal that is public-record based and reproducible.
