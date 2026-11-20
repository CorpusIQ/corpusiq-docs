---
title: "Connect Microsoft SQL Server to Perplexity via MCP"
description: "Connect SQL Server or Azure SQL to Perplexity through CorpusIQ MCP. Ask operational questions in plain English, answered from SELECT queries with no SQL."
category: Perplexity Integrations
tags: ["connect Microsoft SQL Server to Perplexity", "MSSQL Perplexity integration", "Azure SQL in Perplexity", "MCP MSSQL connector", "query SQL Server in plain English", "CorpusIQ MCP"]
last_updated: "2026-11-20"
canonical: "https://www.corpusiq.io/docs/connect-mssql-to-perplexity"
robots: "index,follow"
---

# How to Connect Microsoft SQL Server to Perplexity with CorpusIQ MCP

SQL Server is where the unglamorous records live: orders, invoices, stock moves and line-of-business tables that an ERP writes and nobody reads without a query window. The data is current and the access is narrow, which is exactly why the questions that need it queue behind whoever holds the login.

**Connecting Microsoft SQL Server to Perplexity through CorpusIQ MCP** turns a query request into a question. You ask, the connector builds and runs a SELECT against the database you authorised, and the answer names the tables it read next to the outside context Perplexity already provides.

### Why Connect Microsoft SQL Server to Perplexity?

- **Counts without a ticket.** "How many customers did we add this quarter?" instead of a request to whoever holds the login.
- **Operational totals.** "Show me last month's total sales from the Orders table." Totals, not a CSV.
- **Schema answers.** "Describe the schema of the Invoices table" reads back real columns and types.
- **Cross-source questions.** A database total checked against the same figure in QuickBooks or Stripe in one pass.
- **Read-only by construction.** The connector builds SELECT statements. No INSERT, UPDATE, DELETE or DDL is available.
- **Warehouse and line-of-business in one place.** Several databases can be connected, each with its own read login.

### Before you connect

- Server hostname and port (1433 unless your instance moved it)
- Database name and a SQL login and password; a read-only login is strongly recommended
- Network reachability: if the server sits on a private network, allowlist the outbound address shown in your dashboard
- About 5 minutes

### How It Works

1. **Connect Microsoft SQL Server to CorpusIQ.** Enter the host, port, database name and the credentials of a read-only SQL login in the dashboard.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **Ask an operational question.** CorpusIQ translates it into read-only queries against your operational record and assembles the result.
4. **Perplexity answers** from that result and names the tables and columns each figure came from.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Open **Dashboard**, then **Connections**, and find **MSSQL**.
2. Click **Connect**.
3. Enter host, port (default 1433), database name, username and password. A read-only login is the recommended shape.
4. Optionally toggle encryption and certificate trust to match your server's setup, and allowlist the outbound address if the server sits on a private network.
5. Save. The connector turns from gray to green once the first query succeeds.

**In Perplexity**

6. Open **Settings** and find the **MCP servers** section.
7. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

Then start a new thread and ask a question the data can answer. Which database is reachable is decided by the connection you saved; other databases on the same server are not read.

### Example Perplexity Questions

**Structure and schema**

- "List the tables in the warehouse database, grouped by schema."
- "Describe the schema of the Invoices table."
- "Which tables reference the customer ID column?"

**Operational totals**

- "Show me last month's total sales from the Orders table."
- "How many customers did we add this quarter, by month?"
- "Which line items moved the most units in the last 30 days?"

**Exceptions**

- "Which open orders are older than 30 days and still unshipped?"
- "Which stock items sit below their reorder point?"
- "Which invoices past due are larger than a thousand dollars?"

**Cross-source**

- "Does the revenue in this database match what QuickBooks shows for the same month?" (requires the QuickBooks connector)
- "Do the orders here reconcile with the charges in Stripe?" (requires the Stripe connector)

### Security

- **Read tools only.** The retrieval tools documented on this page read the table list, column schemas and the results of SELECT statements built from your question.
- **No write statements.** The connector does not issue INSERT, UPDATE, DELETE or DDL, and a read-only login removes the capability at the database as well.
- **Your credentials stay yours.** CorpusIQ holds the encrypted login; you can rotate it in the database at any time and update the connection here.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text, tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between SQL Server, CorpusIQ and Perplexity, with encryption and certificate trust configurable to match the server.

### Comparison: SQL Server Management Studio and CorpusIQ MCP with Perplexity

| Aspect | SQL Server Management Studio | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A query, a login and a schema you have to know | A question in the thread you are already working in |
| Audience | Whoever holds the credentials | Anyone the account is shared with, inside the permissions configured |
| Scope | One database per query window | Tables, totals and exceptions in one answer |
| Outside context | Open another tab | Same thread, same answer |
| Write access | Yes, for the login you use | None through the retrieval tools |
| Audit | Whatever the server logs | The tables and columns named in every answer |

SSMS answers what the database contains. The business question is usually whether the number agrees with the other systems that describe the same month, and that answer lives in two places.

### FAQ: Common Questions

<details>
<summary><strong>What does the connector expose?</strong></summary>

The tables in the configured database, column schemas for the tables it is asked about, and the read-only results of SELECT queries built from your questions.
</details>

<details>
<summary><strong>Can Perplexity modify or delete data?</strong></summary>

No. The connector issues SELECT statements only. INSERT, UPDATE, DELETE and DDL are not available through the connection.
</details>

<details>
<summary><strong>Do I need a read-only login?</strong></summary>

It is strongly recommended and it is the second layer of the same boundary: the connector does not build write statements, and a read-only login means the credentials could not carry one if it tried.
</details>

<details>
<summary><strong>What if the server sits behind a firewall?</strong></summary>

Allowlist the outbound address shown in your dashboard. A hostname that resolves from your desk but not from outside the network produces the "Cannot open server" error.
</details>

<details>
<summary><strong>Does it work with Azure SQL?</strong></summary>

Yes. Azure SQL Database connects the same way: host, port, database, login. Encryption is on by default there, so leave certificate trust off unless the server presents a self-signed certificate.
</details>

<details>
<summary><strong>Does this work in ChatGPT or Claude too?</strong></summary>

Yes. SQL Server is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

### See Also

- [Connect Microsoft SQL Server to ChatGPT](connect-mssql-to-chatgpt.md) - the same database questions, asked in ChatGPT
- [Microsoft SQL Server connector reference](connectors/mssql.md) - what is visible, and the boundary
- [Connect PostgreSQL to Perplexity](connect-postgresql-to-perplexity.md) - the same pattern on a different engine
- [Connect QuickBooks to Perplexity](connect-quickbooks-to-perplexity.md) - the books side of the reconciliation
- [Browse all CorpusIQ connectors](connectors.md) - the full list

---

**Next steps:** [Add CorpusIQ to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
