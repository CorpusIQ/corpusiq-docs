---
title: "MCP Server Discovery - September 28, 2026 (Night Sweep)"
description: "Night sweep over the mcp.so homepage (New arrivals, Featured servers and Trending this week sections, 23 unique server blocks, direct fetch) and mcpservers.org /all page 1 via the r.jina.ai reader proxy, with 3 mcp.so detail pages and 6 mcpservers.org detail probes. 2 new business-relevant servers catalogued with guides: ohmyho.st MCP and EQIQs MCP."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-28
---

# MCP Server Discovery - September 28, 2026 (Night Sweep)

**Source:** mcp.so homepage (New arrivals, Featured servers and Trending this week, 23 unique server blocks, direct fetch) + mcpservers.org /all page 1 via the r.jina.ai reader proxy (direct curl Cloudflare-challenged) + 3 detail pages (mcp.so server pages, direct fetch)
**Method:** feed slug/name pairing across all three homepage sections, /all slug extraction with prior-sweep disposition cross-reference, detail-page enrichment for endpoint/auth/tools, endpoint probes (EQIQs endpoint HTTP 401 auth gate, ohmyho.st npm registry package), guide validation (8 frontmatter fields, em-dash scan, redaction scan, title length, 3 FAQ question headings)
**Date:** September 28, 2026 19:00-20:00 MST (02:00-03:00 UTC)

## Summary

| Metric | Count |
|---|---|
| Homepage blocks parsed | 23 unique (8 New arrivals + 9 Featured + 6 new Trending, direct fetch) |
| /all entries classified | 30 (page 1 via r.jina.ai proxy) |
| Detail pages fetched | 3 mcp.so direct + 6 mcpservers.org probes (all 404) |
| Candidates cross-referenced | 23 homepage names + 30 /all slugs against the 726-server catalog plus Sep 27 evening, Sep 28 morning, midday and evening disposal prose |
| New business-relevant servers | 2 |
| Integration guides written | 2 |
| Guide validation | 2/2 PASS |

## New Servers Catalogued (2)

**DevOps and infrastructure**
1. **ohmyho.st MCP** - all-in-one Vercel, Supabase and Resend alternative at docs.ohmyho.st/agents/mcp. A stdio MCP server (npm @amerged/ohmyhost-mcp, Node 22+, Apache-2.0 client, registry name io.github.amerged-org/ohmyhost-mcp) that lets Codex, Claude Code, Cursor, Hermes or OpenClaw deploy a GitHub app (Vite, TanStack Start, Next.js), run managed Postgres, send and receive transactional email and manage domains and budgets from one credit balance. Browser sign-in, you keep your own auth provider. npm registry verified live (latest 0.1.26, published 2026-09-29T02:02Z).

**HR and team**
2. **EQIQs MCP** - working-style and compatibility insights at eqiqs.com/mcp. Remote MCP at https://adgmsnwjynqkhawhioil.supabase.co/functions/v1/mcp over OAuth 2.1 (Bearer token for clients that cannot complete OAuth). 16 named tools across 21 frameworks (DISC, Big Five, MBTI-style): profile CRUD, compatibility scoring, team reads up to 12, meeting prep, lead suggestions, invites, assessments, notes, relationships and a premium coaching narrative with price shown before it runs. Endpoint probe returned HTTP 401 auth gate.

## Identified, Not Catalogued

- **Per-connector re-listing:** Google Search MCP Server (featured; HasData per-connector re-listing of the catalogued gateway, Sep 10 skip-class precedent respected).
- **Prior dispositions:** AI Video MCP by AITuber (Aug 11 disposition: video creation niche, HeyGen-pipeline overlap), AOI Environmental Intelligence, OpenZiti / LLM-Gateway, Medplum, Agent Margin Router, Termany, Hostinger, OpenLore, TinyFish, CUQU, SnapDeploy, Pocket Network, Schemity, plus /all dispositions TRDEFI, the 550W AI pair, TheLuckyStrike relistings, Recordist, Screen Browser, UpRes, Lightdrift, Kairos Signal, Capacity Attest.
- **Repeats already catalogued:** AdWhispr, API Direct, Atomic Mail Agentic, PLUR, LocalCan, Faivelo Email, plus /all page 1 catalogued items (Scribase, Menivor, Audiogram API, Cortex, SkillsInput, Etincel, ParrotNotes, AI Layoffs, Cooper Email).
- **Removed or personal submissions (404 on detail fetch):** wenhua6666668-oss, babbagescabbages, mtangoz, domondi1, itsmostafa, mohammadhijjawi97 - all six fresh mcpservers.org /all page 1 slugs return 404 detail pages; disposed.

## Verification Notes

- 2/2 guides passed validation: 8 frontmatter fields each, zero em-dashes, zero redaction markers, titles under 60 chars, 3 FAQ question headings per guide.
- Endpoints verified this cycle: EQIQs endpoint HTTP 401 auth gate (live server behind auth); ohmyho.st npm registry package @amerged/ohmyhost-mcp HTTP 200 with latest 0.1.26 and registry name io.github.amerged-org/ohmyhost-mcp. No endpoint was guessed.
- EQIQs tool names come from the vendor's published tool list on the mcp.so detail page. ohmyho.st publishes no tool table on the listing; its capability table is prose-derived from the vendor docs with the live-tool-list caveat per doctrine.
- Prior-sweep cutoff: Sep 28 evening stamp 18:05Z. The New arrivals feed has rolled past the evening top (TinyFish): ohmyho.st and EQIQs now sit above it and form the new window.
- mcpservers.org /all now shows 13,611 servers. Core directory listings otherwise unchanged from the evening sweep (mcp.so NOT LISTED, quarantine, no resubmit).
