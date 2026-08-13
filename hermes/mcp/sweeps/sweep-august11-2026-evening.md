---
title: "MCP Sweep — August 11, 2026 (Evening)"
description: "Evening sweep following midday sweep. 3 new business-relevant MCP servers discovered — referral/affiliate program management, full ad workflow, and video"
date: 2026-08-11T22:00:00-07:00
sources: [mcp.so, mcpservers.org]
status: complete
finds: 3
guides: 3
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-august11-2026-evening/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# MCP Server Discovery Sweep — August 11, 2026 (Evening)

## Summary

- **3 genuinely new business-relevant servers found** since the midday sweep (~6 hours later)
- **3 integration guides written** with full setup, tool descriptions, and verdicts
- **12+ additional servers identified** (not catalogued — dev tools, consumer, crypto, or niche)
- **mcpservers.org now at 10,857 servers** (up from 10,856 in the midday sweep — +1 server added since midday)
- **mcp.so stable at ~22,000+**

## Methodology

1. **mcp.so homepage** — Extracted Featured servers, Trending this week, and New Arrivals sections
2. **mcpservers.org homepage + /all** — 30 newest servers (sorted newest-first), plus Featured MCPs
3. **Cross-reference** — All candidates checked against 143-server catalog
4. **Business-relevance filter** — Only servers useful for business operators catalogued
5. **Individual server pages** — Extracted full details from mcp.so server detail pages for verified candidates

## Evening Findings

### ★★★ Cello MCP — Catalogued with Guide

**What:** Remote MCP server for Cello's referral, partner, and affiliate program management platform. Ask AI agents about referrer revenue, churn risk, attribution health, and program benchmarks — in plain language.

**Why it matters:** First MCP server dedicated to referral/affiliate program intelligence. Referral programs drive 30% higher LTV than non-referred customers, but most operators check dashboards monthly at best. Cello MCP puts program data in the AI agent's tool set, enabling proactive partner management instead of reactive dashboard checking.

**Details:**
- Remote MCP: `https://mcp.cello.so/mcp`
- Auth: OAuth (browser sign-in)
- Transport: Streamable HTTP
- Category: Finance & Commerce (mcp.so) / Marketing
- Featured on mcp.so homepage
- Company: Cello (established referral platform)

**Guide:** `/hermes/mcp/servers/external/cello-mcp/`

---

### ★★★ AdWhispr MCP — Catalogued with Guide

**What:** Complete ad workflow MCP — research any brand's live Facebook and TikTok ads (ranked by days running), clone proven winners for your brand, and launch real campaigns on Google, TikTok, and Meta. OAuth sign-in, free tier, no API keys to manage.

**Why it matters:** The most complete ad workflow MCP observed to date — covers the full creative lifecycle (research → clone → launch) across three ad platforms. Combined with our existing AdMake AI MCP (net-new creative generation), operators now have a two-tool AI ad studio. The "days running" ranking as a performance proxy is a genuinely useful heuristic that raw ad libraries don't provide.

**Details:**
- Remote MCP: `https://adwhispr.com/api/mcp`
- Auth: OAuth (browser sign-in, free account)
- Transport: Streamable HTTP
- Pricing: Free tier → Pro $39/mo (unlimited research) → Agency $149/mo
- Category: Productivity (mcp.so) / Marketing
- Featured on mcp.so homepage
- GitHub: `adwhispr/mcp-server`

**Guide:** `/hermes/mcp/servers/external/adwhispr-mcp/`

---

### ★★ ViewMade MCP — Catalogued with Guide

**What:** YouTube research, SEO, and finished video production for AI agents. Listed on mcpservers.org homepage in the "Latest MCPs" section under the Marketing category.

**Why it matters:** Video content production is one of the top operator pain points. The concept of agent-native video production — from research through publishing — is compelling for operators who want YouTube presence without a dedicated video team. However, public MCP documentation is thin (support-oriented rather than developer-focused).

