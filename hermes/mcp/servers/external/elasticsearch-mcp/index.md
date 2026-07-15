---
title: "Elasticsearch MCP — Full-Text Search & Observability for AI Agents"
description: "Connect AI agents to Elasticsearch via the official Elastic MCP server. Full-text search, vector search, aggregations, and observability."
category: mcp
tags: [mcp-server]
last_updated: 2026-07-15
---

# Elasticsearch MCP — Full-Text Search & Observability for AI Agents

## What It Is

Elastic MCP exposes Elasticsearch search and observability capabilities over the Model Context Protocol. AI agents can query any index with Elasticsearch Query DSL, run kNN semantic search, and monitor APM traces, logs, and infrastructure metrics.

## Tools Available

| Tool | Description |
|------|-------------|
| Full-text search | Query any index with Elasticsearch Query DSL |
| Vector search | kNN semantic search across embeddings |
| Aggregations | Buckets, metrics, pipeline aggregations |
| Observability | APM traces, logs, and infrastructure metrics |

## Quick Start

```bash
npx -y @elastic/mcp-server-elasticsearch
```

## Business Use Cases

1. Log investigation: "Find all ERROR-level logs from the payments service in the last hour"
2. Semantic search: "Find documents related to our refund policy"
3. Infrastructure health: "Show me APM traces with latency over 500ms"

## Limitations

- Elasticsearch 8.x+ required. Vector search needs dense_vector field mappings.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connector Catalog](/hermes/mcp/connectors/)
