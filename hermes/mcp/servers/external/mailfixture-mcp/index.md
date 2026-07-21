---
title: "MailFixture — Email & SMS Testing MCP for Automated QA"
description: "Receive-only email and SMS inboxes for automated testing. Wait-for-OTP and wait-for-link tools let AI agents complete verification flows without human intervention."
source: mailfixture.com
stars: 0
language: N/A (Hosted)
transport: Streamable HTTP
auth: API Key
category: Development & QA
last_updated: 2026-07-21
---

# MailFixture — Email & SMS Testing MCP for Automated QA

**Disposable email and SMS inboxes for AI agent testing.** MailFixture provides receive-only inboxes that AI agents can use to complete email/SMS verification flows during automated testing. Wait-for-OTP and wait-for-link tools eliminate the manual verification step.

## What It Does for Operators

- **Receive-only inboxes** — Temporary email and SMS addresses for testing
- **Wait-for-OTP** — AI agent polls inbox until verification code arrives, then returns it
- **Wait-for-link** — AI agent polls inbox for magic link, then returns it
- **No setup** — Inboxes created on demand through MCP tools
- **Agent-native testing** — Complete end-to-end signup flows without human intervention

## Installation

```bash
# No installation — hosted API
# Sign up at mailfixture.com for API key
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "mailfixture": {
      "type": "url",
      "url": "https://mailfixture.com/docs/mcp"
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `create_inbox` | Generate a disposable email or SMS inbox |
| `wait_for_otp` | Poll inbox until OTP arrives, return the code |
| `wait_for_link` | Poll inbox until magic link arrives, return the URL |
| `get_messages` | List all messages received at inbox |
| `delete_inbox` | Clean up temporary inbox |

*Note: Tool names are approximate. Full documentation at mailfixture.com/docs/mcp.*

## Operator Use Cases

1. **QA Automation** — End-to-end signup flow testing without manual email verification
2. **CI/CD Pipelines** — Automated integration tests that complete OAuth and email verification
3. **Developer Tools** — Test password reset, email confirmation, and 2FA flows programmatically
4. **Agent Development** — Build and test AI agents that interact with email-based workflows

## CorpusIQ Angle

MailFixture solves a key testing pain point for operators building on CorpusIQ: automated end-to-end testing of OAuth and email verification flows. For operators integrating CorpusIQ with their own applications, MailFixture enables CI pipelines that fully test the signup → OAuth → email verification → data access flow.

## Limitations

- Receive-only (cannot send emails)
- Temporary inboxes (not for production use)
- SMS coverage may be limited by country
- Rate limits for free tier
