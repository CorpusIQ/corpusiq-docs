---
title: "upCampo MCP - Farm Management Data for AI Agents"
description: "upCampo MCP bridges the upCampo farm management system to Claude and ChatGPT over Streamable HTTP with OAuth sign-in. Agents query production and harvest progress, per-hectare yields, rain per field, pest alerts, work orders, stock minimums, fleet fuel consumption, post-harvest bales and cost per hectare, with per-farm read permissions and confirmed write actions."
category: Business Operations
stars: n/a (new listing)
added: 2026-09-12
source: "mcpservers.org /all page 1 (night crawl) + vendor docs at upcampo.com.br"
relevance: ★★★
tags: [agriculture, farm-management, field-operations, inventory, oauth, remote-mcp, streamable-http]
---

# upCampo MCP

**Remote MCP server (Streamable HTTP, OAuth with upCampo account)** - the assistant channel for upCampo, a Brazilian farm management platform. The same data the UPí WhatsApp assistant consults becomes available inside Claude and ChatGPT: production and harvest, per-field rain, pest alerts, work orders, stock, fleet and costs, with the operator's existing upCampo permissions enforced per farm. Reads on everything, writes only where the user already has posting permission and only with confirmation.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in with an existing upCampo account (ChatGPT plans: Business, Enterprise, Edu)
Endpoint: https://mcp.upcampo.com.br/mcp
Tools: Capability-level (exact tool names not published; permission-mapped per farm)
Pricing: Included in the upCampo UPí module contract (annual, farm-size based)
Category: Business Operations
Built by: upCampo (upcampo.com.br)
```

## Why This Matters for Operators

Farm operations data usually lives in a portal that a manager visits between field rounds. upCampo MCP puts the same data in the assistant the operator already uses: "how much did it rain on field 12 this month" and "which pesticides are below minimum stock" become natural-language questions answered from the live system, not from memory. The permission model is the notable part - the assistant only sees farms the user can already access, each data theme (crops, weather, stock, fleet) carries its own read permission, and writes require the user's existing posting rights plus confirmation. It never deletes anything.

## Tools & Capabilities

Exact tool names are not published; the vendor documents the query surface, which maps to upCampo data themes with per-farm read permissions. Capability-level table from the vendor docs:

| Theme | What the agent answers | Permission |
|---|---|---|
| Production | Harvest progress by sector, productivity per hectare by variety, post-harvest bales and yields | Consulta do tema Lavoura |
| Weather | Rain per field over any period | Consulta do tema clima |
| Pests | Pests above alert level in the latest scouting | Consulta do tema pragas |
| Work orders | Open agricultural orders and their area | Consulta do tema ordens de serviço |
| Stock | Products below minimum stock levels | Consulta do tema estoque |
| Fleet | Active equipment, average fuel consumption | Consulta do tema frota |
| Costs | Cost per hectare per field per season | Consulta do tema custos |
| System help | How-to answers from the help center, no permission needed | None |

Writes cover rain records, supply events and work-order execution - only where the user already has posting permission in upCampo, always with confirmation.

## Installation

1. Prerequisite: the UPí module contracted on the upCampo account, an active portal login, and query permissions released by the company admin (portal, access control, permissions starting with "Consulta do tema").
2. Claude: Settings, Connectors, add custom connector, enter `https://mcp.upcampo.com.br/mcp`, sign in with the upCampo account.
3. ChatGPT: Plugins, enable developer mode (Business plans via workspace admin), create a plugin with the endpoint, choose OAuth, scan tools, sign in.

## Configuration

```json
{
  "mcpServers": {
    "upcampo": {
      "url": "https://mcp.upcampo.com.br/mcp"
    }
  }
}
```

If the connection returns "acesso ainda não liberado" after login, the account is fine - the missing piece is the admin's query permission for that farm. Multi-farm accounts answer for the current farm and switch by name in the question.

## Business Relevance

- **Farm managers** get field-level answers (rain, pests, stock, work orders) without building reports in the portal.
- **Agronomists** query yields by variety and pest pressure by field for scouting decisions.
- **Operations directors** track costs per hectare per season across farms from one assistant.
- **Fleet and stock teams** catch minimum-stock and fuel-consumption issues in natural language.

## Integration with CorpusIQ

upCampo demonstrates the vertical-SaaS connector pattern with the permission discipline CorpusIQ requires: per-farm, per-theme reads and confirmed writes. For operators in the Brazilian agribusiness market, a CorpusIQ agent could combine upCampo field data with financial and marketplace connectors in one operational view. The capability-level tool surface also makes upCampo a good reference for how CorpusIQ documents permission-mapped connectors.

## Limitations

- Portuguese-language vendor docs and Brazilian-market platform; no English documentation yet.
- Exact tool names are not published - the agent surface is permission-mapped per farm, so capability tables are the only public contract.
- Requires the UPí module contract; no free tier or API-key path.
- Region-specific vertical: relevance outside Brazilian agribusiness is limited.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Regeno Farmwalk MCP - UK Farm and Subsidy Data for Agents](/hermes/mcp/servers/external/farmwalk-mcp/)
- [ReelsFarm MCP - AI Short-Form Content with Approval-Gated Publishing](/hermes/mcp/servers/external/reelsfarm-mcp/)
