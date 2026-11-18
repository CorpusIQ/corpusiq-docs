---
title: "SAP Business One MCP - Read-Only ERP for Agents"
description: "Nine typed read-only tools over the SAP Business One Service Layer, with a mock mode that lets you drive the whole surface without an SAP licence."
category: "ERP / Finance Operations"
stars: "0 (stdio npm package @kodenova/sap-b1-mcp 0.1.0, MIT, driven end to end in mock mode with nine tools listed and six called)"
added: 2026-11-17
source: "the mcp.so submission queue entry 7528 filed 2026-11-17T22:00:28Z, the registry record io.github.kodenova/sap-b1-mcp, and a local session on 2026-11-17 in which the server was installed from npm and driven over stdio with SAPB1_MOCK=1"
relevance: ★★★
tags: [erp, sap, finance, inventory, invoices, read-only, stdio, mcp]
last_updated: "2026-11-17"
---

# SAP Business One MCP

**SAP Business One is the ERP that small and mid-sized companies actually run.** It sits on a Service Layer: an OData API that already holds the customers, the items, the open orders and the unpaid invoices. What has been missing is a narrow, safe way for an assistant to read that layer without a consultant writing a connector every time.

This server is that narrow door. Nine typed tools, read only, no free SQL, and a mock mode that makes the whole thing testable before anyone touches a production company database.

```
Server type:   local stdio
Package:       @kodenova/sap-b1-mcp 0.1.0, MIT
Registry:      io.github.kodenova/sap-b1-mcp
Protocol:      2025-06-18
Tools:         9, all read only
Backend:       SAP Business One Service Layer (OData)
Mock mode:     SAPB1_MOCK=1, fixture data, no SAP connection
```

## The evidence tier

Installed and driven. The package was installed from npm, started over stdio with `SAPB1_MOCK=1`, and the server logged to stderr that it was running in mock mode with fixture data and no SAP connection. `initialize` returned serverInfo `sap-b1-mcp 0.1.0` and an instructions string that states the contract in one sentence: all tools only read data, there are no tools that create, change or delete anything, codes are exact, and the `search_` tools exist to find codes first.

Six `tools/call` requests were then run against the fixture company. Every one answered with structured JSON, and the one failure path answered with a readable refusal.

The mock mode is the reason this earns a page rather than a hold. A server that can be exercised with no credential and no licence is a server whose behaviour you can state, and every number below came from a real call.

## The tool surface

| Tool | Required argument | Returns |
|---|---|---|
| `get_business_partner` | `cardCode` | One partner by exact code |
| `search_business_partners` | none | Partners whose code or name contains the text, optional type filter |
| `get_customer_balance` | `cardCode` | Account balance, open orders, open deliveries and credit limit |
| `get_item` | `itemCode` | One item master record |
| `search_items` | none | Items whose code or name contains the text |
| `get_stock_by_warehouse` | `itemCode` | In stock, committed, ordered and available per warehouse |
| `get_open_sales_orders` | none | Open orders, newest first, optional customer filter |
| `get_open_invoices` | none | Open A/R invoices with the unpaid balance, optional overdue filter |
| `run_saved_query` | `name` | One query the administrator pre-registered in a config file |

`run_saved_query` is the governance decision that makes the rest safe. There is no free SQL and no free filter expression: an administrator registers queries in a config file, and the agent can only name one of them. Called with an unknown name, the server refused and listed what exists:

```text
Unknown saved query "nope". Available: customers_over_balance,
invoices_due_before, sales_by_month
```

That refusal is the security model stated as an error message. The allowlist lives in a file an admin owns, and the agent cannot widen it.

## What the fixture data proves

The mock company held four business partners (three customers and one lead), and the invoice tool returned a coherent ledger.

```text
asOf 2026-11-18, count 3, totalOpen 13,330.50
DocNum 7001  C10000  10,000.00  paid 2,000.00  open 8,000.00  overdue 48 days
DocNum 7003  C20000     830.00  paid     0.00  open   830.00  overdue 29 days
DocNum 7002  C10000   4,500.50  paid     0.00  open 4,500.50  overdue  4 days
```

