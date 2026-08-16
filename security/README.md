# Security

CorpusIQ reads authorized business records live and limits what it retains.

## Data Handling

- **Operation-level permissions** — Retrieval and write-capable tools are separately named and safety-annotated; provider scopes vary by documented operation
- **Scoped retention** — Direct MCP does not retain raw customer files or full connector response payloads; operational logs may persist for up to 30 days
- **No raw-data warehouse** — Source systems remain authoritative; optional indexed search has a separate embeddings and minimal-metadata lifecycle
- **No CorpusIQ model training** — CorpusIQ does not use customer data to train models; conversation handling follows the selected AI provider's plan and settings

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
