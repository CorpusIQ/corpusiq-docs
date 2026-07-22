# Connect NetSuite to Claude

Query your NetSuite ERP data directly from Claude using CorpusIQ.

## Setup

1. [Connect NetSuite](https://corpusiq.io) in your CorpusIQ dashboard
2. Add CorpusIQ to Claude Desktop as an MCP server: `https://mcp2.corpusiq.io/mcp`
3. Start asking questions

## Example Questions

- "What was our net income this quarter?"
- "Show me all unpaid invoices over 30 days"
- "Compare revenue by subsidiary for the last 3 months"
- "Which vendors have pending bills due this week?"

## What You Can Access

- Financial statements and transactions
- Accounts payable and receivable
- Inventory and fulfillment
- Purchase orders and vendor records
- Saved searches and reports

## Security

CorpusIQ uses read-only access. Claude can query your NetSuite data but cannot create, update, or delete records.

See the [Claude connector guide](connectors/ai-mcp-server-for-business-data.md) for detailed setup.
