---
title: Hermes Ecosystem — Complete Resource Directory
description: The definitive directory of Hermes Agent resources — 254+ repos, official docs, community tools, SDKs, integrations, benchmarks, and research. Everything in the Hermes universe.
---

# Hermes Ecosystem — Complete Resource Directory

The most comprehensive directory of Hermes Agent resources in existence. 254 repositories, official documentation, community projects, SDKs, integrations, benchmarks, and research — all organized and cross-referenced.

> **Last updated:** June 16, 2026 · **Repos indexed:** 254 · **Categories:** 18
>
> 👉 **[Submit a repo →](https://github.com/CorpusIQ/corpusiq-docs/issues/new?template=submit-repo.yml)** · Missing something? [Open a PR →](https://github.com/CorpusIQ/corpusiq-docs)

---

## 📑 Quick Navigation

| Category | Count | Jump |
|----------|-------|------|
| [Core & Official](#-core--official) | 5 | [↓](#-core--official) |
| [Documentation & Learning](#-documentation--learning) | 9 | [↓](#-documentation--learning) |
| [Community & Awesome Lists](#-community--awesome-lists) | 12 | [↓](#-community--awesome-lists) |
| [UI & Dashboards](#-ui--dashboards) | 10 | [↓](#-ui--dashboards) |
| [Memory & Knowledge](#-memory--knowledge) | 15 | [↓](#-memory--knowledge) |
| [MCP & Integrations](#-mcp--integrations) | 18 | [↓](#-mcp--integrations) |
| [Skills & Plugins](#-skills--plugins) | 40 | [↓](#-skills--plugins) |
| [Tools & Utilities](#-tools--utilities) | 25 | [↓](#-tools--utilities) |
| [Detection & Media Forensics](#-detection--media-forensics) | 1 | [↓](#-detection--media-forensics) |
| [Orchestration, Multi-Agent & Swarms](#-orchestration-multi-agent--swarms) | 13 | [↓](#-orchestration-multi-agent--swarms) |
| [Deployment & Infrastructure](#-deployment--infrastructure) | 14 | [↓](#-deployment--infrastructure) |
| [Security & Governance](#-security--governance) | 5 | [↓](#-security--governance) |
| [Research & Benchmarks](#-research--benchmarks) | 12 | [↓](#-research--benchmarks) |
| [Content & Media](#-content--media) | 8 | [↓](#-content--media) |
| [Platform-Specific](#-platform-specific) | 10 | [↓](#-platform-specific) |
| [Domain Applications](#-domain-applications) | 15 | [↓](#-domain-applications) |
| [Forks & Derivatives](#-forks--derivatives) | 4 | [↓](#-forks--derivatives) |
| [Guides](#-guides) | 2 | [↓](#-guides) |

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

The most comprehensive Hermes production resource: 36+ pages, 254+ repos indexed, 133+ skills cataloged, 37+ MCP connectors, 38-cron reference architecture, memory stack deep-dives, deployment patterns. Everything the official docs don't cover.

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

### cheats1314/cc-memory-arch
⭐ **1** · [github.com/cheats1314/cc-memory-arch](https://github.com/cheats1314/cc-memory-arch)

Three-tier memory architecture inspired by Hermes Agent — global memory → topic-level memory → project-level memory with hierarchical knowledge organization. Scalable memory design pattern for AI agents handling complex, multi-domain workflows with clear context boundaries and progressive knowledge refinement.

**Status:** Experimental  
**Key capabilities:** Three-tier memory, hierarchical architecture, global-topic-project model, context boundaries, memory design patterns

---

## 🔌 MCP & Integrations

Model Context Protocol servers and integration bridges for Hermes.

### CorpusIQ MCP Server
[CorpusIQ](https://corpusiq.io)

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

### raulvidis/hermes-android
⭐ **community** · `Python` · [github.com/raulvidis/hermes-android](https://github.com/raulvidis/hermes-android)

Android device bridge for Hermes. Control and interact with Android devices from your agent.

**Status:** Beta  
**Key capabilities:** Android integration, device control, mobile bridge

---

### teknium1/hermes-miniverse
⭐ **community** · `Python` · [github.com/teknium1/hermes-miniverse](https://github.com/teknium1/hermes-miniverse)

Miniverse pixel worlds bridge for Hermes. Connect agents to interactive pixel art worlds.

**Status:** Beta  
**Key capabilities:** Miniverse worlds, pixel art, interactive environments

---

### vectorize-io/hindsight
⭐ **community** · `Python` · [github.com/vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)

Long-term memory: retain, recall, reflect. Persistent agent memory with reflection cycles.

**Status:** Production  
**Key capabilities:** Long-term memory, retention, recall, reflection

---

### elkimek/honcho-self-hosted
⭐ **community** · `Python` · [github.com/elkimek/honcho-self-hosted](https://github.com/elkimek/honcho-self-hosted)

Self-hosted Honcho memory integration. Run your own Honcho instance for agent memory.

**Status:** Beta  
**Key capabilities:** Self-hosted Honcho, memory platform, privacy

---

### marlandoj/zouroboros-swarm-executors
⭐ **community** · `Python` · [github.com/marlandoj/zouroboros-swarm-executors](https://github.com/marlandoj/zouroboros-swarm-executors)

Claude Code + Hermes executor bridge. Swarm execution across multiple agent frameworks.

**Status:** Experimental  
**Key capabilities:** Swarm execution, Claude Code bridge, multi-framework

---

### Crustocean/reina
⭐ **community** · `Python` · [github.com/Crustocean/reina](https://github.com/Crustocean/reina)

Autonomous agent for the Crustocean platform. Hermes-powered autonomous operations.

**Status:** Beta  
**Key capabilities:** Crustocean platform, autonomous agent, operations

---

### Rainhoole/hermes-agent-acp-skill
⭐ **community** · `Python` · [github.com/Rainhoole/hermes-agent-acp-skill](https://github.com/Rainhoole/hermes-agent-acp-skill)

Multi-agent delegation via ACP (Hermes/Codex/Claude Code). Agent Communication Protocol skill for cross-agent tasks.

**Status:** Beta  
**Key capabilities:** ACP delegation, multi-agent, cross-framework communication

---

### gizdusum/hermes-blockchain-oracle
⭐ **community** · `Python` · [github.com/gizdusum/hermes-blockchain-oracle](https://github.com/gizdusum/hermes-blockchain-oracle)

Solana blockchain MCP server for Hermes. Real-time blockchain data and transaction capabilities.

**Status:** Experimental  
**Key capabilities:** Solana blockchain, MCP server, on-chain data

---

### Ridwannurudeen/hermes-council
⭐ **community** · `Python` · [github.com/Ridwannurudeen/hermes-council](https://github.com/Ridwannurudeen/hermes-council)

Adversarial multi-perspective council for Hermes. Multiple agents debate and critique for better decisions.

**Status:** Experimental  
**Key capabilities:** Adversarial council, multi-perspective, debate framework

---

### unitedideas/nothumansearch-mcp
⭐ **community** · `Python` · [github.com/unitedideas/nothumansearch-mcp](https://github.com/unitedideas/nothumansearch-mcp)

MCP server discovery across 8,600+ sites. Find and connect to MCP servers at scale.

**Status:** Production  
**Key capabilities:** MCP discovery, 8,600+ sites, server search

---

### Hmbown/NemoHermes
⭐ **community** · `Python` · [github.com/Hmbown/NemoHermes](https://github.com/Hmbown/NemoHermes)

NVIDIA capability registry and routing for Hermes. Hardware-accelerated agent capabilities via NVIDIA.

**Status:** Experimental  
**Key capabilities:** NVIDIA integration, capability registry, hardware routing

---

### Andrew-Girgis/microsoft-workspace-skill
⭐ **community** · `Python` · [github.com/Andrew-Girgis/microsoft-workspace-skill](https://github.com/Andrew-Girgis/microsoft-workspace-skill)

Outlook and Microsoft 365 Graph API integration. Office productivity tools from Hermes.

**Status:** Beta  
**Key capabilities:** Outlook integration, Microsoft 365, Graph API

---

### aivanelabs/agent-android
⭐ **community** · `Python` · [github.com/aivanelabs/agent-android](https://github.com/aivanelabs/agent-android)

LAN-first Android control without USB/ADB. Wireless Android device management for Hermes.

**Status:** Beta  
**Key capabilities:** Android control, LAN-first, wireless, no ADB

---

### mrpeter2025/clawsocial-hermes-plugin
⭐ **community** · `Python` · [github.com/mrpeter2025/clawsocial-hermes-plugin](https://github.com/mrpeter2025/clawsocial-hermes-plugin)

Social discovery and WebSocket messaging plugin. Agent-to-agent social networking.

**Status:** Beta  
**Key capabilities:** Social discovery, WebSocket messaging, agent networking

---

### Swih/mistral-mcp
⭐ **community** · `Python` · [github.com/Swih/mistral-mcp](https://github.com/Swih/mistral-mcp)

Full Mistral AI MCP integration: chat, vision, OCR, audio. Complete Mistral platform access.

**Status:** Beta  
**Key capabilities:** Mistral AI, chat, vision, OCR, audio

---

### jau123/MeiGen-AI-Design-MCP
⭐ **1,000+** · `Python` · [github.com/jau123/MeiGen-AI-Design-MCP](https://github.com/jau123/MeiGen-AI-Design-MCP)

9 AI image/video generation models via MCP. Multi-model creative content generation.

**Status:** Production  
**Key capabilities:** Image generation, video generation, 9 AI models, MCP

---

### PipRail
⭐ **community** · `TypeScript` · [github.com/piprail/piprail](https://github.com/piprail/piprail)

Open, self-custody x402 payment rail for AI agents — an SDK plus an MCP server that hands any MCP client a budget-bound wallet. 29 chains across 10 families (EVM, Solana, TON, Tron, NEAR, Sui, Aptos, Algorand, Stellar, XRPL). No backend, no custody, no protocol fee.

**Status:** Production  
**Key capabilities:** x402 payments, 29 chains, MCP server, budget-bound agent wallet, self-custody, no fee

---

### thebrierfox/the-stall
⭐ **community** · `Python` · [github.com/thebrierfox/the-stall](https://github.com/thebrierfox/the-stall)

209 pay-per-call data capabilities via x402 MCP. Monetized data access for autonomous agents.

**Status:** Production  
**Key capabilities:** Pay-per-call, 209 capabilities, x402 MCP, data monetization

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

### Community Skills

### 42-evey/hermes-plugins
⭐ **community** · `Python` · [github.com/42-evey/hermes-plugins](https://github.com/42-evey/hermes-plugins)

Goal management, inter-agent bridge, model selection, and cost control. Modular plugin architecture for extending Hermes capabilities.

**Status:** Beta  
**Key capabilities:** Goal management, inter-agent bridge, model selection, cost control

---

### Romanescu11/hermes-skill-factory
⭐ **381** · `Python` · [github.com/Romanescu11/hermes-skill-factory](https://github.com/Romanescu11/hermes-skill-factory)

A meta-skill plugin for Hermes AI agent that watches your workflow and auto-creates skills from repeated patterns.

**Status:** Beta  
**Key capabilities:** Auto-skill generation, workflow pattern detection, meta-skill architecture

---

### Hmbown/Wizards-of-the-Ghosts
⭐ **community** · `Python` · [github.com/Hmbown/Wizards-of-the-Ghosts](https://github.com/Hmbown/Wizards-of-the-Ghosts)

Fantasy spell-themed skill pack wrapping dev operations. Cast spells to deploy, monitor, and manage infrastructure.

**Status:** Experimental  
**Key capabilities:** DevOps operations, spell-themed interface, infrastructure management

---

### Cranot/super-hermes
⭐ **community** · `Python` · [github.com/Cranot/super-hermes](https://github.com/Cranot/super-hermes)

Teaches Hermes to write better analytical prompts. Improves reasoning depth and analytical quality through prompt engineering.

**Status:** Experimental  
**Key capabilities:** Analytical prompt optimization, reasoning improvement, prompt engineering

---

### Lethe044/hermes-life-os
⭐ **community** · `Python` · [github.com/Lethe044/hermes-life-os](https://github.com/Lethe044/hermes-life-os)

Personal OS agent detecting daily patterns. Learns routines and proactively manages personal productivity.

**Status:** Experimental  
**Key capabilities:** Pattern detection, personal productivity, routine learning

---

### Yonkoo11/hermes-dojo
⭐ **community** · `Python` · [github.com/Yonkoo11/hermes-dojo](https://github.com/Yonkoo11/hermes-dojo)

Self-improvement monitoring agent performance. Tracks and optimizes Hermes agent behavior over time.

**Status:** Beta  
**Key capabilities:** Performance monitoring, self-improvement tracking, agent optimization

---

### Alexeyisme/hermes-spotify-skill
⭐ **community** · `Python` · [github.com/Alexeyisme/hermes-spotify-skill](https://github.com/Alexeyisme/hermes-spotify-skill)

Spotify control for headless Linux. Control music playback from Hermes on servers without desktop environments.

**Status:** Beta  
**Key capabilities:** Spotify API, headless Linux, music control

---

### Lethe044/hermes-skill-marketplace
⭐ **community** · `Python` · [github.com/Lethe044/hermes-skill-marketplace](https://github.com/Lethe044/hermes-skill-marketplace)

An agent that writes, tests, and publishes skills autonomously. Self-sustaining skill ecosystem generator.

**Key capabilities:** Autonomous skill creation, testing, publishing, marketplace ecosystem

---

### beiyuii/personal-api-skill
⭐ **community** · `Python` · [github.com/beiyuii/personal-api-skill](https://github.com/beiyuii/personal-api-skill)

Turns Obsidian vault into an identity layer for agents. Personal knowledge graph as agent context.

**Key capabilities:** Obsidian integration, identity layer, personal knowledge graph

---

### markoblogo/abvx-agent-skills
⭐ **community** · `Python` · [github.com/markoblogo/abvx-agent-skills](https://github.com/markoblogo/abvx-agent-skills)

Auditable cross-platform coding-agent skillpack. Production-grade coding skills with full audit trails.

**Status:** Production  
**Key capabilities:** Cross-platform coding, audit trails, production-grade

---

### adnw-vinc/hermes-nextcloud
⭐ **community** · `Python` · [github.com/adnw-vinc/hermes-nextcloud](https://github.com/adnw-vinc/hermes-nextcloud)

Self-hosted Nextcloud bridge for Hermes. Access files, calendars, and contacts from your own cloud.

**Status:** Beta  
**Key capabilities:** Nextcloud integration, self-hosted, file/calendar/contact access

---

### witt3rd/oh-my-hermes
⭐ **community** · `Python` · [github.com/witt3rd/oh-my-hermes](https://github.com/witt3rd/oh-my-hermes)

Multi-agent orchestration skills for Hermes. Coordinate multiple agents working together on complex tasks.

**Status:** Beta  
**Key capabilities:** Multi-agent orchestration, task coordination, team workflows

---

### Infrasity-Labs/dev-gtm-claude-skills
⭐ **community** · `Python` · [github.com/Infrasity-Labs/dev-gtm-claude-skills](https://github.com/Infrasity-Labs/dev-gtm-claude-skills)

SEO, GEO, and AI discoverability skills. Optimize content for AI-powered search and generative engines.

**Status:** Production  
**Key capabilities:** SEO optimization, GEO strategy, AI discoverability

---

### voidborne-d/master-skill
⭐ **community** · `Python` · [github.com/voidborne-d/master-skill](https://github.com/voidborne-d/master-skill)

Distills entire industries into portable skill folders. Domain expertise packaged as installable Hermes skills.

**Status:** Beta  
**Key capabilities:** Industry distillation, portable skills, domain expertise

---

### Sequenzy/sequenzy-email-marketing
⭐ **community** · `Python` · [github.com/Sequenzy/sequenzy-email-marketing](https://github.com/Sequenzy/sequenzy-email-marketing)

Lifecycle email marketing skill for Hermes. Automated email sequences for customer journeys.

**Status:** Beta  
**Key capabilities:** Email marketing, lifecycle automation, customer journeys

---

### longbridge/skills
⭐ **community** · `Python` · [github.com/longbridge/skills](https://github.com/longbridge/skills)

13 securities trading skills for HK, US, and A-share markets. Financial market data and trading workflows.

**Status:** Production  
**Key capabilities:** Securities trading, HK/US/A-share markets, financial data

---

### remoet-labs/agent-skills
⭐ **community** · `Python` · [github.com/remoet-labs/agent-skills](https://github.com/remoet-labs/agent-skills)

Job-search and career-discovery skill. Automated job hunting, resume optimization, and career pathfinding.

**Status:** Production  
**Key capabilities:** Job search, career discovery, resume optimization

---

### svenmedina07-ship-it/acca-tracker
⭐ **community** · `Python` · [github.com/svenmedina07-ship-it/acca-tracker](https://github.com/svenmedina07-ship-it/acca-tracker)

Multi-sport accumulator bet tracker. Track and analyze accumulator bets across multiple sports.

**Status:** Beta  
**Key capabilities:** Sports betting, accumulator tracking, multi-sport

---

### Agentskills.io Ecosystem

### ZeroPointRepo/youtube-skills
⭐ **community** · `Python` · [github.com/ZeroPointRepo/youtube-skills](https://github.com/ZeroPointRepo/youtube-skills)

YouTube search, channel lookup, and transcript retrieval via TranscriptAPI. Production-ready YouTube integration.

**Status:** Production  
**Key capabilities:** YouTube search, channel lookup, transcript retrieval

---

### mukul975/Anthropic-Cybersecurity-Skills
⭐ **4,000+** · `Python` · [github.com/mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)

753+ cybersecurity skills mapped to MITRE ATT&CK framework. Comprehensive security testing and analysis toolkit.

**Status:** Production  
**Key capabilities:** Cybersecurity testing, MITRE ATT&CK, 753+ skills, security analysis

---

### smartcontractkit/chainlink-agent-skills
⭐ **community** · `Python` · [github.com/smartcontractkit/chainlink-agent-skills](https://github.com/smartcontractkit/chainlink-agent-skills)

Official Chainlink oracle skills for agents. Blockchain data feeds and smart contract interaction.

**Status:** Production  
**Key capabilities:** Chainlink oracles, blockchain data, smart contracts

---

### black-forest-labs/skills
⭐ **community** · `Python` · [github.com/black-forest-labs/skills](https://github.com/black-forest-labs/skills)

Official FLUX image generation skills. State-of-the-art image generation directly from Hermes.

**Status:** Production  
**Key capabilities:** FLUX image generation, AI art, visual content creation

---

### DougTrajano/pydantic-ai-skills
⭐ **community** · `Python` · [github.com/DougTrajano/pydantic-ai-skills](https://github.com/DougTrajano/pydantic-ai-skills)

Pydantic AI integration with type-safe schema validation. Structured, validated agent outputs.

**Status:** Production  
**Key capabilities:** Type-safe AI, schema validation, Pydantic integration

---

### Yarmoluk/cognify-skills
⭐ **community** · `Python` · [github.com/Yarmoluk/cognify-skills](https://github.com/Yarmoluk/cognify-skills)

19 business ops skills: CRM, invoicing, project management. Turnkey business operations toolkit.

**Status:** Beta  
**Key capabilities:** Business operations, CRM, invoicing, project management

---

### tiann/execplan-skill
⭐ **community** · `Python` · [github.com/tiann/execplan-skill](https://github.com/tiann/execplan-skill)

Long-running task lifecycle management. Plan, track, and manage tasks that span hours or days.

**Status:** Beta  
**Key capabilities:** Task lifecycle, long-running execution, plan management

---

### ReinaMacCredy/maestro
⭐ **community** · `Python` · [github.com/ReinaMacCredy/maestro](https://github.com/ReinaMacCredy/maestro)

Skill orchestration with Conductor planning. Compose multiple skills into complex workflows.

**Status:** Beta  
**Key capabilities:** Skill orchestration, Conductor planning, workflow composition

---

### armelhbobdad/bmad-module-skill-forge
⭐ **community** · `Python` · [github.com/armelhbobdad/bmad-module-skill-forge](https://github.com/armelhbobdad/bmad-module-skill-forge)

Converts entire repositories into installable Hermes skills. Automated skill packaging from existing codebases.

**Status:** Beta  
**Key capabilities:** Repo-to-skill conversion, automated packaging, skill forge

---

### cablate/Agentic-MCP-Skill
⭐ **community** · `Python` · [github.com/cablate/Agentic-MCP-Skill](https://github.com/cablate/Agentic-MCP-Skill)

MCP client with agentskills.io validation. Validated, secure MCP integration for Hermes.

**Status:** Beta  
**Key capabilities:** MCP client, skill validation, agentskills.io integration

---

### KYC-rip/ripley-xmr-gateway
⭐ **community** · `Python` · [github.com/KYC-rip/ripley-xmr-gateway](https://github.com/KYC-rip/ripley-xmr-gateway)

Monero blockchain gateway for agents. Privacy-preserving cryptocurrency operations.

**Status:** Experimental  
**Key capabilities:** Monero gateway, privacy, cryptocurrency

---

### PederHP/skillsdotnet
⭐ **community** · `C#` · [github.com/PederHP/skillsdotnet](https://github.com/PederHP/skillsdotnet)

C# agentskills.io with MCP integration. .NET ecosystem skill development for Hermes.

**Status:** Beta  
**Key capabilities:** C# skills, .NET integration, MCP support

---

### TheColonyCC/colony-skill
⭐ **community** · `Python` · [github.com/TheColonyCC/colony-skill](https://github.com/TheColonyCC/colony-skill)

Collaborative intelligence platform skill. Multi-user agent collaboration and knowledge sharing.

**Status:** Beta  
**Key capabilities:** Collaborative intelligence, multi-user, knowledge sharing

---

### Merit-Systems/agentcash-skills
⭐ **community** · `Python` · [github.com/Merit-Systems/agentcash-skills](https://github.com/Merit-Systems/agentcash-skills)

300+ premium APIs via a single skill. Unified API gateway for Hermes with extensive coverage.

**Status:** Beta  
**Key capabilities:** 300+ APIs, unified gateway, premium API access

---

### Xquik-dev/x-twitter-scraper
⭐ **community** · `Python` · [github.com/Xquik-dev/x-twitter-scraper](https://github.com/Xquik-dev/x-twitter-scraper)

Typed X/Twitter access with 43 SKILL.md folders. Structured Twitter data extraction and analysis.

**Status:** Beta  
**Key capabilities:** Twitter/X data, typed access, 43 skill folders

---

### Agents365-ai/drawio-skill
⭐ **1,100+** · `Python` · [github.com/Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill)

Generates draw.io diagrams from natural language. Visual documentation and diagramming from descriptions.

**Status:** Production  
**Key capabilities:** draw.io diagrams, natural language to diagram, visual documentation

---

### Community Plugins

### plur-ai/plur
⭐ **community** · `Python` · [github.com/plur-ai/plur](https://github.com/plur-ai/plur)

Shared memory layer with open engram format (YAML). Cross-agent memory compatibility standard.

**Status:** Beta  
**Key capabilities:** Shared memory, engram format, YAML, cross-agent memory

---

### nativ3ai/hermes-payguard
⭐ **community** · `Python` · [github.com/nativ3ai/hermes-payguard](https://github.com/nativ3ai/hermes-payguard)

Safe USDC/x402 payment plugin for Hermes. Secure micropayment handling for agent transactions.

**Status:** Experimental  
**Key capabilities:** USDC payments, x402 protocol, payment security

---

### robbyczgw-cla/hermes-web-search-plus
⭐ **community** · `Python` · [github.com/robbyczgw-cla/hermes-web-search-plus](https://github.com/robbyczgw-cla/hermes-web-search-plus)

Multi-provider web search routing. Intelligently routes search queries across multiple search engines.

**Status:** Beta  
**Key capabilities:** Multi-provider search, intelligent routing, web search

---

### FahrenheitResearch/hermes-weather-plugin
⭐ **community** · `Python` · [github.com/FahrenheitResearch/hermes-weather-plugin](https://github.com/FahrenheitResearch/hermes-weather-plugin)

Professional NWS/NEXRAD weather data plugin. Real-time weather radar and forecasts for Hermes.

**Status:** Beta  
**Key capabilities:** NWS weather, NEXRAD radar, professional forecasting

---

### FahrenheitResearch/hermes-wxtrain-plugin
⭐ **community** · `Python` · [github.com/FahrenheitResearch/hermes-wxtrain-plugin](https://github.com/FahrenheitResearch/hermes-wxtrain-plugin)

ML weather training datasets. Training data pipeline for meteorological machine learning models.

**Status:** Experimental  
**Key capabilities:** Weather ML, training datasets, meteorological data

---

### anpicasso/hermes-plugin-chrome-profiles
⭐ **community** · `Python` · [github.com/anpicasso/hermes-plugin-chrome-profiles](https://github.com/anpicasso/hermes-plugin-chrome-profiles)

Switch Chrome profiles via Chrome DevTools Protocol. Manage multiple browser identities from Hermes.

**Status:** Experimental  
**Key capabilities:** Chrome profiles, CDP, browser identity management

---

### raulvidis/hermes-cloudflare
⭐ **community** · `Python` · [github.com/raulvidis/hermes-cloudflare](https://github.com/raulvidis/hermes-cloudflare)

Cloudflare browser rendering for Hermes. Headless browsing via Cloudflare's network.

**Status:** Experimental  
**Key capabilities:** Cloudflare rendering, headless browsing, network browsing

---

### 42-evey/evey-bridge-plugin
⭐ **community** · `Python` · [github.com/42-evey/evey-bridge-plugin](https://github.com/42-evey/evey-bridge-plugin)

Claude Code ↔ Hermes bidirectional bridge. Seamless handoff between Claude Code and Hermes workflows.

**Status:** Beta  
**Key capabilities:** Claude Code bridge, bidirectional, workflow handoff

---

### Agent-Analytics/agent-analytics-hermes-plugin
⭐ **community** · `Python` · [github.com/Agent-Analytics/agent-analytics-hermes-plugin](https://github.com/Agent-Analytics/agent-analytics-hermes-plugin)

Signals dashboard tab for Hermes. Real-time analytics and performance metrics visualization.

**Status:** Beta  
**Key capabilities:** Analytics dashboard, signals visualization, performance metrics

---

### Xquik-dev/hermes-tweet
⭐ **community** · `Python` · [github.com/Xquik-dev/hermes-tweet](https://github.com/Xquik-dev/hermes-tweet)

Native X/Twitter plugin for Hermes. Post, read, and interact with Twitter directly from Hermes.

**Status:** Beta  
**Key capabilities:** Twitter integration, native X client, social posting

---

### pingchesu/hermes-curator-evolver
⭐ **community** · `Python` · [github.com/pingchesu/hermes-curator-evolver](https://github.com/pingchesu/hermes-curator-evolver)

Evidence-driven Curator companion for Hermes. Evolves curation strategies based on engagement data.

**Status:** Beta  
**Key capabilities:** Content curation, evidence-driven, engagement optimization

---

### lingjiuu/hermes-dynamic-workflows
⭐ **community** · `Python` · [github.com/lingjiuu/hermes-dynamic-workflows](https://github.com/lingjiuu/hermes-dynamic-workflows)

Dynamic workflows with up to 1,000 subagents. Massively parallel agent execution framework.

**Status:** Beta  
**Key capabilities:** Dynamic workflows, 1000 subagents, parallel execution

---

### ogallotti/rtk-hermes
⭐ **community** · `Python` · [github.com/ogallotti/rtk-hermes](https://github.com/ogallotti/rtk-hermes)

Compresses terminal output by 60-90% token reduction. Dramatically reduces token consumption for terminal operations.

**Status:** Beta  
**Key capabilities:** Terminal compression, token reduction, 60-90% savings

---

### redoracle/hermes-ops-kit
⭐ **community** · `Python` · [github.com/redoracle/hermes-ops-kit](https://github.com/redoracle/hermes-ops-kit)

Operations and security toolkit: routing, secrets management, auditing, cost governance.

**Status:** Beta  
**Key capabilities:** Ops security, secret management, auditing, cost governance

---

### scross01/hermes-custom-dangerous-patterns
⭐ **community** · `Python` · [github.com/scross01/hermes-custom-dangerous-patterns](https://github.com/scross01/hermes-custom-dangerous-patterns)

Custom terminal command approval patterns. Fine-grained control over dangerous command execution.

**Status:** Beta  
**Key capabilities:** Terminal safety, custom patterns, command approval

---

### eleion-ai/mnemo-hermes
⭐ **community** · `Python` · [github.com/eleion-ai/mnemo-hermes](https://github.com/eleion-ai/mnemo-hermes)

pgvector semantic memory plugin for Hermes. PostgreSQL-backed vector memory for persistent agent knowledge.

**Status:** Beta  
**Key capabilities:** pgvector memory, semantic search, PostgreSQL backend

---

### ewkeee/hermes-social-skills
⭐ **0** · `Python` · [github.com/ewkeee/hermes-social-skills](https://github.com/ewkeee/hermes-social-skills)

Chinese social media content automation skillpack for Hermes Agent — voice modeling, AI-powered ideation, automated writing, and cross-platform social posting. Streamline your Xiaohongshu, Weibo, and Douyin content workflow with agent-driven content creation.

**Status:** Beta  
**Key capabilities:** Social media automation, Chinese platforms, voice cloning, AI content writing, multi-platform posting

---

### baipai012-lang/xhs-hot-topic-to-post
⭐ **0** · `Python` · [github.com/baipai012-lang/xhs-hot-topic-to-post](https://github.com/baipai012-lang/xhs-hot-topic-to-post)

End-to-end Xiaohongshu (RED) hot topic content pipeline — tracks trending topics on Xiaohongshu in real-time, generates AI-powered content drafts, and publishes directly to the platform. Closing the loop from trend discovery to content publishing for Hermes-powered social media automation.

**Status:** Beta  
**Key capabilities:** Xiaohongshu trending, hot topic tracking, AI content generation, social publishing pipeline, RED platform

---

### charlieaiworker/telegram-topic-setup-skill
⭐ **0** · `Python` · [github.com/charlieaiworker/telegram-topic-setup-skill](https://github.com/charlieaiworker/telegram-topic-setup-skill)

Telegram forum topic bootstrap skill for Hermes Agent — automatically initializes workspace memory files and project folder structures when a new Telegram forum topic is created. Keeps agent context organized per-topic with zero manual setup, ideal for topic-based agent workspaces.

**Status:** Beta  
**Key capabilities:** Telegram topics, workspace initialization, memory bootstrapping, project scaffolding, topic organization

---

### lijeuki/Hermes-Lark-Topic-Manager
⭐ **0** · `Python` · [github.com/lijeuki/Hermes-Lark-Topic-Manager](https://github.com/lijeuki/Hermes-Lark-Topic-Manager)

Feishu/Lark group chat management skill for Hermes Agent — threaded discussion tracking, message organization, and group chat management. Bring Hermes-powered AI intelligence to your Feishu team collaboration spaces with automated topic threading.

**Status:** Beta  
**Key capabilities:** Feishu integration, Lark platform, group chat management, threaded discussions, team collaboration

---

### huxiaoqiao/flint-hot-topic-tracker-skill
⭐ **0** · `Python` · [github.com/huxiaoqiao/flint-hot-topic-tracker-skill](https://github.com/huxiaoqiao/flint-hot-topic-tracker-skill)

Weibo trending and Toutiao headline tracker skill for Hermes Agent — monitors Weibo hot search rankings, Toutiao top stories, and Baidu index rising topics in real-time. Social media trend intelligence for content creators, marketers, and brand strategists.

**Status:** Beta  
**Key capabilities:** Weibo trending, Toutiao headlines, Baidu index, hot topic monitoring, Chinese social trends

---

### huxiaoqiao/dusk-hot-topic-tracker-skill
⭐ **0** · `Python` · [github.com/huxiaoqiao/dusk-hot-topic-tracker-skill](https://github.com/huxiaoqiao/dusk-hot-topic-tracker-skill)

Multi-platform hot topic tracker skill for Hermes Agent — aggregates trending content from multiple Chinese social platforms into a unified trend dashboard. Discover what's hot across platforms before it peaks, enabling timely content creation.

**Status:** Beta  
**Key capabilities:** Multi-platform tracking, hot topic aggregation, trend discovery, cross-platform monitoring, content timing

---

### huxiaoqiao/cove-hot-topic-tracker-skill
⭐ **0** · `Python` · [github.com/huxiaoqiao/cove-hot-topic-tracker-skill](https://github.com/huxiaoqiao/cove-hot-topic-tracker-skill)

Multi-platform hot topic tracking and content intelligence skill for Hermes Agent — continuous monitoring of trending topics across social media platforms with AI-powered trend analysis and content opportunity scoring. Stay ahead of viral trends across multiple Chinese platforms.

**Status:** Beta  
**Key capabilities:** Hot topic tracking, trend intelligence, content opportunity scoring, multi-platform monitoring, viral trend detection

---

### Atemndobs/hermes-plugins-hub
⭐ **1** · [github.com/Atemndobs/hermes-plugins-hub](https://github.com/Atemndobs/hermes-plugins-hub)

Community directory for Hermes Agent plugins — auto-indexed from GitHub topic tags for seamless plugin discovery. Search, browse, and discover community-built Hermes Agent extensions, skills, and integrations in one centralized, searchable hub.

**Status:** Beta  
**Key capabilities:** Plugin discovery, community directory, GitHub-indexed, plugin search, extension catalog

---

## 🛠 Tools & Utilities

Development tools, utilities, and platforms for the Hermes ecosystem.

### dodo-reach/hermes-desktop
⭐ **community** · `Swift` · [github.com/dodo-reach/hermes-desktop](https://github.com/dodo-reach/hermes-desktop)

Native macOS workspace for Hermes with SSH-based connectivity. Desktop-native agent interaction.

**Status:** Beta  
**Key capabilities:** macOS native, SSH connectivity, desktop workspace

---

### Tranquil-Flow/hermes-neurovision
⭐ **community** · `Python` · [github.com/Tranquil-Flow/hermes-neurovision](https://github.com/Tranquil-Flow/hermes-neurovision)

Terminal neurovisualizer with 42 themes. Visualize agent thought processes in the terminal.

**Status:** Experimental  
**Key capabilities:** Neurovisualization, 42 themes, terminal visualization

---

### roli-lpci/lintlang
⭐ **community** · `Python` · [github.com/roli-lpci/lintlang](https://github.com/roli-lpci/lintlang)

Static linter for agent configs and prompts. Validate agent configurations before deployment.

**Status:** Beta  
**Key capabilities:** Config linting, prompt validation, static analysis

---

### 0xrsydn/nix-hermes-agent
⭐ **community** · `Nix` · [github.com/0xrsydn/nix-hermes-agent](https://github.com/0xrsydn/nix-hermes-agent)

Nix package and NixOS module for Hermes. Reproducible, declarative Hermes deployment.

**Status:** Beta  
**Key capabilities:** Nix packaging, NixOS module, reproducible builds

---

### 0xNyk/openclaw-to-hermes
⭐ **community** · `Python` · [github.com/0xNyk/openclaw-to-hermes](https://github.com/0xNyk/openclaw-to-hermes)

OpenClaw to Hermes migration tool. Automated migration from OpenClaw to Hermes Agent.

**Status:** Beta  
**Key capabilities:** OpenClaw migration, automated conversion, transition tool

---

### unmodeled-tyler/vessel-browser
⭐ **community** · `Python` · [github.com/unmodeled-tyler/vessel-browser](https://github.com/unmodeled-tyler/vessel-browser)

AI-native Linux browser with MCP support. Browser built for agent interaction.

**Status:** Experimental  
**Key capabilities:** AI-native browser, Linux, MCP integration

---

### jo-inc/camofox-browser
⭐ **4,000+** · `Python` · [github.com/jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser)

Stealth headless browser for agents. Undetectable browsing with fingerprint randomization.

**Status:** Production  
**Key capabilities:** Stealth browsing, headless, fingerprint randomization

---

### rookiemann/portable-hermes-agent
⭐ **community** · `C#` · [github.com/rookiemann/portable-hermes-agent](https://github.com/rookiemann/portable-hermes-agent)

Windows desktop app with 100+ integrated tools. All-in-one portable Hermes for Windows.

**Status:** Beta  
**Key capabilities:** Windows desktop, 100+ tools, portable

---

### pyrate-llama/hermes-ui
⭐ **community** · `TypeScript` · [github.com/pyrate-llama/hermes-ui](https://github.com/pyrate-llama/hermes-ui)

Glassmorphic web UI with SSE streaming. Modern, beautiful web interface for Hermes.

**Status:** Beta  
**Key capabilities:** Glassmorphic UI, SSE streaming, web interface

---

### sanchomuzax/hermes-webui
⭐ **community** · `TypeScript` · [github.com/sanchomuzax/hermes-webui](https://github.com/sanchomuzax/hermes-webui)

Lightweight monitoring dashboard for Hermes. Minimal resource usage, maximum visibility.

**Status:** Beta  
**Key capabilities:** Monitoring dashboard, lightweight, web interface

---

### AMAP-ML/SkillClaw
⭐ **705** · `Python` · [github.com/AMAP-ML/SkillClaw](https://github.com/AMAP-ML/SkillClaw)

Auto-evolves skill library from session data. Skills that improve automatically through usage.

**Status:** Production  
**Key capabilities:** Auto-evolution, skill library, session-driven learning

---

### clarvia-project/scanner
⭐ **community** · `Python` · [github.com/clarvia-project/scanner](https://github.com/clarvia-project/scanner)

AEO scoring for MCP tools across 15,400+ servers. Agent Engine Optimization scoring.

**Status:** Production  
**Key capabilities:** AEO scoring, MCP analysis, 15,400+ servers

---

### luoyuctl/agenttrace
⭐ **community** · `Python` · [github.com/luoyuctl/agenttrace](https://github.com/luoyuctl/agenttrace)

Local TUI/CLI session auditor for Hermes. Trace and audit agent sessions from the terminal.

**Status:** Beta  
**Key capabilities:** Session auditing, TUI/CLI, agent tracing

---

### amanning3390/hermeshub
⭐ **community** · `Python` · [github.com/amanning3390/hermeshub](https://github.com/amanning3390/hermeshub)

Community skill hub for Hermes Agent. Discover, share, and install community skills.

**Status:** Beta  
**Key capabilities:** Skill hub, community sharing, skill discovery

---

### chigwell/skilldock.io
⭐ **community** · `TypeScript` · [github.com/chigwell/skilldock.io](https://github.com/chigwell/skilldock.io)

Cross-platform skills marketplace. Buy, sell, and share agent skills across frameworks.

**Status:** Production  
**Key capabilities:** Skills marketplace, cross-platform, skill economy

---

### pumanitro/Global Chat
⭐ **community** · `Python` · [github.com/pumanitro/Global-Chat](https://github.com/pumanitro/Global-Chat)

Cross-protocol agent discovery across 18K+ servers. Universal agent discovery network.

**Status:** Production  
**Key capabilities:** Agent discovery, 18K+ servers, cross-protocol

---

### amanning3390/flowstate-qmd
⭐ **community** · `Python` · [github.com/amanning3390/flowstate-qmd](https://github.com/amanning3390/flowstate-qmd)

Anticipatory memory with RAG. Predicts what the agent will need before it asks.

**Status:** Beta  
**Key capabilities:** Anticipatory memory, RAG, predictive retrieval

---

### AxDSan/Mnemosyne
⭐ **1,150** · `Python` · [github.com/AxDSan/Mnemosyne](https://github.com/AxDSan/Mnemosyne)

Local sub-millisecond memory system with sqlite-vec hybrid. Ultra-fast local vector memory.

**Status:** Beta  
**Key capabilities:** Sub-ms retrieval, sqlite-vec, hybrid memory, local-first

---

### zzet/gortex
⭐ **344** · `Go` · [github.com/zzet/gortex](https://github.com/zzet/gortex)

Code graph and intelligence engine that cuts AI coding agent token usage up to 50×. Indexes 257 languages across multiple repos, exposes via CLI, MCP server, and web UI. Native Hermes integration with 20 built-in skills. Sub-millisecond impact analysis, cross-repo call chains, zero external dependencies — single Go binary.

**Status:** Production  
**Key capabilities:** Token optimization (50×), 257 languages, MCP server, Hermes native, cross-repo graph

---

### ivan-szz/hermes-newsletter-script
⭐ **1** · `Rust` · [github.com/ivan-szz/hermes-newsletter-script](https://github.com/ivan-szz/hermes-newsletter-script)

Zero-config Rust CLI for aggregating tech news from 11 sources with intelligent topic filtering — Hacker News, Reddit, Dev.to, Lobsters, and more. Compiles AI-curated newsletters with topic-aware article selection and formatting, ready for Hermes Agent integration into daily content workflows.

**Status:** Beta  
**Key capabilities:** Tech news aggregation, 11 sources, Rust CLI, topic filtering, AI newsletter generation

---

### thiswind/hermes-cursor-compressor
⭐ **1** · `Python` · [github.com/thiswind/hermes-cursor-compressor](https://github.com/thiswind/hermes-cursor-compressor)

Cursor-style context compression for Hermes Agent — fixes topic drift with minimal summarization that preserves semantic coherence. Intelligently compresses conversation context to reduce token consumption while maintaining task-relevant focus across long-running agent sessions and multi-topic conversations.

**Status:** Beta  
**Key capabilities:** Context compression, topic drift prevention, token optimization, semantic summarization, Cursor-style compression

---

### srmdn/hermes-agent-kit
⭐ **0** · `Python` · [github.com/srmdn/hermes-agent-kit](https://github.com/srmdn/hermes-agent-kit)

Production hardening pack for Hermes Agent — per-topic model routing, intelligent fallback chains, rate limiting, cost control, and operational guardrails. Essential toolkit for running Hermes reliably in production environments at scale with built-in reliability patterns.

**Status:** Beta  
**Key capabilities:** Production hardening, model routing, fallback chains, rate limiting, cost control, per-topic routing

---

### 0xNekr/hermes-topic-router
⭐ **0** · `Python` · [github.com/0xNekr/hermes-topic-router](https://github.com/0xNekr/hermes-topic-router)

Auto-route LLM models per chat topic for Hermes Agent — one bot, multiple models, zero manual switching. Intelligently selects the optimal language model based on conversation topic classification, balancing cost efficiency and capability automatically across all your agent conversations.

**Status:** Beta  
**Key capabilities:** Topic-based routing, model selection, automatic switching, multi-model orchestration, cost optimization

---

### robbyczgw-cla/hermes-topic-monitor
⭐ **2** · `Python` · [github.com/robbyczgw-cla/hermes-topic-monitor](https://github.com/robbyczgw-cla/hermes-topic-monitor)

Proactive topic monitoring with AI importance scoring on a schedule — continuously scans conversation topics and surfaces high-priority items before they're missed. Scheduled intelligence that keeps your Hermes Agent focused on what matters most across all active discussions.

**Status:** Beta  
**Key capabilities:** Topic monitoring, AI importance scoring, scheduled intelligence, proactive alerts, priority surfacing

---

### jiyangnan/weixi-hermes-autonomous-loop
⭐ **0** · `Python` · [github.com/jiyangnan/weixi-hermes-autonomous-loop](https://github.com/jiyangnan/weixi-hermes-autonomous-loop)

Autonomous agent loop system with episodic memory, FAISS vector store, and topic drift detection for Hermes Agent. Self-correcting agent execution that notices when conversations veer off-topic and re-anchors to core objectives using vector-based semantic similarity detection.

**Status:** Beta  
**Key capabilities:** Autonomous loop, episodic memory, FAISS vector store, topic drift detection, self-correction

---

### mz-club/agent-sessions-classify
⭐ **0** · `Python` · [github.com/mz-club/agent-sessions-classify](https://github.com/mz-club/agent-sessions-classify)

Classify, rename, and tidy Hermes Agent session titles into coherent topic groups — automated session organization that turns messy chat histories into a well-structured, searchable knowledge base. Perfect for agents handling dozens of concurrent conversations across multiple topics.

**Status:** Beta  
**Key capabilities:** Session classification, topic grouping, auto-renaming, session organization, knowledge structuring

---

### lecharles/hermes-framework-lab
⭐ **0** · `Python` · [github.com/lecharles/hermes-framework-lab](https://github.com/lecharles/hermes-framework-lab)

Running and evaluating Hermes Agent in Telegram topic-based lanes — experimentation framework for testing agent performance across isolated discussion threads. Benchmark agent behavior in structured topic environments for production tuning and capability evaluation.

**Status:** Beta  
**Key capabilities:** Telegram topic lanes, agent evaluation, performance benchmarking, experimental framework, topic isolation

---

## 🎯 Orchestration, Multi-Agent & Swarms

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

### Abruptive/Ankh.md
⭐ **community** · `Python` · [github.com/Abruptive/Ankh.md](https://github.com/Abruptive/Ankh.md)

TAW Agent x Hermes swarm framework. Cross-framework swarm orchestration for complex tasks.

**Status:** Experimental  
**Key capabilities:** Swarm framework, TAW integration, cross-framework

---

### runtim-enoteslabs/gladiator
⭐ **community** · `Python` · [github.com/runtim-enoteslabs/gladiator](https://github.com/runtim-enoteslabs/gladiator)

AI companies compete for stars. Competitive multi-agent arena for testing agent capabilities.

**Status:** Experimental  
**Key capabilities:** Agent competition, multi-agent arena, capability testing

---

### supermodeltools/bigiron
⭐ **community** · `Python` · [github.com/supermodeltools/bigiron](https://github.com/supermodeltools/bigiron)

AI-native SDLC with code graph. Full software development lifecycle powered by agents.

**Status:** Beta  
**Key capabilities:** AI-native SDLC, code graph, agent-driven development

---

### 1ilkhamov/opencode-hermes-multiagent
⭐ **community** · `Python` · [github.com/1ilkhamov/opencode-hermes-multiagent](https://github.com/1ilkhamov/opencode-hermes-multiagent)

17 specialized agents for Hermes. Pre-configured multi-agent team for diverse tasks.

**Status:** Beta  
**Key capabilities:** 17 agents, specialized roles, multi-agent coordination

---

### krutyshkin/telegram-agent-os
⭐ **2** · `Python` · [github.com/krutyshkin/telegram-agent-os](https://github.com/krutyshkin/telegram-agent-os)

Telegram-first multi-agent operating system for Hermes Agent — role-based bots, topic routing, skill integration, profile management, and built-in safety guardrails. A complete agent OS that turns Telegram into a multi-agent command center with production-grade safety, modular architecture, and scalable multi-bot coordination.

**Status:** Beta  
**Key capabilities:** Multi-agent OS, Telegram-native, role bots, topic routing, skill integration, safety guardrails, profile management

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

### xmbshwll/hermes-agent-docker
⭐ **community** · `Dockerfile` · [github.com/xmbshwll/hermes-agent-docker](https://github.com/xmbshwll/hermes-agent-docker)

Minimal Docker sandbox for Hermes Agent. Quick-start containerized deployment.

**Status:** Beta  
**Key capabilities:** Docker sandbox, minimal setup, containerized

---

### Crustocean/hermes-agent-template
⭐ **community** · `Dockerfile` · [github.com/Crustocean/hermes-agent-template](https://github.com/Crustocean/hermes-agent-template)

Production Docker template for cloud deployment. Battle-tested container configuration.

**Status:** Beta  
**Key capabilities:** Production Docker, cloud deployment, container template

---

### ellickjohnson/portainer-stack-hermes
⭐ **community** · `Dockerfile` · [github.com/ellickjohnson/portainer-stack-hermes](https://github.com/ellickjohnson/portainer-stack-hermes)

Docker Compose + Portainer stack for Hermes. One-click deployment with management UI.

**Status:** Experimental  
**Key capabilities:** Docker Compose, Portainer, one-click deployment

---

### metantonio/hermes-wsl-ubuntu
⭐ **community** · `Shell` · [github.com/metantonio/hermes-wsl-ubuntu](https://github.com/metantonio/hermes-wsl-ubuntu)

WSL2 Ubuntu setup guide for Hermes on Windows. Production deployment walkthrough for Windows users.

**Status:** Production  
**Key capabilities:** WSL2 setup, Ubuntu, Windows deployment, production guide

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

## 🔍 Detection & Media Forensics

Deepfake detection and media verification for autonomous agents.

### resemble-ai/detect-skill
⭐ **community** · `Python` · [github.com/resemble-ai/detect-skill](https://github.com/resemble-ai/detect-skill)

Deepfake detection for agents. Verify media authenticity before agents act on content.

**Status:** Beta  
**Key capabilities:** Deepfake detection, media forensics, content verification

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

### locomoki/tomorrows-front-page
⭐ **1** · `Python` · [github.com/locomoki/tomorrows-front-page](https://github.com/locomoki/tomorrows-front-page)

Turn any topic into tomorrow's front page with MiroFish simulation — AI-powered front page generation that transforms trending topics into newspaper-style editorial layouts. Creative content generation skill for Hermes Agent that visualizes what matters as professional front pages with automated layout and typography.

**Status:** Beta  
**Key capabilities:** Front page generation, MiroFish simulation, topic visualization, newspaper layout, content creation

---

### Delibread0601/askaipods
⭐ **2** · `TypeScript` · [github.com/Delibread0601/askaipods](https://github.com/Delibread0601/askaipods)

Search AI podcast quotes by topic across Lex Fridman, Dwarkesh Patel, No Priors, Latent Space, and more — semantic search engine for AI podcast knowledge discovery. Discover expert insights by topic across the top AI and tech podcast ecosystem, Hermes-compatible for research workflows and content curation.

**Status:** Beta  
**Key capabilities:** AI podcast search, quote discovery, topic search, semantic podcast engine, Lex Fridman, Dwarkesh Patel

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

## 🌐 Domain Applications

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

### bryercowan/hermes-embodied
⭐ **community** · `Python` · [github.com/bryercowan/hermes-embodied](https://github.com/bryercowan/hermes-embodied)

Self-improving robotics via VLA (Vision-Language-Action). Hermes controlling physical robots.

**Status:** Experimental  
**Key capabilities:** Robotics, VLA, embodied AI, self-improving

---

### bigph00t/hermescraft
⭐ **community** · `Python` · [github.com/bigph00t/hermescraft](https://github.com/bigph00t/hermescraft)

Minecraft AI companion with persistent memory. Hermes as a Minecraft agent with long-term memory.

**Status:** Beta  
**Key capabilities:** Minecraft integration, AI companion, persistent memory

---

### Snehal707/Hermes-mars-rover
⭐ **community** · `Python` · [github.com/Snehal707/Hermes-mars-rover](https://github.com/Snehal707/Hermes-mars-rover)

Mars rover simulator with ROS2 and Gazebo. Autonomous rover control via Hermes.

**Status:** Experimental  
**Key capabilities:** Mars rover, ROS2, Gazebo, space robotics

---

### rodmarkun/anihermes
⭐ **community** · `Python` · [github.com/rodmarkun/anihermes](https://github.com/rodmarkun/anihermes)

Local anime server and tracker. Self-hosted anime management with Hermes integration.

**Status:** Beta  
**Key capabilities:** Anime server, local tracker, media management

---

### Christabel337/job-scout-agent
⭐ **community** · `Python` · [github.com/Christabel337/job-scout-agent](https://github.com/Christabel337/job-scout-agent)

Autonomous job hunting agent. Automated job search, application tracking, and interview prep.

**Status:** Beta  
**Key capabilities:** Job hunting, automated applications, career management

---

### JackTheGit/hermes-ai-infrastructure-monitoring-toolkit
⭐ **community** · `Python` · [github.com/JackTheGit/hermes-ai-infrastructure-monitoring-toolkit](https://github.com/JackTheGit/hermes-ai-infrastructure-monitoring-toolkit)

Infrastructure monitoring with Telegram alerts. Proactive infrastructure health monitoring via Hermes.

**Status:** Beta  
**Key capabilities:** Infrastructure monitoring, Telegram alerts, health checks

---

### Ridwannurudeen/hermes-genesis
⭐ **community** · `Python` · [github.com/Ridwannurudeen/hermes-genesis](https://github.com/Ridwannurudeen/hermes-genesis)

Autonomous living world engine. Self-evolving simulated worlds powered by Hermes agents.

**Status:** Experimental  
**Key capabilities:** Living world, simulation, autonomous evolution

---

### Lethe044/hermes-legal
⭐ **community** · `Python` · [github.com/Lethe044/hermes-legal](https://github.com/Lethe044/hermes-legal)

Contract risk analysis in English and Turkish. Legal document review and risk assessment.

**Status:** Experimental  
**Key capabilities:** Legal analysis, contract review, EN/TR, risk assessment

---

### dlkakbs/hermes-startup-architect
⭐ **community** · `Python` · [github.com/dlkakbs/hermes-startup-architect](https://github.com/dlkakbs/hermes-startup-architect)

Investor-ready startup kits. Business plan generation, financial modeling, pitch deck creation.

**Status:** Beta  
**Key capabilities:** Startup kits, investor-ready, business planning

---

### hxsteric/mercury
⭐ **community** · `Python` · [github.com/hxsteric/mercury](https://github.com/hxsteric/mercury)

Multi-chain blockchain cash flow analyzer. Cross-chain financial analysis and tracking.

**Status:** Beta  
**Key capabilities:** Multi-chain, blockchain analysis, cash flow, DeFi

---

### Aum08Desai/hermes-research-agent
⭐ **community** · `Python` · [github.com/Aum08Desai/hermes-research-agent](https://github.com/Aum08Desai/hermes-research-agent)

Autonomous LLM research agent. Self-directed research with literature review and synthesis.

**Status:** Experimental  
**Key capabilities:** Autonomous research, LLM analysis, literature synthesis

---

## 🔀 Forks & Derivatives

Notable forks and derivative projects building on Hermes Agent.

### nativ3ai/hermes-agent-camel
⭐ **community** · `Python` · [github.com/nativ3ai/hermes-agent-camel](https://github.com/nativ3ai/hermes-agent-camel)

CaMeL trust boundaries for Hermes. Enhanced security and trust isolation for autonomous agents.

**Status:** Beta  
**Key capabilities:** Trust boundaries, CaMeL, security isolation

---

### jasperan/orahermes-agent
⭐ **community** · `Python` · [github.com/jasperan/orahermes-agent](https://github.com/jasperan/orahermes-agent)

Oracle OCI GenAI integration for Hermes. Enterprise cloud AI with Oracle infrastructure.

**Status:** Experimental  
**Key capabilities:** Oracle OCI, GenAI, enterprise cloud

---

### kaminocorp/hermes-alpha
⭐ **community** · `Python` · [github.com/kaminocorp/hermes-alpha](https://github.com/kaminocorp/hermes-alpha)

Cloud-deployed Hermes with infrastructure templates. Turnkey cloud deployment with pre-built templates.

**Status:** Beta  
**Key capabilities:** Cloud deployment, infra templates, turnkey setup

---

### beardthelion/hermes-skill-distillation
⭐ **community** · `Python` · [github.com/beardthelion/hermes-skill-distillation](https://github.com/beardthelion/hermes-skill-distillation)

Agentic training trajectories from Hermes sessions. Distill agent behavior into training data.

**Status:** Experimental  
**Key capabilities:** Skill distillation, training trajectories, agentic learning

---

## 📖 Guides

Community-maintained guides, wikis, and deployment references.

### metantonio/hermes-wsl-ubuntu
⭐ **community** · `Shell` · [github.com/metantonio/hermes-wsl-ubuntu](https://github.com/metantonio/hermes-wsl-ubuntu)

WSL2 Ubuntu setup guide for Hermes on Windows. Complete production walkthrough for Windows users.

**Status:** Production  
**Key capabilities:** WSL2 setup, Windows deployment, production guide

---

### martymcenroe/HermesWiki
⭐ **community** · `Markdown` · [github.com/martymcenroe/HermesWiki](https://github.com/martymcenroe/HermesWiki)

Community wiki with deployment patterns and configuration recipes. Crowd-sourced Hermes knowledge base.

**Status:** Beta  
**Key capabilities:** Community wiki, deployment patterns, configuration recipes

---

## 📊 Ecosystem Stats

| Metric | Value |
|--------|-------|
| Total repos indexed | 254 |
| Categories | 18 |
| Official Nous Research repos | 4 |
| Community awesome lists | 12 |
| UI/Dashboard projects | 10 |
| Memory systems | 15 |
| MCP integrations | 18 |
| Skill collections & plugins | 40 |
| Tools & utilities | 24 |
| Research/benchmark projects | 12 |
| Deployment & infra projects | 14 |
| Domain applications | 15 |
| Forks & derivatives | 4 |
| Language-specific resources | 12 (10 CN, 1 JP, 1 EN) |
| Total community stars | 1M+ across all indexed repos |

---

## 🔗 Cross-Reference Index

| Topic | Resources |
|-------|-----------|
| **Getting Started** | [Setup Guide](/hermes/setup/) · [Official Docs](https://hermes-agent.nousresearch.com/docs/) · [Orange Book](https://github.com/alchaincyf/hermes-agent-orange-book) · [27-Chapter Tutorial](https://github.com/longyunfeigu/learn-hermes-agent) |
| **Memory** | [Knowledge Architecture](/hermes/knowledge/) · [GBrain](https://github.com/garrytan/gbrain) · [EverOS](https://github.com/EverMind-AI/EverOS) · [claude-mem](https://github.com/thedotmack/claude-mem) · [mnemosyne](https://github.com/AxDSan/mnemosyne) |
| **MCP** | [MCP Guide](/hermes/mcp/) · [CorpusIQ](https://corpusiq.io) · [Kindly Search](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server) · [Kagi MCP](https://github.com/KSroido/Kagi-Session2API-MCP) |
| **Skills** | [Skills Catalog](/hermes/skills/catalog/) · [Marketing Skills](https://github.com/Ben-Home/marketingskills) · [Skill Factory](https://github.com/Romanescu11/hermes-skill-factory) · [372 Skills](https://github.com/BBridgeers/hermes-skills) |
| **UI** | [Hermes WebUI](https://github.com/nesquena/hermes-webui) · [Desktop](https://github.com/fathah/hermes-desktop) · [Studio](https://github.com/EKKOLearnAI/hermes-studio) · [Workspace](https://github.com/outsourc-e/hermes-workspace) · [Scarf](https://github.com/awizemann/scarf) |
| **Production** | [Deployment](/hermes/infrastructure/) · [Crons](/hermes/governance/scheduling/) · [K8s Operator](https://github.com/paperclipinc/hermes-operator) · [Autonomous Server](https://github.com/JackTheGit/hermes-autonomous-server) |
| **Research** | [Self-Evolution](https://github.com/NousResearch/hermes-agent-self-evolution) · [PawBench](https://github.com/agentscope-ai/PawBench) · [HermesBench](https://github.com/verkyyi/hermesbench) |
| **Security** | [Shellward](https://github.com/jnMetaCode/shellward) · [Skillguard](https://github.com/buzzicra/skillguard) · [NemoClaw](https://github.com/NVIDIA/NemoClaw) |

---

## 🎯 Operational Playbooks

Proven operational patterns for running Hermes in production.

- **Nightly self-evolution + guardrail verification** — Run self-evolution cycles during off-peak hours with automated regression testing to catch drift before it reaches production.
- **Memory pressure management with Honcho/Hindsight** — Monitor memory utilization, set retention policies, and archive stale context to prevent memory bloat and performance degradation.
- **Tune session timeout/expiry early** — Configure session timeouts appropriate to your workflow cadence. Too short breaks long-running tasks; too long wastes resources.
- **OpenClaw side-by-side migration strategy** — Run Hermes and OpenClaw in parallel during transition. Validate behavior parity before cutting over completely.
- **Treat USER.md and MEMORY.md as infrastructure** — Version control your agent personality and memory configuration. These files are as critical as production configs.

---

## 📈 Level-Up Blueprints

Progressive capability blueprints for advancing your Hermes deployment.

- **Memory stack that compounds (Hermes → Honcho → Hindsight → Plur)** — Layer memory systems progressively: start with Hermes built-in, add Honcho for peer modeling, Hindsight for long-term retention, and Plur for cross-agent shared memory.
- **Self-improvement without drift (evolution + linting + regression checks)** — Combine self-evolution with lintlang validation and benchmark regression tests to ensure improvements don't degrade reliability.
- **Operator cockpit (workspace + mission-control + webui)** — Build a unified operator interface combining Hermes Workspace for interaction, Mission Control for fleet management, and WebUI for monitoring.
- **Multi-agent execution layer (ACP + swarm + bigiron)** — Scale from single-agent to multi-agent with ACP delegation, swarm frameworks for parallel execution, and bigiron for AI-native SDLC.
- **Migration + deployment hardening (Nix + Docker + evey-setup)** — Productionize your deployment with Nix for reproducible builds, Docker for isolation, and evey-setup for automated environment provisioning.

---

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

> **📊 Ecosystem Stats:** 254 repos · 18 categories · 1M+ community stars · 40 skill collections · 18 MCP integrations · 15 domain applications

---

## FAQ

### What is the Hermes Ecosystem Directory?

The **Hermes Ecosystem Directory** is the most comprehensive collection of Hermes Agent resources in existence — **254+ repositories** organized across 18 categories including core tools, UIs, memory systems, MCP integrations, skills, deployment, research, and domain applications. It's the definitive map of the Hermes universe.

### How do I find tools and resources for Hermes Agent?

Browse the [Quick Navigation](#-quick-navigation) table above to jump to any of 18 categories: Core & Official, Documentation, UIs, Memory, MCP, Skills, Tools, Orchestration, Deployment, Security, Research, Content, Platform-Specific, Domain Applications, and more. Each entry includes star counts, maintainers, descriptions, and key capabilities.

### How do I submit my Hermes project to the ecosystem?

**[Submit a repo →](https://github.com/CorpusIQ/corpusiq-docs/issues/new?template=submit-repo.yml)** — takes 60 seconds. Include the repo URL, description, and suggested category. Submissions are reviewed within 48 hours and accepted repos appear in this directory with your GitHub handle credited. See the [Contributors page](/hermes/contributors.md) for full guidelines.

### What are the most popular Hermes Agent tools?

Based on community stars: **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** (195K+), **[claude-mem](https://github.com/thedotmack/claude-mem)** (82K+), **[open-design](https://github.com/nexu-io/open-design)** (65K+), **[gbrain](https://github.com/garrytan/gbrain)** (23K+), **[NemoClaw](https://github.com/NVIDIA/NemoClaw)** (21K+), **[screenpipe](https://github.com/screenpipe/screenpipe)** (19K+), and **[hermes-webui](https://github.com/nesquena/hermes-webui)** (14.5K+).

### How does the ecosystem directory stay updated?

The directory is maintained by **[CorpusIQ](https://corpusiq.io)** with monitoring crons that scan GitHub, MCP directories, and community channels for new Hermes Agent resources. Community submissions are reviewed within 48 hours. The discovery engine runs nightly (10 PM - 2 AM Arizona time) to detect new entries.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the Hermes Ecosystem Directory?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The most comprehensive collection of Hermes Agent resources — 254+ repositories across 18 categories including tools, UIs, memory, MCP, skills, deployment, research, and domain applications."
      }
    },
    {
      "@type": "Question",
      "name": "How do I find tools and resources for Hermes Agent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Browse 18 categories via Quick Navigation: Core, Documentation, UIs, Memory, MCP, Skills, Tools, Orchestration, Deployment, Security, Research, and more. Each entry includes stars, maintainers, and capabilities."
      }
    },
    {
      "@type": "Question",
      "name": "How do I submit my Hermes project to the ecosystem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Submit a repo in 60 seconds via the submission form. Include repo URL, description, and category. Reviewed within 48 hours with your GitHub handle credited."
      }
    },
    {
      "@type": "Question",
      "name": "What are the most popular Hermes Agent tools?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hermes Agent (195K+ stars), claude-mem (82K+), open-design (65K+), gbrain (23K+), NemoClaw (21K+), screenpipe (19K+), and hermes-webui (14.5K+) are the most starred projects."
      }
    },
    {
      "@type": "Question",
      "name": "How does the ecosystem directory stay updated?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Maintained by CorpusIQ with monitoring crons scanning GitHub and community channels. Community submissions reviewed within 48 hours. Nightly discovery engine detects new entries."
      }
    }
  ]
}
</script>

## Related Pages

- [Hermes Knowledge Hub — Production Deployment](/hermes/)
- [Documentation Index — Complete Reference](/hermes/index.md)
- [Agent Library — 9 Role Configurations](/hermes/agents/)
- [Community Contributors — Join the Directory](/hermes/contributors.md)
- [Skills Catalog — 133+ Production Skills](/hermes/skills/catalog/)
- [CorpusIQ MCP Connectors — 37+ Business Tools](/hermes/mcp/connectors/)
- [Submit a Repo →](https://github.com/CorpusIQ/corpusiq-docs/issues/new?template=submit-repo.yml)
