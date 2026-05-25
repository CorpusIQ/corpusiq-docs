# Azure Cosmos DB

## What it unlocks
Cosmos DB is often where the unglamorous-but-critical data lives: event logs, telemetry, user activity, IoT readings. Connecting it lets CorpusIQ run read-only queries against your container so you can pull operational data into the same answers as your finance and sales sources.

## Before you connect
- An Azure Cosmos DB account (SQL API)
- The endpoint URL, database name, and container name
- Either a primary key, or an AAD identity with Cosmos DB Data Reader role
- About 3 minutes

## How to connect
1. In CorpusIQ, open Settings → Connectors and find Azure Cosmos DB.
2. Click Configure.
3. <!-- screenshot: Cosmos DB connection form in CorpusIQ -->
4. Enter your endpoint (e.g. `https://yourdb.documents.azure.com:443/`), database name, and container name.
5. Choose your auth method:
   - **Key** — paste the primary key from the Azure portal → Keys.
   - **AAD** — paste the user principal and tenant ID; the service account must have the Cosmos DB Data Reader role on the database.
6. Click Save.

You'll see Cosmos DB change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- Connection status
- A list of containers in the configured database
- Sample-based insights about your container (field shapes, sample values)
- Distinct-value counts grouped by a field
- Arbitrary SELECT queries against your container

CorpusIQ never inserts, updates, or deletes documents.

## Questions you can ask
- "List the containers in my Cosmos database."
- "Run this query against Cosmos: SELECT TOP 10 c.event_type, c.timestamp FROM c WHERE c.user_id = 'abc'"
- "How many distinct event types did we see grouped by day?"
- "What fields does my events container have?"
- "Is my Cosmos connection healthy?"

## Troubleshooting
- **"401 Unauthorized"** — Key is wrong or expired. Get a fresh primary key from Azure portal → Cosmos DB account → Keys.
- **AAD auth fails** — The principal must hold the Cosmos DB Built-in Data Reader role (not just RBAC on the account).
- **Cross-partition errors** — Some queries need `cross_partition=true`. Toggle it in the connection settings if your container is partitioned.
