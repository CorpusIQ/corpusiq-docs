---
title: Hermes Ecosystem — Complete Resource Directory
description: The definitive directory of Hermes Agent resources — 121+ repos, official docs, community tools, SDKs, integrations, benchmarks, and research. Everything in the Hermes universe.
---

# Hermes Ecosystem — Complete Resource Directory

The most comprehensive directory of Hermes Agent resources in existence. 121+ repositories, official documentation, community projects, SDKs, integrations, benchmarks, and research — all organized and cross-referenced.

> **Last updated:** June 16, 2026 · **Repos indexed:** 121+ · **Categories:** 14
>
> Missing something? [Open a PR →](https://github.com/CorpusIQ/corpusiq-docs)

---

## 📑 Quick Navigation

| Category | Count | Jump |
|----------|-------|------|
| [Core & Official](#-core--official) | 5 | [↓](#-core--official) |
| [Documentation & Learning](#-documentation--learning) | 8 | [↓](#-documentation--learning) |
| [Community & Awesome Lists](#-community--awesome-lists) | 12 | [↓](#-community--awesome-lists) |
| [UI & Dashboards](#-ui--dashboards) | 8 | [↓](#-ui--dashboards) |
| [Memory & Knowledge](#-memory--knowledge) | 12 | [↓](#-memory--knowledge) |
| [MCP & Integrations](#-mcp--integrations) | 8 | [↓](#-mcp--integrations) |
| [Skills & Plugins](#-skills--plugins) | 15 | [↓](#-skills--plugins) |
| [Orchestration & Multi-Agent](#-orchestration--multi-agent) | 8 | [↓](#-orchestration--multi-agent) |
| [Deployment & Infrastructure](#-deployment--infrastructure) | 10 | [↓](#-deployment--infrastructure) |
| [Security & Governance](#-security--governance) | 5 | [↓](#-security--governance) |
| [Research & Benchmarks](#-research--benchmarks) | 12 | [↓](#-research--benchmarks) |
| [Content & Media](#-content--media) | 6 | [↓](#-content--media) |
| [Platform-Specific](#-platform-specific) | 10 | [↓](#-platform-specific) |
| [Specialized Applications](#-specialized-applications) | 8 | [↓](#-specialized-applications) |

---

## 🏛 Core & Official

The foundational repositories maintained by Nous Research and core ecosystem maintainers.

### NousResearch/hermes-agent
⭐ **195,064** · `Python` · [github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

The agent that grows with you. Self-improving autonomous AI agent with persistent memory, self-evolving skills, multi-platform messaging gateway (Telegram, Discord, Slack, WhatsApp, Signal, Feishu, WeCom, QQBot, Yuanbao + Teams via plugin), cron scheduling, MCP integration, profiles, and ACP (Agent Communication Protocol). Supports Anthropic, ChatCompletions, Responses API, and Bedrock model providers. 18 messaging platforms, 7 execution backends.

**Maintainer:** [Nous Research](https://nousresearch.com)  
**Docs:** [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs)  
**Discord:** [discord.gg/NousResearch](https://discord.gg/NousResearch)  
**Key capabilities:** Autonomous agent loop, closed learning cycle, multi-platform gateway, cron scheduler, MCP client, skill system, memory providers, model fallback chains  
**Related:** [Hermes Knowledge Hub →](/hermes/) · [Setup Guide →](/hermes/setup/) · [Architecture →](/hermes/architecture/)

---

### NousResearch/hermes-agent-self-evolution
⭐ **4,116** · `Python` · [github.com/NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution)

Evolutionary self-improvement for Hermes Agent using DSPy + GEPA (Genetic Evolution of Prompt Architectures). Automatically generates eval datasets, mutates prompts/tools/skills, evaluates variants across multiple metrics, and auto-files PRs with improvements. ICLR 2026 Oral.

**Maintainer:** Nous Research  
**Key capabilities:** Automatic skill optimization, prompt mutation, eval dataset generation, multi-metric evaluation, automated PR filing  
**Status:** Production-ready · ~$0.10 per optimization run on Gemini Flash  
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### NousResearch/hermes-paperclip-adapter
⭐ **1,598** · `Python` · [github.com/NousResearch/hermes-paperclip-adapter](https://github.com/NousResearch/hermes-paperclip-adapter)

Run Hermes as a managed employee inside Paperclip companies. Connects the agent to Paperclip's task management and governance system — Hermes becomes a deployable workforce unit.

**Maintainer:** Nous Research  
**Key capabilities:** Paperclip integration, managed agent deployment, task management bridge

---

### NousResearch/autonovel
⭐ **1,148** · `Python` · [github.com/NousResearch/autonovel](https://github.com/NousResearch/autonovel)

Autonomous long-form writing pipeline built on Hermes Agent. Generates full manuscripts (100K+ words) end-to-end using the agent loop — plot development, chapter writing, consistency checking.

**Maintainer:** Nous Research  
**Key capabilities:** Long-form content generation, plot management, chapter coherence, agent-driven writing  
**Related:** [Content Operations →](/hermes/content-ops/)

---

### NVIDIA/NemoClaw
⭐ **21,237** · `Python` · [github.com/NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)

Run agents like Hermes and OpenClaw more securely inside NVIDIA OpenShell with managed infrastructure. Hardware-enforced sandboxing for autonomous agents.

**Maintainer:** NVIDIA  
**Key capabilities:** Secure agent sandboxing, hardware-enforced isolation, managed infrastructure  
**Related:** [Deployment →](/hermes/infrastructure/)

---

## 📚 Documentation & Learning

Tutorials, guides, and educational resources for mastering Hermes Agent.

### alchaincyf/hermes-agent-orange-book
⭐ **4,443** · `Markdown` · [github.com/alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book)

"Hermes Agent 从入门到精通" — The Orange Book series. Comprehensive Chinese-language guide to Hermes Agent from beginner to expert. Covers installation, configuration, skills, MCP, deployment, and production patterns.

**Maintainer:** alchaincyf  
**Language:** Chinese (中文)  
**Key capabilities:** Complete tutorial series, production deployment patterns, skill development guide

---

### longyunfeigu/learn-hermes-agent
⭐ **153** · `Markdown` · [github.com/longyunfeigu/learn-hermes-agent](https://github.com/longyunfeigu/learn-hermes-agent)

27-chapter hands-on tutorial for building an autonomous AI agent from scratch. Step-by-step implementation guide covering the full Hermes architecture.

**Maintainer:** longyunfeigu  
**Language:** Chinese (中文)  
**Key capabilities:** 27-chapter curriculum, hands-on exercises, architecture deep-dive

---

### mudrii/hermes-agent-docs
⭐ **58** · `Markdown` · [github.com/mudrii/hermes-agent-docs](https://github.com/mudrii/hermes-agent-docs)

Comprehensive community-maintained documentation for Hermes Agent. Extends the official docs with practical examples, troubleshooting, and deployment patterns.

**Maintainer:** mudrii  
**Key capabilities:** Extended documentation, practical examples, community patterns

---

### Hermes Official Documentation
[hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs/)

Complete official documentation: quickstart, CLI, configuration, messaging gateway, security, tools, skills, memory, MCP, cron, ACP, API server, and architecture. The authoritative reference.

**Maintainer:** Nous Research  
**Related:** [Hermes Knowledge Hub →](/hermes/) (this repo — everything the docs don't cover)

---

### Hermes Official Release Notes
[github.com/NousResearch/hermes-agent/releases](https://github.com/NousResearch/hermes-agent/releases)

Official changelog with feature highlights, migration notes, and fixes for each version. v0.16.0 is current (June 2026).

---

### Hermes Discord Community
[discord.gg/NousResearch](https://discord.gg/NousResearch)

Official Nous Research Discord. Hermes channel for real-time discussion, support, feature requests, and community showcases. Active with 10K+ members.

---

### Hermes Reddit Community
[r/hermesagent](https://www.reddit.com/r/hermesagent/)

Community subreddit with use cases, troubleshooting, production patterns, and creative applications. Megathread: [Hermes Agent Use Cases](https://www.reddit.com/r/hermesagent/comments/1t6gf4j/megathread_hermes_agent_use_cases_what_the/)

---

### xianyu110/awesome-HermesAgent-tutorial
⭐ **8** · [github.com/xianyu110/awesome-HermesAgent-tutorial](https://github.com/xianyu110/awesome-HermesAgent-tutorial)

Tutorial on running Hermes Agent on a server — autonomous agent with built-in learning loop, cross-platform messaging, and 200+ model routing.

---

## 👥 Community & Awesome Lists

Curated resource collections maintained by the Hermes community.

### 0xNyk/awesome-hermes-agent
⭐ **4,017** · [github.com/0xNyk/awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)

Curated list of awesome skills, tools, integrations, and resources for Hermes Agent. The most comprehensive community-maintained awesome list. Active updates.

---

### SamurAIGPT/awesome-hermes-agent
⭐ **1,738** · [github.com/SamurAIGPT/awesome-hermes-agent](https://github.com/SamurAIGPT/awesome-hermes-agent)

Curated collection of skills, plugins, tools, integrations, and resources. Includes ecosystem snapshot reviews and maturity labels (production/beta/experimental).

---

### Ben-Home/awesome-hermes-agent
⭐ **0** · [github.com/Ben-Home/awesome-hermes-agent](https://github.com/Ben-Home/awesome-hermes-agent)

Curated list maintained by CorpusIQ — cross-linked with this knowledge hub for in-depth production guides.

**Related:** [This repository →](/hermes/)

---

### aliaihub/awesome-hermes-usecases
⭐ **101** · [github.com/aliaihub/awesome-hermes-usecases](https://github.com/aliaihub/awesome-hermes-usecases)

Curated real-world use cases for Hermes Agent — the self-improving AI agent from Nous Research. Production deployment stories and patterns.

---

### ChuckSRQ/awesome-hermes-skills
⭐ **66** · [github.com/ChuckSRQ/awesome-hermes-skills](https://github.com/ChuckSRQ/awesome-hermes-skills)

Curated collection of production-ready Hermes Agent skills — brainstorming, PR reviews, code generation, content creation.

---

### ZeroPointRepo/awesome-hermes-skills
⭐ **57** · [github.com/ZeroPointRepo/awesome-hermes-skills](https://github.com/ZeroPointRepo/awesome-hermes-skills)

85 built-in + 78 community skills, install-ready for Hermes Agent. Well-organized skill catalog with installation instructions.

---

### jefferyjob/awesome-hermes-agent-zh
⭐ **55** · [github.com/jefferyjob/awesome-hermes-agent-zh](https://github.com/jefferyjob/awesome-hermes-agent-zh)

Chinese-language curated list of skills, tools, integrations for Hermes Agent. (Hermes Agent 实用技能、工具、集成和资源列表)

---

### 0xarkstar/awesome-hermes-agent
⭐ **32** · [github.com/0xarkstar/awesome-hermes-agent](https://github.com/0xarkstar/awesome-hermes-agent)

Curated list of awesome resources for Hermes Agent by Nous Research.

---

### zcweah1981/awesome-hermes-agent-zh
⭐ **25** · [github.com/zcweah1981/awesome-hermes-agent-zh](https://github.com/zcweah1981/awesome-hermes-agent-zh)

Hermes Agent Chinese-language portal — entry path, deployment, OpenClaw migration, troubleshooting, downloadable solution packs.

---

### AlexAnys/awesome-openclaw-usecases-zh
⭐ **4,322** · [github.com/AlexAnys/awesome-openclaw-usecases-zh](https://github.com/AlexAnys/awesome-openclaw-usecases-zh)

OpenClaw Chinese use case encyclopedia — 50 real scenarios including domestic adaptations of international cases. Automation, content creation, ops, AI assistant, knowledge management.

**Related:** Hermes is the successor to OpenClaw — most patterns apply directly.

---

### SamurAIGPT/awesome-openclaw
[github.com/SamurAIGPT/awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw)

Curated resources for OpenClaw (Hermes predecessor) with native Hermes migration path.

---

### CorpusIQ/corpusiq-docs/hermes ← YOU ARE HERE
⭐ **[Star this repo →](https://github.com/CorpusIQ/corpusiq-docs)**

The most comprehensive Hermes production resource: 36+ pages, 121+ repos indexed, 133+ skills cataloged, 37+ MCP connectors, 38-cron reference architecture, memory stack deep-dives, deployment patterns. Everything the official docs don't cover.

**Related:** [Architecture →](/hermes/architecture/) · [Knowledge →](/hermes/knowledge/) · [Crons →](/hermes/governance/scheduling/) · [MCP →](/hermes/mcp/)

---

## 🖥 UI & Dashboards

Visual interfaces for managing and interacting with Hermes Agent.

### nesquena/hermes-webui
⭐ **14,540** · `TypeScript` · [github.com/nesquena/hermes-webui](https://github.com/nesquena/hermes-webui)

Hermes WebUI: The best way to use Hermes Agent from the web or from your phone. Full-featured web interface with chat, session management, and mobile support.

**Maintainer:** nesquena  
**Key capabilities:** Web chat interface, mobile-responsive, session management, multi-profile support

---

### fathah/hermes-desktop
⭐ **12,296** · `TypeScript` · [github.com/fathah/hermes-desktop](https://github.com/fathah/hermes-desktop)

Desktop Companion for Hermes Agent. Native desktop application with system tray integration, notifications, and always-on access.

**Maintainer:** fathah  
**Key capabilities:** Native desktop app, system tray, notifications, always-on

---

### EKKOLearnAI/hermes-studio
⭐ **8,000** · `TypeScript` · [github.com/EKKOLearnAI/hermes-studio](https://github.com/EKKOLearnAI/hermes-studio)

Web dashboard for Hermes Agent — multi-platform AI chat, session management, scheduled jobs overview, skills browser, and agent configuration. MCP-native.

**Maintainer:** EKKOLearnAI  
**Key capabilities:** Session management, cron visualization, skills browser, multi-platform chat, MCP integration

---

### outsourc-e/hermes-workspace
⭐ **5,720** · `TypeScript` · [github.com/outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace)

Native web workspace for Hermes Agent — chat, terminal, memory browser, skills manager. All-in-one workspace environment.

**Maintainer:** outsourc-e  
**Key capabilities:** Integrated terminal, memory browser, skills manager, chat interface

---

### qingchencloud/clawpanel
⭐ **2,842** · `TypeScript` · [github.com/qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel)

OpenClaw & Hermes Agent multi-engine AI management panel — built-in AI assistant with tool calling, image recognition, multimodal, one-click deployment.

**Language:** Chinese (中文)  
**Key capabilities:** Multi-engine management, tool calling, image recognition, one-click deployment

---

### awizemann/scarf
⭐ **629** · `Swift` · [github.com/awizemann/scarf](https://github.com/awizemann/scarf)

Native macOS and iOS App for the Hermes AI agent — multi-window, multi-profile, native performance. First-class Apple platform experience.

**Maintainer:** awizemann  
**Key capabilities:** Native macOS/iOS, multi-window, multi-profile, Apple design language

---

### kkllxy/hermes-web-ui
⭐ **0** · [github.com/kkllxy/hermes-web-ui](https://github.com/kkllxy/hermes-web-ui)

Web dashboard for Hermes Agent — multi-platform AI chat, session management, scheduled jobs overview.

---

### nexu-io/open-design
⭐ **65,835** · `TypeScript` · [github.com/nexu-io/open-design](https://github.com/nexu-io/open-design)

Local-first, open-source alternative to Claude Design. Native desktop app with 259+ skills. While not Hermes-specific, it demonstrates the broader agent UI ecosystem.

**Related:** Hermes-compatible skills format. Many skills are cross-compatible.

---

## 🧠 Memory & Knowledge

Persistent memory and knowledge management for autonomous agents.

### thedotmack/claude-mem
⭐ **82,700** · `TypeScript` · [github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

Persistent context across sessions for every agent. Captures everything your agent does — files, conversations, decisions — and makes it retrievable. Works with Hermes, Claude Code, Codex, and other agents.

**Key capabilities:** Cross-agent memory, persistent context, automatic capture, retrieval across sessions  
**Related:** [Knowledge Architecture →](/hermes/knowledge/)

---

### garrytan/gbrain
⭐ **22,991** · `Python` · [github.com/garrytan/gbrain](https://github.com/garrytan/gbrain)

Garry's Opinionated OpenClaw/Hermes Agent Brain. Persistent organizational memory with file indexing, semantic search, and knowledge consolidation. 729+ indexed files in our deployment.

**Maintainer:** Garry Tan (Y Combinator)  
**Key capabilities:** File indexing, semantic search, pglite database, 768d embeddings, Dream Cycle consolidation  
**Related:** [Knowledge Architecture →](/hermes/knowledge/) · [Setup Guide →](/hermes/setup/)

---

### EverMind-AI/EverOS
⭐ **7,528** · `Python` · [github.com/EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS)

Self-evolving memory across Agent and platform. The one portable memory layer for every agent — works across Hermes, Claude, GPT, and custom agents.

**Key capabilities:** Self-evolving memory, cross-platform portability, automatic learning  
**Related:** [Memory Stack →](/hermes/knowledge/)

---

### codejunkie99/agentic-stack
⭐ **2,112** · `Python` · [github.com/codejunkie99/agentic-stack](https://github.com/codejunkie99/agentic-stack)

One brain, many harnesses. Portable `.agent/` folder (memory + skills + config) that works across Hermes, Claude Code, Codex, and other agents.

**Key capabilities:** Portable agent configuration, cross-platform memory, unified skill system

---

### AxDSan/mnemosyne
⭐ **1,150** · `Python` · [github.com/AxDSan/mnemosyne](https://github.com/AxDSan/mnemosyne)

The Zero-Dependency, Sub-Millisecond AI Memory System for Hermes Agent. Ultra-fast local memory with minimal overhead.

**Key capabilities:** Zero dependencies, sub-ms retrieval, local-first, Hermes-native

---

### syncable-dev/memtrace-public
⭐ **193** · `Rust` · [github.com/syncable-dev/memtrace-public](https://github.com/syncable-dev/memtrace-public)

Structural memory for AI coding agents. Bi-temporal graph, MCP-native, tracks code changes and relationships over time.

**Key capabilities:** Bi-temporal graph, code structure tracking, MCP-native interface

---

### yoloshii/ClawMem
⭐ **184** · `Python` · [github.com/yoloshii/ClawMem](https://github.com/yoloshii/ClawMem)

On-device memory layer for AI agents. Works with Claude Code, Hermes, and OpenClaw. Local-first, privacy-preserving memory.

**Key capabilities:** On-device memory, privacy-preserving, multi-agent support

---

### yantrikos/yantrikdb-hermes-plugin
⭐ **60** · `Python` · [github.com/yantrikos/yantrikdb-hermes-plugin](https://github.com/yantrikos/yantrikdb-hermes-plugin)

YantrikDB memory provider for Hermes Agent — self-maintaining database with automatic indexing and cleanup.

---

### prakrititz/relayBrain
[github.com/prakrititz/relayBrain](https://github.com/prakrititz/relayBrain)

Portable memory layer for AI agents — switch between Claude, Codex, Gemini, and Hermes without losing context.

---

### screenpipe/screenpipe
⭐ **19,319** · `Rust` · [github.com/screenpipe/screenpipe](https://github.com/screenpipe/screenpipe)

YC S26 — AI that knows what you've seen, said, or heard. Records everything you do and makes it searchable for agents. Hermes-compatible via API.

**Key capabilities:** Screen recording, audio capture, searchable history, agent context

---

### memcore-cloud
Self-evolving memory with cross-session context injection. Auto-injects relevant history into every Hermes turn. Used in our production deployment.

**Related:** [Memory Architecture →](/hermes/knowledge/)

---

### Honcho
Peer memory and identity platform. Conversation continuity, semantic search, peer modeling. MCP-native integration with Hermes.

**Related:** [Knowledge Architecture →](/hermes/knowledge/) · [MCP Integration →](/hermes/mcp/)

---

## 🔌 MCP & Integrations

Model Context Protocol servers and integration bridges for Hermes.

### CorpusIQ MCP Server
[mcp2.corpusiq.io/mcp](https://mcp2.corpusiq.io/mcp)

One OAuth flow. 53 tools. 37+ business platforms. Connect Hermes to Gmail, GA4, Stripe, HubSpot, QuickBooks, Meta Ads, Google Ads, Shopify, Klaviyo, and more through a single MCP server.

**Maintainer:** CorpusIQ  
**Key capabilities:** 37+ business connectors, single OAuth, cross-source analysis, device login flow  
**Related:** [MCP Guide →](/hermes/mcp/) · [Connector Reference →](/hermes/mcp/connectors/)

---

### Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server
⭐ **345** · `Python` · [github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server)

Kindly Web Search MCP Server — web search + robust content retrieval for Hermes and other MCP-compatible agents.

---

### KSroido/Kagi-Session2API-MCP
⭐ **137** · `Python` · [github.com/KSroido/Kagi-Session2API-MCP](https://github.com/KSroido/Kagi-Session2API-MCP)

Free Kagi Search MCP server — access Kagi search and summarizer via session tokens. Hermes-compatible.

---

### zoedsoupe/anubis-mcp
⭐ **147** · `Elixir` · [github.com/zoedsoupe/anubis-mcp](https://github.com/zoedsoupe/anubis-mcp)

Elixir Model Context Protocol (MCP) SDK — forked from hermes-mcp. Bring MCP capabilities to Elixir ecosystems.

---

### ninemindai/agentback
[github.com/ninemindai/agentback](https://github.com/ninemindai/agentback)

AI-native API/MCP framework built for the agent era. Designed to work with Hermes and other autonomous agents.

---

### unifapi-agent/agents
⭐ **491** · `TypeScript` · [github.com/unifapi-agent/agents](https://github.com/unifapi-agent/agents)

Open-source marketing agents for Claude, ChatGPT, Codex, OpenClaw & Hermes. Pre-built marketing workflows as pluggable agents.

---

### BlockRunAI/ClawRouter-Hermes
⭐ **12** · `Python` · [github.com/BlockRunAI/ClawRouter-Hermes](https://github.com/BlockRunAI/ClawRouter-Hermes)

ClawRouter for Hermes — 55+ LLMs, x402 USDC micropayments on Base & Solana. Pay-per-use model routing for Hermes agents.

---

### AlexAI-MCP/hermes-CCC
⭐ **119** · `Python` · [github.com/AlexAI-MCP/hermes-CCC](https://github.com/AlexAI-MCP/hermes-CCC)

Hermes Agent ported to Claude Code Channel — 46 native skills, no OAuth required. Run Hermes skills inside Claude Code.

---

## 🛠 Skills & Plugins

Extend Hermes with community-built skills and plugins.

### wondelai/skills
⭐ **380+** · [github.com/wondelai/skills](https://github.com/wondelai/skills)

Cross-platform skills library that works with Hermes, Claude Code, and other agents. Actively maintained with growing catalog.

---

### coreyhaines31/marketingskills (Ben-Home/marketingskills)
⭐ **0** · [github.com/Ben-Home/marketingskills](https://github.com/Ben-Home/marketingskills)

Complete CMO stack: 45+ marketing skills covering SEO, CRO, copywriting, cold email, ads, analytics, community, launch, pricing, competitors, directory submissions, revops, and content strategy. Includes 51 CLI tools and 200+ directory targets.

**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### tlehman/litprog-skill
⭐ **75+** · [github.com/tlehman/litprog-skill](https://github.com/tlehman/litprog-skill)

Literate programming support across Hermes, Claude Code, and OpenCode. Write code and documentation together.

---

### jnMetaCode/superpowers-zh
⭐ **5,450** · [github.com/jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh)

AI coding superpowers — Chinese enhanced edition. 6 original Chinese skills for Hermes Agent, Claude Code, Cursor, Copilot and other tools.

---

### jnMetaCode/agency-agents-zh
⭐ **15,046** · [github.com/jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh)

216 plug-and-play AI expert roles — supports Hermes Agent, Claude Code, Cursor, Copilot and 17 other tools. Covers engineering, design, marketing, finance, and more.

---

### Romanescu11/hermes-skill-factory
⭐ **381** · `Python` · [github.com/Romanescu11/hermes-skill-factory](https://github.com/Romanescu11/hermes-skill-factory)

A meta-skill plugin for Hermes AI agent that watches your workflow and auto-creates skills from repeated patterns.

---

### GumbyEnder/hermes-kanban
⭐ **252** · `TypeScript` · [github.com/GumbyEnder/hermes-kanban](https://github.com/GumbyEnder/hermes-kanban)

Dedicated Obsidian plugin + Hermes skill that turns Hermes into an autonomous Kanban project manager.

---

### buzzicra/skillguard
[github.com/buzzicra/skillguard](https://github.com/buzzicra/skillguard)

Scan agent skills, MCP configs, and instruction files for risky behavior. Security audit tool for Hermes skill ecosystems.

---

### Agnuxo1/cajal-hermes-skill
⭐ **2** · [github.com/Agnuxo1/cajal-hermes-skill](https://github.com/Agnuxo1/cajal-hermes-skill)

CAJAL scientific paper generation skill for Hermes Agent. Generate research papers following CAJAL methodology.

---

### 0451-software/research-skills
⭐ **0** · [github.com/0451-software/research-skills](https://github.com/0451-software/research-skills)

Research skills for Hermes Agent — paper discovery, archiving, reading, and synthesis.

---

### Undermybelt/hermes-skills-research
⭐ **0** · [github.com/Undermybelt/hermes-skills-research](https://github.com/Undermybelt/hermes-skills-research)

Hermes Agent research skills — paper discovery, literature review, academic research workflows.

---

### dowmar/paper2podcast
⭐ **5** · [github.com/dowmar/paper2podcast](https://github.com/dowmar/paper2podcast)

Hermes skill to transform research papers into studio-quality podcast scripts and audio.

---

### BBridgeers/hermes-skills
⭐ **0** · [github.com/BBridgeers/hermes-skills](https://github.com/BBridgeers/hermes-skills)

372 AI agent skills exported from production Hermes Agent deployment. Massive community skill collection.

---

### crispyb0i/hermes-operator-pack
⭐ **1** · [github.com/crispyb0i/hermes-operator-pack](https://github.com/crispyb0i/hermes-operator-pack)

Battle-tested Hermes Agent skills for solo founders running a portfolio of businesses.

---

### CorpusIQ Skills (This Repo)
[Browse 133+ skills →](/hermes/skills/catalog/)

Our production-tested skill catalog: 45 marketing skills, 12 development skills, 8 operations skills, 5 content skills, 3 governance skills. All tested in 24/7 production deployment.

---

## 🎯 Orchestration & Multi-Agent

Frameworks and patterns for coordinating multiple agents.

### CherryHQ/cherry-studio
⭐ **47,420** · `TypeScript` · [github.com/CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)

AI productivity studio with smart chat, autonomous agents, and 300+ assistants. Unified access to multiple AI models — Hermes-compatible.

---

### MervinPraison/PraisonAI
⭐ **8,152** · `Python` · [github.com/MervinPraison/PraisonAI](https://github.com/MervinPraison/PraisonAI)

Hire a 24/7 AI Workforce. Stop writing boilerplate and start shipping autonomous AI teams. Multi-agent orchestration compatible with Hermes.

---

### mnfst/manifest
⭐ **7,008** · `Python` · [github.com/mnfst/manifest](https://github.com/mnfst/manifest)

Connect your agents and harnesses with any provider. Multi-provider agent orchestration layer.

---

### Mintplex-Labs/anything-llm
⭐ **61,663** · `JavaScript` · [github.com/Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)

Stop renting your intelligence. Own it with AnythingLLM. Everything you need for a powerful, private AI workspace. Hermes-compatible via API.

---

### farion1231/cc-switch
⭐ **102,447** · `TypeScript` · [github.com/farion1231/cc-switch](https://github.com/farion1231/cc-switch)

Cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Hermes Agent. Switch between agents seamlessly.

---

### builderz-labs/mission-control
⭐ **3,700+** · [github.com/builderz-labs/mission-control](https://github.com/builderz-labs/mission-control)

Multi-agent fleet management — task dispatch and cost tracking at scale. Hermes-compatible orchestration.

---

### iOfficeAI/AionUi
⭐ **28,359** · `TypeScript` · [github.com/iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)

Free, local, open-source 24/7 Cowork app for OpenClaw, Hermes Agent, Claude Code, Codex, OpenCode, Cursor, and Windsurf.

---

### koozyapno1/alex-ai-empire
⭐ **3** · `Python` · [github.com/koozyapno1/alex-ai-empire](https://github.com/koozyapno1/alex-ai-empire)

AI Empire Builder — 6-Brain Autonomous Agent Architecture. OpenClaw + Hermes multi-brain system.

---

## 🚀 Deployment & Infrastructure

Running Hermes in production — from Docker to Kubernetes.

### 1Panel-dev/1Panel
⭐ **35,898** · `Go` · [github.com/1Panel-dev/1Panel](https://github.com/1Panel-dev/1Panel)

Modern, open-source VPS control panel — the only one with native AI agent management. One-click Hermes deployment.

---

### paperclipinc/hermes-operator
⭐ **13** · `Go` · [github.com/paperclipinc/hermes-operator](https://github.com/paperclipinc/hermes-operator)

Production-grade Kubernetes operator for Hermes Agent — deploy, scale, and manage Hermes agents as K8s resources.

---

### JackTheGit/hermes-autonomous-server
⭐ **14** · `Shell` · [github.com/JackTheGit/hermes-autonomous-server](https://github.com/JackTheGit/hermes-autonomous-server)

Run Hermes Agent autonomously on your Linux server using systemd and nohup. Production-ready systemd service configuration.

---

### TheAiSingularity/hermesclaw
⭐ **53** · `Dockerfile` · [github.com/TheAiSingularity/hermesclaw](https://github.com/TheAiSingularity/hermesclaw)

Hermes Agent sandboxed by NVIDIA OpenShell — hardware-enforced security for autonomous agent deployment.

---

### H-Ali13381/hermes-linux-ricing
⭐ **16** · `Shell` · [github.com/H-Ali13381/hermes-linux-ricing](https://github.com/H-Ali13381/hermes-linux-ricing)

Desktop customization via Hermes — let your agent configure your Linux desktop environment.

---

### anomaliagent007-hue/hermes-mimo-bridge
⭐ **0** · `Python` · [github.com/anomaliagent007-hue/hermes-mimo-bridge](https://github.com/anomaliagent007-hue/hermes-mimo-bridge)

Production bridge between Hermes Agent and Xiaomi MiMo API — long-chain reasoning for IoT device control.

---

### CorpusIQ Multi-Machine Architecture
[Deployment Guide →](/hermes/infrastructure/)

DGX Spark (primary) + Mac Mini M4 (worker) production deployment. SSH orchestration, model routing (65% cost savings), 38-cron reference.

---

### CorpusIQ Production Cron Reference
[38-Cron Architecture →](/hermes/governance/scheduling/)

Complete cron registry with schedule map, delivery targets, and failure patterns. Everything you need for 24/7 autonomous operations.

---

### Container & Docker Deployments
Hermes supports Docker, Singularity, Modal, Daytona, and Vercel Sandbox execution backends. [Official Docker guide →](https://hermes-agent.nousresearch.com/docs/user-guide/docker)

---

### langbot-app/LangBot
⭐ **16,349** · `Python` · [github.com/langbot-app/LangBot](https://github.com/langbot-app/LangBot)

Production-grade platform for building agentic IM bots. Multi-platform intelligent robot development with agent, knowledge base, and plugin system. Hermes-compatible.

---

## 🔒 Security & Governance

Security tools, governance frameworks, and safety systems.

### jnMetaCode/shellward
⭐ **109** · `Python` · [github.com/jnMetaCode/shellward](https://github.com/jnMetaCode/shellward)

AI Agent Security Middleware — 8-layer defense, DLP data flow, prompt injection protection. Hermes-compatible security layer.

---

### CorpusIQ System Registry
[Governance →](/hermes/governance/)

Directory-level validation before any file creation. No duplicates, no orphaned code. 11 governance files tracked.

---

### CorpusIQ Drift Prevention
[Drift Protocol →](/hermes/governance/)

Nightly integrity checks: registry consistency, skill/cron alignment, token health, memory sync. 1 AM daily.

---

### CorpusIQ Email Operations
[Email Ops →](/hermes/governance/email/)

Autonomous inbox management: 4-tier classification, SLA-based response, Gmail API integration. team@ + info@ monitored every 15 minutes.

---

### CorpusIQ Token Lifecycle
[Auth Guide →](/hermes/infrastructure/auth/)

OAuth lifecycle management with refresh automation, expiration monitoring, and alerting. Gmail, GitHub, HeyGen, Postiz tokens.

---

## 🔬 Research & Benchmarks

Academic research, evaluation frameworks, and benchmarking tools.

### agentscope-ai/PawBench
⭐ **59** · `Python` · [github.com/agentscope-ai/PawBench](https://github.com/agentscope-ai/PawBench)

Benchmark for evaluating LLM × harness performance. Measures how well different models perform with different agent frameworks including Hermes.

---

### verkyyi/hermesbench
⭐ **6** · `Python` · [github.com/verkyyi/hermesbench](https://github.com/verkyyi/hermesbench)

Reliability-first benchmark and evaluation harness for Hermes Agent running on local models. Tests tool calling accuracy and agent reliability.

---

### chejinge/agent-product-benchmark-hermes
⭐ **0** · `Python` · [github.com/chejinge/agent-product-benchmark-hermes](https://github.com/chejinge/agent-product-benchmark-hermes)

Multi-dimensional evaluation framework for AI coding agents — Hermes Edition. Evaluates code generation, debugging, and refactoring.

---

### brianyazzz/HermesEval
⭐ **0** · `Python` · [github.com/brianyazzz/HermesEval](https://github.com/brianyazzz/HermesEval)

Continuous evaluation and benchmarking pipeline for Nous Research open-source models on Hermes Agent.

---

### am423/hermesbenchv0_1
⭐ **0** · `Python` · [github.com/am423/hermesbenchv0_1](https://github.com/am423/hermesbenchv0_1)

Hermes Agent benchmark v0.1 — evaluate local models on actual tool-calling performance within Hermes.

---

### CogalNocloz/Hermes_evaluation
⭐ **0** · `Vue` · [github.com/CogalNocloz/Hermes_evaluation](https://github.com/CogalNocloz/Hermes_evaluation)

Benchmark Hermes — Hello World Nuxt 4 style evaluation framework.

---

### Panoramar8046/hermes-agent-metaharness
⭐ **0** · `Python` · [github.com/Panoramar8046/hermes-agent-metaharness](https://github.com/Panoramar8046/hermes-agent-metaharness)

Optimize LLM system quality using an outer-loop meta-harness to auto-tune Hermes agent configurations.

---

### zakahadi/llm-eval-cli
⭐ **0** · `Rust` · [github.com/zakahadi/llm-eval-cli](https://github.com/zakahadi/llm-eval-cli)

CLI developer tool for running custom evaluation suites with OpenAI-compatible endpoints. Hermes-compatible.

---

### soarsmu/HERMES
⭐ **8** · `Python` · [github.com/soarsmu/HERMES](https://github.com/soarsmu/HERMES)

Source code for SANER 2022 research paper "HERMES: Using Commit Message Analysis to Improve Software Evolution". (Note: different project, included for academic reference.)

---

### devghori1264/Hermes_Research_Paper_arxive_preprint
⭐ **0** · [github.com/devghori1264/Hermes_Research_Paper_arxive_preprint](https://github.com/devghori1264/Hermes_Research_Paper_arxive_preprint)

arXiv preprint for Hermes research.

---

### izillionways/academic-research-skills-hermes
⭐ **1** · [github.com/izillionways/academic-research-skills-hermes](https://github.com/izillionways/academic-research-skills-hermes)

Hermes-compatible adaptation of Academic Research Skills for deep research workflows.

---

### easyvibecoding/vibe-sci
⭐ **1** · `Python` · [github.com/easyvibecoding/vibe-sci](https://github.com/easyvibecoding/vibe-sci)

Provider-neutral autonomous ML research paper writer — ideation to LaTeX compilation. Hermes-powered.

---

## 🎬 Content & Media

Video generation, content creation, and media processing with Hermes.

### CorpusIQ HeyGen Video Pipeline
[Video Pipeline →](/hermes/content-ops/video/)

Daily UGC video generation: 10-scenario library, 6-avatar rotation, HeyGen v2 API, FFmpeg post-production, multi-platform distribution via Postiz.

---

### CorpusIQ Social Publishing
[Social Distribution →](/hermes/content-ops/social/)

Cross-platform publishing: X, LinkedIn, TikTok, Instagram, YouTube. Postiz-powered, Mac Mini worker, 3x daily schedule.

---

### Alfo-Tech-Lab/vidilearn
[github.com/Alfo-Tech-Lab/vidilearn](https://github.com/Alfo-Tech-Lab/vidilearn)

Production-grade content extraction agent for YouTube and Web. Hermes-compatible video analysis pipeline.

---

### smfworks/smf-notebooklm-video-pipeline
⭐ **2** · [github.com/smfworks/smf-notebooklm-video-pipeline](https://github.com/smfworks/smf-notebooklm-video-pipeline)

Google NotebookLM to social content pipeline. Create compelling social content from NotebookLM audio overviews. Hermes-integrated.

---

### aiunlocked1412/hermes-agent-pixel
⭐ **14** · `JavaScript` · [github.com/aiunlocked1412/hermes-agent-pixel](https://github.com/aiunlocked1412/hermes-agent-pixel)

Watch your Hermes agent work live as a character in the Pixel Agents online world. Visual representation of agent activity.

---

### CorpusIQ Community Engagement
[Engagement Strategy →](/hermes/content-ops/engagement/)

Help-first community engagement: 6x daily commenting, cross-platform monitoring, operator-first content strategy.

---

## 🌏 Platform-Specific

Chinese, Japanese, Korean, and other language-specific Hermes resources.

### Chinese (中文) Resources

| Resource | Stars | Description |
|----------|-------|-------------|
| [alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book) | 4,443 | Complete tutorial — beginner to expert |
| [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | 15,046 | 216 AI expert roles for Hermes + 17 tools |
| [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | 5,450 | AI coding superpowers, Chinese edition |
| [AlexAnys/awesome-openclaw-usecases-zh](https://github.com/AlexAnys/awesome-openclaw-usecases-zh) | 4,322 | 50 real OpenClaw use cases |
| [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | 2,842 | Multi-engine management panel |
| [longyunfeigu/learn-hermes-agent](https://github.com/longyunfeigu/learn-hermes-agent) | 153 | 27-chapter hands-on tutorial |
| [jefferyjob/awesome-hermes-agent-zh](https://github.com/jefferyjob/awesome-hermes-agent-zh) | 55 | Chinese awesome list |
| [zcweah1981/awesome-hermes-agent-zh](https://github.com/zcweah1981/awesome-hermes-agent-zh) | 25 | Chinese portal + solution packs |
| [xianyu110/awesome-HermesAgent-tutorial](https://github.com/xianyu110/awesome-HermesAgent-tutorial) | 8 | Server deployment tutorial |
| [modoojunko/awesome-novel-skill](https://github.com/modoojunko/awesome-novel-skill) | 242 | Novel writing skill (Chinese) |

---

### Japanese (日本語) Resources

| Resource | Stars | Description |
|----------|-------|-------------|
| [ToseaAI/awesome-html-slide-skills](https://github.com/ToseaAI/awesome-html-slide-skills) | 45 | HTML slide generation skills |

---

## 🎯 Specialized Applications

Domain-specific Hermes Agent applications and integrations.

### Lethe044/hermes-incident-commander
⭐ **42** · `Python` · [github.com/Lethe044/hermes-incident-commander](https://github.com/Lethe044/hermes-incident-commander)

Autonomous SRE agent built on Hermes — detects, heals, and learns from production incidents. Self-improving incident response.

---

### mrbooboo1987-creator/hermes-grok-trading-system
⭐ **0** · `Python` · [github.com/mrbooboo1987-creator/hermes-grok-trading-system](https://github.com/mrbooboo1987-creator/hermes-grok-trading-system)

Autonomous 24/7 AI trading agent powered by Grok 4.20. Hermes-based trading system.

---

### SergeySolovyev/sergei-brand-agent
⭐ **0** · `Python` · [github.com/SergeySolovyev/sergei-brand-agent](https://github.com/SergeySolovyev/sergei-brand-agent)

Autonomous AI agent (Hermes + Triad) promoting commercial brand — content creation, social media, engagement.

---

### Boatsure/PaperDigest
⭐ **0** · [github.com/Boatsure/PaperDigest](https://github.com/Boatsure/PaperDigest)

Hermes Agent Skill for ML researchers — personalized paper reading and digest generation.

---

### colbymchenry/codegraph
⭐ **50,162** · `TypeScript` · [github.com/colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)

Pre-indexed code knowledge graph, auto-syncs on code changes. Works with Claude Code, Codex, Gemini, and Hermes Agent.

---

### adrienbrault/ollama-nous-hermes2pro
⭐ **36** · [github.com/adrienbrault/ollama-nous-hermes2pro](https://github.com/adrienbrault/ollama-nous-hermes2pro)

Ollama models of NousResearch/Hermes-2-Pro-Mistral-7B-GGUF. Run Hermes models locally.

---

### dodo-reach/hermes-link-curator
⭐ **88** · `Python` · [github.com/dodo-reach/hermes-link-curator](https://github.com/dodo-reach/hermes-link-curator)

Hermes profile pack for archiving and browsing curated links + web dashboard. Personal knowledge management.

---

### zszszszsz/.config
⭐ **342** · `Lua` · [github.com/zszszszsz/.config](https://github.com/zszszszsz/.config)

Hermes agent configuration reference — OpenWrt + Hermes integration patterns.

---

## 📊 Ecosystem Stats

| Metric | Value |
|--------|-------|
| Total repos indexed | 121+ |
| Categories | 14 |
| Official Nous Research repos | 4 |
| Community awesome lists | 12 |
| UI/Dashboard projects | 8 |
| Memory systems | 12 |
| MCP integrations | 8 |
| Skill collections | 15+ |
| Research/benchmark projects | 12 |
| Language-specific resources | 12 (10 CN, 1 JP, 1 EN) |
| Total community stars | 600K+ across all indexed repos |

---

## 🔗 Cross-Reference Index

| Topic | Resources |
|-------|-----------|
| **Getting Started** | [Setup Guide](/hermes/setup/) · [Official Docs](https://hermes-agent.nousresearch.com/docs/) · [Orange Book](https://github.com/alchaincyf/hermes-agent-orange-book) · [27-Chapter Tutorial](https://github.com/longyunfeigu/learn-hermes-agent) |
| **Memory** | [Knowledge Architecture](/hermes/knowledge/) · [GBrain](https://github.com/garrytan/gbrain) · [EverOS](https://github.com/EverMind-AI/EverOS) · [claude-mem](https://github.com/thedotmack/claude-mem) · [mnemosyne](https://github.com/AxDSan/mnemosyne) |
| **MCP** | [MCP Guide](/hermes/mcp/) · [CorpusIQ MCP](https://mcp2.corpusiq.io/mcp) · [Kindly Search](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server) · [Kagi MCP](https://github.com/KSroido/Kagi-Session2API-MCP) |
| **Skills** | [Skills Catalog](/hermes/skills/catalog/) · [Marketing Skills](https://github.com/Ben-Home/marketingskills) · [Skill Factory](https://github.com/Romanescu11/hermes-skill-factory) · [372 Skills](https://github.com/BBridgeers/hermes-skills) |
| **UI** | [Hermes WebUI](https://github.com/nesquena/hermes-webui) · [Desktop](https://github.com/fathah/hermes-desktop) · [Studio](https://github.com/EKKOLearnAI/hermes-studio) · [Workspace](https://github.com/outsourc-e/hermes-workspace) · [Scarf](https://github.com/awizemann/scarf) |
| **Production** | [Deployment](/hermes/infrastructure/) · [Crons](/hermes/governance/scheduling/) · [K8s Operator](https://github.com/paperclipinc/hermes-operator) · [Autonomous Server](https://github.com/JackTheGit/hermes-autonomous-server) |
| **Research** | [Self-Evolution](https://github.com/NousResearch/hermes-agent-self-evolution) · [PawBench](https://github.com/agentscope-ai/PawBench) · [HermesBench](https://github.com/verkyyi/hermesbench) |
| **Security** | [Shellward](https://github.com/jnMetaCode/shellward) · [Skillguard](https://github.com/buzzicra/skillguard) · [NemoClaw](https://github.com/NVIDIA/NemoClaw) |

---

## 🤝 Contributing

This directory is maintained by [CorpusIQ](https://corpusiq.io). New resources are discovered continuously by monitoring crons that scan GitHub, MCP directories, and community channels.

**To add a resource:**
1. Fork [CorpusIQ/corpusiq-docs](https://github.com/CorpusIQ/corpusiq-docs)
2. Add your entry to the appropriate category in this file
3. Include: repo URL, description, maintainer, stars, language, key capabilities
4. Submit a PR

**We especially welcome:**
- New community repositories
- Production deployment stories
- Research papers and benchmarks
- MCP server implementations
- Skills and plugins
- Language-specific resources

---

*Last updated: June 16, 2026 · [Star this repo →](https://github.com/CorpusIQ/corpusiq-docs) · Powered by CorpusIQ*