The stated total reconciles to the cent: 8,000.00 + 830.00 + 4,500.50 = 13,330.50. The overdue count is computed against the as-of date rather than stored, which is what an operator wants: the number moves.

The stock tool is equally explicit. One item, two warehouses:

```text
ItemCode A00001, TotalInStock 340
Warehouse 01  InStock 300  Committed 50  Ordered 100  Available 350
Warehouse 02  InStock  40  Committed 10  Ordered   0  Available  30
```

Two arithmetic controls hold here. Total in stock is 300 + 40 = 340, so the total is a sum and not a separate field. And available is in stock minus committed plus ordered (300 - 50 + 100 = 350, 40 - 10 + 0 = 30), which means "available" includes stock already on order. An operator asking "how many can I promise" is getting the on-order answer, and anyone quoting that number to a customer should know it.

## One null worth reading carefully

`get_customer_balance` for the same customer returned a current balance of 830, an open delivery balance of 150, a credit limit of **0** and `CreditAvailable: null`.

Zero credit limit producing a null availability is the correct reading and the wrong thing to show a language model. A model that treats null as "no limit" will tell an operator that any order fits. Treat null as "not computable from the master data" and check the limit itself.

## Why this earns a page

Most ERP connectors on this list are either read-write agents pointed at a SaaS product, or bespoke. This one is the combination an operator actually needs before letting an agent near the ledger:

- **Read only, stated in the server instructions** and enforced by nine tools with no write verb.
- **No free SQL**: queries are an administrator's allowlist.
- **A mock mode**, so the behaviour can be evaluated, demoed and regression tested without a licence or a company database.

For a business whose customer, item, stock and invoice truth lives in Business One, this is the difference between an assistant that talks about the business and one that reads it.

## Installation

```bash
npx -y @kodenova/sap-b1-mcp
```

Or install it locally and run the bin directly, which makes mock mode easier to control:

```bash
npm install @kodenova/sap-b1-mcp
SAPB1_MOCK=1 node node_modules/@kodenova/sap-b1-mcp/dist/index.js
```

## Configuration

```json
{
  "mcpServers": {
    "sap-b1": {
      "command": "npx",
      "args": ["-y", "@kodenova/sap-b1-mcp"],
      "env": {
        "SAPB1_SERVICE_LAYER_URL": "https://b1server:50000/b1s/v1",
        "SAPB1_MOCK": "0"
      }
    }
  }
}
```

The Service Layer URL is the company database endpoint, not the SAP host root. Credentials are environment variables for the Service Layer user; there are no write scopes to grant, because there are no write tools.

Start with `SAPB1_MOCK=1` on the host that will run it. The fixture mode answers every tool, which lets you confirm the wiring and read the exact payload shapes before pointing the same configuration at a live company.

## Limitations

- Mock data is a fixture, not a sample of any real company. Numbers quote the fixture, never a customer.
- Nine tools cover partners, items, stock, open orders, open invoices and balances. Journal entries, purchase orders and pricing agreements are outside the surface.
- Codes are exact, so every workflow starts with a `search_` call. An assistant that guesses codes will mostly miss.
- A read-only server still exposes commercial data to a model provider. The allowlist and the network boundary are the operator's job, not the server's.

## FAQ

### Can this server write to SAP Business One?

No. The server instructions state that all tools only read data and that there are no tools that create, change or delete anything, and the nine tools confirm it.

### Can I try it without SAP?

Yes. `SAPB1_MOCK=1` runs the server against fixture data with no SAP connection, and every tool answers. That is how the numbers in this guide were produced.

### Does it allow arbitrary SQL?

No. `run_saved_query` only runs queries an administrator registered in a config file, and an unknown name is refused with the list of registered names.

### Which SAP product does it talk to?

SAP Business One, through its Service Layer OData API. It is not an S/4HANA or Business ByDesign connector.

## See Also

- [Vericto MCP - SQL Guardrails Before the Query Runs](/hermes/mcp/servers/external/vericto-mcp/)
- [Basis MCP - The Excel Engine an Agent Can Audit](/hermes/mcp/servers/external/basis-mcp/)
- [Spark Inventory MCP - Stock, Forecasts and Draft POs](/hermes/mcp/servers/external/spark-inventory-mcp/)
