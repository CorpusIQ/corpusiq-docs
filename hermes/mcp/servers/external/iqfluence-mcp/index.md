---
title: "IQFluence MCP - Creator Vetting and Media Plans"
description: "Search 455M Instagram, TikTok and YouTube creator profiles, check fake followers and audience overlap, and build a costed media plan."
category: Marketing
stars: n/a (hosted platform, no public repo)
added: 2026-10-21
source: "mcp.so /feed page 1 (card iqfluence-mcp, posted 16:27Z)"
relevance: ★★★
tags: [influencer-marketing, creator-vetting, audience-overlap, fake-followers, media-planning, instagram, tiktok, youtube, remote-mcp]
last_updated: "2026-10-21"
---

# IQFluence MCP

**Creator spend fails for two reasons that both surface before the contract: the followers are not real, and three of the five creators reach the same people. This server prices and checks both before a budget is committed.**

```
Server type: Remote (Streamable HTTP)
Endpoint: https://mcp.iqfluence.io/mcp
Auth: OAuth 2.1 in the browser, or an API key for scripts and CI
Live check: unauthenticated POST initialize returned HTTP 401 {"error":"invalid_token"}
Authorization server: /.well-known/oauth-authorization-server returned HTTP 200 with authorize, token, register and revoke endpoints, authorization_code and refresh_token grants, PKCE S256
Vendor: IQFluence (iqfluence.io)
```

## Why This Matters for Operators

An influencer budget is approved on a projection that nobody can check: the audience is somewhere else, the engagement rate is self-reported and the overlap between two creators is invisible until both invoices arrive. The three questions that decide whether a campaign works are all answerable from profile and audience data, and all three are usually answered by intuition instead.

IQFluence puts a 455M profile index behind the assistant and charges per answer rather than per seat, which changes the order of work: the search is free at three rows, and the money is spent only on the creators that survive the first look.

## What It Actually Does

Fifteen tools are named in the vendor's own docs, with the credit cost stated for each paid step:

- `search_influencers` finds Instagram, TikTok and YouTube creators by niche, location, size, engagement and audience demographics. The first 3 results come back in full and the rest are hidden; `unlock_search_results` reveals them at 0.02 credits per account.
- `get_influencer_report` is the vetting surface: audience and its quality, fake-follower signals, engagement, growth, content and contacts, at 1 credit, and free if the same report was bought in the last 30 days.
- `compare_influencers` puts 2 to 5 creators side by side at 1 credit per creator without a recent report, and `audience_overlap` returns shared audience and unique reach at 1 credit per calculation, free when a creator has no audience data.
- `build_media_plan` returns expected views, engagements, CPM and cost per engagement at 1 credit per creator without a recent report, which is the projection an approval actually needs.
- Discovery and research: `get_creator_posts` and `get_hashtag_posts` (0.02 credits a page), `get_post`, `get_post_comments`, `get_contacts` (0.04 credits per account with contacts).
- Account surface: `get_account_balance`, `list_campaigns`, `get_campaign_stats`, `list_my_reports`.

Two behaviours matter more than the tool list. The assistant states the cost of a paid step before running it and asks first whenever a task would cost more than 5 credits, and a daily credit limit can be set per assistant key. Every paid request is written to the account's request history with its parameters, cost and time.

## Installation

```
claude mcp add iqfluence-mcp --transport http https://mcp.iqfluence.io/mcp
```

The client detects OAuth and opens a browser to sign in. Codex, Cursor, VS Code, ChatGPT and Gemini CLI are documented with their own snippets at https://iqfluence.io/docs/mcp. For scripts and CI, create a key in Profile and send it as a bearer token; requests through MCP still spend credits.

## Limits Worth Knowing

- The tool count and per-call costs above come from the vendor's documentation. The endpoint authenticates before it will answer `tools/list`, so an unauthenticated probe confirms only that it is live and gated.
- Contact data covers public channels. Direct messages and private details are not part of the surface.
- Plan credits do not roll over, and top-ups are valid for 3 months, so a large annual booking is money that expires.
- The first 3 rows of a search are free by design. A search that returns 200 creators is a paid unfold, not a free list.
- The platform is priced for teams that buy creator data regularly. At $199 a month it is not a one-off check, and the free trial is 5 credits once per account.

## Pricing

| Plan | Monthly | Yearly (20 percent off) | Credits |
|---|---|---|---|
| Starter | $199/month | $1,910.40 | 300 |
| Pro | $299/month | $2,870.40 | 500 |

Top-ups are $0.79 per credit from 50 credits with an active plan, valid for 3 months. The trial gives 5 credits on the first connection, valid for 30 days, once per account. Upgrading from Starter to Pro is prorated.

## FAQ

### What does one vetted shortlist actually cost?
A search is free for its first 3 rows. Unlocking a page of hidden rows is 0.02 credits per account, a full report on a creator is 1 credit, and a media plan is 1 credit per creator without a recent report. A shortlist of ten creators checked properly is therefore around 10 credits plus unlocks, which is under $8 at the top-up rate and under a tenth of a Starter month.

### What is the audience overlap check for?
Five creators in one niche can share most of the same followers, and reach is then counted twice while the budget is spent twice. Overlap returns shared audience and unique reach per creator, which turns a list into a set with a real combined reach.

### Are the fake-follower checks a guarantee of audience quality?
No. They are signals derived from audience and engagement patterns, and they are strongest when they disagree with what a creator reports. Treat a clean report as a reason to look further, not as proof.

### Why catalogue this when creator finders were held before?
Creator-finder entries were held twice against thin scraper tools that returned a name and a follower count. This is the first surface here where the vetting itself is priced per answer, and where audience overlap and a costed media plan come from the same index. The gap is named rather than closed, because a denser creator class would make this one redundant.

## See Also

- [ViewsBase MCP - Creator Payouts for Clipping Campaigns](/hermes/mcp/servers/external/viewsbase-mcp/)
- [UXArmy MCP - Run User Research From the Assistant](/hermes/mcp/servers/external/uxarmy-mcp/)
