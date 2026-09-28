---
title: "Cooper Email MCP - Agent Inboxes with OAuth 2.1"
description: "Cooper Email gives AI agents their own inboxes: create an address, send and receive mail, and search messages over MCP."
category: Communication & Email
stars: n/a (new listing)
added: 2026-09-28
source: "mcpservers.org server page (cooperemail.com)"
relevance: ★★
tags: [email, inbox, oauth, mail-automation, communication, remote-mcp]
---

# Cooper Email MCP

**Email inboxes an AI agent creates and operates itself.** Cooper Email runs a hosted MCP at `https://cooperemail.com/mcp` where agents create inboxes, send and receive mail and search messages, authenticating with OAuth 2.1 plus PKCE or a Bearer key for scripts.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 + PKCE, or Bearer key for scripts and Cursor
Endpoint: https://cooperemail.com/mcp
Tools: onboard and inbox creation, send, receive, search
Pricing: vendor pricing (cooperemail.com)
Category: Communication & Email
Built by: Cooper Email (cooperemail.com)
```

## Why This Matters for Operators

The standard way to give an agent email, a shared Gmail account, breaks the moment the agent needs its own identity: separate inboxes for research bots, support aliases or campaign mail should not share a human mailbox. Cooper lets the agent create its own inbox through a normal connector flow, with the consent screen approving the exact inbox.

The engineering posture is reassuring for operator scrutiny: discovery endpoints publish the OAuth protected resource and authorization server metadata, dynamic client registration is supported, and every token authorizes the same account as an API key.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Onboarding | cooper_onboard creates an inbox in the connector flow |
| Send and receive | Mail in and out of agent-created inboxes |
| Search | Full-text search across messages |

Tool names are served from the endpoint; cooper_onboard is named in the published connector playbook.

## Installation

```bash
claude mcp add --transport http cooper-email https://cooperemail.com/mcp
```

The consent screen creates an inbox or accepts an existing key. Cursor and Claude Code configs are published at cooperemail.com/connectors.

## Configuration

```json
{
  "mcpServers": {
    "cooper-email": {
      "type": "http",
      "url": "https://cooperemail.com/mcp"
    }
  }
}
```

## Business Relevance

- **Founders** give each agent workflow its own address instead of a shared inbox
- **Support teams** run agent-driven inboxes with OAuth consent per box
- **Growth operators** spin up research-bot addresses on demand
- **Developers** get scripted access through Bearer keys alongside OAuth flows

## Integration with CorpusIQ

Cooper complements the CorpusIQ Gmail and Outlook connectors the same way Faivelo and Postfleet do: human inboxes stay on Gmail while agent-originated traffic runs through Cooper addresses, keeping identity boundaries clean.

Pair Cooper inboxes with the CorpusIQ HubSpot and ActiveCampaign connectors: the agent handles the mail conversation while the CRM records the contact and the automation tool sequences the follow-up.

## Limitations

- New listing, no track record yet
- ChatGPT plugin listing is a submission path, not an approved OpenAI directory listing
- Self-hosting requires external storage setup, production notes reference Turso on Vercel
- Tool names beyond cooper_onboard are not published

## FAQ

### How does the agent get an inbox?

The consent flow calls cooper_onboard during connector setup, creating the inbox or accepting an existing key.

### What auth does it use?

OAuth 2.1 with PKCE for Claude and ChatGPT connectors, plus Bearer keys for scripts and Cursor.

### What is the MCP endpoint?

https://cooperemail.com/mcp with Streamable HTTP transport and an /api/mcp alias.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
