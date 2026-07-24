---
name: "iGaming Tools MCP"
description: "Structured iGaming reference data — slot specs, RTP variants, providers, regulators, news and jobs"
category: "Database"
source: "mcpservers.org"
discovered: "2026-07-23"
verified: true
remote_endpoint: "https://i-gaming.tools/docs/mcp/"
---

# iGaming Tools MCP — Gaming Industry Reference Data

A structured MCP server providing iGaming reference data: slot specifications, RTP (Return to Player) variants, game providers, regulatory information, industry news, and job listings.

## What It Does

- **Slot database** — Technical specifications, RTP percentages, volatility ratings for thousands of slots
- **Provider directory** — Game providers with portfolio overviews and market presence
- **Regulatory data** — Licensing jurisdictions, compliance requirements, restricted markets
- **Industry news** — Curated iGaming news feed
- **Job listings** — Industry job postings

## Quick Start

```bash
# Remote endpoint
hermes mcp add igaming-tools --url https://i-gaming.tools/mcp

# Or Claude Code
claude mcp add igaming-tools --url https://i-gaming.tools/mcp
```

**Prerequisites:** Check i-gaming.tools for API access requirements.

## Key Tools

| Tool | Description |
|------|-------------|
| `search_slots` | Search slot games by name, provider, RTP range |
| `get_slot_specs` | Full technical specs for a specific slot |
| `list_providers` | Browse game providers with portfolio stats |
| `get_regulatory_info` | Licensing requirements by jurisdiction |
| `get_industry_news` | Latest iGaming industry headlines |
| `search_jobs` | Find iGaming industry job listings |

## Use Cases

- **Competitive analysis** — Compare slot portfolios across providers
- **Market research** — Analyze RTP trends, volatility preferences by region
- **Compliance** — Check regulatory requirements before entering new markets
- **Content creation** — Pull slot data for reviews, comparison articles

---

*Discovered via [mcpservers.org](https://mcpservers.org) sweep. Listed in the [CorpusIQ MCP Catalog](https://corpusiq-docs/hermes/mcp/).*
