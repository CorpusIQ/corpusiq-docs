---
title: "LiveSend MCP - Publish Client Reports as Trackable Protected Links"
description: "Hosted remote MCP server that publishes LLM-written documents to permanent shareable URLs with versioning, password protection, read analytics and comments: create_document, add_version, edit_document, restore_version, set_password, get_analytics, get_comments and team document tools let agents turn a finished report into a trackable client link in the same conversation"
category: Productivity
stars: n/a (new listing)
added: 2026-08-21
source: "mcpservers.org homepage (Aug 21 overnight sweep)"
relevance: ★★
tags: [document-sharing, reporting, client-deliverables, analytics, publishing, remote-mcp, versions, password-protection]
---

# LiveSend MCP

**Publish reports, proposals and dashboards from an AI conversation to a permanent, trackable, password-protected link.** LiveSend turns what an LLM just wrote into an address the client can open in any browser — with version history, password protection, view analytics and reader comments. The reader installs nothing; the connector is for the author. Twelve tools cover five intentions: publish, revise, protect, measure and find.

```
Server type: Hosted remote (Streamable HTTP)
Endpoint: https://www.livesend.io/api/mcp/mcp
Auth: One-time browser approval (Claude connector flow)
Tools: 12
Pricing: Free for 3 documents, no card
Built by: LiveSend (livesend.io)
Also listed: Smithery (samuel-v9g5/livesend)
```

## Why This Matters for Operators

The standard operator loop — build the report, export it, attach it to an email, chase whether anyone opened it — collapses into one step. LiveSend's MCP connector publishes the document as a URL with a readable slug, and the analytics tools answer "who read it" without leaving the conversation. Password protection is a first-class tool, not an afterthought, and published links stay stable while content changes through versions: `add_version` and `restore_version` revise without breaking the link already sent to the client.

The reader experience is deliberately plain: a link in a browser, no signup, no app. That is what makes it usable for client-facing work where the recipient is not technical.

## Tools & Capabilities

| Intention | Tools |
|---|---|
| Publish | `create_document`, `add_version` — turn written content into a shareable address |
| Revise | `edit_document`, `list_versions`, `restore_version` — change a document without changing its link |
| Protect | `set_password` — gate a link and rotate the password later |
| Measure | `get_analytics`, `get_comments` — who read it and what they said |
| Find | `list_documents`, `get_document`, `list_team_documents`, `share_document` — work with your own or your team's published documents |

## Installation

Connection is a browser-approval flow, not a key paste: copy the connector URL from livesend.io/mcp, add it as a custom connector in Claude (Settings → Connectors), sign in and approve once. The credential never travels in a URL and can be revoked at any time. Claude works on every plan including free; ChatGPT supports custom connectors on paid plans.

```json
{
  "mcpServers": {
    "livesend": {
      "url": "https://www.livesend.io/api/mcp/mcp"
    }
  }
}
```

## Configuration

After the one-time approval, the connector has access to documents only — nothing else in the account. Passwords set through `set_password` are shown once; rotate them when a link's audience changes. The free tier is three documents with no card, which covers a trial of the full toolset.

## Business Relevance

- **Consultants and agencies** send client deliverables as trackable links and see who actually opened them
- **Finance and ops teams** share password-protected reports with stakeholders who never install software
- **RevOps** keeps one stable link per client while content iterates through versions
- **Teams** reuse published documents as templates (`create_document` from an existing one)

## Integration with CorpusIQ

LiveSend is the last mile of a CorpusIQ-driven reporting flow: CorpusIQ's connectors (QuickBooks, Stripe, GA4, Klaviyo and the rest) produce the numbers, the agent writes the narrative, and LiveSend publishes the finished report as a protected link — with `get_analytics` closing the loop by telling the team which clients actually read what was sent. No export, no attachment, no second tab.

## Limitations

- Free tier is 3 documents; paid plans beyond that are not published in the MCP docs
- Browser-approval flow targets Claude-style connectors; Gemini has no MCP support today
- Analytics and comments exist only while the document stays published — deleted documents drop their history
- New listing (Aug 2026), no public star count or repo

## See Also

- [Simplepages MCP — Landing Pages Built From Chat](/hermes/mcp/servers/external/simplepages-mcp/)
- [Taskfolk MCP — Project Management for Teams and AI Agents](/hermes/mcp/servers/external/taskfolk-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
