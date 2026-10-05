---
title: Vocenya MCP - Business Calls, Leads and Bookings
description: "Remote MCP for Vocenya, the AI receptionist for small business: read calls, leads, bookings and chats, add leads and queue compliant callbacks."
category: Business Operations
stars: n/a (new listing)
added: 2026-10-05
source: mcp.so feed (Oct 5, 2026 morning sweep)
relevance: ★★★
tags: [business-operations, ai-receptionist, phone, calls, leads, bookings, small-business, remote-mcp, oauth]
---

# Vocenya MCP

**Remote MCP server (Streamable HTTP, OAuth)** - the official server from GH Business Solutions that connects an assistant to one Vocenya business account. Vocenya is the AI receptionist for local and small businesses: it answers phone calls and website chats around the clock, books appointments, captures leads and hands off to trained human agents or the owner. Through this MCP server an assistant reads the calls, leads, bookings and chats on that account, adds leads from other systems, queues compliant outbound AI callbacks and manages the Do Not Call list.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (PKCE, dynamic client registration) or an organization API key
Endpoint: https://vocenya.com/mcp/platform
Companion servers: https://vocenya.com/mcp/docs and https://vocenya.com/mcp/site (public, no key)
Tools: 9 (calls, leads, bookings, chats, outbound, Do Not Call)
Compliance: DNC lists, consent checks, 8am-8pm local calling hours, daily limits
Built by: GH Business Solutions | Docs: vocenya.com/docs/mcp
```

## Why This Matters for Operators

For a phone-led business, the receptionist layer holds the truth about demand: which calls were answered, which chats turned into bookings, which leads never called back. That record usually sits in a dashboard nobody opens, disconnected from the numbers in the rest of the business. This server puts it in the conversation: an assistant can pull the day's calls, find the leads that went quiet, queue a compliant callback and check the booking calendar, all from the same thread where the operator asks about revenue and ad spend.

The scope model is worth noting on its own. Every tool is scoped (calls:read, leads:write, outbound:write, dnc:write and so on), OAuth 2.1 handles the connector path, and even the write surface is wrapped in the same compliance machinery Vocenya applies to every call: Do Not Call lists, AI-call consent on record, 8am-8pm local calling hours and daily limits. Automation here does not create a compliance problem, which is the usual reason operators keep phone systems away from agents.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Calls | `list_calls` and `get_call` read calls handled by the AI, GH Live agents or the team (`calls:read`) |
| Leads | `list_leads` and `get_lead` read leads from calls, chats and forms (`leads:read`); `create_lead` adds a lead from another system with an optional AI callback (`leads:write`) |
| Bookings | `list_bookings` reads appointments the AI booked (`bookings:read`) |
| Chats | `list_chats` reads website live chat conversations (`chats:read`) |
| Outbound | `queue_outbound_call` asks the AI to call someone who consented, compliance checked first (`outbound:write`) |
| Do Not Call | `add_do_not_call` adds a number to the Do Not Call list (`dnc:write`) |

## Installation

```bash
claude mcp add --transport http vocenya https://vocenya.com/mcp/platform
```

OAuth 2.1 sign-in (PKCE, dynamic client registration) on first connect, supported by Claude and ChatGPT connectors. For clients that prefer keys, create a scoped API key on the Developers page of the Vocenya portal and send it as `Authorization: Bearer vk_...`; `vk_test_...` keys return separate sample data and never ring anyone. Setup pages for Claude Code, Claude Desktop, Cursor and ChatGPT: vocenya.com/docs/mcp. The companion docs and site servers are public and keyless.

## Business Relevance

- **One ledger for demand**: pull every call, lead, booking and chat the AI handled into the same assistant that answers questions about the rest of the business.
- **Compliant follow-up**: outbound callbacks are queued through the same DNC, consent, calling-hours and daily-limit checks as every Vocenya call.
- **Lead capture without retyping**: `create_lead` pushes a lead from another system (a form, a marketplace, a missed conversation) into Vocenya with an optional AI callback.
- **Service-business rhythm**: for clinics, home services, salons and trades, the missed call is the lost job. This is the surface where that data lives.

## Integration with CorpusIQ

CorpusIQ reads the financial and marketing systems read-only; Vocenya covers the phone and lead layer. A composed workflow: measure bookings and lead sources from Vocenya against ad spend in Google Ads and demand in GA4 through CorpusIQ, and answer "which channel actually produced jobs" with both halves of the record in one conversation. CorpusIQ stays read-only and never writes; Vocenya exposes its own scoped write tools (`create_lead`, `queue_outbound_call`, `add_do_not_call`) that the operator grants through OAuth or a portal key.

## Limitations

- One business account per connection: the account you sign in to with OAuth, or whose API key you connect.
- Three of the nine tools write (`create_lead`, `queue_outbound_call`, `add_do_not_call`); scope keys accordingly and use least privilege.
- Accounts in HIPAA mode never return transcripts, AI summaries or chat messages through this server.
- Hosted by Vocenya and governed by its terms; the server requires sign-in or a key (a live POST initialize returns 401 unauthenticated, confirming it is auth-gated).

## FAQ

### What is Vocenya?

An AI receptionist for local and small businesses made by GH Business Solutions: it answers phone calls and website chats around the clock, books appointments, captures leads, hands off to human agents or the owner, and places outbound AI calls with compliance checks.

### Does this MCP server write to my account?

Three scoped write tools exist: adding a lead, queueing a compliant outbound call, and updating the Do Not Call list. Everything else is read-only, and keys carry their own scopes.

### How does authentication work?

OAuth 2.1 with PKCE and dynamic client registration for Claude and ChatGPT connectors, or an organization API key created on the Developers page of the Vocenya portal.

### What about call compliance?

Outbound calls queued through MCP pass the same checks as every Vocenya call: Do Not Call lists, AI-call consent on record, 8am-8pm local calling hours and daily limits.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [PlaceCall MCP - Agent Phone Calls to Real Businesses](/hermes/mcp/servers/external/placecall-mcp/)
