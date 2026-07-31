---
title: "AfterLaunch MCP — Integration Guide"
description: "Agentic growth marketing MCP — 29 tools for AI answer visibility, growth backlog, and shipping actions across ChatGPT, Gemini, Perplexity, and Google AI Overviews."
category: mcp
tags: [mcp-server, growth-marketing, seo, geo, ai-visibility, marketing-automation, hermes-agent]
last_updated: 2026-07-30
---

# AfterLaunch MCP — AI Growth Marketing for Hermes Agent

AfterLaunch is an AI growth marketing agent that operates as an MCP server — 29 tools covering AI answer visibility, ranked growth backlogs, drafted deliverables, and ship actions. It monitors how your brand appears across ChatGPT, Gemini, Perplexity, and Google AI Overviews, then gives your agents a prioritized feed of what to ship next.

## What It Does

AfterLaunch turns growth marketing into agent-native tools:

- **AI Answer Visibility** — Query what ChatGPT, Gemini, Perplexity, and Google AI Overviews say about your product, competitors, and category. See where you're mentioned, where competitors are, and where gaps exist.
- **Ranked Growth Backlog** — A prioritized feed of growth moves (content, SEO fixes, GEO optimizations, distribution plays) ordered by expected impact.
- **Drafted Deliverables** — Each growth move comes with a draft (blog post outline, landing page copy, social thread, schema markup) ready for refinement and publishing.
- **Ship Actions** — Execute the growth moves: publish content, submit to directories, update schema, trigger re-indexing, and more.
- **Anonymous Discovery** — Query visibility data without an API key (rate-limited). Sign up for full access.

### 29 Tools

| Category | Tools | Description |
|----------|-------|-------------|
| **Visibility** | `check_visibility`, `check_competitor_visibility`, `check_category_visibility` | Query AI answer engines for your brand, competitors, and category terms |
| **GEO Audit** | `audit_geo_presence`, `audit_schema_gaps`, `audit_content_gaps` | Audit your Generative Engine Optimization readiness |
| **Backlog** | `get_growth_backlog`, `prioritize_backlog`, `get_next_move` | Ranked, prioritized feed of what to ship next |
| **Content** | `draft_content`, `optimize_content`, `generate_schema` | Draft blog posts, optimize for GEO, generate structured data |
| **Distribution** | `submit_to_directory`, `syndicate_content`, `schedule_social` | Distribute content across platforms |
| **Analytics** | `track_visibility_trend`, `measure_impact`, `get_competitor_moves` | Track visibility changes and measure growth impact |
| **Shipping** | `ship_content`, `ship_schema`, `trigger_reindex` | Execute and publish growth actions |

### Why It Matters for Operators

Traditional SEO tools (Ahrefs, Semrush) tell you about Google rankings. AfterLaunch tells you about AI answer visibility — the surface that's rapidly replacing traditional search. If your product isn't mentioned when someone asks ChatGPT "best business analytics platform," you're invisible to an audience that's growing 40% month-over-month. AfterLaunch closes that gap with tools your AI agents can use directly.

**Competitive landscape:** Similar to Fulcru MCP (search visibility with execution arm, catalogued July 27) but broader — Fulcru focuses on content gap analysis while AfterLaunch adds GEO optimization, AI answer monitoring across 4 engines, and direct shipping actions.

## Quick Setup

### Prerequisites
- **AfterLaunch account:** Sign up at [afterlaunch.io](https://afterlaunch.io)
- **MCP-compatible client:** Claude Code, Codex, Cursor, Hermes Agent, or any HTTP MCP client

### Connection Details

| Field | Value |
|-------|-------|
| **Transport** | Streamable HTTP (Remote) |
| **Endpoint** | `https://afterlaunch.io/api/mcp` |
| **Authentication** | API key (optional for discovery; required for ship actions) |
| **Tools** | 29 |
| **MCP Registry** | `io.afterlaunch/agentic-growth-marketing` v1.0.0 |

### Anonymous Discovery (No Key Required)

```bash
curl -s -X POST https://afterlaunch.io/api/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":1}'
```

### Add to Hermes Agent

```json
{
  "mcpServers": {
    "afterlaunch": {
      "transport": "http",
      "url": "https://afterlaunch.io/api/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_AFTERLAUNCH_API_KEY"
      }
    }
  }
}
```

### Environment Variables

```bash
export AFTERLAUNCH_API_KEY="al_..."
```

## Example Usage

### Check Your AI Visibility

Ask your agent: *"What does ChatGPT say about us vs our competitors?"*

The agent calls `check_visibility` and `check_competitor_visibility` to surface where you appear, where competitors appear, and the gap analysis — all in one pass.

### Generate a GEO-Optimized Blog Post

Ask your agent: *"Write a blog post about [topic] optimized for AI answer engines."*

The agent calls `draft_content` with GEO optimization parameters, returns a draft structured for AI answer visibility, then `ship_content` publishes it.

### Get Your Growth Backlog

Ask your agent: *"What growth moves should we ship this week?"*

The agent calls `get_growth_backlog` and `prioritize_backlog` to return a ranked list with expected impact scores, drafted deliverables, and shipping instructions.

## Pricing

AfterLaunch offers a free tier with anonymous discovery (rate-limited). Paid tiers unlock full tool access, higher rate limits, and ship actions. Check [afterlaunch.io/pricing](https://afterlaunch.io/pricing) for current plans.

## Repository & Resources

| Resource | URL |
|----------|-----|
| **GitHub** | [github.com/afterlaunch/mcp](https://github.com/afterlaunch/mcp) |
| **Website** | [afterlaunch.io](https://afterlaunch.io) |
| **Developer Docs** | [afterlaunch.io/developers](https://afterlaunch.io/developers) |
| **MCP Registry** | `io.afterlaunch/agentic-growth-marketing` |

## Verdict: ★★★ — Essential for Growth Operators

AfterLaunch is the first MCP server that gives AI agents direct visibility into AI answer engines and the tools to act on that data. For any business operator running growth through AI agents, this is a category-defining tool. The anonymous discovery tier means you can test it without commitment.

**Strengths:** 29 tools covering the full GEO pipeline (audit → backlog → draft → ship), anonymous discovery, multi-engine visibility (ChatGPT + Gemini + Perplexity + Google AIOs), agent-native design.

**Limitations:** Brand new (0 GitHub stars, created July 30, 2026), unproven at scale, unclear what the free tier rate limits are, ship actions require paid tier.

**Best for:** SaaS founders, growth marketers, and AI-native operators who want their agents to manage GEO and AI answer visibility without switching contexts.
