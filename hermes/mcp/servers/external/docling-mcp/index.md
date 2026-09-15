---
title: Docling MCP - Agentic Document Processing from IBM's Docling
description: "MCP server making Docling agentic: PDF and document conversion to structured JSON/Markdown, document generation and caching, with remote (Docling Serve API), local and hybrid execution and Milvus/LlamaIndex RAG integration. LF AI & Data project, MIT, 727 stars."
category: Productivity
stars: "727 (docling-project/docling-mcp)"
added: 2026-09-01
source: "chatmcp/mcpso issue #3873 (Sep 1, 2026)"
relevance: ★★★
tags: [mcp-server, document-processing, pdf, rag, conversion, docling, local-first]
---

# Docling MCP

**Docling, made agentic.** Docling MCP wraps the Docling document-processing library as an MCP service: convert PDFs and other documents into structured JSON or Markdown, generate documents, and cache conversions for repeat use. It runs in remote mode against the Docling Serve API, in local mode with automatic local fallback, and integrates with Milvus and LlamaIndex for RAG pipelines.

```
Server type: stdio (local) or Streamable HTTP (Docling Serve remote mode)
Install: pip install docling-mcp (PyPI) / uvx
Compatibility: docling-mcp >=3.0.0 requires MCP Python SDK >=2.0.0; pin <3.0.0 for SDK v1 clients
Registry: listed on the official MCP Registry + Glama
License: MIT · LF AI & Data project · Built by the Docling project (IBM open source)
```

## Why This Matters for Operators

Documents are where business data goes to die. Docling MCP gives agents a real conversion surface instead of a regex hack.

First, **structured output from messy files.** PDFs, scanned layouts and mixed-format documents convert to JSON or Markdown with layout structure preserved, which means an agent can actually search, cite and re-render what used to be a wall of pixels.

Second, **execution flexibility.** Local mode keeps documents on your hardware; remote mode offloads to the Docling Serve API; hybrid mode tries remote and falls back locally. That matters for operators with privacy constraints on some documents and throughput needs on others.

Third, **RAG-native.** Milvus and LlamaIndex integrations mean the converted output feeds a retrieval pipeline directly, so the agent's answers are grounded in the actual document content.

## Tools and Capabilities

| Capability | Description |
|-----------|-------------|
| Document conversion | PDF and document files to structured JSON / Markdown |
| Document generation | Generate documents through the service |
| Caching | Reuse converted results to avoid repeat processing |
| Execution modes | Remote (Docling Serve API), local, hybrid with automatic local fallback |
| RAG integrations | Milvus and LlamaIndex for vector retrieval pipelines |

## Verification (Sep 1, 2026)

- GitHub verified: docling-project/docling-mcp, 727 stars, 135 forks, Python, MIT, pushed Sep 1, 2026.
- Official MCP Registry listing confirmed via the project badge; Glama listing confirmed.
- LF AI & Data foundation project (docling-project org, IBM open source lineage).
- Submitted via chatmcp/mcpso issue #3873 with a client configuration snippet for Cursor / Claude Desktop (stdio transport).
