---
title: "carddav-mcp - Address Book Operations over CardDAV for Agents"
description: "carddav-mcp reads and writes address books over CardDAV from an MCP client: contacts, groups and contact photos on Radicale, Baikal, Nextcloud, SOGo, Fastmail, iCloud and any RFC 6352 server. 17 tools with read-only mode, both vCard group conventions, single-query search and If-Match guarded writes. TypeScript stdio, MIT."
category: Productivity
stars: 0
added: 2026-09-07
source: "chatmcp/mcpso issue #3966"
relevance: ★★
tags: [carddav, contacts, address-book, groups, stdio, productivity, local]
---

# carddav-mcp - Address Book Operations over CardDAV for Agents

**Local stdio MCP server (TypeScript, MIT)** - carddav-mcp reads and writes address books over CardDAV from an MCP client: contacts, groups and contact photos on any server that implements RFC 6352 - Radicale, Baikal, Nextcloud, SOGo, Fastmail, iCloud and hosted providers generally. Part of the ni-c suite alongside imap-mcp, smtp-mcp and caldav-mcp.

```
Server type: Local (stdio, TypeScript)
Auth: CardDAV account credentials; no vendor API
Install: npx @ni-c/carddav-mcp
Tools: 17 (10 read, 7 write); CARDDAV_READ_ONLY=true unregisters the write tools
Pricing: Free software
Category: Productivity
Built by: ni-c (github.com/ni-c/carddav-mcp)
```

## Why This Matters for Operators

Contact data has a long tail of legacy detail - a vCard property a phone wrote in 2014, a group defined in the Apple convention that the other convention cannot see - and naive contact tools destroy exactly that. carddav-mcp's writes are read-modify-write over the parsed card guarded with If-Match, never a document rebuilt from the fields the server models, so unknown properties, photos and parameters survive every edit.

**Both group conventions are read (vCard 4 KIND:group with MEMBER, and Apple's X-ADDRESSBOOKSERVER-KIND), and a written group follows whichever convention the address book already uses - because a group in the other convention is invisible in the client the person is looking at.**

## Tools & Capabilities

| Group | What the agent does |
|---|---|
| Contact operations | Read, create, update and delete contacts with full property preservation |
| Groups | Read both group conventions; write in the address book's existing convention |
| Photos | Read and write contact photos |
| Search | Single addressbook-query per search with local re-checking of results |
| Safety controls | CARDDAV_READ_ONLY unregisters write tools; CARDDAV_ALLOW_TOOLS=essential narrows to a curated six |

## Installation

```bash
npx @ni-c/carddav-mcp
```

## Configuration

```json
{
  "mcpServers": {
    "carddav": {
      "command": "npx",
      "args": ["@ni-c/carddav-mcp"],
      "env": {
        "CARDDAV_URL": "https://dav.example.com",
        "CARDDAV_USERNAME": "ops@example.com"
      }
    }
  }
}
```

Set CARDDAV_READ_ONLY=true for a strictly read-only surface, or CARDDAV_ALLOW_TOOLS=essential to narrow to a curated six-tool set.

## Business Relevance

- **Sales teams** let the agent maintain CRM-adjacent contact books on self-hosted servers.
- **Teams on Nextcloud or Fastmail** get agent contact management without platform lock-in.
- **Privacy-conscious operators** keep contact data on their own CardDAV server, not a vendor CRM.
- **Developers** complete the ni-c stack: imap-mcp (mail), smtp-mcp (send), caldav-mcp (calendar), carddav-mcp (contacts).

## Integration with CorpusIQ

CorpusIQ holds the revenue relationships; carddav-mcp holds the people. A composed workflow: the agent identifies top accounts in CorpusIQ's Stripe data, then updates the stakeholder contacts and groups in the team's CardDAV address book so every touchpoint has current details.

## Limitations

- Brand new listing (issue #3966, Sep 6, 2026); repo and package are days old (0 stars).
- Requires a CardDAV-compatible server; proprietary contact stores are out of scope.
- Write safety depends on the server honoring If-Match.

## See Also

- [caldav-mcp - Calendar Operations over CalDAV for Agents](/docs/hermes/mcp/servers/external/caldav-mcp)
- [imap-mcp - Read-Only IMAP Mailbox Operations for Agents](/docs/hermes/mcp/servers/external/imap-mcp)
- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
