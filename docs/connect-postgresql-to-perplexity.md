---
title: "Connect PostgreSQL to Perplexity via MCP"
description: "Connect PostgreSQL to Perplexity through CorpusIQ MCP. Ask about orders, customers and revenue in plain language and get answers with the tables named"
category: Perplexity Integrations
tags: ["connect PostgreSQL to Perplexity", "Postgres Perplexity integration", "MCP database connector", "SQL data to AI", "ask Perplexity about a database", "CorpusIQ MCP"]
last_updated: "2026-11-14"
canonical: "https://www.corpusiq.io/docs/connect-postgresql-to-perplexity"
robots: "index,follow"
---

# How to Connect PostgreSQL to Perplexity with CorpusIQ MCP

A PostgreSQL database holds the operational truth of a business: orders, customers, invoices, inventory, events. Almost nobody outside engineering can read it.

Most questions about that data end in one of two places: a request to the data team, or a spreadsheet exported last month and quietly out of date.

Connecting PostgreSQL through CorpusIQ MCP puts the read side of the database behind a plain-language question. You ask, Perplexity reads the tables as they stand, and the answer names the tables and columns it used.

### Why Connect PostgreSQL to Perplexity?

- **Counts without a ticket.** "How many orders did we take last week, by day?" instead of a request to engineering.
- **Customer questions.** "Which accounts are above 10,000 in revenue over the last 90 days?"
- **Stock state.** "Which SKUs have stock on hand below the reorder point?"
- **Behaviour questions.** "What is the average time between signup and first order?"
- **Schema-aware SQL.** Perplexity reads the tables and columns the connecting role can see, then writes the join rather than describing how to write it.
- **Read-only by role.** SELECT on the schemas you grant, and nothing else. The retrieval tools documented on this page are read-only.

### How It Works

1. **Create a read-only role in PostgreSQL** and grant SELECT on the schemas you want reachable.
2. **Connect PostgreSQL to CorpusIQ** in the dashboard with the host, database name and that role's credentials.
3. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
4. **CorpusIQ translates** the question into a read-only query, runs it against your instance, and returns the rows.
5. **Perplexity answers** from the result, naming the tables it read and adding outside context where you asked for it.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

### Setup Steps

**In PostgreSQL**

1. Create a role for this purpose. Do not reuse the application owner account.
2. Grant SELECT on the schemas that hold the data you want answerable, and nothing else.
3. Confirm the instance accepts connections from outside its own network. An allowlist has to include the connector before anything else works.

**In CorpusIQ**

4. Open your dashboard and go to **Connectors**.
5. Select **PostgreSQL** and enter the host, database name and the read-only credentials.
6. The connector turns green once the first query succeeds.

**In Perplexity**

7. Open **Settings** and find the **MCP servers** section.
8. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

9. Connect and approve the CorpusIQ authorization page once.
10. Start a new thread and ask a question about the database.

### Example Perplexity Questions

**Trading and revenue**

- "How many orders did we take last week, by day?"
- "Show revenue by month for the last 12 months and tell me which month broke the trend."
- "Which customers spent more than 10,000 in the last 90 days?"
- "Is that customer concentration normal for a business of our size?"

**Operations and stock**

- "Which SKUs are below the reorder point right now, sorted by how far below?"
- "What is the median time from order to shipment, by warehouse?"
- "Which orders are still open after 14 days?"

**Schema and exploration**

- "List the tables in the public schema and tell me which ones look transactional."
- "Which columns join the orders table to the customers table?"
- "Write the query that answers the last question, then run it."

**Cross-source**

- "Compare the orders table total for last month against Stripe payouts." (requires the Stripe connector)
- "Which accounts in the CRM have no rows in the orders table?" (requires the CRM connector)

### Security

- **Read-only role.** SELECT on scoped schemas. The credential cannot write, and the MCP path does not try.
- **Credential stays in CorpusIQ.** Connection details are held encrypted; the database decides what the role may see.
- **Network allowlist.** The instance has to accept the connection for anything to work, so an allowlist stays the first control, not an afterthought.
- **Scoped direct-MCP retention.** Raw customer files and full connector response payloads are not retained. Operational logs keep query text, tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between your database, CorpusIQ and Perplexity.

### Comparison: A SQL Client vs PostgreSQL in Perplexity

| Aspect | A SQL client | CorpusIQ MCP with Perplexity |
|---|---|---|
| Who can use it | Someone who writes SQL | Anyone who can ask a question |
| Input | A query | A question in plain language |
| Outside context | Switch tabs and search separately | Same thread, same answer |
| Joins across systems | Export both sides | Asked across connectors |
| Write risk | Whatever the login can do | None through the retrieval tools |
| Answer | Rows to interpret | Rows plus the reading of them |

A query returns rows. The question is what the rows mean, and that is the part a person still has to do.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity change anything in the database?</strong></summary>

No. The retrieval tools documented on this page are read-only, and the role you create carries SELECT on the schemas you granted. Nothing writes, deletes or alters a table.
</details>

<details>
<summary><strong>Which PostgreSQL versions and managed services are covered?</strong></summary>

Anything that speaks the PostgreSQL wire protocol, including the managed offerings on AWS, Google Cloud and Azure. The connector connects the same way a client would.
</details>

<details>
<summary><strong>Does it read the whole database?</strong></summary>

Only what the role can see. Schema grants are the boundary, so a database with several tenant schemas can expose one of them.
</details>

<details>
<summary><strong>What about row-level visibility?</strong></summary>

Row-level security policies still apply to the connecting role. If the policy restricts rows, the answers only ever see the rows the role may read.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. Each question runs against the current state of the tables. Verify time-sensitive figures against the cited rows.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. PostgreSQL is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Where is the database data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [read-only and security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect PostgreSQL to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
