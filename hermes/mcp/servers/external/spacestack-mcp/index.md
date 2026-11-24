---
title: "Spacestack MCP - Venue Bookings Inside the Assistant"
description: "An events CRM behind a complete OAuth chain: two scopes, a workspace switch an owner must flip, and a role model the token cannot express."
category: "Productivity"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-24
source: "A mcpservers.org canonical arrival at /servers/spacestack and an mcp.so feed card stamped 2026-11-24T04:10Z; keyless initialize on https://mcp.spacestack.io/mcp answering 401 with a WWW-Authenticate resource_metadata pointer; the protected-resource document and the RFC 8414 authorization-server document read 2026-11-24; product, permission and pricing facts read from www.spacestack.io/help-center/ai-assistants (updated November 24, 2026) and www.spacestack.io/pricing, both on 2026-11-24"
relevance: "★★"
tags: [venue-management, crm, events, bookings, oauth, remote-mcp, productivity]
last_updated: "2026-11-24"
---

# Spacestack MCP

**A wedding venue's calendar is the whole business: one Saturday double-booked is a refund, a review and a lost referral.** Spacestack is venue management software for wedding venues, event spaces and the groups that run several of them, and its MCP server lets a chat assistant answer the two questions a venue answers all day, whether a date is free and what is booked next, and take the action that follows, which is to put a new inquiry on the calendar.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.spacestack.io/mcp
Auth:        OAuth, scopes spacestack:read and spacestack:write
Tools:       not published on the listing; the endpoint refuses keyless
Pricing:     $99 per venue per month billed yearly ($1,188 a year), 30-day trial
```

## The gate, measured

`initialize` with no credential answers **401**, and the refusal is a bearer challenge that names its own documentation:

```
www-authenticate: Bearer error="invalid_token",
  error_description="Authentication required",
  resource_metadata="https://mcp.spacestack.io/.well-known/oauth-protected-resource/mcp"
```

The protected-resource document at that exact path answers **200**:

```json
{"resource":"https://mcp.spacestack.io/mcp",
 "authorization_servers":["https://mcp.spacestack.io"],
 "scopes_supported":["spacestack:read","spacestack:write"],
 "bearer_methods_supported":["header"],
 "resource_name":"Spacestack",
 "resource_documentation":"https://www.spacestack.io/help-center/ai-assistants"}
