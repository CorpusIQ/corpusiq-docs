---
title: "MCP Email Server — IMAP/SMTP Email for AI Agents"
description: "Integration guide for ai-zerolab/mcp-email-server. IMAP and SMTP email access via MCP for Hermes Agent. Send/receive emails from AI agents."
category: mcp
tags: [mcp-server, email, imap, smtp, hermes-agent, integration]
last_updated: 2026-07-15
mcp_server: ai-zerolab/mcp-email-server
stars: 281
source: mcpservers.org
---

# MCP Email Server — IMAP/SMTP Email for AI Agents

**Repository:** [ai-zerolab/mcp-email-server](https://github.com/ai-zerolab/mcp-email-server)
**Stars:** 281 ★
**Category:** Communication / Email
**License:** MIT
**Last Updated:** 2026-07-14

## What It Does

Provides IMAP and SMTP access for AI agents via MCP. Agents can read, search, and send emails through standard email protocols — no API wrappers needed. Works with any email provider that supports IMAP/SMTP (Gmail, Outlook, Fastmail, ProtonMail Bridge, self-hosted).

### Tools Provided

| Tool | Description |
|------|-------------|
| `send_email` | Send email via SMTP with to, subject, body, cc, bcc |
| `search_emails` | Search IMAP inbox by sender, subject, date range, body |
| `read_email` | Read full email content by UID |
| `list_mailboxes` | List available IMAP folders/labels |
| `move_email` | Move email between folders |
| `delete_email` | Delete email by UID |
| `mark_read` / `mark_unread` | Flag management |

## Comparison: CorpusIQ Email Connector vs MCP Email Server

| Feature | CorpusIQ Email Connector | MCP Email Server |
|---------|--------------------------|------------------|
| **Protocol** | Gmail API / Outlook Graph API | IMAP + SMTP (universal) |
| **Auth** | OAuth (simpler setup) | App passwords / credentials |
| **Provider coverage** | Gmail + Outlook only | ANY IMAP/SMTP provider |
| **Search** | Gmail search syntax (powerful) | Basic IMAP SEARCH |
| **Attachments** | Full attachment handling | Limited (MIME raw) |
| **Setup complexity** | 1 OAuth click | Configure host/port/creds |
| **Best for** | Gmail/Outlook users, simplicity | Multi-provider, self-hosted, privacy |

**Verdict:** MCP Email Server is complementary, not competitive. Use it for non-Gmail/Outlook providers (Fastmail, ProtonMail, self-hosted). CorpusIQ email connector remains superior for Gmail/Outlook workflows.

## Setup for Hermes Agent

### Prerequisites

- Email account with IMAP/SMTP access enabled
- App-specific password (Gmail) or regular credentials (other providers)
- Node.js 18+

### Step 1: Clone and Install

```bash
cd ~/mcp-servers
git clone https://github.com/ai-zerolab/mcp-email-server.git
cd mcp-email-server
npm install
npm run build
```

### Step 2: Configure Credentials

Create a `.env` file:

```env
IMAP_HOST=imap.gmail.com
IMAP_PORT=993
IMAP_USER=your-email@gmail.com
IMAP_PASSWORD=your-app-password
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

**Gmail notes:** Enable IMAP in Gmail settings + generate an [App Password](https://myaccount.google.com/apppasswords) (requires 2FA enabled).

### Step 3: Register with Hermes

```bash
hermes mcp add email -- node ~/mcp-servers/mcp-email-server/dist/index.js
```

Or via `~/.hermes/config.yaml`:

```yaml
mcp_servers:
  email:
    command: node
    args:
      - /home/hermes/mcp-servers/mcp-email-server/dist/index.js
    env:
      IMAP_HOST: imap.gmail.com
      IMAP_PORT: "993"
      IMAP_USER: your-email@gmail.com
      IMAP_PASSWORD: your-app-password
      SMTP_HOST: smtp.gmail.com
      SMTP_PORT: "587"
      SMTP_USER: your-email@gmail.com
      SMTP_PASSWORD: your-app-password
```

### Step 4: Verify

```bash
hermes mcp list
# Should show: email (ai-zerolab/mcp-email-server) — CONNECTED
```

## Use Cases

1. **Unified inbox search:** Query multiple email accounts across providers through one MCP interface
2. **Automated email triage:** Agent scans inbox, categorizes, and drafts responses
3. **Self-hosted email integration:** Connect self-hosted mail servers (Dovecot, iRedMail) to AI agents
4. **Privacy-first email:** Bypass Gmail API tracking — read email over standard IMAP
5. **Email migration scripts:** Move emails between accounts/providers via agent orchestration

## Security Considerations

- Store credentials in environment variables, never in config files
- Use app-specific passwords, not account master passwords
- IMAP/SMTP credentials provide full email access — scope carefully
- Consider a dedicated email account for agent use rather than personal inbox
- Gmail users: app passwords require 2FA (good for security)
- The MCP server runs locally — credentials never leave your machine

## Limitations

- No OAuth support — credentials-based auth only
- Limited attachment handling (raw MIME only)
- IMAP SEARCH syntax is less powerful than Gmail's search operators
- No push notifications — polling-based inbox monitoring
- Single account per server instance (run multiple instances for multiple accounts)

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `Authentication failed` | Verify app password, check IMAP is enabled in provider settings |
| `Connection refused` | Check IMAP/SMTP port numbers; some providers use non-standard ports |
| `Command timeout` | Increase `IMAP_TIMEOUT` env var; Gmail IMAP can be slow on large inboxes |
| `Certificate error` | Set `NODE_TLS_REJECT_UNAUTHORIZED=0` for self-signed certs (not recommended for production) |

## Related Guides

- [CorpusIQ Email Connector](/hermes/mcp/connectors/email/) — OAuth-based Gmail/Outlook
- [Google Search Console MCP](/hermes/mcp/servers/external/google-search-console-mcp/) — SEO analytics via MCP
- [ComparEdge LLM Cost MCP](/hermes/mcp/servers/external/comparedge-llm-cost-mcp/) — Token cost intelligence
