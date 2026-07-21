---
title: "Mermail — Privacy-First Email Inboxes for AI Agents"
description: "Privacy-first email inboxes built for AI agents. Read, search, draft, send, and triage mail over Streamable HTTP MCP. Give your AI agent its own email address."
source: docs.mermail.app
stars: 0
language: N/A (Hosted)
transport: Streamable HTTP
auth: API Key
category: Communication & Email
last_updated: 2026-07-21
---

# Mermail — Privacy-First Email Inboxes for AI Agents

**Email inboxes purpose-built for AI agents.** Mermail gives AI agents their own email address with full read, search, draft, send, and triage capabilities through MCP. Privacy-first: data is encrypted and not used for training.

## What It Does for Operators

- **Agent email addresses** — Give your AI agent its own inbox (e.g., agent@yourcompany.mermail.app)
- **Full email MCP** — Read, search, draft, send, and triage emails through MCP tools
- **Privacy-first** — Encrypted storage, no training on your email data
- **Streamable HTTP** — Remote endpoint, no local mail server needed
- **Triage tools** — AI agents can categorize, prioritize, and draft responses

## Installation

```bash
# No installation — hosted platform
# Sign up at mermail.app, create agent inboxes
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "mermail": {
      "type": "url",
      "url": "https://docs.mermail.app/ai/mcp"
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `read_mail` | Read emails from agent inbox |
| `search_mail` | Search emails by sender, subject, content |
| `draft_reply` | Draft an email reply |
| `send_mail` | Send an email from agent address |
| `triage_inbox` | Categorize and prioritize incoming mail |
| `manage_folders` | Organize emails into folders/labels |

*Note: Tool names are approximate. Full documentation at docs.mermail.app.*

## Operator Use Cases

1. **Customer Support** — Give AI agents their own support inbox. Agent triages, drafts responses, escalates complex issues.
2. **Lead Qualification** — Route inbound leads to AI agent inbox. Agent researches, scores, and drafts responses.
3. **Newsletter Management** — AI agent monitors newsletter subscriptions and reader replies.
4. **Vendor Communications** — Dedicated agent inbox for vendor invoice follow-ups and order confirmations.

## CorpusIQ Angle

Mermail is the cleanest email MCP for operators who want to isolate AI agent email from their primary inbox. While CorpusIQ connects to Gmail for business communications, Mermail provides a separate, agent-native email layer. Use CorpusIQ for human email + Mermail for agent-originated email workflows.

## Limitations

- Separate email addresses (not your existing Gmail/Outlook)
- New platform — deliverability and spam filtering TBD
- API key auth only (no OAuth for individual users)
- Pricing not publicly documented as of July 2026
