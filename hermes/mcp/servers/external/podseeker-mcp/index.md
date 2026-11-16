---
title: "Podseeker MCP - Podcast Booking Database"
description: "A hosted MCP server over a podcast booking database: difficulty, expected credentials, recent guests, contacts and Client Fit."
category: Marketing
stars: "0 (the repository holds the public description and example config; the server itself is hosted)"
added: 2026-11-16
source: "the chatmcp/mcp-directory submission queue entry #7471 filed 2026-11-16T17:36:29Z, read against the vendor repository README, the vendor API documentation and a live 401 at the endpoint on 2026-11-16"
relevance: ★★
tags: [pr, public-relations, podcast-booking, media-list, contacts, prospecting, marketing, hosted-mcp]
last_updated: "2026-11-16"
---

# Podseeker MCP

**A podcast pitch fails on three facts nobody publishes together:** whether the show takes guests at all, how hard it is to book, and which address belongs to the person who books it. A search engine returns the show's website. A directory returns its category and an episode count. Neither answers the question the operator actually has, which is whether this show is a fit for this client and who to write to.

Podseeker is a podcast database whose product is that answer. Every show carries **booking difficulty**, the **credentials it expects of a guest**, its **recent guests and what they talked about**, and **known contacts** with a role and a confidence level, with a contact-search tool for the shows that have nobody on file. The database is filtered the way a booking workflow runs: active shows, guest-friendly shows, listener estimates, audience location and recent activity. **This pass could not drive it** (the endpoint refuses anonymous callers by design), so the tool surface below is read from the vendor's own README table and its API documentation rather than from a `tools/list` response, and the evidence tier says so plainly.

```
Server type:   remote Streamable HTTP (hosted)
Endpoint:      https://app.podseeker.co/mcp
Registry:      co.podseeker/podseeker, versions 1.0.0 and 1.0.1 published
Auth:          OAuth 2.1 with dynamic client registration, or an API key as a bearer header
Tools:         19 (documented in the vendor README)
Repo:          github.com/podseeker/podseeker-mcp (MIT, 0 stars, created 2026-11-16; README, server.json, example config)
Pricing:       100 free credits, then US$99 a month
Listed on:     the mcp.so submission queue as #7471
```

## The evidence tier

**Documented, not driven.** `initialize` on the endpoint answered **401** with a body that names both routes in: *Connect Podseeker from your assistant, or send an API key*, followed by the key page at `app.podseeker.co/api`. That is a liveness signal and not a failure, the same reading this catalog applies to every OAuth-gated vendor server: the endpoint exists, it wants a credential, and the credential is self-serve.

What was verified directly: the endpoint answers **401** to an anonymous `initialize`, the official registry carries **two** records (`co.podseeker/podseeker` **1.0.0** and **1.0.1**), the repository exists under the vendor's own organisation with an **MIT** licence and a README that enumerates all **19** tool names, and the vendor's API documentation and pricing page are live. What was **not** verified: any tool's actual response shape, any argument name, the credit cost of any individual call, or the accuracy of a single booking-difficulty score. Those gaps are stated in Limitations rather than filled in from marketing copy.

## The tool surface

The README publishes the full table. Grouped by the job it does:

| Job | Tools | What they cover |
|---|---|---|
| Find shows | `search_podcasts`, `get_podcast`, `lookup_podcast`, `similar_podcasts` | Search with the app's filters, open a show's full profile and contacts, resolve a show from its Apple Podcasts ID, and expand from one good show to its neighbours. |
| Find people | `enrich_podcast_contacts`, `get_enrichment` | Research direct host and producer emails for a show that has nobody on file, then check the result of that search. |
| The client book | `list_clients`, `get_client`, `create_client`, `update_client` | The people being booked, held so a recommendation can be made against a real profile rather than a prompt. |
| Match a client to shows | `recommend_podcasts`, `get_recommendations` | Recommendations for a client, each carrying a **Client Fit** rating and the reason for it. |
| Shortlists | `list_media_lists`, `get_media_list`, `create_media_list`, `update_media_list`, `add_to_media_list`, `remove_from_media_list` | Media lists that are the same objects the team sees in the Podseeker app, so an agent-built shortlist is a shared artifact rather than a chat transcript. |
| Account | `get_usage` | The credit balance. |

