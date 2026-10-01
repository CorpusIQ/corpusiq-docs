---
title: "MCP Server Discovery - October 1, 2026 (Midday Sweep)"
description: "Midday MCP ecosystem sweep: Zyte MCP, Builders in Fintech MCP and AgentGrid MCP catalogued, with 17 candidates dispositioned."
last_updated: 2026-10-01
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october1-2026-midday"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - October 1, 2026 (Midday Sweep)

## Summary

3 new business-relevant MCP servers catalogued with integration guides.

Firecrawl was unconfigured this cycle, so every directory fetch ran through the r.jina.ai reader proxy. That proxy was also the only way past the Cloudflare wall on mcpservers.org: direct `curl` on both the `/all` listing and the individual detail pages returned `<title>Just a moment...</title>` challenge shells, while the same URLs through the reader proxy returned full content.

## Sources Swept

| Source | Method | Yield |
| --- | --- | --- |
| mcp.so /feed | r.jina.ai reader proxy | 30 server blocks |
| mcpservers.org /all | r.jina.ai reader proxy | 30 slugs |
| mcpservers.org detail pages | r.jina.ai reader proxy | 23 pages classified |
| mcp.so server pages | r.jina.ai reader proxy | 3 detail fetches |

## New Servers Catalogued

### Zyte MCP - Web Data Extraction for Agents

Official remote Streamable HTTP server at `mcp.zyte.com/v1/mcp` with OAuth sign-in. 34 tools covering unblocked HTTP fetching, browser rendering with clicks, typing, JavaScript and screenshots, structured AI extraction of product, article, job and listing fields, country and language-scoped web search, cost and usage reporting, and Scrapy Cloud project, spider, job, schedule and collection control. Server use is free; Zyte API and Scrapy Cloud usage bills to your own account.

Relevance: HIGH. **Endpoint verified** (HTTP 405 on bare GET, the expected method-not-allowed response for a Streamable HTTP MCP endpoint).

### Builders in Fintech MCP - Fintech Funding Data

Keyless read-only remote Streamable HTTP at `buildersinfintech.ai/mcp`. 19 tools over 2,400+ fintech funding rounds with investors and lead flags, company and investor profiles, daily fintech news, 150+ newsletter issues, and knowledge from 53 podcast episodes, plus a curated events calendar, a weekly Funding Index and investor follow-on scorecards. Editorially sourced, amounts never converted between currencies, CC BY 4.0 data licence, 500 calls per connection per day.

Relevance: HIGH. **Endpoint verified** (site and `/mcp` page both HTTP 200).

### AgentGrid MCP - Shared Workspace for Agents

Remote Streamable HTTP at `api.agentgrid.io/v1/mcp` with OAuth. 10 tools giving agents a governed team workspace where humans and agents build, host, publish and review live apps, docs and files. Every artifact is a real git repository that can be cloned, committed to and published to a public URL, with pinned change requests resolvable by commit trailer and shell-free file read and edit tools.

Relevance: HIGH. **Endpoint verified** (HTTP 401 on bare GET, the expected auth-required response).

## Also Identified (Not Catalogued)

Appman AI (App Store and Google Play ASO analytics, store-marketing analytics class already covered), NordicContacts (Nordic B2B decision-maker contact database, data-broker contact class with the Apollo and Hunter precedents), Postqued (social scheduling and approvals, social publishing class already covered by Blog2Social and uplika), Deploy Social (social publishing for one Deploy workspace, same class), Revamp (AI website redesign, web-builder utility class), Flows (product adoption infrastructure and in-app onboarding, product-analytics utility class), FirstSales (email deliverability diagnostics, email-infrastructure class), PromptQuorum (public read-only MCP over local-LLM guides and a software directory, dev-content utility class), Confirme by Synapse (Ed25519-signed third-party receipts, agent-verification class), xTiles (visual project and task planning, project-management class already covered), Leadsgram (lead finding and market research, sponsored placement), Trust Check (Base token and wallet honeypot simulation with x402 pay-per-call, crypto-security class), AgentHands (agents hiring humans, human-task-marketplace class with the Open Task Relay precedent), D365 Mockup Agent (Dynamics 365 mockup drafting, dev-utility class, prior disposition respected), Lintlab PDF to Markdown (Apify actor, 2 total users, thin Apify actor class), CycleCalcs (astronomy API, niche vertical, prior disposition), Reps Gym Workout Log (consumer fitness).

404-shell slugs excluded without a detail fetch: arcmira, liendeadline, uuriko, ahmedkhaleel2004, apmleokeo-gif, karl-andres, lrehmann.

## Prior Dispositions Respected

FlatHunt (Berlin housing aggregator, disposed October 1 morning), TATUAT.RO (Romanian tattoo-supply retail, September 30 night), MCP DB Wizard (ruled September 10 late-night), Porkbun, GAIP Agents, oceanalt-aml-mcp, uplika, prodready, Webshare, trip1, elmah.io MCP, HeyLead, fAlpha, TokElements, Unipile, Dumpster Controls, Rebbel, MeroFoundry, MemeSwap MCP, Common Paper Contracts, Genchi, Manifold MCP, PixelDojo, Povver, Aayat AI, Adviserry and Blog2Social.

## CorpusIQ Directory Status

| Directory | Status | Verification |
| --- | --- | --- |
| mcpservers.org | LISTED | `/servers/corpusiq-io` resolves with CorpusIQ content via reader proxy (direct curl returns a Cloudflare challenge shell) |
| glama.ai/mcp | LISTED | HTTP 200 on `/mcp/servers/@corpusiq/corpusiq-docs` |
| smithery.ai | LISTED | Registry API returns displayName CorpusIQ at `benoit-p/Cprusiq` |
| PulseMCP | LISTED | Title `Official CorpusIQ MCP Server | PulseMCP` via reader proxy (direct curl 403, known Cloudflare artifact) |
| mcp.so | NOT LISTED | Instant moderation deletion, manual submission required |
| registry.modelcontextprotocol.io | BLOCKED | Needs npm account and domain verification file |
| agenticskills.io | BLOCKED | Form reachable (HTTP 200) but the review queue backend is disabled |

## Notes

No new MCP directories surfaced this cycle. The `/all` page carried 30 slugs that were entirely fresh against the prior ledger, but classification put most of them in covered classes (social publishing, dev utilities, project management) or behind the 404 shell; the business-operator-grade finds came from the feed and the fintech corner of `/all`.
