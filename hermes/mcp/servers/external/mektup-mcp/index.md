---
title: "Mektup MCP - CorpusIQ Docs - CorpusIQ Docs"
description: Email infrastructure over MCP — register domains, create mailboxes, send and receive mail, and manage threads, drafts and folders through 41 agent tools. A real mailbox for AI agents, not a one-way sending API.
category: Communication & Email
stars: n/a (new listing)
added: 2026-08-16
source: mcp.so
relevance: ★★★
tags: [email, mailbox, communication, oauth, domain-registration, ai-agents]
---

# Mektup MCP

**Remote email-infrastructure server (Streamable HTTP, Bearer token)** — Mektup gives AI agents and their humans a real email mailbox instead of a one-way sending API. Through 41 MCP tools an agent can register a domain, create a mailbox, send and receive mail, and manage threads, drafts, and folders. MIT, built by WeeCi (`github.com/WeeCi/mektup-mcp`), with signup and dashboard at usemektup.com.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer API token (mek_live_...)
Endpoint: https://mcp.usemektup.com/mcp
Tools: 41 tools (domains, mailboxes, send/receive, threads, drafts, folders)
Pricing: Commercial — sign up at usemektup.com
Category: Communication & Email
Built by: github.com/WeeCi/mektup-mcp
```

## Why This Matters for Operators

Email for agents has mostly meant transactional send APIs — fire a message, never receive anything back. Mektup closes the loop: an agent can own a mailbox, receive inbound mail, and work it the way a human assistant would, from drafting replies to filing threads. For operators, that turns agent workflows from "the agent emails me a report" into "the agent runs the inbox" — domain registration included, so a side project or client workstream can get its own mail presence without a human provisioning step.

The safety profile matters too: the Bearer token gates the API, and mailbox operations stay inside one vendor account with a dashboard for review, so the human keeps visibility over what the agent sent and received.

## Tools & Capabilities

The 41 tools group into five surfaces:

| Area | Capability |
|---|---|
| Domains | Register and configure domains for agent mailboxes |
| Mailboxes | Create mailboxes, manage addresses and settings |
| Send & Receive | Send mail, fetch inbound messages |
| Threads | Manage conversation threads and replies |
| Drafts & Folders | Draft management, folder organization |

## Installation

```json
{
  "mcpServers": {
    "mektup": {
      "url": "https://mcp.usemektup.com/mcp",
      "headers": {
        "Authorization": "Bearer mek_live_..."
      }
    }
  }
}
```

Create the token from the usemektup.com dashboard, then add the server to any Streamable-HTTP-capable client (Claude, Cursor, Codex, or a custom agent runtime).

## Business Relevance

- **Client service desks** can let an agent triage a shared inbox and draft replies for human approval
- **Automated workflows** gain a receive path — confirmations, bounce handling, and inbound triggers become agent-addressable
- **New projects** get domain plus mailbox provisioned in one conversation instead of an admin ticket
- **Agent teams** get per-role mailboxes with a single vendor dashboard for oversight

## Integration with CorpusIQ

Mektup sits alongside CorpusIQ's email connectors as the inbound-capable complement: CorpusIQ covers Gmail/Outlook reading for existing human inboxes, while Mektup provisions agent-owned mail infrastructure. An operator can pair them — CorpusIQ watches the primary business inbox, and a Mektup mailbox handles agent-driven campaigns or client sub-brands, with all credentials held in the same secret store and rotated centrally.

## Limitations

- Commercial service — pricing tiers are not published on the MCP listing; verify before committing
- Brand-new listing (submitted Aug 16, 2026); no community track record yet
- No published per-tool schema in the listing — tool discovery is the source of truth
- Email deliverability still depends on the vendor's infrastructure and domain reputation

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
