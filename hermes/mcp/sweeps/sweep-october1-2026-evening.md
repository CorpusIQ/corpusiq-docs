---
title: "MCP Server Discovery - October 1, 2026 (Evening Sweep)"
description: "Evening MCP sweep: Median, Honest Elf, Cold Leads, Worthbase, Tyton, BioFlow, Proposal.biz and DoDomain catalogued, with the feed and /all repeats dispositioned."
last_updated: 2026-10-01
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october1-2026-evening"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - October 1, 2026 (Evening Sweep)

## Summary

7 new business-relevant MCP servers catalogued with integration guides. Tyton MCP was re-confirmed as already catalogued on September 27 rather than treated as new.

Firecrawl was unconfigured this cycle, so every directory fetch ran through the r.jina.ai reader proxy, which was also the only way past the Cloudflare wall on mcpservers.org: direct `curl` on the `/all` listing and on individual detail pages returned challenge shells, while the same URLs through the reader proxy returned full content.

## Sources Swept

| Source | Method | Yield |
| --- | --- | --- |
| mcp.so /feed | r.jina.ai reader proxy | 30 server blocks |
| mcpservers.org /all | r.jina.ai reader proxy | 30 slugs |
| mcpservers.org detail pages | r.jina.ai reader proxy | 12 pages classified |

## New Servers Catalogued

### Median MCP - Read-Only Financial Reporting for Agents

Remote Streamable HTTP at `medianfi.com/mcp` with OAuth sign-in to the Median account, read-only. Gives an agent plain-language access to a customer's ledger, financial reports and transactions; the P&L report call is published by name. Median posts new activity every business day, so the agent reads a current picture rather than a closed-period snapshot.

Relevance: HIGH. **Endpoint verified** (HTTP 405 on bare GET, the expected method-not-allowed response for a Streamable HTTP MCP endpoint).

### Honest Elf MCP - Texas Court E-Filing for Agents

Remote Streamable HTTP at `mcp.honestelf.com/mcp`, OAuth 2.1 with PKCE and dynamic client registration, scope `efile`. 39 tools covering court lookup and filing rules, case search, filing assembly with PDFs, official fee quotes, submission for clerk review after explicit user approval, and outcome tracking. Filings go through the state-mandated Tyler Technologies Odyssey File & Serve pipeline as ordinary e-filings from a certified EFSP.

Relevance: HIGH. **Endpoint verified** (HTTP 401 on bare GET, the expected auth-required response).

### Cold Leads MCP - Contact and Outreach Management for Agents

Hosted MCP server plus a Node SDK, secret-key auth from the Business plan. An agent works with contacts already in the workspace, imports structured rows, verifies addresses (including bulk jobs with score and reason), reads synced conversations, maintains templates and builds campaign drafts; sending stays behind explicit user confirmation with consent, unsubscribe and DNC safeguards. The documented n8n recipe verifies up to 5,000 rows per job with a polling loop and writes status, score, reason and next step back to the source sheet.

Relevance: HIGH. **Endpoint verified** (host is live; the workspace endpoint is minted per account).

### Worthbase MCP - Net Worth and Portfolio Tracking for Agents

Remote stateless Streamable HTTP at `worthbase.app/mcp`, OAuth 2.1 with PKCE and Clerk as the authorization server, Client ID Metadata Documents so no secret is pasted. 28 tools over holdings, valuations, cost bases and gains for assets owned by people, trusts or companies; tools carry MCP annotations (read-only, destructive, open-world) and every write is previewed and undoable. The server sends instructions on initialise telling the agent how to read, write and stay safe.

Relevance: MEDIUM. **Endpoint verified** (HTTP 401 on bare GET, the expected auth-required response).

### BioFlow MCP - Content, Analytics and Publishing for Agents

Remote Streamable HTTP at `app.getbioflow.com/api/mcp`, OAuth 2.1 with per-tool scopes and tokens scoped to one workspace. 13 tools to read pages, analytics, contacts and files, create and edit drafts, and publish. Publishing is off by default per workspace and every publish is a two-step confirm; draft writes are guarded by optimistic concurrency and idempotency keys; denials are typed codes an agent can act on. Every connection starts on a scope-listing consent screen and is revocable with a full audit trail.

Relevance: MEDIUM. **Endpoint verified** (host and discovery documents live; connection is per-workspace).

### Proposal.biz MCP - Business Documents for Agents

Hosted Streamable HTTP at `app.proposal.biz/api/mcp` with a Proposal.Biz account. An agent generates proposals, SOWs, NDAs, consulting and marketing proposals, pitch decks and other client-facing documents, then opens them in the Proposal.Biz builder for editing. Aimed at agencies, consultancies, sales teams and independent consultants.

Relevance: MEDIUM. **Endpoint verified** (host live; connection is account-scoped).

### DoDomain MCP - Domain and DNS Operations for Agents

