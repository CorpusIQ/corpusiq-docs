---
title: "BusyMail MCP - CorpusIQ Docs"
description: Human-approval email over MCP — read, organize, and send from your existing IMAP accounts, with nothing sent until you approve it
category: Productivity
stars: n/a (new listing)
added: 2026-08-13
source: mcpservers.org
relevance: ★★
tags: [email, imap, approvals, human-gate, productivity, remote-mcp]
---

# BusyMail MCP

**Remote MCP server (Streamable HTTP or local script, token auth) from BusyMail.** An email client for the IMAP accounts you already have, exposed over MCP — the assistant reads, searches, tidies, and writes replies, and every outbound message sits in an Approvals queue until you approve or reject it. It is not a mailbox you move to: your accounts stay where they are.

```
Server type: Remote (Streamable HTTP) or local Node script
Auth: Bearer token with per-token permissions (read / organize / send)
Endpoint: https://busymail.app/mcp
Tools: Read + search + summarize, organize (archive, unarchive, pin), send (queued for approval)
Pricing: Invite-only during rollout
Category: Email / Productivity
Built by: BusyMail (busymail.app)
```

## Why This Matters for Operators

Email assistants have existed for years; the failure mode has always been the same — the assistant sends, and you find out later. BusyMail's design answer is absolute: **a token can never send mail.** It can only queue. Approval happens while you are signed in, so the token that wrote a message can never approve it. That separation — writer and approver can never be the same session — is the strongest email-safety architecture yet observed in an MCP server.

**Scoped tokens make delegation safe.** You pick read, organize, or send per token; no token can touch settings, passwords, two-factor, or account management. Revoke one token without affecting the others.

## Tools & Capabilities

| Capability | What the assistant can do |
|---|---|
| Read | Message content, summaries, search, sent mail — every token has this |
| Organize | Archive, unarchive, pin — real moves on your mail server, visible in every other client |
| Send | Queue mail for your approval; also reads everything already queued on the account |

File attachments via the local script path never pass through the AI client — the script reads the file from disk and sends it on.

## Installation

```bash
claude mcp add busymail --transport http https://busymail.app/mcp --header "Authorization: Bearer YOUR_TOKEN"
```

Clients that can run a local script (Node + curl + POSIX shell) get the full experience including path-based attachments; the script is fetched fresh each start, so it always matches BusyMail and nothing is cached.

## Configuration

```json
{
  "mcpServers": {
    "busymail": {
      "type": "http",
      "url": "https://busymail.app/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_TOKEN"
      }
    }
  }
}
```

Tokens are created under Settings → MCP. An account is required, and BusyMail is invite-only right now.

## Business Relevance

- **Founders and operators** get an inbox assistant that physically cannot send without them — the first safe delegation.
- **Executive assistants (human or agentic)** triage and draft in bulk, with the principal approving only what matters.
- **Teams on shared inboxes** scope tokens so different agents get read-only vs organize vs send.

## Integration with CorpusIQ

BusyMail and CorpusIQ occupy different halves of the email problem and compose cleanly. CorpusIQ's Gmail connectors (Google Workspace) are the business data layer — business inbox monitoring, the metrics, the CRM writes. BusyMail is the operator's personal execution layer with the approval gate. An operator can run both: CorpusIQ watches the business inboxes and feeds leads into HubSpot or Close, while BusyMail gives the same operator an approval-gated assistant over personal IMAP mail. Two different trust models, one clear boundary.

## Limitations

- Invite-only during rollout — not open to signup yet
- Attachments via remote HTTP are limited to base64-encoded payloads, well below what BusyMail accepts locally
- No settings, password, 2FA, or account management over MCP (by design)
- Low-volume inboxes gain less — the approval queue is for volume triage

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
