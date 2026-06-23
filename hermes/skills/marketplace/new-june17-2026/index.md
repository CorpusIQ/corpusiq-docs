---
title: New Skills  --  June 17, 2026 (nousresearch/hermes-agent expansion)
description: 6 new Hermes Agent skills discovered June 17, 2026 from nousresearch/hermes-agent  --  native MCP client, office document generation, DuckDuckGo search, meme generation, vLLM serving, and Excel authoring.
---

# New Skills  --  June 17, 2026

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) via [skills.sh](https://skills.sh/nousresearch/hermes-agent)
**Date:** June 17, 2026
**Total new:** 6 skills

## Skills Discovered

| # | Skill | Installs | Description |
|---|-------|----------|-------------|
| 1 | `native-mcp` | 79 | MCP client: connect servers, register tools (stdio/HTTP) |
| 2 | `pptx-author` | 14 | Build PowerPoint decks headless with python-pptx  --  for pitch decks |
| 3 | `duckduckgo-search` | 14 | Free web search via DuckDuckGo  --  text, news, images, videos. No API key needed |
| 4 | `meme-generation` | 13 | Generate meme images by picking templates and overlaying text with Pillow |
| 5 | `serving-llms-vllm` | 13 | vLLM: high-throughput LLM serving with OpenAI API compatibility |
| 6 | `excel-author` | 13 | Build Excel workbooks headless with openpyxl  --  formulas, named ranges, audits |

## Detailed Skill Descriptions

### 1. native-mcp (79 installs)  --  MCP Client ⭐ TOP PICK
Connects to MCP servers over stdio and HTTP transports, registers tools, and manages server lifecycle. Core infrastructure skill  --  enables Hermes agents to connect to any MCP-compatible server. This is the foundational skill that underpins the entire MCP ecosystem integration within Hermes Agent.

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill native-mcp
```

**Key capabilities:**
- Connect to MCP servers over stdio (subprocess) and HTTP
- Auto-discover tools from connected servers
- Manage server lifecycle (start, stop, reconnect)
- Register tools from multiple servers simultaneously
- Handle server disconnects and reconnection gracefully

### 2. pptx-author (14 installs)  --  PowerPoint Generation
Build PowerPoint decks programmatically with python-pptx. Works with excel-author for data-backed presentations where every number traces to a workbook cell.

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill pptx-author
```

**Use cases:** Pitch decks, quarterly reports, training materials, data presentations.

### 3. duckduckgo-search (14 installs)  --  Free Web Search
Privacy-focused web search via DuckDuckGo  --  text, news, images, videos. No API key or billing required. Falls back to the `ddgs` CLI when installed; uses the Python DDGS library otherwise.

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill duckduckgo-search
```

**Use cases:** Backup search provider, privacy-sensitive research, zero-cost search.

### 4. meme-generation (13 installs)  --  Meme Image Creation
Generate meme images by selecting templates and overlaying text with Pillow. Produces actual .png meme files suitable for social media posting.

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill meme-generation
```

**Use cases:** Social media engagement, community interaction, visual content.

### 5. serving-llms-vllm (13 installs)  --  vLLM Serving
High-throughput LLM serving with vLLM. OpenAI API-compatible interface with support for AWQ/GPTQ quantization. For serving local models with production-grade throughput.

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill serving-llms-vllm
```

**Use cases:** Self-hosted model serving, cost optimization, high-throughput inference.

### 6. excel-author (13 installs)  --  Excel Workbook Generation
Build auditable Excel workbooks with openpyxl  --  blue/black/green cell conventions, formulas instead of hardcoded values, named ranges, balance checks, and sensitivity tables.

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill excel-author
```

**Use cases:** Financial models, data exports, audit-ready spreadsheets.

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace Home](/hermes/skills/marketplace/) →*
*↑ [New June 2026](/hermes/skills/marketplace/new-june-2026/) | [June 13 Update 3](/hermes/skills/marketplace/new-june13-2026-update3/) →*
*Powered by CorpusIQ*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
