---
title: "Nowistay MCP - Vacation Rental PMS in the Chat"
description: "A vacation-rental PMS and channel manager inside the chat: bookings, nightly prices, guest messages and cleaning tasks across five OTAs"
category: Productivity
stars: "n/a (hosted; OAuth with fourteen read and write scopes, keyless call returns 401)"
added: 2026-11-09
source: "mcp.so feed card published 2026-11-09T17:06:33Z (slug nowistay); the endpoint at api.nowistay.com/mcp, where a keyless initialize answered 401 Missing bearer token; the protected-resource document listing fourteen scopes; and the listing's own product notes"
relevance: ★★★
tags: [vacation-rental, airbnb, booking, property-management, channel-manager, hospitality, pms, remote-mcp]
last_updated: "2026-11-09"
---

# Nowistay MCP

**A short-term rental operator does not have one calendar, they have five: Airbnb, Booking.com, Vrbo, Expedia and Agoda each hold a version of the truth, and the double-booking happens in the gap between them. Nowistay is the property management system and channel manager that sits on top, and its MCP server puts that combined view in the chat with a staged-write rule attached.**

```text
Server type: Remote (Streamable HTTP)
Endpoint:    https://api.nowistay.com/mcp
Auth:        OAuth 2.1; keyless calls return 401 Missing bearer token
Scopes:      14, seven resource families at read and write
Listing:     mcp.so, Productivity, verified and featured
Publisher:   Nowistay (listing claimed by the vendor)
Docs:        nowistay.com
```

## What the endpoint says about itself

This entry is gated rather than open, and the gate is the most informative thing about it. A keyless `initialize` returns `401` with a plain JSON body rather than a JSON-RPC error:

```text
POST https://api.nowistay.com/mcp
{"detail":"Missing bearer token"}
```

The protected-resource document then describes the permission surface precisely, and it is the reason this server is worth cataloguing at all. Fourteen scopes, in seven pairs:

```text
properties.read    properties.write
calendar.read      calendar.write
bookings.read      bookings.write
missions.read      missions.write
messages.read      messages.write
guides.read        guides.write
knowledge.read     knowledge.write
```

That is the shape of an operational system rather than a read-only feed: bookings, nightly rates, the cleaning schedule, guest conversations, welcome guides and the operator's own knowledge base, each with a write beside the read. Authorization server is `https://api.nowistay.com` itself, bearer method `header`. Two things are worth noting for anyone wiring it up. The scope list is fine-grained enough that a client can hold a read-only grant for a reporting assistant and a separate write grant for the operations assistant, which is the split most operators actually want. And mcp.so shows no tool list for this listing, with the page saying tool discovery may need the provider's credentials, so the tool names have to come from `tools/list` after OAuth rather than from the directory.

## What the product does

Nowistay is a PMS and channel manager for vacation rentals with an AI co-host built in. The MCP server is the same surface exposed to an external assistant: properties, bookings synced from the five OTAs, calendars and prices, guest conversations, cleaning missions, welcome guides, and the private knowledge the co-host answers from.

The behaviours it documents are the interesting part, because they are choices about trust:

- **Every change is staged.** The assistant shows what will happen and nothing is written until the person confirms. This is the right default for an agent holding `bookings.write`.
- **Read-only questions never change data.** A question cannot mutate state as a side effect.
- **OTA reservations stay read-only.** A booking that arrived from Airbnb or Booking.com is not edited from the chat, which matches how channel managers actually work: the reservation belongs to the platform of record.
- **Guest contact details are handled separately** from the conversation transcript, which is the distinction a data-protection review will ask about first.

The vendor's own example questions map cleanly onto the tool families: arrivals this week across every property, prices for the next thirty days with the empty weekends flagged, a three-night minimum for July and August, a summary of tonight's guest thread with a draft reply, a cleaning task for Saturday at 11am, and revenue against cleaning cost per property for the quarter as a table.

## Why an operator would want this in the chat

The work this replaces is not glamorous and it is not small. A host with twenty units spends the morning in five dashboards reconciling availability, then answers the same guest questions in three inboxes, then texts a cleaner a list that lives in a spreadsheet. Each of those is a lookup followed by a decision, which is exactly the shape an assistant handles well when it has the real data behind it.

The staged-write rule is what makes it usable rather than dangerous. An operator's instinct is to distrust anything that can change a booking, and that instinct is correct: a wrong price on a live listing costs money within minutes. Staging turns the assistant into a colleague who prepares the change and waits for the nod, which is a different product from an autonomous agent and the one this class should have.

## The class it enters, with the owners named

Property software is well represented here, and short-term rental is the slice that was missing. [Skywalk](/hermes/mcp/servers/external/skywalk-appfolio-mcp/) reads AppFolio, which is long-term residential management. [AskRentAI](/hermes/mcp/servers/external/askrentai-mcp/) does Rent Manager property intelligence, [Tektolo](/hermes/mcp/servers/external/tektolo-mcp/) handles rental turnover and deposit settlement, and [fixRAgent](/hermes/mcp/servers/external/fixragent-mcp/) covers maintenance triage. All four assume a lease measured in months.

Nowistay is the nightly-rate business, and the mechanics are different in ways that matter: availability is a two-way sync against five channels rather than a ledger the operator owns, the price changes by the night, and the labour is a cleaning mission between guests rather than a work order. Naming a first-of-class entry is only worth doing when the class boundary is real, and here it is: no catalogued server holds a channel-manager view of Airbnb, Booking.com, Vrbo, Expedia and Agoda with a write path back to them.

## Limits, stated as limits

Nothing answers without OAuth, so this guide measures the permission surface and the vendor's own product description rather than tool output; the tool list has to come from `tools/list` with a live grant. The scope list includes `messages.write` and `bookings.write`, which means a poorly scoped client can message a guest or change a reservation, so grant per task rather than per account. OTA-sourced reservations being read-only is a documented behaviour, which is sensible and also means the assistant cannot fix a bad Airbnb booking for you; that correction still happens in the channel. And it is one vendor's system: if you are not running Nowistay as your PMS, this is not a connector to Airbnb, it is a connector to Nowistay.

## Frequently asked questions

### What does Nowistay MCP do without credentials?

Nothing except tell you it needs a token: `initialize` returns `401` with `Missing bearer token`. The permission model is still readable, because the OAuth protected-resource document is public and lists all fourteen scopes.

### Which OTAs does it actually cover?

Airbnb, Booking.com, Vrbo, Expedia and Agoda, per the vendor's own product description. Reservations received from those platforms stay read-only through the MCP, and the channel manager keeps them in sync.

### Can the assistant change a price or a booking on its own?

No. Every change is staged first: the assistant shows what will happen and nothing is written until a person confirms. Read-only questions never change data, and OTA-sourced reservations are not editable through the connector at all.

### How granular is the access?

Fourteen scopes in seven read and write pairs across properties, calendar, bookings, missions, messages, guides and knowledge. A reporting assistant can hold the read half only, which is the grant to use when the job is answering questions rather than operating the account.

### Is this the same as the long-term rental connectors in this catalog?

No. Skywalk, AskRentAI, Tektolo and fixRAgent are built around leases and property management at monthly cadence. Nowistay is a nightly-rate business with five channels to keep in sync, cleaning turns between guests and guest conversations in the tool surface.
