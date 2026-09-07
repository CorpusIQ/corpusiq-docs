---
title: "caldav-mcp - Calendar Operations over CalDAV for Agents"
description: "caldav-mcp reads and writes calendars over CalDAV from an MCP client: events, tasks and journal entries on Radicale, Baikal, Nextcloud, SOGo, Fastmail, iCloud and any standards-compliant server. 22 tools with read-only mode, client-side recurring-event expansion, calendar fencing and If-Match guarded writes. TypeScript stdio, MIT."
category: Productivity
stars: 0
added: 2026-09-07
source: "chatmcp/mcpso issue #3958"
relevance: ★★
tags: [caldav, calendar, scheduling, stdio, productivity, local]
---

# caldav-mcp - Calendar Operations over CalDAV for Agents

**Local stdio MCP server (TypeScript, MIT)** - caldav-mcp gives an MCP client read and write access to calendars over the CalDAV standard: events, tasks and journal entries on Radicale, Baikal, Nextcloud, SOGo, Fastmail, iCloud and hosted providers generally. It is part of the ni-c suite alongside imap-mcp (read mailbox) and smtp-mcp (send mail).

```
Server type: Local (stdio, TypeScript)
Auth: CalDAV account credentials; no vendor API
Install: npx @ni-c/caldav-mcp
Tools: 22 (10 read, 12 write); CALDAV_READ_ONLY=true unregisters the write tools
Pricing: Free software
Category: Productivity
Built by: ni-c (github.com/ni-c/caldav-mcp)
```

## Why This Matters for Operators

Calendar data is scheduling truth, and agents that cannot touch it fall back to asking humans to read their own calendars aloud. caldav-mcp puts calendar operations in the agent's hands with the ni-c safety conventions: writes are read-modify-write guarded with If-Match so unknown properties, alarms and attendees survive edits; recurring events are expanded client-side with three independent bounds; and a CALDAV_CALENDARS fence confines the server to named calendars, enforced at the point where ids are decoded.

**Calendar content is treated as untrusted input - a scheduling-enabled server lets anyone who knows your address write into your calendar - so returned content is fenced with a per-call nonce and nothing the server says in its own voice quotes it.**

## Tools & Capabilities

| Group | What the agent does |
|---|---|
| Event operations | Read, create, update and delete events across the server's calendars |
| Tasks and journals | Task and journal entry management over VTODO and VJOURNAL |
| Recurrence | Client-side expansion of recurring events, bounded against pathological rules |
| Safety controls | CALDAV_READ_ONLY unregisters write tools; CALDAV_CALENDARS fences to named calendars; series changes ask a person through MCP elicitation |

## Installation

```bash
npx @ni-c/caldav-mcp
```

## Configuration

```json
{
  "mcpServers": {
    "caldav": {
      "command": "npx",
      "args": ["@ni-c/caldav-mcp"],
      "env": {
        "CALDAV_URL": "https://dav.example.com",
        "CALDAV_USERNAME": "ops@example.com",
        "CALDAV_CALENDARS": "Work,Team"
      }
    }
  }
}
```

Set CALDAV_READ_ONLY=true to keep the server strictly read-only; writes are otherwise read-modify-write over the parsed tree guarded with If-Match from the same read.

## Business Relevance

- **Exec assistants and ops teams** let the agent manage meetings across standards-compliant servers.
- **Teams on Nextcloud or Fastmail** get agent scheduling without migrating calendar stacks.
- **Security-conscious operators** use the calendar fence to keep the agent inside named calendars.
- **Developers** pair caldav-mcp with imap-mcp and smtp-mcp for a complete ni-c communications stack.

## Integration with CorpusIQ

CorpusIQ knows when revenue events happen; caldav-mcp knows when people are available to act on them. A composed workflow: the agent reads the revenue calendar from CorpusIQ's Stripe data, finds open slots via caldav-mcp, and books the follow-up meeting inside the same task.

## Limitations

- Brand new listing (issue #3958, Sep 5, 2026); repo and package are days old (0 stars).
- Requires a CalDAV-compatible server; proprietary calendars (Google Calendar API-only setups) are out of scope.
- Write safety depends on the server honoring If-Match; a misbehaving server degrades to optimistic writes.

## See Also

- [carddav-mcp - Address Book Operations over CardDAV for Agents](/hermes/mcp/servers/external/carddav-mcp/)
- [imap-mcp - Read-Only IMAP Mailbox Operations for Agents](/hermes/mcp/servers/external/imap-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
