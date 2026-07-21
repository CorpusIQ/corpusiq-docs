---
title: "PreTestAds — Ad Creative Scoring MCP for AI Agents"
description: "Score video and image ads before you spend. AI-powered creative testing benchmarked against 76 top TikTok ads. $5 USDC per run via x402 or account credits via OAuth."
source: github.com/krecicki/pretestads-agent-scripts
stars: 0
language: Unknown
transport: Streamable HTTP (Remote) + stdio
auth: x402 (USDC payment) or OAuth
category: Marketing & Advertising
last_updated: 2026-07-21
---

# PreTestAds — Ad Creative Scoring MCP for AI Agents

**Pre-flight ad creative testing through MCP.** Before spending budget on ads, run your creative through PreTestAds' AI scoring engine. Benchmarked against 76 of the best-performing TikTok ads. Pay $5 USDC per run via x402 protocol, or use account credits through OAuth.

## What It Does for Operators

- **Creative scoring** — AI evaluates video/image ads for predicted performance before you spend
- **TikTok benchmarked** — Scoring model trained on 76 top-performing TikTok ads
- **x402 payment** — Pay $5 USDC per analysis using the x402 payment protocol (no subscription needed)
- **OAuth option** — Account credits for frequent users
- **Agent-native** — Score ads directly from your AI agent during creative development

## Installation

```bash
git clone https://github.com/krecicki/pretestads-agent-scripts.git
cd pretestads-agent-scripts
# Follow repo instructions for setup
# Or use the remote OAuth endpoint
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "pretestads": {
      "command": "node",
      "args": ["path/to/pretestads/server.js"]
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `score_video_ad` | Score a video creative against benchmark data |
| `score_image_ad` | Score a static image creative |
| `get_benchmark` | Retrieve benchmark performance data |
| `compare_ads` | Side-by-side comparison of multiple creatives |
| `get_recommendations` | AI-generated improvement suggestions |

*Note: Tool names are approximate. See github.com/krecicki/pretestads-agent-scripts.*

## Operator Use Cases

1. **DTC Brands** — Score 10 video variations before spending $5K on the winner
2. **Agencies** — Pre-test client creative in minutes instead of running $500 test campaigns
3. **Performance Marketers** — Iterate creative with AI feedback before launch
4. **Content Creators** — Validate hooks and CTAs against TikTok benchmarks

## CorpusIQ Angle

PreTestAds + CorpusIQ = closed-loop ad optimization for operators. Use PreTestAds to score creative before launch → run ads on Meta/TikTok → track ROAS through CorpusIQ's ad platform connectors → feed performance data back into creative scoring. The creative-to-revenue feedback loop, all through AI agents.

## Limitations

- Scoring benchmarked against TikTok ads only — may not translate to Meta, YouTube, etc.
- $5/run pricing adds up for high-volume testing
- Scoring is predictive, not guaranteed — real performance may vary
- x402 payment protocol adds friction for first-time users
