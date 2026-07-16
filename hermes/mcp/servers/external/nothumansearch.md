---
title: "NotHumanSearch — AI Agent Search Engine"
description: "Connect NotHumanSearch MCP to understand how AI agents discover and rank your business. Optimize for agentic search visibility."
category: mcp
tags: [mcp, geo, ai-search, agentic-seo, nothumansearch, visibility]
last_updated: 2026-07-08
---

# NotHumanSearch — AI Agent Search Engine for Operators

NotHumanSearch is a search engine built for AI agents — not humans. It ranks sites by agentic readiness: llms.txt files, OpenAPI specs, MCP endpoints, and AI plugin manifests. As AI agents become the primary consumers of web content, traditional SEO metrics (PageRank, backlinks) become less relevant. NotHumanSearch measures what AI agents actually care about.

## Why This Matters for Operators

- **Paradigm shift**: AI agents increasingly browse the web on behalf of users — your site needs to be discoverable by AI, not just humans
- **New ranking factors**: llms.txt, structured APIs, MCP endpoints, and JSON-LD matter more than backlinks
- **Competitive intelligence**: See which competitors are agent-ready and where you're falling behind
- **Actionable fixes**: Get specific recommendations to improve agentic discoverability

## Quick Start

```bash
# Add to Hermes
hermes mcp add nothumansearch -- npx -y @unitedideas/nothumansearch-mcp

# Or via GitHub
git clone https://github.com/unitedideas/nothumansearch
cd nothumansearch
npm install
```

## Core Capabilities

| Tool | What It Does |
|------|-------------|
| Search | Search across all indexed sites by agentic readiness score |
| Rank Check | Check where your domain ranks for specific queries |
| Audit | Full agentic-readiness audit of your site |
| Competitors | See which competitors rank above you and why |
| Recommendations | Get prioritized fixes to improve agentic visibility |

## Usage Patterns

### Check Your Agentic Readiness

```python
# Audit your site for AI agent discoverability
audit = mcp_nothumansearch(
    action="audit_site",
    params={"domain": "yourcompany.com"}
)
# Returns: {
#   agentic_score: 72/100,
#   has_llms_txt: false,      ← CRITICAL FIX
#   has_openapi_spec: true,
#   has_mcp_endpoint: false,   ← HIGH PRIORITY
#   has_jsonld: true,
#   recommendations: [...]
# }
```

### Competitive Agentic Intelligence

```python
# See who AI agents find when searching for your keywords
competitors = mcp_nothumansearch(
    action="search",
    params={
        "query": "business analytics platform",
        "perspective": "ai_agent"  # Search as an AI agent would
    }
)
# Returns sites ranked by agentic readiness, not human SEO metrics
for site in competitors.results:
    print(f"{site.domain}: agentic_score={site.score}, has_llms_txt={site.features.llms_txt}")
```

### Fix What AI Agents Can't See

```python
# Get prioritized recommendations
recommendations = mcp_nothumansearch(
    action="get_recommendations",
    params={"domain": "yourcompany.com"}
)

for rec in recommendations.prioritized:
    # Example outputs:
    # 1. Add llms.txt (impact: HIGH, effort: LOW)
    # 2. Register MCP endpoint (impact: HIGH, effort: MEDIUM)
    # 3. Add ai-plugin.json manifest (impact: MEDIUM, effort: LOW)
    # 4. Publish OpenAPI spec at /openapi.json (impact: MEDIUM, effort: MEDIUM)
    print(f"{rec.priority}. {rec.title} (impact: {rec.impact}, effort: {rec.effort})")
```

## Operator Playbook: Agentic SEO Pipeline

1. **Audit**: Run `audit_site` on your domain → get agentic score + gap analysis
2. **Fix**: Implement top recommendations (llms.txt is always #1)
3. **Monitor**: Weekly rank checks for your target keywords from AI agent perspective
4. **Compete**: Track competitor agentic scores and reverse-engineer their approach
5. **Report**: Monthly agentic visibility report alongside traditional SEO metrics

## The Essentials Checklist

What every site needs for AI agent discoverability:

| Asset | Priority | Effort | Impact |
|-------|----------|--------|--------|
| **llms.txt** at root | CRITICAL | 10 min | HIGH |
| **OpenAPI spec** at /openapi.json | HIGH | 1-2 hrs | HIGH |
| **JSON-LD** structured data | HIGH | 30 min | MEDIUM |
| **MCP endpoint** (if applicable) | HIGH | varies | HIGH |
| **ai-plugin.json** manifest | MEDIUM | 20 min | MEDIUM |
| **Robots.txt** for AI crawlers | MEDIUM | 5 min | MEDIUM |
| **Sitemap.xml** updated | LOW | auto | LOW |

## Complementary Tools

| Tool | Purpose |
|------|---------|
| MentionsAPI | Track if AI models recommend your brand |
| Geoly GEO MCP | AI brand visibility reporting |
| getAdvantage MCP | Scan how ChatGPT/Claude read your app |
| SEOcrawl AI | Traditional SEO + GEO combined |
| Rampify | Crawl site for AI-visibility gaps |

## Why This Is a New Category

Traditional SEO optimized for Google's PageRank. But AI agents don't use PageRank — they read llms.txt, consume structured APIs, and evaluate MCP endpoints. NotHumanSearch measures what matters to AI agents. Operators who optimize for agentic search now will own this channel before it gets crowded.

---

*Integration guide for CorpusIQ operators. NotHumanSearch is a community project by @unitedideas. Agentic search is an emerging category — rankings and methodology may evolve rapidly.*
