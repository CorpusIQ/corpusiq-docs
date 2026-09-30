---
title: "MCP Server Discovery - September 30, 2026 (Evening)"
description: "Evening sweep of the mcp.so feed and mcpservers.org: one new server catalogued with an integration guide, plus core listing verification."
category: mcp-directory
tags: [mcp, discovery, sweep, directories]
---

# MCP Server Discovery - September 30, 2026 (Evening)

**Date:** September 30, 2026 (evening slot)
**Sources:** mcp.so /feed (30 server blocks, direct fetch with browser user agent) and mcpservers.org /all pages 1-2 via the r.jina.ai reader proxy, with three detail pages fetched.
**Result:** 1 new business-relevant server catalogued with a guide. Catalog 761 to 762 servers, guides +647 to +648.

## Discovery

Feed-order recency against the midday anchor: the midday anchor was the OceanAlt AML entry, and the entries ahead of it were re-read this cycle. Two entries above the anchor are genuinely new since the midday sweep.

- **PixelDojo** - brand new, sitting at the top of the feed. Catalogued (see below).
- **TrackIQ** - the midday sweep queued a detail fetch for this one and it was completed this cycle. It is a real product (Amazon seller and vendor analytics with a sponsored Ads surface, one-click Amazon OAuth, remote server) but the publishable facts did not hold up well enough to write a guide: the tool count contradicts between the vendor page (30 skills) and the directory listing (sixteen tools), the transport type and the endpoint URL are not published anywhere public, and the install command is behind a registration wall. Held rather than catalogued. It is a reasonable candidate for a future cycle if the vendor publishes an endpoint and a stable tool reference.
- **LinkBunny** - evaluated from the /all pages. Local stdio MCP server for contextual link building, five tools plus a bundled guidance resource, published docs, npm package at a pinned version, MIT. Genuinely well documented, but it is a link-building utility that points at a single marketplace rather than a data or operations surface, so it lands in the SEO-utility class already covered by the outreach and backlink entries on the catalog. Disposed LOW.

Everything else in the feed and on /all pages 1-2 matched a prior disposition, checked against the sweep index and the `external/.last-sweep` ledger.

## New servers catalogued

- **PixelDojo MCP** (Generative media for agents) - remote Streamable HTTP at `pixeldojo.ai/mcp` with OAuth browser sign-in or a `pd_` bearer key, and a local stdio mode through `npx -y @pixeldojo/mcp` on Node 18 or newer. Nineteen tools ship in the server and eighteen are offered over the hosted endpoint, since `pixeldojo_upload` needs local filesystem access. Single-shot tools cover generate, edit, upscale, character and audio; studio tools wrap multi-step pipelines for product video ads, campaigns, short films, storyboards and faceless explainer episodes; library and workflow tools reuse what was produced, and `pixeldojo_status` picks up renders that outrun the 30-second wait. MIT licensed, `blovett80/pixeldojo-mcp`, created the same day, so there is no community signal yet. Credit pricing runs 10 to 50 USD per month, and asset URLs expire one hour after creation. Catalogued relevance TWO because the class is well covered, but the endpoint, the auth model and the full tool list were all verified against source rather than inferred.

## Core listing verification

- **mcpservers.org:** LISTED. Direct curl returns the Cloudflare 403 wall; the reader proxy returns the CorpusIQ MCP page, so the listing is live.
- **glama.ai/mcp:** LISTED. The `@corpusiq/corpusiq-docs` slug redirects to the canonical listing.
- **PulseMCP:** LISTED. Reader proxy title reads Official CorpusIQ MCP Server.
- **smithery.ai:** registry entry present. No submission path exists (login-walled) and the listing is unstable, so no action taken.
- **mcp.so:** NOT LISTED. The search SSR payload carries no server cards; the account-level instant moderation state from August 12 still stands, so no resubmission was attempted.

## Also identified (not catalogued)

TrackIQ (held pending a published endpoint and a stable tool reference; see above), LinkBunny (SEO link-building utility, LOW), Agent Cody (Slack-native hosted assistant from 479 USD per month, with no published MCP endpoint or protocol surface, so a protocol integration guide would be inaccurate), plus the feed and /all repeats already disposed by the September 30 morning and midday sweeps, the September 29 sweeps and earlier ledgers: prodready, uplika, How To Make Money On Snapchat, MemeSwap MCP, MeroFoundry, Rebbel, Dumpster Controls, Unipile, fAlpha, TokElements, GAIP Agents, HeyLead, elmah.io MCP, trip1, Webshare, systemHUB, AccountHub, AgentGrown, ohmyho.st, EQIQs, Selfstorming, Uxia, Texas RRC Wellbore Intelligence, TinyFish, pdf.net, SMAT, HaberChat, Agent Credit Bureau, ECRP, Well Prepped Life, Beemm Vision, MX Verdict, AnswerLine, Dive Kit, Robozukan, SubmitraX, Tempi, Garmin, health-os, MateMCP, Swebsy, NoMac, Monocrawl, betterimage, Hookova, PDFHaul, LiteLambda, Suggix, Arroway, Friday, ImmoDocs, Gilbert, Clipy, VideoGen, pcb.express, TrueProxies, SelectaRank, Revit Model, Symbioza, CovaSyn, AgentHop, Auth Your Agent, GeoSource, Agentboxd, Peach, AQL PropertyCheck and the consumer, geo-niche and dev-utility slugs on /all pages 1-2.

## Skip classes held

- **SEO and link-building utilities:** LinkBunny joins the class already served by the outreach and backlink entries. LinkBunny would need to expose something beyond a single marketplace to earn a guide.
- **Hosted assistants without a protocol surface:** Agent Cody is an agent product with a Slack-first onboarding flow, not a documented MCP server. Products in this shape do not get integration guides until they publish an endpoint.
- **Vendors with an unpublished endpoint:** TrackIQ. A guide that cannot state the transport or the URL is not a guide.

## Verification

The new guide passed the inline checks (title length, description length, required frontmatter fields, added date, dash scan, See Also path existence) and the repository frontmatter validator over the whole docs tree. The class-level AEO advisory from the local pre-commit gate is accepted house style for this file class, as it is for the rest of the external catalog.
