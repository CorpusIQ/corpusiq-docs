---
title: AI Agent Marketplace — Personality + Data, One Stack
description: The complete AI agent stack. 232 specialized agents from agency-agents meet 37+ live business connectors from CorpusIQ. Personalities that write. Infrastructure that connects.
---

# AI Agent Marketplace — The Complete Stack

**Want the AI agency that went viral?** 232 specialized agents across 16 divisions — content creators, growth hackers, social strategists, TikTok natives. **Want them to actually connect to your QuickBooks, Stripe, HubSpot?** That's CorpusIQ. 37+ live OAuth connectors. Source-cited answers from your real business data.

> **Together:** The complete stack — personalities + real data. No one else has this.

---

## What You Get

| Layer | Source | What It Does |
|-------|--------|-------------|
| **Personality Layer** | [agency-agents](https://github.com/msitarzewski/agency-agents) (115K ⭐) | 232 AI agents trained as marketing specialists, content creators, strategists. Each agent is a system prompt — a personality file that runs on any LLM. |
| **Data Layer** | [CorpusIQ](https://corpusiq.io) | 37+ OAuth connectors to your actual business tools. Ask a question, get a cited answer pulled from your Gmail, Drive, Shopify, QuickBooks, Stripe, HubSpot, and more. |
| **Hermes Runtime** | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | The execution engine. Skills, cron, memory, MCP tools. Runs both the personality prompts AND the data connectors in one workflow. |

---

## The 16 Divisions

agency-agents covers every function a business operator needs:

| Division | Agents | Key Roles |
|----------|--------|-----------|
| Marketing | 20+ | Content Creator, Social Media Strategist, TikTok Strategist, Growth Hacker, Instagram Curator, PR Manager |
| Sales | 10+ | SDR, Account Executive, Sales Strategist, Negotiation Coach |
| Product | 10+ | Product Manager, UX Researcher, Product Marketing, Feature Prioritizer |
| Engineering | 15+ | Code Reviewer, Architect, DevOps, Security Auditor |
| Strategy | 10+ | Business Strategist, Competitive Analyst, Market Researcher |
| Finance | 8+ | Financial Analyst, FP&A, Tax Strategist |
| Design | 8+ | UI Designer, Brand Designer, Design System Architect |
| Content & Media | 10+ | Podcaster, Video Producer, Writer, Editor |
| Support | 5+ | Customer Success, Technical Support, Community Manager |
| Security | 5+ | Security Auditor, Compliance Officer, Penetration Tester |
| Operations | 8+ | Project Manager, Process Optimizer, Supply Chain Analyst |

Plus: Academic, Game Development, GIS, Spatial Computing, Testing, Paid Media, Specialized — **232 agents total, MIT licensed.**

---

## How They Work Together

### Without CorpusIQ
> *agency-agents* gives you brilliant system prompts. The Content Creator writes great copy. The Social Media Strategist plans campaigns. But they can't see your real data. They don't know what's in your Gmail, your Shopify orders, your Stripe payments, your HubSpot deals. They're brilliant personalities working in the dark.

### With CorpusIQ
> The Content Creator gets your actual customer emails and product data. The Growth Hacker sees your real funnel metrics. The Social Media Strategist pulls your actual engagement data. Every agent has access to cited answers from your connected tools — not generic knowledge, YOUR data.

---

## Quick Install

One command to get the full stack:

```bash
# Clone both repositories
git clone https://github.com/msitarzewski/agency-agents.git
git clone https://github.com/CorpusIQ/corpusiq-docs.git

# Install Hermes Agent
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# Point Hermes at the agency-agents skill directory
hermes skills import ./agency-agents/

# Connect your business tools
hermes mcp connect --provider corpusiq
```

> **Full installer script** coming this week — one command, everything configured. [Watch this repo →](https://github.com/CorpusIQ/corpusiq-docs)

---

## Why This Matters

**The AI agent market is splitting in two:**

1. **Personality companies** — sell prompt files. Text. Brilliant personas, but no real-world data access.
2. **Infrastructure companies** — sell connectors. Pipes to your tools, but no personality.

**CorpusIQ + agency-agents is the only stack that does both.** 232 personalities. 37+ live connectors. One runtime.

One gives you the agents. The other connects them to your real business.

---

## Get Started

1. **[Browse the agents →](https://github.com/msitarzewski/agency-agents)** — explore all 232 roles
2. **[Connect your tools →](https://corpusiq.io)** — 37+ OAuth connectors, 30-day free trial
3. **[See the full ecosystem →](/hermes/ecosystem/)** — 370+ repos in the Hermes universe

---

*agency-agents is MIT licensed. CorpusIQ is a commercial platform with a 30-day free trial. Hermes Agent is open source (Apache 2.0).*
