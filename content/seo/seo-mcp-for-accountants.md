# MCP for Accountants — Ask QuickBooks Questions in Plain English

You spend half your day in QuickBooks. Pulling reports. Running P&Ls. Checking invoices. Reconciling accounts.

What if you could just ask?

> "What's our net income this quarter compared to last quarter?"

> "Show me all unpaid invoices over $5,000 and how many days they're overdue."

> "Which customers have the highest outstanding balance?"

> "Reconcile our Stripe deposits against QuickBooks for this month."

No reports. No exports. No filters. Just questions and answers — drawn from live QuickBooks data.

## The accountant's daily grind

Every accountant knows this routine:

1. Client asks a question ("what's our gross margin by service line?")
2. You open QuickBooks, find the right report, adjust the date range, run it
3. The answer isn't quite what they needed, so you run another report
4. Export to Excel, build a pivot, format it
5. Email it back. Total time: 30-45 minutes

Repeat for 10 clients. That's your whole day.

## How MCP changes the workflow

Connect QuickBooks to an AI assistant once (30 seconds, OAuth, read-only). Then ask:

**Monthly close:**
> "Run the P&L for this month. Compare it to last month and the same month last year. Flag any variances over 10%."

**Accounts receivable:**
> "Show me every invoice past due by more than 30 days, sorted by amount. Include the customer name and last payment date."

**Cash flow:**
> "What's our cash position? Include Stripe deposits that haven't hit QuickBooks yet."

**Client questions:**
> "What was our revenue by service line last quarter? Break it down by customer."

Each answer takes 15 seconds instead of 30 minutes.

## Read-only means safe

Every connection is read-only. The AI can query QuickBooks but cannot create a transaction, modify an entry, or change a single number.

For accountants who handle sensitive financial data, this is non-negotiable. And it's built in from the start.

## What your clients get

When a client can ask their own questions — "what's my burn rate?" "who owes me money?" "how am I doing vs budget?" — they stop emailing you for basic reports.

You spend less time pulling data and more time giving strategic advice. "Here's what the numbers mean and what you should do about them."

That's the job you wanted when you became an accountant.

## The setup

```json
{
  "mcpServers": {
    "corpusiq": {
      "url": "https://mcp2.corpusiq.io/mcp",
      "transport": "streamable-http"
    }
  }
}
```

Connect QuickBooks. Add Stripe for payment reconciliation. Add HubSpot if you track billable client activity. Five minutes total.

Then ask your first question: "Show me everything I need to know for month-end close."

---

*CorpusIQ connects 37+ business tools to AI assistants. QuickBooks-native. Read-only. 5-minute setup. [corpusiq.io](https://www.corpusiq.io)*
