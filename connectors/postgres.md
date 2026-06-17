# PostgreSQL

## What it unlocks
Point CorpusIQ at your production or analytics Postgres database and ask questions about your real data in plain English. Skip the JIRA ticket to engineering for one-off counts.

## Before you connect
- Connection details: host, port, database name, username, password.
- A read-only Postgres role is strongly recommended (CREATE USER ... WITH NOLOGIN... GRANT SELECT...).
- Network access — if the database is in a private VPC, allowlist CorpusIQ's outbound IP.
- About 5 minutes.

## How to connect
This is not an OAuth flow. You configure Postgres directly.

1. Open your CorpusIQ dashboard and click Connections.
2. Find PostgreSQL and click Connect.
<!-- screenshot: Postgres connection form in CorpusIQ -->
3. Paste your connection string, or fill in host, port (default 5432), database, user, and password individually.
4. Save. CorpusIQ tests the connection.

You'll see PostgreSQL change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
- Tables in the database you configured.
- Schema and column types for any table you ask about.
- Read-only results of SELECT queries it builds from your questions.

CorpusIQ runs SELECT queries only. No writes, no schema changes.

## Questions you can ask
- "How many active subscriptions do we have?"
- "What's our MRR by plan this month?"
- "Describe the users table."
- "Show signups per day for the last 30 days."

## Troubleshooting
- "Connection refused" — your Postgres host is blocking CorpusIQ. Allowlist the outbound IP shown in the dashboard.
- "Password authentication failed" — confirm the role exists and the password is correct. URL-encode special characters in passwords.
- "Permission denied for table" — grant SELECT on the schema to your CorpusIQ user.

<!-- DOC-GAP: No internal SETUP doc exists. Setup steps inferred from registry + standard Postgres conventions. Verify before publish. -->

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
