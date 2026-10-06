---
title: "Pocket Invoice MCP - Invoices and Estimates from Chat"
description: "Create invoices, estimates and PDFs, track unpaid balances and record payments from your AI assistant, with confirm-gated sends."
category: Finance / Accounting
stars: n/a (new listing)
added: 2026-10-06
source: "mcpservers.org /all"
relevance: ★★
tags: [invoicing, accounting, finance, invoices, smb, pdf, oauth, remote-mcp]
---

# Pocket Invoice MCP

**Remote MCP server (Streamable HTTP, OAuth)** - invoicing from the conversation. Pocket Invoice is the free invoice maker used on iOS, Android and the web; its MCP server lets an assistant draft invoices, estimates and purchase orders, generate branded PDFs, check unpaid balances and record received payments, all against the same account and company records as the apps.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth - sign in, choose one company, approve permissions
Endpoint: https://api.freedominvoice.com/mcp
Tools: documents (invoices, estimates, POs), PDFs, sends, customers and items, business figures, payments
Pricing: Free (unlimited invoices, no watermark)
Built by: Pocket Invoice (freedominvoice.com)
```

## Why This Matters for Operators

Invoicing is the chore at the end of every job: remember the line items, find the client details, pick the template, export the PDF, write the email. For owner-operators it happens at night or on the phone in a van. Pocket Invoice's server turns it into a sentence - "Invoice Acme $500 for website design, due in 14 days" - and the invoice, number and PDF come back into the same account the apps use.

**The permission model is the part worth reading.** Sending starts disabled and every send needs confirmation in the chat; the assistant can record a received payment but cannot take a card payment, transfer funds or issue a refund; the connection is scoped to one company with the operator's existing team permissions. That is the right shape for finance tools in an agent era: full drafting power, human confirmation before anything leaves the building.

The records stay together too. Documents share the same customers, products and stock as the mobile apps, so the books do not fork: what the agent creates is what the owner sees on their phone.

## Tools & Capabilities

| Area | What the agent can do |
|---|---|
| Documents | Draft invoices, estimates and purchase orders; edit, copy or convert an existing document |
| PDFs | Generate the branded PDF with your logo and company details; get a download link and web preview |
| Sends | Prepare the email, show the recipients, send after confirmation and check sending status |
| Customers and items | Find or update saved clients, products and stock |
| Business figures | Sales, outstanding balances and expenses over the dates you choose |
| Payments | Record a payment or deposit against an invoice and update its balance (no money movement) |

## Installation

Connect from the assistant: Codex via Settings, MCP servers, Add server; Claude via Customize, Connectors, Add custom connector; ChatGPT via developer mode and Plugins; Cursor and Windsurf via their MCP config files.

```bash
claude mcp add --transport http pocket-invoice https://api.freedominvoice.com/mcp
```

Tested with Codex; any client with remote MCP, Streamable HTTP and OAuth support works.

## Configuration

```json
{
  "mcpServers": {
    "pocket-invoice": {
      "url": "https://api.freedominvoice.com/mcp"
    }
  }
}
```

Sign in when prompted, choose one company and approve permissions. Revoke the connection any time under AI connections in Pocket Invoice.

## Business Relevance

- **Owner-operators** draft and send invoices without opening the app or remembering numbers.
- **Freelancers and contractors** turn a job description into a branded PDF in one sentence.
- **Small agencies** check "which invoices still have an unpaid balance" as a Monday-morning question.
- **Anyone on the free tier** gets unlimited invoices with no PDF watermark; the MCP uses the same account limits.

## Integration with CorpusIQ

Where CorpusIQ reads the accounting stack - QuickBooks, Stripe, Shopify - Pocket Invoice is the lightweight issuing surface for operators who are not on a full platform, or who want a fast second surface for field work. The composed pattern: create and send the invoice conversationally, record the payment when it lands, then let CorpusIQ's read-only connectors reconcile revenue and receivables against the books so nothing slips between the two.

## Limitations

- Sending starts disabled; every send requires confirmation in the chat.
- The assistant cannot charge cards, transfer funds or issue refunds; it records payments only.
- Account, storage and membership limits apply, same as the apps.
- OAuth connection is scoped to one company per connection.
- Brand new listing: no track record from this catalog yet.

## FAQ

### Is it really free?

Yes. Unlimited invoices and no PDF watermark. MCP access uses your existing account and its limits.

### Can the assistant email invoices on its own?

No. Sending is disabled until you enable it, and every send shows the document and recipients for confirmation first. Sending status is readable afterward.

### Can it move money?

No. It records received payments against invoices and reads balances; it cannot charge a card, transfer funds or refund.

### Which assistants work?

Codex is tested; Claude, ChatGPT, Cursor and Windsurf have published setup paths, and any client supporting remote MCP with OAuth works with the same URL.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [InvoiceParser Pro MCP - Invoice to Excel from Chat](/hermes/mcp/servers/external/invoice-parser-pro-mcp/)
- [Peil MCP - Freelance Time Tracking and Invoicing](/hermes/mcp/servers/external/peil-mcp/)
