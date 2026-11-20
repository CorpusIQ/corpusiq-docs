---
title: "Connect Azure Cosmos DB to Perplexity via MCP"
description: "Connect Azure Cosmos DB to Perplexity through CorpusIQ MCP. Ask about containers, event types and event volume in plain English, with objects named."
category: Perplexity Integrations
tags: ["connect Azure Cosmos DB to Perplexity", "Cosmos DB Perplexity integration", "MCP cosmosdb connector", "ask Perplexity about telemetry", "container queries in plain English", "CorpusIQ MCP"]
last_updated: "2026-11-20"
canonical: "https://www.corpusiq.io/docs/connect-cosmosdb-to-perplexity"
robots: "index,follow"
---

# How to Connect Azure Cosmos DB to Perplexity with CorpusIQ MCP

Cosmos DB is written to constantly and read almost never, because reading it means writing a query. Event logs, telemetry, user activity and device readings accumulate in a container that has no natural reporting surface and no reason for anyone outside the engineering team to open the portal.

**Connecting Azure Cosmos DB to Perplexity through CorpusIQ MCP** puts that container behind a plain-English question. You ask how many events of a type arrived last week, the connector runs a read query against the container you configured, and the answer names the objects it read next to the outside context Perplexity already provides.

### Why Connect Azure Cosmos DB to Perplexity?

- **Container visibility.** "List the containers in my Cosmos database" without opening the portal.
- **Field discovery.** Sample-based field shapes and sample values, so you can see what is queryable before writing anything.
- **Volume by type and day.** "How many distinct event types did we see, grouped by day, for the last two weeks?"
- **Ad-hoc reads.** A read query against the container you configured, asked as a sentence.
- **Health checks.** "Is my Cosmos connection healthy?" answered from the connector itself.
- **Read-only by capability.** The retrieval tools documented on this page read container metadata, sample data and query results. They never insert, update or delete a document.

### Before you connect

- An Azure Cosmos DB account using the SQL API
- The endpoint URL, database name and container name
- Either the primary key, or an AAD identity holding the Cosmos DB Data Reader role on the database
- About 3 minutes

### How It Works

1. **Connect Azure Cosmos DB to CorpusIQ.** Enter the endpoint, database and container, then choose key or AAD authentication.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **Ask a container question.** CorpusIQ runs the read query against your container and assembles the result.
4. **Perplexity answers** from that result and names the container and the fields each figure came from.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Open **Dashboard**, then **Connectors**, and find **Azure Cosmos DB**.
2. Click **Configure**.
3. Enter your endpoint, for example `https://yourdb.documents.azure.com:443/`, plus the database name and the container name.
4. Choose the auth method: **Key** pastes the primary key from the Azure portal, **AAD** takes the user principal and tenant ID, and that identity needs the Cosmos DB Data Reader role on the database.
5. Click Save. The connector turns from gray to green once the first read succeeds.

**In Perplexity**

6. Open **Settings** and find the **MCP servers** section.
7. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

Then start a new thread and ask a question the data can answer. Which container is reachable is decided by the database and container you typed at configure time; nothing outside it is read.

### Example Perplexity Questions

**Containers and fields**

- "List the containers in my Cosmos database."
- "What fields does my events container have, and what does a sample record look like?"
- "Which fields are present on most records and which are sparse?"

**Volume and shape**

- "How many distinct event types did we see grouped by day over the last two weeks?"
- "How has the record count per day moved since the start of the month?"
- "Which event type has the longest tail, and how many records sit in it?"

**Operational**

- "Is my Cosmos connection healthy?"
- "Run this against Cosmos: SELECT TOP 10 c.event_type, c.timestamp FROM c WHERE c.user_id = 'abc'"
- "Which user IDs appear most often in the last seven days of activity events?"

**Cross-source**

- "Do signup events in Cosmos line up with the signups QuickBooks shows as paying customers?" (requires the QuickBooks connector)
- "Which event types spike on the same days as ad spend?" (requires an ads connector)

### Security

- **Read tools only.** The retrieval tools documented on this page read connection status, container lists, sample field shapes, distinct-value counts and query results.
- **No document is written.** The connector runs SELECT statements. Inserts, updates and deletes are outside the connection, not hidden behind a confirmation.
- **Your Azure grant stays yours.** With key auth CorpusIQ holds the encrypted key, and with AAD it holds a scoped identity; both can be revoked in Azure at any time.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text, tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Cosmos DB, CorpusIQ and Perplexity.

### Comparison: Azure Portal Data Explorer and CorpusIQ MCP with Perplexity

| Aspect | Azure Portal Data Explorer | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A SQL query and a partition key | A question in the thread you are already working in |
| Scope | One container per query window | Container shape, field census and volume in one answer |
| Access | Portal access and the query dialect | Plain English, no query to write |
| Context | Open another tab for the business figure | Outside context and your telemetry in the same answer |
| Write access | Yes, for anyone with the role | None through the retrieval tools |
| Audit | Query history per portal session | The objects named in every answer |

The portal answers what is in the container. The business question is usually what the telemetry says about a customer or a release, and that answer needs the rest of the record.

### FAQ: Common Questions

<details>
<summary><strong>What does the connector expose?</strong></summary>

Connection status, the containers in the configured database, sample-based field shapes and sample values, distinct-value counts grouped by a field, and the results of read queries against the container.
</details>

<details>
<summary><strong>Can Perplexity write to Cosmos DB?</strong></summary>

No. The connector runs SELECT statements only. There is no insert, update, delete or container management action in the connection.
</details>

<details>
<summary><strong>Key or AAD, which should I use?</strong></summary>

Key auth is the shortest path and takes the primary key from the Azure portal. AAD avoids a long-lived key: the identity needs the Cosmos DB Data Reader role on the database, plus the user principal and tenant ID.
</details>

<details>
<summary><strong>Does it read every container in the account?</strong></summary>

No. Configure one database and one container. The other containers in the account are not reachable through that connection.
</details>

<details>
<summary><strong>How fresh is the data?</strong></summary>

Queries run against the live container when you ask. Event volume that is still being written can move between two consecutive questions, so a window that includes the current hour may show partial figures.
</details>

<details>
<summary><strong>Does this work in ChatGPT or Claude too?</strong></summary>

Yes. Cosmos DB is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

### See Also

- [Connect Azure Cosmos DB to ChatGPT](connect-cosmosdb-to-chatgpt.md) - the same container questions, asked in ChatGPT
- [Azure Cosmos DB connector reference](connectors/cosmosdb.md) - what is visible, and the boundary
- [Connect PostgreSQL to Perplexity](connect-postgresql-to-perplexity.md) - the relational side of the same data estate
- [Connect Microsoft SQL Server to Perplexity](connect-mssql-to-perplexity.md) - operational tables beside the telemetry
- [Browse all CorpusIQ connectors](connectors.md) - the full list

---

**Next steps:** [Add CorpusIQ to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
