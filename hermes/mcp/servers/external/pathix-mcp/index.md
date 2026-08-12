---
title: Pathix MCP — Microsoft Dynamics 365 Forensics
description: "Setup and usage guide for Pathix MCP — Microsoft Dynamics 365 Forensics. Part of the Hermes resource directory."
last_updated: 2026-08-12
---

# Pathix MCP — Microsoft Dynamics 365 Forensics

**Priority:** MEDIUM | **Category:** Enterprise / ERP / Compliance  
**Transport:** Remote Streamable HTTP | **Auth:** OAuth via Microsoft Entra  
**Website:** https://pathix.app  
**Discovered:** July 27, 2026 (chatmcp/mcpso #3317)

## What It Does for Operators

Pathix is a forensics platform for Microsoft Dynamics 365 and the Dataverse. It scans an environment and parses compiled plugin IL, classic workflow XAML, Power Automate flow definition JSON, form scripts, canvas app Power Fx, dataflows, and the security model. The resulting dependency graph is exposed as read-only MCP tools.

**For operators in Microsoft-ecosystem enterprises:** Pathix answers the questions the native Dataverse MCP cannot: what writes a given column, what reads it, what breaks if you change a table, who can actually reach it, and which recent deployment explains a field behaving differently.

## Installation

```bash
# Self-hosted, commercial — runs in customer's Azure subscription
# No public endpoint or standalone install
# Deployment via Azure Marketplace: https://pathix.app
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "pathix": {
      "url": "https://YOUR-PATHIX-DEPLOYMENT.azurewebsites.net/mcp",
      "transport": "streamable-http",
      "auth": "oauth"
    }
  }
}
```

## Tools (21, all read-only)

Key capabilities:
- Cross-component dependency tracing (what writes/reads each column)
- Impact analysis (what breaks if this table changes)
- Security model reachability (who can access what, and through which path)
- Deployment forensics (which recent change explains this behavior)
- Plugin IL decompilation analysis
- Power Automate flow dependency mapping

Every dependency edge carries resolution confidence (declared / parsed / AI-derived / unresolved).

## Operator Use Cases

1. **Change impact analysis:** Before modifying a Dynamics 365 table, ask Pathix "what reads this column?" — instantly see all plugins, flows, scripts, and reports that would break
2. **Security audit:** Map the actual reachability of sensitive fields — does that intern's security role accidentally grant access to financial data through a chain of inherited permissions?
3. **M&A system integration:** When merging two companies, scan both Dynamics environments to identify shared dependencies, conflicts, and integration points
4. **Deployment forensics:** "Sales pipeline conversion dropped 15% since Tuesday" → Pathix shows which deployment changed the opportunity close logic
5. **Compliance evidence:** Generate dependency maps for SOX/GDPR auditors showing exactly which systems touch regulated data

## CorpusIQ Angle

**Complementary — enterprise vertical.** CorpusIQ's data sources could be enriched with Pathix dependency data for enterprises on Dynamics 365. A combined view would let operators see: "This QuickBooks integration depends on these 3 plugins, this security role, and this Power Automate flow."

## Limitations

- **Commercial + self-hosted only** — no free tier, no public endpoint. Enterprise sales motion required
- Azure-only deployment (customer's Azure subscription)
- Microsoft Dynamics 365 / Dataverse only (not Salesforce, NetSuite, etc.)
- 21 read-only tools — no write capability for remediation
- OAuth via Microsoft Entra requires enterprise identity setup
