# AI Agent Users

Connect your AI agent directly to CorpusIQ via MCP at [corpusiq.io/mcp/direct-connection](https://www.corpusiq.io/mcp/direct-connection).

## Direct MCP Connection Architecture

```
AI Agent (Claude, Cursor, Hermes, etc.)
        |
        | MCP Protocol
        |
CorpusIQ MCP Endpoint
        |
        | OAuth 2.0 Device Flow
        |
36 Business Data Sources (Stripe, Shopify, Quickbooks, etc.)
```

Your AI agent connects to a single MCP endpoint. CorpusIQ handles authentication, data retrieval, and normalization across all 36 connected sources. Your agent sees one unified interface.

## Agent Authentication Process

CorpusIQ uses OAuth 2.0 Device Flow for agent authentication. No browser required:

1. Your agent initiates a connection to the MCP endpoint
2. CorpusIQ returns a device code and verification URL
3. You verify the connection once via any browser or mobile device
4. Your agent receives an access token
5. Subsequent connections use the refresh token

**Device login takes approximately 45 seconds from start to finish.**

[Watch the device login demo](https://github.com/CorpusIQ/corpusiq-docs/blob/main/assets/mcp-device-login-demo.mp4)

## Connection Requirements

- MCP-compatible AI agent (Claude Desktop, Cursor, Hermes, Windsurf, etc.)
- Internet connection
- One-time device verification via browser or mobile device
- No API keys needed from individual data sources

## Supported MCP Capabilities

| Capability | Description |
|-----------|-------------|
| **tools/list** | Discover all available data query tools |
| **tools/call** | Execute queries against connected data sources |
| **resources/list** | List available data sources and schemas |
| **resources/read** | Read specific data from a connected source |
| **prompts/list** | Get suggested query prompts |
| **prompts/get** | Retrieve a specific prompt template |

## Available Tools and Actions

Your AI agent can perform these actions through the MCP endpoint:

**Revenue & Financial:**
- Query Stripe revenue, invoices, subscriptions
- Pull Quickbooks P&L, balance sheet, transactions
- Check payment status and history

**Customer & CRM:**
- Search HubSpot contacts and deals
- Query customer purchase history
- Check support ticket status

**E-commerce:**
- Query Shopify orders and products
- Check inventory levels
- Pull Amazon Seller metrics

**Marketing:**
- Query Meta Ads campaign performance
- Pull Google Analytics data
- Check Klaviyo email metrics

**Database:**
- Execute PostgreSQL and MySQL queries
- Query MongoDB collections
- Read from Microsoft SQL Server

**Full list of 36 connectors in the [connectors directory](../connectors/README.md).**

## Security Considerations

- OAuth 2.0 Device Flow with refresh tokens
- All connections use HTTPS/TLS
- Tokens are scoped to specific data sources
- No raw API keys exposed to AI agents
- Device verification prevents unauthorized access
- Refresh tokens can be revoked at any time
- Audit logging of all agent queries

## Troubleshooting Procedures

**Connection refused:**
- Verify the MCP endpoint URL: `https://www.corpusiq.io/mcp/direct-connection`
- Check internet connectivity
- Ensure your agent supports MCP protocol

**Authentication failed:**
- Verify your device code hasn't expired (5 minute window)
- Complete device verification at the provided URL
- Check that your account has active data source connections

**Tool not found:**
- Run `tools/list` to see available tools
- Ensure your data sources are connected in the CorpusIQ dashboard
- Some tools require specific data source connections

**Rate limiting:**
- CorpusIQ enforces fair-use rate limits
- If you hit limits, queries will return 429 with retry-after header
- Contact support for increased limits
