# Microsoft SQL Server (MSSQL)

## What it unlocks
Connect a SQL Server or Azure SQL database and ask questions about your operational data without writing SQL. Useful for internal systems — ERPs, line-of-business apps, data warehouses.

## Before you connect
- Connection details: server hostname, port, database name, username, password.
- A read-only SQL login is strongly recommended.
- Network access — if the database is on a private network, allowlist CorpusIQ's outbound IP.
- About 5 minutes.

## How to connect
This is not an OAuth flow. You configure MSSQL directly.

1. Open your CorpusIQ dashboard and click Connections.
2. Find MSSQL and click Connect.
<!-- screenshot: MSSQL configuration form -->
3. Enter host, port (default 1433), database name, username, and password.
4. Optionally toggle encryption and certificate trust to match your server's setup.
5. Save.

You'll see MSSQL change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
- The tables in the database you configured.
- Column schemas for any table you ask about.
- Read-only results of SELECT queries it builds from your questions.

CorpusIQ runs SELECT queries only. No INSERT, UPDATE, DELETE, or DDL.

## Questions you can ask
- "List the tables in the warehouse database."
- "Show me last month's total sales from the Orders table."
- "How many customers did we add this quarter?"
- "Describe the schema of the Invoices table."

## Troubleshooting
- "Login failed" — check that SQL Authentication is enabled on the server (not just Windows Auth) and the credentials are correct.
- "Cannot open server" — firewall is blocking CorpusIQ. Allowlist the outbound IP from your dashboard.
- "Encryption error" — toggle "Trust server certificate" if your server uses a self-signed cert.
