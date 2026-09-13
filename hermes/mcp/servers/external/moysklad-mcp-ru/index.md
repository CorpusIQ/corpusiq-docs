---
title: "moysklad-mcp-ru - MoySklad ERP Access for AI Agents"
description: "moysklad-mcp-ru gives Claude Code, Cursor, Codex and Cowork direct access to a MoySklad account over the JSON API 1.2: 32 tools cover stock, products, orders, counterparties, profit, turnover and money reports plus document creation behind a two-gate write model. Eight generic meta-tools reach the full 892-method catalogue. Installed via uvx, MIT licensed, Russian-language ERP."
category: ERP
stars: 2 (GitHub)
added: 2026-09-12
source: "mcpservers.org /all page 1 (night crawl) + GitHub repo ilyautov/moysklad-mcp-ru (MIT, pushed 2026-09-12)"
relevance: ★★★
tags: [erp, moysklad, inventory, accounting, russia, stdio, uvx, write-gates]
---

# moysklad-mcp-ru MCP

**Local MCP server (stdio via uvx, API token)** - an AI bridge to MoySklad (МойСклад), the Russian inventory and accounting ERP. Instead of walking the web portal, the agent calls the JSON API 1.2 directly: real stock levels, orders, counterparties and money reports with source fields, plus document creation behind two write gates. 32 tools, with 8 generic meta-tools reaching the full 892-method catalogue.

```
Server type: Local (stdio)
Auth: MoySklad API token (per-account)
Install: uvx moysklad-mcp-ru
Tools: 32 (8 meta-tools over a 892-method catalogue + typed reads + gated writes)
Write model: Two gates - documents are created as DRAFTS, conducting is a separate destructive step with confirmation
License: MIT (repo ilyautov/moysklad-mcp-ru, pushed 2026-09-12)
Category: ERP
Built by: Ilya Utov, AI Frontier lab (aifrontier.tech)
```

## Why This Matters for Operators

The standard failure mode of ERP-plus-AI is an assistant that either walks the browser and stumbles or invents numbers that sound confident. moysklad-mcp-ru removes both: numbers come from the real API with source and fields, and writes are physically blocked until the operator enables them and points them at a test account first. The two-gate write model - a document is created as a draft, and conducting it (which moves the accounting) is a separate destructive step with confirmation - is the discipline every ERP integration should have shipped with.

## Tools & Capabilities

| Type | Tools |
|---|---|
| Meta-tools | `ms_call_method`, `ms_call_raw`, `ms_fetch_all`, `ms_map` (covers the full 892-method catalogue with access classes) |
| Typed reads | `ms_get_stock`, `ms_get_products`, `ms_get_orders`, `ms_get_profit`, `ms_get_money`, `ms_get_turnover`, plus counterparties and reports |
| Gated writes | `ms_build_document` (draft preview, no write) and document tools with 7 role types: purchaseorder, supply, demand, invoicein, invoiceout and more |
| Utilities | `convert_money_to_kopecks` (API amounts are kopecks; reads return rubles) |
| Cabinet tools | Multi-account (multicabinet) switching and self-check (`doctor` command) |

Access classes per catalogue method: reads execute immediately, creates require confirmation, conducting and deletion require a second flag. 0 mutations are marked as read - enforced by a test suite (104 tests, CI on GitHub Actions).

## Installation

```bash
uvx moysklad-mcp-ru
```

Add it to Claude Code, Cursor, Codex or Cowork as a stdio MCP server, then configure the account token. Verify the install with `moysklad-mcp-ru doctor` - it prints the version, tool count, catalogue size and write-gate state without network calls. The write gate is OFF by default and should be pointed at a test cabinet before anything else.

## Configuration

```json
{
  "mcpServers": {
    "moysklad": {
      "command": "uvx",
      "args": ["moysklad-mcp-ru"]
    }
  }
}
```

The account token goes in the environment the server reads at startup; the README's install section walks through each client.

## Business Relevance

- **Russian-market retailers and wholesalers** get agent access to stock, orders and counterparties in their own ERP.
- **Finance operators** pull profit, turnover and money reports with real API numbers instead of model guesses.
- **Warehouse teams** draft receivings and shipments with the safety of the two-gate write model.
- **Multi-entity groups** switch cabinets from one server (multicabinet support).

## Integration with CorpusIQ

moysklad-mcp-ru shows the ERP-connector pattern at the safety standard CorpusIQ aims for: read defaults, explicit gates on writes, source fields on every number. For operators in the Russian market, a CorpusIQ agent could pair this with the existing marketplace family guides (Ozon, Wildberries) to cover warehouse ERP plus marketplace channels in one reporting stack. The alpha status means it belongs in evaluation, not production books, yet.

## Limitations

- Alpha software: the curated core is battle-tested on a test cabinet, but imported methods are exploration-grade.
- Russian-language ERP and docs; English README exists but the vendor ecosystem is Russian-market.
- stdio only - no hosted remote endpoint.
- A tool, not an accountant: operator review still required for conducted documents.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [marketplaces-mcp-ru - Russian Marketplace Seller Operations for Agents](/hermes/mcp/servers/external/marketplaces-mcp-ru/)
- [Ozon MCP Server - Marketplace Seller Operations for Agents](/hermes/mcp/servers/external/ozon-mcp-server/)