**Details:**
- Source: mcpservers.org (homepage Latest section)
- Category: Marketing
- Status: Early-stage (limited public MCP docs)
- Support: viewmade.com/support

**Guide:** `/hermes/mcp/servers/external/viewmade-mcp/`

---

## Also Identified (Not Catalogued)

| Server | Source | Category | Why Not Catalogued |
|---|---|---|---|
| **Medplum** (2.5K⭐) | mcp.so Trending | Healthcare | Healthcare compliance platform — significant but industry-specific |
| **PLUR** (226⭐) | mcp.so Trending | Memory | Agent memory with 98% R@5 on LongMemEval — excellent but developer tool, not operator-facing |
| **Termany** (174⭐) | mcp.so Trending | Dev Tools | Agent-native terminal — developer tool |
| **LocalCan** (82⭐) | mcp.so Trending | Dev Tools | ngrok alternative (tunnels, traffic inspection) — dev tool |
| **BetterBugs** | mcp.so Featured | Dev Tools | Bug report loading for AI agents — developer tool |
| **AI Video MCP by AITuber** | mcp.so Featured | Content | Video creation for AI agents — content niche, competing with HeyGen pipeline we already have |
| **directree** (brand new) | mcp.so New Arrivals | Dev Tools | Software directory querying — not business-ops |
| **scvd.store** | mcp.so New Arrivals | Infrastructure | x402 trust layer/conformance checking — crypto infrastructure |
| **crosscode-cli** | mcp.so New Arrivals | Dev Tools | Multiplayer coding sync — developer tool |
| **SportsTrackLive** | mcp.so New Arrivals | Consumer | Sports tracking — consumer niche |
| **Sightseer MCP** | mcpservers.org | Consumer | Travel/campground search — consumer niche |
| **Various (6+)** | mcpservers.org | Various | WorkloadTruth, TokenTrust, NeuronScope, ComputeLedger, InferBench, auditreach — all developer/ML tools |

## Key Observations

1. **The MCP catalog is now deep enough for category specialization.** With Cello MCP (referrals), AdWhispr MCP (ads), AdMake AI MCP (creative), JaxSuite AI MCP (cold outreach), and DripRaven MCP (WhatsApp) — all catalogued on the same day — we're seeing MCP coverage across the full marketing stack.

2. **"Agent-native" is the new "API-first."** Cello's pitch ("connect once, query in plain language") and AdWhispr's ("no API keys to manage") continue the trend observed in the midday sweep: MCP servers are positioning as dashboard replacements, not API wrappers.

3. **Ad workflow MCPs are becoming a sub-category.** We now have four distinct ad-related MCPs: AdWhispr (research → clone → launch), AdMake AI (generate → research → publish), OpusGrowth (cross-platform campaign management), and Meta Ads MCP (Pipeboard). Each covers a different slice of the ad lifecycle.

4. **mcpservers.org growth slowing.** Only +1 server in ~6 hours (10,856→10,857) vs. +45 in the previous 6 hours. Suggests the evening window is lower-submission or the growth rate is normalizing.

5. **PLUR's 98% R@5 benchmark is notable.** While not catalogued (developer tool), PLUR's performance on LongMemEval-S (N=500) makes it worth tracking for potential CorpusIQ internal use as agent memory infrastructure.

## CorpusIQ Angle

The marketing MCP stack is now complete enough that a CorpusIQ operator could theoretically run their entire growth function through MCP-connected AI agents: competitive ad research (AdWhispr/AdMake AI) → creative generation (AdMake AI) → campaign launch (AdWhispr/OpusGrowth/Meta Ads) → social listening (Xpoz) → SEO audit (SiteGuru) → referral program management (Cello) → cold outreach (JaxSuite AI). The missing piece is unified analytics across all these channels — which is exactly what CorpusIQ's 37+ business connectors provide.

## Catalog Status

- **Before sweep:** 143 servers, 43 guides
- **After sweep:** 146 servers, 46 guides (+3)
- **Next sweep:** Aug 12 morning
