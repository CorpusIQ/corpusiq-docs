# MongoDB

## What it unlocks
Point CorpusIQ at your own MongoDB and ask questions about your application data in plain English. No more pulling engineers off feature work to write one-off queries.

## Before you connect
- Connection details for the MongoDB cluster you want to query: host, port, username, password, database name.
- The credentials should be read-only — CorpusIQ never needs write access.
- A network path: if your cluster is private, allowlist CorpusIQ's outbound IP or use a public read replica.
- About 5 minutes.

## How to connect
This is not an OAuth flow. You configure MongoDB directly.

1. Open your CorpusIQ dashboard and click Connections.
2. Find MongoDB and click Connect.
<!-- screenshot: MongoDB configuration form in CorpusIQ -->
3. Paste your MongoDB connection string (or fill in host, port, user, password individually).
4. Choose the database you want CorpusIQ to query.
5. Save.

You'll see MongoDB change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
- The collections in the database you specified.
- Document structure and sampled fields.
- Read-only query results you ask for.

CorpusIQ runs read queries only. It never inserts, updates, or drops anything.

## Questions you can ask
- "How many users signed up in the last 7 days?"
- "What's the average order value in the orders collection this month?"
- "Show me the schema of the events collection."
- "Find documents in customers where status is churned."

## Troubleshooting
- "Connection refused" — your MongoDB host is blocking CorpusIQ. Allowlist the IP shown in the dashboard.
- "Auth failed" — double-check the username and password. Special characters in passwords must be URL-encoded.
- No collections listed — confirm the user has read access to the database you selected.

<!-- DOC-GAP: No internal SETUP doc exists. Setup steps inferred from registry + standard MongoDB driver conventions. Verify before publish. -->
