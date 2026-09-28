---
title: "MCP Server Discovery - September 28, 2026 (Midday Sweep)"
description: "Midday sweep over the mcp.so feed (30 server blocks, direct fetch) and mcpservers.org /all page 1 via the r.jina.ai reader proxy, with 4 detail pages fetched. 2 new business-relevant servers catalogued with guides: Uxia MCP and Selfstorming MCP."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-28
---

# MCP Server Discovery - September 28, 2026 (Midday Sweep)

**Source:** mcp.so feed (30 server blocks, direct fetch) + mcpservers.org /all page 1 via the r.jina.ai reader proxy (direct curl Cloudflare-challenged) + 4 detail pages (mcp.so server pages via the reader proxy)
**Method:** feed slug/name pairing with age text, /all slug extraction with prior-sweep disposition cross-reference, detail-page enrichment for endpoint/auth/tools, guide validation (8 frontmatter fields, em-dash scan, redaction scan, title length)
**Date:** September 28, 2026 10:00-11:00 MST (17:00-18:00 UTC)

## Summary

| Metric | Count |
|---|---|
| Feed blocks parsed | 30 (mcp.so, direct fetch) |
| /all entries classified | 30 (page 1 via r.jina.ai proxy) |
| Detail pages fetched | 4 |
| Candidates cross-referenced | 28 feed names + 30 /all slugs against the 723-server catalog plus Sep 27 evening and Sep 28 morning disposal prose |
| New business-relevant servers | 2 |
| Integration guides written | 2 |
| Guide validation | 2/2 PASS |

## New Servers Catalogued (2)

**User research**
1. **Uxia MCP** - AI user testing and UX research at platform.uxia.app/api/mcp-v2/mcp. AI-simulated testers evaluate websites, prototypes and onboarding flows: research drafts with tasks and surveys, synthetic audiences, cost preview before an approved launch, severity-ranked findings with screenshot evidence. OAuth with PKCE.

**Marketing**
2. **Selfstorming MCP** - curated marketing libraries and ideation at www.selfstorming.com/api/mcp. 1,800+ award-winning campaigns broken down to brief, idea, mechanic and strategy, 850+ sourced findings from WARC, Kantar, System1 and Ipsos, technique and framework libraries, and ideation, naming and hooks sessions saved as exportable boards. OAuth login, Selfstorming Pro subscription.

## Identified, Not Catalogued

- **Dev infra class:** TinyFish (browser automation, search and fetch with a wallet for Agent and Browser modes).
- **Niche vertical:** Texas RRC Wellbore Intelligence (oil and gas wellbore records from the Texas Railroad Commission, 25 free rows, $499 unlimited).
- **Repeats and prior dispositions:** the remainder of the feed was Sep 27 evening and Sep 28 morning repeats (Stackcut, PaperOffice AI, Databar.ai, Tyton, Screen Browser, Agent Traffic Lab, Metabind demo, DSCR Lender Data, Senaro, SnapDeploy, HostingFor.AI, Schemity, nu:legal, Companero, Twistly, Email Spam Tester, Laso Finance, Pocket Network, LiquidVision, Beyond Payday, Soar Flight Booking); /all page 1 carried only morning-sweep dispositions (TheLuckyStrike relistings, Grill, Inferrail, System One Connector, since-cutoff, WhichTrim, Agent Traffic Lab, Screen Browser).

## Verification Notes

- 2/2 guides passed validation: 8 frontmatter fields each, zero em-dashes, zero redaction markers, titles under 60 chars, 3 FAQ question headings per guide.
- Both endpoints come from vendor or directory pages fetched this cycle: Uxia (platform.uxia.app/api/mcp-v2/mcp, from the mcp.so detail page), Selfstorming (www.selfstorming.com/api/mcp, from the mcp.so server page; vendor docs at selfstorming.com/tools/mcp/docs). No endpoint was guessed.
- Tool names are served from the endpoints; capability tables reflect the vendors' published capability sets per doctrine.
- Core directory listings re-verified this cycle: mcpservers.org LISTED (reader proxy title), glama.ai LISTED (HTTP 200), smithery.ai registry entry present (benoit-p/Cprusiq), mcp.so NOT LISTED (empty-state; quarantine, no resubmit), PulseMCP LISTED (proxy title).
- Prior-sweep cutoff: Sep 28 morning stamp 10:18Z. The feed had rolled heavily since: 4 blocks above the morning top (Selfstorming, Uxia, Texas RRC, TinyFish) formed the new window.
