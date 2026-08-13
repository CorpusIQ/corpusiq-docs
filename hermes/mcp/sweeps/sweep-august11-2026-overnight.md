---
title: "MCP Sweep — August 11, 2026 (Overnight)"
description: "Overnight sweep following Aug 10 evening sweep. 3 new business-relevant MCP servers discovered — social media intelligence, LinkedIn content ops, and SEO"
date: 2026-08-11T03:00:00-07:00
sources: [mcp.so, mcp.so GitHub issues]
status: complete
finds: 3
guides: 3
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-august11-2026-overnight/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# MCP Server Discovery Sweep — August 11, 2026 (Overnight)

## Summary

- **3 genuinely new business-relevant servers found** since the Aug 10 evening sweep
- **3 integration guides written** with full setup, tool descriptions, and verdicts
- **1 server added TODAY** (scvd.store, Aug 11) — x402 infrastructure, not business-operator relevant
- **15 GitHub issues** submitted to mcp.so since the evening sweep — 3 were business-relevant
- **mcpservers.org JSON-LD broken** — no data returned from /all page

## Methodology

1. **mcp.so homepage SSR** — Extracted `recentServers` from TanStack Router hydration payload (7 servers, Aug 8-11)
2. **mcp.so/feed** — 30 server cards extracted via h3 block parsing
3. **mcp.so GitHub issues** — 15 most recent `chatmcp/mcpso` issues scanned (Aug 10-11 submissions)
4. **mcpservers.org /all** — JSON-LD extraction attempted but returned no data (broken, consistent with prior sweeps)
5. **Cross-reference** — All candidates checked against 134-server catalog with Python fuzzy matching
6. **Business-relevance filter** — Only servers useful for business operators catalogued

## Evening Findings

### ★★★ SiteGuru MCP — Catalogued with Guide

**What:** Remote MCP server connecting SiteGuru's full SEO dataset — crawl audits, Google Search Console rankings, Google Analytics traffic, backlink profiles, and indexation status — to AI agents via OAuth or API key.

**Why it matters:** First commercial SEO platform to ship MCP with full operational data access. Operators can ask "What should I fix first?" or "Which pages lost the most traffic?" and get prioritized, actionable answers — not just reports. Frictionless one-click OAuth setup.

**Details:**
- Remote MCP: `https://mcp.siteguru.co/mcp`
- Auth: OAuth (one-click) or Bearer API key
- Transport: Streamable HTTP
- No public GitHub repo
- Company: SiteGuru (established SEO tool)
- Added to mcp.so: ~Aug 9

**Guide:** `/hermes/mcp/servers/external/siteguru-mcp/`

---

### ★★★ LinkedMash MCP — Catalogued with Guide

**What:** Hosted MCP server for LinkedIn saved posts — search, organize, draft, schedule, publish, and analyze. Import via Chrome extension, then connect any MCP client.

**Why it matters:** First "content engine" MCP that turns passive LinkedIn consumption into active content creation. Operators who save posts for inspiration can now search that library, draft from it, schedule posts, and analyze performance — all through their AI agent. Covers the full content lifecycle.

**Details:**
- Remote MCP: `https://mcp.linkedmash.com/api/mcp`
- Auth: Bearer token (lm_ prefix)
- Transport: Streamable HTTP
- REST API also available: `api.linkedmash.com/v1`
- Export to Notion, Sheets, Airtable, Miro
- Submitted via GitHub issue #3516 (Aug 10, 22:28 UTC)
- No public GitHub repo

**Guide:** `/hermes/mcp/servers/external/linkedmash-mcp/`

---

### ★★★ Xpoz MCP — Catalogued with Guide

**What:** Social media intelligence MCP — 3B+ posts indexed across Twitter/X, Instagram, Reddit, and TikTok. Brand monitoring, social listening, lead generation, competitive intelligence. No platform API keys required. Remote MCP with OAuth 2.1.

**Why it matters:** Best-in-class multi-platform social MCP. The "no platform API keys" design eliminates the biggest friction in social data access. Trusted by NYU, UC Berkeley, Columbia, Georgia Tech, and the Linux Foundation. 2-minute setup. For operators doing brand monitoring or social listening, this replaces 4 separate platform APIs.

