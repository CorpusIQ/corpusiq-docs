# Architecture

CorpusIQ connects AI agents and chat interfaces to 36 business data sources through a single MCP endpoint.

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    AI Clients                            │
│  Claude Desktop · Cursor · Hermes · ChatGPT · Windsurf  │
└────────────────────┬────────────────────────────────────┘
                     │ MCP Protocol
┌────────────────────▼────────────────────────────────────┐
│              CorpusIQ MCP Endpoint                       │
│           corpusiq.io/mcp/direct-connection              │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ OAuth 2.0    │  │ Tool Registry│  │ Prompt Store  │  │
│  │ Device Flow  │  │              │  │              │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                 Connector Layer                          │
│                                                          │
│  Stripe · Shopify · Quickbooks · HubSpot · PostgreSQL   │
│  GA4 · Meta Ads · Klaviyo · Gmail · Slack · MongoDB     │
│  ... 26 more connectors                                  │
└─────────────────────────────────────────────────────────┘
```

## Key Components

### MCP Endpoint
The single entry point for all AI interactions. Implements the Model Context Protocol specification. Supports `tools/list`, `tools/call`, `resources/list`, `resources/read`, `prompts/list`, and `prompts/get`.

### Authentication Layer
OAuth 2.0 Device Authorization Grant for AI agents. Email-based authentication for chat users. Each data source connection requires one-time OAuth authorization.

### Connector Layer
Individual adapters for each of the 36 supported business data sources. Each connector handles authentication, data retrieval, normalization, and error handling for its specific API.

### Data Flow

1. AI agent sends a query via MCP
2. MCP endpoint authenticates the request
3. Tool registry maps the query to the appropriate connector(s)
4. Connector retrieves data from the source API
5. Data is normalized and returned to the agent
6. Agent presents the answer to the user

## Security Model

- Read-only access to all connected data sources
- OAuth 2.0 with refresh token rotation
- Device flow prevents credential exposure
- HTTPS/TLS for all connections
- Audit logging of all queries
- Scoped access per data source

## Deployment

CorpusIQ is a hosted service. The MCP endpoint runs on production infrastructure with automatic scaling and high availability.

The [demo.corpusiq.io](https://demo.corpusiq.io) chat interface is a web application that connects to the same MCP endpoint used by AI agents.
