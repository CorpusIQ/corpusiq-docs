# Recipe: Monthly Close in Minutes Instead of Days

**Time to value:** 5 minutes setup.
**Connectors needed:** QuickBooks, Stripe. Optional: Shopify.
**Skill level:** Operator. No code.

## The problem

Monthly close means logging into QuickBooks and running a dozen reports: P&L, balance sheet, AR aging, AP aging, open invoices, unreconciled transactions. Each report takes 3 to 5 minutes to find, set date ranges, export, and review.

Then you do the same thing in Stripe. And Shopify. Then you compare them. Then you realize your QuickBooks P&L total and your Stripe settlement total differ by $847 and you spend 40 minutes finding it.

Your accountant does this every month and bills you for the time.

## What you'll ask your AI

After connecting QuickBooks and Stripe:

- "Run my monthly close for June. Show me P&L summary, outstanding invoices, unreconciled Stripe charges, and any discrepancies between Stripe settlements and QuickBooks deposits."
- "Which QuickBooks invoices from June are still unpaid? Sort by amount, show me the biggest ones first."
- "Compare this month's P&L to last month. What changed by more than 20 percent?"

## Setup

1. Connect QuickBooks and Stripe through CorpusIQ
2. Read-only OAuth for both. Your AI reads financial data, never creates, edits, or deletes anything.
3. Ask your first close question.

## Example: Full monthly close in one question

Ask:

> "Close June 2026 for me. Show P&L: total revenue, COGS, gross profit, operating expenses, net income. Show AR aging: invoices over 30, 60, 90 days. List Stripe charges from June that don't match any QuickBooks deposit. Flag anything unusual."

Your AI queries QuickBooks for financial statements and AR, Stripe for charges and payouts, cross-references by amount and date, and delivers a complete close package in seconds. Every number has a source citation.

## Why this matters

A typical monthly close for a small business takes 8 to 16 hours. Most of that is pulling reports from different tools and reconciling them. Your AI can do the data gathering and reconciliation in seconds.

You still review the numbers. You still make the calls. But you stop being a report runner and start being an operator.

One question. All your tools. Close done.

---

**Contributed by:** CorpusIQ Growth Agent
**Connectors used:** `quickbooks`, `stripe`, `shopify` (optional)
