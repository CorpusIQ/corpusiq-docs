---
title: "Ripplewatch MCP - Competitor Momentum vs Your Deals"
description: "A competitive analyst in Claude and ChatGPT that scores each competitor move against your positioning and your own won and lost deals."
category: Competitive Intelligence
stars: n/a (hosted, $29 a month plus prepaid usage)
added: 2026-11-05
source: "The mcp.so card ripplewatch at 2026-11-05T22:39:20.350Z (Data and Analytics, verified and featured, OAuth, remote); the official MCP registry record ai.ripplewatch/ripplewatch 0.1.0 published 2026-10-21T04:13:37Z with a streamable-http remote at https://www.ripplewatch.ai/api/mcp; HTTP reads on ripplewatch.ai/ (200, the ten scored inputs and the free read), /how-it-works (200, the four-step signal path), /pricing (200, the $29 plus usage terms), /connect/guide (200, the win-and-loss ingestion paths, the five momentum labels and the delivery schedule), /faq (200, the question set), /security (200, the assistant capability list, retention and encryption statements) and /sitemap.xml (200); the OAuth metadata at /.well-known/oauth-protected-resource/api/mcp and /.well-known/oauth-authorization-server (both 200); and one keyless JSON-RPC initialize against the endpoint returning HTTP 401"
relevance: ★★★
tags: [competitive-intelligence, win-loss, momentum, sales, positioning, oauth, remote-mcp, slack, claude, chatgpt]
last_updated: "2026-11-05"
---

# Ripplewatch MCP

**Most competitive intelligence answers what a competitor did. Ripplewatch answers whether it cost you a deal.** Every competitor gets one Momentum label built from hiring, pricing, product, press and funding activity, and every signal is scored against two private things the vendor's rivals do not hold: how you position yourself and who you sell to, and the actual reasons your deals were won or lost. The same price cut therefore lands as urgent for one company and as noise for another, and the reasoning is printed with the verdict instead of being left as an exercise for the reader.

```
Server type: Remote, Streamable HTTP
Endpoint:    https://www.ripplewatch.ai/api/mcp
Auth:        OAuth, browser sign-in and consent, authorization_code plus refresh_token
             through the vendor's Supabase authorization server, scopes openid, profile,
             email, phone, offline_access; approval screen names the client app
Registry:    ai.ripplewatch/ripplewatch 0.1.0, active, published 2026-10-21T04:13:37Z
Tools:       not published by name; the capability surface is stated in prose on /security
Pricing:     $29 a month plus prepaid usage from a $50 balance, first charge $79
Delivery:    Claude, ChatGPT or any remote MCP client; Slack, email and a daily digest
Vendor:      Ripplewatch, ripplewatch.ai
```

**Evidence tier.** A keyless `initialize` against `https://www.ripplewatch.ai/api/mcp` returned **HTTP 401** with `{"error":"Authentication required."}` and a `WWW-Authenticate` header pointing at `https://www.ripplewatch.ai/.well-known/oauth-protected-resource/api/mcp`. That protected-resource document answers **200** and names `https://www.ripplewatch.ai` as the authorization server with `bearer_methods_supported: ["header"]`. The authorization-server metadata answers **200** with an authorization code grant, a refresh token grant, dynamic client registration at `/oauth/clients/register`, and `code_challenge_methods_supported: ["S256","plain"]`. So the endpoint is real and gated, and nothing below is a live tool payload. What was measured: the 401 shape, both metadata documents, the registry record, and the vendor's own pages on capability, pricing, win and loss ingestion, delivery schedule and security. Tool names are not published anywhere the vendor exposes, so this entry documents the capability groups rather than a `tools/list` result, and says so instead of inventing names.

## What the assistant is allowed to do

The vendor states the permission surface plainly on its security page, which is more useful than a tool list for an operator deciding whether to connect: once approved, a connected assistant **can** read competitors, momentum labels, signals and trends, ask questions answered against your positioning and ICP, add competitors, and log won and lost deals and customer feedback. It **cannot** change billing or team settings. Every connected app is listed under Settings, Developer, and disconnecting one revokes its access immediately.

