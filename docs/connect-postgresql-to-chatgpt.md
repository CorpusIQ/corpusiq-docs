---
title: Connect PostgreSQL to ChatGPT via MCP
description: "Connect a PostgreSQL database to ChatGPT through CorpusIQ MCP. Ask about tables, orders and customers in plain English with cited answers."
category: ChatGPT Integrations
tags: ["connect PostgreSQL to ChatGPT", "Postgres ChatGPT integration", "MCP database connector", "SQL data to ChatGPT", "ask questions about a database", "CorpusIQ MCP"]
last_updated: "2026-10-20"
canonical: "https://www.corpusiq.io/docs/connect-postgresql-to-chatgpt"
robots: "index,follow"
---

# How to Connect PostgreSQL to ChatGPT with CorpusIQ MCP

A PostgreSQL database holds the operational truth of a business: orders, customers, invoices, events, inventory. The problem is that only a handful of people can read it, and everyone else waits for a report. **Connecting PostgreSQL to ChatGPT through CorpusIQ MCP** puts the read side of that database behind a plain-English question, with read-only access and a cited answer.

Direct MCP retrieval is read-only and does not retain raw customer files or full connector response payloads; operational query logs are retained for up to 30 days.

## What Questions Can You Ask?

- "How many orders did we take last week, by day?"
- "Which customers had revenue above $10,000 in the last 90 days?"
- "What is the average time between signup and first order?"
- "Which SKUs have stock on hand below the reorder point?"
- "Show me revenue by month for the last 12 months, and the trend line."

Answers come from the database as it stands when you ask. No nightly extract, no warehouse refresh.

## FAQ: Common Questions

<details>
<summary><strong>Is the connection read-only?</strong></summary>

Yes. The retrieval path reads. It does not write, update, or delete rows, and it does not run schema changes. If you need a separate write path for an application, that is a different credential with a different purpose.
</details>

<details>
<summary><strong>What do I need to connect a database?</strong></summary>

A reachable PostgreSQL instance and a role that can read the schemas you want exposed. The usual practice is a dedicated read-only role scoped to those schemas rather than your application's owner account. Connection details are entered once in the CorpusIQ dashboard; they are not exposed to the assistant.
</details>

<details>
<summary><strong>Does it work with hosted Postgres?</strong></summary>

Yes, if the instance accepts connections from outside its own network. Providers that restrict inbound access to an allowlist need that allowance added before the connector can reach the database. Supabase, Neon, RDS, and Cloud SQL all support this.
</details>

<details>
<summary><strong>How does the assistant know my schema?</strong></summary>

It exposes the tables and columns the connecting role can see. That is also why scoping the role matters: what the role cannot see, the assistant cannot answer from. A role with access to 12 schemas will produce worse answers than a role scoped to the 3 that matter.
</details>

<details>
<summary><strong>Can it join tables?</strong></summary>

Yes. Joins, aggregations, and date bucketing are the point of putting a database behind this interface. "Revenue by month by channel" usually means three tables and a join the requester would never have written themselves.
</details>

<details>
<summary><strong>Will it show raw customer records?</strong></summary>

It answers the question you ask by running a read-only SELECT against the connected database. CorpusIQ does not retain raw customer files or full connector response payloads. If your data policy forbids exposing certain columns at all, exclude them from the connecting role's grants; that is the control that matters.
</details>

<details>
<summary><strong>Can I combine database data with Shopify, Stripe, or QuickBooks?</strong></summary>

Yes. A question like "does our Stripe revenue match the orders table for last month" reads both sources in one pass. That comparison is usually the reason a database connector is worth connecting at all. See [Benefits of MCP for Business](benefits-of-mcp-for-business.md).
</details>

<details>
<summary><strong>What about performance?</strong></summary>

Queries run against your database, so cost follows your own query patterns. Filter by date range and select the columns you need, exactly as you would with any client. A read replica is the safest place to point this at if the primary is load sensitive.
</details>

## How It Works

1. You create a read-only role in PostgreSQL for the schemas you want available.
2. You add the connection in the CorpusIQ dashboard.
3. You add the CorpusIQ MCP server to ChatGPT. See the [Quick Start guide](quick-start.md).
4. ChatGPT discovers the database tools and calls them when a question needs your data.
5. Only a SELECT runs, and its result is returned live.

## Setup Guide

1. **Create a read-only role.** Grant SELECT on the schemas you want exposed, nothing more.
2. **Sign up** at [corpusiq.io](https://www.corpusiq.io) -- the 30-day trial needs no credit card.
3. **Connect PostgreSQL.** Dashboard, Connections, PostgreSQL, then enter the host, database, and the read-only credentials.
4. **Connect ChatGPT.** Add the CorpusIQ MCP server per the [Quick Start guide](quick-start.md).
5. **Verify.** Ask a question whose answer you already know, for example last month's order count.
6. **Explore.** Move to the question nobody has had time to answer.

## Related Pages

- [Connect PostgreSQL to Claude](connect-postgresql-to-claude.md) -- the same connection, set up for Claude Desktop
- [Browse all CorpusIQ connectors](connectors.md) -- the full list
- [MCP vs API Integrations](mcp-vs-api-integrations.md) -- why the access model differs
- [CorpusIQ Security Architecture](../security/) -- how credentials and data are handled
- [How to Connect Business Data to ChatGPT](how-to-connect-business-data-to-chatgpt.md) -- the general setup
- [AI for Data Analysis](ai-for-data-analysis.md) -- the analysis use case
- [Rate Limits and Quotas](how-it-works/rate-limits-and-quotas.md) -- the operational limits

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
