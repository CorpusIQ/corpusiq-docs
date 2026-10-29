---
title: "Conecto MCP - A Whole Back Office Paid Per Call"
description: "CRM, invoices, books, email, phone, help desk and site analytics for an agent, measured at 2,009 tools across 52 areas, paid per call from credit."
category: Business Operations
stars: ★★ (401 with OAuth metadata, 2,009 tools counted across 52 keyless area servers)
added: 2026-10-28
source: "live probe of https://api.conecto.chat/v1/mcp returning HTTP 401 with scope tools plus the protected-resource document at api.conecto.chat/.well-known/oauth-protected-resource/v1/mcp, a first-hand tools/list count across all 52 area servers at api.conecto.chat/mcp/<area> totalling 2,009 tools, the 59 KB vendor skill file conecto.chat/SKILL.md, and chatmcp/mcpso issue #6328"
relevance: ★★★
tags: [back-office, crm, invoicing, bookkeeping, pay-per-call, agent-native, oauth, remote-mcp]
last_updated: "2026-10-28"
---

# Conecto MCP

**An agent that can run a business needs somewhere to run it. Bolting six SaaS tools onto a chat gives an agent six logins, not a business.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://api.conecto.chat/v1/mcp
Areas:       https://api.conecto.chat/mcp/<area>, 52 areas
Auth:        OAuth 2.1, or a Conecto key as a Bearer token
Tools:       2,009 counted across the 52 area servers
Pricing:     Pay per call from a prepaid USD balance, reads free to 1M a month
Signup:      One API call, $1.00 of credit, no subscription
```

## Why This Matters for Operators

Every other entry in this catalogue connects an assistant to a system a business already runs. This one is the opposite proposition: the assistant gets a back office to run directly, so the CRM, the invoices, the books, the inbox, the phone line, the help desk and the website chat exist as one surface with one balance, and there is nothing to integrate first.

That is worth recording because the integration tax is where most agent pilots die. A small business that wants an agent to chase an unpaid invoice needs the invoice, the customer record and the outbound message in the same callable space. Here they are 52 areas of one server, scoped per key.

The pricing model is the second reason it belongs in the catalogue. Calls are priced individually from a prepaid balance, reads of the business's own data are free up to a million a month, and failed calls cost nothing, which makes the cost of an agent's mistake a failed call rather than a subscription month.

## What It Returns, Verified

A bare `initialize` on `https://api.conecto.chat/v1/mcp` returned **HTTP 401** with

```
WWW-Authenticate: Bearer resource_metadata="https://api.conecto.chat/.well-known/oauth-protected-resource/v1/mcp", scope="tools"
```

and the resource document names the authorization server `https://conecto.chat/api/bots/oauth`, scope `tools`, `resource_name` **Conecto**.

The area servers answer `tools/list` **without a key**, so the tool surface was counted first hand rather than taken from the submission: **52 areas**, **2,009 tools** in total, with the largest being `crm` 69, `books` 61, `purchasing` 53, `hiring` 53, `invoices` 52, `hr` 51, `helpcenter` 48, `analytics` 46, `newsletters` 43, `admin` 43, `outreach` 41 and `calendar` 41. The submission filed on the mcp.so tracker claimed **581 tools across 52 areas**, so the claim understates the surface by roughly three times, and the measured number is what this entry records.

The vendor's skill file at `conecto.chat/SKILL.md` (59 KB) is the operating manual an agent is meant to read: one signup call with a business name and an owner email returns a `conecto_sk_` key and $1.00 of credit, areas are ticked per key, and a key limited to some areas or tools sees only those in `tools/list`.

## Limits Worth Recording

This is a new back office, not a bridge to an existing one. A business already running QuickBooks or HubSpot does not get its history imported by connecting this, and the catalogue's `QuickBooks`, `Fortnox` and `Xero` entries remain the path for reading the systems a business actually keeps. Writes cost money, so scoping a key to the areas an agent genuinely needs is the difference between a bounded assistant and an unbounded spender, and listing tools requires no key while calling them does. The area list is wide enough that 2,009 tools is a prompt-weight problem for a client without tool filtering, which is why the per-area servers exist and are the recommended shape.

## FAQ

### Do I need to replace my current CRM and accounting?
No, and it is not an import path. It gives the agent its own backend to operate. If the business keeps QuickBooks, use the QuickBooks or Fortnox entry instead.

### What does it cost?
Calls are paid individually from a prepaid balance, with reads of the business's own data free up to 1,000,000 a month and failed calls charged nothing. Signup grants $1.00 of credit.

### How many tools are there really?
**2,009** across the 52 area servers, counted first hand with `tools/list`. The submission claimed 581.

### Can an agent spend money on its own?
Yes, from the prepaid balance, which is why per-area keys and the vendor's rules section sit in front of the spend. A failed or refused call is free.

### Does it expose AI visibility tracking in this catalogue's sense?
It has a `visibility` area that tracks buyer questions across ChatGPT, Claude, Gemini, Grok, Perplexity, DeepSeek and AI Overviews. The catalogue's own AEO tooling is a separate entry, and this is a run-it-yourself surface inside a broader back office.
