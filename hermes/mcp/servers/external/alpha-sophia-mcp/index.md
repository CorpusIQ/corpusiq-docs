---
title: "Alpha Sophia MCP - US Healthcare Provider and Market Data"
description: "Official Alpha Sophia MCP server for US healthcare market intelligence: resolve providers, organizations, and sites of care, run filtered searches and counts, and size markets across procedures, diagnoses, affiliations, publications, and clinical trials. OAuth remote HTTP."
category: Data & Analytics
stars: 0
added: 2026-08-25
source: mcp.so homepage
relevance: ★★★
tags: [mcp-server, healthcare, providers, market-sizing, clinical-trials, life-sciences]
---

# Alpha Sophia MCP

**The commercial healthcare data layer for agents.** Alpha Sophia maintains a database of every US healthcare provider (HCP), healthcare organization (HCO), and site of care, with attributes spanning procedures (CPT/HCPCS), diagnoses (ICD-10 and CCSR), provider taxonomy and specialty, location, affiliations, prescriptions, open payments, education, publications, and clinical trials. The MCP server exposes that data as agent tools for list building and market sizing.

```
Server type: Remote Streamable HTTP (hosted)
Endpoint: https://api.alphasophia.com/v1/mcp
Auth: OAuth sign-in with an Alpha Sophia account (no API key or env var)
Tools: resolve_entity, search/count/market_size (providers, sites of care), search/count (clinical trials, investigators, publications, authors)
Repo: github.com/alphasophia/claude-plugins (proprietary license)
Requires: API and Agent modules enabled, active subscription, agent token balance
```

## Why This Matters for Operators

Healthcare targeting is a filter problem: the right providers for a launch hide behind taxonomy codes, procedure volumes, and affiliation data. Alpha Sophia compresses the workflow into resolve-then-filter tools. `resolve_entity` maps an ambiguous name to a canonical entity before any filtering runs, and the `search`/`count`/`market_size` pairs let an agent build a candidate list, validate its size, and then quantify the market before anyone commits budget. The bundled Claude Code Skill encodes the same resolve-before-filter rules the vendor's in-app assistant uses, so the agent applies the platform's own playbook instead of improvising filters.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `resolve_entity` | Resolves a name to a canonical healthcare entity before filtering |
| `search` / `count` | Filtered search and counts for providers and sites of care |
| `market_size` | Market sizing over providers and sites of care for a filter set |
| `search` / `count` (research) | Search and counts for clinical trials, investigators, publications, and authors |

The remote server exposes the MCP surface over HTTP at `api.alphasophia.com/v1/mcp`; the plugin repo bundles the same tools with a Skill that teaches the agent resolve-before-filter usage, providers vs sites of care distinctions, the filter DSL, and worked examples.

## Installation

The vendor distributes this as a Claude Code plugin that wires MCP automatically:

```shell
/plugin marketplace add alphasophia/claude-plugins
/plugin install alpha-sophia@alpha-sophia
```

The MCP endpoint itself can be added directly to any MCP client that supports OAuth at `https://api.alphasophia.com/v1/mcp`.

## Configuration

On first tool call the client prompts for Alpha Sophia account sign-in and access approval. The organization must have the API and Agent modules enabled, an active subscription, and agent token balance. No API key or environment variable is required.

## Business Relevance

- **Targeting:** build lists of the right providers by specialty, procedures, and location.
- **Market sizing:** quantify a market before sales territory or launch decisions.
- **KOL mapping:** find top authors and investigators in a therapy area.
- **Commercial due diligence:** affiliations, open payments, and publication history in one query.

## Integration with CorpusIQ

Alpha Sophia's structured JSON output pairs with CorpusIQ connectors for the commercial side of healthcare operations: load target lists into your CRM (HubSpot or Close), attach market-size evidence to deal records, and reconcile launch planning in Notion or Airtable so the data and the pipeline live in one place.

## Limitations

- Requires a paid Alpha Sophia subscription with the API and Agent modules enabled.
- The public repo is a generated distribution of the commercial monorepo (proprietary license, 0 stars).
- Endpoint enumeration is refused without OAuth (401 on anonymous initialize); the tool list above comes from the vendor's plugin documentation.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Korea Business Verify - Real-Time Korean Business Verification](/docs/hermes/mcp/servers/external/korea-business-verify)
