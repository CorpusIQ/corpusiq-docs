---
title: "QuickBooks - CorpusIQ Docs - CorpusIQ"
description: "Make your books answerable in plain English. Cash position, P&L, overdue invoices, AR aging, customer balances - without opening QuickBooks Online and."
---
# QuickBooks

## What the QuickBooks connector does

The QuickBooks connector makes your books answerable in plain English from any AI assistant. Connect once and ChatGPT, Claude, or Perplexity can query cash position, profit and loss, balance sheet, overdue invoices with days overdue, AR and AP aging, customer and vendor balances, and spend across any date range - without opening QuickBooks Online or rebuilding the same report you ran last month. The connection uses Intuit's own consent flow: sign in, choose the company file, approve. CorpusIQ never creates invoices, records payments, or changes anything in your books; it does not retain raw customer files or full connector response payloads, and operational query logs are bounded. QuickBooks Online is supported, Desktop is not. Setup takes about two minutes.

## What it unlocks

Make your books answerable in plain English. Cash position, P&L, overdue invoices, AR aging, customer balances - without opening QuickBooks Online and rebuilding the same report you ran last month.

## Before you connect
- A QuickBooks Online account (QBO). Desktop is not supported.
- Admin or Company Admin access - accountants connecting on behalf of a client need the right permission level.
- About 2 minutes.

## How to connect
1. Open your CorpusIQ dashboard and click Connections.
2. Find QuickBooks and click Connect.
<!-- screenshot: QuickBooks card on CorpusIQ connections page -->
3. Sign into Intuit if prompted.
4. Choose the QuickBooks company file you want to connect.
<!-- screenshot: Intuit "Choose a company" picker -->
5. Click Connect on the consent screen.

You'll see QuickBooks change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
- Profit and Loss report (any date range).
- Balance Sheet.
- Invoices, payments, bills.
- Overdue invoices with days overdue.
- AR and AP aging.
- Customers, vendors, products and services.
- Chart of accounts.
- Company profile.

Read-only. CorpusIQ never creates invoices, records payments, or changes anything in your books.

## Questions you can ask
- "What was our P&L last quarter?"
- "Show me overdue invoices over $5,000."
- "How much cash is on the balance sheet?"
- "Who owes us money - sorted by oldest invoice?"
- "What did we spend on contractors this year?"

## Troubleshooting
- "Could not connect to Intuit" - Intuit OAuth occasionally rate-limits. Wait 60 seconds and retry.
- Wrong company file connected - disconnect QuickBooks in your dashboard and reconnect, picking the correct company.
- Numbers don't match your accountant's report - make sure you specify accrual vs. cash basis in your question; CorpusIQ uses your QuickBooks default.

## Frequently Asked Questions

### How do I connect QuickBooks to ChatGPT?

Connect QuickBooks in the CorpusIQ dashboard, then ask your question in ChatGPT. CorpusIQ exposes the books through its MCP endpoint, so ChatGPT can query P&L, balance sheet, invoices and aging in plain English once the connector shows Connected.

### Is the QuickBooks connection read-only?

Yes. CorpusIQ never creates invoices, records payments, or changes anything in your books. The connection uses Intuit's consent flow with the requested scopes shown before approval, and raw customer files or full connector response payloads are not retained.

### Does CorpusIQ work with QuickBooks Desktop?

No. The connector requires QuickBooks Online. Desktop is not supported.

### Can an accountant connect a client's QuickBooks?

Yes, with the right permission level. Accountants connecting on behalf of a client need Company Admin access or the equivalent permission in the client's QuickBooks Online account.

### Why do my numbers not match my accountant's report?

Specify accrual versus cash basis in your question. CorpusIQ uses your QuickBooks default, and each accounting view can report the same activity differently.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "How do I connect QuickBooks to ChatGPT?", "acceptedAnswer": {"@type": "Answer", "text": "Connect QuickBooks in the CorpusIQ dashboard, then ask your question in ChatGPT. CorpusIQ exposes the books through its MCP endpoint, so ChatGPT can query P&L, balance sheet, invoices and aging in plain English once the connector shows Connected."}},
    {"@type": "Question", "name": "Is the QuickBooks connection read-only?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. CorpusIQ never creates invoices, records payments, or changes anything in your books. The connection uses Intuit's consent flow with the requested scopes shown before approval, and raw customer files or full connector response payloads are not retained."}},
    {"@type": "Question", "name": "Does CorpusIQ work with QuickBooks Desktop?", "acceptedAnswer": {"@type": "Answer", "text": "No. The connector requires QuickBooks Online. Desktop is not supported."}},
    {"@type": "Question", "name": "Can an accountant connect a client's QuickBooks?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, with the right permission level. Accountants connecting on behalf of a client need Company Admin access or the equivalent permission in the client's QuickBooks Online account."}},
    {"@type": "Question", "name": "Why do my numbers not match my accountant's report?", "acceptedAnswer": {"@type": "Answer", "text": "Specify accrual versus cash basis in your question. CorpusIQ uses your QuickBooks default, and each accounting view can report the same activity differently."}}
  ]
}
</script>

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
