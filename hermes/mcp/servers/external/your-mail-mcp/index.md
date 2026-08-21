---
title: "your-mail-mcp - Self-Hosted Read-Only IMAP Email for MCP Clients"
description: "Self-hosted MCP server that gives AI clients read-only access to IMAP mail (Gmail, iCloud, any provider) through a one-way mbsync mirror indexed by notmuch. Ten read-only tools: search, ids, files, count, show, thread, text, folders, refresh and attachment, with junk and trash excluded by default, prompt-injection markers on all mail text, and OAuth 2.0 with Dynamic Client Registration. Docker image or static Go binaries; no write path to any account."
category: Communication & Email
stars: n/a (new listing)
added: 2026-08-21
source: "mcp.so GitHub issue #3669"
relevance: ★★
tags: [email, imap, self-hosted, read-only, notmuch, oauth, docker, inbox, triage, privacy]
---

# your-mail-mcp

**Read-only IMAP email for MCP clients, self-hosted, with no write path back to any account.** your-mail-mcp mirrors one or more IMAP accounts into a local maildir with mbsync, indexes the mirror with notmuch, and serves search, threading and attachment reads to Claude, ChatGPT or any streamable-HTTP MCP client through an OAuth gate. Sending, deleting, moving and tagging do not exist in the process, which makes always-on agents and scheduled digests safe to leave running over a mailbox.

```
Server type: Self-hosted (Streamable HTTP)
Endpoint: http://localhost:8080/mcp (or your public URL behind a tunnel)
Auth: OAuth 2.0 with Dynamic Client Registration
Tools: 10, all read-only
Stack: Docker image (linux/amd64 + arm64) or static Go binaries, mbsync + notmuch
Built by: wildsurfer (github.com/wildsurfer/your-mail-mcp)
```

## Why This Matters for Operators

Mail is where the answers live: booking references, invoices, warranty periods, promises made in writing. An operator who needs "what did the accountant say about VAT and when" or "collect everything between me and the builder about the roof, in order" normally spends twenty minutes across search UIs. your-mail-mcp turns that into one agent question over the full history, every account in one index, junk and trash excluded by default.

The read-only architecture is the point, not a limitation. The mbsync configuration for every account carries `Sync Pull`, `Create Near`, `Remove None`, `Expunge None`, and the only IMAP operation in the Go code is a single `LIST` at startup to discover junk and trash folder names. A malicious email that reaches the assistant gets read and nothing more.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `search` | Search mail, returns thread summaries as JSON |
| `ids` | Return message ids matching a query |
| `files` | Return maildir file paths matching a query |
| `count` | Count messages matching a query |
| `show` | Show one message: headers and decoded body as JSON |
| `thread` | Show the whole thread containing a message |
| `text` | Return the plain-text body of one message, converting HTML |
| `folders` | List accounts, folders, index tags, last sync and last error |
| `refresh` | Sync INBOX now and report how many messages arrived |
| `attachment` | One attachment or MIME part by part number; over 5MB gets a signed download link |

`search`, `ids`, `files` and `count` take notmuch queries (`from:`, `to:`, `subject:`, `tag:`, `folder:`, date ranges, combined with and/or/not), an optional `account` scope, and `include_excluded` to bring junk and trash back in. Multi-account setups work with any folder structure and language via RFC 6154 SPECIAL-USE discovery.

## Installation

Setup is two files (an accounts list and an env file) plus Docker Compose. Three deployment modes, in order of reach: (1) local machine only, `PUBLIC_URL=http://127.0.0.1:8080`; (2) your machine reachable from anywhere via Tailscale Funnel or Cloudflare Tunnel; (3) a VPS with a public hostname. Once up, connect any client:

```json
{
  "mcpServers": {
    "your-mail": {
      "url": "http://127.0.0.1:8080/mcp"
    }
  }
}
```

Claude and ChatGPT connect through OAuth 2.0 with Dynamic Client Registration and a passphrase consent step. For clients with broken OAuth support, the README documents an `mcp-remote` fallback that performs the dance and re-exposes the server over stdio.

## Configuration

Each account gets a generated mbsync config; environment variables control `PUBLIC_URL`, sync interval, attachment size cap (5MB) and account credentials. Every byte of mail text is wrapped in untrusted-content markers to resist prompt injection, and oversized attachments are served through short-lived signed links instead of inline. The server logs no message bodies, and the accounts file lives alongside the server, not in any client.

## Business Relevance

- **Executives and founders** triage "what actually needs me" across all inboxes in one query
- **Customer-facing operators** pull the client's requirements out of the thread and into the working session without retyping
- **Finance and legal** retrieve contractual wording and dated answers with the source message attached
- **Teams running always-on agents** get email context without ever granting send, delete or move

## Integration with CorpusIQ

CorpusIQ's 40+ connectors cover the structured business layer: books, ads, CRM, analytics. your-mail-mcp covers the unstructured layer at the edge: the client's exact words, the vendor's written promise, the dated reply. A CorpusIQ-driven workflow can hold the numbers (Stripe, QuickBooks, GA4) while your-mail-mcp holds the correspondence that explains them, both inside the same agent session.

## Limitations

- Self-hosted: requires Docker (or Go binaries), mbsync and notmuch; no hosted option
- Read-only by design: no send, no delete, no move, no tag, no draft handling
- Mail lives on disk where you deploy it; mode 3 (VPS) puts it on rented storage
- New listing (Aug 2026), zero public stars, single-maintainer project
- Bearer-token and OAuth surface must be placed behind the tunnel config, not exposed raw

## See Also

- [BusyMail MCP - Email Operations for Agents](/hermes/mcp/servers/external/busymail-mcp/)
- [Radmail - Email Insights for Founders](/hermes/mcp/servers/external/radmail/)
- [MisarMail MCP - Transactional Email from MCP Clients](/hermes/mcp/servers/external/misarmail-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
