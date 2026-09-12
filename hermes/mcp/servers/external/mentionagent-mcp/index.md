---
title: "MentionAgent MCP - Publisher Outreach and Backlink Placements for Agents"
description: "Remote MCP server that moves link-building outreach into the agent you already use. Agents triage the reply inbox, read placement threads with stored link terms, draft site-specific placement requests, send approved replies, and mark deals won - with every email read by a human before it goes out."
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-09-11
source: mcpservers.org /all
relevance: ★★★
tags: [outreach, link-building, seo, backlinks, email, remote-mcp]
---

# MentionAgent MCP

**Remote MCP server (Streamable HTTP, bearer key)** - runs your outreach from the agent you already use. MentionAgent manages publisher outreach and backlink placements as agent tools: list threads waiting on a reply, read a thread with its stored link terms (which page of theirs links to you, with what anchor, and which page of yours links back), draft site-specific placement requests, send approved replies, and close placements as won. The agent never learns recipient addresses - `send_reply` has no recipient field, so an email can only ever go back to the person already in the thread.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer key in the Authorization header (created once in the dashboard, shown once)
Endpoint: https://mentionagent.ai/mcp
Tools: 10 documented (get_status, list_inbox, get_thread, draft_reply, send_reply, mark_deal, list_pending_drafts, edit_draft, approve_batch, set_sending)
Pricing: Vendor plans at mentionagent.ai (key from Settings → Agent access)
Category: Sales & Outreach
Built by: MentionAgent
```

## Tools

| Tool | Purpose |
|---|---|
| get_status | Connection check - sites on the account and what the agent can and cannot do |
| list_inbox | Threads filtered by state, e.g. needs_reply |
| get_thread | One thread in full; existing terms return as a stored record (their page, anchor, your page) |
| draft_reply | MentionAgent writes the reply - it crawls the publisher's site, picks the page and the exact paragraph to ask for, and drafts the email around it |
| send_reply | Send one approved reply; no recipient field, the address comes from the thread |
| mark_deal | Close a thread as won - the agreed placement stops reading as pending; sends nothing |
| list_pending_drafts | Drafts waiting for review before a batch goes out |
| edit_draft | Rewrite a draft in plain English (shorter, less formal) |
| approve_batch | Send the reviewed batch |
| set_sending | Pause sending for a site until a date |

Nothing is sent without explicit approval - the workflow is draft, review in chat, approve, and every email lands in the human's chat to read and edit first.

## Connection

1. Create a key in the MentionAgent dashboard under Settings → Agent access (shown once).
2. Claude Code - `claude mcp add --transport http mentionagent https://mentionagent.ai/mcp --header "Authorization: Bearer <your key>"`
3. Any other client - add an HTTP MCP server with the endpoint URL and the `Authorization: Bearer <your key>` header.
4. Call `get_status` with no arguments to confirm the connection and see the sites on the account.
5. A packaged Claude SEO skill (the server as a Claude Code plugin) is published at mentionagent.ai/claude-seo-skill.

## Verification (Sep 11, 2026 evening sweep)

Endpoint live-probed over JSON-RPC: anonymous initialize returned `{"error":"invalid_token","error_description":"Missing Authorization header"}` - live and auth-gated exactly as documented. The mcpservers.org listing carries the full workflow walkthrough (a real session: list_inbox → get_thread → draft_reply → send_reply → mark_deal) and the one-click Claude connector uses OAuth, which the vendor notes it does not yet support - bearer header is the supported path.

## See Also

- [GramClaw MCP - Telegram Outreach Workflow for Agents](/hermes/mcp/servers/external/gramclaw-mcp/)
- [Reach MCP - Operate a Real LinkedIn Account from Your Agent](/hermes/mcp/servers/external/reach-mcp/)
- [SEOVally MCP - Scoped SEO and AI-Search Audits for Agents](/hermes/mcp/servers/external/seovally-mcp/)
