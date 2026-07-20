---
title: "fastCRW MCP — Open-Source Rust Web Crawler and Search API for AI Agents"
description: "fastCRW is an open-source (AGPL-3.0), self-hostable Rust web crawler and search API. Single ~6MB static binary exposing search and crawl endpoints for AI agents. No API keys, no cloud dependency."
category: mcp
tags: [mcp-server, web-crawler, search, rust, self-hosted, open-source, data-extraction]
last_updated: 2026-07-19
---

# fastCRW MCP Server — Rust Web Crawler for Agents

fastCRW is an open-source, self-hostable web crawler and search API written in Rust. It ships as a single ~6MB static binary that exposes search and crawl endpoints for AI agents. No API keys, no cloud dependency, no usage limits — run it on your own hardware.

**Source:** awesome-mcp-servers PR #8861 (discovered July 19, 2026)
**Category:** Search & Data Extraction
**Author:** us (GitHub)
**Repo:** https://github.com/us/fastcrw
**License:** AGPL-3.0
**Status:** Active

## Why This Matters

Web search is the most common MCP tool and also the most rate-limited and expensive (Brave API costs, Firecrawl credits). fastCRW offers a self-hosted alternative — crawl and search the web from your own infrastructure, with no per-query billing. The 6MB Rust binary means it runs on anything from a Raspberry Pi to a cloud VM.

## Installation

```bash
# Download the binary
curl -L https://github.com/us/fastcrw/releases/latest/download/fastcrw-linux-amd64 -o fastcrw
chmod +x fastcrw

# Run directly
./fastcrw --port 8080
```

## Claude Desktop / Hermes Configuration

```json
{
  "mcpServers": {
    "fastcrw": {
      "command": "/path/to/fastcrw",
      "args": ["--port", "8080"]
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `search` | Web search with ranking and pagination |
| `crawl` | Deep crawl a URL with configurable depth |
| `extract` | Extract clean content from a crawled page |
| `status` | Check crawler health and index size |

## Performance

- Binary size: ~6MB
- Memory: ~50MB idle, scales with crawl depth
- Index: SQLite-backed, survives restarts
- Rate limiting: Configurable politeness delays built in

## CorpusIQ Relevance

For CorpusIQ operators who need competitive intelligence or market research at scale, fastCRW provides an unlimited, self-hosted alternative to paid search APIs. Combined with DataNexus for structured public data, it creates a complete open-source intelligence pipeline.

## See Also

- [[sweeps/sweep-july19-2026]]
- [[datanexus-mcp]]
