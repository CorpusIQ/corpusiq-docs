---
title: "GreenCalculus MCP: Audit-Traced Carbon Accounting"
description: "Hosted MCP server for sourced greenhouse-gas emission factors and audit-traced carbon calculations - lookup, search and resolve factors, then calculate activity, electricity, embodied, PCAF financed, freight, spend and business-travel emissions. Every value returns its source cell and pinned data version."
category: Compliance
stars: 0
added: 2026-08-23
source: "mcpservers.org /all + GitHub README"
relevance: ★★★
tags: [carbon-accounting, esg, csrd, emission-factors, ghg-protocol, pca-f, sustainability, remote-mcp]
last_updated: "2026-10-19"
---

# GreenCalculus MCP

**Sourced greenhouse-gas emission factors and audit-traced carbon calculations as an MCP server - every value comes back with its exact source cell and a pinned data version, so an agent hands back a number a person can cite and a machine can reproduce instead of a guess.** The server is remote-first: point your client at the URL with a Bearer key, or use the thin stdio/Docker bridge for clients that can only spawn local processes.

```
Server type: Remote (Streamable HTTP, hosted) with stdio/Docker bridge
Auth: Bearer API key (free key at greencalculus.com)
Endpoint: https://mcp.greencalculus.com
Official registry: com.greencalculus/api
Tools: 11 (factor lookup/search/resolve + 8 calculators)
Category: Compliance / ESG
Built by: jeremiahsay (GitHub, MIT)
```

## Why This Matters for Operators

CSRD and supplier ESG programs have turned carbon numbers from marketing copy into audited disclosures - and most of the numbers floating around are LLM guesses with no source. GreenCalculus attacks exactly that failure mode: every factor carries its source and version, `explain_absence` says why a factor does not exist instead of returning nothing, and the calculators are explicit about what they omit (for example, embodied-carbon runs flag missing lifecycle stages under EN 15978). The output is reproducible: same inputs, same pinned data version, same number - which is what an auditor actually wants.

The factor tools close the researcher's loop: search the corpus by free text, resolve a messy real-world description ("cubic meter of ready-mix concrete in France") to the best-matching factor, and fetch one factor by key with provenance. The emission-factor data returned by the API carries the license of its underlying source, named in every response.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `lookup_factor` | Fetch one emission factor by key, with its source and version |
| `search_factors` | Search the factor corpus by free text |
| `resolve_factor` | Map a messy real-world description to the best-matching factor |
| `explain_absence` | Say why a factor does not exist, rather than returning nothing |
| `calculate_activity` | Activity to emissions, with unit conversion and GHG Protocol scope |
| `calculate_electricity` | Location-based and market-based electricity |
| `calculate_embodied` | Embodied carbon (EN 15978), explicit about missing lifecycle stages |
| `calculate_pcaf` | PCAF financed emissions, with the audit trail |
| `calculate_freight` | Freight by mode, distance and load |
| `calculate_spend` | Spend-based EEIO |
| `calculate_business_travel` | Business travel across modes |

## Installation

```bash
claude mcp add --transport http greencalculus https://mcp.greencalculus.com --header "Authorization: Bearer YOUR_KEY"
```

For stdio-only clients: `npx -y greencalculus-mcp` with `GREENCALCULUS_API_KEY`, or Docker (`docker run -i --rm -e GREENCALCULUS_API_KEY greencalculus/mcp` - the `-i` flag is required and `-t` must be omitted). `GC_API_KEY` is accepted as an alias for the key variable.

## Configuration

```json
{
  "mcpServers": {
    "greencalculus": {
      "url": "https://mcp.greencalculus.com",
      "headers": { "Authorization": "Bearer YOUR_KEY" }
    }
  }
}
```

Free keys at greencalculus.com. A REST API with docs and Python/JS SDKs is also published (greencalculus.com/developers).

## Business Relevance

- **CSRD-reporting companies** get audit-traced calculations with pinned data versions and named sources instead of unauditable LLM math.
- **Supply-chain and procurement teams** calculate freight, spend and activity emissions inside the agent that runs their vendor analysis.
- **Financial institutions** use the PCAF tool for financed-emissions estimates with a full audit trail.
- **Sustainability consultants** resolve messy client descriptions to correct factors with provenance, and explain gaps honestly.
