---
title: "Connect Azure Cosmos DB to ChatGPT via MCP"
description: "Connect Azure Cosmos DB to ChatGPT through CorpusIQ MCP. Ask about containers, events and telemetry in plain English, read-only, with the objects named."
category: ChatGPT Integrations
tags: ["connect Azure Cosmos DB to ChatGPT", "Azure Cosmos DB ChatGPT integration", "MCP cosmosdb connector", "ask ChatGPT about business data", "CorpusIQ MCP"]
last_updated: "2026-11-20"
canonical: "https://www.corpusiq.io/docs/connect-cosmosdb-to-chatgpt"
robots: "index,follow"
---

# How to Connect Azure Cosmos DB to ChatGPT with CorpusIQ MCP

Cosmos DB is usually where the high-volume records live: event logs, telemetry, user activity, IoT readings. It is written to constantly and read almost never, because reading it means writing queries.

Connecting Cosmos DB through CorpusIQ MCP puts a read-only query path behind a plain-English question. You ask how many events of a type arrived last week, and the connector runs the query against your container and reports back.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Why Connect Azure Cosmos DB to ChatGPT?

- **Container visibility.** "List the containers in my Cosmos database" without opening the portal.
- **Field discovery.** Sample-based field shapes and sample values, so you can see what is queryable before writing anything.
- **Distinct counts.** "How many distinct event types did we see, grouped by day?" as a sentence.
- **Ad-hoc SELECT.** Arbitrary read queries against the container you configured.
- **Health checks.** "Is my Cosmos connection healthy?" answered from the connector itself.

### How It Works

1. **Connect Azure Cosmos DB to CorpusIQ.** Enter the endpoint, database and container, then choose key or AAD authentication.
2. **Connect CorpusIQ to ChatGPT** as an MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ translates** the question into read-only queries against your event and telemetry data and assembles the result.
4. **ChatGPT answers** from that result and names the objects each figure came from.

### Before you connect

- An Azure Cosmos DB account using the SQL API
- The endpoint URL, database name and container name
- Either the primary key, or an AAD identity holding the Cosmos DB Data Reader role
- About 3 minutes

### Setup Steps

**In CorpusIQ**

1. In CorpusIQ, open **Dashboard** then **Connectors** and find **Azure Cosmos DB**.
2. Click **Configure**.
3. Enter your endpoint, for example `https://yourdb.documents.azure.com:443/`, plus the database name and container name.
4. Choose the auth method: **Key** pastes the primary key from the Azure portal, **AAD** takes the user principal and tenant ID.
5. Click Save. The connector turns from gray to green once the first query succeeds.

**In ChatGPT**

6. Install **CorpusIQ** from the ChatGPT app store, or add the CorpusIQ MCP server under **Settings**, **Connectors**.
7. Approve the CorpusIQ authorization when prompted, once.
8. Start a new conversation and ask a question that needs your data.

If the connector does not appear, work through the [Quick Start guide](quick-start.md) before changing anything else.

### Example ChatGPT Questions

**Discovery**

- "List the containers in my Cosmos database."
- "What fields does my events container have?"
- "Show me sample values for the event_type field."

**Volume and shape**

- "How many distinct event types did we see, grouped by day?"
- "How many documents arrived in the last 24 hours?"
- "Run this query against Cosmos: SELECT TOP 10 c.event_type, c.timestamp FROM c WHERE c.user_id = 'abc'"

**Operational**

- "Is my Cosmos connection healthy?"
- "Which containers are getting the most writes this week?"

### Security

- **Read-only container access.** The connector exposes reads: connection status, container listing, sample field insight, distinct-value counts and SELECT queries.
- **No document writes.** It never inserts, updates, or deletes documents.
- **Two auth paths.** A primary key works, or an AAD identity scoped to the Cosmos DB Built-in Data Reader role. The AAD path keeps a long-lived key out of the picture.
- **Revocable at any time.** Rotate the key in the Azure portal, or remove the role assignment, and the connection stops working.
- **Scoped direct-MCP retention.** CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Comparison: the native interface vs Azure Cosmos DB through ChatGPT

| Question | The native interface | CorpusIQ MCP with ChatGPT |
|---|---|---|
| Input | A SQL query and knowledge of the document shape | A question in plain language |
| Output | Raw documents | An answer with the query and the shape named |
| Discovery | Data Explorer, container by container | Fields and sample values asked for directly |
| Write path | Full SDK or portal access | None exposed to the assistant |

### FAQ: Common Questions

<details>
<summary><strong>Which Cosmos API does this support?</strong></summary>

The SQL API. Accounts built on the MongoDB, Cassandra, Gremlin or Table APIs are a different query surface and are not what this connector targets.
</details>

<details>
<summary><strong>Key auth or AAD - which should I use?</strong></summary>

AAD if your tenant already manages access centrally: the service account needs the Cosmos DB Built-in Data Reader role on the database, which is a data-plane role, not just an RBAC assignment on the account. Key auth is faster to set up and easier to rotate.
</details>

<details>
<summary><strong>401 Unauthorized. What is wrong?</strong></summary>

The key is wrong or has been rotated. Fetch the current primary key from the Azure portal under the account's Keys blade and re-enter it.
</details>

<details>
<summary><strong>AAD authentication keeps failing. Why?</strong></summary>

The identity needs the Cosmos DB Built-in Data Reader role on the database itself. An RBAC role on the account is not the same permission and will not open the data plane.
</details>

<details>
<summary><strong>Cross-partition errors on some queries. What do I do?</strong></summary>

Some queries have to fan out across partitions. Toggle `cross_partition` in the connection settings for a partitioned container.
</details>

<details>
<summary><strong>Can the assistant write or delete documents?</strong></summary>

No. The connector runs reads and SELECT queries. Inserts, updates, deletes and container changes stay in your application, where they are tested and reviewed.
</details>

---

**Next steps:** [Connect Azure Cosmos DB to ChatGPT now](https://www.corpusiq.io/docs/connectors/cosmosdb)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

## See also

- [Connect Azure Cosmos DB to Claude](connect-cosmosdb-to-claude.md) - containers, events and telemetry in one thread.

- [Connect Azure Cosmos DB to Perplexity](connect-cosmosdb-to-perplexity.md) - the same container questions, asked in Perplexity.

- [Azure Cosmos DB connector reference](connectors/cosmosdb.md) - connection requirements, visible objects and troubleshooting.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
