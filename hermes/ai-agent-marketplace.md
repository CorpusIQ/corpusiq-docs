---
title: AI Agent Marketplace - Personality + Data, One Stack
description: The complete AI agent stack. 283 specialized agents from agency-agents meet 40+ live business connectors from CorpusIQ. Personalities that write. Infrastructure that connects.
canonical: "https://www.corpusiq.io/docs/hermes/ai-agent-marketplace/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes agent", "ai agent", "nous research"]

---

# AI Agent Marketplace - The Complete Stack

**Want the AI agency that went viral?** 283 specialized agents across 18 divisions - content creators, growth hackers, social strategists, TikTok natives. **Want them to actually connect to your QuickBooks, Stripe, HubSpot?** That's CorpusIQ. 40+ live OAuth connectors. Source-cited answers from your real business data.

> **Together:** The complete stack - personalities + real data. No one else has this.

---

## What You Get

| Layer | Source | What It Does |
|-------|--------|-------------|
| **Personality Layer** | [agency-agents](https://github.com/msitarzewski/agency-agents) (165K ⭐) | 283 AI agents trained as marketing specialists, content creators, strategists. Each agent is a system prompt - a personality file that runs on any LLM. |
| **Data Layer** | [CorpusIQ](https://corpusiq.io) | 40+ OAuth connectors to your actual business tools. Ask a question, get a cited answer pulled from your Gmail, Drive, Shopify, QuickBooks, Stripe, HubSpot, and more. |
| **Hermes Runtime** | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | The execution engine. Skills, cron, memory, MCP tools. Runs both the personality prompts AND the data connectors in one workflow. |

---

## The 18 Divisions

agency-agents covers every function a business operator needs (counts read from the repo roster on Oct 28, 2026):

| Division | Agents | Key Roles |
|----------|--------|-----------|
| Engineering | 66 | Code Reviewer, Architect, DevOps Automator, Mobile, Embedded, Platform |
| Specialized | 58 | Sales Outreach, Research, Automation, Remediation, domain specialists |
| Marketing | 37 | Content Creator, Social Media Strategist, TikTok Strategist, Instagram Curator, PR Manager |
| Game Development | 21 | Unity, Unreal, Godot, Roblox Studio specialists |
| GIS | 13 | Geospatial analysis, mapping pipelines, remote sensing |
| Security | 12 | Security Auditor, Compliance Officer, Penetration Tester |
| Design | 10 | UI Designer, Brand Guardian, UX Researcher, design systems |
| Sales | 10 | Outbound Strategist, Account Strategist, Deal Strategist, Sales Coach |
| Testing | 9 | Test automation, evidence collection, performance testing |
| Paid Media | 7 | PPC Strategist, Search Query Analyst, Paid Media Auditor |
| Project Management | 7 | Project Shepherd, process and vendor management |
| Product | 6 | Product Manager, UX Researcher, competitive analysis |
| Support | 6 | Support Responder, Community Manager, onboarding |
| Spatial Computing | 6 | AR/VR, 3D design, spatial UX |
| Academic | 6 | Literature review, research synthesis |
| Finance | 5 | Financial Analyst, FP&A, crypto and Web3 |
| Healthcare | 3 | Clinical and health-domain specialists |
| Research | 1 | Deep research and market analysis |

**283 agents total, MIT licensed.** The roster also ships as a native app for macOS, Linux, and Windows at [agencyagents.app](https://agencyagents.app).

---

## How They Work Together

### Without CorpusIQ
> *agency-agents* gives you brilliant system prompts. The Content Creator writes great copy. The Social Media Strategist plans campaigns. But they can't see your real data. They don't know what's in your Gmail, your Shopify orders, your Stripe payments, your HubSpot deals. They're brilliant personalities working in the dark.

### With CorpusIQ
> The Content Creator gets your actual customer emails and product data. The Growth Hacker sees your real funnel metrics. The Social Media Strategist pulls your actual engagement data. Every agent has access to cited answers from your connected tools - not generic knowledge, YOUR data.

---

## Quick Install

One command to get the full stack:

```bash
# 1. Get the roster
git clone https://github.com/msitarzewski/agency-agents.git

# 2. Install Hermes Agent (one-line installer from the official docs)
curl -fsSL https://hermes-agent.nousresearch.com/install.sh > /tmp/hermes-install.sh && bash /tmp/hermes-install.sh

# 3. Connect CorpusIQ over MCP (OAuth)
hermes mcp add corpusiq --url https://mcp2.corpusiq.io/mcp --auth oauth
hermes mcp test corpusiq
```

Agent files in the roster are prompt and personality definitions. Point your agent at the ones you want, or use the roster's own installer scripts, and they run on whichever model you configure in Hermes.


---

## Why This Matters

**The AI agent market is splitting in two:**

1. **Personality companies** - sell prompt files. Text. Brilliant personas, but no real-world data access.
2. **Infrastructure companies** - sell connectors. Pipes to your tools, but no personality.

**CorpusIQ + agency-agents is the only stack that does both.** 283 personalities. 40+ live connectors. One runtime.

One gives you the agents. The other connects them to your real business.

---

## Get Started

1. **[Browse the agents →](https://github.com/msitarzewski/agency-agents)** - explore all 283 roles
2. **[Connect your tools →](https://corpusiq.io)** - 40+ OAuth connectors, 30-day free trial
3. **[See the full ecosystem →](/hermes/ecosystem)** - 447+ repos in the Hermes universe

---

*agency-agents is MIT licensed. CorpusIQ is a commercial platform with a 30-day free trial. Hermes Agent is open source (MIT).*
