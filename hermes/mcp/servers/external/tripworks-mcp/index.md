---
title: "TripWorks MCP - Tour Operator Bookings and Manifests"
description: "A tour and activity booking platform exposed over MCP: day-of manifests, waivers, reports and check-in, with 50 scopes and a preview before every change"
category: "Travel & Hospitality"
stars: "n/a (hosted, OAuth only, enabled per account under Setup Integrations)"
added: 2026-11-10
source: "the mcpservers.org canonical for /servers/tripworks-mcp, the official registry record com.tripworks/tripworks 1.0.2 published 2026-11-08T23:14:34Z, the vendor help page help.tripworks.com/integrations/connect-tripworks-mcp-to-your-ai-assistant, and the endpoint itself, where a keyless initialize answered 401 with a JSON-RPC error object and the protected-resource and authorization-server documents returned 200"
relevance: ★★★
tags: [travel, tours, activities, bookings, manifest, waivers, check-in, reports, oauth, streamable-http, remote-mcp]
last_updated: "2026-11-10"
---

# TripWorks MCP

**The question a tour operator asks at 09:40 is not how many bookings came in. It is who is on the 10:00 departure, who has not signed the waiver, and did anyone check in.** TripWorks is an AI-native booking and CRM platform for tour, activity and attraction operators, and its MCP server is wired for that day-of question rather than for the reporting dashboard: trips with their orders and guests, the day manifest with check-in and waiver status, a report runner, the audit log, and the phone calls the AI call agent recorded.

```text
Server type:  Remote (Streamable HTTP)
Endpoint:     https://mcp.tripworks.com/mcp
Auth:         OAuth 2.1, authorization code with PKCE (S256)
Scopes:       50 published in the authorization-server metadata
Registry:     com.tripworks/tripworks 1.0.2, published 2026-11-08T23:14:34Z
Enablement:   per account, Setup Integrations > AI Assistants
Probe:        401 plus the protected-resource document, tools not driven
```

## What the endpoint says about itself

A keyless `POST initialize` answered **401** with a JSON-RPC error object, `-32001 Missing or malformed Authorization header`, and a `WWW-Authenticate` header naming `resource_metadata="https://mcp.tripworks.com/.well-known/oauth-protected-resource"`. Following that exact path returned **200** with the resource `https://mcp.tripworks.com/mcp` and one authorization server, the same host. The authorization-server metadata at `/.well-known/oauth-authorization-server` answered **200** and is the most informative document in this pass:

```text
issuer              https://mcp.tripworks.com
authorize           /oauth/authorize
token               /oauth/token
registration        /oauth/register          (dynamic client registration)
grants              authorization_code, refresh_token
PKCE                S256 only
token auth          none                     (public client, no secret)
scopes              50
```

Fifty scopes is the product brief in the vendor's own nouns: `bookings.read` and `bookings.write`, `manifest.read`, `waivers.read` and `waivers.write`, `waiver-types`, `trips`, `trip-sources`, `trip-notes`, `experiences` and `experience-timeslots` with their timeslot-config pair, `resources` with blackouts implied, `restrictions`, `gift-cards`, `promo-codes`, `reviews`, `resellers`, `customers`, `locations`, `knowledge-bases`, `payments.read`, `phone-calls.read`, `reports.read`, `analytics.read`, `audit-log.read`, `api-logs.read`, `widgets` and `widget-logs`, `user-avatars`, plus `account.read`. Three of those are read-only by construction and worth naming, because they bound what an agent can reach: `manifest.read`, `payments.read` and `audit-log.read` have no write counterpart in the published set.

## What the vendor documents, labelled as vendor copy

The help article states that turning the feature on requires the **Setup integrations catalog** permission, which ships with the built-in Owner group, and that if the AI Assistants card is absent it may not be enabled for that account at all. The server URL is one address for every account, because the account is chosen at approval time, not in the URL.

The documented capability table, in the vendor's own areas:

```text
Trips and bookings   look up trips with orders and guests, a booking's products,
                     add-ons, waivers and custom fields; check guests in or
                     change status; mark waivers signed; add or remove guests
Trip notes           read a trip's notes, add one
Day-of manifest      who is booked on each departure, with check-in and waiver
                     status
Reports and analytics run a report and download the result; counts, totals,
                     averages and period comparisons
Experiences          look up, create, edit, delete
Locations            look up, create, edit
Customers            look up, create, edit, delete
Booking restrictions look up, create, edit
Resources            assign and unassign on departures, create or clear blackouts
Resellers            look up and edit
Reviews              look up guest reviews
Phone calls          list calls and tags, read a call summary, transcript and
                     the questions and tips found in it
Promo codes, trip sources, team members   look up and review
Audit log            what changed, when, and which team member changed it
Account settings     settings and guest policies
Search               keyword search across trips, bookings, customers, gift
                     cards, payments, resellers, calls, notes, voucher codes
```

