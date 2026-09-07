---
title: "RankCLI MCP - Local SEO and GEO Audits for AI Agents"
description: "RankCLI MCP runs free local SEO and GEO checks entirely on the operator's machine: a comprehensive SEO audit plus AI-search-visibility analysis (GPTBot, ClaudeBot, PerplexityBot access and LLM-friendliness), focused single-purpose checks, and generator tools for robots.txt, schema markup and security headers. No signup, no API key."
category: SEO
stars: 0
added: 2026-09-07
source: "chatmcp/mcpso issue #3963"
relevance: ★★
tags: [seo, geo, ai-crawlers, audits, stdio, local, robots-txt, schema]
---

# RankCLI MCP - Local SEO and GEO Audits for AI Agents

**Local stdio MCP server (npm, MIT)** - RankCLI packages 280+ automated SEO and GEO checks behind a small MCP tool surface that runs entirely on the operator's machine: nothing is sent to any server, no signup and no API key. The agent can run full audits, focused checks and even generate the fixes (robots.txt, schema, security headers) directly.

```
Server type: Local (stdio, Node.js)
Auth: None (optional account linking only for dashboard history and GitHub auto-fix PRs)
Install: npx @rankcli/mcp-server
Tools: 13 (audits, focused checks, generators, account linking)
Pricing: Free
Category: SEO
Built by: RankCLI (rankcli.dev); repo github.com/integrallis/rankcli-cli
```

## Why This Matters for Operators

SEO tooling has moved to the cloud, which means every audit requires an account, a subscription and a pipeline that ships site data to a vendor. RankCLI MCP inverts that: the checks run locally and the agent is the interface. For operators who would rather ask "how is our site doing on structured data, Core Web Vitals and AI-crawler access" in a conversation than log into yet another dashboard, that is the right shape.

**The GEO checks are the forward-looking half: GPTBot, ClaudeBot and PerplexityBot access plus LLM-friendliness signals are exactly the factors that decide whether AI answer engines can cite the site at all.**

## Tools & Capabilities

| Group | Tools |
|---|---|
| Comprehensive audits | seo_analyze (on-page, structured data, security headers, mobile, images, internal linking), seo_geo_check (AI-search visibility) |
| Focused checks | seo_core_web_vitals, seo_structured_data, seo_security_headers, seo_images, seo_internal_links, seo_mobile, seo_ai_crawlers |
| Fix generation | seo_generate_robots, seo_generate_schema, seo_generate_security_headers |
| Optional account linking | rankcli_connect / rankcli_disconnect for dashboard history and GitHub auto-fix PRs |

## Installation

```bash
npx @rankcli/mcp-server
```

## Configuration

```json
{
  "mcpServers": {
    "rankcli": {
      "command": "npx",
      "args": ["@rankcli/mcp-server"]
    }
  }
}
```

No environment variables required. The optional rankcli_connect flow links the CLI to the dashboard for history and auto-fix pull requests; audits and generators work fully offline without it.

## Business Relevance

- **SEO teams** run audit cycles inside the agent instead of a separate tool subscription.
- **Founders** get an instant AI-visibility read on their site before launching GEO work.
- **Developers** ship schema, robots and header fixes the agent generates as files, reviewable in a PR.
- **Agencies** run client audits locally, keeping site data in-house.

## Integration with CorpusIQ

RankCLI audits the site's technical and AI-visibility surface; CorpusIQ measures the outcome. A composed workflow: the agent runs RankCLI checks, applies the generated schema and robots fixes, then tracks the resulting organic traffic and conversions through CorpusIQ's GA4 connector to close the loop.

## Limitations

- Brand new listing (issue #3963, Sep 6, 2026); repo and npm package are days old (0 stars).
- Local stdio only - no hosted endpoint; the agent must run where the repo lives.
- SEO audit depth is the 280-check battery, but no keyword rank tracking or backlink data.

## See Also

- [Ranki MCP - SEO and AEO Audits](/hermes/mcp/servers/external/ranki-mcp/)
- [Encited MCP - SEO and AI Visibility for Agents](/hermes/mcp/servers/external/encited-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
