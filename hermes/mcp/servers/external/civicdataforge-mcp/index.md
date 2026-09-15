---
title: "CivicDataForge MCP - Government Records Evidence Platform"
description: "Hosted MCP relay for official US and Norway public records: STR permit registries, LEIE exclusion screening, property violations, restaurant inspections, childcare licensing, EPA ECHO compliance, and Norwegian company evidence. 14 tools live-probed, Apify-token auth."
category: Compliance
stars: 0
added: 2026-08-25
source: mcpservers.org /all listing
relevance: ★★★
tags: [mcp-server, public-records, str-permits, leie, property, compliance, government-data]
---

# CivicDataForge MCP

**Official public records, one agent-native relay.** CivicDataForge gives MCP-compatible agents structured access to official government records through a credential-safe relay backed by Apify. The official bundle exposes ten evidence tools across property compliance, healthcare integrity, regulated-facility safety, and Norwegian company evidence, plus four Apify plumbing tools. Public tool discovery works without credentials; calls use your own Apify token.

```
Server type: Remote Streamable HTTP (hosted relay) or local stdio gateway
Endpoint: https://civicdataforge.pages.dev/mcp
Auth: None for initialize/tools/list; X-Apify-Token header for tool calls
Tools: 14 verified by live probe (server v1.4.0)
Repo: github.com/equinoxaifinance-rgb/civicdataforge-mcp (MIT, actively maintained)
```

## Why This Matters for Operators

Compliance screening and due diligence mean pulling evidence from government sources that each have their own query language. CivicDataForge normalizes the hard ones into single tools: LEIE screening for healthcare hiring (HHS-OIG exclusions by name, NPI, state, or specialty), STR permit lookup across 31 US short-term-rental sources, property violations for real estate due diligence, and EPA ECHO compliance history for facility and counterparty checks. Every result is source-bound government-record evidence, which is exactly what audits and investor diligence want.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `civicdataforge--civicdataforge-evidence-gateway` | Routes a supported property, company, restricted-party, EPA facility, or right-to-know question to the correct evidence source |
| `civicdataforge--str-permit-registry` | STR permit research across 31 supported US short-term-rental permit sources |
| `civicdataforge--fl-dbpr-vacation-rentals` | Florida statewide DBPR vacation-rental and lodging-license evidence |
| `civicdataforge--property-violations` | Municipal building, property, and code-violation research |
| `civicdataforge--leie-exclusion-screening` | HHS-OIG LEIE screening by name, valid NPI, state, specialty, or exclusion type |
| `civicdataforge--restaurant-inspection-scores` | Official restaurant inspection scores, violations, and facility history |
| `civicdataforge--multistate-childcare-licensing` | Cross-state childcare licensing, inspection, and deficiency research |
| `civicdataforge--texas-childcare-licensing` | Texas-only childcare operation, inspection, and deficiency evidence |
| `civicdataforge--epa-echo-facility-compliance` | Bounded EPA ECHO facility query with published compliance and enforcement identity |
| `civicdataforge--norway-company-evidence` | Exact nine-digit Norwegian organisation-number evidence or bounded name research |
| `get-actor-run`, `get-dataset-items`, `get-key-value-store-record`, `abort-actor-run` | Apify plumbing: run status, dataset rows, key-value records, abort |

## Installation

Connect directly; discovery is public and calls spend your Apify token:

```json
{
  "mcpServers": {
    "civicdataforge": { "type": "http", "url": "https://civicdataforge.pages.dev/mcp" }
  }
}
```

The repo also ships a stdio gateway (`npm ci && APIFY_TOKEN=... npm start`) for Glama-style deployments; calls require the installing user's own Apify token.

## Configuration

Add an `X-Apify-Token` header with your Apify API token. Each underlying Actor has its own pricing, input schema, and limits on its Apify Store page. Successful calls return the Apify run ID, dataset ID, status, and up to 1,000 rows; larger outputs stay in your Apify dataset.

## Business Relevance

- **Healthcare hiring compliance:** LEIE exclusion screening before onboarding or contracting.
- **Real estate diligence:** STR permits and property violations in one query.
- **Facility due diligence:** EPA ECHO compliance history for counterparties.
- **Nordic operations:** Norwegian company evidence from Brønnøysund registers.

## Integration with CorpusIQ

CivicDataForge's structured evidence output pairs with CorpusIQ connectors for workflow automation: log LEIE screening results in your HR or compliance tracker, attach property evidence to CRM deal records, and trigger dashboards from the returned dataset IDs.

## Limitations

- Requires an Apify account and API token; per-Actor pricing applies.
- Tool calls are evidence lookups, not legal or compliance certifications.
- Coverage is jurisdiction-bounded; check the vendor's proof page for supported sources.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [GovGazette MCP - Federal Contract and Award Intelligence](/docs/hermes/mcp/servers/external/govgazette-mcp)
- [SAM.gov MCP - Federal Procurement Data](/docs/hermes/mcp/servers/external/sam-gov-mcp)
- [Acquisition.gov MCP - FAR Overhaul and Agency Deviations](/docs/hermes/mcp/servers/external/acquisition-gov-mcp)
