---
title: "Connect PostgreSQL to Claude via MCP - Live Database Answers"
description: "Connect a PostgreSQL database to Claude through CorpusIQ MCP. Ask about orders, customers and revenue in plain language and get answers with the tables named."
category: Claude Integrations
tags: ["connect PostgreSQL to Claude", "Postgres Claude integration", "MCP database connector", "SQL data to Claude", "ask Claude about a database", "CorpusIQ MCP"]
last_updated: "2026-10-30"
canonical: "https://www.corpusiq.io/docs/connect-postgresql-to-claude"
robots: "index,follow"
---

# How to Connect PostgreSQL to Claude with CorpusIQ MCP

A PostgreSQL database holds the operational truth of a business: orders, customers, invoices, inventory, events. Almost nobody in the company can read it. Everyone else waits for a report, and the report is out of date the day it arrives.

Connecting PostgreSQL through CorpusIQ MCP puts the read side of that database behind a plain-language question. You ask, Claude reads the tables as they stand, and the answer names what it looked at.

### Why Connect PostgreSQL to Claude?

- **Counts without a ticket.** "How many orders did we take last week, by day?" instead of a request to engineering.
- **Customer questions.** "Which accounts are above 10,000 in revenue over the last 90 days?"
- **Inventory state.** "Which SKUs have stock on hand below the reorder point?"
- **Behaviour questions.** "What is the average time between signup and first order?"
- **Schema-aware SQL.** Claude reads the tables and columns the connecting role can see, then writes the join instead of describing how to write it.
- **Read-only by scope.** The connection reads. It does not update, delete, or run schema changes.

### How It Works

1. **Create a read-only role in PostgreSQL** and grant SELECT on the schemas you want reachable.
2. **Connect PostgreSQL to CorpusIQ** in the dashboard with the host, database name, and that role's credentials.
3. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your account settings.
4. **CorpusIQ translates** the question into a read-only query, runs it against your instance, and returns the rows.
5. **Claude answers** from the result, naming the tables and columns it used.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In PostgreSQL**

1. Create a role for this purpose. Do not reuse the application's owner account.
2. Grant SELECT on the schemas that hold the data you want answerable, and nothing else.
3. Confirm the instance accepts connections from outside its own network. An allowlist has to include the connector before anything else can work.

**In CorpusIQ**

4. Log in and open **Connections**.
5. Select **PostgreSQL** and enter the host, database name, and the read-only credentials.
6. Copy the MCP config block shown under **Settings, Integrations, Claude Desktop**.

**In Claude Desktop**

7. Open **Settings, Developer, Edit Config**. This opens `claude_desktop_config.json`.
8. Add the CorpusIQ entry:

```json
{
  "mcpServers": {
    "corpusiq": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote",
        "https://www.corpusiq.io/mcp/direct-connection"
      ]
    }
  }
}
```

9. Save the file and fully quit Claude Desktop. Not just the window: quit the application.
10. Reopen Claude, complete the device login when prompted, and the tools indicator appears next to the message box.

If the tools indicator does not appear, work through [Claude can't see CorpusIQ](troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

### Example Claude Questions

**Trading and revenue**

- "How many orders did we take last week, by day?"
- "Show revenue by month for the last 12 months and tell me which month broke the trend."
- "Which customers spent more than 10,000 in the last 90 days?"

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
- **Credential stays in CorpusIQ.** Connection details are entered once in the dashboard and are not exposed to the assistant.
- **Visible is answerable.** What the role cannot see, the answer cannot contain. Scoping the role is the control that matters.
- **Revocable in minutes.** Drop the role or revoke the connection and access ends.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between your database host, CorpusIQ, and Claude.

### Comparison: A Reporting Tool vs Postgres Through Claude

| Aspect | Dashboard or BI tool | CorpusIQ MCP with Claude |
|---|---|---|
| Who can ask | Whoever was trained on the tool | Anyone who can write a sentence |
| New question | A new chart or a request | A question, answered live |
| Joins | Modelled in advance | Written per question |
| Across sources | Warehouse or export first | Asked in one pass |
| Latency to first answer | Days to weeks | Under a minute |
| Write access | As configured | None, read-only role |

The BI tool is the right home for numbers you check every Monday. The connector is the right tool for the question nobody has asked before.

### FAQ: Common Questions

<details>
<summary><strong>Is the connection read-only?</strong></summary>

Yes. The retrieval path reads. It does not update or delete rows, and it does not run schema changes. A write-capable path for an application is a different credential with a different purpose, and it is not part of this connector.
</details>

<details>
<summary><strong>What do I need to connect a database?</strong></summary>

A reachable PostgreSQL instance and a role that can read the schemas you want exposed. The standard practice is a dedicated read-only role scoped to those schemas rather than your application's owner account. Connection details go in once, in the CorpusIQ dashboard.
</details>

<details>
<summary><strong>Does it work with hosted Postgres?</strong></summary>

Yes, if the instance accepts connections from outside its own network. Supabase, Neon, RDS, and Cloud SQL all support this, and providers that restrict inbound access to an allowlist need that allowance added before the connector can reach the database.
</details>

<details>
<summary><strong>How does Claude know my schema?</strong></summary>

It sees the tables and columns the connecting role can see, which is also why scoping the role matters. A role with access to twelve schemas produces worse answers than a role scoped to the three that matter, because irrelevant tables compete for attention and invite the wrong join.
</details>

<details>
<summary><strong>Can it join tables?</strong></summary>

Yes. Joins, aggregations, and date bucketing are the reason to put a database behind this interface. "Revenue by month by channel" usually means three tables and a join nobody in the room would have written by hand.
</details>

<details>
<summary><strong>Will it show raw customer records?</strong></summary>

It runs a read-only SELECT for the question you ask. CorpusIQ does not retain raw customer files or full connector response payloads. If your data policy forbids exposing certain columns at all, exclude them from the connecting role's grants. That is the control that holds, not a prompt instruction.
</details>

<details>
<summary><strong>Can I combine database data with Shopify, Stripe, or QuickBooks?</strong></summary>

Yes. "Does our Stripe revenue match the orders table for last month" reads both sources in one pass, and that comparison is usually the reason a database connector is worth connecting at all.
</details>

<details>
<summary><strong>What about performance?</strong></summary>

Queries run against your database, so cost follows your own query patterns. Filter by date range and select the columns you need, exactly as you would in any client. A read replica is the safest target if the primary is load sensitive.
</details>

<details>
<summary><strong>Why Claude rather than the database console?</strong></summary>

Claude reads the schema, holds the whole question, and writes the query while explaining what it assumed. The console gives you an empty prompt. For one-off questions from people who do not live in SQL, that difference is the product.
</details>

---

**Next steps:** [Connect PostgreSQL to Claude now](https://corpusiq.io/connect/postgresql-with-claude)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