The documented filters are the part that separates this from a podcast search engine: **topic**, **guest-friendly**, **booking difficulty**, **listener estimates**, **audience location** and **recent episodes**. A search that requests shows taking guests, with an email on file and a low booking difficulty, is a qualified shortlist in one call rather than three tools and a manual sort.

## What a contact record carries

The vendor states that every contact comes back with a **role** and a **confidence level**, which is the field that decides what a workflow does next: a host email at high confidence can be queued for a draft, a producer email at low confidence can be routed to enrichment first. The enrichment tool exists precisely for the shows where the profile has the wrong person or nobody at all, and `get_enrichment` polls that research instead of returning a promise.

The server **does not send email**. Pitching stays in the Podseeker app, so the write surface is the client book and the media lists rather than an outbound mail path. For an operator wiring an agent into a PR workflow, that boundary is easier to defend internally than a connector that can mail a stranger on its own.

## Pricing and the credit model

**100 free credits, then US$99 a month.** The vendor's phrasing is that each tool uses the same credits as its equivalent API endpoint, while clients, media lists and usage are free. In practice that means the discovery and enrichment calls are the ones that cost, and the bookkeeping around them does not, which is the right shape for a workflow that searches widely and saves narrowly. The credits are attached to an account or an organisation's API plan rather than to the MCP connection, so a team can share one plan across several agents.

## Installation

Claude Code, with an API key:

```bash
claude mcp add --transport http podseeker https://app.podseeker.co/mcp --header "Authorization: Bearer YOUR_KEY"
```

Any client that takes a JSON config:

```json
{"mcpServers": {"podseeker": {"type": "http", "url": "https://app.podseeker.co/mcp"}}}
```

The vendor documents the OAuth path for Claude and ChatGPT as a custom connector: paste the server URL, choose OAuth where the client asks, approve in the Podseeker window that opens, and the connection carries the account's plan. API keys are created at `app.podseeker.co/api`.

## Limitations

- **Not driven.** No response shape, argument name or credit cost in this guide was observed from a live call. The tool list is the vendor's README table, and the scoring fields (`Client Fit`, booking difficulty, listener estimates) are the vendor's own constructs rather than measured quantities.
- **Credits are consumed by the useful calls.** Search, profile opens and contact enrichment are the paid surface, so an agent that loops over a topic list can spend a month of credits in a session. Budget the loop before wiring one up, the same advice this catalog gives for any credit-metered server.
- **Estimates presented as ratings.** Booking difficulty and listener figures are the vendor's estimates and the guide does not restate them as facts about a show. The Client Fit rating is a model output with a stated reason attached, which makes it auditable but not authoritative.
- **One vertical and one asset class of data.** Podcasts only; there is no journalist, newsletter or YouTube channel coverage in the tool list, which is the line between this server and the broader media-contact products.
- **A new repository behind a product that is not new.** The public repo was created on **2026-11-16** and holds listing files and example configuration, so its **0** stars say nothing about the product's age; the vendor states the database has powered podcast outreach since 2021, and that claim is the vendor's rather than something this pass could check.

## See Also

- [Media List MCP - Journalist and Podcast Contacts](/hermes/mcp/servers/external/media-list-mcp/) for the broader pitch-contact surface across journalists, editors and creators
- [Audiogram API MCP - Podcast Search and Transcripts](/hermes/mcp/servers/external/audiogramapi-mcp/) for podcast search and transcripts where the question is what was said rather than who to book
- [Podcast Sponsorship Discovery MCP - Lead Generation](/hermes/mcp/servers/external/podcast-sponsorship-mcp) for the sponsor side of the same medium
