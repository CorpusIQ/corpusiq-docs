---
title: "Riddle Quiz Maker MCP — Interactive Content and Lead Generation from AI Clients"
description: "Official vendor MCP from Riddle.com: create and manage quizzes, polls, surveys, personality tests, forms, predictors, minigames and leaderboards with 62 tools — branching logic, custom design, live stats, lead capture and embed code — over Streamable HTTP with OAuth."
category: Marketing
stars: n/a (new listing)
added: 2026-08-21
source: mcp.so
relevance: ★★★
tags: [quiz, lead-generation, interactive-content, surveys, polls, marketing, oauth, remote-mcp]
---

# Riddle Quiz Maker MCP

**The official Riddle.com MCP server — 62 tools that let an AI client build, publish and measure interactive content end to end.** Riddle is an established quiz and interactive-content platform used for lead generation; its MCP surface exposes the Creator API so an agent can draft a personality test, wire the branching logic, publish it and pull live stats without leaving the conversation. Templates, design, leaderboards, predictions and embed codes are all tool-addressable.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth
Endpoint: https://www.riddle.com/creator/api/v3/mcp
Tools: 62 (creation, templates, stats, embed, lead capture)
Pricing: Riddle.com plans (not published on listing)
Category: Marketing
Built by: Riddle.com (github.com/riddle-com)
```

## Why This Matters for Operators

Interactive content is the highest-converting top-of-funnel format most marketing teams skip because building a branching quiz takes a day in a dashboard. **Riddle's MCP makes the agent the builder:** describe the audience and the outcome you want — a lead-qualification quiz, a segmenting personality test, a product recommender — and the tools create it with branching logic and embed code in minutes.

Because stats and lead data live behind the same endpoint, the follow-up question ("how did Tuesday's quiz perform, and which answers map to which leads") is one more tool call rather than a dashboard export.

## Tools & Capabilities

62 tools cover the full content lifecycle. Representative families:

| Tool family | Purpose |
|---|---|
| `riddleTemplate_create` / `_list` / `_publicList` / `_get` / `_use` | Save, list and reuse templates — personal, project and Riddle's public library |
| Quiz / poll / survey creation | Build any Riddle type with branching logic and custom design |
| Stats & results | Live performance data, per-answer breakdowns, leaderboards |
| Lead capture | Collect and export leads from forms and gated quizzes |
| Embed & publish | Generate embed code for any site |

The listing shows the template family in full detail; the remaining tools cover the other Riddle types (quiz, poll, survey, personality test, form, predictor, minigame, leaderboard).

## Installation

```bash
claude mcp add riddle --transport http https://www.riddle.com/creator/api/v3/mcp
```

Per-client walkthroughs (Claude Code, Codex, Cursor, VS Code) are published on the vendor's help site at riddle.com/help/api/mcp.

## Configuration

```json
{
  "mcpServers": {
    "riddle": {
      "type": "http",
      "url": "https://www.riddle.com/creator/api/v3/mcp"
    }
  }
}
```

OAuth sign-in on first connect. Project-scoped permissions gate template operations; publishing and embed generation run against the connected Riddle.com account.

## Business Relevance

- **Marketing teams** ship lead-gen quizzes and personality tests without a designer or developer
- **E-commerce operators** build product-recommender quizzes that segment visitors before checkout
- **HR and L&D** run polls, surveys and scored assessments with live stats
- **Publishers** grow engagement with predictors, minigames and leaderboards embedded in articles

## Integration with CorpusIQ

Riddle is the acquisition layer; CorpusIQ is the measurement layer. A composed workflow has Riddle's tools publish a gated quiz and capture leads while CorpusIQ's GA4 connector tracks the traffic that reached it and Klaviyo flows the captured leads into nurture — the agent can then answer "which channel's traffic converts best on the quiz" in one session. Lead exports from Riddle pair directly with CorpusIQ's CRM connectors (HubSpot, Close) for pipeline routing.

## Limitations

- Requires a Riddle.com account and plan; OAuth to your Creator workspace
- 62 tools is a large surface — agents need clear instructions to pick the right family
- Interactive-content niche: strong for lead-gen and engagement, not a general marketing tool
- Hosted vendor platform; content lives in Riddle's system
- Live tool names beyond the template family served from the endpoint

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
