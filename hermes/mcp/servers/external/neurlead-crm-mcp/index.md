---
title: "NeurLead CRM MCP - Field-Service Ops Behind an OAuth Grant"
description: "The first field-service CRM here: leads, chats, a price-list estimate, dispatch and invoices behind a 32-scope OAuth grant with published plans."
category: "CRM"
stars: "n/a (vendor-hosted; MCP wrapper open at Neurlead/neurlead-crm-mcp)"
added: 2026-11-27
source: "mcp.so submission queue issue #8214 filed 2026-11-27T04:52:49Z (two servers, one publisher); official registry com.neurlead/crm; initialize on https://mcp.neurlead.com/connect/mcp answering 401 with a Bearer challenge naming https://mcp.neurlead.com/.well-known/oauth-protected-resource/connect/mcp, which answered 200 and enumerated 32 scopes on 2026-11-27; the plan document at https://mcp.neurlead.com/connect/plans read keylessly the same day; the control model read from the repository README at github.com/Neurlead/neurlead-crm-mcp"
relevance: "★★★"
tags: [crm, field-service, home-services, trades, dispatch, estimates, invoices, leads, oauth, human-in-the-loop, remote-mcp]
last_updated: "2026-11-27"
---

# NeurLead CRM MCP

**A trades business does not lose money in the software. It loses money between the call and the quote, and again between the quote and the invoice.** A plumber with four vans answers leads on a phone, prices from a sheet in his head, and finds out at month end which jobs were never billed. NeurLead is a CRM and dispatcher for exactly that business, and its MCP server exposes the workspace to an assistant: leads and their chats, the price list, the schedule, technicians, estimates and invoices.

It is also the first field-service CRM in this catalog. Nothing here has carried leads, dispatch and invoicing for a trade business, which is why it earns an entry even though every tool sits behind an OAuth grant this pass could not obtain.

```
Server type:  Remote (Streamable HTTP)
Endpoint:     https://mcp.neurlead.com/connect/mcp
Auth:         OAuth 2.0 with PKCE and dynamic client registration
Registry:     com.neurlead/crm
Challenge:    401 with WWW-Authenticate Bearer realm="NeurLead",
              resource_metadata=".../.well-known/oauth-protected-resource/connect/mcp"
Plan doc:     https://mcp.neurlead.com/connect/plans   keyless, machine-readable
Tools:        not readable without a workspace (initialize answers 401)
```

`initialize` answered **401** with a plain JSON body, `{"error": "sign in to your workspace first", "plans": "...", "signup": "..."}`, and the `WWW-Authenticate` header carried the protected-resource pointer. So the discovery documents are public and the tool surface is not.

## What the challenge document gives away

The protected-resource document answered **200** and named **32 scopes**. Read as a capability map, it is a better description of the product than most vendors publish:

| Scope group | Scopes |
|---|---|
| Leads | `leads:read`, `leads:create`, `leads:write` |
| Conversations | `chats:read`, `chats:write`, `chat:write`, `calls:read`, `calls:create`, `notes:write` |
| Selling | `catalog:read`, `prices:write`, `estimates:draft`, `estimates:send` |
| Money | `invoices:draft`, `invoices:send`, `invoices:mark_paid`, `invoices:void`, `money:read` |
| Scheduling | `schedule:read`, `visits:write`, `tasks:write` |
| Publishing | `campaigns:write`, `webhooks:manage` |
| Account surface | `companies:read`, `companies:write`, `team:read`, `team:write`, `status:write`, `files:write`, `setup:write`, `reports:read`, `offline_access` |

The granularity is the interesting part. Drafting an estimate, sending an estimate, recording a payment, voiding an invoice and changing a price are five separate grants, so a workspace can let an assistant **draft** while a person still has to **send and mark paid**. That is the same boundary this catalog keeps rewarding in other tools: the assistant does the work, a person keeps the authority.

## The plan document is written for the assistant to read

`https://mcp.neurlead.com/connect/plans` answers with no credential and is not a rendered page. It is JSON built for a model to quote:

| Plan | Price | Cities | AI leads a month | Adds |
|---|---|---|---|---|
| Starter | **$99**/mo | 1 | 200 | base workspace |
| Growth | **$199**/mo | 5 | 1,000 | 100 "Sara" AI calls a month |
| Pro | **$399**/mo | unlimited | unlimited | unlimited AI calls, content studio, multiple Thumbtack accounts |

