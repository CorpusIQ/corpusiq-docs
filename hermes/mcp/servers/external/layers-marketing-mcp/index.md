---
title: "Layers Growth MCP - TikTok Growth Loop for Agents"
description: "Hosted MCP that runs a TikTok growth loop from a repository: a standing map of competitor accounts, an evidence-ranked queue of content tests, an editable plan for the next test, delivery to a TikTok draft inbox and recorded results. Every charge is quoted before it happens; posting, spending and billing changes wait for a human click."
category: Marketing
stars: "n/a (new listing, layers/mcp)"
added: 2026-09-01
source: "mcp.so homepage recentServers (Sep 1, 2026 night sweep)"
relevance: ★★
tags: [mcp-server, tiktok, growth, content-marketing, social-media, human-in-the-loop, oauth, remote-mcp]
---

# Layers Growth MCP

**One MCP server that runs a TikTok growth loop.** Layers Growth MCP gives a coding agent a standing growth plan: a map of the accounts a product competes with, an evidence-ranked queue of content tests, an editable plan for the next test, delivery to a TikTok draft inbox, and a recorded result with the next test to run. Endpoint live and OAuth-gated (401 verified Sep 1, 2026); the agent calls one named outcome per job and every charge is quoted before it happens.

```
Server type: Hosted, remote (Streamable HTTP)
Endpoint: https://mcp.layers.com/mcp (health: /health)
Auth: Bearer session from one-time browser OAuth sign-in (401 AUTH_REQUIRED verified anonymous)
Setup: npm install -g @layers/cli, then `layers setup` in the repo (writes .mcp.json + skill)
Repo: github.com/layers/mcp (MIT, created Sep 1, 2026)
Built by: Layers (layers.com)
```

## Why This Matters for Operators

TikTok growth is a loop: pick a test, ship content, read the result, pick the next test. Most tools automate one step. Layers holds the whole loop as machine-readable state an agent can drive.

First, **the competitor map is standing state, not a one-off report.** The server keeps a map of the accounts the product competes with, so every planning call starts from the same ground truth instead of a fresh scrape.

Second, **evidence-ranked testing.** The queue of content tests is ranked by evidence, and the plan for the next test is editable - the agent proposes, the human adjusts, and the loop advances one named outcome per job.

Third, **human gates on everything that costs or publishes.** Every charge is quoted before it happens, and posting, spending and billing changes each wait for a human click. The agent can plan, render and draft freely; the operator stays the only one who ships.

## Tools and Capabilities

Capability-level table sourced from the vendor's MCP docs; the live tool list is served from the endpoint after OAuth sign-in (anonymous enumeration is refused with 401).

| Surface | What it covers |
|---------|----------------|
| Competitor map | Standing map of the accounts the product competes with, kept in the Layers project |
| Content tests | Evidence-ranked queue of content tests and an editable plan for the next test |
| Rendering | Render the video or slideshow for the planned test through the Layers platform |
| Delivery | Deliver drafts to a TikTok draft inbox; posting waits for human approval |
| Results | Recorded result per test, feeding the next test selection |
| Billing | Every charge quoted before execution; billing changes human-approved |

## Installation

```bash
npm install -g @layers/cli
layers setup
```

Run setup from the repository the agent works in. It opens the browser once for sign-in, writes the `.mcp.json` entry and the Layers skill into the repo, and stores the session in the OS credential store - nothing secret lands in the repository. The CLI is the credential's only reader alongside the MCP client.

## Configuration

```json
{
  "mcpServers": {
    "layers": {
      "type": "http",
      "url": "https://mcp.layers.com/mcp"
    }
  }
}
```

Setup binds the server to one Layers organization and project through the repository. The one-time browser sign-in is the only human step; after that the agent plans, renders and drafts autonomously while posting and spending stay behind the human click.

## Business Relevance

- **Consumer brands and DTC teams** keep a continuous TikTok test loop running with the agent as the operator and the human as the approver.
- **Founders without a content team** get a standing growth plan instead of ad-hoc posting.
- **Agencies** run one Layers project per client, each bound to its own repo and approver.
- **Growth operators** get charge quotes before execution, making agent-driven spend auditable.

## Integration with CorpusIQ

Layers composes with CorpusIQ as the channel layer on top of the business data CorpusIQ reads. A CorpusIQ workflow that sees Shopify revenue or GA4 traffic by landing page can feed the next test into the Layers queue, let the agent render the draft, and record the result back against the same business metrics that justified the test. The operator keeps one governance point: CorpusIQ supplies the performance truth, Layers runs the content loop, and the human click gates every posting and spending change - so the agent never ships unaudited.

## Limitations

- Brand new listing (repo created Sep 1, 2026); no public adoption data yet.
- OAuth session required; no anonymous or keyless mode - the 401 on anonymous initialize is expected.
- TikTok-centric growth loop; other platforms are not the current focus.
- Capability-level tool table above; exact tool names appear after sign-in.
- Vendor-hosted platform; the loop's quality depends on Layers' rendering and delivery services.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [YG3 MCP - Marketing Operations for Autonomous Agents](/hermes/mcp/servers/external/yg3-mcp)
- [AdTest.AI MCP - Pre-Spend Ad Creative Scoring](/hermes/mcp/servers/external/adtest-mcp)
- [Social Glass MCP - Cultural Intelligence for Brand and Research Teams](/hermes/mcp/servers/external/social-glass-mcp)
