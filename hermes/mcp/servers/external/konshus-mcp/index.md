---
title: "Konshus MCP - Personal Memory Vault for Every AI Client"
description: "A member-owned memory vault that ingests ChatGPT, Claude, Gemini and Grok history, distils it into sourced memories, and serves it to any MCP client under per-scope tokens with time-travel recall."
category: Memory and Knowledge
stars: n/a (hosted, subscription with a free tier)
added: 2026-11-05
source: "The mcp.so card konshus at 2026-11-05T17:29:38.960Z (Memory and Knowledge, verified and featured, submitted by Daniel Urmann); the official MCP registry record ai.konshus/memory at 1.0.0 published 2026-11-05T17:35:03Z with a streamable-http remote at https://konshus.ai/api/mcp; HTTP reads on konshus.ai/mcp (200, the 11-tool table, scope groups and self-reported usage), konshus.ai/pricing (200, the five-tier ladder and the free Ember tier), konshus.ai/llms.txt (200, the source list and the product ladder), konshus.ai/.well-known/oauth-authorization-server and /.well-known/oauth-protected-resource (200, the OAuth metadata); and two keyless JSON-RPC calls against the endpoint returning HTTP 401"
relevance: ★★
tags: [personal-memory, memory-portability, provenance, oauth, scoped-tokens, chatgpt, claude, gemini, consumer, read-write]
last_updated: "2026-11-05"
---

# Konshus MCP

**Every memory entry in this catalog belongs to a project, an agent or a team. Konshus is the first entry whose unit of memory is the person.** It takes a member's own AI history, chats from ChatGPT, Claude, Gemini and Grok, plus journals, notes, document archives and social exports, and distils it into sourced atoms: short facts that each carry where they came from and how confident the system is. Any MCP client that connects then reads that same vault, so a switcher keeps their context when they change assistants instead of starting from zero.

```
Server type: Remote, Streamable HTTP (stateless)
Endpoint:    https://konshus.ai/api/mcp
Auth:        OAuth 2.1 with PKCE and dynamic client registration, scope vault:rw,
             or a personal token issued per scope at /vault/connections/manage
Version:     1.0.0 (registry ai.konshus/memory, published 2026-11-05)
Tools:       11, grouped into summary, recall, capture and full-mirror scopes
Pricing:     Ember free (50 memories) then $49, $149, $299 and $599 a year
Coverage:    Member vaults only; 25 sources, 22 live, 1 beta, 2 announced
Vendor:      Konshus, konshus.ai
```

**The evidence tier is stated rather than implied.** A keyless `initialize` against `https://konshus.ai/api/mcp` returned **HTTP 401** with `{"code":-32001,"message":"Unauthorized: Missing Authorization header. Konshus MCP is stateless - every request (initialize, tools/list, tools/call) must include 'Authorization: Bearer ...'"}`. A second call with a probe token returned **401** `Invalid or expired token. Create a new token at https://konshus.ai/vault/connections/manage`. So no tool was called and nothing below is a live payload. What was measured: the two **401** shapes, the RFC 9728 protected-resource metadata naming the authorization server, the authorization-server metadata listing `authorization_code`, `refresh_token`, `S256` and a registration endpoint, the vendor's own tool table and scope groups at `konshus.ai/mcp` (**200**), the pricing ladder at `konshus.ai/pricing` (**200**), the source list at `konshus.ai/llms.txt` (**200**) and the registry record at **1.0.0**. The usage figures the vendor prints on its own page are self-reported and are labelled as such below.

## The eleven tools, by scope

The scope grouping is the part an operator should read first: a token is issued for one of four scopes, so the assistant that receives it gets exactly that surface and nothing else.

| Scope | Tool | What comes back |
| --- | --- | --- |
| summary | `get_whisper` | a ~300-word identity primer, intended to be read before every reply |
| summary | `get_briefing` | the multi-page briefing for deep context |
| summary | `get_persona_summary` | who the person is, how they think, what matters to them |
| summary | `get_vault_stats` | sources connected, atom count, last import |
| recall | `search_atoms` | semantic search over distilled memories, with `as_of` for a point-in-time view |
| recall | `search_artifacts` | raw source search across chats, notes, journals and documents |
| recall | `recall_past_self` | date-anchored recall such as what was thought about a topic on a given day |
| recall | `explain_what_you_know_about` | a synthesised narrative with citations rather than a list of links |
| recall | `whats_changed_since` | memories added or edited since a date, phrased as a catch-up |
| capture | `log_signal` | writes a new memory back into the vault mid-conversation |
| full mirror | `get_mega_briefing` | the full persona export, described as a 15-page document |

Three details are load-bearing. **`as_of` on `search_atoms`** turns the vault into a time series, which is what makes a question like what did we believe about pricing in June answerable with a date rather than a guess. **`whats_changed_since`** is the same mechanism pointed forward as a standup. **`log_signal`** is the only write, and it is the reason the OAuth scope is `vault:rw` rather than read-only: a connected assistant can add to the vault, not merely read it.

## Why it earns an entry when five memory entries already sit here

