---
title: "Booksmate MCP - Invoice Fetching and Spend Reports"
description: "Fetch invoices and receipts from your inbox and 500+ supplier portals, extract the data, and run spend reports from your agent."
category: Finance / Accounting
stars: n/a (new listing)
added: 2026-10-07
source: "mcpservers.org /all page 2 (Oct 7, 2026 evening sweep)"
relevance: ★★★
tags: [invoices, receipts, bookkeeping, spend-reports, accounting, document-extraction]
---

# Booksmate MCP

**Hosted MCP server that puts your invoices and receipts inside your agent** - Booksmate collects documents from your inbox and 500+ supplier portals, extracts the data, and syncs it to your accounting tools. The MCP endpoint lets ChatGPT, Claude, Codex and any other client search, summarise, upload and package those documents in plain language.

```
Server type: Remote (Streamable HTTP at https://mcp.booksmate.com)
Auth: OAuth 2.1 sign-in, no API key to paste
Setup line: "Set up Booksmate from booksmate.com/agents" (or add the endpoint yourself)
Docs: https://booksmate.com/docs/features/mcp-server/
Connects: Gmail and Microsoft inboxes for collection; Google Drive, Xero and QuickBooks for export
Pricing: 14-day trial for $0
Category: Finance / Accounting
Built by: Booksmate
```

## Why This Matters for Operators

Invoice admin is a scavenger hunt: the AWS invoice is in email, the courier receipt is in a supplier portal, the client dinner receipt is a photo, and the accountant wants all of it in one export by month end. Booksmate does the fetching and extraction; the MCP server makes the result queryable. "Show my 10 largest unexported invoices from last quarter" and "How much VAT did I pay last quarter?" become single prompts against the documents already in your account. The extraction stage is human-friendly too: you can ask which documents failed to scan and fix just those.

## Tools & Capabilities

| Capability | What the agent can do |
|---|---|
| Search documents | find invoices and receipts by vendor, date, amount, status, category or currency |
| Upload files | attach a PDF or image for extraction, then search the resulting data |
| Summarise spend | group spend by vendor, month, category, currency, document type or direction, including VAT |
| Scan email | trigger ingestion for connected Gmail or Microsoft inboxes and check job status |
| Find duplicates | catch double-paid invoices and month-over-month jumps on recurring bills |
| Package documents | create a ZIP of selected documents with a short-lived download link for handoff |

Your client fetches the live tool list at connect time; the capability areas above are from the vendor's MCP documentation.

## Installation

The one-line path: ask your agent to "Set up Booksmate from booksmate.com/agents", which walks the client through adding the server.

Manual setup: add `https://mcp.booksmate.com` as a remote Streamable HTTP server in your client. OAuth 2.1 sign-in happens in the browser; there is no API key to paste.

## Business Relevance

- **Founders and ops leads:** answer spend questions from chat - biggest unexported invoices, software spend by quarter, top suppliers by amount paid, duplicate detection.
- **Bookkeepers and accountants:** get a clean feed of extracted invoices and receipts into Xero, QuickBooks or a Drive folder instead of chasing PDFs.
- **Teams with messy inboxes:** connect the inbox, let collection run, and ask which documents failed extraction instead of auditing everything by hand.

## Integration with CorpusIQ

CorpusIQ reads your financial systems (Stripe, QuickBooks) and keeps the answers consistent across AI clients. Booksmate covers the paper trail behind those numbers: reconcile what CorpusIQ reports with the actual invoices and receipts, and hand your accountant a packaged ZIP at month end, all from the same assistant.

## Limitations

- Requires a Booksmate account and at least one connected inbox or upload source; the 14-day trial gives full evaluation time.
- Extraction is automated; ask which documents failed to scan before closing a period.
- Brand new listing - endpoint documented and live (probe: 401 OAuth sign-in) with no third-party track record yet.

## FAQ

### Do I need to give it access to my email?

Only the inboxes you connect, through the provider's standard OAuth flow. Documents land in your Booksmate account; the MCP server reads and writes within that account.

### Where do the documents go after extraction?

They feed the search and spend-report tools, and can be exported to Google Drive, Xero or QuickBooks, or packaged as a ZIP with a short-lived link.

### Can it catch double payments?

Yes - duplicate detection is one of the documented capabilities ("Did I pay this invoice twice?").

### Is there an API key?

No. The MCP server uses OAuth 2.1 browser sign-in; you approve the tool scopes once when connecting.

## See Also

- [Accountable MCP - AI Bookkeeping for Startups](/hermes/mcp/servers/external/accountable-mcp/)
- [SuperBooks MCP - Bookkeeping and Financial Reports for Agents](/hermes/mcp/servers/external/superbooks-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
