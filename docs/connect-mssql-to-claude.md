---
title: "Connect Microsoft SQL Server to Claude via MCP"
description: "Connect Microsoft SQL Server to Claude through CorpusIQ MCP. Ask about tables, orders and customers in plain English, read-only, with the objects named."
category: Claude Integrations
tags: ["connect Microsoft SQL Server to Claude", "Microsoft SQL Server Claude integration", "MCP mssql connector", "ask Claude about business data", "CorpusIQ MCP"]
last_updated: "2026-11-17"
canonical: "https://www.corpusiq.io/docs/connect-mssql-to-claude"
robots: "index,follow"
---

# How to Connect Microsoft SQL Server to Claude with CorpusIQ MCP

SQL Server is where the unglamorous records live: orders, invoices, stock moves, line-of-business tables that an ERP writes and nobody reads without a query window. The data is current and the access is narrow - a handful of people hold the credentials.

Connecting SQL Server through CorpusIQ MCP turns a query request into a question. You ask, the connector runs a SELECT against the database you authorised, and the answer names the tables it read.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Why Connect Microsoft SQL Server to Claude?

- **Counts without a ticket.** "How many customers did we add this quarter?" instead of a request to whoever holds the login.
- **Operational totals.** "Show me last month's total sales from the Orders table." Totals, not a CSV.
- **Schema answers.** "Describe the schema of the Invoices table" reads back real columns and types.
- **Cross-source questions.** A database total checked against the same figure in QuickBooks or Stripe in one pass.
- **Read-only by construction.** The connector builds SELECT statements. No INSERT, UPDATE, DELETE, or DDL.

### How It Works

1. **Connect Microsoft SQL Server to CorpusIQ.** Enter the host, port, database name and the credentials of a read-only SQL login in the dashboard.
2. **Connect CorpusIQ to Claude** as an MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ translates** the question into read-only queries against your operational record and assembles the result.
4. **Claude answers** from that result and names the objects each figure came from.

### Before you connect

- Server hostname and port (1433 unless your instance moved it)
- Database name
- A SQL login and password - a read-only login is strongly recommended
- Network reachability: if the server sits on a private network, allowlist the outbound address shown in your dashboard

### Setup Steps

**In CorpusIQ**

1. Open your CorpusIQ dashboard and go to **Connectors**.
2. Find **Microsoft SQL Server (MSSQL)** and click Connect. This is a direct configuration form, not an OAuth flow.
3. Enter the host, port, database name, username and password.
4. Optionally toggle encryption and certificate trust so they match your server's setup.
5. Save. The connector turns from gray to green once the first connection succeeds.

**In Claude Desktop**

6. Open **Settings**, **Developer**, **Edit Config**. This opens `claude_desktop_config.json`.
7. Add the CorpusIQ entry:

```json
{
  "mcpServers": {
    "corpusiq": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote",
        "https://mcp2.corpusiq.io/mcp"
      ]
    }
  }
}
```

8. Save the file and quit Claude Desktop completely, not just the window.
9. Reopen Claude and complete the device login when prompted. The tools indicator appears next to the message box.

If the tools indicator does not appear, work through [Claude can't see CorpusIQ](troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

### Example Claude Questions

**Inventory and structure**

- "List the tables in the warehouse database."
- "Describe the schema of the Invoices table, including column types."
- "Which tables look transactional rather than reference data?"

**Revenue and customers**

- "Show me last month's total sales from the Orders table."
- "How many customers did we add this quarter?"
- "Which customers ordered more than 10,000 in the last 90 days?"

**Cross-source**

- "Does the Orders table total for last month match the QuickBooks revenue figure?" (requires the QuickBooks connector)
- "Which customers in the CRM have no rows in the Orders table?" (requires the CRM connector)

### Security

- **Read-only login.** Create a SQL login that holds SELECT on the schemas you want exposed, and nothing else. That grant is the boundary.
- **SELECT only.** The connector builds SELECT statements. It does not insert, update, delete, or run schema changes.
- **Network position.** A private instance stays private until its firewall allows the connection, so an allowlist sits in front of the credential.
- **Revocable at any time.** Disable the SQL login or remove the connection in CorpusIQ and access stops.
- **Scoped direct-MCP retention.** CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Comparison: the native interface vs Microsoft SQL Server through Claude

| Question | The native interface | CorpusIQ MCP with Claude |
|---|---|---|
| Input | A query window and knowledge of the schema | A question in plain language |
| Output | Rows you read | A synthesised answer naming the tables used |
| Access | Whoever holds the login | The read-only login you scoped |
| Write path | Whatever the login allows | None exposed to the assistant |
| Cross-source | Copy the result into another tool | Asked alongside finance and CRM data |

### FAQ: Common Questions

<details>
<summary><strong>Does this work with Azure SQL as well as SQL Server?</strong></summary>

Yes. Azure SQL is the same engine reached over the network, so the same host, port, database and credential fields apply. Add the outbound address to the server's firewall rules.
</details>

<details>
<summary><strong>Do I have to use a read-only login?</strong></summary>

The connector only ever builds SELECT statements, but a read-only login means a mistake upstream cannot become a write. Create the login with SELECT on the schemas you want answerable and leave it there.
</details>

<details>
<summary><strong>Login failed. What should I check?</strong></summary>

SQL Authentication has to be enabled on the server - Windows Authentication alone is not enough for this connection type. Then confirm the username, password and database name.
</details>

<details>
<summary><strong>Cannot open server. Is the password wrong?</strong></summary>

Usually not. That error is the network: the server's firewall is refusing the connection. Allowlist the outbound address shown in your CorpusIQ dashboard.
</details>

<details>
<summary><strong>Encryption error on save. What now?</strong></summary>

A self-signed certificate fails the default trust check. Toggle "Trust server certificate" to match your server's setup, or install a certificate the server can validate.
</details>

<details>
<summary><strong>Which tables can the assistant see?</strong></summary>

Exactly the tables your SQL login can read. If a table is missing from answers, the login is missing the grant - that is the intended control point.
</details>

---

**Next steps:** [Connect Microsoft SQL Server to Claude now](https://www.corpusiq.io/docs/connectors/mssql)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

## See also

- [Connect Microsoft SQL Server to ChatGPT](connect-mssql-to-chatgpt.md) - tables, schema and operational totals in one thread.

- [Microsoft SQL Server connector reference](connectors/mssql.md) - connection requirements, visible objects and troubleshooting.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
