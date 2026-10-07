---
title: "AdTest.AI MCP - Pre-Spend Ad Creative Scoring"
description: "Stdio MCP that scores image, video or text ads on 13 dimensions (message clarity, emotional resonance, visual design, brand distinctiveness, platform fit, predicted CTR, compliance) before you spend media budget. One tool, analyze_advert, with an async submit-and-poll flow for video. npm package adtest-mcp, MIT, free account."
category: Marketing
stars: "n/a (new listing, menaker/adtest-mcp)"
added: 2026-09-01
source: "chatmcp/mcpso issue #3884 (Sep 1, 2026 night sweep)"
relevance: ★★
tags: [mcp-server, advertising, ad-creative, scoring, marketing-analytics, stdio]
---

# AdTest.AI MCP

**Pre-spend scoring for ad creatives.** AdTest.AI gives an agent one tool, `analyze_advert`, that runs a 13-dimension AI analysis of an image, video or text ad - message clarity, emotional resonance, visual design, brand distinctiveness, platform fit, predicted CTR, compliance and more - before media budget is committed. Stdio server, npm-published (adtest-mcp v1.1.0, verified Sep 1, 2026), MIT.

```
Server type: Stdio (local process)
Install: npx -y adtest-mcp
Auth: API key via ADTEST_API_KEY env var (free account at app.adtest.ai)
Tools: 1 (analyze_advert) with async video flow
Pricing: 1 credit per successful analysis; free account available
License: MIT
Built by: AdTest.AI (adtest.ai)
```

## Why This Matters for Operators

Creative is the highest-leverage spend decision in paid media, and it is usually made on intuition. AdTest.AI turns the pre-flight check into a repeatable machine call.

First, **scoring happens before the budget does.** The agent analyzes the creative, the operator reads the dimensions, and only then does media spend start - the tool's own flow is pre-spend by design.

Second, **one call covers three formats.** Pass a public URL of an image or video ad, a local file, or raw ad copy text; video runs through an async submit-and-poll flow so the agent is not holding a long request.

Third, **compliance in the scorecard.** The 13 dimensions include compliance checks, which matters for regulated verticals where a creative that converts but violates platform policy is a budget risk.

## Tools and Capabilities

| Tool | What it does |
|------|--------------|
| `analyze_advert` | Takes a public ad URL, a local file, or copy text and returns AdTest.AI's 13-dimension analysis: message clarity, emotional resonance, visual design, brand distinctiveness, platform fit, predicted CTR, compliance and more. Video uses an async submit-and-poll flow. |

The issue body's tool list matches the published npm package (verified v1.1.0, published Sep 1, 2026). Each successful analysis costs 1 credit on the free account.

## Installation

```bash
npm install -g adtest-mcp
```

Or via Claude Code:

```bash
claude mcp add adtest -e ADTEST_API_KEY=adk_your_key -- npx -y adtest-mcp
```

Get the free API key at app.adtest.ai under Developer.

## Configuration

```json
{
  "mcpServers": {
    "adtest": {
      "command": "npx",
      "args": ["-y", "adtest-mcp"],
      "env": {
        "ADTEST_API_KEY": "your_key"
      }
    }
  }
}
```

The server is stdio-only; there is no hosted endpoint. The key travels only to AdTest.AI's scoring API and stays out of prompts.

## Business Relevance

- **Performance marketers** score every creative before flight, keeping a pre-spend record for each test cell.
- **Agencies** standardize creative QA across clients with one dimension set, making pass/fail consistent.
- **DTC and e-commerce teams** test text, image and video variants cheaply before paying for placements.
- **Regulated verticals** catch compliance flags on creatives before platform review does it for them.

## Integration with CorpusIQ

AdTest.AI composes with CorpusIQ as the pre-spend gate inside marketing workflows. A CorpusIQ-connected agent that reads campaign performance from Google Ads or Shopify can pull underperforming creatives, run them through AdTest.AI, and hand back the dimension scorecard to decide what to pause, iterate or scale - with the scoring result stored next to the performance data. The operator keeps one governance point: CorpusIQ supplies the spend and revenue truth, AdTest.AI supplies the creative diagnosis, and the human stays the only one who commits budget.

## Limitations

- Brand new listing (repo and npm package both created Sep 1, 2026); scoring model has no public validation history yet.
- Single tool; the value is the 13-dimension model, not a broad workflow surface.
- Requires a free account and API key even for evaluation; credits meter every analysis.
- Video support is asynchronous - plan for the poll step in agent loops.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [YG3 MCP - Marketing Operations for Autonomous Agents](/hermes/mcp/servers/external/yg3-mcp)
- [Layers Growth MCP - TikTok Growth Loop for Agents](/hermes/mcp/servers/external/layers-marketing-mcp)
- [Social Glass MCP - Cultural Intelligence for Brand and Research Teams](/hermes/mcp/servers/external/social-glass-mcp)
