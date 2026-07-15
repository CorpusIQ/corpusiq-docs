---
title: "Scrivener MCP — Integration Guide"
description: "Connect Scrivener manuscripts to AI assistants. 53+ tools for document management, writing analysis, semantic search, and character/plot tracking."
category: mcp
tags: [mcp-server, writing, productivity, content-creation, document-management]
last_updated: 2026-07-14
---

# Scrivener MCP Server

**Repository:** [writerslogic/scrivener-mcp](https://github.com/writerslogic/scrivener-mcp)
**By:** Writers Logic
**Stars:** 33
**Category:** Productivity, Writing, Content Creation
**Auth:** Local (file system access)

## Overview

The Scrivener MCP server is the first dedicated bridge between Scrivener — the industry-standard writing tool for authors, screenwriters, and researchers — and AI assistants. With 53 tools spanning document management, writing analysis, content enhancement, offline semantic search, and character/plot tracking, it transforms how writers interact with their manuscripts.

At 33 GitHub stars with a comprehensive toolset, this is one of the most ambitiously scoped MCP servers targeting a specific professional tool. The offline semantic search capability (no cloud dependency) is particularly notable for privacy-conscious authors.

## What You Can Do

- **Document Management:** Navigate, create, and organize Scrivener projects through natural language
- **Writing Analysis:** Analyze prose for readability, pacing, repetition, and style consistency
- **Content Enhancement:** Generate suggestions for scene improvement, dialogue refinement, and structural edits
- **Semantic Search:** Search across entire manuscripts for themes, character arcs, and plot points — fully offline
- **Character & Plot Tracking:** Query character appearances, relationship maps, and plot thread progress
- **Export Assistance:** Format and prepare manuscripts for submission or publication

## Installation

```json
{
  "mcpServers": {
    "scrivener": {
      "command": "npx",
      "args": ["-y", "@writerslogic/scrivener-mcp"]
    }
  }
}
```

Requires Scrivener 3 installed locally. The MCP server reads from your Scrivener project files directly.

## Use Cases for Operators

1. **Content teams:** Manage long-form content (ebooks, whitepapers, documentation) with AI-assisted editing
2. **Technical writers:** Search large documentation projects semantically, track revision history
3. **Marketing teams:** Analyze brand voice consistency across campaign copy, landing pages, and email sequences
4. **Ghostwriters:** Accelerate manuscript production with AI-assisted research and drafting
5. **Publishing operations:** Streamline editorial workflows from draft to final manuscript

## Integration with CorpusIQ

While Scrivener is primarily a creative/professional writing tool, operators managing content-heavy businesses (newsletters, documentation, educational content) can use this alongside CorpusIQ's business analytics for a complete content operations stack.

## Limitations

- Requires Scrivener 3 (macOS/Windows) — no web version support
- 53 tools is a large surface area; some may be unstable in early releases
- Offline semantic search quality depends on local embedding model
- Not suitable for real-time collaborative editing — single-user project model

## Verdict

MEDIUM-HIGH VALUE for content-heavy operators. At 33 stars with a comprehensive 53-tool surface, this is a serious effort. The offline semantic search alone justifies evaluation for teams managing large document libraries. Not relevant for ecommerce or SaaS analytics operators, but valuable for publishing, education, and content marketing teams.

---

*Discovered: July 14, 2026 via mcp.so. Guide by CorpusIQ MCP Discovery Engine.*
