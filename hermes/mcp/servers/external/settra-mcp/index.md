---
title: Settra MCP - Governed Tabular Data for AI Agents
description: Self-hosted MCP server that syncs Google Sheets, CSV, Excel and Parquet files into PostgreSQL and exposes durable snapshots through a governed semantic layer, so agents query operational data with approved definitions instead of raw SQL or source credentials.
category: Data & Analytics
stars: n/a (new listing)
added: 2026-09-06
source: mcpservers.org
relevance: ★★
tags: [postgresql, semantic-layer, data-governance, google-sheets, bi, dlt, self-hosted]
---

# Settra MCP - Governed Tabular Data for AI Agents

**MCP server (self-hosted)** - synchronizes source tabular data (Google Sheets, CSV, Excel and Parquet files selected from Google Drive) into PostgreSQL and exposes durable snapshots through a governed semantic layer. Agents discover exact schemas, inspect bounded samples and run structured queries without raw SQL or direct access to source credentials. Built for teams that want agents to work with operational data safely, consistently and repeatably.

```
Server type: self-hosted (managed hosting on request)
Auth: Google OAuth for Drive sources; MCP grants per workspace
Endpoint: your deployment (collection-scoped MCP URLs available)
Tools: schema discovery, bounded samples, structured queries over approved semantics
Pricing: open source self-host; managed hosting via support@outermeasure.com
Category: Data & Analytics
Built by: omhq (github.com/omhq/settra)
```

## Why This Matters for Operators

The operational spreadsheets that actually run a business - pipeline trackers, operations trackers, forecast models - live in Google Sheets and Excel files that change constantly. Handing an agent raw SQL access to a database is how tables get misread; handing it the sheets is how credentials leak. Settra sits between: files sync into PostgreSQL through a dlt full-sync pipeline, and the agent queries through a Cube-powered semantic layer where names, measures, dimensions and business definitions are approved ahead of time.

**The governance is the product: agents ask "summarize this month's pipeline" or "find overdue items in the operations tracker" and get bounded, structured results - not raw rows - while a per-source YAML controls parsing, schedules, schema contracts and descriptions.** Every account starts with a private personal workspace, and collections group related pipes into focused agent workspaces so an agent loads only the context it needs. Google OAuth refresh tokens are encrypted per workspace with the deployment secret and never stored in the product database or source YAML.

For operators, that converts "the numbers live in a spreadsheet somewhere" into a queryable, auditable surface that an agent cannot break with a bad join.

## Tools & Capabilities

| Capability | What an agent can do |
|---|---|
| Schema discovery | Discover exact schemas for registered pipes and destinations |
| Bounded inspection | Inspect bounded samples of synced data before querying |
| Structured queries | Run structured queries over the canonical semantic layer (measures, dimensions, business definitions) |
| Workspace selection | Ask which collection to use, load its context once, then query only its derived tables and cubes |
| Snapshot durability | Read the last successful PostgreSQL snapshot while a new load stages |

Settra detects file format, initial CSV delimiter, encoding and header row automatically, and performs complete replacement loads with dlt. Per-source YAML controls parsing overrides, selected sheets, schedules, types, names, schema contracts and descriptions. The tool list is served from your deployment after registration.

## Installation

```bash
git clone https://github.com/omhq/settra.git
cd settra
docker compose up -d
```

Requirements: a Google Cloud Web OAuth client and a browser-restricted Google Picker API key (Settra requests file-specific access only to files users select), plus PostgreSQL configured through the deployment's `POSTGRES_*` settings.

## Configuration

```json
{
  "mcpServers": {
    "settra": {
      "type": "http",
      "url": "https://your-settra-deployment/mcp"
    }
  }
}
```

A collection-specific MCP URL can pin an agent to one workspace; the global URL lets the agent ask which collection to use. MCP grants, connections and request metrics are isolated per workspace.

## Business Relevance

- **Ops teams** let agents answer tracker questions (overdue items, changed rows, target comparisons) from live sheets without credential sharing
- **Finance and revenue ops** reuse approved definitions like "active customer" or "recognized revenue" in every agent query
- **Data-governance-minded operators** keep raw SQL out of agent hands and approval semantics in the middle
- **Teams on spreadsheets today** get a durable PostgreSQL snapshot layer without abandoning the files they already use

## Integration with CorpusIQ

Settra complements CorpusIQ by covering the spreadsheet data layer that sits below formal systems of record. CorpusIQ reads the governed SaaS stack (QuickBooks, Stripe, HubSpot, GA4); Settra reads the operational files those systems do not see - pipeline trackers, forecast models, ops checklists - through the same governed philosophy. A composed workflow: an agent compares the pipeline in a Settra-synced sales sheet against closed-won revenue from CorpusIQ's Stripe connector, flags rows that changed or need follow-up, and reports with both sources named. Both surfaces keep writes out of agent hands.

## Limitations

- Self-hosted: you run PostgreSQL and the sync pipeline; managed hosting exists but is via email request
- Sources are Google Drive tabular files today (Sheets, CSV, Excel, Parquet) - no direct database or SaaS sources yet
- New listing (September 2026) - no long community track record
- Query results flow to the AI provider you connect, so that provider's retention policies apply
- The semantic layer must be authored per source for the governance to mean anything

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
