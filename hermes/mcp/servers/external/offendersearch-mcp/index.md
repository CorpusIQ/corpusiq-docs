---
title: "OffenderSearch MCP: Nationwide Registry Screening"
description: "Search all 58 US sex-offender registries - every state, DC and the territories - in one tool call with scored, de-duplicated, provenance-tagged records. batch_search for up to 1,000 lookups, registry coverage catalog, 25 free searches, metered pricing from $0.15 per call."
category: Compliance
stars: 0
added: 2026-08-23
source: "mcpservers.org /all + GitHub README + vendor page"
relevance: ★★★
tags: [background-screening, public-records, safety-compliance, hr-screening, registry-search, staffing, remote-mcp]
last_updated: "2026-10-19"
---

# OffenderSearch MCP

**Search all 58 US sex-offender registries - every state, DC and the territories - from any MCP client in one tool call, with scored, de-duplicated, provenance-tagged records built on a continuously updated national dataset with 100% US coverage.** One call returns `matchConfidence`, `matchBasis` (why it matched), DOB verification state, aliases, addresses, offense detail, and a per-source citation with `lastCheckedAt` - so an agent can cite exactly which registry said what.

```
Server type: Local stdio or remote (Streamable HTTP, self-hostable)
Auth: API key (free tier: 25 searches, no card required)
Tools: 3 (search_offenders, batch_search, get_registry_coverage)
Pricing: metered, $0.15 per call, volume tiers (offendersearch.app/pricing)
Built with: official Python MCP SDK (FastMCP)
Category: Compliance / Screening
Built by: Offendersearch (offendersearch.app)
```

## Why This Matters for Operators

A nationwide background check across 58 registries is normally either a slow manual grind or an enterprise contract. OffenderSearch collapses it to one tool call with a scored result set: per-registry outcomes (`sourceStatus`), plain-language warnings, and citations that name the registry and when it was checked. For staffing firms, property managers, healthcare providers and screening platforms, that turns "run a check" into something an agent can do inside an existing workflow - with the compliance boundary stated up front: results are public-record data and not a consumer report, and must not be used for FCRA-covered decisions without appropriate process.

The batch tool is the operator feature: up to 1,000 lookups in one call, row-in row-out, each through the same engine as a single search - the difference between screening one applicant and screening an applicant pool.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `search_offenders` | Search every registry for one person or location - name, DOB, age, city/state/ZIP, street address, GIS radius, or free text. Returns scored matches with per-registry outcome and plain-language warnings |
| `batch_search` | Up to 1,000 lookups in one call, row-in/row-out, same engine as single search |
| `get_registry_coverage` | Public coverage catalog: every registry code, scope, legal status and health; no API key needed |

## Installation

```bash
# Local stdio (from the repo)
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

`claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "offendersearch": {
      "command": "python",
      "args": ["/path/to/services/mcp-server/server.py"],
      "env": { "OFFENDERSEARCH_API_KEY": "os_live_..." }
    }
  }
}
```

## Configuration

For a self-hosted remote instance (per-request key, multi-tenant by design):

```bash
MCP_TRANSPORT=streamable-http OFFENDERSEARCH_API_KEY="os_live_..." python server.py
```

Keys are free to create at offendersearch.app/sign-up and work immediately (25 free searches, no card). The hosted endpoint setup is documented on the vendor's MCP server page (offendersearch.app/mcp-server); API reference and OpenAPI at offendersearch.app/docs.

## Business Relevance

- **Staffing and property-management operators** run registry checks inside existing agent workflows instead of a separate tab per candidate.
- **Healthcare and screening providers** get a documented API and MCP surface with HIPAA-aware enterprise options (BAA available).
- **Volume screeners** use `batch_search` for pools up to 1,000 lookups per call at metered pricing.
- **Compliance teams** get citations per record - registry, status, and last-checked date - for defensible screening logs.