```

Two scopes, and the split is the one that matters to an operator: read means read, write means create and update. The authorization server is the MCP host itself, and its RFC 8414 document answers **200** with authorization code and refresh grants, a dynamic registration endpoint, and `none`, `client_secret_post` and `client_secret_basic` as token endpoint methods, so a desktop client can register itself without a manual key. That is four measured hops and no hand-written client secret anywhere in the chain, which is the cleanest outcome for a client that supports remote OAuth and a dead end for one that does not: this endpoint has no API-key path published.

The bare well-known route without the `/mcp` suffix answers **404**, so a client that trims the suffix will fail at the discovery step rather than at the token step. Worth knowing before blaming the vendor for a credential problem.

## The permission model is the product

The MCP listing does not carry a tool list, and that is honest rather than lazy: the tool surface changes with the role of the person who connected. What the vendor documents, in a help article updated on **November 24, 2026**, is a boundary worth reading before anyone switches this on:

| The assistant can | The assistant cannot |
| --- | --- |
| Search and read bookings, contacts, accounts, tours, tasks, invoices, inquiries and reports | Delete or archive anything |
| Check availability and read the calendar | Send documents, invoices or messages to clients |
| With write access: create and update contacts, accounts, bookings, events, tours and tasks, and add notes | Take, void or refund payments |
| Use a daily briefing dashboard | Change settings, billing or the team |

Three mechanics sit under that table and all three are unusual enough to quote. **The connector acts as the signed-in team member, with that person's role**, so a viewer's assistant can only read and no assistant can exceed the role of the human who connected it. **The connect step offers Read only or Read and write**, chosen per person rather than per workspace, which means an owner can let the sales lead write and the bookkeeper read. And **the workspace switch is off by default**: an owner or admin turns it on under Settings, then AI assistants, and turning it off disconnects everyone straight away. A workspace-level kill switch that the vendor documents as immediate is the single best control an operator can ask for, and it sits above OAuth rather than inside it.

Two consequences the vendor states plainly and an operator should not skip. Changes an assistant makes appear **under the person's name**, so attribution survives the delegation. And Spacestack **keeps a log of what assistants do for 90 days** for support and security, visible only to Spacestack staff, while nobody inside the workspace, including the owner, can read what a colleague asked the assistant. That is a defensible split, but it means the workspace audit trail is your own database changes, not the conversation.

## What it is actually for

The worked examples on the help page are the product direction, and they are concrete: *"Is next Saturday open for a 120-guest wedding?"*, *"What tours do we have this week, and what should I know before each one?"*, *"Which new inquiries from the last 7 days haven't been answered yet?"*, and *"Add a lead for Sarah Kim, wedding for about 120 guests in fall 2027, and book her a tour Thursday at 2pm."*

The last one carries the detail that shows the vendor thought about the failure mode: **before it books a tour, the agent asks whether Spacestack should email the guest a confirmation**, and if a tour that already emails its guest is moved or cancelled, the guest hears about it exactly as they would if a person had changed it in the app. That is the difference between a chat window that reports and a chat window that acts: the side effects a human would trigger are preserved, and the irreversible one is confirmed first.

## Pricing and what it means per venue

Read from the pricing page on 2026-11-24: **one plan, every feature, priced per venue**. **$99 per venue per month billed yearly, $1,188 per venue a year**, monthly billing offered at a higher rate, **unlimited seats**, no setup fees, and a **30-day free trial with no card**. Groups running **5 or more venues** are quoted custom. White-glove migration is included on every plan, and the vendor names the systems it moves venues from: HoneyBook, Dubsado, Tripleseat, Event Temple, Planning Pod, Perfect Venue, spreadsheets and email.

The MCP connector itself is included in the plan, which the help page states in the FAQ, and the one real cost outside it belongs to the AI vendor: ChatGPT custom connectors require a paid ChatGPT plan. For a group of five venues, the annual commitment is **$5,940** before the AI subscription, so the decision is a real one and the trial is the honest way to test it.

For a single-venue operator the comparison the vendor makes is the right one: general client CRMs are cheaper and do not model date holds, tours and BEOs; traditional venue platforms model them and add quotes, contracts and setup fees. Whether $99 a venue a month is worth it comes down to how many inquiries are answered late, which is a number the operator has and the catalog does not.

## How to use it

1. Have an owner or admin open **Settings**, then **AI assistants**, and switch the connector **On**. The server address appears with the connect steps.
2. In ChatGPT, enable Developer mode under Settings, Apps and Connectors, Advanced settings; create a custom connector named Spacestack with the address `https://mcp.spacestack.io/mcp` and authentication left on **OAuth**.
3. In Claude, the vendor says Spacestack appears in Claude's connector directory, so there is no address to paste: search for Spacestack under Settings, Connectors, choose Connect, then pick the workspace and **Read only** or **Read and write**. That directory claim is the vendor's and was not verified in this pass; the custom-connector path with the same address works either way.
4. For Claude Code, Cursor and tools that cannot open a browser sign-in, create a **personal access token** under Settings, AI assistants, and copy it at creation time because it is shown once.
5. Start with a read question before a write one. A date availability check costs nothing and proves the calendar connection; the first write should be a tour on a date the operator can verify by eye.

## Boundaries recorded

- The catalog listing carries **no tool list** and the endpoint refuses keyless, so the tool surface in this guide is the vendor's documented capability rather than a measured schema. Re-probe after any vendor release.
- **No API-key path** is documented. Clients without remote OAuth support are limited to the personal access token route.
- **A log of assistant activity exists but is Spacestack's, not the workspace's.** An operator who needs a record of what was asked should keep it on their own side.
- The listing arrived through **mcpservers.org** at `/servers/spacestack` and the mcp.so feed at **04:10Z on 2026-11-24**, submitted by the vendor, which is the doing-it-right pattern: the product, the docs and the connector all changed the same day.
