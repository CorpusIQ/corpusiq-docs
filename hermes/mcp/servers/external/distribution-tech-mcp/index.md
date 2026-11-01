---
title: "distribution.tech MCP - Book X Creator Posts From the Chat"
description: "A creator distribution marketplace exposed as tools: find the X creators your buyers follow, price a post before you commit, sign a plan inside a spending mandate, and get proof for every placement. Guest tier needs no key."
category: Marketing and Growth
stars: n/a (marketplace, per-placement pricing)
added: 2026-10-31
source: "The chatmcp/mcpso submission issue #6523 filed on 2026-10-31 at 22:46:13Z; a keyless JSON-RPC initialize, tools/list, guest_status, inventory and resolve_audience against https://app.distribution.tech/api/mcp/guest; one failed plan_quote_guest call; and HTTP reads on distribution.tech, distribution.tech/docs, distribution.tech/docs/agents and distribution.tech/pricing"
relevance: ★★★
tags: [creator-marketing, x-twitter, distribution, influencer-marketplace, campaigns, launch, spending-mandate, guest-tier, remote-mcp, streamable-http]
last_updated: "2026-10-31"
---

# distribution.tech MCP

**Every founder who has bought a post has bought it the same way: a DM, a screenshot of a rate card, a PayPal transfer, and no way to prove the post ran. This connector is that market with a price, an approval step and evidence attached, exposed to an agent as tools.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://app.distribution.tech/api/mcp/guest   (no key)
             https://app.distribution.tech/api/mcp         (API key or OAuth)
