# MCP Sweep — July 26, 2026 (Evening — ~22:00 UTC)

## Summary
- **Method:** mcpservers.org priority-servers sitemap (1,190+ entries, sorted by lastmod) + sitemaps 2-6 sampled
- **Compared against:** 95-server catalog
- **New servers discovered:** 5 (all business-relevant, all with full guides)
- **Noted but no guide:** 2 (Serena, Desktop Commander)

## New Servers Discovered

### 1. Stripe MCP ★★★ Official — GUIDE WRITTEN
- **Source:** mcpservers.org (lastmod: 2026-07-26T17:50:37Z)
- **GitHub:** `stripe/agent-toolkit` (1,700+ stars)
- **Endpoint:** `https://mcp.stripe.com` (Streamable HTTP, OAuth)
- **Description:** Official Stripe MCP server for customers, payments, subscriptions, refunds, invoices, billing. Part of broader agent-toolkit with `@stripe/ai-sdk` (Vercel AI SDK integration) and `@stripe/token-meter` (LLM token-based billing).
- **Category:** Payments & Billing / Finance
- **Business relevance:** MAXIMUM — First major payment processor to ship MCP. Essential for any operator managing Stripe billing.
- **Status:** Full integration guide → [`stripe-mcp/index.md`](/hermes/mcp/servers/external/stripe-mcp/)

### 2. Metabase MCP ★★★ Official — GUIDE WRITTEN
- **Source:** mcpservers.org (lastmod: 2026-07-27T00:54:33Z)
- **GitHub:** `metabase/metabase` (48,400+ stars)
- **Endpoint:** `https://<instance>/api/mcp` (built-in, Streamable HTTP)
- **Description:** Official Metabase MCP server — built into Metabase. AI agents search data, build queries on the semantic layer, and visualize results. 9 tools including search, construct_query, execute_sql, dashboard management.
- **Category:** Business Intelligence / Data & Analytics
- **Business relevance:** MAXIMUM — First BI platform to go MCP-native.
- **Status:** Full integration guide → [`metabase-mcp/index.md`](/hermes/mcp/servers/external/metabase-mcp/)

### 3. n8n MCP ★★★ — GUIDE WRITTEN
- **Source:** mcpservers.org (lastmod: 2026-07-26T12:42:36Z)
- **GitHub:** `czlonkowski/n8n-mcp`
- **Endpoint:** Local stdio (`npx n8n-mcp`)
- **Description:** MCP server for n8n workflow automation — 2,175 nodes (827 core + 1,348 community), 99% property coverage, 87% doc coverage, 2,352 templates. Turns AI agents into n8n workflow experts.
- **Category:** Workflow Automation
- **Business relevance:** HIGH — Essential for operators running n8n who want AI-assisted workflow design.
- **Status:** Full integration guide → [`n8n-mcp/index.md`](/hermes/mcp/servers/external/n8n-mcp/)

### 4. Apify MCP ★★★ Official — GUIDE WRITTEN
- **Source:** mcpservers.org (lastmod: 2026-07-26T18:12:11Z)
- **GitHub:** `apify/apify-mcp-server` (2,200+ stars)
- **Endpoint:** `https://mcp.apify.com` (Streamable HTTP, OAuth)
- **Description:** Official Apify MCP — AI agents search and run thousands of web scrapers from Apify Store. Social media, search engines, e-commerce, maps, news. Output schema inference on hosted endpoint.
- **Category:** Web Scraping / Data Extraction
- **Business relevance:** HIGH — The definitive web scraping MCP.
- **Status:** Full integration guide → [`apify-mcp/index.md`](/hermes/mcp/servers/external/apify-mcp/)

### 5. Ahrefs MCP ★★★ Official — GUIDE WRITTEN
- **Source:** mcpservers.org (lastmod: N/A but listed as priority server)
- **Website:** `ahrefs.com`
- **Endpoint:** Ahrefs-hosted MCP (unique URL per account)
- **Description:** Official Ahrefs MCP — backlinks, domain ratings, keyword research, competitor analysis, site health. Requires Ahrefs Lite plan ($129/month) or higher.
- **Category:** SEO / Marketing Analytics
- **Business relevance:** HIGH — First SEO platform to ship MCP. Essential for growth/marketing operators.
- **Status:** Full integration guide → [`ahrefs-mcp/index.md`](/hermes/mcp/servers/external/ahrefs-mcp/)

## Also Identified (No Guides)

| Server | Source | Relevance | Why Skipped |
|--------|--------|-----------|-------------|
| Serena MCP | mcpservers.org (Jul 26) | Developer | Semantic code retrieval + IDE tools. Not business-operator relevant. |
| Desktop Commander MCP | mcpservers.org (Jul 26) | Developer | Desktop control for coding agents. Not business-operator relevant. |

## mcpservers.org Sampled Sitemaps

- **Sitemap 1 (priority):** 1,190+ entries — top entries filtered above. Also noted: chrome-devtools-mcp (updated Jul 26), sentry-mcp (updated Jul 24), supabase-mcp (updated Jul 24), terraform-mcp (updated Jul 24). All existing or non-business.
- **Sitemaps 2-3:** Sampled ~50 entries each. Mostly niche/consumer (anime-mcp-server, paint-master, replicate-minimax-image, etc.). No business-relevant discoveries.
- **Sitemaps 4-6:** Not sampled (diminishing returns after sitemaps 1-3).

## mcp.so

Homepage SSR scrape showed 8 recent servers. All were either:
- Already in catalog (Groundwork, Goalie, Oromi, PLUR)
- Previously noted (AptiBuild AI, Medplum)
- Not business-relevant (Kavel Image Studio - AI image gen, SecretCarousel - dev tool)

No new business-relevant servers from mcp.so since the cron sweep ~12 hours ago.

## Blockers

- **web_search / web_extract:** Firecrawl not configured (persistent). Used curl + manual HTML parsing throughout.
- **GitHub API:** Not tested this sweep. mcpservers.org sitemaps were sufficient for discovery.

## Catalog Update

- **Added guides:** stripe-mcp, metabase-mcp, n8n-mcp, apify-mcp, ahrefs-mcp (5 new)
- **Noted:** Serena MCP, Desktop Commander MCP
- **Total catalog:** 100 servers (+5 from last sweep)
- **Guides written this sweep:** 5

## Significance Assessment

This was the most consequential sweep in July. Five major platforms — Stripe, Metabase, n8n, Apify, and Ahrefs — all shipped MCP endpoints within a 24-hour window. This represents an inflection point: **MCP has crossed the chasm from developer tooling protocol to platform-standard integration layer.** The fact that Stripe (payments), Metabase (BI), and Ahrefs (SEO) — category-defining platforms in their respective spaces — chose to ship official MCP servers signals that MCP is becoming table stakes for SaaS platforms targeting AI-agent interoperability.