The neighbors are agent memory, not personal memory. [Agentic Memory MCP](/hermes/mcp/servers/external/agentic-memory-mcp/) is ordered conversation history, key-value context and FIFO queues for agent-to-agent handoff, with Redis on the hot path. [AIS Memory MCP](/hermes/mcp/servers/external/ais-memory-mcp/) pairs session memory with a W3C DID identity for agents. [MCP Long-Term Memory](/hermes/mcp/servers/external/mcp-long-term-memory/) is GraphRAG over Neo4j. [Linksee Memory](/hermes/mcp/servers/external/linksee-memory/) is local-first cross-agent memory with a forgetting curve and drift detection. [SPM](/hermes/mcp/servers/external/spm-structured-project-memory/) is project-scoped with context packs and access control. All five answer **what the work needs remembered**.

Konshus answers **what the person already told another vendor**. The ingestion side is the product: ChatGPT exports, Claude exports, Gemini Takeout, Grok, plus Day One, Obsidian, Notion, Bear or Evernote, Readwise, Kindle, Apple Books, RSS and Substack, Limitless and Plaud transcripts, voice memos, Facebook, Instagram and LinkedIn archives, an X archive, and a pasted document path. The vendor counts **25** sources with **22** live, Google Calendar in beta and Apple Health plus Spotify announced. Each distilled atom keeps its source and a confidence label, and the vault review screen lets the member edit or delete an atom, with the edit recorded against the source it came from.

That is a different surface from anything here, and it is the one an operator who uses three assistants actually hits: context that lives inside one vendor's product and disappears on the next model rollout.

## What it costs, read from the pricing page

| Tier | Price (launch) | Active memories | Storage | Window |
| --- | --- | --- | --- | --- |
| Ember | free, no card | 50 | not stated | not stated |
| Spark | **$49/yr** (from $98) | 250 to 500 | 10 GB | 1 year |
| Founding | **$149/yr** (from $456) | 2,500 to 10,000 | 50 GB | 3 years |
| Counsel | **$299/yr** (from $996) | 10,000 to 35,000 | 100 GB | 7 years |
| Counsel Pro | **$599/yr** (from $2,388) | highest capacity | 300 GB | lifetime |

The free tier is real but narrow: **50 memories, journal and paste only**, so an assistant connected to an Ember vault sees what the member typed in rather than what was imported from their AI history. The import path that gives the vault its value starts at Spark, and the full ChatGPT, Claude and social imports start at Founding. Storage of raw files is kept at every tier, and the plan controls how far back the active mirror reaches. The vendor states the launch discount applies until a founding cohort fills, currently **1,456 of 4,000** memberships remaining, and that the Founding price locks for life.

## Limits, and the claims this pass could not verify

- **It is a consumer product, not a business data connector.** Nothing here reads a ledger, a CRM or a warehouse. The operator value is context portability and per-memory provenance, not another source of business facts.
- **`vault:rw` is the only scope.** An agent granted access can write to the vault through `log_signal`, so the per-scope tokens are the control that matters: issue capture to nothing, and read scopes to the clients that need them.
- **The encryption and discretion claims are marketing.** "We can't even access it", "no human ever reads it" and "Swiss-grade discretion" appear on the vendor's own pages and cannot be checked from outside. Treat them as unverified until a security document or audit is published.
- **The usage figures are self-reported.** The vendor prints **99.81%** uptime over seven days, **12,055** calls, **448** connected clients and a **0.9s** p50 on its own `/mcp` page. A reader is trusting one page, not an independent monitor.
- **Stateless by design.** There is no `Mcp-Session-Id` lifecycle: every request carries the bearer. That is simpler for a gateway and it means a token leak is a full-scope leak until the token is rotated at `/vault/connections/manage`.
- **One member, one vault.** This is a single-person surface. It does not model a team, a shared workspace or per-client separation, which is exactly what SPM and Agentic Memory do model.

## Common questions

### Can an assistant connect to Konshus without a member account?

No. Both probe calls returned **401**: the endpoint advertises OAuth with dynamic client registration and PKCE, but the resource behind it is one member's vault, so there is nothing to read without that member's authorization.

### Does it replace ChatGPT memory or Claude Projects?

It competes with them rather than extending them. The vendor's pitch is that a persona export survives a model deprecation, that the same vault can be pasted or connected into a different vendor, and that each memory keeps its source. Whether the persona export is good enough is a judgment the vendor's own founder testimonial is making, not something a probe can settle.

### Is the MCP server the product, or the app?

The app. The MCP server is the delivery surface: it is how the vault reaches Claude Desktop, Cursor, Zed, ChatGPT and anything else that speaks MCP. That is why the tool list is shaped like reading a briefing rather than querying a database.

## How to start

1. Create an account, pick a name for the vault and complete the five-question intro; the free Ember tier needs no card.
2. Import one source and review the atoms the system proposed, editing or deleting before anything is served to an assistant.
3. Open `/vault/connections`, issue a token for the scope you want, and paste the MCP URL into the client.
4. Read the connection log after the first session: every call streams there, which is the control that makes a write-capable memory server tolerable.
