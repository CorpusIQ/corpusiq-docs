---
title: DeepLedger MCP - QuickBooks Online for AI Agents
description: "DeepLedger connects QuickBooks Online to AI agents with 24 tools for entries, reports and month-end close, review tasks instead of guesses."
category: Finance
stars: n/a (new listing)
added: 2026-09-27
source: "mcp.so server page (mcp.deepledger.ai)"
relevance: ★★★
tags: [quickbooks, accounting, bookkeeping, month-end-close, journal-entries, bank-feed, reports, remote-mcp]
---

# DeepLedger MCP

**An agent that does real bookkeeping in a live QuickBooks Online company, and asks instead of guessing.** DeepLedger connects QuickBooks Online to Claude, ChatGPT, Grok, Copilot, Gemini, Cursor and other agents through one endpoint at `https://mcp.deepledger.ai/mcp`. The agent categorizes bank-feed transactions, records bills, invoices, payments, deposits and journal entries, generates reports from natural-language prompts and helps complete the month-end close. When it is uncertain, it creates a review task instead of recording, and approved decisions become memory the agent reuses.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (sign in to DeepLedger, authorize QuickBooks)
Endpoint: https://mcp.deepledger.ai/mcp
Tools: 24 (transactions, lookups, reports, workflow)
Pricing: vendor pricing (deepledger.ai)
Category: Finance / Accounting
Built by: DeepLedger (deepledger.ai)
```

## Why This Matters for Operators

Bookkeeping backlogs are rarely a knowledge problem; they are a volume and discipline problem. DeepLedger's design is built around the real failure mode of AI accounting, which is confident wrong entries. Before recording anything, the agent checks the vendor or customer's history, open bills and invoices, and possible duplicates. When it cannot be sure how to categorize a transaction, it creates a review task instead of guessing, and the operator's approvals become rules the agent follows next time.

The multi-company support matters too: operators with several QuickBooks companies can connect them, switch by asking, and simplify intercompany transactions.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Transactions | qbBill, qbBillPayment, qbExpense, qbInvoice, qbReceivePayment, qbDeposit, qbTransfer, qbJournalEntry, qbSalesReceipt, qbRefundReceipt, qbEstimate, qbCredit, qbRecurringTransaction, qbVoidTransaction |
| Lookups | qbMasterData, qbFetchTransactions, qbCompanyProfile (list and switch companies) |
| Reports | qbReports, customReports |
| Workflow | bankFeed, tasks, closeRun, agentMemory, documents, qbAttachFile, qbSendEmail, getGuide |

## Installation

```bash
claude mcp add deepledger --transport http https://mcp.deepledger.ai/mcp
```

The first connection opens a browser window to sign in to DeepLedger and authorize the QuickBooks company. No API key is needed.

## Configuration

```json
{
  "mcpServers": {
    "deepledger": {
      "type": "http",
      "url": "https://mcp.deepledger.ai/mcp"
    }
  }
}
```

Optional Gmail, Outlook, Google Drive or shared-drive connectors can be added to the agent so it can use those sources while DeepLedger handles the accounting actions in QuickBooks.

## Business Relevance

- **Founders** clear bookkeeping backlogs with review tasks instead of surprises
- **Bookkeepers** handle more companies through one conversation surface
- **Finance teams** run month-end close as a tracked, agent-driven process
- **Multi-entity operators** switch companies by asking and simplify intercompany entries

## Integration with CorpusIQ

DeepLedger complements the CorpusIQ QuickBooks connector: CorpusIQ reads profit and loss, invoices and AR aging for business recaps, while DeepLedger performs the write-side actions like categorizing transactions and recording bills inside QuickBooks. CorpusIQ's executive financial workflows can consume the books DeepLedger maintains, keeping reporting and bookkeeping in a clean division.

## Limitations

- Write-side accounting needs operator trust in review tasks at first
- Live company writes mean mistakes carry real bookkeeping consequences
- OAuth flow requires both DeepLedger and QuickBooks sign-ins
- New listing; the live tool list is served from the endpoint

## FAQ

### Does the agent ever guess an entry?

No. When unsure how to categorize a transaction it creates a review task, and approvals become rules it follows next time.

### Can it handle multiple QuickBooks companies?

Yes. Connect several companies, switch by asking, and simplify intercompany transactions.

### What sign-in is required?

OAuth to DeepLedger and QuickBooks on first connect; no API key.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
