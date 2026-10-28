---
title: "AhaSend MCP - Transactional Email From an Agent"
description: "European email API for agents with OAuth sign in, scoped keys, delivery diagnosis and campaign sends that stop for a human yes."
category: Operations / Email Infrastructure
stars: ★★ (free 1,000 emails a month, OAuth)
added: 2026-10-28
source: "live probe of https://mcp.ahasend.com/mcp returning HTTP 401 with the body no bearer token, the vendor README published on mcp.so covering OAuth 2.1, the recipient cap, the campaign confirmation step, the local developer binary and the MIT source repository github.com/AhaSend/ahasend-mcp"
relevance: ★★
tags: [email, transactional-email, smtp, deliverability, dns, campaigns, oauth, streamable-http, open-source]
last_updated: "2026-10-28"
---

# AhaSend MCP

**The most expensive email failure is the one nobody reports: an order confirmation that never arrived, discovered when the customer asks for a refund.**

```
Server type: Remote (Streamable HTTP), open-source server
Endpoint:    https://mcp.ahasend.com/mcp
Auth:        OAuth 2.1 in the browser, no key to copy
Local dev:   build cmd/ahasend-mcp-dev, AHASEND_API_KEY
             and AHASEND_ACCOUNT_ID
Free plan:   1,000 emails a month
Single send: 50 recipients by default
Source:      github.com/AhaSend/ahasend-mcp (MIT)
```

## Why This Matters for Operators

Transactional email is infrastructure a business owns without noticing. It runs until a domain authentication record expires or a provider starts deferring, and then the failure shows up as a support ticket rather than an alert. The question an operator actually asks is "why did this one not arrive", and the honest answer usually lives in a delivery log that no one opens.

This server exposes the log to an agent in plain language, and it does so with two decisions that matter more than the tool count. First, a single send is capped at 50 recipients by default, and anything larger has to be a campaign, which shows the details and sends only after the user confirms. That closes the accidental-blast failure mode rather than warning about it. Second, received email is hidden from the agent unless explicitly enabled and is then marked untrusted, which is the right default for anything that can be instructed by a stranger.

## What It Returns, Verified

The endpoint is live and gated correctly: a bare `initialize` on `https://mcp.ahasend.com/mcp` returned HTTP 401 with the body `no bearer token`. The documented auth path is OAuth 2.1 with a browser login and no key in the config, and the server itself is MIT at `github.com/AhaSend/ahasend-mcp`, built on the Go SDK at `github.com/AhaSend/ahasend-go`. A local stdio build exists for testing, `cmd/ahasend-mcp-dev`, taking `AHASEND_API_KEY` and `AHASEND_ACCOUNT_ID`.

The published capability surface, from the vendor README:

- Send transactional, template and conversation-reply email, and cancel a scheduled send
- Diagnose deliveries: list and inspect messages, explain why one failed, read deliverability, bounce and delivery-time statistics
- Manage sending domains and check their DNS records
- Create and version templates in two editors, designs as AhaML markup or as MJML
- Manage contacts, lists and segments, and create, test, schedule and send campaigns
- Manage webhooks, inbound routes, suppressions, SMTP credentials and sub-accounts

Two structural details carry weight. Tool exposure is scoped by the API key, so a key that cannot write does not show the write tools at all, and a read-only mode exists. And the underlying platform is a European email API with its own servers in the EEA and ISO 27001 certification, which is a different data-residency answer from the American providers.

## Limits Worth Recording

- **The tool list was not enumerated.** OAuth gates the surface, so the evidence is the 401 shape plus the vendor documentation, not a `tools/list` response. Treat the capabilities as documented rather than observed.
- **Campaign sends still need a person.** The confirmation step is the point, so an agent cannot run a newsletter unattended; if that is the requirement, this is the wrong tool on purpose.
- **50 recipients per send is a default, not a ceiling.** It is configurable, but raising it moves the guard rather than removing the risk.
- **Inbound email is hostile input.** Received mail is hidden by default and marked untrusted when enabled. Anything that reads it needs the same treatment as a web page.
- **The free plan is a real plan.** 1,000 emails a month is enough to prove a flow and not enough to run a business on, and nothing in the server hides that line.
- **Sub-accounts are the platform path.** Isolating each customer's sending reputation means provisioning sub-accounts, which is an architecture decision made before the first send.

## Wiring It Up

```json
{"mcpServers": {"ahasend": {"url": "https://mcp.ahasend.com/mcp"}}}
```

Authenticate in the browser on first connect; there is no key to paste. For local work, build `cmd/ahasend-mcp-dev` and pass `AHASEND_API_KEY` and `AHASEND_ACCOUNT_ID`, which is also the safest place to test a template before a domain is involved.

## FAQ

### Does it need an API key in the config?

No. The remote server uses OAuth 2.1 with a browser login, so the client holds a session rather than a pasted secret. The API key path exists for the local developer binary.

### Can an agent send a newsletter on its own?

No. Campaign sends show the send details and complete only after the user confirms, and a single send is capped at 50 recipients by default. Bulk mail has to go through the campaign path with that confirmation.

### Does it read my inbox?

Only if inbound routes are enabled and the received-email surface is turned on, and mail that arrives that way is marked untrusted rather than treated as instructions.

### Where is the code?

The MCP server is MIT at `github.com/AhaSend/ahasend-mcp`, built on the Go SDK at `github.com/AhaSend/ahasend-go`.
