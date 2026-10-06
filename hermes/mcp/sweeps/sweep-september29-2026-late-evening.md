---
title: "MCP Server Discovery - September 29, 2026 (Late Evening)"
description: "Late evening sweep over the mcp.so /feed (29 server blocks, direct fetch) and mcpservers.org /all pages 1-2 via the r.jina.ai reader proxy, with 7 detail pages fetched. 5 new business-relevant servers catalogued with guides: Unipile MCP, Rebbel MCP, fAlpha MCP, Porkbun MCP and Dumpster Controls MCP."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-29
---

# MCP Server Discovery - September 29, 2026 (Late Evening)

**Source:** mcp.so /feed (29 server blocks, direct fetch) + mcpservers.org /all pages 1-2 via the r.jina.ai reader proxy + 7 mcp.so detail pages via the reader proxy
**Method:** feed slug/name pairing with feed-order recency (the evening sweep had catalogued GAIP Agents as the newest arrival; the 7 entries ahead of it in feed order were evaluated fresh), /all slug extraction, two-round token-probe cross-reference against the 745-server catalog plus all disposal prose (sweep reports, .last-sweep files, index.md), targeted context greps for generic-token and name-form hits, detail-page enrichment for endpoint/auth/tools, guide validation (8 frontmatter fields, em-dash scan, title length, FAQ question headings)
**Date:** September 29, 2026 19:00-19:20 MST (September 30, 2026 02:00-02:20 UTC)

## Summary

| Metric | Count |
|---|---|
| Feed blocks parsed | 29 server blocks (29 unique) |
| /all entries classified | 60 (pages 1-2 via r.jina.ai proxy) |
| Detail pages fetched | 7 via the reader proxy (mcp.so /servers route) |
| Candidates cross-referenced | 28 names and slugs against the 745-server catalog plus disposal prose |
| New business-relevant servers | 5 |
| Integration guides written | 5 |
| Guide validation | 5/5 PASS |

## New Servers Catalogued (5)

**Sales & Outreach**
1. **Unipile MCP** - one Streamable HTTP endpoint for LinkedIn (Sales Navigator, Recruiter), WhatsApp, Instagram, Telegram and email. Endpoint developer.unipile.com/mcp?branch=v2.0, API key auth. Capabilities drawn from the vendor's documented use cases: Sales Navigator lead search with seniority and headcount filters, conversation sync with new-message webhooks, threaded email sends over Gmail, Outlook and IMAP. No public repo; listing shows no static tool table (live tool list served from the endpoint).

**Social Media Management**
2. **Rebbel MCP** - approval-gated social marketing for small business. Endpoint app.rebbel.io/api/mcp, OAuth sign-in, Verified and Featured on mcp.so. Builds a brand guide from your website, drafts campaigns (posts, captions, images) and publishes only after server-enforced approval to Facebook, Instagram, X, LinkedIn, Threads and Bluesky; disconnecting a platform stops all activity. Performance read-back for recent posts. GitHub alexdaltonmccoy/rebbel-gemini-extension, MIT, 0 stars, pushed Sep 3.

**Finance**
3. **fAlpha MCP** - read-only US equity research. Endpoint agent.falpha.ai/mcp, OAuth 2.1 or personal access token. 17 read-only tools grouped on the listing: model signal with drivers, flips and term structure, screener, news sentiment, analyst coverage, SEC filings and XBRL, FRED macro, company profile and ratios. Data sources: fAlpha model signal, Financial Modeling Prep, SEC EDGAR, FRED. No-card trial token at falpha.ai/mcp/trial; agent kit repo techbammoney/falpha-agent-kit, MIT, 0 stars, pushed Sep 29. The server never places orders.

**Business Operations**
4. **Porkbun MCP** - official registrar server. Hosted endpoint mcp.porkbun.com/mcp (OAuth sign-in) plus local npx -y @porkbunllc/mcp-server with API keys. Domain availability, registration, renewal and transfers; DNS records, nameservers, glue records, DNSSEC; safety nets (preflight risky changes, zone rollback); Secure Static Hosting deploys; URL forwarding, contacts, webhooks and Cloudflare-connected domains. Agent-safety design: idempotent writes, dry-run first on billable and destructive operations, integer cents, stable error codes.

5. **Dumpster Controls MCP** - free dumpster rental software with a remote MCP at mcp.dumpstercontrols.io/mcp, OAuth 2.1. 24 tools: 12 read-only (orders, customers, invoices, landfill receipts, drivers, finance summaries), propose-then-confirm writes (task completion, task assignment, order updates, invoice sends, customer upserts) and app-only confirmations for price changes and cancellations. Money never moves through the server; every request runs as the signed-in user limited to their company and role. Listed in Claude's connector directory and the official MCP Registry as io.dumpstercontrols/dumpster-controls.

## Identified, Not Catalogued

- **TokElements** - TikTok LIVE overlay widgets (gift alerts, goals, leaderboards, chat, song requests) built and managed from an MCP client. Creator and consumer class.
- **MeroFoundry** - hosted application platform with 145 tools behind one MCP endpoint; the agent designs data, logic, UI, sign-in and publishes the app. Dev infra class.

## Non-Business Servers (Not Catalogued)

/all pages 1-2 carried only prior dispositions this cycle: the Sep 29 morning ledger had already disposed Court Rules MCP, Mooncatcher Wire, L'Oiseau Bleu, WarpLink, Bankrolled, disclosedby, Rhylthyme, Bazous, BuySignal Deals, Upleex, eSIM-Global, IbiPoint, e-eSIM and Cybergenic Database (name-form variants fooled the token crossref; the context grep resolved them). The midday and evening ledgers disposed elmah.io, Webshare, trip1, AQL PropertyCheck, HaberChat, Beemm Vision, MX Verdict, AnswerLine, Dive Kit, Robozukan, SubmitraX, StudyDiff, rewire-bio Genomics, j0hanz Filesystem and the GenPark single-author burst.

## Directory Listing Status Check

Carried forward from the Sep 29 evening sweep, not re-verified this cycle: glama.ai listed, mcpservers.org listed, smithery listed (Cprusiq), mcp.so not listed (moderation deletion state), PulseMCP listed.

## Verification Notes

- Work ran on the Spark clone (fresh at 00004dc22, post-evening-sweep); the Mac Mini was stale (working tree at midday counts despite evening-sweep HEAD) and was resynced after push.
- Feed timestamps skew ahead of wall clock; feed ORDER was the recency signal: GAIP Agents (evening-catalogued) sat at feed position 8, so positions 1-7 were the post-evening arrivals.
- No endpoint probes were needed this cycle: all 5 catalogued servers publish their endpoint and auth on the listing.
- Zero invented tool names: fAlpha and Dumpster Controls tool groups come from the listing's published tables; Unipile, Rebbel and Porkbun capabilities are the vendor's published feature groups with the live-tool-list caveat stated in the guides.
