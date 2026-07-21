---
title: "codicil — Documentation Indexing MCP with Chroma + Ollama"
description: "Index your repo's Markdown/YAML/TOML docs into a local Chroma vector store and expose query_docs/reindex_docs over MCP. Uses Ollama embeddings when available, falls back to keyword search."
source: github.com/colehellman/codicil
stars: 0
language: Python
transport: stdio
auth: None
category: Knowledge & Documentation
last_updated: 2026-07-21
---

# codicil — Documentation Indexing MCP

**Repo documentation made queryable through MCP.** codicil indexes your repository's Markdown, YAML, and TOML documentation into a local Chroma vector store. AI agents can then query docs semantically. Uses Ollama embeddings when available; gracefully degrades to keyword search with zero external dependencies.

## What It Does for Operators

- **Semantic doc search** — AI agents can query your project's documentation using natural language
- **Zero infra** — No external API keys needed. Works entirely locally with Chroma (embedded) + optional Ollama
- **Graceful degradation** — If Ollama isn't running, falls back to live keyword search on disk — no failure mode
- **Auto-reindex** — Reindex command for when docs change
- **Multi-format** — Supports Markdown, YAML, and TOML documentation files

## Installation

```bash
git clone https://github.com/colehellman/codicil.git
cd codicil
pip install -r requirements.txt

# Optional: Install Ollama for semantic search
# curl -fsSL https://ollama.com/install.sh | sh
# ollama pull nomic-embed-text
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "codicil": {
      "command": "python",
      "args": ["-m", "codicil.server"],
      "env": {
        "CODICIL_DOCS_PATH": "/path/to/your/repo/docs"
      }
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `query_docs` | Semantic (or keyword) search across indexed documentation |
| `reindex_docs` | Rebuild the vector index from updated docs |
| `get_doc_context` | Retrieve the full document for a search result |
| `list_indexed` | List all indexed documents and their status |

*Note: Tool names are approximate. See github.com/colehellman/codicil.*

## Operator Use Cases

1. **Development Teams** — "How do we handle error retries in our SDK?" → AI agent queries internal docs
2. **Technical Writers** — Verify documentation coverage by querying for missing topics
3. **Onboarding** — New team members ask AI agents about internal processes instead of digging through wikis
4. **Open Source Maintainers** — Give contributors AI-powered documentation search

## CorpusIQ Angle

codicil solves an internal documentation problem that many CorpusIQ operators face: "where is that documented?" For operators building on CorpusIQ, codicil can index the CorpusIQ docs alongside their own internal documentation, giving AI agents a unified knowledge surface.

## Limitations

- Chroma is embedded (not production-scale for massive doc corpuses)
- Semantic search quality depends on Ollama embedding model
- No cloud sync — each developer runs their own index
- Python-only (no Node/TypeScript version)
