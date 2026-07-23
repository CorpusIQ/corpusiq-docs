# Security

CorpusIQ is built on the principle that your business data should never leave your tools.

## Data Handling

- **Read-only access** — We request the minimum permissions needed from each connector
- **No data storage** — Query results are passed directly to your AI tool and discarded
- **No data copying** — Your data stays in Shopify, Stripe, QuickBooks, etc.
- **No training** — Your data is never used to train AI models

## Authentication

- **Per-connector OAuth** — Each data source uses its own authentication
- **API keys** — Scoped, revocable keys for programmatic access
- **MCP authentication** — OAuth 2.0 Device Grant for AI tools

## Infrastructure

- Encrypted in transit (TLS 1.3)
- Encrypted at rest (AES-256)
- SOC 2 Type II compliance in progress

## MCP Security

When you connect an AI tool to CorpusIQ via MCP, the connection is authenticated and scoped. Your AI tool can only query data through the MCP protocol — it never gets direct API access to your business tools.

See [MCP Security Best Practices](../docs/mcp-security-best-practices.md) for detailed guidance.
