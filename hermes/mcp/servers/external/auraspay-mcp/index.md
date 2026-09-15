---
title: AurasPay Merchant MCP - Payment Review and Links
description: "AurasPay connects merchant accounts to AI assistants over remote MCP: read payment requests, account and support data, and prepare shareable payment links where every creation opens a separate review on AurasPay first. OAuth 2.0 with PKCE and scoped read and write permissions."
category: Finance
stars: n/a (new listing)
added: 2026-09-15
source: "chatmcp/mcpso issue #4150 + vendor docs at mcp.auraspay.com"
relevance: ★★★
tags: [payments, payment-links, merchant, fintech, oauth, scoped-permissions, review-gated, remote-mcp]
---

# AurasPay Merchant MCP

**Payment activity and payment-link prep with a human gate on every write.** AurasPay exposes a merchant account to MCP clients over Streamable HTTP with OAuth 2.0 and PKCE: assistants read payment requests, reports and account data, prepare payment links, and every creation opens a separate review on AurasPay before it runs. Scopes decide what the assistant may see or do, and disconnecting revokes future access.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.0 with PKCE (scoped; separate opt-in permissions for writes)
Endpoint: https://mcp.auraspay.com/api/mcp
Tools: Scoped tool set across account, payments, support, wallets, preferences and integrations
Pricing: AurasPay merchant account required (merchant developer preview)
Category: Finance / Payments
Built by: AurasPay (auraspay.com)
```

## Why This Matters for Operators

Payments is the domain where letting an agent act unreviewed is normally unacceptable. AurasPay's design puts the review step where the risk is: reads are scoped by approved permissions, and writes such as creating a payment link or verifying a payment require human approval in AurasPay itself. The assistant prepares; the operator reviews; nothing silently moves.

## Tools & Capabilities

Scoped groups from the published tool catalog (permissions are opt-in per scope):

| Tool | Purpose |
|---|---|
| `auraspay_account_get` | Merchant profile |
| `auraspay_account_balance` | Legacy dashboard counters (not a wallet balance) |
| `auraspay_payments_list` | Paginated payment requests |
| `auraspay_payment_get` | One owned payment request |
| `auraspay_payment_qr` | The original stored QR image, not regenerated |
| `auraspay_payment_invoice` | Completed-payment receipt or platform fee PDF |
| `auraspay_payments_export_csv` | Spreadsheet-safe CSV of a selected page |
| `auraspay_payments_analyze` | Analysis of a selected page |
| `auraspay_dashboard_stats` | Owned payment counts and completed totals |
| `auraspay_supported_tokens` | Current assets and networks allowed for the account |
| `auraspay_payment_create` | Request a payment link; opens a separate review on AurasPay |
| `auraspay_payment_verify` | Verify one owned pending payment after reviewing its transaction signature |

Additional scoped groups cover support tickets, wallet ownership challenges, notification preferences, plugin and webhook metadata, and API key metadata (masked, never full keys).

## Installation

The documented flow is to add the remote server URL in an AI application that supports remote MCP and OAuth:

```
https://mcp.auraspay.com/api/mcp
```

Then sign in on auraspay.com, review the requesting app name and permissions, and approve only a client you trust. Direct setup is published for several clients; the vendor does not claim named-client certification or marketplace approval.

## Configuration

```json
{
  "mcpServers": {
    "auraspay": {
      "type": "http",
      "url": "https://mcp.auraspay.com/api/mcp"
    }
  }
}
```

## Business Relevance

- **Merchants** check payment activity and pull receipts or CSV exports from the assistant instead of the dashboard.
- **Support teams** read tickets and assistant conversations, and can route replies through review-gated sends.
- **Finance ops** get payment-link prep with an approval step, so links are reviewed before they exist.
- **Developers** get a documented OAuth 2.0 + PKCE flow and a scoped tool surface for building merchant integrations.

## Integration with CorpusIQ

CorpusIQ's connectors cover processor and accounting records (Stripe, QuickBooks and more); AurasPay covers merchant-side payment requests and links. A composed workflow: reconcile processor volume via CorpusIQ against payment requests via AurasPay, and have the assistant prepare a payment link for a customer while the operator approves it on AurasPay. Both surfaces are read-first, with writes behind explicit human review.

## Limitations

- Merchant developer preview: this is a supported subset, not the entire dashboard. Available tools depend on enabled features and approved permissions.
- A payment link is a payment request, not proof of payment or a transfer of funds.
- Writes require a separate authenticated review on AurasPay; some scopes are opt-in.
- Never share wallet seed phrases, private keys or passwords in an AI conversation (vendor guidance, and good practice regardless).
- Brand new to this catalog.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
