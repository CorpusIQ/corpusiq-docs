---
title: "Userbrain MCP — UX Research Analytics for AI Agents"
description: "Explore user testing data, summarize session feedback, and uncover UX insights from unmoderated usability tests — all through your MCP client."
category: mcp
tags: [mcp-server, ux-research, usability-testing, user-testing, product-research]
last_updated: 2026-07-08
---

# Userbrain MCP — UX Research Connector

## What It Is

Userbrain MCP (`userbrain.com`) connects AI agents to Userbrain's unmoderated remote usability testing platform. Product teams can query test session data, summarize participant feedback, identify pain points, and surface actionable UX insights — all from within their AI assistant. No more manually watching hours of test recordings.

## Tools Available

| Tool | Description |
|------|-------------|
| Test search | Find tests by project, participant segment, or date |
| Feedback summarization | AI-powered summary of participant comments by theme |
| Pain point detection | Surface recurring usability issues across sessions |
| Participant insights | Query by demographic, behavior, or task completion |

## Quick Start

```bash
# Hosted endpoint
https://mcp.userbrain.com/mcp
```

## Business Use Cases

1. **Pre-launch validation**: "Summarize the top 3 pain points from last week's checkout flow tests"
2. **Feature prioritization**: "Which features did participants request most across all Q3 tests?"
3. **Competitor benchmarking**: "Compare task completion rates between our app and Competitor X based on benchmark tests"
4. **CorpusIQ combo**: Pair UX insights with analytics data (GA4, PostHog via CorpusIQ) to connect what users say with what they actually do

## Limitations

- **Userbrain-specific**: Requires a Userbrain account with test data
- **Remote-hosted**: Depends on userbrain.com availability
- **Summarization quality**: AI-generated summaries should be spot-checked against raw recordings

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Analytics Connectors — GA4, PostHog](/hermes/mcp/connectors/)
