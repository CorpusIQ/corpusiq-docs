# Architecture

CorpusIQ connects your business tools to AI platforms through a read-only MCP server. No data is moved, copied, or stored.

## How It Works

1. **Connect** — You authenticate each data source once. CorpusIQ stores a read-only token.
2. **Query** — Your AI tool sends a question through the MCP protocol.
3. **Route** — CorpusIQ determines which connectors are needed and queries them in parallel.
4. **Answer** — Results are returned to your AI tool with full source citation.

## Key Design Decisions

- **Read-only by default** — CorpusIQ never writes to your business tools
- **No data warehouse** — Queries run against live APIs, not stale copies
- **Single MCP server** — One endpoint for all 37+ connectors
- **Source citation** — Every answer includes which tool and field the data came from

## Technical Details

See [How It Works](../how-it-works/) for deep dives on cross-source query execution, caching, and the MCP protocol implementation.
