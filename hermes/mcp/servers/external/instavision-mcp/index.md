---
title: InstaVision MCP - Instagram Creator and Lead Discovery
description: Remote MCP that finds Instagram creators and leads by niche, city, follower range or lookalike accounts, with spend caps and email enrichment.
category: Marketing
stars: n/a (new listing)
added: 2026-10-04
source: mcp.so feed
relevance: ★★★
tags: [marketing, instagram, influencer-marketing, creator-discovery, lead-generation, remote-mcp, api-key]
---

# InstaVision MCP

**Remote MCP server (Streamable HTTP, API key) or local npx bridge** - the official server from InstaVision that puts Instagram creator and lead discovery inside an agent. Nine tools run a full loop: list the discovery playbooks, estimate credits before spending anything, launch a run against 11 search playbooks, poll its status, read results row by row, export a theme-sectioned PDF, and manage the cross-run dedup pool so later runs skip accounts already delivered. Playbook listing and cost estimates work without a key; everything that touches an account needs one.

```
Server type: Remote (Streamable HTTP) or local npx bridge
Auth: InstaVision API key (Bearer header or INSTAVISION_API_KEY)
Endpoint: https://instavision.co/api/mcp/mcp
Tools: 9 (playbooks, cost estimate, launch, status, results, dedup pool, PDF export)
Pricing: 500 free credits on new accounts; 1 credit = 1 profile scanned
Category: Marketing
Built by: InstaVision (afanasenkoa/instavision-mcp bridge on GitHub, MIT)
```

## Why This Matters for Operators

Finding the right Instagram accounts is normally a tab-by-tab manual exercise: hashtag scrolling, screenshotting profiles, hunting for a public email, then copy-pasting rows into a sheet that goes stale by the next campaign. InstaVision turns that into a structured run: pick a playbook, set a hard credit cap, launch, and read a table where every row carries the handle, follower count, public email, an AI category, and a qualification gate (pass, relevance or evidence).

The spend model is the operator-friendly part. One credit equals one profile scanned, the cap is agreed before a run starts (at most 500 credits), and the run reports processed and returned counts with credits charged. A discovery run becomes a budgeted, repeatable operation instead of an open-ended scrape.

**The key advantage is a cost-capped, deduplicated discovery loop that keeps working across campaigns.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| List playbooks | The discovery playbooks, their input fields and credit ranges; works without a key |
| Estimate cost | Min and max credit cost for a run without launching or spending anything |
| Launch discovery (`launch_discovery`) | Starts a run with a required `creditsCap` (at most 500); this spends real credits |
| Run status | queued, running, succeeded, failed or aborted, with processed and returned counts |
| Run results | Paginated rows: handle, name, followers, email, AI category, qualification gate, duplicate and language flags |
| Dedup pool | Cross-run list of accounts already delivered, newest first |
| Import handles | Adds Instagram handles or profile URLs to the dedup pool as imported |
| Clear pool (destructive) | Clears the pool; the default clears only your blocklist |
| Export PDF | Theme-sectioned PDF report with a signed download URL that expires after 1 hour |

Playbooks cover keyword and hashtag search, local creators by city, lookalikes of example accounts, people who liked or commented on a post, and enrichment of a list you already have. Filters include follower range, public email and AI category.

## Installation

Remote endpoint for Claude Code, Cursor, Codex and VS Code:

```json
{
  "mcpServers": {
    "instavision": {
      "type": "http",
      "url": "https://instavision.co/api/mcp/mcp",
      "headers": { "Authorization": "Bearer YOUR_INSTAVISION_API_KEY" }
    }
  }
}
```

Claude Desktop uses the npx bridge (needs Node.js). On Windows, if npx fails to launch, wrap it as `cmd /c npx -y instavision-mcp`:

```json
{
  "mcpServers": {
    "instavision": {
      "command": "npx",
      "args": ["-y", "instavision-mcp"],
      "env": { "INSTAVISION_API_KEY": "YOUR_INSTAVISION_API_KEY" }
    }
  }
}
```

## Configuration

Create an API key at instavision.co/settings/api-keys. Pass it only in the header or the environment variable, never as a URL parameter, and revoke it from the same page when rotating. Without a key the bridge still starts: the agent can list playbooks and estimate credits, and account calls fail with a pointer to the keys page. New accounts get 500 free credits; through MCP a single run caps at 500 credits, at most 5 runs run at once, and the daily ceiling is 2,000 credits. Accounts already delivered to you are skipped in later runs unless a launch explicitly sets `excludeSeen` to false.

## Business Relevance

- **Influencer marketing** - shortlist creators in a niche and follower range for a campaign without manual hashtag work.
- **Local marketing** - find micro-creators in a specific city for geo-targeted pushes.
- **Lookalike prospecting** - expand from a few known accounts to similar ones.
- **Lead generation** - collect accounts with a public email for outreach.
- **Engagement mining** - find the people who liked or commented on a competitor's post.
- **Agencies** - run the same discovery loop per client with per-run caps that keep spend predictable.

## Integration with CorpusIQ

CorpusIQ's connectors are read-only windows into the systems an operator already runs, including Meta surfaces: what was actually posted, how it performed, what the shop sold. InstaVision works the other side of the same problem: it finds the creators and leads worth approaching before any of them are connected.

A composed workflow: pull last month's channel performance from CorpusIQ, ask InstaVision for creators whose niche and audience match the channels that are working, then have the assistant assemble the outreach list with both sets of facts attached. CorpusIQ reads the business; InstaVision reads the creator market around it.

## Limitations

- claude.ai and ChatGPT connectors are not supported yet - the hosted service has not shipped OAuth, so web connectors cannot sign in; use Claude Code, Cursor, Codex, VS Code or the Claude Desktop bridge.
- Searches spend credits (1 credit = 1 profile scanned); the estimate tool is free, the launch is not.
- Results are built from public profile data; rows carry duplicate and language flags for review rather than guarantees.
- The PDF download URL expires after 1 hour.
- The search service is hosted by InstaVision; only the npx bridge is open source.

## FAQ

### What is InstaVision?

An Instagram creator and lead discovery service with an MCP server: it finds accounts by niche, city, follower range, lookalikes or engagement, and returns structured rows with public emails where available.

### Does it need an API key?

For account work, yes. Listing playbooks and estimating credits work without one.

### How is spending controlled?

You set a `creditsCap` (at most 500) before each run; 1 credit equals 1 profile scanned. At most 5 runs run at once and 2,000 credits a day flow through MCP.

### Which clients does it support?

Claude Code, Cursor, Codex and VS Code connect to the remote endpoint with a key header; Claude Desktop uses the npx bridge. Web connectors await OAuth support.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [AffiliateSpy MCP - Competitor Creator Discovery](/hermes/mcp/servers/external/affiliatespy-mcp/)
- [UGC VZ MCP - Creator Discovery for Agents](/hermes/mcp/servers/external/ugc-vz-mcp/)