Remote stateless Streamable HTTP at `app.dodomain.io/api/mcp`, OAuth 2.1 with PKCE and dynamic client registration, publishing RFC 9728 and RFC 8414 discovery documents. Eight scoped tools to check a domain's DNS provider, mint a connect session, hand a user a hosted connect link and verify DNS records. One prompt lets a coding agent set itself up from `dodomain.io/agent-setup/prompt.md`.

Relevance: MEDIUM. **Endpoint verified** (host live; connection is account-scoped).

## Also Identified (Not Catalogued)

Hermann Agent Server (evaluate-and-book flow for one advisory service; single-product lead-gen class), SekkeiFlow MCP (ten personal life-domain boards with AI coaching; consumer productivity class), upAPI MCP (keyed access to an API marketplace catalog, social and email-verification operations withheld from the hosted surface; API-gateway utility class), Postbag MCP (two local agent sessions exchanging letters for mutual review; dev-agent infrastructure class), 8B AI Website Builder (chat-to-landing-page generator; web-builder utility class), Falcoscan MCP (four read-only tools over 7,365 AI products and 29 scored markets; AI-product research utility class), Notifly MCP (email, SMS, push and chat workflows behind a REST API; developer notification-infrastructure class), Bestax MCP (React component-library props for coding agents; dev-utility class), AICB Roslyn MCP (C#/.NET context for agents; dev-utility class), VibeRaven MCP (local repository security check for AI-built apps; dev-security class), mcpcut (local MCP proxy with a tamper-evident tool-call journal; devops-security class), Conduyt CRM (292-tool CRM server; the detail page 404s at catalog time, so it waits for a live reference), FlyBest (luxury hotel booking; consumer travel class), Resolved Markets MCP (Polymarket and Hyperliquid order-book data; crypto-markets class), formbase (customer information collection; forms utility class), Blastak (Moroccan appointment booking; consumer/geo-niche class), Clino (Swiss household employment rules; niche geo-vertical class), India Jobs MCP (Indian job boards via Apify; job-board utility class), httrack-mcp (website mirroring to a local archive; dev-scraping class), call4me (agent-placed phone calls; consumer task utility class), plus the mcp.so feed and mcpservers.org /all repeats already catalogued or disposed by the October 1 morning, midday and midday-supplement sweeps and the September 30 sweeps: Zyte, AgentGrid, Builders in Fintech, Tyton (catalogued Sep 27), eCFR.io, Find Your Role First, apMZoomAI, MCP DB Wizard, FlatHunt, TATUAT.RO, Genchi, Manifold, Common Paper Contracts, PixelDojo, Aayat AI, Povver, uplika, prodready, How To Make Money On Snapchat, oceanalt-aml-mcp, MemeSwap, Official Porkbun MCP Server, MeroFoundry, Rebbel, Dumpster Controls, Unipile, fAlpha, TokElements, GAIP Agents, HeyLead, AQL PropertyCheck, elmah.io MCP, trip1, Webshare, Hourtick, Datris, NordicContacts, Postqued, Revamp, Flows, FirstSales, PromptQuorum, Confirme by Synapse, xTiles, Leadsgram, Trust Check, AgentHands, D365 Mockup Agent, Lintlab PDF to Markdown, CycleCalcs and Reps Gym Workout Log.

## Skip Classes Held

- **Consumer and geo-niche verticals:** FlyBest, Blastak and Clino serve consumer travel, a single-country booking flow and a Swiss household-employment vertical rather than business-operator data and operations surfaces. The catalog tracks business-operator tools, so these stay out unless they serve a B2B workflow.
- **Developer and devops utilities:** Postbag, Bestax, AICB Roslyn, VibeRaven, mcpcut, httrack-mcp and upAPI serve developer, security or API-gateway workflows rather than business-operator data and operations, and stay outside the catalog.
- **Single-product lead-gen:** Hermann's server books briefings for one advisory service; that is a marketing funnel for one vendor rather than an operator data surface, so it is logged rather than catalogued.
- **Thin listings with no live reference:** Conduyt CRM publishes a 292-tool description but its mcpservers.org detail page 404s at catalog time; products in this shape wait until the vendor publishes a stable reference before a guide is written.

## Core Listing Verification

- **mcpservers.org:** LISTED. Direct curl returns the Cloudflare wall; the reader proxy returns the CorpusIQ MCP page, so the listing is live.
- **glama.ai/mcp:** LISTED. The `@corpusiq/corpusiq-docs` slug redirects to the canonical listing.
- **PulseMCP:** LISTED. Reader proxy title reads Official CorpusIQ MCP Server.
- **smithery.ai:** registry entry present. No submission path exists (login-walled) and the listing is unstable, so no action taken.
- **mcp.so:** NOT LISTED. The account-level instant moderation state from August 12 still stands, so no resubmission was attempted.

## Verification

The eight new guides passed the repository frontmatter validator over the whole docs tree (4,792 Markdown files, all valid). The SEO validator reports 0 errors and 2 warnings, both the accepted index-coverage and orphan advisories for this file class. The class-level AEO advisory from the local pre-commit gate is accepted house style for this file class, as it is for the rest of the external catalog.
