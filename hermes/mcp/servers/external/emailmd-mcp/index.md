---
title: "emailmd MCP Server - CorpusIQ Docs"
description: "Setup and usage guide for emailmd MCP Server. Part of the Hermes resource directory. URL: https://github.com/anypost/emailmd."
last_updated: 2026-08-12
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/emailmd-mcp/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# emailmd MCP Server

**URL:** https://github.com/anypost/emailmd
**mcpservers.org:** https://mcpservers.org/servers/anypost/emailmd
**Category:** Communication / Email
**Priority:** HIGH

## What It Does for Operators

emailmd lets your AI agent write and preview emails. It renders markdown into email-safe HTML that holds up in Outlook and Gmail, lints drafts for deliverability problems, and returns a live preview link. No more broken formatting or spam-triggering markup when your agent drafts emails for you.

## Installation

```bash
npx emailmd mcp
```

Or use the hosted server (no API key required).

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "emailmd": {
      "command": "npx",
      "args": ["emailmd", "mcp"]
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `render_email` | Convert markdown to email-safe HTML |
| `lint_email` | Check draft for deliverability issues |
| `preview_email` | Generate live preview link |
| `send_email` | Send via configured SMTP |

## Operator Use Cases

1. **Automated client communications** — agent drafts professional emails from bullet points
2. **Newsletter preview** — verify rendering in Outlook/Gmail before sending
3. **Deliverability checking** — catch spam triggers before hitting send
4. **Template management** — maintain markdown email templates, render on demand
5. **Multi-format testing** — verify email appearance across clients

## CorpusIQ Angle

emailmd complements CorpusIQ's business communication workflows. Operators who use AI agents to manage client communications can ensure professional, deliverable emails without manual HTML editing. The markdown-first approach aligns with agent-native workflows.

## Limitations

- Requires SMTP configuration for sending
- Preview quality depends on email client rendering engines
- New project (added July 2026), ecosystem still maturing

---
**Discovered:** July 24, 2026 via awesome-mcp-servers PR #10685
**Repo:** anypost/emailmd
