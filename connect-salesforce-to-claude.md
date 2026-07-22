# Connect Salesforce to Claude

Query your Salesforce data directly from Claude using CorpusIQ.

## Setup

1. [Connect Salesforce](https://corpusiq.io) in your CorpusIQ dashboard
2. Add CorpusIQ to Claude Desktop as an MCP server: `https://mcp2.corpusiq.io/mcp`
3. Start asking questions

## Example Questions

- "Show me all open opportunities closing this month"
- "Which accounts haven't been contacted in 30 days?"
- "What's our pipeline value by stage?"
- "Pull up the last 5 activities for account Acme Corp"

## What You Can Access

- Opportunities and pipeline
- Accounts and contacts
- Activities and tasks
- Reports and dashboards
- Custom objects (depending on your Salesforce setup)

## Security

CorpusIQ uses read-only access. Claude can query your Salesforce data but cannot create, update, or delete records.

See the [Claude connector guide](connectors/ai-mcp-server-for-business-data.md) for detailed setup.
