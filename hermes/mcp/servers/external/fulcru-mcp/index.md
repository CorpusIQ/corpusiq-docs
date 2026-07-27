# Fulcru MCP — AI Search Visibility with Execution Arm

**Priority:** HIGH | **Category:** Marketing / SEO  
**Transport:** Remote Streamable HTTP | **Auth:** Bearer token  
**Repository:** [gsmmediaro/fulcru-agent](https://github.com/gsmmediaro/fulcru-agent) (AGPL-3.0)  
**Website:** https://fulcru.app  
**Discovered:** July 27, 2026 (chatmcp/mcpso #3318)

## What It Does for Operators

Fulcru finds the questions where ChatGPT, Gemini, and Perplexity name your competitor instead of you — then writes the page that closes that gap and measures whether it worked. Most AI-visibility tools stop at a score. Fulcru carries the loop all the way through to measured outcomes.

**This is the first MCP server that closes the AI-SEO loop end-to-end.** For business operators who depend on AI-driven search traffic, knowing what AI assistants say about your brand vs competitors is existential.

## Installation

```bash
# Remote endpoint (no local install)
# Auth: get Bearer token from https://fulcru.app integrations page
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "fulcru": {
      "url": "https://little-orca-977.convex.site/mcp",
      "transport": "streamable-http",
      "headers": {
        "Authorization": "Bearer YOUR_FULCRU_TOKEN"
      }
    }
  }
}
```

## Tools (5)

| Tool | Description |
|------|-------------|
| `fulcru_visibility` | Current AI visibility score and competitive landscape |
| `fulcru_gaps` | Exact prompts where competitors are named instead of you |
| `fulcru_write_page` | Drafts the article targeting a specific gap, grounded in cited sources |
| `fulcru_publish_page` | Snapshots the mention rate at publish time for before/after comparison |
| `fulcru_delta` | Reports what changed after publishing — the actual result |

## Operator Use Cases

1. **Competitive AI share-of-voice:** "What questions do ChatGPT/Gemini answer with a competitor's brand instead of ours?" — run `fulcru_gaps`, identify top 5 competitor mentions, prioritize by search volume
2. **Content ROI measurement:** Publish a page targeting a specific AI query, then measure `fulcru_delta` after 2 weeks to see if AI assistants now cite your brand instead
3. **Product launch monitoring:** When launching a new feature, use `fulcru_visibility` to track whether AI assistants surface it when users ask about the category
4. **M&A due diligence:** Check a target company's AI visibility before acquisition — are they winning the AI search war in their category?
5. **Agency reporting:** For operators running client engagements, Fulcru provides hard numbers on AI visibility improvement

## CorpusIQ Angle

**Complementary.** CorpusIQ provides cross-source business data (financials, operations, marketing analytics). Fulcru adds the AI-search layer that's increasingly critical for operator decision-making. Operators could use CorpusIQ to identify revenue-impacted segments, then use Fulcru to close the AI-visibility gaps in those segments.

## Limitations

- Remote-only (no local install), depends on fulcru.app uptime
- AGPL-3.0 license
- Requires paid subscription for production use
- New product (submitted July 2026), may have evolving API surface
