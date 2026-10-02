---
title: "Insourcia MCP - French Company Intelligence for AI Agents"
description: "Hosted French company intelligence MCP server: search companies by name or SIREN/SIRET and pull financials, directors, ownership graphs, M&A and insolvency events. OAuth or API-key auth."
category: Business Intelligence
stars: n/a (hosted, no public repo)
added: 2026-08-29
source: mcpservers.org /all page 2
relevance: ★★★
tags: [mcp-server, company-data, french-registry, siren, ownership, due-diligence, business-intelligence, remote-mcp]
---

# Insourcia MCP

**The official MCP server for Insourcia, a French company-intelligence platform: search French companies by name or SIREN/SIRET and pull financials, directors, ownership graphs, M&A and insolvency events into any MCP client.** The hosted server exposes the same tool catalogue as Insourcia's REST tools RPC endpoint, with two authentication modes - OAuth for clients that support it, and API-key-in-URL for everything else.

```
Server type: Remote (Streamable HTTP), hosted
Auth: OAuth (mcp.insourcia.io/mcp) or API key embedded in URL (minted in account settings)
Endpoint: https://mcp.insourcia.io/mcp
Tools: Same catalogue as Insourcia's /v1/rpc/tools REST endpoint
Pricing: Account-based; sign up at app.insourcia.io
Category: Business Intelligence / Company Data
Built by: Insourcia (insourcia.io); listed on Smithery and the official MCP registry
```

## Why This Matters for Operators

French counterparty research outside France means fighting the SIREN/SIRET identifiers, the ownership graphs, and the French-language registry interfaces at once. Insourcia packages the whole thing behind one native MCP endpoint: an agent searches by company name or identifier and gets financials, directors, ownership graphs, M&A events, and insolvency history in a single structured response, ready to fold into a due-diligence memo or a supplier file.

The two-mode auth is built for the way agent teams actually run: OAuth for Claude-style clients, and a per-account URL with the key embedded for everything from n8n to custom tools. The same catalogue also ships as a REST tools RPC endpoint, so non-MCP systems can call the identical surface.

**French company intelligence becomes one structured MCP call with ownership graphs and insolvency history attached.**

## Tools & Capabilities

Capability-level from the vendor's docs and listing; the tool catalogue mirrors the REST /v1/rpc/tools endpoint and exact names are visible after connecting (anonymous enumeration is not published).

| Capability area | What the agent can do |
|---|---|
| Company search | Find French companies by name or SIREN/SIRET identifiers |
| Financials | Pull reported financial data for a company |
| Governance | Read directors and leadership records |
| Ownership | Traverse ownership graphs and corporate structure |
| Events | Retrieve M&A and insolvency events tied to a company |

## Installation

```bash
claude mcp add --transport http insourcia https://mcp.insourcia.io/mcp
```

OAuth clients connect to the endpoint directly and approve in the browser. For API-key mode, open app.insourcia.io/settings?tab=api and copy the ready-made URL with your key from the API/MCP tab; the docs (insourcia.io/guides/mcp, in French) walk through Claude Desktop, Cursor, Smithery toolbox, and n8n/Zapier/Make integrations.

## Configuration

```json
{
  "mcpServers": {
    "insourcia": {
      "type": "http",
      "url": "https://mcp.insourcia.io/mcp"
    }
  }
}
```

Toggle between OAuth and API-key mode in the account settings; the key-embedded URL is the drop-in option for clients without OAuth support.

## Business Relevance

- **Due-diligence and compliance teams** get ownership graphs, financials, and insolvency events for French counterparties in one call.
- **Procurement** pre-screens French suppliers by SIREN before contracts, with the governance structure surfaced alongside.
- **Finance and legal staff** run M&A and insolvency event checks without navigating French registry portals.
- **Agent stacks covering European markets** add French coverage that integrates natively instead of scraping.

## Integration with CorpusIQ

Insourcia extends the same pattern as the catalog's other regional verification servers: a CorpusIQ workflow can take a French supplier from the CRM or QuickBooks, resolve its SIREN via Insourcia, and write the ownership graph and insolvency history back into the account record. Paired with CorpusIQ's general connectors, operators get a single agent pass that covers both the relationship state (CRM, billing) and the counterparty's public-registry reality (Insourcia), which is exactly the split a supplier-review checklist needs.

## Limitations

- French market only - no cross-border coverage.
- Account required; no anonymous or free tier documented publicly.
- Docs are French-language; the REST/MCP tool catalogue requires connection to enumerate.
- No public repo - hosted service with Smithery distribution.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Israel Business Intelligence MCP - Israeli Company Verification for Agents](/hermes/mcp/servers/external/israel-business-intelligence-mcp)
- [Korea Business Verify MCP - Live KYB Checks for Korean Companies](/hermes/mcp/servers/external/korea-business-verify)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
