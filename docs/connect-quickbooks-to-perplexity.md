---
title: "Connect QuickBooks to Perplexity via MCP"
description: "Connect QuickBooks to Perplexity through CorpusIQ MCP. Ask about margin, overdue invoices and cash position and get cited answers from your own books"
category: Perplexity Integrations
tags: ["connect QuickBooks to Perplexity", "QuickBooks Perplexity integration", "MCP QuickBooks connector", "QuickBooks data to AI", "ask QuickBooks in plain English", "CorpusIQ MCP"]
last_updated: "2026-11-12"
canonical: "https://www.corpusiq.io/docs/connect-quickbooks-to-perplexity"
robots: "index,follow"
---

# How to Connect QuickBooks to Perplexity with CorpusIQ MCP

Perplexity is good at the outside world. Industry benchmarks, market context, what changed this week.

It cannot see your gross margin, your overdue invoices, or your cash position, because none of that is public.

Connecting QuickBooks through CorpusIQ MCP puts both in one thread. Perplexity answers the question about your business from your own books, read-only, and names the records it read.

### Why Connect QuickBooks to Perplexity?

- **Margin questions in context.** "Our gross margin is 61 percent. How does that compare to the industry average?" Both halves answered in one thread.
- **Overdue receivables.** "Which customers are more than 30 days past due, and how much do they owe?"
- **Cash position.** A question that pulls balance sheet, AR aging and AP aging together instead of three reports.
- **Spend review.** "What did we spend on software this quarter, and which vendors grew the most?"
- **Benchmark framing.** Take a real number from QuickBooks, then ask Perplexity how it compares.
- **Read-only by scope.** The OAuth grant is read access to company data. It cannot post a journal entry or edit an invoice.

### How It Works

1. **Connect QuickBooks to CorpusIQ** through Intuit's OAuth consent screen, granting read-only access.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ reads** the accounts, invoices, customers and reports that answer the question.
4. **Perplexity answers** with the figure, the period it covers, and the world knowledge you asked for around it.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational query logs are kept for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Open your dashboard and go to **Connectors**.
2. Select **QuickBooks** and click **Connect QuickBooks**.
3. You land on Intuit's OAuth consent screen. Review the scopes (Company Info, Customers, Invoices, Accounts, Reports, Vendors) and approve the read-only grant.
4. Return to CorpusIQ. The connector turns green and your books are queryable.

**In Perplexity**

5. Open **Settings** and find the **MCP servers** section.
6. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

7. Connect and approve the CorpusIQ authorization page once.
8. Start a new thread and ask a question about your books.

Requires QuickBooks admin credentials for the initial grant. No API keys to manage and no analyst in the loop.

### Example Perplexity Questions

**Profitability**

- "What was our net income last quarter, and how does our margin compare to the industry average?"
- "Which service line has the highest gross margin, and is that normal for our sector?"
- "How has our operating expense ratio moved over the last four quarters?"

**Receivables**

- "Which customers are more than 30 days overdue, and what is the total?"
- "Who are our five largest open invoices, and how old are they?"
- "Which customer has been late three months in a row?"

**Cash and spend**

- "What is our cash position today, and what is due out in the next two weeks?"
- "What did we spend on software this quarter, and which vendors grew most?"

**Cross-source**

- "Do the customers who are past due in QuickBooks still have open deals in the CRM?" (requires the CRM connector)
- "Compare QuickBooks revenue to Shopify payouts for the same month." (requires the Shopify connector)

### Security

- **Read-only retrieval tools.** The tools documented on this page are marked read-only, and the OAuth grant covers read access to company information, customers, invoices, accounts, reports and vendors. There is no path from Perplexity into a journal entry.
- **No stored credentials on your side.** CorpusIQ holds the encrypted OAuth token; you hold the Intuit grant and can revoke it at any time.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Intuit, CorpusIQ and Perplexity.

### Comparison: QuickBooks Reports vs QuickBooks in Perplexity

| Aspect | QuickBooks reports | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A report you configure | A question in plain language |
| Output | Rows and totals | An answer with the period named |
| Outside context | Copy the number elsewhere | Same thread, same answer |
| Cross-system | Export and join by hand | Asked across connectors |
| Follow-up | Rebuild the report | Ask the next question |
| Write access | Yes, by you | None, read-only |

A report answers the question you already knew how to configure. A connected ledger answers the one you did not.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity change anything in QuickBooks?</strong></summary>

No. The retrieval tools are marked read-only, so the connection cannot post a journal entry or edit an invoice. Books, bills and customer records are untouched.
</details>

<details>
<summary><strong>Does this need a QuickBooks accountant or developer seat?</strong></summary>

No. The connection is an OAuth grant made by a QuickBooks admin, and the questions are plain language.
</details>

<details>
<summary><strong>Which QuickBooks products are covered?</strong></summary>

QuickBooks Online. The connector reads through the Intuit API, so the same grant covers company info, sales, purchases and reports for that company.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. Each question reads the current state of the books, so an invoice paid a minute ago is reflected in the next answer. Verify time-sensitive figures against the cited record.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. QuickBooks is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Can I keep one company out of reach?</strong></summary>

The grant is per company. Connect a different QuickBooks company and it carries its own authorization, so you choose which books are visible.
</details>

<details>
<summary><strong>Where is the QuickBooks data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [read-only and security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect QuickBooks to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
