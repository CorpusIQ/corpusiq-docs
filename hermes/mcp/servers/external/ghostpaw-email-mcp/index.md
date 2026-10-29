---
title: "GhostPaw Email MCP - An IMAP Mailbox for an Agent"
description: "Point an agent at a real mailbox over IMAP and SMTP, with a local SQLite cache that makes search and threading instant."
category: Communication
stars: ★★ (package and tools verified, v0.5.10, MIT)
added: 2026-10-29
source: "npm package @ghostpaw/email 0.5.10 read from the npm registry on 29 October 2026 (MIT, repository GhostPawJS/email) and the vendor submission with its five tool names"
relevance: ★★
tags: [email, imap, smtp, mailbox, threading, full-text-search, local-mcp, zero-dependency]
last_updated: "2026-10-29"
---

# GhostPaw Email MCP

**An assistant that can read a mailbox is useful. An assistant that re-reads ten thousand messages from the server every time you ask a question is not.**

```
Server type: Local (stdio)
Install:     npx -y @ghostpaw/email mcp
Package:     @ghostpaw/email 0.5.10, MIT
Runtime:     Node.js 24 or newer
Protocols:   IMAP for reading, SMTP for sending
Cache:       local SQLite with threading, full-text search, folder sync
Dependencies: none at runtime
Tools:       mail_read, mail_search, mail_compose, mail_organize, mail_sync
```

## Why This Matters for Operators

Standards-based email is the least fashionable and most portable option in this catalogue. Every hosted email connector here depends on one vendor's API, its quotas and its continued goodwill. IMAP and SMTP have been the same for decades and work against whatever mailbox a business already pays for, including a tired shared inbox that nobody wants to migrate.

The design decision worth recording is the local cache. The server keeps a SQLite copy with threading, full-text search and folder synchronisation, so a question about last year's correspondence is answered from disk rather than by crawling the server. `mail_search` can search the local cache or the server, and `mail_sync` is the tool that reconciles the two.

The engine is written with **no runtime dependencies**, which for a component that sits next to credentials is a meaningful property rather than a stylistic one: there is no dependency tree to audit.

## The Five Tools

- **`mail_read`** shows folders, the message queue, threads and single messages.
- **`mail_search`** searches the local cache or the server, which is the difference between a fast answer and a slow one.
- **`mail_compose`** sends new mail, replies and forwards, and saves drafts.
- **`mail_organize`** marks, moves, labels, archives or trashes messages.
- **`mail_sync`** manages the IMAP connection and keeps local state in step with the server.

The same five tools power the stdio server, the `ghostpaw-email` command-line tool, an Agent Skill and a TypeScript library, so behaviour is one implementation rather than four.

## What Was Verified

The npm registry entry for `@ghostpaw/email` resolved on 29 October 2026 at version **0.5.10**, licence **MIT**, repository `github.com/GhostPawJS/email`, with two bins, `email` and `ghostpaw-email`. The description states the shape directly: a standalone IMAP/SMTP email engine for Node.js with a SQLite local cache, threading, sync and zero dependencies, with a built-in LLM tool facade. Author is Maximilian Stroh, and the official registry entry is `io.github.GhostPawJS/email`.

## Limits Worth Recording

IMAP and SMTP are credentials, not OAuth grants, on most providers. Nothing in this server changes the fact that an app password usually has to be issued, and that the password grants whatever the mailbox grants. Scope it at the provider where the provider allows it.

A local cache is a local copy of correspondence. It sits on the machine running the server, under the operator's control, and that is a retention question someone should answer deliberately.

There is no hosted endpoint. Browser chat clients cannot reach a stdio server, so this works in Claude Desktop, Claude Code, Cursor, Codex and similar local clients.

## FAQ

### Does it work with any email provider?
Any provider that offers IMAP and SMTP, which is most of them including self-hosted and shared hosting accounts.

### Why keep a local cache?
So search and threading are fast and cheap. `mail_search` can read the cache, and `mail_sync` reconciles it with the server, so a question does not cost a full traversal of the mailbox.

### Can the agent send mail?
Yes, through `mail_compose`, which sends new mail, replies and forwards, and can save a draft instead of sending.

### What are the runtime requirements?
Node.js 24 or newer. The engine itself has no runtime dependencies.

### Can I use it from the ChatGPT or Claude web app?
No. It is a local stdio server, so it needs a desktop or local client.
