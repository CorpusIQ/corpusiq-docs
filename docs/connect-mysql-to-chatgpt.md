---
title: Connect MySQL to ChatGPT via MCP
description: "Connect a MySQL database to ChatGPT through CorpusIQ MCP. Ask about orders, customers and revenue in plain English with cited answers."
category: ChatGPT Integrations
tags: ["connect MySQL to ChatGPT", "MySQL ChatGPT integration", "MCP database connector", "SQL data to ChatGPT", "ask questions about MySQL", "CorpusIQ MCP"]
last_updated: "2026-10-20"
canonical: "https://www.corpusiq.io/docs/connect-mysql-to-chatgpt"
robots: "index,follow"
---

# How to Connect MySQL to ChatGPT with CorpusIQ MCP

MySQL sits under a large share of commerce and SaaS applications, and its data is usually reachable only through the application that owns it. Anyone who wants a number either asks an engineer or exports a CSV. **Connecting MySQL to ChatGPT through CorpusIQ MCP** opens the read side of that database to a plain-English question, with a read-only credential and a cited answer.

Direct MCP retrieval is read-only and does not retain raw customer files or full connector response payloads; operational query logs are retained for up to 30 days.

## What Questions Can You Ask?

- "How many new customers signed up each week this quarter?"
- "Which products had the highest return rate last month?"
- "What is average order value by channel, by month?"
- "Which subscriptions are past due?"
- "Show me the ten slowest-moving SKUs by days since last sale."

## FAQ: Common Questions

<details>
<summary><strong>Is the connection read-only?</strong></summary>

Yes. The retrieval path reads tables and returns results. It does not write, update, or delete rows, and it does not alter schema. A dedicated read-only role reinforces that at the database level, which is the control that actually holds.
</details>

<details>
<summary><strong>What does it need to connect?</strong></summary>

A reachable MySQL instance and a user with SELECT on the schemas you want available. Connection details are entered once in the CorpusIQ dashboard and are not passed to the assistant. A read replica is a sensible target if the primary is busy.
</details>

<details>
<summary><strong>Does it work with MySQL hosted on a provider?</strong></summary>

Yes, provided the instance accepts connections from outside its own network. Managed providers often allowlist inbound IPs, so the connector has to be permitted before it can reach the database. PlanetScale, RDS, and Cloud SQL all support this.
</details>

<details>
<summary><strong>How does it handle a large schema?</strong></summary>

It exposes the tables and columns visible to the connecting role. That is why scoping matters: a role limited to the six tables that answer real questions produces sharper answers than a role that sees every table in the instance, including logs and staging copies.
</details>

<details>
<summary><strong>Can it join across tables?</strong></summary>

Yes. Joins, aggregates, and date grouping are the reason to connect a database at all. "Revenue by month by plan" typically touches three tables that no one outside engineering would know how to combine.
</details>

<details>
<summary><strong>Will answers expose personal data?</strong></summary>

Answers follow the question and come from a read-only SELECT against the connected database. CorpusIQ does not retain raw customer files or full connector response payloads. If a column must never be exposed, revoke it from the connecting role; that is the boundary the connector cannot cross.
</details>

<details>
<summary><strong>Can I compare MySQL data with Shopify or Stripe?</strong></summary>

Yes. "Does the orders table match Stripe payouts for last month" reads both sources in one pass, which is usually the first question worth asking after connecting. See [Benefits of MCP for Business](benefits-of-mcp-for-business.md).
</details>

<details>
<summary><strong>Is this the same as the PostgreSQL connector?</strong></summary>

The pattern is identical: read-only, schema-aware, plain-English questions. The difference is the driver and the connection details. See [Connect PostgreSQL to ChatGPT](connect-postgresql-to-chatgpt.md) if your data lives there instead.
</details>

## Setup Guide

1. **Create a read-only user.** Grant SELECT on the schemas you want exposed, nothing more.
2. **Sign up** at [corpusiq.io](https://www.corpusiq.io) -- the 30-day trial needs no credit card.
3. **Connect MySQL.** Dashboard, Connections, MySQL, then enter the host, database, and read-only credentials.
4. **Connect ChatGPT.** Add the CorpusIQ MCP server per the [Quick Start guide](quick-start.md).
5. **Verify.** Ask for a number you already know, such as last month's order count.
6. **Explore.** Then ask the question that has always needed an engineer.

## Related Pages

- [Connect PostgreSQL to ChatGPT](connect-postgresql-to-chatgpt.md) -- the same pattern for PostgreSQL
- [Browse all CorpusIQ connectors](connectors.md) -- the full list
- [MCP vs API Integrations](mcp-vs-api-integrations.md) -- why the access model differs
- [CorpusIQ Security Architecture](../security/) -- how credentials and data are handled
- [AI for Data Analysis](ai-for-data-analysis.md) -- the analysis use case
- [Rate Limits and Quotas](how-it-works/rate-limits-and-quotas.md) -- the operational limits

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
