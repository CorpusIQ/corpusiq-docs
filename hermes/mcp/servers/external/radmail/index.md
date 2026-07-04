---
title: RadMail MCP Integration Guide
description: Full setup guide for RadMail — the email operating system for AI agents with inbox search, commitment tracking, and reviewable draft replies
---

# RadMail MCP — Integration Guide

**The email operating system for AI agents.** RadMail searches your real inbox, surfaces a "Right Now" lane, tracks commitments, and drafts reviewable replies — all through MCP. No tool can auto-send money, change banking, or make irreversible decisions without human approval.

> **Source:** mcp.so · **Last seen:** July 4, 2026 Feed

## What It Does

RadMail turns your email inbox into an MCP-accessible data source with agent-native controls. Unlike basic email MCP servers that just read/write, RadMail adds intelligence layers:

1. **Smart Inbox Search** — Search by sender, subject, content with relevance ranking
2. **"Right Now" Lane** — AI-prioritized view of emails needing immediate attention
3. **Commitment Tracking** — Detects promises, deadlines, and action items from email threads
4. **Draft Replies** — Generates reviewable draft responses (never auto-sends)
5. **Safety Gating** — Financial actions, banking, and irreversible operations require explicit human approval

## Key Capabilities

- **Search** — Ranked inbox search by sender, subject, content, date range
- **Prioritization** — AI-curated "Right Now" lane for urgent/important emails
- **Commitment Extraction** — Automatically detects and tracks commitments and deadlines
- **Draft Generation** — Creates reviewable reply drafts with context from thread history
- **Safety Guardrails** — Blocks auto-send for financial/banking/irreversible actions

## Installation

```bash
# Contact radmail-ai for access (not yet on npm)
# Expected install command (verify with official docs):
npx -y radmail-mcp
```

## Hermes / Claude Desktop Configuration

```json
{
  "mcpServers": {
    "radmail": {
      "command": "npx",
      "args": ["-y", "radmail-mcp"],
      "env": {
        "RADMAIL_EMAIL": "you@example.com",
        "RADMAIL_TOKEN": "your-auth-token"
      }
    }
  }
}
```

## CorpusIQ Use Cases

### 1. Morning Email Triage
```
"Show me my Right Now lane and summarize any new commitments or 
deadlines from overnight emails."
```
The agent surfaces urgent emails, extracts commitments, and presents a prioritized action list.

### 2. Client Follow-Up
```
"Find all emails from Acme Corp in the last 2 weeks. Did I promise 
anything I haven't delivered? Draft follow-ups for each open thread."
```
Searches sender history, cross-references commitments, drafts replies.

### 3. Weekly Digest
```
"Summarize all unresolved email threads from this week, grouped by 
sender, with action items I haven't completed."
```
Generates a weekly accountability report from inbox data.

## Operator Value

| Use Case | Time Saved | Safety Benefit |
|----------|-----------|----------------|
| Morning triage | 20-30 min/day | Never misses urgent items |
| Commitment tracking | Eliminates forgotten promises | All deadlines surfaced |
| Draft replies | 5-10 min per email | Human reviews before sending |

## Prerequisites

- Email account with IMAP/OAuth access
- RadMail authentication token
- MCP client (Claude Desktop, Cursor, Hermes)

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Can't connect to inbox | Verify email credentials and IMAP/OAuth setup |
| Search returns no results | Check date range and search terms; ensure inbox is accessible |
| Drafts look generic | Provide more context in prompts; specify tone and key points |

## Safety Note

RadMail's core design principle: **no irreversible action without human approval.** The agent can read, search, and draft — but sending, financial transactions, and account changes require explicit human confirmation. This makes it safe for production business use.

## Related Resources

- [External MCP Server Catalog](/hermes/mcp/servers/external/) — full curated catalog
- [CorpusIQ MCP Connectors](/hermes/mcp/connectors/) — 37+ native business data connectors
- [PortEden Secure Email](/hermes/mcp/servers/external/#secure-email-gmail--outlook) — alternative email firewall approach

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Servers Home](/hermes/mcp/servers/) →*

*Guide created July 4, 2026. RadMail is currently available via mcp.so. Check official channels for latest access and pricing.*
