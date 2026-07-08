# Connect QuickBooks to Claude — Financial Answers in Plain English

You run your business on QuickBooks. P&L, balance sheet, invoices, expenses. Every answer requires running a report.

What if you could just ask Claude?

> "What's our net income this quarter? Compare to last quarter."

> "Which customers owe us money? How much and how long?"

> "Show me expenses by category. Any unusual spikes?"

Here's how in 2 minutes.

## Step 1: corpusiq.io — connect QuickBooks via OAuth (read-only, 30 seconds)

## Step 2: Add to Claude Desktop

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

## Step 3: Ask Claude anything about your QuickBooks data

Live data. Every time. Read-only.

---

*CorpusIQ: Connect QuickBooks to Claude. 2 minutes. [corpusiq.io](https://www.corpusiq.io)*