Two things follow from that shape. The write surface is narrow on purpose: the only things an agent can add are competitors and deal outcomes, which is exactly the private context that makes the scores specific. And the account boundary is the control that matters, since there are no per-scope tokens to issue. One server process against one account is the model.

## The ten inputs and the one number

Each signal is scored **-100 to +100**, and the scores roll into a single label per competitor. The vendor publishes the input list on its homepage, with the two integration-dependent feeds marked opt-in:

| Input | Note |
| --- | --- |
| Hiring | job postings and role changes |
| Pricing activity | pricing page and plan edits |
| Product changes | changelog and feature moves |
| Press and funding | announcements and rounds |
| Relevance trend | how much of it maps to your ICP |
| Win rate vs you | drawn from the deals you log |
| Review sentiment | review sites, negative and positive shifts |
| Buzz | Reddit and Hacker News |
| GitHub activity | opt-in |
| Ad activity | opt-in |

The consumer-facing band is stated on the homepage as **below -15 is Cooling, above +15 is Heating up, and in between is Steady**, over a -100 to +100 range. The help guide expands that to five labels in the product: **Heating up, Steady, Cooling, Gone quiet** and **Not enough history yet**, with an explicit low-confidence marker when a label is backed by thin data. That last part is the detail worth trusting: a competitor with two signals is not presented with the same certainty as one with twenty, and a competitor that goes dark is labelled Gone quiet rather than Cooling, because the vendor is saying quiet is not the same as harmless.

You also get your own momentum, computed from your win-rate and customer-feedback trends, which is the only figure here that is about you rather than about them.

## Why this earns an entry when three competitive intelligence guides already sit here

The neighbours are strong and they answer different questions. [Rivalize MCP](/hermes/mcp/servers/external/rivalize-mcp/) returns a one-call teardown of a competitor's positioning, pricing, ads, social, reviews and hiring, cited, built entirely from public web evidence. [Debriefing MCP](/hermes/mcp/servers/external/debriefing-mcp/) tracks named competitors, keeps evidence-backed signals, digests and battlecards. [Klarix Intelligence Engine](/hermes/mcp/servers/external/klarix-intelligence-engine-mcp/) scores ICP fit and writes displacement playbooks from cited public evidence. All three read the public web and hand back what they found.

Ripplewatch scores the public web against **your** closed deals. That is a different data join, and it changes the answer. A competitor cutting the entry tier by 30 percent is a fact for Rivalize and a fact for Ripplewatch, but only Ripplewatch can say that the last four deals you lost to them were lost on price at team sizes between 10 and 50 seats, so this is the change that will cost you the next four. The win and loss history is the moat, not the crawling.

The ingestion side is what makes that practical, and the vendor lists six paths: say it in plain English, fill the form under Settings and Data, upload a CSV exported from your CRM, forward or paste a deal list to the address shown in Settings, ask the assistant to read closed deals from a tool it can already reach, or run the whole thing on a schedule. HubSpot has an official connector for Claude and other assistants, and Gong's connector is read-only and returns call summaries instead of transcripts, so a competitor mention from a call is logged as a one-line summary by design. The vendor's own worked example is a Claude or ChatGPT recurring task: every Friday at 9am, pull the deals that closed lost this week with the reason for each, add them to Ripplewatch, and report how many were added.

## Where the output lands

This is a feed with no dashboard, and the split is deliberate. **Slack is the team surface**: high-relevance alerts as they happen, the weekly briefing at a day and time you choose, and a monthly recap on the first of the month that starts once the account is three weeks old. **The assistant is the analyst**: it is where a Slack alert gets turned into why it matters and what to do about it, and every Slack message carries an Ask Ripplewatch button that hands the question over. **Email is the fallback**: one alert email a day without Slack, the briefing on Mondays, and balance or billing alerts always to the account owner.

Alerts fire only on High relevance, never on a quiet day, and the weekly briefing is skipped on a quiet week. That restraint is the difference between a signal feed and a notification tax.

## What it costs, read from the pricing page

