---
name: "dokumendiregister MCP"
description: "Free, no-API-key MCP server for Estonian public-authority document registers"
category: "Data & Analytics"
source: "mcp.so"
discovered: "2026-07-23"
verified: false
repository: "https://github.com/dokumendiregister/dokumendiregister"
---

# dokumendiregister MCP — Estonian Public Document Search

A free, no-authentication MCP server that searches Estonian public-authority document registers (dokumendiregistrid). One search across all authorities, with every document linked to the companies named in it. Built on dokumendiregister.ee open data.

## What It Does

- **Unified search** — Search across all Estonian public authority document registers in one query
- **Company linking** — Every document is linked to the companies named within it
- **No API key** — Completely open access, no authentication required
- **Open data** — Built on Estonia's public dokumendiregister.ee infrastructure

## Quick Start

```bash
# Clone and install
git clone https://github.com/dokumendiregister/dokumendiregister
cd dokumendiregister
npm install

# Add to Claude Code
claude mcp add dokumendiregister -- npx tsx src/index.ts

# Or Hermes Agent
hermes mcp add dokumendiregister -- npx tsx /path/to/dokumendiregister/src/index.ts
```

**Prerequisites:** Node.js 20+. No API key needed.

## Key Tools

| Tool | Description |
|------|-------------|
| `search_documents` | Full-text search across all authority registers |
| `get_document` | Retrieve a specific document by ID |
| `find_company_docs` | Get all documents referencing a specific company |
| `list_authorities` | List all covered public authorities |

## Use Cases

- **Due diligence** — Search for all public documents mentioning a target company
- **Compliance monitoring** — Track regulatory filings and public notices for monitored entities
- **Legal research** — Cross-reference company documents across multiple authorities
- **Market intelligence** — Monitor competitors' public filings in Estonia

---

*Discovered via [mcp.so](https://mcp.so) sweep. Listed in the [CorpusIQ MCP Catalog](https://corpusiq-docs/hermes/mcp/).*