Two mechanics in that table deserve to be read as design rather than as features. **Filtering and totals are server-side**: the vendor states that listing tools filter by fields such as email, name or date, and that counting, summing, averaging and period comparison run across matching records, which is what makes "customers with a gmail address" and "how many guests this month" answerable without the model paging the whole table. And **the report link expires in 15 minutes**, which the article says plainly and which a scheduled report job has to plan for.

## The permission model is the interesting part

Three layers, and they are all stated:

**The connected person's permission group.** The connection runs as the person who approved it and can never exceed that group. The vendor publishes the per-area permission, so the mapping is checkable rather than implied: viewing trips needs View Trips to read and Edit bookings on trips or Change existing trips to write; the manifest needs View the daily manifest; reports need the View reports module plus the permission for each report; experiences need Manage activities or experiences; calls need Manage company profile to list and Playback and analyze phone calls to open a single call.

**The approval choice at connect time.** The approval screen offers Read access, Write access, or both, and the article is explicit that leaving Write unchecked stops every create, edit and delete even where the person's own permissions would allow it. That is a per-connection narrowing, which is the right shape: the same human can have a writing assistant in one client and a read-only one in another.

**Preview before write.** Every create, edit and delete returns a preview, and nothing is saved until the assistant repeats the request with a confirmation. The vendor also states the honest limit: deleting a customer or an experience cannot be undone.

There is a fourth control that no MCP server in this catalog has offered before in these words: the article frames the choice of protocol by **who is acting**. With MCP a real person is always behind the connection, so requests follow that person's permissions and need that person's approval; an API key or a Zapier connection is a standing credential with nobody approving each call. The same vendor publishes all four surfaces, and it recommends MCP when a person is in the loop and the others when software runs alone. For an operator deciding which door to open, that is the clearest statement of the MCP boundary this catalog has recorded.

## The class it enters, with the owners named

This is the first **tour and activity operator** surface here. The nearest neighbours sit at different points of the travel workflow rather than on this one:

- [Nowistay MCP](/hermes/mcp/servers/external/nowistay-mcp/) is a property management system and channel manager for short-term rentals, where the unit is let by the night and the guest is one record. A tour operator sells a departure with a manifest, a capacity and a waiver per person.
- [Vocenya MCP](/hermes/mcp/servers/external/vocenya-mcp/) handles business calls, leads and bookings, which is the inbound half and not the day-of half.
- **Meridian Dispatch** was held on the trip planning class, and planning an itinerary is a different job from running a departure that leaves in twenty minutes.
- **Cotlet** reaches the apps that have no API through a browser, and its typed half covers salon, trades and field-service front desks. A booking platform that publishes its own MCP endpoint does not need a browser to be reached.

What none of them carries is the manifest: the per-departure list with check-in state and waiver state, which is the document an operator prints and a guide checks at the dock.

## Limits, stated as limits

The connection is per account and gated twice: an account admin must have the Setup integrations catalog permission to switch AI Assistants on, and the feature may not be enabled for every account yet, with the vendor directing a customer to support if the card is missing. The server was measured to the handshake and the two metadata documents only, because the tool list sits behind the OAuth gate; every tool name and area above is vendor copy, not a driven list. The published scope set is broad and includes deletes on customers and experiences, so Read access first is the sane default rather than a cautious one. And anything the assistant reads is passed to the assistant's own platform under that platform's terms, which the vendor states in the article and which is true of every MCP connector in this catalog.

## Frequently asked questions

### What is the TripWorks MCP server URL?

`https://mcp.tripworks.com/mcp`, one address for every account, copied from the AI Assistants page under Setup Integrations. The account is selected when the connection is approved, not in the URL.

### Can the assistant change bookings without asking?

Not without a confirmation. Every create, edit and delete returns a preview and nothing is saved until the request is repeated with approval. If Write access was left unchecked at connect time, no change of any kind is possible.

### Which guests were on a departure and who has not signed a waiver?

That is the manifest tool's job, documented as who is booked on each departure with check-in and waiver status, beside the booking tools that can check a guest in, change a status, mark a waiver signed, and add or remove a guest on a trip order.

### Does an MCP connection see more than the person does?

No. The connection runs as the person who approved it and inherits that permission group, so a team member moved to a smaller group loses the same access in the assistant. That is the vendor's stated behaviour and it is the reason the per-area permission table is published.

### How long does a downloaded report stay valid?

Fifteen minutes. The report tool starts the report and returns a download link, and the vendor states that the link expires, so a job that needs the file has to fetch it in the same turn.
