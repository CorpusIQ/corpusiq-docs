---
title: Hermes Agent Production Knowledge Repository — Deploy Autonomous AI Agents
description: "Everything the official Hermes docs don't cover. Production-tested patterns from 1,200+ hours of autonomous operations: 6-layer architecture, 133+ skills, 38 crons, 6 memory systems, 37+ MCP connectors."
category: Documentation
tags:
  - hermes-agent
  - autonomous-agents
  - production-deployment
  - ai-agent-architecture
  - mcp-ecosystem
last_updated: 2026-06-16
---

<p align="center">
  <img src="https://raw.githubusercontent.com/NousResearch/hermes-agent/main/assets/banner.png" alt="Hermes Agent" width="600">
</p>

<h1 align="center">Hermes Agent — The Production Knowledge Repository</h1>

<p align="center">
  <b>Everything the <a href="https://hermes-agent.nousresearch.com/docs/">official docs</a> don't cover.<br>
  Drawn from 1,200+ hours of production autonomous agent operations.</b>
</p>

<p align="center">
  <a href="https://github.com/CorpusIQ/corpusiq-docs/issues/new?template=submit-repo.yml"><img src="https://img.shields.io/badge/📤_Submit_a_Repo-Add_your_Hermes_resource-brightgreen" alt="Submit a Repo"></a>
  <a href="https://github.com/CorpusIQ/corpusiq-docs/blob/main/hermes/ecosystem.md"><img src="https://img.shields.io/badge/📚_Ecosystem-234_repos-blue" alt="Ecosystem"></a>
  <a href="https://github.com/CorpusIQ/corpusiq-docs"><img src="https://img.shields.io/badge/⭐_Star_us-Make_this_the_#1_Hermes_resource-gold" alt="Star"></a>
</p>

<p align="center">
  <a href="#-quick-start"><b>Quick Start</b></a> ·
  <a href="#-architecture"><b>Architecture</b></a> ·
  <a href="#-memory--knowledge"><b>Memory</b></a> ·
  <a href="#-skills-marketplace"><b>Skills</b></a> ·
  <a href="#-mcp-ecosystem"><b>MCP</b></a> ·
  <a href="#-production-crons"><b>Crons</b></a> ·
  <a href="#-deployment"><b>Deployment</b></a> ·
  <a href="#-ecosystem"><b>Ecosystem</b></a>
</p>

<br>

## Why This Exists