Auth:        guest tier keyless; buying needs an approved brand and a key
Tools:       6 on the guest surface, 22 documented on the account surface
Limits:      60 requests per 10 minutes per client address (guest)
Pricing:     one all-in price per post, one total per plan
```

## What it does

The guest surface is the first half of the deal and it is readable without an account:

- `inventory` answers how much of the network is on sale today per channel, as counts only, never names: verified, listed, bookable, and priced units.
- `resolve_audience` takes a described profile (product, audience, geography, at least one of product or audience) and returns the segments it matches, the regions it resolves to, the coverage per channel and whether that coverage is thin.
- `plan_quote_guest` estimates the all-in price range per post in one format (`post`, `quote` or `thread`) across every creator on sale now, and multiplies by the number of posts named (1 to 50).
- `guest_status` reports what the connection can do without a key, the guest limits, and the claim path.
- `brain_get` returns the saved company context, which as a guest is version 0 and empty.
- `feedback_send` is stated to need an account and answers with a claim rather than sending.

The account surface, documented at `/docs/agents`, is 22 tools that carry a campaign from conversation to evidence: `creators_search`, `creator_get`, `creator_ask_price`, `plan_quote`, `create_campaign`, `plan_add_creator`, `plan_remove_creator`, `plan_move_dates`, `plan_swap_creator`, `set_creator_guidelines`, `approve_plan`, `archive_campaign`, `rename_campaign`, `delete_campaign`, `campaign_status`, `evidence`, `results`, `brain_get`, `inventory`, `resolve_audience`, `feedback_send` and `feedback_list`.

## What this pass measured

`initialize` on the guest endpoint returned **HTTP 200** in 0.34 seconds, `protocolVersion` `2025-06-18`, `serverInfo` name `distribution` at version **1.37.0**, with `tools.listChanged`, resources and prompts all advertised. `tools/list` returned 5,393 bytes and all **six** guest tools with full schemas.

`guest_status` then described its own limits precisely: `signed_in: false`, `access: "guest"`, `answers_now` listing five tools, `needs_account` listing `feedback_send`, a tool-call limit of **60 per 10 minutes per client address**, and a separate limit of **3 `plan_quote_guest` calls per 7 days per client address**. That second limit is the important number for anyone planning to use this as a price research tool: three quotes a week.

`inventory`, computed at `2026-11-01T04:02:35Z` with coverage as of `04:02:33Z`, returned one channel, `x_creators`, `sale: "live"`, `level: "strong"`, with **1,005** verified nodes, **1,005** listed, **86** bookable now and **255** posts carrying a current price.

`resolve_audience` on a described profile (a B2B AI data layer for ecommerce and SaaS operators, US) resolved to three segments, `ai` (AI builders and early adopters), `saas_b2b` (B2B software buyers and operators) and `finance` (Finance and investors), region `us`, `unresolved: false`, and then narrowed the inventory to **792** approved creators, **63** bookable and **187** priced posts, with `thin: false`. The gap between 1,005 and 792 is the whole argument for the tool: an audience filter removed 213 creators who exist but do not reach that audience.

`plan_quote_guest` failed. The call returned `isError: true` with the text `unavailable: The network could not be read just now. Try again.` No price was obtained, one of the three weekly attempts was spent, and the defect is recorded below rather than papered over.

## The containment worth reading twice

The spending model is the reason this entry is worth a guide rather than a line in a list. Per the agent documentation, a key carries a **mandate** that caps what it can spend, signing a plan produces a payment link **inside that mandate**, and a brand cannot buy at all until it has been reviewed and approved. So the failure mode an operator fears, an agent committing a budget because it was told to "get us some reach", is bounded by a number a human set before the agent ran.

The second containment is the guest tier's own design: counts, not names. A guest can learn how deep the network is and how well it matches an audience without reading a single creator's identity, and creator names arrive on a plan before signing, with two alternates and the ability to swap a placement.

## The operator decision this answers

Paid distribution is the leg most product teams cannot plan, because the unit price is opaque until someone answers an email. Three numbers decide it, and this surface returns all three before a human talks to anyone: how many creators reach the audience (792), how many are purchasable today (63), and how many posts are actually priced (187). A thin market is visible as a `thin: true` and a low bookable count rather than discovered after a week of DMs.

The workflow is the interesting part for an agent-first operator: the agent reads coverage for a described audience, asks the price in the format it wants, assembles a plan with named creators and alternates, and stops at an approval. That is a procurement process a founder can audit, which is more than can be said for a DM thread and a bank transfer.

## Where it sits in this catalogue

Nothing here does what this does. The nearest entries touch one edge of it:

- [B2B Creators MCP](/hermes/mcp/servers/external/b2b-creators-mcp/) is a creator and expert sourcing surface, which answers who exists, not what a post costs or whether it ran.
- [PR CY MCP](/hermes/mcp/servers/external/pr-cy-mcp/) is press and media placement rather than creator placement.
- The social scheduling and publishing entries ([Blog2Social](/hermes/mcp/servers/external/blog2social-mcp/), the bulk publishers) post content you already own to accounts you already control, which is the opposite side of the market: owned distribution versus paid distribution.
- The ad connectors buy impressions inside a platform's auction with a self-serve interface and no human seller, so there is no approval or proof step to model.

## What this pass did not establish

The price is unmeasured, and it is the number that matters. `plan_quote_guest` returned an `isError` payload on the first attempt, and two of the three weekly guest quotes remain, so the all-in range per post is an unknown rather than a finding. Everything about the buying half is documentation: no brand approval was sought, no key was created, so `create_campaign`, `approve_plan`, `evidence`, `results` and the mandate enforcement are read from `/docs/agents` and not driven.

Also unread or unverified: what share of a placement's price reaches the creator; whether `evidence` is a screenshot, a link, a platform metric or all three; whether the 3-campaigns-a-day limit applies per brand or per key; and whether the 1,005-creator inventory is audited for follower authenticity, which the site's "reviewed creators" language implies and this pass did not test.

## FAQ

### Does it need an API key?
Not to read the market. The guest endpoint is keyless and returns coverage, audience fit, price estimates and status. Buying a placement needs an approved brand plus an API key from the workspace, or OAuth.

### Can an agent spend without approval?
It can sign a plan, and signing produces a payment link rather than a charge, inside a mandate the brand set on the key. Publishing a campaign to the network is gated on brand review, and the documented flow puts `approve_plan` after a plan exists, with `evidence` and `results` after it runs.

### Why did the price quote fail?
`plan_quote_guest` returned `unavailable: The network could not be read just now. Try again.` That is a transient-service error at the vendor, not a permissions error, and it cost one of three weekly guest quote attempts. Retry later in the week rather than in the same minute.

### How current is the inventory?
The response stamps both `computed_at` and `coverage_as_of`. In this call they were 2.4 seconds apart, so the counts are a live read rather than a nightly snapshot, and a bookable count that moves between two calls minutes apart is a marketplace, not a bug.

### Is this the same as buying ads?
No. Ads are an auction with self-serve targeting and no seller. This is a marketplace of named humans whose posts are priced individually, with approval, mandate and per-placement proof.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the full catalogue this entry belongs to
- [B2B Creators MCP](/hermes/mcp/servers/external/b2b-creators-mcp/) - who exists, rather than what a post costs
- [PR CY MCP](/hermes/mcp/servers/external/pr-cy-mcp/) - placement in press rather than in creators
- [Blog2Social MCP](/hermes/mcp/servers/external/blog2social-mcp/) - owned distribution, the other side of the same budget line