**Details:**
- Remote MCP: `https://mcp.xpoz.ai/mcp`
- Auth: OAuth 2.1
- Transport: Streamable HTTP
- GitHub: `xpozpublic/xpoz-mcp` (MIT, 10⭐, 18 commits)
- Python SDK: `pip install xpoz`
- Submitted via GitHub issue #3507 (Aug 10, 08:36 UTC)

**Guide:** `/hermes/mcp/servers/external/xpoz-mcp/`

---

## Also Identified (Not Catalogued)

### DocuQueue MCP (#3508) — ★★
PDF generation, form filling, document management from AI chat. `io.github.docuqueue/docuqueue-mcp`. Remote MCP. 1⭐ on GitHub. Document operations are useful for operators but this is early-stage (1 star, brand new). Watching for maturity.

### Data Studio Agent (#3506) — ★★
Unified database MCP (70+ SQL + NoSQL), local-first. Submitted Aug 10. Potentially significant for data operators but no public GitHub repo found — could not verify. Watching.

### SV Number (#3514) — ★
Private phone numbers in 200+ countries for SMS verification. Potentially useful for operators managing multi-factor auth setups across services. Niche use case.

### Other GitHub Submissions (Dev Tools / Consumer / Niche)
- **scvd.store** (Aug 11): x402 trust layer/conformance checking — infrastructure
- **crosscode-cli** (Aug 10): Multiplayer coding sync — dev tool
- **SportsTrackLive** (Aug 9): Sports tracking — consumer niche
- **FLINT Network** (Aug 8): Agent integrity for money movement — security infra
- **q-ring** (Aug 8): Quantum keyring for agents — dev tool
- **FiatDock** (Aug 8): Agent marketplace (USDC/x402) — payments infra
- **mcp-x** (#3511): CLI tool for MCP servers — dev tool
- **MeshMarket** (#3509): Agent capability exchange — dev tool
- **gandr-mcp** (#3505): TTS for agents — dev tool
- **oura-mcp** (#3503): Oura Ring API — consumer health
- **Poliety MCP** (#3501): AI news feed with integrity verification — media niche
- **UAPDrop** (#3515): Declassified UFO records — niche
- **InstaSeer** (#3504), **HokAI** (#3502), **Redbark** (#3499): Insufficient info

### mcp.so/feed Additional (Dev Tools / Consumer / Regional Niche)
- cloro, Faxer, LocalCan, Constants, Apiosk, Stratyfix, Contio MeetingOS, Plainpaper, Coinfuty, FormLM, Heterogent, Agimem, Nero AI Image Processing, Departi (travel compliance), GoLeasy (German leasing), Xata (database dev tool), Trimtab AIS (shipping/logistics niche)

## Key Observations

1. **Social/content MCPs are the Aug 11 theme.** Xpoz (social listening), LinkedMash (LinkedIn content), and SiteGuru (SEO) form a complete "operator visibility stack" — listen, create, and optimize across all channels.

2. **Commercial platforms now shipping MCP.** SiteGuru and LinkedMash are both established commercial products (not open-source projects) that added MCP as a feature — continuing the trend started by QuickBooks/Oracle MCPs (datagrout.ai), DealMachine, and Meta Ads. MCP is becoming a standard SaaS integration pattern.

3. **mcpservers.org JSON-LD extraction remains broken.** For the 5th consecutive sweep, the `/all` page's JSON-LD `itemListElement` returned no data. This source is effectively dead for cron sweeps. mcp.so homepage SSR + GitHub issues are the reliable primary sources.

4. **High submission velocity.** 15 GitHub issues submitted to mcp.so in ~24 hours (Aug 10-11). The MCP ecosystem is adding ~15 new servers per day through mcp.so alone.

5. **"No API keys" as a differentiator.** Xpoz's key selling point is abstracting away platform API complexity. This pattern — MCP as the one integration point that hides multi-platform auth — may become standard for social/data APIs.

## CorpusIQ Angle

The operator visibility stack (Xpoz + LinkedMash + SiteGuru) is directly relevant to CorpusIQ's growth mission. Social listening for operator pain points → LinkedIn content drafting from saved inspiration → SEO optimization of landing pages. CorpusIQ's 37+ business connectors complement this by providing the financial/revenue context that social data alone can't answer.

## Catalog Status

- **Before sweep:** 134 servers, 137 guides
- **After sweep:** 137 servers, 140 guides (+3)
- **Next sweep:** Aug 11 evening or Aug 12 morning