The same document states a **14-day trial**, that a **card is required** at signup, and then hands the client an instruction list in the imperative: *"Show the user these plans and let them choose one"*, *"Give them the signup_url of that plan. They enter a card on Stripe themselves; nothing is charged for the trial days"*, *"Their login arrives by email right after checkout. Then they add connect_mcp_url as a custom connector in Claude or ChatGPT and press Allow."*

**That is a commercial message addressed to the model rather than the person**, and it is worth sitting with. The upside is honest pricing in a machine-readable place, which almost no vendor does. The downside is that a listing page an operator never sees now carries instructions the assistant is meant to follow. This catalog records the pattern rather than judging it, and quotes the prices because the endpoint published them.

## The control model is the product

The parts a trades owner actually cares about come from the vendor's own README, and they are specific:

- **Per-area access.** For each area the owner chooses whether the assistant has no access, can look, or can change.
- **Messages start in suggest-only.** The assistant drafts a customer reply and a person sends it.
- **Five actions always wait for a person:** recording an outside payment, voiding an invoice or estimate, booking a visit, starting a campaign, and changing prices or setup after go-live.
- **Sensitive topics route to a person** by rule: refunds, cancellations, complaints, damage, contracts, card numbers.
- **Every request lands in an audit log** in the workspace, and the owner can disconnect the assistant at any moment.

Read against the scope list, these are not marketing claims but enforcement points a workspace can implement per grant: `invoices:mark_paid` and `invoices:void` exist as scopes precisely so they can be withheld.

## What an operator can ask it

From the vendor's examples, which describe the intended loop well:

- "Who is waiting for a reply, and what should I answer?"
- "Which invoices have been unpaid for more than three days?"
- "Which technicians are free Friday morning?"
- "Set up my CRM from our website and ask me only what is missing."

The last one is the most interesting: a workspace whose setup can be drafted from the company's own website, with the assistant asking for whatever the site did not say.

## The second server from the same publisher

Issue #8214 filed two servers. **Neuro Home** (`https://mcp.neurohome.us/neuro-home/mcp`, registry `us.neurohome/neuro-home`) is the consumer side: describe a home repair in words or with up to three photos, get the matching job from about **100** services in **10** groups, see the price before booking, pick a free arrival window, and confirm by text, in **eight** US metros (Miami, Tampa, Atlanta, Washington DC, Austin, Raleigh, Charlotte, Houston). `initialize` answers **401** with `invalid_token` and its own protected-resource document. It is a booking marketplace rather than an operator's system, so it is noted here and not given a separate entry; the closest surface already catalogued is HireNimbus, which finds and books verified local pros.

## What is not verifiable from this pass

Honest limits, stated rather than glossed:

- **No tool list.** `initialize` answers 401, so neither the tool names nor their schemas could be read. The capability map above comes from the scope list.
- **No payload.** Nothing was driven, so no figure in this entry is a measured output; every number is the vendor's own published value.
- **US-only.** Both servers are United States products: the trades are US trades and the eight cities are US cities.
- **A card is required for the trial.** The plan document says so plainly, which is worth flagging to anyone who expects a no-card trial.

## Frequently asked questions

### Is NeurLead a CRM or a dispatcher?

Both, in one workspace. The product answers leads, prices jobs from the owner's own price list, dispatches technicians, and prepares estimates and invoices, so the office work and the field assignment share one record instead of two systems.

### Can the assistant message customers on its own?

Not by default. Messages start in suggest-only mode, where the assistant drafts and a person sends, and sensitive topics (refunds, cancellations, complaints, damage, contracts, card numbers) always route to a person regardless of the access setting.

### What does it cost?

**$99**, **$199** or **$399** a month by tier, with a **14-day** trial that requires a card and charges nothing during the trial days. The prices come from the vendor's own machine-readable plan document, read keylessly on 2026-11-27.

### Why is a gated server in this catalog?

Because the gate is the shape of the product, not an accident. A CRM holding a business's leads, prices and invoices should not answer a stranger, and the scope list published on the open discovery route is enough to describe the surface precisely.

## See also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
