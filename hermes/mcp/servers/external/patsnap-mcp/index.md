---
title: "Patsnap Patent Literature Search MCP — Global IP Research for AI Agents"
description: "Professional MCP tool for searching Patsnap's global patent and literature databases using natural language, semantic, or keyword queries. Markdown-formatted bibliographic data."
category: mcp
tags: [mcp-server, patent-search, ip-research, competitive-intelligence, literature-search]
source: mcp.so
discovered: 2026-07-22
stars: 1
author: patsnap
github: https://github.com/patsnap
---

# Patsnap Patent Literature Search MCP

**Professional MCP server** for searching Patsnap's global patent and literature databases. Supports natural language, semantic, and keyword queries with precise filtering. Returns bibliographic data in Markdown format — ideal for AI agent consumption.

## Why It Matters for Operators

Patent and literature research is critical for operators in technology, manufacturing, biotech, and any industry where intellectual property drives competitive advantage. Patsnap MCP brings this capability directly into your AI agent's workflow.

Use cases for CorpusIQ operators:
- **Competitive Intelligence:** Search competitor patent portfolios to understand their R&D direction
- **Freedom to Operate:** Verify your product doesn't infringe existing patents before launching
- **Technology Scouting:** Discover emerging technologies and potential acquisition targets
- **Literature Review:** Search scientific literature for market research and due diligence
- **IP Portfolio Management:** Monitor your own patent landscape alongside business metrics

## Technical Details

| Field | Value |
|-------|-------|
| **Transport** | Likely Streamable HTTP |
| **Auth** | API Key (Patsnap account required) |
| **Category** | Search |
| **Source** | [mcp.so/servers/patsnap-patent-literature-search-mcp](https://mcp.so/servers/patsnap-patent-literature-search-mcp) |
| **Author** | Patsnap (patsnap.com) |
| **Created** | July 22, 2026 |
| **Stars** | ⭐ 1 |
| **Verified** | ✅ |

## Capabilities

- **Natural Language Search:** "Find patents related to AI-powered accounting automation"
- **Semantic Search:** Concept-based search beyond exact keyword matching
- **Keyword Search:** Traditional Boolean and field-specific queries
- **Precise Filtering:** Filter by jurisdiction, date range, assignee, IPC classification
- **Markdown Output:** Clean, structured bibliographic data ready for AI processing
- **Global Coverage:** Patsnap's database covers 170+ jurisdictions

## Setup

### Claude Desktop / Codex
```json
{
  "mcpServers": {
    "patsnap": {
      "type": "streamable-http",
      "url": "https://api.patsnap.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_PATSNAP_API_KEY"
      }
    }
  }
}
```

## CorpusIQ Integration

Patsnap MCP pairs with CorpusIQ for operator workflows:

1. **Competitive Intel Pipeline:** Patsnap patent search → CorpusIQ company financials → comprehensive competitor profile
2. **M&A Due Diligence:** Patsnap IP portfolio analysis + CorpusIQ financial data + DataNexus MCP for vendor verification
3. **R&D Prioritization:** Patsnap technology landscape + CorpusIQ market data = data-driven R&D investment decisions

## Limitations

- Requires Patsnap subscription/account (enterprise pricing)
- New MCP server (July 22, 2026) — early-stage, API may evolve
- Patent data is inherently complex — agents may need guidance on search strategy
- Not all jurisdictions may have full-text searchable patents

## See Also

- [[index]] — Full external MCP catalog
- [[datanexus-mcp]] — Public data intelligence (patents, contracts, vulnerabilities)
- [[sugra-api-mcp]] — Comprehensive business data MCP
- [[sam-gov-mcp]] — Government contracting MCP
