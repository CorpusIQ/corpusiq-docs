# MCP Sweep — July 26, 2026 (Afternoon Cron — ~18:00 UTC)

## Summary
- **Method:** mcpservers.org /all JSON-LD (30 newest) + mcp.so sitemap page 19 + chatmcp/mcpso GitHub issues
- **Compared against:** 93 existing catalog entries
- **New servers discovered since last sweep (July 26 12:00 UTC):** 2 (business-relevant)
- **Guides written:** 2

## Blockers
- **GitHub API rate-limited:** Authenticated `gh api` calls hit rate limit. Switched to unauthenticated `curl` for repo lookups. Individual repo API calls worked; `gh search repos` still blocked ("User flagged as spammy").
- **awesome-mcp-servers PR queue:** Rate limited, skipped this sweep.
- **Firecrawl:** Still unconfigured. All extraction via curl.

## New Servers Discovered

### 1. STEADYWRK Dispatch ★★★ — GUIDE WRITTEN
- **Source:** chatmcp/mcpso GitHub issue #3309 (submitted July 26, 2026)
- **Endpoint:** `https://steadywrk.app/api/mcp` (Streamable HTTP, POST-only JSON-RPC)
- **Description:** Field-service dispatch for AI agents — instant quotes, tracked work orders, and public evals across 8 trade verticals (HVAC, plumbing, electrical, roofing, general contracting, landscaping, pest control, cleaning). Public read tools (dispatch.evals, dispatch.index) are free with no signup. Quote/order tools require API key.
- **Website:** steadywrk.app — "Sovereign AI Company in Aqaba, Jordan"
- **Business relevance:** HIGH — First MCP server for field-service operations. Directly useful for property managers, facilities operators, construction companies, and any business that dispatches tradespeople. 8 verticals cover the most common field-service categories.
- **Category:** Operations / Field Service
- **Status:** Full integration guide written → [`steadywrk-dispatch-mcp.md`](/hermes/mcp/servers/external/steadywrk-dispatch-mcp/)

### 2. TendFeed ★★★ — GUIDE WRITTEN
- **Source:** chatmcp/mcpso GitHub issue #3300 (submitted July 25, 2026)
- **Endpoint:** `https://tendfeed.eu/api/mcp/tendfeed` (Streamable HTTP, stateless)
- **GitHub:** `github.com/tendfeed-eu/tendfeed-mcp` (0⭐, JavaScript, created July 25, 2026, MIT license)
- **Description:** Bid/no-bid intelligence for EU public tenders, built on 592,000 real TED contract awards — competition density, price corridors, SME fit scoring, and beachhead rankings for every open tender. Free guest tier for expired tender data (no signup); live board at 99 EUR/month.
- **Website:** tendfeed.eu — "See how many you are bidding against — before you calculate."
- **Business relevance:** HIGH — Procurement intelligence for any company bidding on EU public contracts. The 592K award dataset provides real competitive intelligence that replaces manual spreadsheet analysis. SME-fit scoring is particularly valuable for smaller operators who waste resources bidding on tenders they can't win.
- **Category:** Business Intelligence / Procurement
- **Status:** Full integration guide written → [`tendfeed-mcp.md`](/hermes/mcp/servers/external/tendfeed-mcp/)

## Previously Noted Servers (No Change)

| Server | Status | Why No Guide |
|--------|--------|--------------|
| BountyVerdict Agent Decision Tools | Noted July 23 | Developer-focused (GitHub bounties, CI flake detection, MCP tool drift). Not business ops. |
| Retasc | mcpservers.org /all | Unknown business model, no website content. Monitoring. |
| Santiment | mcpservers.org /all | Crypto market data — not general business ops. |
| AIQUAA Playwright | mcpservers.org /all | Testing tool for developers. |

## Already Cataloged (Confirmed, No Action)

The following servers appeared in today's scans but were already in our catalog from July 21 or earlier sweeps:
- FreshBooks MCP, BuiltWith MCP, KPI Depot MCP, 1ClickReport MCP (July 21)
- CDN.MN, TaskerArmy Agent, Reelier, Taplio, iGaming Tools, Outside Agent, Fixou, Argus Testing, KoreanAds, Routara LLM Gateway, AI Consensus, Index One, Agent Browser MCP (July 23-24 sweeps)
- FeatureBoard, Confluence to Markdown (July 23 sweep)
- Oromi Agent Services (July 26 morning sweep)

## mcpservers.org /all Page — Current Top 30

The JSON-LD extraction returned 30 servers. All 30 matched existing catalog entries (either full guides written or noted as low relevance). The `/all` page tracks the 30 most recently added servers — this confirms no new servers were added to mcpservers.org between our morning sweep (~12:00 UTC) and now (~18:00 UTC).

## mcp.so Sitemap Page 19 — Notable Non-Business Entries

~280 servers on page 19. Extracted all — overwhelming majority are test repos ("hello-world-test", "mcp-server-demo-*", "weather-mcp-server-*"), single-platform utilities (Pokemon, RuneScape, Minecraft), or non-English entries. Filtered to business-relevant candidates and cross-referenced against catalog — none were genuinely new and business-relevant. Examples of what was filtered:
- `mailchimp-mcp-server-by-cdata` — CData connector, likely wrapper (already covered by existing CData integrations)
- `shopify-mcp-server-abhi-tapestry` — Shopify (CorpusIQ covers this natively)
- `stripe-mcp-client` — Stripe (CorpusIQ covers this natively)
- `airwallex` — Cross-border payments (interesting but single-platform)
- Various `linkedin-ads-*`, `google-ads-*` — Covered by OpusGrowth MCP

## chatmcp/mcpso Issues — Full Scan

20 newest issues scanned (July 23-26):
- #3313: Removal request (service discontinued)
- #3312: health-export-mcp (Apple Health — consumer, not business ops)
- #3311: Engram MCP (SQLite agent memory — developer tool)
- #3310: Nauti-Labs Clearance (x402 payment flow — developer/infra)
- **#3309: STEADYWRK Dispatch — GUIDE WRITTEN ★★★**
- #3308: Sayba (AI agent social platform — consumer/social)
- #3307: PingCheck (status page monitoring — infra, medium relevance, no guide)
- #3304: hwatu (visual verification browser — developer tool)
- #3303: VK/VKontakte (Russia-specific social media)
- #3301: x-use (browser-native Twitter — covered by existing X/Twitter tools)
- **#3300: TendFeed — GUIDE WRITTEN ★★★**
- #3299: GoldBean (53 Chinese AI tools — noted July 25 morning)
- #3297: Prerender Buddy MCP (crawler visibility — noted July 25 morning)
- #3296: Humanity4AI (9 humanity skills — noted July 25 morning)
- #3295: Agentic Memory (persistent memory — noted July 25 morning)
- #3294: Polystrike (Polymarket tweet counters — crypto/niche)
- #3293: Skills Loader (noted July 25 morning, guide written)
- #3292: AIS Memory (persistent memory — developer tool)
- #3290: MartinLoop MCP Server (unknown, not in catalog)
- #3289: Meltema Weather (weather data — not business ops)

## Catalog Update
- **Added:** steadywrk-dispatch-mcp.md (full guide), tendfeed-mcp.md (full guide)
- **Index updated:** 93 → 95 servers, +2 guides
- **Total catalog:** 95 servers

## Next Sweep
- Next cron sweep scheduled. Focus sources: mcpservers.org /all page, chatmcp/mcpso issues (new submissions since #3313), mcp.so sitemap page 19 (check for new entries after 18:00 UTC).
- Consider adding mcpservers.org sitemap shard 6 scan for full coverage.