The [official Hermes docs](https://hermes-agent.nousresearch.com/docs/) tell you what each feature does. They don't tell you how to run a production autonomous agent that operates a business.

This repository fills that gap. Every pattern here is drawn from a real production deployment running on:
- **NVIDIA DGX Spark** — primary compute, inference, 96+ skills
- **Apple Mac Mini M4** — worker node, browser automation, content ops
- **38 production crons** — email, social, video, research, governance, monitoring
- **73+ executable skills** — marketing, development, operations, content
- **6 memory systems** — Honcho, GBrain, memcore-cloud, GraphRAG, Dream Cycle, Session DB
- **195K+ stars** on the core [Hermes Agent repo](https://github.com/NousResearch/hermes-agent)

**This is the repo you wish existed when you started building production agents.**

---

## 📖 Table of Contents

- [Quick Start — Production in 15 Minutes](#-quick-start)
- [Architecture — The 6-Layer Model](#-architecture)
- [Memory & Knowledge](#-memory--knowledge)
- [Skills Marketplace](#-skills-marketplace)
- [MCP Ecosystem](#-mcp-ecosystem)
- [Production Cron Reference](#-production-crons)
- [Deployment Patterns](#-deployment)
- [Content Operations at Scale](#-content-operations)
- [Governance & Operations](#-governance--operations)
- [Community Ecosystem](#-ecosystem)
- [Contributing](#-contributing)

---

## 🚀 Quick Start

### Production deployment in 15 minutes

```bash
# 1. Install Hermes Agent
pip install hermes-agent

# 2. Initialize with a profile
hermes profile create my-agent

# 3. Set up persistent memory (choose your stack)
# Option A: Honcho (peer memory + semantic search)
hermes mcp add honcho -- npx mcp-remote https://mcp.honcho.dev

# Option B: GBrain (organizational knowledge base)
git clone https://github.com/garrytan/gbrain && cd gbrain && ./setup.sh

# Option C: memcore-cloud (self-evolving memory)
pip install memcore-cloud && memcore-cloud init

# 4. Add your first MCP server for business tools
hermes mcp add corpusiq -- url https://mcp2.corpusiq.io/mcp

# 5. Deploy your first autonomous cron
hermes cron create --prompt "Check email every 15 minutes, classify leads, respond to urgent" --schedule "*/15 * * * *"

# 6. Go deeper with the content guides below
```

**Next steps:** [Full Setup Guide](/hermes/setup/) · [Infrastructure](/hermes/infrastructure/) · [Governance](/hermes/governance/)

---

## 🏗 Architecture

### The 6-Layer Production Model

Most Hermes setups are single-machine, human-driven chat loops. Production requires six distinct layers:

```
┌─────────────────────────────────────────────────────────────┐
│                    GOVERNANCE LAYER                          │
│  System Registry · Email Ops · 38 Crons · Token Lifecycle   │
├─────────────────────────────────────────────────────────────┤
│                  CONTENT OPERATIONS                          │
│  Video Pipeline · Social Publishing · Engagement Engines     │
├─────────────────────────────────────────────────────────────┤
│                 KNOWLEDGE & MEMORY                           │
│  GBrain · Honcho · memcore-cloud · GraphRAG · Dream Cycle   │
├─────────────────────────────────────────────────────────────┤
│                   SKILLS & TOOLS                             │
│  73+ Skills · 65 CLI Tools · MCP Infrastructure              │
├─────────────────────────────────────────────────────────────┤
│                   INFRASTRUCTURE                             │
│  DGX Spark · Mac Mini M4 · Browser Auto · Auth · Routing    │
├─────────────────────────────────────────────────────────────┤
│                 AGENT ORCHESTRATION                          │
│  Hermes v0.16+ · CrewAI · LangGraph · Reflexion             │
└─────────────────────────────────────────────────────────────┘
```

**Read the full architecture:** [content/architecture.md](/hermes/architecture/)

### Multi-Machine Deployment

| Node | Role | Hardware | Primary Workload |
|------|------|----------|------------------|
| **DGX Spark** | Primary | NVIDIA ARM64 | Inference, orchestration, 96+ skills, LLM routing |
| **Mac Mini M4** | Worker | Apple Silicon 16GB | Browser automation, Postiz publishing, FFmpeg video |

**Why two machines?** Browser automation is noisy, GPU-hungry, and crash-prone. Offloading it to a dedicated worker keeps the primary agent stable. SSH orchestration between nodes is zero-config with Hermes profiles.

[Full deployment guide →](/hermes/infrastructure/)

---

## 🧠 Memory & Knowledge

The single biggest gap between a chat agent and an autonomous operator is **persistent knowledge**. Without memory, every session starts from zero. Here's the stack we run:

### Memory Stack Comparison

| System | Type | What It Solves | Setup Time |
|--------|------|----------------|------------|
| **[Honcho](https://mcp.honcho.dev)** | Peer memory | Who are you, what platforms are banned, what decisions were made | 2 min |
| **[GBrain](https://github.com/garrytan/gbrain)** | Organizational knowledge | What files exist, what code does what, what was built when | 10 min |
| **[memcore-cloud](https://github.com/memcore-cloud)** | Self-evolving memory | Cross-session context injection, raw source tracking, FTS5 recall | 5 min |
| **GraphRAG** | Relationship memory | How entities and concepts connect — not just what documents say | 30 min |
| **Dream Cycle** | Consolidation | Nightly job at 3 AM that merges, deduplicates, and strengthens memories | Cron |
| **Session DB** | SQLite + FTS5 | Full conversation history, searchable across sessions | Built-in |

### The Honcho + GBrain + memcore-cloud Pattern

This is the production-tested triple stack:

```
Session Start
    │
    ├── Honcho: Load peer context (bans, tokens, rules, preferences)
    ├── GBrain: Query organizational knowledge (files, code, architecture)
    ├── memcore-cloud: Inject cross-session context (what happened last time)
    │
    ▼
Agent operates with full context
    │
    ▼
Session End (or every 30 min)
    │
    ├── Honcho: Write new observations, update peer models
    ├── GBrain: Index new files, update embeddings
    ├── Dream Cycle: Queue consolidation for 3 AM
    └── Session DB: Auto-logged by Hermes
```

**Read the full memory guide →** [content/knowledge/](/hermes/knowledge/)

### Memory: Why Not Just Vector DB?

| Approach | Good For | Bad For |
|----------|----------|---------|
| **Simple Vector DB** | Semantic search over documents | No peer identity, no conversation history, no consolidation |
| **Honcho** | Peer identity, conversation memory, decision tracking | Raw document search |
| **GBrain** | Organizational knowledge, code understanding, file indexing | Conversation history |
| **memcore-cloud** | Cross-session context injection, raw source tracking | Peer modeling |
| **All three together** | Complete agent memory architecture | Slightly more setup (15 min) |

**Key insight:** These aren't competitors — they solve different problems. Run all three.

---

## 🛠 Skills Marketplace

Hermes Agent ships with a built-in skill system. Skills are reusable, self-contained workflows that the agent loads on demand. Here's what we've built and tested in production:

### By Category

| Category | Count | Highlights |
|----------|-------|------------|
| **Marketing** | 45 | SEO comparison pages, CRO optimization, ad analytics, content strategy, community engagement |
| **Development** | 12 | GitHub PR workflows, code review, CI/CD, repo management, codebase inspection |
| **Operations** | 8 | Email automation, cron management, system audits, lead capture |
| **Content** | 5 | Video generation (HeyGen), social publishing (Postiz), engagement engines |
| **Governance** | 3 | System registry, drift prevention, session handoff |

### Top 10 Most-Used Skills

1. **corpusiq-social-cadence-engine** — 6x daily social posting across X, LinkedIn, TikTok, Instagram, YouTube
2. **corpusiq-email-operating-rules** — Autonomous inbox management with 4-tier classification
3. **help-first-community-engagement** — Find operators asking questions, answer without selling
4. **corpusiq-heygen-video-pipeline** — Daily UGC video generation with 10-scenario rotation
5. **corpusiq-daily-html-reporting** — 6 PM daily report with 6 locked sections
6. **corpusiq-execution-discipline** — No-permission-gates, framework-first, data-driven execution
7. **corpusiq-organic-discovery** — Find organic promotion opportunities across platforms
8. **corpusiq-autonomous-growth-intelligence** — Proactive gap-spotting and improvement recommendations
9. **corpusiq-session-start** — Mandatory pre-flight checks before every session
10. **corpusiq-governance-system** — Registry verification, drift detection, integrity checks

### Where Skills Come From

| Source | URL | What You Get |
|--------|-----|--------------|
| **[agentskills.io](https://agentskills.io)** | Open standard skill hub | Cross-agent compatible skills |
| **[skills.sh](https://skills.sh)** | Community marketplace | New skills discovered daily |
| **[wondelai/skills](https://github.com/wondelai/skills)** | 380+ stars | Cross-platform skills library |
| **[tlehman/litprog-skill](https://github.com/tlehman/litprog-skill)** | 75+ stars | Literate programming support |
| **This repo** | `/content/skills/` | Production-tested, CorpusIQ-optimized |

[Full skills catalog →](/hermes/skills/)

---

## 🔌 MCP Ecosystem

Model Context Protocol (MCP) servers extend Hermes with structured tools. Here's every MCP integration we've tested:

### CorpusIQ MCP — 53 Business Tools

The [CorpusIQ MCP server](https://corpusiq.io) connects Hermes to 37+ business platforms through a single OAuth flow:

| Category | Connectors |
|----------|-----------|
| **CRM** | HubSpot, LeadConnector, Close, ActiveCampaign, Odoo |
| **Analytics** | GA4, PostHog, Search Console |
| **Email** | Gmail, Outlook, Klaviyo, Mailchimp, Constant Contact |
| **Ads** | Google Ads, Meta Ads (Facebook + Instagram), LinkedIn Ads, TikTok Ads |
| **Ecommerce** | Shopify, Amazon Seller, eBay, Stripe |
| **Finance** | QuickBooks |
| **SEO** | Ahrefs, Semrush |
| **Social** | YouTube, TikTok, Slack, Instagram, Facebook |
| **Storage** | Google Drive, OneDrive, Dropbox, Airtable, Notion |
| **Calendar** | Google Calendar, Outlook Calendar, Calendly |
| **Database** | PostgreSQL, MSSQL, Cosmos DB, MongoDB |
| **Other** | Monday.com, Postscript (SMS), GunBroker |

**One OAuth flow. 53 tools. 37+ platforms.** No more managing 37 API keys.

```bash
# Add CorpusIQ MCP to Hermes
hermes mcp add corpusiq -- url https://mcp2.corpusiq.io/mcp
```

### Other MCP Servers We Use

| Server | Purpose | Setup |
|--------|---------|-------|
| **[Honcho](https://mcp.honcho.dev)** | Peer memory & identity | `npx mcp-remote https://mcp.honcho.dev` |
| **[hermes-studio](https://github.com/EKKOLearnAI/hermes-studio)** | Web dashboard | `hermes mcp add hermes-studio` |
| **[EverOS](https://github.com/EverMind-AI/EverOS)** | Self-evolving memory | Standalone service |

[Full MCP guide →](/hermes/mcp/)

### MCP Directory Submissions

We maintain CorpusIQ listings across MCP directories:

| Directory | Status | URL |
|-----------|--------|-----|
| **Smithery** | ✅ Live | [smithery.ai](https://smithery.ai) |
| **mcp.so** | ✅ Live | [mcp.so](https://mcp.so) |
| **mcpservers.org** | ✅ Live | [mcpservers.org](https://mcpservers.org) |
| **glama.ai** | ⏳ Pending | Manual browser OAuth required |

---

## ⏰ Production Crons

38 production crons run this agent autonomously. Here's the reference architecture:

### Cron Categories

| Category | Count | Examples |
|----------|-------|----------|
| **Email Operations** | 4 | Monitor (every 15m), Responder (every 30m), Forward handler, Job reply forwarder |
| **Social Publishing** | 3 | Social posting (3x daily), Daily rotation, GitHub promotion |
| **Content Operations** | 2 | Video pipeline (6 AM daily), Content cross-posting |
| **Community Engagement** | 5 | Help-first commenting (6x daily), GitHub issues (4x), Channel scan, IG monitoring |
| **Research & Discovery** | 5 | Tech research (every 6h), MCP server monitor, Skills monitor, GitHub discovery, PH RSS |
| **Governance** | 6 | Health monitor (10 PM), Self-improvement (11 PM), Drift prevention (1 AM), Auth check, MCP directory check, Docs monitor |
| **Memory** | 1 | GBrain dream cycle (3 AM) |
| **Growth** | 2 | Organic discovery, Daily growth geo tools |
| **Job Search** | 1 | Daily job search + resume generation (7 AM) |
| **GitHub** | 2 | Issue poller (every minute), Auto-ack issues (every 6h) |
| **Hermes Release** | 1 | Release monitor (3x daily) |

### Cron Schedule Map (Arizona Time)

```
00:00 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
01:00 ██ Drift prevention
02:00 ██ Hermes release check
03:00 ██ GBrain dream cycle · MCP server monitor
04:00 ██ Skills monitor
05:00 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
06:00 ████████ Video pipeline · Social posting · Help-first commenting
07:00 ████████████ Job search · Auth health · Daily rotation · Growth tools · Organic discovery
08:00 ██████ GitHub promotion · Help-first · Channel scan · Cross-platform monitor
09:00 ██████ Social posting · GitHub discovery
10:00 ████████████ Help-first · IG monitor · MCP directory · GitHub issues · Hermes release
11:00 ██ MCP server monitor
12:00 ████ Help-first · Skills monitor
13:00 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
14:00 ██ Daily rotation
15:00 ████ Social posting · Help-first · IG monitor
16:00 ██ GitHub promotion
17:00 ████ Help-first · GitHub issues
18:00 ██████ Daily report (6 PM) · Hermes release
19:00 ██ MCP server monitor · Organic discovery
20:00 ████ Skills monitor · Cross-platform monitor
21:00 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
22:00 ██ System health monitor
23:00 ██ Daily self-improvement
```

**Every line is a cron you can copy.** [Full cron reference →](/hermes/governance/scheduling/)

---

## 🖥 Deployment

### Multi-Machine Architecture

```
┌────────────────────────────────────────────────────────────┐
│                      DGX SPARK (Primary)                    │
│                                                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │ Hermes   │  │  CrewAI  │  │ LangGraph│  │ Reflexion│  │
│  │ v0.16.0  │  │Orchestra-│  │Workflows │  │  Self-   │  │
│  │          │  │   tion   │  │          │  │Improve   │  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘  │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Memory Layer                                        │  │
│  │  Honcho · GBrain · memcore-cloud · GraphRAG         │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  MCP Gateway                                         │  │
│  │  CorpusIQ (53 tools) · Honcho · hermes-studio        │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                            │
│                    SSH Orchestration                        │
└────────────────────────┬───────────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────────┐
│                  MAC MINI M4 (Worker)                       │
│                                                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │ Browser  │  │ Postiz   │  │  FFmpeg  │  │ Playwright│  │
│  │  Use     │  │  Social  │  │  Video   │  │  Browser  │  │
│  │          │  │Publisher │  │  Proc.   │  │  Agents   │  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘  │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### Model Routing Strategy

Not every task needs Claude Opus. Our cost-optimized routing saves ~65% vs premium-only:

| Task Type | Model | Cost/Task |
|-----------|-------|-----------|
| Lightweight ops, simple queries | Qwen | ~$0.001 |
| Local inference, embeddings | Ollama | Free |
| Research, content, coding | DeepSeek V4 | ~$0.01 |
| Strategy, architecture, contracts | Claude Opus | ~$0.05 |

[Full deployment documentation →](/hermes/infrastructure/)

---

## 🎬 Content Operations

Autonomous content production running daily:

### Video Pipeline (6 AM Daily)

Fully automated UGC video production:
- Scenario library with rotation to prevent repeats
- Avatar rotation with gender-balanced casting
- AI-powered script generation
### Video Pipeline (6 AM Daily)

Fully automated UGC video production: scenario rotation library, avatar casting, AI script generation, HeyGen v2 API rendering, FFmpeg post-production, and multi-platform distribution to TikTok, Instagram, and YouTube Shorts.

### Social Publishing (3x Daily)

Scheduled posting across X and LinkedIn. Help-first content strategy — solve operator problems before mentioning product.

[Full content operations guide →](/hermes/content-ops/)

---

## 🏛 Governance & Operations

### System Registry

Every component is registered before creation. No duplicates. No orphaned code. 11 governance files track:
- Skills inventory (73+)
- Cron registry (38 jobs)
- Token lifecycle (Gmail, GitHub, HeyGen, Postiz)
- Platform status (X, LinkedIn, TikTok, Instagram, YouTube)
- Memory systems (Honcho, GBrain, memcore-cloud)

### Email Operations

Autonomous inbox management with tiered classification and SLA-based response routing.

### Nightly Self-Improvement (11 PM)

Reviews the day's mistakes from IMPROVEMENT_LOG.md, patches affected skills, updates memory with learned corrections. The system gets better every night.

[Full governance documentation →](/hermes/governance/)

---

## 🌐 Ecosystem

### Official Resources

| Resource | Stars | Description |
|----------|-------|-------------|
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 195K+ | Core project |
| [Official Docs](https://hermes-agent.nousresearch.com/docs/) | — | Installation, CLI, gateway, tools, skills |
| [Release Notes](https://github.com/NousResearch/hermes-agent/releases) | — | Changelog per version |
| [Discord](https://discord.gg/NousResearch) | — | Community support |
| [autonovel](https://github.com/NousResearch/autonovel) | — | Autonomous long-form writing |
| [hermes-paperclip-adapter](https://github.com/NousResearch/hermes-paperclip-adapter) | — | Paperclip integration |
| [tinker-atropos](https://github.com/NousResearch/tinker-atropos) | — | RL training for tool-calling |

### Memory & Knowledge

| Project | Stars | What It Does |
|---------|-------|-------------|
| [garrytan/gbrain](https://github.com/garrytan/gbrain) | 23K+ | Opinionated agent brain layer |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 82K+ | Persistent context across sessions |
| [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | 7.5K+ | Self-evolving memory across agents |

### User Interfaces

| Project | Stars | Description |
|---------|-------|-------------|
| [hermes-webui](https://github.com/nesquena/hermes-webui) | 14.5K+ | Web interface for Hermes |
| [hermes-desktop](https://github.com/fathah/hermes-desktop) | 12K+ | Desktop companion |
| [hermes-studio](https://github.com/EKKOLearnAI/hermes-studio) | 8K+ | Web dashboard |
| [hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | 500+ | Chat + terminal + skills manager |

### Orchestration & Multi-Agent

| Project | Stars | Description |
|---------|-------|-------------|
| [mission-control](https://github.com/builderz-labs/mission-control) | 3.7K+ | Multi-agent fleet management |
| [PraisonAI](https://github.com/MervinPraison/PraisonAI) | 8K+ | 24/7 AI workforce |
| [manifest](https://github.com/mnfst/manifest) | 7K+ | Connect agents with any provider |

### Skills & Tools

| Resource | Description |
|----------|-------------|
| [agentskills.io](https://agentskills.io) | Open standard skill hub |
| [skills.sh](https://skills.sh) | Community skill marketplace |
| [wondelai/skills](https://github.com/wondelai/skills) | Cross-platform skills library (380+ ★) |
| [tlehman/litprog-skill](https://github.com/tlehman/litprog-skill) | Literate programming skills (75+ ★) |

### Deployment & Infrastructure

| Project | Description |
|---------|-------------|
| [1Panel](https://github.com/1Panel-dev/1Panel) | VPS control panel with native AI agent support (35K+ ★) |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Secure agent execution with managed infrastructure (21K+ ★) |

### Related Awesome Lists

| List | Focus |
|------|-------|
| [awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw) | OpenClaw ecosystem (Hermes predecessor) |
| [awesome-ai-agents-2026](https://github.com/Ben-Home/awesome-ai-agents-2026) | 300+ AI agents and frameworks |

---

## 📊 Production Metrics

From a real deployment running 24/7:

| Metric | Value |
|--------|-------|
| **Active crons** | 28 active, 8 paused |
| **Skills deployed** | 73+ |
| **MCP servers** | 2 (CorpusIQ: 53 tools, Honcho: peer memory) |
| **Memory systems** | 6 (Honcho, GBrain, memcore-cloud, GraphRAG, Dream Cycle, Session DB) |
| **Business connectors** | 37+ (via CorpusIQ MCP) |
| **Platforms published to** | 5 (X, LinkedIn, TikTok, Instagram, YouTube) |
| **Email inboxes monitored** | 2 (team@ + info@) |
| **Cost optimization** | ~65% savings via multi-model routing |
| **Uptime** | 24/7 since June 12, 2026 |

---

## 🗺 Repository Structure

```
/
├── README.md                          ← You are here
├── content/
│   ├── index.md                       ← Content hub
│   ├── architecture.md                ← Full 6-layer architecture
│   ├── setup/                         ← Installation & configuration
│   ├── orchestration/                 ← Hermes, CrewAI, LangGraph, Reflexion
│   │   ├── hermes/
│   │   ├── crewai/
│   │   ├── langgraph/
│   │   └── reflexion/
│   ├── knowledge/                     ← Memory & knowledge architecture
│   ├── skills/                        ← Skills marketplace & development
│   │   ├── marketing/
│   │   ├── development/
│   │   └── operations/
│   ├── mcp/                           ← MCP server guides
│   │   └── servers/
│   ├── infrastructure/                ← Deployment & infrastructure
│   │   ├── dgx/
│   │   ├── mac-mini/
│   │   ├── browser/
│   │   ├── auth/
│   │   └── routing/
│   ├── content-ops/                   ← Content production
│   │   ├── video/
│   │   ├── social/
│   │   └── engagement/
│   ├── governance/                    ← Operations & control
│   │   ├── registry/
│   │   ├── email/
│   │   ├── scheduling/
│   │   └── monitoring/
│   └── outputs/                       ← Production case studies
└── LICENSE
```

---

## 🤝 Contributing

This is a living repository maintained by **CorpusIQ** — the operating system for business agents. Content is generated and updated by monitoring crons that detect new Hermes releases, MCP servers, skills, and community resources.

**To contribute:**
1. Fork the repo
2. Add your production-tested setup, skill, or pattern
3. Submit a PR with details of what you built and how it works in production

We especially welcome:
- Production deployment architectures
- Memory/knowledge stack setups
- Multi-agent orchestration patterns
- MCP server integration guides
- Autonomous cron workflows
- Governance and monitoring approaches

---

## ⭐ Why Star This Repo?

If you're building production AI agents with Hermes, this is your field manual. Everything here is:

- **Production-tested** — Not hypothetical. Runs 24/7.
- **Community-curated** — Pulled from the full Hermes ecosystem.
- **Beyond the docs** — The official docs tell you *what*. This tells you *how*.
- **Actively maintained** — Updated as the ecosystem evolves.

**[Star this repo](https://github.com/CorpusIQ/corpusiq-docs)** if you want the definitive Hermes resource to exist.

---

## FAQ

### What is the Hermes Agent Production Knowledge Repository?

The **Hermes Agent Production Knowledge Repository** is the definitive field manual for running autonomous AI agents in production. Drawn from 1,200+ hours of real 24/7 deployment on DGX Spark + Mac Mini M4, it covers architecture, memory systems, skills, MCP integrations, cron scheduling, and deployment patterns — everything the [official Hermes docs](https://hermes-agent.nousresearch.com/docs/) don't cover.

### How do I deploy Hermes Agent in production?

Follow the [Quick Start guide](#-quick-start) for a 15-minute production setup: install Hermes, initialize a profile, set up persistent memory (Honcho/GBrain/memcore-cloud), add MCP connectors via [CorpusIQ](/hermes/mcp/connectors/), and deploy your first autonomous cron. See the [Architecture section](#-architecture) for the full 6-layer model.

### What hardware and infrastructure does this deployment use?

The documented production deployment runs on **NVIDIA DGX Spark** (primary compute, inference, 96+ skills, 21 cron jobs) and **Apple Mac Mini M4** (worker node, browser automation, social publishing). Multi-machine SSH orchestration is zero-config with Hermes profiles. See [deployment patterns](#-deployment) for the full architecture.

### How many crons and skills does the production deployment run?

The deployment runs **38 production crons** across 11 categories (email ops, social publishing, content ops, community engagement, research, governance, memory, growth, job search, GitHub, release monitoring) and **73+ executable skills** across marketing, development, operations, content, and governance.

### How do I contribute or submit a resource to the ecosystem?

**[Submit a repo →](https://github.com/CorpusIQ/corpusiq-docs/issues/new?template=submit-repo.yml)** — takes 60 seconds. We accept Hermes skills, MCP servers, plugins, tools, UI/dashboards, deployment guides, tutorials, benchmarks, and research. Every submission reviewed within 48 hours and added to the [ecosystem directory](/hermes/ecosystem.md) with full submitter credit.

### What's the difference between this repository and the official Hermes docs?

The [official docs](https://hermes-agent.nousresearch.com/docs/) tell you **what** each feature does. This repository tells you **how** to run a production autonomous agent — covering memory stack architecture, cron scheduling patterns, multi-machine deployment, skill marketplace integration, content operations at scale, and governance systems. Official docs = reference. This repo = field manual.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the Hermes Agent Production Knowledge Repository?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The definitive field manual for running autonomous AI agents in production, drawn from 1,200+ hours of real 24/7 deployment covering architecture, memory, skills, MCP, cron scheduling, and deployment patterns."
      }
    },
    {
      "@type": "Question",
      "name": "How do I deploy Hermes Agent in production?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Follow the Quick Start guide: install Hermes, initialize a profile, set up persistent memory, add MCP connectors via CorpusIQ, and deploy your first autonomous cron. See Architecture for the full 6-layer model."
      }
    },
    {
      "@type": "Question",
      "name": "What hardware and infrastructure does this deployment use?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The production deployment runs on NVIDIA DGX Spark (primary compute, 96+ skills) and Apple Mac Mini M4 (worker, browser automation). Multi-machine SSH orchestration is zero-config with Hermes profiles."
      }
    },
    {
      "@type": "Question",
      "name": "How many crons and skills does the production deployment run?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The deployment runs 38 production crons across 11 categories and 73+ executable skills across marketing, development, operations, content, and governance."
      }
    },
    {
      "@type": "Question",
      "name": "How do I contribute or submit a resource to the ecosystem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Submit a repo in 60 seconds via the submission form. Accepted repos are added to the ecosystem directory with full submitter credit within 48 hours."
      }
    },
    {
      "@type": "Question",
      "name": "What's the difference between this repository and the official Hermes docs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Official docs tell you what each feature does. This repo tells you how to run a production autonomous agent: memory architecture, cron patterns, multi-machine deployment, content ops at scale, and governance."
      }
    }
  ]
}
</script>

## Related Pages

- [Hermes Documentation Index — Complete Reference](/hermes/index.md)
- [Ecosystem Directory — 234+ Community Resources](/hermes/ecosystem.md)
- [Agent Library — 9 Production Agent Blueprints](/hermes/agents/)
- [Skills Catalog — 133+ Production Skills](/hermes/skills/catalog/)
- [Cron Scheduling — 38 Production Cron Reference](/hermes/governance/scheduling/)
- [Architecture — 6-Layer Production Model](/hermes/architecture/)
- [CorpusIQ MCP Connectors — 37+ Business Tools](/hermes/mcp/connectors/)
- [Community Contributors — Join the Directory](/hermes/contributors.md)

---

## 📤 Submit Your Hermes Resource

Have a Hermes-related repo, tool, skill, or integration? 

👉 **[Submit it here — takes 60 seconds](https://github.com/CorpusIQ/corpusiq-docs/issues/new?template=submit-repo.yml)**

Every submission reviewed within 48 hours. Accepted repos added to the [ecosystem directory](https://github.com/CorpusIQ/corpusiq-docs/blob/main/hermes/ecosystem.md) with full submitter credit.

**We accept:** Hermes skills, MCP servers, plugins, tools, UI/dashboards, deployment guides, tutorials, benchmarks, research, and anything extending the Hermes ecosystem.

---

<p align="center">
  <b>Powered by <a href="https://corpusiq.io">CorpusIQ</a> — the operating system for business agents.</b><br>
  <sub>One connector. 37+ tools. Your business data, finally answering your questions.</sub>
</p>


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
