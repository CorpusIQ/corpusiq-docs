---
title: "WarmySender MCP - Self-Hosted Cold Email With Hard Caps"
description: "WarmySender is AGPL-3.0 self-hosted cold email whose MCP server creates and starts campaigns but cannot send a message or raise a mailbox cap."
category: "Sales & Outreach"
stars: 0 (new repository)
added: 2026-11-20
source: "chatmcp/mcpso submission #7729 + warmysender-oss/warmysender README (12,408 bytes) and its open-source versus hosted comparison table, 2026-11-21"
relevance: ★★
tags: [cold-email, deliverability, self-hosted, agpl, smtp, sequences, docker, remote-mcp]
last_updated: "2026-11-20"
---

# WarmySender MCP

**Self-hosted cold email with an MCP server that deliberately cannot send.** The app, a worker and PostgreSQL run from one `docker compose up`, campaigns and sequences live in your own database, and the MCP endpoint at `/mcp` creates and starts campaigns inside limits enforced in code. The scheduler sends. A tool cannot raise a limit and a tool cannot put a message on the wire.

```
Server type: Self-hosted app with MCP at /mcp, plus REST at /api/v1
Auth: API key, created and revoked in the app (shown once, stored hashed)
Transport: Streamable HTTP served by your own instance
License: AGPL-3.0 (TypeScript + PostgreSQL)
Repository: https://github.com/warmysender-oss/warmysender
Category: Sales & Outreach
```

## Why This Matters for Operators

Cold email is the one channel where an agent with a send tool is a liability. The failure mode is not a bad email; it is a loop that mails ten thousand people at 3am from a domain the company needs. WarmySender's answer is structural: per-mailbox daily cap, sending window, random gap between sends and a ramp for a new mailbox are enforced by the application, the defaults are conservative (**30 a day per mailbox, hard maximum 50**), and the MCP surface exposes campaign operations without exposing the send primitive.

That is the difference worth recording against the catalog's hosted cold-email entries. Emailchaser and Coldrig are closed-source services that a team rents; this one runs on the operator's own machine, with their own mailboxes, and the database never leaves the server.

## The Agent Contract

From the vendor README, in its own terms:

- **MCP and API tools create and start campaigns. The scheduler sends.**
- **A tool cannot raise a limit or send a message.**
- **Reply drafting saves a draft that a person sends from the inbox.**

That third line matters as much as the first two. The agent does the expensive part (read the reply, write the response) and a human still presses send on a conversation that a prospect expects to be personal.

## What the Self-Hosted App Covers

| Area | Included in the open-source app |
|---|---|
| Runtime | `docker compose up` runs app, worker and PostgreSQL; jobs stay in Postgres through pg-boss |
| Accounts | Email and password; the first visitor becomes admin and invites teammates by link |
| Mailboxes | Any SMTP/IMAP host, with presets for Gmail and Google Workspace app passwords, Zoho, Hostinger, Fastmail and custom hosts; Microsoft 365 through your own Entra app |
| Sending controls | Per-mailbox daily cap, sending window, random gap, ramp for new mailboxes |
| Lists | CSV import, lists, global suppression list |
| Sequences | Variables and fallbacks, same-thread follow-ups, a launch check that lists problems in words |
| Compliance | `List-Unsubscribe` and one-click unsubscribe; no open or click tracking in v1 |
| Inbox | Unified inbox; a real reply stops the sequence, auto-replies are labelled and do not stop it, bounces are suppressed |
| Reporting | Stats per campaign, step and mailbox |
| Interfaces | REST `/api/v1` and MCP `/mcp`, with connection snippets for six clients in `docs/agents.md` |

The diagnostic worth knowing about is a DNS deliverability check on each mailbox (SPF, DKIM, DMARC, MX), also available as `pnpm doctor` or `docker compose run app doctor`. It will not fix a cold domain for you, but it tells you the domain is cold before the campaign does.

## Installation

```bash
git clone https://github.com/warmysender-oss/warmysender
cd warmysender
docker compose up
```

Then, in the running app: create the admin account, add a mailbox and check its DNS report, create an API key, and add the MCP endpoint to the client:

```json
{
  "mcpServers": {
    "warmysender": {
      "type": "http",
      "url": "https://your-warmysender-host/mcp",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```

The vendor lists Claude, ChatGPT, Cursor, Codex, OpenClaw and Hermes Agent as supported clients. The same actions exist on the REST API when a workflow needs them outside an agent.

## Pricing

The open-source application carries no licence fee and runs on your server. Warmup network, mailbox verification, a leads database and LinkedIn are **hosted-only** features that a self-hoster connects with a WarmySender key, and the core app works with no key at all. The hosted product is advertised at **Pro $9 a month** on a sign-up offer; that figure is the vendor's and applies to the cloud service, not to this repository.

## Honest Limits

- **No warmup network in the open-source app.** Warmup is a hosted feature reached with a key. A team that wants warmup from day one is buying the cloud plan, not running this.
- **You operate PostgreSQL and the worker.** Deliverability, IP reputation, domain age and unsubscribe handling are yours; the application enforces caps, it does not earn trust.
- **The cap is a guardrail, not a licence.** 30 a day per mailbox by default with a hard ceiling of 50 is a technical control. Sending 50 a day from a cold domain is still a bad plan.
- **v1 does not track opens or clicks**, by design and per the README. Any reporting that assumes engagement events is reading a system that does not emit them.
- **Young repository.** Published with no star history and a first release inside November 2026, so treat the MCP surface as an early one and pin the image you deploy.
- **No hosted endpoint to probe.** Unlike the remote servers in this catalog there is nothing to challenge from a documentation host, so this guide records the vendor's documented contract rather than a measured gate.

## Integration with CorpusIQ

CorpusIQ holds the pipeline truth an outbound campaign is judged against: who replied, who booked, what closed. WarmySender holds the sending side. Running it self-hosted keeps the mailbox credentials, the corpus of prospects and the reply text on the operator's own infrastructure, which is the arrangement most B2B teams actually want, and the REST API is enough to feed campaign and mailbox stats into a weekly review beside the CRM numbers.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [Coldrig MCP - Agent-Native Cold Email Infrastructure](/hermes/mcp/servers/external/agent-cold-email-mcp)
- [Emailchaser MCP - Cold Email Operations for Agents](/hermes/mcp/servers/external/emailchaser-mcp)
