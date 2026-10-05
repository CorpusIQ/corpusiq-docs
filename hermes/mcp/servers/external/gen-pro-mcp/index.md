---
title: GEN MCP - Social Video Creation and Publishing
description: "Hosted MCP for a social video engine: spot trends, write scripts, generate multi-scene videos and schedule posts, with a free editor."
category: Marketing
stars: n/a (new listing)
added: 2026-10-04
source: mcpservers.org
relevance: ★★
tags: [marketing, social-media, video, content-creation, publishing, scheduling, remote-mcp, oauth]
---

# GEN MCP

**Hosted remote MCP server (Streamable HTTP, OAuth or PAT)** - GEN turns an assistant into a social video production line: research trends in a niche, write scripts, draft multi-scene videos in the Vidsheet editor across models from Kling to Seedance and Nano Banana to GPT Image, then schedule the result to connected social accounts. Agents can even register themselves: a POST to `api.gen.pro/v1/agents/register` with a handle that begins with `agent:` creates the user, workspace, agent and API key in one response.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (Claude, ChatGPT, Codex, Grok) or a Personal Access Token
Endpoint: https://mcp.gen.pro
Tools: gen_discover (capability explorer), gen_vidsheet_action, plus the pipeline it surfaces
Pricing: Editor and scheduling free; AI generation draws credits (card or x402 crypto)
Category: Marketing
Built by: GEN (gen.pro)
```

## Why This Matters for Operators

Social video is where most small brands lose the most time: trend research in one tab, scripting in another, generation in a third, scheduling in a fourth. GEN compresses that into one workspace an agent can drive. The **Vidsheet** is the unit of work - rows are videos, columns hold inputs and ingredients - so a working setup becomes a template: duplicate the last row, change the script or the look, generate again. That turns one-off video production into a repeatable pipeline.

For solo operators and agencies the entry cost is deliberately low: the video editor and post scheduling are free, and only AI media generation consumes credits (payable by card or x402 crypto). Automations close the loop - one of GEN's own examples is generating a video every day from new listings research.

**The key advantage is a repeatable, template-driven video pipeline that an agent can run end to end, from trend to scheduled post.**

## Tools & Capabilities

| Capability | What it does |
|---|---|
| `gen_discover` | Explores GEN's domains and what the connected account can do, including a billing view to check generation access before spending |
| `gen_vidsheet_action` | Creates, renames and reads Vidsheets and drives their actions |
| Vidsheet editor | Multi-scene video setups: rows as videos, cells as inputs, across models from Kling to Seedance and Nano Banana to GPT Image |
| AI text fields | Generate ideas and prompts from web research or your own briefs |
| Variables | Reuse values across prompts; global variables hold character sheets and style guides |
| Creation cards | Turn inputs into text, images, video, audio and captions |
| Research | Spot trends and get content ideas from web research and connected socials |
| Publishing | Connect social accounts and auto-schedule posts from the pipeline; a publishing calendar tracks them |
| Automations | Schedule recurring production, for example a new video from fresh research every day |

## Installation

```bash
claude mcp add --transport http gen https://mcp.gen.pro
```

Then run `/mcp` inside Claude Code and sign in. ChatGPT adds it under Settings, Plugins, MCPs as a Streamable HTTP server at `https://mcp.gen.pro`, and Grok Bot accepts the one-line prompt GEN publishes. Claude Desktop and claude.ai add it as a custom connector, and for file attachments (photos and voice samples) the docs list the capability and allowlist settings to enable.

## Configuration

OAuth is the default path in every client that supports it. For clients without OAuth, mint a Personal Access Token on the GEN API page and send it as `Authorization: Bearer`. A REST surface mirrors the MCP server at `api.gen.pro` with its schema published at `api.gen.pro/openapi.yaml`, and the agent setup guide lives at `gen.pro/skill.md` - including self-registration for agents with no account (`POST api.gen.pro/v1/agents/register`, returning a PAT that must be stored immediately). Creating and renaming Vidsheets and reading your own identity or balance work on an unfunded account; check `gen_discover` with the billing view before generating media.

## Business Relevance

- **E-commerce brands** - turn product research into short video ads through a template pipeline instead of a manual edit suite.
- **Faceless channels and clipping** - run recurring production on a schedule with automations.
- **Agencies** - per-client workspaces and agents, with free editing and scheduling to keep client overhead off the bill.
- **Solo operators** - start on the free editor and scheduling, and pay only when generation credits are actually needed.
- **Content ops teams** - keep a Vidsheet as the reusable production template so each new video is a row, not a project.

## Integration with CorpusIQ

CorpusIQ reads which channels actually convert - marketing performance from GA4, Meta, Google Ads and the checkout side from Shopify or Stripe, all read-only. GEN produces the next round of content for the channels those numbers favour. Measure in CorpusIQ, produce and publish in GEN, and let the assistant carry the findings between the two.

A composed workflow: an operator reviews last month's ad performance through CorpusIQ, asks GEN to draft three video angles for the winning product, generates them in the Vidsheet, and schedules the best one. The numbers stay grounded in the business; the content engine runs on top of them.

## Limitations

- AI media generation requires paid access and credits; only drafting, editor access and scheduling are free. Credits are bought by card or x402 crypto.
- Publishing requires connecting the target social accounts inside GEN first.
- The service is hosted by GEN; there is no self-hosted path.
- Model availability (Kling, Seedance, Nano Banana, GPT Image and others) depends on GEN's catalog and your access tier.
- Auth for automated agents means managing a PAT, or using self-registration and storing the returned key securely.

## FAQ

### What is GEN?

A social video content engine with a hosted MCP server: trend research, scripting, multi-scene AI video generation in the Vidsheet editor, and scheduling to connected social accounts.

### Is GEN free?

The video editor and post scheduling are free, and the MCP and API themselves are free. AI media generation draws credits purchasable by card or x402.

### How does an agent connect without OAuth?

Two ways: a Personal Access Token sent as a Bearer header, or agent self-registration - `POST api.gen.pro/v1/agents/register` with a unique `agent:` handle returns an API key to store as the agent's PAT.

### Can GEN publish without me?

It schedules posts to accounts you connect, and automations can run on a schedule you define. Drafting, editing and generation are driven from your prompts or pipelines inside your own workspace.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Genviral MCP - Social Media Creation and Publishing](/hermes/mcp/servers/external/genviral-mcp/)
- [InstantClips MCP - E-Commerce Short-Form Video Ads](/hermes/mcp/servers/external/instantclips-mcp/)