| Item | Terms |
| --- | --- |
| Platform fee | **$29 a month**, no seat fee, unlimited teammates on one account |
| Usage | prepaid balance, minimum **$50** top-up, drawn by answers and by each competitor tracked |
| First charge | **$79**, being the platform fee plus the starting balance, tax extra |
| Refund | platform fee and unused balance refundable within **30 days**; usage already spent is not |
| Free access | a competitor snapshot with no signup and no card; no free tier on the product itself |

The metering line is the one to read twice: **answers and each tracked competitor both draw from the balance**. That means the cost of the product scales with how many competitors you watch, not only with how often you ask, so a team that tracks a dozen competitors pays on the watching even in a quiet month.

## Limits, and the claims this pass could not verify

- **No published tool names.** The endpoint refuses anonymous calls and the vendor does not publish a tool reference, so the capability groups above come from its security page rather than from `tools/list`. Anyone who needs the exact tool names has to connect an account to get them.
- **No SOC 2.** The security page says so in its own first paragraph, and states that it only describes what is true now. That is honest, and it means an operator who needs an attested control environment should treat this as a small-vendor product.
- **Business context leaves your infrastructure.** The vendor states that relevant parts of your context and competitor signals are sent to Anthropic's Claude models per request, under terms the vendor describes as zero data retention. The scoring is not local, and no part of the product runs offline.
- **The interesting numbers are self-reported.** Momentum in the marketing example is an illustrative figure with made-up company names, and the vendor says so in the caption. There is no independent monitor of the label quality.
- **Deal history is only as good as what you feed it.** A CRM with no loss reasons produces a thin model, and the vendor's own page admits the read is general until deals are logged. The autopilot prompts are the fix, and they depend on the assistant having read access to the CRM, which on some ChatGPT plans is read-only and therefore cannot write anything back.
- **One account, one shared picture.** Teammates share the same competitors and deal history. There is no per-team or per-client separation, which matters to an agency running competitive work for several clients.
- **PKCE offers `plain`.** The authorization server advertises both `S256` and `plain`. A client that accepts `plain` gives up part of the protection PKCE exists to provide, so this is a place to insist on `S256` if you control the client.

## Common questions

### Does it replace Crayon or Klue?

It is aimed at a different buyer. The vendor's own framing is that enterprise CI platforms are priced for teams with a dedicated competitive function, while this is priced for a company where tracking competitors is nobody's full-time job. The honest comparison is the deal-history join: the question is whether the enterprise platform in front of you ingests your closed deals as scoring context, not whether it crawls more pages.

### Can I read anything without an account?

No. The connector requires an OAuth sign-in and the endpoint answers 401 to a keyless initialize. What is free is the separate competitor snapshot on the website, which needs no signup and no card, and is a read of public signals rather than a session against the MCP server.

### Does the assistant see my CRM directly?

Only if you connected that CRM to the assistant as well. Ripplewatch itself holds the deals you or your assistant log. The usual pattern is the assistant reading HubSpot or Gong and handing summaries over, which keeps the CRM credential with the assistant and leaves Ripplewatch holding outcomes rather than credentials.

### Is Slack required?

No, and it changes what you receive rather than what you can ask. Without Slack, alerts arrive as one email a day and the weekly briefing is emailed on Mondays. With Slack connected, alerts, the briefing and the recap post to a channel the whole team sees, and email becomes optional.

## How to start

1. Add `https://www.ripplewatch.ai/api/mcp` as a custom connector in Claude or ChatGPT, sign in, and approve the client on the consent screen. In ChatGPT this goes through developer mode, which the vendor labels as beta.
2. Add the competitors you actually lose deals to, not the ones in the analyst deck. Two or three is enough for the first read.
3. Log three recent deals in the customer's own words, including the ones you won. Loss reasons are what sharpen the relevance scoring.
4. Ask what changed and why it matters, then read the first weekly briefing before adding more competitors, so the balance is spent on watching things that moved.
5. If more than one person uses it, connect Slack and agree who logs deals. The email path reaches the account owner only.
