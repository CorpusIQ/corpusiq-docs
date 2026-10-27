---
title: CampaignStack MCP - Safe LinkedIn and Email Outreach
description: Run LinkedIn and email outreach from Claude with daily action budgets, per-account proxies, ICP scoring and a human approval queue before anything sends - 90+ tools over one endpoint.
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-09-02
source: mcp.so
relevance: ★★★
tags: [linkedin, cold-outreach, lead-generation, sales-automation, email, remote-mcp]
last_updated: "2026-10-24"
---

# CampaignStack MCP

**Remote MCP server (Streamable HTTP, API key)** - campaign orchestration for B2B lead generation agencies running outbound at volume across LinkedIn and email, built by the CampaignStack team. Ninety-plus tools let Claude and other agents drive the whole platform, from lead scoring to send approval.

```
Server type: Remote (Streamable HTTP)
Auth: API key (csu_ prefix)
Endpoint: https://mcp.campaignstack.io/mcp
Tools: 90+ (campaigns, lead scoring, LinkedIn and email sends, reply inbox, review queue)
Pricing: Per-account plans; docs at docs.campaignstack.io
Category: Sales & Outreach
Built by: CampaignStack Team
```

## Why This Matters for Operators

Outbound automation has a well-earned reputation for torching LinkedIn accounts. Most tools fire at full volume from day one and get the client banned. CampaignStack inverts the design around one constraint: **a client's LinkedIn account is not replaceable.**

Every connected account gets a hard daily action budget that ramps up over weeks, its own residential proxy, and a persistent browser fingerprint that stays stable between sessions. AI drafts the messages, a human approves them in a review queue before anything leaves the account, and auto-send stays off until you switch it on. Leads are scored against your ICPs, signals like job changes and post engagement decide who is worth contacting, and replies land in one shared inbox.

## Tools & Capabilities

| Area | What the tools do |
|---|---|
| Account safety | Daily action budgets with visible ramp, per-account proxy and fingerprint status |
| Campaign management | Build and run LinkedIn and email sequences across clients |
| Lead scoring | Score prospects against ICP definitions and engagement signals |
| Drafting and review | AI-drafted messages queued for human approval before send |
| Reply handling | One shared inbox for all campaign replies |

The MCP surface exposes 90+ tools driving this platform; docs at docs.campaignstack.io cover the current tool reference.

## Installation

```bash
claude mcp add campaignstack --transport http https://mcp.campaignstack.io/mcp --header "Authorization: Bearer csu_your_api_key_here"
```

## Configuration

```json
{
  "mcpServers": {
    "campaignstack": {
      "type": "http",
      "url": "https://mcp.campaignstack.io/mcp"
    }
  }
}
```

Authentication uses a workspace API key from the CampaignStack dashboard, attached as a bearer authorization header.

## Business Relevance

- **Lead gen agencies** run multi-client outbound with account-safety rails their clients can see
- **Founders** get cold outreach with a human approval gate instead of a fire-and-forget bot
- **Sales teams** score and prioritize leads from real engagement signals instead of list buys
- **Ops leaders** keep every send, budget and reply visible in one dashboard

## Integration with CorpusIQ

CampaignStack is the outbound engine next to CorpusIQ's inbound intelligence. An operator running both gets a complete revenue loop: CampaignStack's agent drafts and queues LinkedIn and email sequences, while CorpusIQ connectors read the business data that feeds targeting - Stripe revenue to spot high-value customer lookalikes, HubSpot pipeline to prioritize accounts, GA4 to see which campaign traffic converts. The agent can close the loop by scoring a reply against the company's actual transaction history before a human approves the next touch.

## Limitations

- Brand new listing with no track record yet
- Requires API key and paid plan for production use
- Conservative by design: ramping budgets and approval queues mean slower volume than aggressive tools
- LinkedIn-native and email-native; not a general social channel
