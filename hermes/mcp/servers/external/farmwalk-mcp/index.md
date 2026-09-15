---
title: "Regeno Farmwalk MCP - UK Farm and Subsidy Data for Agents"
description: "UK farm and subsidy data for agents: organisations, farms, agreements, compliance scores, land parcels, vault documents and tasks with 24 OAuth-scoped tools."
category: Business Operations
stars: n/a (no public repo)
added: 2026-09-03
source: mcpservers.org
relevance: ★★
tags: [agriculture, farm-management, compliance, subsidies, operations, land-data, remote-mcp]
---

# Regeno Farmwalk MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 with PKCE)** - Farmwalk connects an AI assistant to UK farm and subsidy data: scheme agreements, compliance scores, land parcels, evidence tracking, document vaults, task management and consultation transcripts, with interactive Mapbox maps rendered in chat.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 PKCE (scopes farmwalk:read / farmwalk:write); PAT fallback
Endpoint: https://farmwalk.app/mcp
Tools: 24 (21 data tools, 3 interactive app tools)
Pricing: Farmwalk platform account
Category: Business Operations
Built by: Regeno (farmwalk.app/ai/mcp)
```

## Why This Matters for Operators

UK farm operators carry a compliance burden that is punishingly document-heavy: SFI, Countryside Stewardship, Red Tractor and H&S schemes each have agreements, evidence links, deadlines and payment conditions, all tracked across parcels and hedgerows. Farmwalk makes that dataset queryable by an assistant with scheme-aware tools instead of spreadsheets.

**The compliance angle is the operator value:** a compliance summary aggregates scores, item counts and upcoming deadlines across farms, evidence status tracks completion per agreement, and the interactive dashboard renders scheme scores and deadlines in chat. The vault search covers documents, photos, audio and video by name or AI transcription - so a photograph of a hedgerow taken in 2024 becomes a findable compliance record.

## Tools & Capabilities

Twenty-one data tools plus three interactive app tools; representative set:

| Tool | Purpose |
|---|---|
| list_organisations / list_farms / get_farm | Organisations, farms with SBI and CPH numbers, full farm details |
| list_agreements / get_agreement | Scheme agreements with items, payments and inspections |
| get_compliance_summary | Aggregated compliance scores, item counts, upcoming deadlines |
| list_evidence / get_evidence_status | Evidence links and completion status per agreement |
| list_parcels / get_parcel | Land parcels, fields, hedgerows with geometry and scheme items |
| list_vault_files / search_vault | Documents, photos, audio and video, searchable by AI transcription |
| list_tasks / create_task / update_task | Task management with priorities and assignees |
| search | Unified search across farms, agreements, vault and tasks |
| list_consult_sessions / get_consult_summary / get_consult_actions | Consultation transcripts, AI summaries and extracted actions |
| show_parcel_map / show_farm_map / show_compliance_dashboard | Interactive Mapbox satellite maps and compliance dashboard in chat |

## Installation

```bash
claude mcp add farmwalk --transport http https://farmwalk.app/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "farmwalk": {
      "type": "http",
      "url": "https://farmwalk.app/mcp"
    }
  }
}
```

First use opens the browser for OAuth 2.1 with PKCE; the operator approves read-only or read-and-write scopes. For clients without OAuth support, a Personal Access Token from Settings, Security, Personal Access Tokens can be sent as the authorization header instead.

## Business Relevance

- **Farm operators** query agreements, deadlines and evidence across all farms in plain language
- **Agronomists and agents** check scheme compliance and task status from chat
- **Land managers** review parcel maps and compliance dashboards without a dashboard login

## Integration with CorpusIQ

Farmwalk is a vertical sibling of CorpusIQ's horizontal approach: CorpusIQ reads the financial and commercial systems around a business (QuickBooks, Stripe), while Farmwalk reads the operational and compliance layer of a farm. A composed workflow: CorpusIQ's QuickBooks connector tracks subsidy payments as they land, Farmwalk shows which agreements and evidence deadlines those payments correspond to, and the operator gets a single assistant that reconciles compliance work with the money it generates.

## Limitations

- UK farm and subsidy data only - single-market vertical
- Platform account required; no anonymous tier
- Write scope covers task management, not scheme submissions
- Newer listing; verify live tool names against the endpoint after connecting

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [ZenSched MCP - Field Workforce Scheduling for Agents](/docs/hermes/mcp/servers/external/zensched-mcp)
- [Worklittle Jobs MCP - Job Search and Market Data for AI Agents](/docs/hermes/mcp/servers/external/worklittle-jobs)
