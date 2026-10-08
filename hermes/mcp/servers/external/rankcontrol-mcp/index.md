---
title: "RankControl MCP - SEO Content Program for Agents"
description: "Give your agent the whole SEO content program: AI-visibility tracking, article planning and publishing, link building and reports."
category: SEO
stars: n/a (new listing)
added: 2026-10-07
source: "chatmcp/mcpso issue #4925 (Oct 7, 2026 evening sweep)"
relevance: ★★★
tags: [seo, content-marketing, ai-search, link-building, publishing, analytics]
---

# RankControl MCP

**Hosted MCP server that puts an entire SEO content program inside your agent** - visibility data, the content pipeline, repurposing, link building, brand memory and reports as 80+ tools. Your agent researches what buyers search, drafts and publishes the articles, then reads back the Google and AI-search traffic they bring in.

```
Server type: Remote (Streamable HTTP at https://api.rctrl.com/mcp) plus a local npm server (npx rankcontrol mcp)
Auth: OAuth browser sign-in on the remote connector, or a scoped API key (rctrl_pk_...) for the local server
Docs: https://rctrl.com/docs/mcp
Package: npm rankcontrol; registry io.github.rankcontrol/rankcontrol; repo github.com/rankcontrol/rankcontrol
Tools: 80+ across visibility, content, reports, analytics, repurposing, link building, social and brand memory
Pricing: Runs against your RankControl workspace; the remote connector requires workspace-owner sign-in
Category: SEO
Built by: RankControl
```

## Why This Matters for Operators

Most SEO stacks stop at reporting: a dashboard tells you what happened, then a human does everything else. RankControl closes the loop over MCP. The same server your agent calls to see which queries cite competitors but not you is the server that plans the article, drafts it in your brand voice, publishes it to Shopify, Webflow or Framer, and then reports the traffic and citations it earned. For an operator running content as an acquisition channel, the agent stops being a copy machine and becomes the program manager.

## Tools & Capabilities

| Area | Tools |
|---|---|
| Visibility | score, trend, share of voice, cited sources, sentiment, citation checks, tracked queries, crawler access |
| Content | list, scored ideas, hide ideas, plan ideas and titles, commit, generate, publish, reschedule, archive, citability report, internal links |
| Reports | exec summary, top wins, agent activity, page engagement, traffic, funnel |
| Analytics | traffic, rankings with Google AI Overview shown and cited per keyword, page engagement, data sources, Cloudflare connect |
| Repurposing | queue, generate drafts, edit, Buffer and Postiz channels, push, mark posted |
| Link building | backlinks and stats, outreach pipeline, contact finding, reply drafting, queueing, Editorial Circle |
| Social | thread prospects, stats, status, reply drafting |
| Brand memory | read everything, update voice and style, manage products and buyer profiles, suggest audiences |

## Installation

Remote connector, one command:

```bash
claude mcp add --transport http rankcontrol https://api.rctrl.com/mcp
```

Sign in in the browser, review the consent list and approve. Claude, Cursor and any Streamable HTTP client work the same way.

Local server for CI, headless setups or key-scoped control:

```bash
npx rankcontrol mcp
```

## Configuration

```json
{
  "mcpServers": {
    "rankcontrol": {
      "command": "npx",
      "args": ["rankcontrol", "mcp"],
      "env": { "RANKCONTROL_API_KEY": "rctrl_pk_your_key" }
    }
  }
}
```

Agents that run shell commands can learn the CLI directly: `npx skills add rankcontrol/rankcontrol` installs a skill with the full command reference and the review-gate rules.

## Safety Model

The server enforces the same guardrails for agents as for humans. Publicly visible actions (publish, social push, outreach send, team invites) return a dry-run preview until called again with `confirm: true`, and the tool descriptions tell the agent a human should approve first. The remote connector acts only under what the owner approved on the consent screen; a local key without `write:publish` cannot publish no matter what the agent asks. Costly tools sit at 5 to 10 calls per minute, and every key is revocable in Settings.

## Business Relevance

- **SEO and content teams:** run the whole plan-measure loop from chat - find queries where competitors are cited instead of you, plan and publish the fix, then verify the citations landed.
- **Founders running their own content:** skip the dashboard shuffle; the agent works the pipeline in your brand voice and reports outcomes.
- **Agencies:** manage link outreach, repurposing and client reporting through the same workspace the team already uses.

## Integration with CorpusIQ

CorpusIQ reads your business systems (GA4, Search Console, Stripe, Shopify) and keeps your numbers consistent across AI clients. RankControl adds the content execution lane on top: read what your site earned through CorpusIQ, then have your agent plan, publish and iterate the articles behind it in the same conversation.

## Limitations

- The remote connector signs in as the workspace owner and needs onboarding finished first; publishing destinations (Shopify, Webflow, Framer) connect in the dashboard before the agent can publish.
- The consent screen lists everything the connector can do; review it before approving, and disconnect by removing the connector.
- Brand new listing - no published third-party track record yet; pricing lives on rctrl.com.

## FAQ

### Does the agent publish without approval?

No. Publishes, outreach sends and social pushes return a preview first and require a second call with `confirm: true`, and the tool descriptions instruct the agent to get a human decision.

### What makes this different from an SEO reporting server?

It carries the execution side: content planning, generation, publishing and repurposing, not just metrics. The visibility and analytics tools sit alongside the pipeline that acts on them.

### Can it report on AI search specifically?

Yes - rankings show Google AI Overview presence and citations per tracked keyword, alongside cited sources and share of voice across answer surfaces.

### Is there a headless option?

Yes, the same package runs as a local MCP server under an API key with per-key scopes, for CI or headless workflows.

## See Also

- [Encited MCP - SEO and AI Visibility for Agents](/hermes/mcp/servers/external/encited-mcp/)
- [Tracetify MCP - SEO, GEO and Growth Reports for Agents](/hermes/mcp/servers/external/tracetify-mcp/)
- [IndexLinks MCP - Page Submission and Crawl Receipts](/hermes/mcp/servers/external/indexlinks-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
