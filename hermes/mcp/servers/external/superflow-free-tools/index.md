---
title: "Superflow Free Tools MCP - Website QA and AI-Visibility Checks"
description: "Hosted keyless remote MCP server with 13 website QA and AI-visibility tools: check whether ChatGPT, Claude, Perplexity and Google AI can reach and cite a page, test robots.txt against every AI crawler, generate llms.txt and llms-full.txt, JSON-LD validation and generation, social preview checks, tech stack detection, full-page screenshots, alt text drafts, UTM builder, page-to-Markdown and favicon checks"
category: SEO
stars: n/a (new listing)
added: 2026-08-21
source: "mcp.so GitHub issue #3668"
relevance: ★★
tags: [seo, ai-visibility, llms-txt, robots-txt, json-ld, social-previews, tech-stack, utm, website-qa, remote-mcp, geo]
---

# Superflow Free Tools MCP

**Website QA and AI-visibility tooling as one keyless remote MCP server.** Superflow Free Tools exposes 13 QA tools over Streamable HTTP with no account and no API key: AI visibility checks across ChatGPT, Claude, Perplexity and Google AI, robots.txt testing against every major AI crawler, llms.txt generation following the llmstxt.org convention, JSON-LD validation and generation, social preview checks, tech stack detection, full-page screenshots, alt text drafts, a UTM builder, page-to-Markdown conversion, favicon checks and MD5 hashing.

```
Server type: Hosted remote (Streamable HTTP)
Endpoint: https://usesuperflow.ai/api/mcp
Auth: None (no account, no API key)
Tools: 13 (verified live Aug 21, 2026)
Server: superflow-free-tools v1.0.0
Registry: ai.usesuperflow/tools
Built by: Superflow (usesuperflow.ai)
```

## Why This Matters for Operators

AI-driven search is now a real acquisition channel, and almost nobody measures whether their site is reachable to the AI crawlers that matter. The individual checks here exist as scattered one-off tools; Superflow packs the whole pre-publish and post-publish QA loop into a single endpoint an agent can call mid-workflow. An agent drafting a landing page can generate the llms.txt, validate the JSON-LD, confirm the social preview renders on LinkedIn, and verify GPTBot can still crawl the robots.txt — all in the same conversation, with no setup beyond pointing the client at the URL.

The keyless design is the adoption hook: zero signup friction, tools are stateless and read-only (plus a UTM builder and MD5 hash), and the server runs on the vendor's infra.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `check_ai_visibility` | Checks whether ChatGPT, Claude, Perplexity and Google AI can reach, read, and cite a page |
| `check_robots_txt_for_ai` | Tests a site's robots.txt against GPTBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot and other AI crawlers |
| `generate_llms_txt` | Generates llms.txt and llms-full.txt for a site per the llmstxt.org convention, inventorying the site from robots.txt |
| `page_to_markdown` | Converts a page to clean CommonMark with navigation, cookie banners and boilerplate stripped |
| `generate_json_ld` | Writes a schema.org JSON-LD block for a page and validates it against the same checks a validator runs |
| `validate_json_ld` | Checks the structured data already on a page against Schema.org and what search engines accept |
| `check_social_preview` | Reads Open Graph and Twitter card tags and reports how the link renders on X, LinkedIn, Facebook, Slack, Discord |
| `detect_tech_stack` | Fingerprints a page to identify platform, framework, CMS, ecommerce apps, analytics, CDN and hosting |
| `check_favicon` | Verifies a site's favicon works, reading every icon declaration and fetching each one |
| `capture_full_page_screenshot` | Captures a full-height PNG in a real headless browser, scrolling so lazy content renders |
| `generate_alt_text` | Finds images on a page and drafts alt text using a vision model that actually looks at them |
| `build_utm_url` | Builds a campaign URL with UTM parameters normalized to one tagging convention and reports the GA4 default channel group |
| `hash_md5` | Hashes text to MD5 for checksums, cache keys and dedupe keys |

Live probe Aug 21, 2026: server `superflow-free-tools` v1.0.0, all 13 tools above confirmed on the endpoint.

## Installation

```bash
claude mcp add --transport http superflow https://usesuperflow.ai/api/mcp
```

```json
{
  "mcpServers": {
    "superflow": {
      "type": "http",
      "url": "https://usesuperflow.ai/api/mcp"
    }
  }
}
```

No API key, no account, no self-hosting. Any MCP client that supports Streamable HTTP can connect directly. Documentation lives at usesuperflow.ai/tools/mcp.

## Configuration

Nothing to configure. Tools are stateless: each call takes the URL or text it operates on as a parameter. Rate limits are not published; treat the free endpoint as best-effort and batch heavy crawls accordingly.

## Business Relevance

- **Marketing teams** validate every landing page's AI visibility, JSON-LD and social previews before launch
- **SEO operators** audit llms.txt and robots.txt coverage as AI search becomes a measurable channel
- **Content teams** produce clean Markdown, alt text and UTM-tagged campaign URLs from one toolset
- **Agencies** run competitor tech stack detection on prospects without a separate vendor tool

## Integration with CorpusIQ

The AI-visibility checks pair naturally with CorpusIQ's search console and analytics surfaces: `check_ai_visibility` and `check_robots_txt_for_ai` identify gaps in AI-crawler reach, CorpusIQ's Search Console connector tracks conventional Google performance on the same pages, and GA4 confirms whether traffic actually follows. For link campaigns, `build_utm_url` output can be fed straight into CorpusIQ's campaign tracking rather than hand-built tagging.

## Limitations

- 13 tools live (the directory submission lists 19; the endpoint exposes 13 as of Aug 21, 2026)
- Read-only QA tooling plus a UTM builder and MD5 hash — no crawl infrastructure, no indexing writes
- No published rate limits on the free keyless endpoint
- Tools operate on one URL per call; bulk site audits require the agent to loop

## See Also

- [Simplepages MCP — Landing Pages Built From Chat](/hermes/mcp/servers/external/simplepages-mcp/)
- [AdMapix MCP — Competitor Ad Creative Intelligence](/hermes/mcp/servers/external/admapix-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
