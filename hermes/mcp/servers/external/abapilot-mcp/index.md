---
title: abapilot — SAP ECC / S4HANA MCP Server
subtitle: In-system ABAP for SAP ECC and on-premise S/4HANA
source: abapilot-mcp
github: https://github.com/NicoHern/abapilot-mcp
created: 2026-07-22
category: Enterprise / SAP
stars: 0
tags: [sap, abap, ecc, s4hana, enterprise, erp]
---

# abapilot — SAP ECC / S4HANA MCP Server

**In-system ABAP** MCP server for SAP ECC and on-premise S/4HANA. No BTP, no ADT, no RISE required. Runs directly inside the SAP system, giving AI agents native ABAP access to the world's most widely deployed ERP.

## What It Does

SAP ECC runs 70%+ of global enterprise transactions. abapilot puts MCP directly inside SAP:

- **In-system execution** — Runs as ABAP code inside SAP, not an external wrapper
- **No middleware** — No BTP, no SAP Cloud Connector, no ADT (ABAP Development Tools)
- **ECC + S/4HANA** — Works on both legacy ECC and modern S/4HANA
- **Native ABAP access** — Full access to SAP function modules, BAPIs, tables

## Business Operator Use Cases

| Use Case | Value |
|----------|-------|
| **SAP Query Agent** | "Show me all open purchase orders for vendor 10042" — direct table query |
| **Master Data Management** | "Update material master descriptions for these 50 SKUs" |
| **Financial Close** | "Run FBL3N for GL account 400000, export to CSV" |
| **SAP Monitoring** | "Check SM37 for any failed batch jobs this morning" |

## Installation

Deployed inside SAP as ABAP code:

1. Import the ABAP source into your SAP system (transaction SE38/SE80)
2. Activate the ABAP objects
3. Configure ICF node for HTTP access
4. Point your MCP client at the SAP HTTP endpoint

```json
{
  "mcpServers": {
    "abapilot": {
      "type": "url",
      "url": "https://sap-your-system:44300/abapilot/mcp"
    }
  }
}
```

## Tools Provided

- `abap_query` — Execute ABAP SQL queries with result streaming
- `call_function` — Call any SAP function module (BAPI/RFC)
- `read_table` — Read SAP table contents with filters
- `execute_report` — Run SAP reports (transactions)
- `get_system_info` — SAP system version, patch level, database

## Limitations

- **0 stars, brand new** — Created July 22, 2026.
- **SAP Basis transport required** — Installing ABAP code in SAP requires Basis team coordination. Not self-service.
- **Security risk** — MCP agent with ABAP access is a powerful attack surface. Restrict to read-only unless absolutely necessary.
- **SAP license implications** — Indirect access licensing may apply. Verify with your SAP account team.

## Operator Verdict

★★★ **Game-changing if it works.** Most SAP integration requires expensive middleware (SAP PI/PO, BTP). In-system MCP bypasses all of that. The security and licensing concerns are real — treat this as experimental and restrict to dev/QA systems until proven. For SAP operators managing large ECC landscapes, this could eliminate months of integration work.
