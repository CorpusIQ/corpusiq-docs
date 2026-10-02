---
title: "imap-mcp - Read-Only IMAP Mailbox Operations for Agents"
description: "IMAP mailbox access for agents with a deliberate no-send design: list folders, search and read messages with BODY.PEEK so unread state is preserved, track seen state, save attachments and store draft replies in your own Drafts folder. Messages arrive nonce-fenced with SPF/DKIM/DMARC verdicts and prompt-injection-shape flags. stdio via npx @ni-c/imap-mcp, MIT."
category: Communication & Email
stars: "n/a (new listing, ni-c/imap-mcp)"
added: 2026-08-30
source: "mcp.so GitHub issue #3843"
relevance: ★★
tags: [mcp-server, email, imap, inbox, triage, security, stdio, npm]
---

# imap-mcp

**IMAP mailbox operations for agents, with a deliberate no-send design.** imap-mcp exposes any IMAP mailbox to an MCP client: list folders, search and read messages, track what the assistant has already seen, save attachments and draft replies. It speaks IMAP rather than one vendor's API, so it works with whatever provider you already have. The headline security posture: it deliberately cannot send mail, and it reads with BODY.PEEK so your own unread state is never touched.

```
Server type: Local (stdio via npx, or ghcr.io/ni-c/imap-mcp container)
Auth: IMAP credentials (host, port, user, password or app password)
Protocol: IMAP (any provider - Gmail, Fastmail, iCloud, Zoho, self-hosted Dovecot)
Tools: 11 (curated 6 with IMAP_ALLOW_TOOLS=essential)
Writes: off unless IMAP_READ_ONLY=false; deletes need human confirmation
Registry: io.github.ni-c/imap-mcp v0.2.0 (official MCP registry)
Pricing: Free (open source)
License: MIT · Repo: github.com/ni-c/imap-mcp (created Aug 26, 2026)
Built by: ni-c (also ships healthchecks-mcp, google-search-console-mcp and wikijs-mcp)
```

```json
{
  "mcpServers": {
    "imap": {
      "command": "npx",
      "args": ["-y", "@ni-c/imap-mcp"],
      "env": {
        "IMAP_HOST": "imap.example.com",
        "IMAP_PORT": "993",
        "IMAP_USER": "you@example.com",
        "IMAP_PASSWORD": "your app password"
      }
    }
  }
}
```

## Why This Matters for Operators

Email is where most operational decisions still land, and giving an agent inbox access is usually dangerous. imap-mcp's design answers the three objections operators actually have.

First, **no outbound channel.** Private data plus untrusted content plus an outbound channel is what makes an agent exploitable by indirect prompt injection, and this server does without the third. `save_draft` stores the reply in your Drafts folder for you to send from your own client - the agent proposes, a person disposes.

Second, **verdicts arrive with the message.** Each message comes with SPF/DKIM/DMARC verdicts, matching prompt-injection shapes and mixed-script word flags, and message bodies arrive fenced between markers carrying a per-call random nonce. Markdown image syntax is defused so a rendering client cannot be induced to fetch a tracking URL.

Third, **your unread state is sacred.** Reads use BODY.PEEK so the agent never marks your mail as read behind your back; the server tracks what the agent has already seen through its own IMAP keyword instead of your flags.

## Tool Groups (11 tools, 6 in essential mode)

- **Folders:** list folders (and create when writes are enabled)
- **Search and read:** search messages, read message bodies (fenced with nonce markers)
- **Seen tracking:** the server's own IMAP keyword tracks what the agent already processed
- **Attachments:** save attachments to disk
- **Drafts:** `save_draft` writes replies into your Drafts folder - nothing is ever sent
- **Safety:** `IMAP_READ_ONLY=false` to enable mailbox writes; deleting asks a human through MCP elicitation where the client supports it; `IMAP_ALLOW_TOOLS=essential` registers a curated six

Exact tool names are enumerated in the repo README; the capability groups above follow the submission's description.

## Verification (Aug 30, 2026)

- npm registry: @ni-c/imap-mcp v0.2.0 published Aug 30, 2026, with provenance
- Official MCP registry: io.github.ni-c/imap-mcp listed at v0.2.0 ("IMAP mailbox")
- GitHub repo live (MIT, created Aug 26, 2026)
- Author's sibling servers (healthchecks-mcp, google-search-console-mcp, wikijs-mcp) already verified in this catalog

## Notes and Caveats

- stdio only: no hosted remote endpoint
- Cannot send, by design: pair it with a separate send-side server (or a person) when outbound is needed
- Brand new listing (repo created Aug 26, 2026, zero stars): early-adopter tooling
- Registry namespace is crowded: Digilac/simap-mcp and Temple-of-Epiphany/imap-mcp-pro are different servers from other vendors and are not catalogued here
- Write mode is off by default: set IMAP_READ_ONLY=false consciously, and prefer the essential tool set for anything exposed to untrusted content

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [BusyMail MCP - Human-Approval Email over MCP](/hermes/mcp/servers/external/busymail-mcp)
- [MCP Email Server - IMAP/SMTP Email for AI Agents](/hermes/mcp/servers/external/mcp-email-server)
- [healthchecks-mcp - Cron Job Health and Failure Forensics for Agents](/hermes/mcp/servers/external/healthchecks-mcp)
