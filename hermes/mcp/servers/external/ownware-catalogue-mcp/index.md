---
title: "Ownware Catalogue MCP - Self-Hosted Business Apps"
description: "Forty-eight self-hosted business apps with 274 MCP tools: purchase approvals, fixed assets, PO matching, petty cash, timesheets and more."
category: ERP
stars: n/a (no public repo)
added: 2026-09-30
source: "mcpservers.org server page (ownware.io)"
relevance: ★★
tags: [erp, self-hosted, procurement, accounting, operations, approval-gated, audit-log, remote-mcp]
---

# Ownware Catalogue MCP

**Self-hosted business apps your agent can operate over MCP.** Ownware is a catalogue of 48 self-hosted applications, each exposing its own MCP endpoint with the same three-fact handshake: address, key and streamable HTTP. Together they declare 274 tools across purchase approvals, fixed-asset registers, PO and packing-slip extraction, petty cash, certificates, timesheets and more. Keys can be minted read-only, in which case the write tools are not even advertised to the assistant.

```
Server type: Remote (Streamable HTTP), self-hosted per install
Auth: Bearer API key with read-only or read-write scope
Endpoint: https://your-install/mcp
Tools: 274 across 48 products
Pricing: per-product licensing from ownware.io
Category: ERP
Built by: ownware.io
```

## Why This Matters for Operators

Giving an AI write access to business records is the scary part of agentic ops. Ownware's answer is structural: read-only keys that hide the write tools entirely, an audit log that records every action beside the key's user, no delete tools anywhere in the catalogue, and no outbound customer email from any tool. Destruction and outbound mail stay human clicks by design.

The read-only mode is what makes the catalogue approachable: an assistant can answer questions from your invoicing, rota or fixed-asset register while being refused, by name, if it tries to write. Then read-write keys unlock drafting, with everything landing in the audit log.

## Tools & Capabilities

| Product | Purpose | Tools |
|---|---|---|
| Approva | Purchase approvals with sign-off by amount | 9 (list_requests, create_request, approve_request, reject_request, pending_report, list_vendors, list_cost_centers) |
| Assetora | Fixed-asset register, depreciation to the cent | 5 (list_assets, asset_detail, create_asset, dispose_asset, depreciation_report) |
| Cargora | PO and packing-slip extraction, short-shipment and price-gap catching | 6 (list_documents, line_item_update, match_status, discrepancies, export_rows) |
| Cashora | Petty cash ledger that proves out at month-end | 4 (list_boxes, box_detail, record_entry, month_report) |
| Certora | Certificate verification with a self-hosted verify page | 6 (list_templates, issue_certificates, verify_certificate, expiring_report) |
| Clockora | Staff timesheets by project with approvals | 4 (hours by project, totals, approvals, no invoicing) |

The full 48-product tool list is published per product, exactly as each declares them to tools/list; a ✎ marks the tools that can change something. Each product ships an API.md with its exact tool list.

## Installation

```bash
claude mcp add --transport http invora https://your-install/mcp
```

Install the apps from ownware.io, mint a key in Settings, then point any MCP client at your install's /mcp path with the key in the Authorization header. n8n's MCP Client node and any local model reach the same endpoint over plain JSON-RPC 2.0.

## Configuration

```json
{
  "mcpServers": {
    "invora": {
      "type": "http",
      "url": "https://your-install/mcp"
    }
  }
}
```

The key acts as one user and inherits that user's role. Pick read-only and the endpoint stops advertising write tools; pick read-write and every change lands in the audit log. Keys are revocable from the same page.

## Business Relevance

- **Operators who self-host** get ERP-grade MCP access without sending business data to a hosted model
- **Finance teams** run purchase approvals and fixed-asset registers with sign-off rules frozen on each record
- **Warehouse and supply teams** match POs against packing slips with discrepancy reports
- **Compliance-minded operators** get a no-delete, no-outbound-mail tool surface by design

## Integration with CorpusIQ

Ownware covers the self-hosted operational records; CorpusIQ covers the cloud financial and marketing picture. A composed workflow: an Ownware read-only key answers the purchase-approval and fixed-asset questions from the self-hosted install, while CorpusIQ answers revenue, spend and traffic questions from Stripe, QuickBooks, Google Ads and GA4 connectors. Operators who run their own stack keep write access local and analytics in one agent session.

## Limitations

- Self-hosted products: you run and maintain each install
- 48-product catalogue with per-product licensing, not one subscription
- No delete tools and no outbound email tools, which is deliberate but may not fit every workflow
- Each product's MCP surface is scoped to its own domain, so cross-app queries need multiple connections

## FAQ

### Can the assistant delete records?

No. No tool in the catalogue deletes records, and none emails customers. Destruction and outbound mail stay human clicks.

### What does a read-only key change?

The write tools are not advertised to the assistant at all, and write attempts are refused by name. The audit log records every read-write action with the key's user beside it.

### Is the endpoint vendor-specific?

No. It is MCP over streamable HTTP with one request per response; any client that speaks the transport works, including ones that do not exist yet.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [DeepLedger MCP - QuickBooks Online for AI Agents](/hermes/mcp/servers/external/deepledger-mcp/)
- [Handl MCP - Billing Operations for Small Agencies](/hermes/mcp/servers/external/handl-mcp/)
- [systemHUB MCP - SOP Management for Business Agents](/hermes/mcp/servers/external/systemhub-mcp/)
