---
title: "LedgerCrossing MCP - QuickBooks Desktop for AI Agents"
description: "Reach QuickBooks Desktop (Pro, Premier and Enterprise) from any MCP client through all 240 qbXML operations, on the machine where the books live."
category: Finance
stars: n/a (new listing)
added: 2026-10-12
source: "mcpservers.org /all (Oct 12, 2026 evening sweep)"
relevance: ★★
tags: [quickbooks, accounting, bookkeeping, desktop, qbxml, erp, finance-ops, local-mcp]
last_updated: "2026-10-19"
---

# LedgerCrossing MCP

**Local MCP server (Windows, runs beside QuickBooks Desktop)** - connect any MCP client to QuickBooks Desktop (Pro, Premier and Enterprise) on the machine where the company file lives. The agent browses all 240 qbXML operations, validates what it wrote before executing, then runs it: queries, invoices, payments, edits, exactly the capability the vendor's REST API has.

```
Server type: Local (Windows app next to QuickBooks Desktop; REST API + MCP server on the machine or office network)
Auth: API key on every path (Bearer or X-Api-Key); the app refuses remote exposure without a key
Endpoint: local / office-network endpoint from the app; setup guide at ledgercrossing.com/docs/mcp
Tools: 6 (list_operations, get_operation, validate_qbxml, run_qbxml, explain_error, get_status)
Pricing: included in the $299 one-time product
Category: Finance / Accounting
Built by: LedgerCrossing (ledgercrossing.com)
Website: ledgercrossing.com
Listing: mcpservers.org /all (Oct 12, 2026 evening sweep)
```

## Why This Matters for Operators

QuickBooks Desktop has no cloud API. It talks through a local COM interface on the machine where it runs, which is why every other QuickBooks MCP server on the market addresses QuickBooks Online and cannot touch it. That leaves a real gap: businesses that keep years of books in Desktop cannot give an AI assistant access to their actual ledger.

LedgerCrossing closes it from the inside. The bridge runs next to QuickBooks, compiles the agent's request against Intuit's own qbXML specification, and executes it with the same authority as the vendor's API. The agent discovers capability on demand instead of memorizing it: list the operations, read the field rules for one, validate the request locally (no QuickBooks round trip), and only then run it. Errors come back explained, and runaway unbounded queries are rejected by default unless the operator opts out.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| list_operations | All 240 qbXML operations with category and minimum QuickBooks version |
| get_operation | The full field reference for one operation: element order, required flags, enums, version gates |
| validate_qbxml | Check a request locally against the catalog before it runs |
| run_qbxml | Execute against QuickBooks Desktop and return the response: reads and writes |
| explain_error | Turn a QuickBooks status code into what went wrong and what to change |
| get_status | Is QuickBooks up, which company file is open, is the bridge connected |

## Installation

Set up per the vendor guide at ledgercrossing.com/docs/mcp: install the Windows app on the QuickBooks machine, set an API key, and point the MCP client at the local endpoint. The app can also expose the endpoint to the office network with one setting.

## Configuration

Because MCP and the REST API share the endpoint, the client setup is the same as the vendor's API configuration: the base URL of the bridge on your machine, with the API key as a Bearer or X-Api-Key header. The exact block is generated in the app; the canonical steps are at ledgercrossing.com/docs/mcp.

## Business Relevance

- **SMB finance teams on QuickBooks Desktop** can ask the actual ledger for the answers instead of exporting reports: open invoices, aging, payment status, customer detail.
- **Operators who run month-end** get an agent that can pull the exact lists and totals, with validation catching malformed requests before they touch the books.
- **Multi-entity and franchise setups** that stayed on Desktop for compliance or habit now have an automation path that does not require migrating to QuickBooks Online.
- **Bookkeepers and fractional CFOs** serving Desktop clients can automate routine queries across client files, scoped per machine.

## Integration with CorpusIQ

CorpusIQ answers across the business's systems; LedgerCrossing reaches the one system that had no cloud door. Where the catalog's other QuickBooks entries (the hosted QuickBooks Online server and Deepledger) cover Online companies, LedgerCrossing covers Desktop: pair a CorpusIQ Stripe or Shopify source with the Desktop ledger and ask whether the payments in the sales system match the invoices and deposits in QuickBooks Desktop, with each side read from its own source of record.

## Limitations

- Windows and QuickBooks Desktop only (Pro, Premier, Enterprise); QuickBooks Online companies use the catalog's Online entries instead.
- MCP is not read-only: run_qbxml executes whatever qbXML the agent writes, including edits. Scope the API key and the machine, and use the built-in bounded-query guardrail.
- Commercial product ($299 one-time); hosted reachability options beyond the local and office network are priced separately. The setup places the bridge on the machine where the company file lives, so plan for that machine's security.

## FAQ

### Why is a local MCP server needed for QuickBooks Desktop?

QuickBooks Desktop exposes no cloud API; it is reachable only through the local COM interface on the machine where it runs. LedgerCrossing is a Windows bridge that sits next to it and speaks MCP, which is what makes Desktop reachable from a cloud AI client at all.

### Is this the same as the QuickBooks Online MCP servers?

No. The catalog's hosted QuickBooks Online server and Deepledger address Online companies. LedgerCrossing is the Desktop path, and the two do not overlap in coverage.

### Can the agent write to the books?

Yes, with the same capability as the REST API: queries, invoices, payments and edits. Validation, error explanation and a bounded-query default reduce the blast radius, and the operator controls the key and the network exposure.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
