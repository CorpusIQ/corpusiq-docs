---
title: byakugan MCP Server
description: "Setup and usage guide for byakugan MCP Server. Part of the Hermes resource directory."
last_updated: 2026-08-12
---

# byakugan MCP Server

**URL:** https://github.com/JayOfemi/byakugan
**mcpservers.org:** N/A (pending)
**Category:** Productivity / AI Text Analysis
**Priority:** MEDIUM

## What It Does for Operators

Private, local AI-text analysis for the AI you already use. Runs detection of AI-generated text, identifies exact AI-tell spans, checks for content reuse, and performs grammar analysis — all locally. No data leaves your machine.

## Installation

```bash
npx byakugan
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "byakugan": {
      "command": "npx",
      "args": ["byakugan"]
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `detect_ai_text` | Identify AI-generated content spans |
| `check_reuse` | Cross-reference for content reuse |
| `grammar_pass` | Grammar and style analysis |
| `analyze_document` | Full document analysis pass |

## Operator Use Cases

1. **Content verification** — verify vendor/partner content authenticity
2. **Quality assurance** — grammar and style checking for outgoing communications
3. **Plagiarism detection** — check content reuse across team submissions
4. **AI policy compliance** — ensure content meets human-authored standards
5. **Due diligence** — verify prospect/client communications

## CorpusIQ Angle

For operators who need to verify content authenticity in business communications. The local-only approach means sensitive business documents never leave your infrastructure. Complements CorpusIQ's content generation with verification capabilities.

## Limitations

- Local-only (no cloud option)
- New project (July 2026)
- Detection accuracy varies by AI model

---
**Discovered:** July 24, 2026 via awesome-mcp-servers PR #10871
**Repo:** JayOfemi/byakugan
