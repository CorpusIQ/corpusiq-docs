# MCP Server Discovery Sweep — August 17, 2026 (Evening)

## Summary

- **9 new business-relevant servers** since the August 17 midday sweep
- **9 integration guides written** (LucidRents, AwardCast, StorePilot, Inside Ads, Bitroad, Secondhand, Atono, xete, Personhood)
- **The human-gated settlement pattern arrives** — xete's draft-then-verify settlement is the approval-gate doctrine applied to money itself
- **Public-records data is productizing into MCP** — LucidRents (buildings) and AwardCast (federal contracts) both package public records into no-auth agent surfaces
- **App portfolio operations gained a cross-store console** — StorePilot joins Google Play and the App Store into one 34-tool stdio server

## Sources Scanned

- mcp.so homepage (New Arrivals, createdAt-timestamped)
- chatmcp/mcpso GitHub issues (15 newest submissions, Aug 17 07:43 through 23:57 UTC)
- mcpservers.org homepage (29 slug links, no new business-relevant)
- Cross-referenced against the 379-entry external catalog

## Catalogued (9)

### LucidRents Building Intelligence MCP ★★★
Apartment building intelligence from public records for NYC, LA, and Chicago (~2M buildings) — violations, 311 complaints, reviews, rents, and landlord portfolio records. Read-only, no auth, Streamable HTTP. `lucidrents.com/api/mcp`

### AwardCast MCP ★★★
Public US federal contracting data — SAM.gov solicitations, agency buying profiles, award history, recompete radar with named incumbents, closing-price ranges by agency/NAICS, forecast accuracy scorecard. No auth, 8 tools, citable search/fetch. `awardcast.ai/mcp` (repo ChosingDept/awardcast-mcp)

### StorePilot MCP ★★★
Whole app portfolio across Google Play and App Store Connect from one local MCP server — crash/ANR vitals vs Google's bad-behavior thresholds, anomaly detections, installs, ratings, earnings, reviews. stdio, `pip install storepilot`, MIT, 34 tools. `github.com/sonlenef/storepilot-mcp`

### Inside Ads MCP ★★
Pre-flight audience validation for shipped products — reach, click range, CPC against budget, with an explicit no-inventory verdict; then landing-page parse and campaign generation. OAuth, Streamable HTTP. `app.inside.ad/api/mcp` (repo inside-ad/claude-plugin)

### Bitroad MCP ★★
Marketplace where AI agents buy goods and services under spending caps, with returns and disputes as protocol features. Streamable HTTP. `app.bitroad.ai/api/v1/mcp` (repo bitroadai/bitroad-mcp)

### Secondhand MCP ★★
Search Facebook Marketplace, eBay, Depop, and Poshmark from any MCP client — price/condition/category/size/color filters, full listing details, deep-research search/fetch. Local npm (MIT) or hosted remote with OAuth. `secondhandmcp.com/mcp`

### Atono MCP Server ★★
Atono agile project management over MCP — backlog, bugs, sprints, epics, timeboxes, AI-generated investigation context, work-item updates. Docker, Apache-2.0. `github.com/atono-io/atono-mcp-server`

### xete MCP ★★
Encrypted agent messaging plus non-custodial Solana settlement — the agent drafts a payment it cannot sign (no signing path in code) and a separate verify tool proves the draft before a human signs. stdio, `uvx xete-mcp`

### Personhood MCP ★★
Rewrites AI-generated text to read as human in preset or custom persona voices for LinkedIn posts, cold emails, DMs, and tweets. Hosted, Bearer key, per-generation billing. `api.givepersonhood.com/mcp`

## Also Identified (not catalogued)

- **FineData.ai** — one-line listing ("Finedata MCP-server"), no tool docs (thin-docs rule)
- **cute-web-scraper** — capable local scraping utility (24 tools, no API key), saturated category
- **komnet** — git-backed coordination between coding agents, dev tool
- **Booklet** — markdown publishing for dev docs, dev tool
- **Dizko** — live city events, consumer
- **freshrss-mcp / linkwarden-mcp / audiobookshelf-mcp** — personal self-hosted media tools
- Repeats already catalogued or previously skipped: ListingGood, Mektup, TravelAnimator, AuraNet Omni-Oracle Engine

## Key Observation

The 9 finds split into three patterns. (1) Public records are the new no-auth data layer — LucidRents and AwardCast both package government and municipal records into free, credential-free agent surfaces, extending the public-data trend from GovTrade and Taiwan Law into real estate and federal procurement. (2) The human-gate is now being applied to money itself — xete's draft-then-verify settlement (agent drafts, cannot sign, independent verify before human signature) is the strongest enforcement yet of the agent-proposes-human-disposes doctrine, and Bitroad's spending caps apply the same idea to procurement. (3) Store operations are consolidating — StorePilot joins WisWes Magento and Mercopilot in making commerce surfaces agent-addressable, this time across both app stores at once. Personhood also marks the de-AI content stack's arrival as a hosted, per-generation-billed utility, sitting alongside Prose Coach and Etincel as the third delivery model for voice-controlled text.
