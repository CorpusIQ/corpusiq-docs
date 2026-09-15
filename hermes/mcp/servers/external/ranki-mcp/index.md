---
title: "Ranki MCP - Free SEO and AEO Audits for AI Agents"
description: "Open-source SEO and AEO MCP: 22 tools for on-page audits, Core Web Vitals, image optimization, sitemap llms.txt and robots generation plus AI-citation visibility, hosted at mcp.ranki.io with npm stdio fallbacks. MIT, free tier."
category: SEO
stars: "0 (new listing, 1fancy/seo-aeo-audit-mcp-ranki)"
added: 2026-09-01
source: "mcpservers.org /all page 1 - rankdelta-ai listing (Sep 1, 2026 morning sweep)"
relevance: ★★★
tags: [mcp-server, seo, aeo, geo, core-web-vitals, llms-txt, image-optimization, audits]
---

# Ranki MCP

**Open-source SEO and AEO MCP that does not just report - it drives the fix.** Ranki audits any URL for SEO and Answer Engine Optimization, measures real Core Web Vitals through Google PageSpeed Insights, and then instructs the agent to convert images, rewrite tags, drop in JSON-LD schema and generate sitemap.xml, llms.txt and robots.txt - then re-runs the audit to prove the score moved. 22 tools, hosted and self-hostable.

```
Server type: Hosted (mcp.ranki.io) plus npm stdio implementations
Endpoint: https://mcp.ranki.io (X-API-Key header for the full tier)
Auth: free advisor tier, no key (5 calls per IP per day); Ranki.io API key lifts to 500 calls per day
npm: @ranki.io/seo-aeo-mcp (TypeScript server), @ranki.io/mcp (stdio shim for the hosted server)
Repo: github.com/1fancy/seo-aeo-audit-mcp-ranki (MIT, created Jun 2026)
Website: ranki.io
Tools: 22 (audits, speed, image optimization, generators, content strategy, GSC bridge)
```

## Why This Matters for Operators

Most SEO tools describe the problem and stop. Ranki is built so the agent completes the fix inside the editor.

First, **audits with literal fix recipes.** audit_seo returns a 10-check scorecard with per-failure recipes, and audit_core_web_vitals names the exact file slowing the page ("LCP element is hero.png at 2.4 MB, convert to WebP saves 1.8 MB"). An agent gets an actionable work order, not a score.

Second, **AEO is treated as a first-class surface.** audit_aeo checks the signals that decide whether ChatGPT, Claude and Perplexity cite your site - FAQPage JSON-LD, llms.txt presence, crawler permissions, definitional intros - which is the discovery channel operators keep losing because legacy tools never score it.

Third, **the loop closes.** After the fixes, the agent re-runs the audit to prove the score moved, and the ai_visibility bridge tool shows which tracked topics actually appeared in AI answers at capture time. That is measurement, not vibes.

## Tools and Capabilities

All 22 tools are documented in the repo README with schemas. npm packages verified published Sep 1, 2026.

| Area | Tools | What they do |
|------|-------|--------------|
| Audits | `audit_seo`, `audit_aeo`, `audit_hidden_pages` | Scorecards with fix recipes; classifies hidden paths into a ready robots.txt block |
| Speed and images | `audit_speed`, `audit_core_web_vitals`, `optimize_images` | Real Lighthouse and CWV data via PageSpeed Insights; AVIF/WebP conversion commands and responsive picture markup |
| Generators | `generate_sitemap_xml`, `generate_llms_txt`, `generate_robots_txt` | Deploy-ready baseline files for search and AI crawlers |
| Content strategy | `seo_starter_kit`, `find_topic_ideas`, `find_keyword_gap`, `propose_titles_metas`, `explain_seo_terms` | Starter files, topic briefs, gap methodology, title and meta candidates, glossary |
| Ranki.io bridge | `get_account`, `list_projects`, `list_articles`, `get_article`, `list_rank_tracking`, `list_gsc_keywords`, `ai_visibility` | Real GSC keywords, rank tracking, AI citations and the article library from a Ranki.io account |
| Install | `install_skill` | Install commands for the companion ranki-seo-skills across Claude, Cursor, Windsurf and more |

## Installation

The hosted endpoint plus a one-line stdio installer:

```bash
npx @ranki.io/cli install
```

Manual config for the hosted server with an API key:

```json
{
  "mcpServers": {
    "ranki": {
      "url": "https://mcp.ranki.io",
      "headers": { "X-API-Key": "rk_live_..." }
    }
  }
}
```

## Configuration

No key needed for the free advisor tier: 15 tools, 5 calls per IP per day. A Ranki.io API key (auto-created for every account at app.ranki.io/developer) lifts the cap to 500 calls per day and unlocks all 22 tools including the bridge tools that read real GSC keywords, rank tracking, AI citations and the article library from your Ranki.io account. Two npm packages provide stdio paths: the TypeScript server and the hosted-server shim.

## Business Relevance

- **Operators who ship sites fast** get the four baseline files (robots, sitemap, llms.txt, JSON-LD) most launched sites are missing, generated in one call.
- **Content teams** get topic briefs, title and meta candidates and keyword-gap methodology without a paid keyword subscription.
- **Anyone answering "why are we invisible to ChatGPT"** gets an AEO scorecard plus recorded AI-citation snapshots.
- **Developers** get image conversion commands and responsive markup as literal output, ready to commit.

## Integration with CorpusIQ

Ranki composes with CorpusIQ as the organic-acquisition half of a growth loop. CorpusIQ answers from the revenue and pipeline side (Stripe, HubSpot, Google Ads) while Ranki audits and fixes the organic surface: Core Web Vitals, AI-crawler readiness, schema and llms.txt. An operator can ask "fix our AI visibility, then tell me whether the pages people find actually convert" and get the audit, the fix and the revenue answer in one workflow. Pairs naturally with CiteRank for AI-search visibility benchmarking and with the ni-c Search Console MCP for property-level query data.

## Limitations

- Free tier is small (5 calls per IP per day); sustained work needs the Ranki.io API key tier.
- Bridge tools (GSC, rank tracking, articles, AI citations) only return data for projects inside a Ranki.io account.
- Hosted endpoint answered route negotiation on an anonymous probe Sep 1, 2026 (405 at root, 404 at /mcp); the npm stdio packages are the verified consumable path and the README config is the source of record for the endpoint.
- Brand new repo, zero stars; expect early-stage changes.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [CiteRank MCP - AI Search Visibility & GEO Audits for AI Agents](/docs/hermes/mcp/servers/external/citerank-mcp)
- [Google Search Console MCP (ni-c) - Property Setup and Search Analytics](/docs/hermes/mcp/servers/external/google-search-console-ni-c-mcp)
- [Seomely MCP](/docs/hermes/mcp/servers/external/seomely-mcp)
