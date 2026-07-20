---
title: Hermes Ecosystem  --  Complete Resource Directory
description: The definitive directory of Hermes Agent resources  --  440+ repos, official docs, community tools, SDKs, integrations, benchmarks, and research. Everything in the Hermes universe.
---

# Hermes Ecosystem  --  Complete Resource Directory

The most comprehensive directory of Hermes Agent resources in existence. 450+ repositories, official documentation, community projects, SDKs, integrations, benchmarks, and research  --  all organized and cross-referenced.

> **Last updated:** July 19, 2026 · **Repos indexed:** 412+ · **Categories:** 18
>
> 👉 **[Submit a repo →](https://github.com/CorpusIQ/corpusiq-docs/issues/new?template=submit-repo.yml)** · Missing something? [Open a PR →](https://github.com/CorpusIQ/corpusiq-docs)

---

## 📑 Quick Navigation

|| Category | Count | Jump |
|----------|-------|------|
| [Core & Official](#-core--official) | 6 | [↓](#-core--official) |
| [Documentation & Learning](#-documentation--learning) | 9 | [↓](#-documentation--learning) |
| [Community & Awesome Lists](#-community--awesome-lists) | 34 | [↓](#-community--awesome-lists) |
| [UI & Dashboards](#-ui--dashboards) | 14 | [↓](#-ui--dashboards) |
|| [Memory & Knowledge](#-memory--knowledge) | 30 | [↓](#-memory--knowledge) |
| [MCP & Integrations](#-mcp--integrations) | 33 | [↓](#-mcp--integrations) |
| [Skills & Plugins](#-skills--plugins) | 69 | [↓](#-skills--plugins) |
|| [Tools & Utilities](#-tools--utilities) | 57 | [↓](#-tools--utilities) |
| [Detection & Media Forensics](#-detection--media-forensics) | 1 | [↓](#-detection--media-forensics) |
|| [Orchestration, Multi-Agent & Swarms](#-orchestration-multi-agent--swarms) | 27 | [↓](#-orchestration-multi-agent--swarms) |
|| [Deployment & Infrastructure](#-deployment--infrastructure) | 22 | [↓](#-deployment--infrastructure) |
| [Security & Governance](#-security--governance) | 6 | [↓](#-security--governance) |
| [Research & Benchmarks](#-research--benchmarks) | 12 | [↓](#-research--benchmarks) |
| [Content & Media](#-content--media) | 8 | [↓](#-content--media) |
| [Platform-Specific](#-platform-specific) | 11 | [↓](#-platform-specific) |
| [Domain Applications](#-domain-applications) | 22 | [↓](#-domain-applications) |
| [Forks & Derivatives](#-forks--derivatives) | 8 | [↓](#-forks--derivatives) |
| [Guides](#-guides) | 2 | [↓](#-guides) |

---

## 🏛 Core & Official

The foundational repositories maintained by Nous Research and core ecosystem maintainers.

### NousResearch/hermes-agent
⭐ **203,044** · `Python` · [github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

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

Run Hermes as a managed employee inside Paperclip companies. Connects the agent to Paperclip's task management and governance system  --  Hermes becomes a deployable workforce unit.

**Maintainer:** Nous Research  
**Key capabilities:** Paperclip integration, managed agent deployment, task management bridge

---

### NousResearch/autonovel
⭐ **1,148** · `Python` · [github.com/NousResearch/autonovel](https://github.com/NousResearch/autonovel)

Autonomous long-form writing pipeline built on Hermes Agent. Generates full manuscripts (100K+ words) end-to-end using the agent loop  --  plot development, chapter writing, consistency checking.

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

### Salomondiei08/oh-my-hermes
⭐ **620** · `Shell` · [github.com/Salomondiei08/oh-my-hermes](https://github.com/Salomondiei08/oh-my-hermes)

An opinionated workflow layer for building, shipping, and operating apps with Hermes Agent. Provides structured patterns for project scaffolding, deployment pipelines, and operational workflows  --  a "dotfiles for Hermes" approach to agent-driven development.

**Maintainer:** Salomondiei08  
**Key capabilities:** Project scaffolding, deployment pipelines, operational workflow patterns, opinionated Hermes configurations  
**Related:** [Skills Catalog →](/hermes/skills/catalog/) · [Deployment →](/hermes/infrastructure/)

---

## 📚 Documentation & Learning

Tutorials, guides, and educational resources for mastering Hermes Agent.

### alchaincyf/hermes-agent-orange-book
⭐ **4,443** · `Markdown` · [github.com/alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book)

"Hermes Agent 从入门到精通"  --  The Orange Book series. Comprehensive Chinese-language guide to Hermes Agent from beginner to expert. Covers installation, configuration, skills, MCP, deployment, and production patterns.

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
**Related:** [Hermes Knowledge Hub →](/hermes/) (this repo  --  everything the docs don't cover)

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

Tutorial on running Hermes Agent on a server  --  autonomous agent with built-in learning loop, cross-platform messaging, and 200+ model routing.

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

Curated list maintained by CorpusIQ  --  cross-linked with this knowledge hub for in-depth production guides.

**Related:** [This repository →](/hermes/)

---

### aliaihub/awesome-hermes-usecases
⭐ **101** · [github.com/aliaihub/awesome-hermes-usecases](https://github.com/aliaihub/awesome-hermes-usecases)

Curated real-world use cases for Hermes Agent  --  the self-improving AI agent from Nous Research. Production deployment stories and patterns.

---

### ChuckSRQ/awesome-hermes-skills
⭐ **66** · [github.com/ChuckSRQ/awesome-hermes-skills](https://github.com/ChuckSRQ/awesome-hermes-skills)

Curated collection of production-ready Hermes Agent skills  --  brainstorming, PR reviews, code generation, content creation.

---

### ZeroPointRepo/awesome-hermes-skills
⭐ **57** · [github.com/ZeroPointRepo/awesome-hermes-skills](https://github.com/ZeroPointRepo/awesome-hermes-skills)

85 built-in + 78 community skills, install-ready for Hermes Agent. Well-organized skill catalog with installation instructions.

---

### jefferyjob/awesome-hermes-agent-zh
⭐ **55** · [github.com/jefferyjob/awesome-hermes-agent-zh](https://github.com/jefferyjob/awesome-hermes-agent-zh)

Chinese-language curated list of skills, tools, integrations for Hermes Agent. (Hermes Agent 实用技能、工具、集成和资源列表)

---

### daodao97/Awesome-AI-Agent-Skills
⭐ **41** · [github.com/daodao97/Awesome-AI-Agent-Skills](https://github.com/daodao97/Awesome-AI-Agent-Skills)

Curated awesome list of AI agent skills across platforms  --  a comprehensive collection of agent skills, plugins, and extensions compatible with Hermes Agent, Claude Code, Cursor, and other AI coding platforms. Community-driven resource for discovering and sharing agent capabilities.

**Key capabilities:** Curated skill list, multi-platform agent skills, community-driven, Hermes-compatible, skill discovery
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### 0xarkstar/awesome-hermes-agent
⭐ **32** · [github.com/0xarkstar/awesome-hermes-agent](https://github.com/0xarkstar/awesome-hermes-agent)

Curated list of awesome resources for Hermes Agent by Nous Research.

---

### zcweah1981/awesome-hermes-agent-zh
⭐ **25** · [github.com/zcweah1981/awesome-hermes-agent-zh](https://github.com/zcweah1981/awesome-hermes-agent-zh)

Hermes Agent Chinese-language portal  --  entry path, deployment, OpenClaw migration, troubleshooting, downloadable solution packs.

---

### AlexAnys/awesome-openclaw-usecases-zh
⭐ **4,324** · [github.com/AlexAnys/awesome-openclaw-usecases-zh](https://github.com/AlexAnys/awesome-openclaw-usecases-zh)

50+ OpenClaw use cases in Chinese  --  the definitive Chinese-language resource for real-world OpenClaw deployments. Covers automation, content creation, DevOps, AI assistant, and knowledge management scenarios with domestic adaptations of international cases. Essential reference for Chinese-speaking Hermes and OpenClaw users building production agent workflows.

**Related:** Hermes is the successor to OpenClaw  --  most patterns apply directly.

---

### mergisi/awesome-openclaw-agents
⭐ **3,692** · [github.com/mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents)

162 OpenClaw agent templates  --  the largest curated collection of ready-to-deploy agent configurations for OpenClaw and Hermes. Covers automation, development, content creation, data analysis, customer support, and DevOps agent patterns with copy-paste deployment instructions. Each template includes configuration, dependencies, and usage examples. An essential launchpad for Hermes users migrating from OpenClaw or building new agent workflows.

**Related:** Hermes is the successor to OpenClaw  --  templates are directly adaptable.

---

### SamurAIGPT/awesome-openclaw
[github.com/SamurAIGPT/awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw)

Curated resources for OpenClaw (Hermes predecessor) with native Hermes migration path.

---

### ksimback/hermes-ecosystem
⭐ **1,020** · [github.com/ksimback/hermes-ecosystem](https://github.com/ksimback/hermes-ecosystem)

Hermes Atlas  --  community map of every tool, skill, and integration for Hermes Agent. Discover the complete Hermes universe through an interactive, searchable directory that maps skills to use cases, tools to platforms, and integrations to workflows. The definitive community-maintained ecosystem navigator.

**Key capabilities:** Ecosystem mapping, tool discovery, skill directory, integration map, community-curated, interactive directory
**Related:** [This directory →](/hermes/ecosystem/)

---

### VoltAgent/awesome-agent-skills
⭐ **25,574** · [github.com/VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)

1,000+ agent skills from official dev teams and community  --  the most comprehensive cross-platform agent skills directory. Curated collection of production-grade skills for Claude Code, Cursor, Codex CLI, Gemini CLI, Hermes Agent, and other AI coding agents. Official team-verified skills alongside community contributions with quality ratings and compatibility matrices. Essential resource for discovering battle-tested skills that work across the agent ecosystem.

**Key capabilities:** 1,000+ skills, official dev teams, cross-platform, community-vetted, quality ratings, compatibility matrix
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### sickn33/antigravity-awesome-skills
⭐ **40,916** · [github.com/sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)

1,500+ agentic skills for Claude Code, Cursor, Codex CLI, Gemini CLI, and Hermes Agent  --  the largest independently curated skill collection in the agent ecosystem. Massive library spanning development, content creation, automation, data analysis, and business operations. Regularly updated with new skills from the broader AI coding community. A go-to resource for Hermes users seeking proven, cross-compatible agent capabilities.

**Key capabilities:** 1,500+ skills, multi-platform, Claude Code/Cursor/Codex/Gemini/Hermes, largest curated collection, continuously updated
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### hesreallyhim/awesome-claude-code
⭐ **46,655** · [github.com/hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)

Curated skills, hooks, slash-commands, agent orchestrators, and plugins for AI coding agents  --  the definitive resource for extending Claude Code and Hermes Agent with community-built extensions. Covers skill development patterns, hook systems, multi-agent orchestration, and IDE integration workflows. Essential reference for anyone building on Claude Code-compatible agent frameworks including Hermes Agent, with cross-compatible skill formats and shared ecosystem patterns.

**Key capabilities:** Skills catalog, hooks system, slash-commands, agent orchestrators, plugins, Claude Code + Hermes compatible, community extensions
**Related:** [Skills Catalog →](/hermes/skills/catalog/) · [Architecture →](/hermes/architecture/)

---

### anthropics/skills
⭐ **151,734** · [github.com/anthropics/skills](https://github.com/anthropics/skills)

Official Anthropic repository for Agent Skills  --  the canonical reference implementation for the agent skills protocol. Defines the standard skill format, conventions, and best practices that Hermes Agent skills follow. Essential starting point for anyone developing custom skills for Hermes or contributing to the broader agent skills ecosystem. The authoritative source for skill development patterns and protocol compliance.

**Key capabilities:** Official Anthropic, canonical reference, skill protocol, standard format, Hermes-compatible, skill development patterns
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### ComposioHQ/awesome-claude-skills
⭐ **64,883** · [github.com/ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)

Curated list of Claude Skills, resources, and tools for customizing AI workflows  --  one of the largest skill discovery resources in the agent ecosystem. Comprehensive directory covering development, automation, content creation, and business operations skills with Hermes Agent compatibility. Major skill discovery hub for Hermes users seeking battle-tested, community-vetted agent capabilities from the broader Claude and AI coding ecosystem.

**Key capabilities:** Curated skill list, Claude + Hermes compatible, AI workflow customization, community-vetted, skill discovery, major resource hub
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### wshobson/agents
⭐ **36,858** · [github.com/wshobson/agents](https://github.com/wshobson/agents)

Multi-harness agentic plugin marketplace for Claude Code, Codex CLI, Cursor, OpenCode, GitHub Copilot, and Hermes Agent  --  the unified plugin discovery layer spanning every major AI coding harness. Browse, discover, and install plugins that work across your entire agent toolkit without framework lock-in. Essential resource for Hermes users building multi-harness workflows that span Claude Code, Codex, Cursor, and Copilot environments with seamless cross-platform plugin compatibility.

**Key capabilities:** Multi-harness marketplace, Claude Code/Codex/Cursor/Copilot/Hermes, plugin discovery, cross-platform, framework-agnostic
**Related:** [Skills Catalog →](/hermes/skills/catalog/) · Plugins

---

### github/awesome-copilot
⭐ **35,145** · [github.com/github/awesome-copilot](https://github.com/github/awesome-copilot)

GitHub's official community-contributed instructions, agents, skills, and configurations for Copilot and compatible agent platforms  --  the authoritative Copilot extension ecosystem directly maintained by GitHub. Curated collection of Copilot-ready resources with documented Hermes Agent compatibility paths. Essential reference for organizations standardizing on GitHub's agent ecosystem while leveraging Hermes Agent for autonomous workflows beyond Copilot's built-in capabilities.

**Key capabilities:** Official GitHub, Copilot skills, community-contributed, agent configurations, Hermes-compatible, enterprise standard
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### CorpusIQ/corpusiq-docs/hermes ← YOU ARE HERE
⭐ **[Star this repo →](https://github.com/CorpusIQ/corpusiq-docs)**

The most comprehensive Hermes production resource: 36+ pages, 326+ repos indexed, 133+ skills cataloged, 37+ MCP connectors, production-cron reference architecture, memory stack deep-dives, deployment patterns. Everything the official docs don't cover.

**Related:** [Architecture →](/hermes/architecture/) · [Knowledge →](/hermes/knowledge/) · [Crons →](/hermes/governance/scheduling/) · [MCP →](/hermes/mcp/)

---

### davepoon/buildwithclaude
⭐ **3,075** · [github.com/davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)

Curated hub for Claude Skills, Agents, Commands, Hooks, and Plugins. The definitive reference for discovering cross-compatible Hermes Agent skills and extensions  --  every Claude Code extension listed here has a direct migration path to Hermes skill format. Essential resource for expanding your agent's capabilities with community-validated, battle-tested extensions from the broader AI agent ecosystem.

**Key capabilities:** Skills hub, agents directory, hooks catalog, Claude-to-Hermes migration, community-validated extensions, cross-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### jeremylongshore/claude-code-plugins-plus-skills
⭐ **2,389** · [github.com/jeremylongshore/claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills)

Open-source marketplace with 425 plugins, 2,810 skills, and 200 agents  --  the largest unified repository of cross-compatible Hermes Agent extensions. Browse, discover, and install production-ready skills and plugins with verified Hermes compatibility. A one-stop marketplace for exponentially expanding your agent's toolbox with community-built capabilities spanning every domain.

**Key capabilities:** 425 plugins, 2,810 skills, 200 agents, open marketplace, Hermes-compatible, largest unified repository
**Related:** [Skills Catalog →](/hermes/skills/catalog/) · Plugins

---

### anthropics/claude-code
⭐ **132,851** · [github.com/anthropics/claude-code](https://github.com/anthropics/claude-code)

Official Anthropic Claude Code repository. Agentic coding tool that lives in your terminal with full codebase understanding. Reference implementation for agent-based development workflows applicable to Hermes deployments.

**Maintainer:** Anthropic
**Key capabilities:** Agentic coding, terminal-native, full codebase understanding, reference implementation, Hermes-compatible patterns
**Related:** [Architecture →](/hermes/architecture/)

---

### shareAI-lab/learn-claude-code
⭐ **67,001** · [github.com/shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)

Nano Claude Code-like agent harness built from scratch. Educational resource for understanding agent architecture patterns applicable to Hermes. Learn how agentic coding harnesses work by studying a minimal implementation.

**Key capabilities:** Educational resource, agent architecture, minimal implementation, Hermes-applicable patterns, nano agent harness
**Related:** [Architecture →](/hermes/architecture/)

---

### anthropics/claude-plugins-official
⭐ **30,288** · [github.com/anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

Official Anthropic-managed directory of high-quality Claude Code plugins. Reference implementation for agent plugin architecture applicable to Hermes  --  demonstrates canonical plugin patterns, lifecycle management, and quality standards for agent extensions. The authoritative source for understanding how production-grade agent plugin systems are structured and governed.

**Maintainer:** Anthropic
**Key capabilities:** Official plugin directory, canonical plugin architecture, quality standards, lifecycle management, Hermes-applicable patterns
**Related:** Plugins · [Skills Catalog →](/hermes/skills/catalog/)

---

### diet103/claude-code-infrastructure-showcase
⭐ **9,707** · [github.com/diet103/claude-code-infrastructure-showcase](https://github.com/diet103/claude-code-infrastructure-showcase)

Claude Code infrastructure examples with skill auto-activation, hooks, and agents. Practical architecture patterns for Hermes deployments  --  showcases real-world infrastructure configurations with automated skill loading, hook-based event systems, and multi-agent coordination setups that translate directly to Hermes production environments.

**Key capabilities:** Infrastructure examples, skill auto-activation, hook systems, multi-agent patterns, production-ready, Hermes-applicable
**Related:** [Infrastructure →](/hermes/infrastructure/) · [Architecture →](/hermes/architecture/)

---

### rohitg00/awesome-claude-code-toolkit
⭐ **2,085** · [github.com/rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit)

Comprehensive Claude Code toolkit: 135 agents, 35 curated skills, 42 commands, 176+ plugins. Discovery resource for Hermes-compatible tools  --  the largest single-curator collection of cross-compatible agent extensions spanning every capability domain. An essential browsing destination for Hermes users seeking battle-tested tools, skills, and plugins from the broader agent ecosystem.

**Key capabilities:** 135 agents, 35 skills, 42 commands, 176+ plugins, cross-compatible discovery, curated toolkit, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/) · Plugins

---

### multica-ai/andrej-karpathy-skills
⭐ **178,262** · [github.com/multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)

Andrej Karpathy AI skills collection  --  a comprehensive curated set of AI development skills, patterns, and methodologies from the legendary AI educator, researcher, and former Tesla Autopilot/OpenAI leader. Covers deep learning architecture design, neural network training methodology, practical AI engineering patterns, data curation strategies, and production ML deployment best practices refined through years of leading-edge AI research and education. Drop-in compatible with Hermes Agent for expert-level AI development capabilities backed by Karpathy's battle-tested approaches to building intelligent systems that work in the real world.

**Key capabilities:** Andrej Karpathy skills, deep learning patterns, neural network design, training methodology, AI engineering, production ML, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### heilcheng/awesome-agent-skills
⭐ **5,670** · [github.com/heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)

Awesome Agent Skills  --  a curated collection of agent skills and capabilities for AI coding agents across Claude Code, Cursor, Codex, Hermes Agent, and other platforms. Community-driven resource cataloging production-grade skills with compatibility ratings, installation guides, and real-world usage examples. An essential discovery hub for finding battle-tested agent skills that extend autonomous agent capabilities across development, operations, content creation, and domain-specific workflows.

**Key capabilities:** Curated agent skills, multi-platform, community-driven, compatibility ratings, skill discovery, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### zhayujie/CowAgent
⭐ **45,469** · `Python` · [github.com/zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)

CowAgent  --  comprehensive AI agent framework for building autonomous task execution systems with multi-modal capabilities. Provides a structured approach to agent development with built-in memory management, tool integration, and multi-step reasoning pipelines. Production-ready framework for deploying autonomous agents that learn from interactions, manage complex task graphs, and coordinate across multiple knowledge domains  --  compatible with Hermes Agent for extended autonomous workflows.

**Key capabilities:** AI agent framework, autonomous task execution, multi-modal, memory management, tool integration, multi-step reasoning, Hermes-compatible
**Related:** [Architecture →](/hermes/architecture/) · [Orchestration →](#-orchestration-multi-agent--swarms)

---

### ksimback/hermes-ecosystem
⭐ **1,076** · `HTML` · [github.com/ksimback/hermes-ecosystem](https://github.com/ksimback/hermes-ecosystem)

🗺️ Hermes Atlas — the community map of every tool, skill, and integration for Hermes Agent by Nous Research. Live at hermesatlas.com. The go-to visual directory for discovering the full Hermes ecosystem landscape — browse tools, skills, integrations, and community projects in an interactive map format.

**Key capabilities:** Ecosystem visualization, tool discovery, community directory, interactive mapping, Hermes-compatible
**Related:** [Architecture →](/hermes/architecture/) · [Skills Catalog →](/hermes/skills/catalog/)

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

Web dashboard for Hermes Agent  --  multi-platform AI chat, session management, scheduled jobs overview, skills browser, and agent configuration. MCP-native.

**Maintainer:** EKKOLearnAI  
**Key capabilities:** Session management, cron visualization, skills browser, multi-platform chat, MCP integration

---

### outsourc-e/hermes-workspace
⭐ **5,720** · `TypeScript` · [github.com/outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace)

Native web workspace for Hermes Agent  --  chat, terminal, memory browser, skills manager. All-in-one workspace environment.

**Maintainer:** outsourc-e  
**Key capabilities:** Integrated terminal, memory browser, skills manager, chat interface

---

### qingchencloud/clawpanel
⭐ **2,842** · `TypeScript` · [github.com/qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel)

OpenClaw & Hermes Agent multi-engine AI management panel  --  built-in AI assistant with tool calling, image recognition, multimodal, one-click deployment.

**Language:** Chinese (中文)  
**Key capabilities:** Multi-engine management, tool calling, image recognition, one-click deployment

---

### awizemann/scarf
⭐ **629** · `Swift` · [github.com/awizemann/scarf](https://github.com/awizemann/scarf)

Native macOS and iOS App for the Hermes AI agent  --  multi-window, multi-profile, native performance. First-class Apple platform experience.

**Maintainer:** awizemann  
**Key capabilities:** Native macOS/iOS, multi-window, multi-profile, Apple design language

---

### bytedance/UI-TARS-desktop
⭐ **36,725** · `TypeScript` · [github.com/bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)

Open-Source Multimodal AI Agent Stack  --  ByteDance's desktop-native agent framework with vision-language understanding, GUI automation, and multi-step task execution. Combines computer vision, natural language processing, and action execution into a unified desktop agent that can see, understand, and interact with any GUI application. Production-grade infrastructure for building autonomous desktop agents that navigate interfaces, fill forms, extract data, and execute complex workflows across applications.

**Maintainer:** ByteDance
**Key capabilities:** Multimodal agent, vision-language, GUI automation, desktop agent, cross-application, production-grade
**Related:** [UI & Dashboards →](#-ui--dashboards)

---

### kkllxy/hermes-web-ui
⭐ **0** · [github.com/kkllxy/hermes-web-ui](https://github.com/kkllxy/hermes-web-ui)

Web dashboard for Hermes Agent  --  multi-platform AI chat, session management, scheduled jobs overview.

---

### nexu-io/open-design
⭐ **66,838** · `TypeScript` · [github.com/nexu-io/open-design](https://github.com/nexu-io/open-design)

Open Design platform  --  local-first, open-source design tool with 259+ skills for AI-powered creative workflows. Native desktop application enabling agent-driven design, prototyping, and visual content generation. Cross-compatible skill format with Hermes Agent, making it a powerful companion for autonomous design workflows in the Hermes ecosystem.

**Related:** Hermes-compatible skills format. Many skills are cross-compatible.

---

### chrisryugj/hermes-dashboard
⭐ **31** · `HTML` · [https://github.com/chrisryugj/hermes-dashboard](https://github.com/chrisryugj/hermes-dashboard)

Web dashboard for Hermes Agent gateway — full config, MCP, cron, model management without CLI


---

### synthalorian/hermes-wingman
⭐ **5** · `Dart` · [https://github.com/synthalorian/hermes-wingman](https://github.com/synthalorian/hermes-wingman)

The complete Hermes Agent GUI — Flutter desktop + mobile app + Rails 8 web dashboard. Glass morphism UI, 29 themes, Rust backend. Replaces the entire Hermes CLI.


---

### praveenkay/Hermes_Portal
⭐ **1** · `Python` · [https://github.com/praveenkay/Hermes_Portal](https://github.com/praveenkay/Hermes_Portal)

Hermes Agent Web UI -- cross-platform dashboard: sessions, agents, desktop, projects.


---

## 🧠 Memory & Knowledge

Persistent memory and knowledge management for autonomous agents.

### thedotmack/claude-mem
⭐ **82,700** · `TypeScript` · [github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

Persistent context across sessions for every agent. Captures everything your agent does  --  files, conversations, decisions  --  and makes it retrievable. Works with Hermes, Claude Code, Codex, and other agents.

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

Self-evolving memory across Agent and platform. The one portable memory layer for every agent  --  works across Hermes, Claude, GPT, and custom agents.

**Key capabilities:** Self-evolving memory, cross-platform portability, automatic learning  
**Related:** [Memory Stack →](/hermes/knowledge/)

---

### codejunkie99/agentic-stack
⭐ **2,112** · `Python` · [github.com/codejunkie99/agentic-stack](https://github.com/codejunkie99/agentic-stack)

One brain, many harnesses. Portable `.agent/` folder (memory + skills + config) that works across Hermes, Claude Code, Codex, and other agents.

**Key capabilities:** Portable agent configuration, cross-platform memory, unified skill system

---

### mnemosyne-oss/mnemosyne
⭐ **1,358** · `Python` · [github.com/mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne)

The Zero-Dependency, Sub-Millisecond AI Memory System for Hermes Agents and Everyone Else. Production-grade local memory with zero external dependencies — battle-tested across agents, AI, ML, and Nous Research workflows.

**Key capabilities:** Zero dependencies, sub-ms retrieval, local-first, Hermes-native, agents/AI/ML ecosystem

---

### AVIDS2/memorix
⭐ **519** · `TypeScript` · [github.com/AVIDS2/memorix](https://github.com/AVIDS2/memorix)

Open-source cross-agent memory layer for coding agents via MCP. Compatible with Claude Code, Codex, Cursor, Windsurf, Gemini CLI, Antigravity, OpenClaw, Hermes Agent, Oh-my-Pi, Pi, Copilot, Kiro, OpenCode, and Trae. Local-first, Apache-2.0 licensed.

**Key capabilities:** Cross-agent memory, MCP-native server, local-first sessions, 14+ agent compatibility, TypeScript SDK
**Related:** [MCP & Integrations →](#-mcp--integrations) · [Memory Stack →](/hermes/knowledge/)

---

### CodeAbra/iai-personal-memory-engine
⭐ **307** · `Python` · [github.com/CodeAbra/iai-personal-memory-engine](https://github.com/CodeAbra/iai-personal-memory-engine)

MCP memory server for AI coding assistants. Works with Claude Code, Cursor, Codex, Gemini CLI, Cline, Continue, Cherry Studio, Zed, Hermes, OpenClaw, and any MCP client. Local, encrypted, verbatim recall. MIT.

**Maintainer:** CodeAbra
**Key capabilities:** Local encrypted memory, verbatim recall, MCP-native, cross-agent support, SQLite + vector DB hybrid
**Related:** [MCP & Integrations →](#-mcp--integrations) · [Memory Stack →](/hermes/knowledge/)

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

YantrikDB memory provider for Hermes Agent  --  self-maintaining database with automatic indexing and cleanup.

---

### prakrititz/relayBrain
[github.com/prakrititz/relayBrain](https://github.com/prakrititz/relayBrain)

Portable memory layer for AI agents  --  switch between Claude, Codex, Gemini, and Hermes without losing context.

---

### screenpipe/screenpipe
⭐ **19,319** · `Rust` · [github.com/screenpipe/screenpipe](https://github.com/screenpipe/screenpipe)

YC S26  --  AI that knows what you've seen, said, or heard. Records everything you do and makes it searchable for agents. Hermes-compatible via API.

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

Three-tier memory architecture inspired by Hermes Agent  --  global memory → topic-level memory → project-level memory with hierarchical knowledge organization. Scalable memory design pattern for AI agents handling complex, multi-domain workflows with clear context boundaries and progressive knowledge refinement.

**Status:** Experimental  
**Key capabilities:** Three-tier memory, hierarchical architecture, global-topic-project model, context boundaries, memory design patterns

---

### MemTensor/MemOS
⭐ **9,901** · `Python` · [github.com/MemTensor/MemOS](https://github.com/MemTensor/MemOS)

Self-evolving memory operating system for LLM and AI agents  --  hybrid retrieval with cross-task memory persistence. Learn, recall, and adapt across sessions without manual memory management. Designed for Hermes, Claude, GPT, and autonomous agent workflows requiring continuous knowledge accumulation.

**Key capabilities:** Self-evolving memory, hybrid retrieval, cross-task persistence, automatic learning, agent-native memory OS  
**Related:** [Memory Stack →](/hermes/knowledge/)

---

### stephenschoettler/hermes-lcm
⭐ **741** · `Python` · [github.com/stephenschoettler/hermes-lcm](https://github.com/stephenschoettler/hermes-lcm)

Lossless Context Management: DAG-based context engine that never loses a message  --  production-grade memory for Hermes Agent. Built on directed acyclic graph architecture that preserves every conversation turn with full provenance tracking, context branching, and deterministic replay. Eliminates context window truncation artifacts and enables infinite conversation depth through intelligent context graph traversal, making it the definitive solution for long-running Hermes Agent sessions requiring perfect message retention.

**Key capabilities:** DAG-based context, lossless message retention, production-grade memory, context branching, deterministic replay, infinite conversation depth, Hermes-native
**Related:** [Knowledge Architecture →](/hermes/knowledge/) · [Memory Stack →](/hermes/knowledge/)

---

### rohitg00/agentmemory
⭐ **23,165** · `Python` · [github.com/rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)

The #1 persistent memory solution for AI coding agents. Drop-in memory layer for Hermes agents that prevents context loss across sessions with vector-backed recall  --  maintain perfect conversation continuity even across restarts. Production-grade memory persistence with sub-millisecond retrieval for autonomous agent workflows requiring flawless recall across unlimited sessions.

**Key capabilities:** Persistent memory, vector-backed recall, drop-in integration, context continuity, cross-session recall, Hermes-native
**Related:** [Memory Stack →](/hermes/knowledge/)

---

### Bessouat40/RAGLight
⭐ **663** · `Python` · [github.com/Bessouat40/RAGLight](https://github.com/Bessouat40/RAGLight)

RAGLight  --  lightweight Retrieval-Augmented Generation implementation optimized for agent memory and knowledge retrieval. Provides a minimal, fast RAG pipeline that serves as a drop-in knowledge layer for autonomous agents needing efficient document indexing, semantic search, and context injection. Designed for low-latency agent workflows where traditional vector databases are overkill  --  perfect for Hermes Agent knowledge management in resource-constrained environments with sub-100ms retrieval over moderate document collections.

**Key capabilities:** RAG implementation, lightweight retrieval, agent memory, semantic search, document indexing, context injection, Hermes-compatible
**Related:** [Knowledge Architecture →](/hermes/knowledge/) · [Memory Stack →](/hermes/knowledge/)

---

### Sibyl-Labs/Sibyl-Memory
⭐ **84** · `Python` · [https://github.com/Sibyl-Labs/Sibyl-Memory](https://github.com/Sibyl-Labs/Sibyl-Memory)

Sibyl Memory Plugin for Hermes enables persistent memory across long time horizons, and enables relational context previously unavailable. Self-learning and auto-skill creation creates an agent that grows with you.  Local SQLite, structured tiers, no vector DB. SDK, CLI, MCP server, Hermes plugin.


---

### itechmeat/open-second-brain
⭐ **71** · `TypeScript` · [https://github.com/itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)

Local-first 🧠 memory for Hermes Agent that lives in your Obsidian vault and remembers project context. Nightly 😴 dream passes turn repeat corrections into confirmed preferences with measurable confidence. Adapters ship for Claude Code, Codex, and OpenClaw, with an MCP server for anything else.


---

### itsXactlY/mazemaker
⭐ **49** · `Python` · [https://github.com/itsXactlY/mazemaker](https://github.com/itsXactlY/mazemaker)

Semantic memory system with knowledge graph, spreading activation, embedding-based recall, autonomous dream consolidation, and C++ LSTM+kNN pattern learning for any /MCP and the Hermes Agent.

**Topics:** `aes-256`, `agent`, `agents`, `ai`, `brain`, `claude`, `codex`, `gpt`

---

### xMannixx/agent-memory-skill
⭐ **2** · `Python` · [https://github.com/xMannixx/agent-memory-skill](https://github.com/xMannixx/agent-memory-skill)

Local-first SQLite memory for Hermes with authority lanes, recall snippets, audit/recovery, confidence decay, and query-aware plugin retrieval.

**Topics:** `agent-memory`, `hermes`, `local-first`, `memory`, `retrieval`, `sqlite`

---

### luluthehermeticcrabBot/phronesis
⭐ **2** · `JavaScript` · [https://github.com/luluthehermeticcrabBot/phronesis](https://github.com/luluthehermeticcrabBot/phronesis)

Practical wisdom from agent experience. Auto-skill creation, FTS5 session search, persona system, memory consolidation, and Telegram notifications — bridging Hermes Agent's adaptive learning loop into OpenCode's plugin ecosystem.


---

### samrusani/AliceBot
⭐ **1** · `Python` · [https://github.com/samrusani/AliceBot](https://github.com/samrusani/AliceBot)

Local-first AI agent memory and second-brain runtime with MCP, governed scheduler, live capture connectors, dogfood telemetry, OpenClaw, and Hermes integrations.

**Topics:** `agent-memory`, `agentic-control-plane`, `ai-agents`, `ai-memory`, `context-engineering`, `continuity-layer`, `developer-tools`, `dogfooding`

---

### siddiqitaha/hermes-knowledge-brain
⭐ **0** · `Python` · [https://github.com/siddiqitaha/hermes-knowledge-brain](https://github.com/siddiqitaha/hermes-knowledge-brain)

Model-agnostic memory substrate for AI agents

**Topics:** `ai-agents`, `knowledge-graph`, `memory`, `python`

---

### Aphelios01-sdk/hermes-brain
⭐ **0** · `Python` · [https://github.com/Aphelios01-sdk/hermes-brain](https://github.com/Aphelios01-sdk/hermes-brain)

Hermes Agent skills and memories - AI training knowledge base


---

### ahonore42/logios-brain
⭐ **0** · `Python` · [https://github.com/ahonore42/logios-brain](https://github.com/ahonore42/logios-brain)

A server-side memory and knowledge graph API for AI agents. Stores episodic memories (Postgres+Qdrant), semantic knowledge (Neo4j), and identity instructions, with native integration libraries for agent frameworks like Hermes, OpenClaw, Pi, GoClaw, Claude Agent SDK, and ZeroClaw.


---

### yun520-1/mark-heartflow-skill
⭐ **26** · `JavaScript` · [github.com/yun520-1/mark-heartflow-skill](https://github.com/yun520-1/mark-heartflow-skill)

心虫 (HeartFlow) — Cognitive state encoder + autonomous decision engine. 60 modules encode raw text into structured cognitive data, judgment engine handles multi-path decisions, decision routing does field tracking, self-healing RL learns from errors. Invoked by Hermes Agent via MCP, providing structured cognitive snapshots to LLMs.

**Key capabilities:** Cognitive state encoding, multi-path decision engine, field tracking, self-healing reinforcement learning, MCP-native integration, structured cognitive snapshots
**Maintainer:** yun520-1

---

### cx2002302-lang/zettelkasten-second-memory
⭐ **16** · `TypeScript` · [github.com/cx2002302-lang/zettelkasten-second-memory](https://github.com/cx2002302-lang/zettelkasten-second-memory)

An OpenClaw (2026.4/2026.6+) and Hermes Agent plugin that turns AI conversations into a permanent Zettelkasten knowledge base — atomic notes, bi-directional links, knowledge distillation, and MCP tool exposure. Converts agent dialogue into structured, interlinked knowledge artifacts with SQLite persistence.

**Maintainer:** cx2002302-lang
**Topics:** `knowledge-management`, `zettelkasten`, `mcp-server`, `note-taking`, `second-memory`, `knowledge-graph`
**Key capabilities:** AI conversation → Zettelkasten, bi-directional linking, MCP tool exposure, SQLite persistence, atomic notes, knowledge distillation

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

### apache/camel
⭐ **6,238** · `Java` · [github.com/apache/camel](https://github.com/apache/camel)

Open source integration framework  --  Apache Camel is the industry-standard enterprise integration framework with 300+ components for connecting virtually any system, protocol, or API. Battle-tested over two decades with a mature component ecosystem covering databases, message queues, SaaS platforms, cloud services, file systems, and IoT protocols. Hermes Agent users leverage Camel as an integration backbone for building robust agent pipelines with enterprise-grade reliability, monitoring, and error handling. The definitive open-source integration layer for production agent deployments.

**Maintainer:** Apache Software Foundation
**Key capabilities:** 300+ integration components, enterprise integration patterns, message routing, protocol translation, ETL, Hermes-compatible
**Related:** [MCP Guide →](/hermes/mcp/)

---

### Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server
⭐ **345** · `Python` · [github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server)

Kindly Web Search MCP Server  --  web search + robust content retrieval for Hermes and other MCP-compatible agents.

---

### anysearch-ai/anysearch-mcp-server
⭐ **1,166** · `TypeScript` · [github.com/anysearch-ai/anysearch-mcp-server](https://github.com/anysearch-ai/anysearch-mcp-server)

Unified real-time search MCP server for AI agents  --  aggregates results from Google, Bing, Brave, and DuckDuckGo with a single API. Drop-in search backend for Hermes Agent providing fresh, ranked web results with configurable source priority and result filtering. Eliminates the need for multiple search MCP servers.

**Key capabilities:** Multi-engine search, Google/Bing/Brave/DuckDuckGo, unified API, real-time results, MCP-native
**Related:** [MCP Guide →](/hermes/mcp/)

---

### KSroido/Kagi-Session2API-MCP
⭐ **137** · `Python` · [github.com/KSroido/Kagi-Session2API-MCP](https://github.com/KSroido/Kagi-Session2API-MCP)

Free Kagi Search MCP server  --  access Kagi search and summarizer via session tokens. Hermes-compatible.

---

### AVIDS2/memorix
⭐ **519** · `TypeScript` · [github.com/AVIDS2/memorix](https://github.com/AVIDS2/memorix)

Open-source cross-agent memory layer for coding agents via MCP. Compatible with Claude Code, Codex, Cursor, Windsurf, Gemini CLI, Antigravity, OpenClaw, Hermes Agent, Oh-my-Pi, Pi, Copilot, Kiro, OpenCode, and Trae. Provides persistent, searchable memory across multiple AI coding assistants through the Model Context Protocol.

**Maintainer:** AVIDS2  
**Key capabilities:** Cross-agent memory, MCP integration, persistent storage, multi-assistant compatibility, local-first architecture  
**Related:** [MCP Guide →](/hermes/mcp/) · [Knowledge Systems →](/hermes/knowledge/)

---

### zoedsoupe/anubis-mcp
⭐ **147** · `Elixir` · [github.com/zoedsoupe/anubis-mcp](https://github.com/zoedsoupe/anubis-mcp)

Elixir Model Context Protocol (MCP) SDK  --  forked from hermes-mcp. Bring MCP capabilities to Elixir ecosystems.

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

ClawRouter for Hermes  --  55+ LLMs, x402 USDC micropayments on Base & Solana. Pay-per-use model routing for Hermes agents.

---

### AlexAI-MCP/hermes-CCC
⭐ **119** · `Python` · [github.com/AlexAI-MCP/hermes-CCC](https://github.com/AlexAI-MCP/hermes-CCC)

Hermes Agent ported to Claude Code Channel  --  46 native skills, no OAuth required. Run Hermes skills inside Claude Code.

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

### papersgpt/papersgpt-for-zotero
⭐ **2,461** · `TypeScript` · [github.com/papersgpt/papersgpt-for-zotero](https://github.com/papersgpt/papersgpt-for-zotero)

Zotero AI MCP plugin with ChatGPT, Claude, DeepSeek, and Grok integration  --  bring AI-powered research assistance directly into your Zotero reference manager. Query, summarize, and analyze academic papers using your preferred LLM through MCP. Hermes-compatible research acceleration tool for academics and knowledge workers.

**Key capabilities:** Zotero integration, academic paper analysis, multi-LLM support (ChatGPT/Claude/DeepSeek/Grok), MCP-native, research workflow automation
**Related:** [MCP Guide →](/hermes/mcp/)

---

### PipRail
⭐ **community** · `TypeScript` · [github.com/piprail/piprail](https://github.com/piprail/piprail)

Open, self-custody x402 payment rail for AI agents  --  an SDK plus an MCP server that hands any MCP client a budget-bound wallet. 29 chains across 10 families (EVM, Solana, TON, Tron, NEAR, Sui, Aptos, Algorand, Stellar, XRPL). No backend, no custody, no protocol fee.

**Status:** Production  
**Key capabilities:** x402 payments, 29 chains, MCP server, budget-bound agent wallet, self-custody, no fee

---

### thebrierfox/the-stall
⭐ **community** · `Python` · [github.com/thebrierfox/the-stall](https://github.com/thebrierfox/the-stall)

209 pay-per-call data capabilities via x402 MCP. Monetized data access for autonomous agents.

**Status:** Production  
**Key capabilities:** Pay-per-call, 209 capabilities, x402 MCP, data monetization

---

### travisvn/awesome-claude-skills
⭐ **13,515** · [github.com/travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)

Curated list of Claude Skills, resources, and tools with community ratings. Excellent discovery resource for Hermes-compatible skills  --  browse hundreds of rated skills, extensions, and plugins that extend AI coding agents. Community-maintained quality scores help identify the most battle-tested and reliable skills for production use with Hermes Agent.

**Key capabilities:** Skill discovery, community ratings, curated resource list, Claude-to-Hermes cross-compatibility, quality-scored recommendations
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### agentskills/agentskills
⭐ **20,627** · [github.com/agentskills/agentskills](https://github.com/agentskills/agentskills)

Specification and documentation for the Agent Skills protocol  --  the standard reference for skill interoperability across AI agent platforms including Hermes, Claude Code, Cursor, and others. Defines the canonical skill manifest format, skill lifecycle (install → configure → execute → update → remove), cross-platform compatibility requirements, and best practices for skill authors targeting multiple agent ecosystems.

**Key capabilities:** Skill protocol specification, cross-platform interoperability, skill manifest standard, lifecycle definition, authoring best practices, Hermes-compatible standard
**Related:** [Skills Catalog →](/hermes/skills/catalog/) · [MCP Guide →](/hermes/mcp/)

---

### ComposioHQ/composio
⭐ **28,809** · [github.com/ComposioHQ/composio](https://github.com/ComposioHQ/composio)

1,000+ toolkits, tool search, context management, authentication, and sandboxed workbench for building AI agents. Comprehensive MCP integration platform with enterprise-grade tool management for Hermes Agent deployments.

**Maintainer:** Composio
**Key capabilities:** 1,000+ toolkits, tool search, context management, authentication, sandboxed workbench, MCP-native, Hermes-compatible
**Related:** [MCP Guide →](/hermes/mcp/)

---

### activepieces/activepieces
⭐ **22,794** · `TypeScript` · [github.com/activepieces/activepieces](https://github.com/activepieces/activepieces)

AI agents + MCPs + workflow automation platform with ~400 MCP servers. Open-source alternative showing how MCP integrates with business workflows  --  combines autonomous AI agents with a visual workflow builder and an extensive MCP ecosystem for connecting Hermes to hundreds of business tools. Demonstrates production MCP deployment patterns at scale across sales, marketing, operations, and support workflows.

**Maintainer:** Activepieces
**Key capabilities:** AI agents, ~400 MCP servers, workflow automation, visual builder, business integrations, open-source, Hermes-compatible
**Related:** [MCP Guide →](/hermes/mcp/) · [Infrastructure →](/hermes/infrastructure/)

---

### mystx-ai/mystx-skill-mcp
⭐ **57** · [github.com/mystx-ai/mystx-skill-mcp](https://github.com/mystx-ai/mystx-skill-mcp)

MCP server for agent skill management and discovery  --  Mystx AI's Model Context Protocol server enabling seamless skill installation, execution, and management across Hermes Agent and compatible platforms. Provides standardized skill lifecycle management through MCP with discovery, versioning, and cross-platform compatibility.

**Key capabilities:** MCP server, skill management, skill discovery, cross-platform, skill lifecycle, Hermes-compatible
**Related:** [MCP Guide →](/hermes/mcp/) · [Skills Catalog →](/hermes/skills/catalog/)

---

### cohnen/mcp-google-ads
⭐ **641** · `TypeScript` · [github.com/cohnen/mcp-google-ads](https://github.com/cohnen/mcp-google-ads)

MCP server for Google Ads  --  Model Context Protocol server providing autonomous agents with direct access to Google Ads campaign management, performance reporting, and optimization workflows. Enables Hermes Agent to read campaign metrics, analyze ad performance, manage keywords, and generate optimization recommendations through standardized MCP tool calls. Production-ready bridge between autonomous agents and the Google Ads platform for automated PPC management and reporting.

**Key capabilities:** Google Ads MCP server, campaign management, performance reporting, keyword analysis, PPC automation, Hermes-compatible
**Related:** [MCP Guide →](/hermes/mcp/) · [Integrations →](#-mcp--integrations)

---

### r-huijts/strava-mcp
⭐ **442** · `TypeScript` · [github.com/r-huijts/strava-mcp](https://github.com/r-huijts/strava-mcp)

MCP server for Strava  --  Model Context Protocol server connecting autonomous agents to Strava fitness data, activity tracking, and performance analytics. Grants Hermes Agent access to athlete profiles, activity logs, route data, segment leaderboards, and training metrics through standardized MCP tool calls. Enables agent-driven fitness analysis, training plan optimization, and performance insights from Strava's extensive activity database.

**Key capabilities:** Strava MCP server, fitness data access, activity tracking, training analytics, athlete profiles, Hermes-compatible
**Related:** [MCP Guide →](/hermes/mcp/) · [Integrations →](#-mcp--integrations)

---

### executeautomation/mcp-database-server
⭐ **358** · `TypeScript` · [github.com/executeautomation/mcp-database-server](https://github.com/executeautomation/mcp-database-server)

Database MCP server  --  universal Model Context Protocol server providing autonomous agents with SQL database access across PostgreSQL, MySQL, SQLite, and SQL Server. Enables Hermes Agent to execute queries, explore schemas, and analyze data through standardized MCP tool calls with built-in connection pooling, query sanitization, and result streaming. Production-ready database bridge for agent-driven data exploration, reporting, and ETL workflows.

**Key capabilities:** Database MCP server, SQL access, multi-database support, query execution, schema exploration, Hermes-compatible
**Related:** [MCP Guide →](/hermes/mcp/) · [Integrations →](#-mcp--integrations)

---

### aptro/superset-mcp
⭐ **186** · `TypeScript` · [github.com/aptro/superset-mcp](https://github.com/aptro/superset-mcp)

Apache Superset MCP server  --  Model Context Protocol server connecting autonomous agents to Apache Superset dashboards, charts, and data exploration capabilities. Enables Hermes Agent to query Superset datasets, retrieve chart data, list dashboards, and generate data visualizations through standardized MCP tool calls. Bridges the gap between autonomous agents and business intelligence platforms for agent-driven data analysis and reporting.

**Key capabilities:** Apache Superset MCP, BI integration, dashboard access, chart data retrieval, data exploration, Hermes-compatible
**Related:** [MCP Guide →](/hermes/mcp/) · [Integrations →](#-mcp--integrations)

---

### CodeGraphContext/CodeGraphContext
⭐ **3,775** · [github.com/CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext)

Code graph context for AI coding agents  --  provides structured code knowledge graphs that give agents deep understanding of codebase architecture, dependencies, and relationships. Enables Hermes Agent to navigate complex codebases with full architectural awareness through MCP.

**Key capabilities:** Code graph context, codebase architecture, dependency mapping, MCP-native, Hermes-compatible
**Related:** [MCP Guide →](/hermes/mcp/)

---

### getsentry/XcodeBuildMCP
⭐ **5,935** · [github.com/getsentry/XcodeBuildMCP](https://github.com/getsentry/XcodeBuildMCP)

Sentry Xcode Build MCP  --  Model Context Protocol server connecting autonomous agents to Xcode build systems and Sentry error monitoring. Enables Hermes Agent to trigger Xcode builds, monitor build status, retrieve build logs, and correlate build failures with Sentry error reports through standardized MCP tool calls.

**Maintainer:** Sentry
**Key capabilities:** Xcode build MCP, Sentry integration, build automation, error monitoring, iOS development, Hermes-compatible
**Related:** [MCP Guide →](/hermes/mcp/)

---

### IvanMurzak/Unity-MCP
⭐ **3,231** · [github.com/IvanMurzak/Unity-MCP](https://github.com/IvanMurzak/Unity-MCP)

Unity MCP server  --  Model Context Protocol server bridging autonomous agents with the Unity game engine. Enables Hermes Agent to control Unity Editor, manipulate game objects, manage scenes, trigger builds, and automate game development workflows through standardized MCP tool calls.

**Key capabilities:** Unity MCP, game engine integration, Unity Editor control, scene management, build automation, Hermes-compatible
**Related:** [MCP Guide →](/hermes/mcp/)

---

### ksimback/hermes-atlas-mcp
⭐ **6** · `JavaScript` · [https://github.com/ksimback/hermes-atlas-mcp](https://github.com/ksimback/hermes-atlas-mcp)

MCP server exposing the Hermes Atlas ecosystem catalog — 100+ Hermes Agent tools, skills, plugins, and integrations — to any MCP-aware client (Claude Desktop, Cursor, Continue).


---

### goagent123/hermes-composio-bridge
⭐ **0** · `Unknown` · [https://github.com/goagent123/hermes-composio-bridge](https://github.com/goagent123/hermes-composio-bridge)

Hermes Agent Composio MCP integration - connects Hermes to Composio for 1000+ tool integrations


---

### megberts/mcp-hermes-integration
⭐ **0** · `Shell` · [https://github.com/megberts/mcp-hermes-integration](https://github.com/megberts/mcp-hermes-integration)

Connect Hermes Agent to WebsitePublisher.ai via MCP — 59 tools for AI-powered web publishing

**Topics:** `hermes-agent`, `mcp`

---

### wottz-inc/shopify-hermes-oauth
⭐ **0** · `TypeScript` · [https://github.com/wottz-inc/shopify-hermes-oauth](https://github.com/wottz-inc/shopify-hermes-oauth)

Hermes-first Shopify OAuth connector for agent-safe multi-store access, read-only reporting, guardrails, audit logging, and MCP integration.

**Topics:** `agents`, `ecommerce`, `hermes-agent`, `mcp`, `oauth`, `shopify`

---

### LordVaderXIII/grok-connectors
⭐ **0** · `Unknown` · [https://github.com/LordVaderXIII/grok-connectors](https://github.com/LordVaderXIII/grok-connectors)

Collection of Grok/xAI tool connectors, MCP integrations, browser-to-api workflows, and utilities for agent systems like Hermes and OpenClaw. Self-hosted Unraid/Home Assistant compatible examples and docs.


---

## 🛠 Skills & Plugins

Extend Hermes with community-built skills and plugins.

### addyosmani/agent-skills
⭐ **61,368** · [github.com/addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

Production-grade engineering skills for AI coding agents  --  practical, battle-tested patterns for real-world agent deployments from Addy Osmani (Google Chrome engineering leader). Covers software architecture, performance optimization, testing strategies, code review automation, and DevOps workflows refined through production use. Essential skillset for Hermes Agent users building mission-critical software with agentic workflows backed by engineering best practices from one of the industry's most respected voices.

**Key capabilities:** Production-grade engineering, Addy Osmani, software architecture, performance optimization, testing strategies, DevOps, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### K-Dense-AI/scientific-agent-skills
⭐ **28,418** · [github.com/K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

160,000+ user scientific agent skills library  --  turn any AI agent into an AI Scientist. Massive collection of research-grade scientific skills covering hypothesis generation, experiment design, literature synthesis, data analysis, paper writing, and peer review workflows. Transforms Hermes Agent into a full-fledged scientific research assistant capable of accelerating discovery across disciplines from biology and chemistry to physics and computer science.

**Key capabilities:** 160K+ users, AI Scientist, research skills, hypothesis generation, experiment design, paper writing, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### vercel-labs/agent-skills
⭐ **28,004** · [github.com/vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)

Vercel's official collection of agent skills  --  production-tested patterns for agent deployments on Vercel's edge platform. Covers frontend development, API integration, deployment automation, performance monitoring, and edge computing workflows optimized for the Vercel ecosystem. Essential resource for Hermes Agent users deploying agentic applications at global scale with Vercel's infrastructure, combining the power of autonomous agents with world-class edge delivery.

**Key capabilities:** Official Vercel, production-tested, edge deployment, frontend development, API integration, deployment automation, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### phuryn/pm-skills
⭐ **19,057** · [github.com/phuryn/pm-skills](https://github.com/phuryn/pm-skills)

100+ agentic product management skills from discovery to launch  --  the complete PM toolkit for AI agents. Covers the full product lifecycle: market research, user story generation, PRD creation, roadmap planning, sprint management, stakeholder communication, and launch execution. Drop-in compatible with Hermes Agent for autonomous product management workflows that accelerate product development cycles from weeks to days.

**Key capabilities:** 100+ PM skills, product discovery, PRD generation, roadmap planning, sprint management, product lifecycle, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### wondelai/skills
⭐ **380+** · [github.com/wondelai/skills](https://github.com/wondelai/skills)

Cross-platform skills library that works with Hermes, Claude Code, and other agents. Actively maintained with growing catalog.

---

### NeoLabHQ/context-engineering-kit
⭐ **1,126** · [github.com/NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit)

Hand-crafted skills for dramatically improving agent result quality through context engineering  --  the art and science of providing AI agents with precisely the right context to produce superior outputs. Compatible with OpenCode, Cursor, and Hermes Agent. Elevate your agent's reasoning depth, accuracy, and output quality with context-optimized skill patterns designed by AI engineering experts who understand what agents need to succeed on complex, multi-step tasks.

**Key capabilities:** Context engineering, result quality optimization, hand-crafted skills, OpenCode/Cursor/Hermes compatible, reasoning improvement, output accuracy
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### VoltAgent/awesome-openclaw-skills
⭐ **50,309** · [github.com/VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)

Curated collection of 5,400+ OpenClaw skills filtered from the official registry  --  the largest organized skill library in the agent ecosystem. Browse, discover, and install production-ready skills for automation, content creation, development, and business operations. Hermes-compatible with direct migration path for OpenClaw skills.

**Key capabilities:** 5,400+ skills, curated registry, production-ready, OpenClaw-to-Hermes migration, community-vetted
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

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

### davila7/claude-code-skill-pornhub
⭐ **86** · [github.com/davila7/claude-code-skill-pornhub](https://github.com/davila7/claude-code-skill-pornhub)

Claude Code skill integrating Pornhub platform capabilities  --  enables AI coding agents to interact with Pornhub's API for content discovery, metadata retrieval, and platform automation. Cross-compatible with Hermes Agent for automated content workflows and platform integrations.

**Key capabilities:** Pornhub API integration, content discovery, Claude Code skill, platform automation, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### jnMetaCode/superpowers-zh
⭐ **5,450** · [github.com/jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh)

AI coding superpowers  --  Chinese enhanced edition. 6 original Chinese skills for Hermes Agent, Claude Code, Cursor, Copilot and other tools.

---

### jnMetaCode/agency-agents-zh
⭐ **15,046** · [github.com/jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh)

216 plug-and-play AI expert roles  --  supports Hermes Agent, Claude Code, Cursor, Copilot and 17 other tools. Covers engineering, design, marketing, finance, and more.

---

### kepano/obsidian-skills
⭐ **35,869** · `TypeScript` · [github.com/kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)

Agent skills for Obsidian by Kepano  --  teach Hermes agents to read, write, and navigate Obsidian vaults using CLI and Markdown. Unlock your second brain for autonomous agents: query notes, create linked documents, manage daily notes, and execute Obsidian commands through natural language. Essential bridge between personal knowledge management and agent workflows.

**Key capabilities:** Obsidian vault integration, Markdown-native, CLI automation, knowledge graph access, daily notes, personal knowledge management
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### GarethManning/education-agent-skills
⭐ **320** · [github.com/GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills)

165 evidence-based education skills for Claude, Codex, and Hermes Agent  --  pedagogically sound teaching workflows grounded in educational research. Lesson planning, student assessment, curriculum design, differentiated instruction, and classroom management skills built on proven instructional methodologies.

**Key capabilities:** 165 education skills, evidence-based pedagogy, lesson planning, curriculum design, Claude/Codex/Hermes compatible, instructional design
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

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

Research skills for Hermes Agent  --  paper discovery, archiving, reading, and synthesis.

---

### Undermybelt/hermes-skills-research
⭐ **0** · [github.com/Undermybelt/hermes-skills-research](https://github.com/Undermybelt/hermes-skills-research)

Hermes Agent research skills  --  paper discovery, literature review, academic research workflows.

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

Chinese social media content automation skillpack for Hermes Agent  --  voice modeling, AI-powered ideation, automated writing, and cross-platform social posting. Streamline your Xiaohongshu, Weibo, and Douyin content workflow with agent-driven content creation.

**Status:** Beta  
**Key capabilities:** Social media automation, Chinese platforms, voice cloning, AI content writing, multi-platform posting

---

### baipai012-lang/xhs-hot-topic-to-post
⭐ **0** · `Python` · [github.com/baipai012-lang/xhs-hot-topic-to-post](https://github.com/baipai012-lang/xhs-hot-topic-to-post)

End-to-end Xiaohongshu (RED) hot topic content pipeline  --  tracks trending topics on Xiaohongshu in real-time, generates AI-powered content drafts, and publishes directly to the platform. Closing the loop from trend discovery to content publishing for Hermes-powered social media automation.

**Status:** Beta  
**Key capabilities:** Xiaohongshu trending, hot topic tracking, AI content generation, social publishing pipeline, RED platform

---

### charlieaiworker/telegram-topic-setup-skill
⭐ **0** · `Python` · [github.com/charlieaiworker/telegram-topic-setup-skill](https://github.com/charlieaiworker/telegram-topic-setup-skill)

Telegram forum topic bootstrap skill for Hermes Agent  --  automatically initializes workspace memory files and project folder structures when a new Telegram forum topic is created. Keeps agent context organized per-topic with zero manual setup, ideal for topic-based agent workspaces.

**Status:** Beta  
**Key capabilities:** Telegram topics, workspace initialization, memory bootstrapping, project scaffolding, topic organization

---

### lijeuki/Hermes-Lark-Topic-Manager
⭐ **0** · `Python` · [github.com/lijeuki/Hermes-Lark-Topic-Manager](https://github.com/lijeuki/Hermes-Lark-Topic-Manager)

Feishu/Lark group chat management skill for Hermes Agent  --  threaded discussion tracking, message organization, and group chat management. Bring Hermes-powered AI intelligence to your Feishu team collaboration spaces with automated topic threading.

**Status:** Beta  
**Key capabilities:** Feishu integration, Lark platform, group chat management, threaded discussions, team collaboration

---

### huxiaoqiao/flint-hot-topic-tracker-skill
⭐ **0** · `Python` · [github.com/huxiaoqiao/flint-hot-topic-tracker-skill](https://github.com/huxiaoqiao/flint-hot-topic-tracker-skill)

Weibo trending and Toutiao headline tracker skill for Hermes Agent  --  monitors Weibo hot search rankings, Toutiao top stories, and Baidu index rising topics in real-time. Social media trend intelligence for content creators, marketers, and brand strategists.

**Status:** Beta  
**Key capabilities:** Weibo trending, Toutiao headlines, Baidu index, hot topic monitoring, Chinese social trends

---

### huxiaoqiao/dusk-hot-topic-tracker-skill
⭐ **0** · `Python` · [github.com/huxiaoqiao/dusk-hot-topic-tracker-skill](https://github.com/huxiaoqiao/dusk-hot-topic-tracker-skill)

Multi-platform hot topic tracker skill for Hermes Agent  --  aggregates trending content from multiple Chinese social platforms into a unified trend dashboard. Discover what's hot across platforms before it peaks, enabling timely content creation.

**Status:** Beta  
**Key capabilities:** Multi-platform tracking, hot topic aggregation, trend discovery, cross-platform monitoring, content timing

---

### huxiaoqiao/cove-hot-topic-tracker-skill
⭐ **0** · `Python` · [github.com/huxiaoqiao/cove-hot-topic-tracker-skill](https://github.com/huxiaoqiao/cove-hot-topic-tracker-skill)

Multi-platform hot topic tracking and content intelligence skill for Hermes Agent  --  continuous monitoring of trending topics across social media platforms with AI-powered trend analysis and content opportunity scoring. Stay ahead of viral trends across multiple Chinese platforms.

**Status:** Beta  
**Key capabilities:** Hot topic tracking, trend intelligence, content opportunity scoring, multi-platform monitoring, viral trend detection

---

### Atemndobs/hermes-plugins-hub
⭐ **1** · [github.com/Atemndobs/hermes-plugins-hub](https://github.com/Atemndobs/hermes-plugins-hub)

Community directory for Hermes Agent plugins  --  auto-indexed from GitHub topic tags for seamless plugin discovery. Search, browse, and discover community-built Hermes Agent extensions, skills, and integrations in one centralized, searchable hub.

**Status:** Beta  
**Key capabilities:** Plugin discovery, community directory, GitHub-indexed, plugin search, extension catalog

---

### Jeffallan/claude-skills
⭐ **9,949** · [github.com/Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills)

66 specialized skills for full-stack developers  --  production patterns for agent development. Comprehensive skill library covering frontend frameworks (React, Vue, Svelte), backend stacks (Node.js, Python, Go), database optimization, CI/CD pipelines, cloud deployment patterns, and testing strategies. Each skill follows battle-tested production patterns refined through real-world full-stack development. Drop-in compatible with Hermes Agent for accelerating full-stack development workflows with agentic assistance.

**Key capabilities:** 66 full-stack skills, React/Vue/Svelte, Node.js/Python/Go, CI/CD pipelines, cloud deployment, production patterns, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### AgriciDaniel/claude-seo
⭐ **9,080** · [github.com/AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)

Universal SEO skill for AI agents with 25 sub-skills and 18 sub-agents covering technical SEO, E-E-A-T optimization, content strategy, keyword research, on-page optimization, link building, and performance analytics. Transforms Hermes Agent into a comprehensive SEO automation platform  --  audit sites, generate optimized content, track rankings, analyze competitors, and implement technical SEO fixes through agentic workflows. Modular sub-agent architecture enables parallel SEO task execution across multiple domains.

**Key capabilities:** 25 sub-skills, 18 sub-agents, technical SEO, E-E-A-T optimization, content strategy, keyword research, rank tracking, competitor analysis, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### zubair-trabzada/geo-seo-claude
⭐ **8,179** · [github.com/zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude)

GEO-first SEO skill for AI agents  --  comprehensive AI search optimization for any website with citability scoring. Built for the Generative Engine Optimization era: optimize content for AI-powered search engines (Google SGE, Perplexity, ChatGPT Search) with proprietary citability scoring that measures how likely your content is to be cited by AI-generated answers. Includes brand authority building, structured data optimization, AI-friendly content formatting, and citation-worthiness analysis. Essential for Hermes Agent users optimizing content for the AI-search landscape.

**Key capabilities:** GEO-first optimization, citability scoring, AI search optimization, Google SGE, Perplexity, brand authority, structured data, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### Orchestra-Research/AI-Research-SKILLs
⭐ **9,769** · [github.com/Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)

Comprehensive open-source library of AI research and engineering skills for any agent platform. Covers the full AI research lifecycle: literature review automation, experiment design, hyperparameter optimization, model training orchestration, ablation studies, result analysis, and paper writing. Research-grade skills developed by the Orchestra Research team for accelerating AI R&D workflows with agentic assistance. Drop-in compatible with Hermes Agent for AI researchers and ML engineers.

**Key capabilities:** AI research library, literature review, experiment design, hyperparameter optimization, model training, ablation studies, paper writing, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### Imbad0202/academic-research-skills
⭐ **32,144** · [github.com/Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)

Academic research skills pipeline: research → write → review → revise → finalize for AI agents. Complete academic writing workflow automated through agentic skills  --  from initial literature survey and source evaluation through drafting, peer review simulation, revision cycles, and final manuscript preparation. Supports multiple citation styles (APA, MLA, Chicago, IEEE), LaTeX formatting, figure/table generation, and journal-specific submission formatting. One of the most popular academic agent skills, trusted by 32K+ researchers.

**Key capabilities:** Research pipeline, writing workflow, peer review simulation, multi-citation styles, LaTeX formatting, journal submission, 32K+ users, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### blader/humanizer
⭐ **24,563** · [github.com/blader/humanizer](https://github.com/blader/humanizer)

Agent skill that removes signs of AI-generated writing from text  --  humanizes content by adjusting tone, cadence, vocabulary variation, sentence structure diversity, and stylistic naturalness. Goes beyond simple paraphrasing to analyze and transform AI writing patterns into authentically human-sounding prose while preserving meaning, accuracy, and factual content. Essential for Hermes content agents producing blog posts, marketing copy, emails, social media, and any customer-facing content where natural human voice matters.

**Key capabilities:** AI text humanization, tone adjustment, cadence variation, vocabulary diversity, style transformation, content authenticity, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### Donchitos/Claude-Code-Game-Studios
⭐ **21,773** · [github.com/Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)

Turn Claude Code into a full game development studio with 49 AI agents, 72 workflow skills, and coordination system. Comprehensive game development pipeline: concept design, prototyping, 3D modeling assistance, shader programming, level design, playtesting automation, sound design, and build/deploy orchestration. The 49 specialized agents collaborate through a coordination layer that manages dependencies, merge conflicts, and asset pipelines. Adaptable for Hermes Agent to power end-to-end game development with agentic workflows.

**Key capabilities:** 49 AI agents, 72 workflow skills, game dev pipeline, concept to deploy, 3D modeling, shader programming, level design, coordination system, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### SamurAIGPT/Generative-Media-Skills
⭐ **3,566** · `Python` · [github.com/SamurAIGPT/Generative-Media-Skills](https://github.com/SamurAIGPT/Generative-Media-Skills)

Multi-modal Generative Media Skills  --  comprehensive skill pack enabling Hermes Agent to create, edit, and transform images, video, audio, and 3D content. Covers AI image generation (Stable Diffusion, DALL-E, Midjourney APIs), video editing and generation, audio synthesis and voice cloning, 3D model creation, and media pipeline automation. Transforms Hermes into a full creative media studio capable of producing professional-grade multi-modal content with agent-driven workflows.

**Key capabilities:** Multi-modal generation, image/video/audio/3D, Stable Diffusion, DALL-E, media pipeline automation, creative studio, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### Gentleman-Programming/Gentleman-Skills
⭐ **556** · `Python` · [github.com/Gentleman-Programming/Gentleman-Skills](https://github.com/Gentleman-Programming/Gentleman-Skills)

Community-driven Claude Code skills  --  a growing collection of practical, peer-reviewed skills for AI coding agents. Covers software development best practices, code review automation, testing strategies, documentation generation, and DevOps workflows. Community-maintained with active contributions and real-world testing across Claude Code, Hermes Agent, and compatible platforms. Designed to be drop-in compatible with Hermes skill system for immediate productivity gains.

**Key capabilities:** Community-driven, peer-reviewed, software development, code review, testing, DevOps, Claude Code/Hermes compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### nextlevelbuilder/ui-ux-pro-max-skill
⭐ **93,501** · [github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

UI/UX Pro Max skill for AI agents  --  a comprehensive design and prototyping toolkit that transforms autonomous agents into full-stack design partners. Covers design systems architecture, component library generation, accessibility pattern enforcement, responsive layout design, user research synthesis, design token management, and Figma-to-code workflows. Drop-in compatible with Hermes Agent for professional-grade UI/UX design capabilities including automated design audits, accessibility compliance checking, and production-ready component code generation across React, Vue, and Svelte frameworks.

**Key capabilities:** UI/UX design skill, design systems, accessibility patterns, component architecture, Figma integration, responsive design, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### binance/binance-skills-hub
⭐ **904** · [github.com/binance/binance-skills-hub](https://github.com/binance/binance-skills-hub)

Binance Skills Hub  --  official collection of agent skills from Binance for cryptocurrency trading, market analysis, blockchain data access, and DeFi workflow automation. Provides Hermes Agent with production-grade access to Binance APIs, market data streams, portfolio management, and trading strategy execution through well-structured, audited skill modules. Enterprise-grade skills for autonomous agents operating in crypto and blockchain domains with built-in rate limiting, error handling, and security best practices.

**Key capabilities:** Binance skills, crypto trading, market analysis, blockchain data, DeFi automation, enterprise-grade, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### CYC2002tommy/Deep-Research-Agent
⭐ **58** · `JavaScript` · [https://github.com/CYC2002tommy/Deep-Research-Agent](https://github.com/CYC2002tommy/Deep-Research-Agent)

This is a skill that can be used for most of the agentic AI, which enables your Hermes, Openclaw ...etc to look for a bunch of papers based on your research plan. It will access to scopus by the scopus mcp, and OpenAlex api ...etc


---

### uzairansaruzi/robinhood-agent-skill
⭐ **30** · `Python` · [https://github.com/uzairansaruzi/robinhood-agent-skill](https://github.com/uzairansaruzi/robinhood-agent-skill)

Robinhood portfolio advisor skill for Hermes Agent, OpenClaw, Claude Code, Codex, and other MCP-compatible AI agents


---

### LYAKAKOY/Hermes-Codex-Plugin
⭐ **15** · `Python` · [https://github.com/LYAKAKOY/Hermes-Codex-Plugin](https://github.com/LYAKAKOY/Hermes-Codex-Plugin)

Local-first memory, recall, and skill evolution plugin for Codex agents.

**Topics:** `agent-memory`, `ai-agent`, `codex`, `codex-plugin`, `developer-tools`, `fts5`, `mcp`, `memory`

---

### agentchatme/agentchat-hermes
⭐ **12** · `Python` · [https://github.com/agentchatme/agentchat-hermes](https://github.com/agentchatme/agentchat-hermes)

AgentChat platform plugin for Nous Research's Hermes Agent runtime — peer-to-peer messaging for autonomous agents over WebSocket. Bundles the agent etiquette skill. (PyPI: agentchatme-hermes)


---

### roach88/hermetic
⭐ **2** · `Python` · [https://github.com/roach88/hermetic](https://github.com/roach88/hermetic)

Sync Claude Code plugins into Hermes as native skills and delegation skills.


---

### Guoen0/xiaoduiyou-public
⭐ **2** · `Python` · [https://github.com/Guoen0/xiaoduiyou-public](https://github.com/Guoen0/xiaoduiyou-public)

Public Xiaoduiyou Agent plugins and skills for Hermes and OpenClaw


---

### dexter7wolf/telegram-file-sender
⭐ **2** · `Unknown` · [https://github.com/dexter7wolf/telegram-file-sender](https://github.com/dexter7wolf/telegram-file-sender)

Hermes Agent skill/plugin per inviare file locali su Telegram


---

### jinlio/feishu-table-patch
⭐ **2** · `Python` · [https://github.com/jinlio/feishu-table-patch](https://github.com/jinlio/feishu-table-patch)

A Hermes skill plugin that converts Markdown (tables + rich text) to Feishu card messages via Schema 2.0 + tag:markdown


---

### verkyyi/agentfeeds-hermes-plugin
⭐ **1** · `Python` · [https://github.com/verkyyi/agentfeeds-hermes-plugin](https://github.com/verkyyi/agentfeeds-hermes-plugin)

Hermes plugin and skill for Agent Feeds


---

### poogas/hermes-skill-installer
⭐ **1** · `JavaScript` · [https://github.com/poogas/hermes-skill-installer](https://github.com/poogas/hermes-skill-installer)

Skill installer plugin for Hermes Agent


---

## 🛠 Tools & Utilities

Development tools, utilities, and platforms for the Hermes ecosystem.

### WEIFENG2333/phistory
⭐ **340** · `HTML` · [github.com/WEIFENG2333/phistory](https://github.com/WEIFENG2333/phistory)

Phistory automatically archives versioned system prompt snapshots from agent CLIs like Claude Code, Codex, OpenClaw, and Hermes. Tracks prompt evolution over time, enabling diff-based analysis of how agent behavior changes with prompt modifications. Essential for prompt engineering and agent debugging workflows.

**Maintainer:** WEIFENG2333
**Key capabilities:** Prompt snapshot archiving, versioned system prompt history, multi-agent CLI support (Claude Code/Codex/OpenClaw/Hermes), diff-based prompt analysis, agent debugging

---

### danny-avila/LibreChat
⭐ **39,302** · `TypeScript` · [github.com/danny-avila/LibreChat](https://github.com/danny-avila/LibreChat)

Enhanced ChatGPT clone featuring Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI  --  a full-featured, open-source chat platform with native MCP support that's fully compatible with Hermes Agent. Deploy your own AI chat interface with built-in agent orchestration, skill execution, and multi-model routing. The MCP-native architecture makes it a natural companion for Hermes Agent deployments, providing a polished chat UI with enterprise-grade features including file handling, code execution, and multi-modal support.

**Key capabilities:** MCP-native, multi-model (DeepSeek/Anthropic/AWS/OpenAI), agent orchestration, skill execution, open-source chat platform, Hermes-compatible
**Related:** [MCP Guide →](/hermes/mcp/)

---

### vercel-labs/skills
⭐ **22,616** · `TypeScript` · [github.com/vercel-labs/skills](https://github.com/vercel-labs/skills)

The open agent skills tool  --  `npx skills` CLI for installing and managing agent skills across platforms. One-command skill installation and management for Hermes Agent, Claude Code, Cursor, and other AI coding agents. Vercel's official skills CLI provides a unified interface for discovering, installing, updating, and removing agent skills with dependency resolution and version management. Streamline your Hermes Agent skill workflow with the industry-standard skills package manager.

**Key capabilities:** npx skills CLI, cross-platform skill management, install/update/remove, Vercel official, dependency resolution, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### wanshuiyin/Auto-claude-code-research-in-sleep
⭐ **12,280** · `Python` · [github.com/wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

Lightweight Marathon AI Dev Runner  --  autonomous coding agent that runs continuous development sessions with automatic context management, checkpoint recovery, and sleep/wake cycle optimization for long-running AI coding tasks. Designed for marathon coding sessions where agents work through complex multi-hour development workflows without losing context or momentum. Drop-in compatible with Hermes Agent for autonomous development that runs while you sleep  --  wake up to completed features, passing tests, and merged PRs.

**Key capabilities:** Marathon coding, autonomous development, context management, checkpoint recovery, continuous sessions, sleep/wake optimization, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### diegosouzapw/OmniRoute
⭐ **6,449** · `TypeScript` · [github.com/diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)

Free AI gateway: one endpoint, multiple models  --  unified API gateway providing a single endpoint to access dozens of AI models from OpenAI, Anthropic, Google, Meta, DeepSeek, and more. Intelligent model routing with automatic fallback, load balancing, and cost optimization across providers. Hermes Agent users gain seamless multi-model access without managing multiple API keys or provider-specific SDKs  --  route any agent request to the optimal model based on cost, capability, or availability.

**Key capabilities:** Unified AI gateway, multi-model routing, automatic fallback, load balancing, cost optimization, single endpoint, Hermes-compatible
**Related:** [MCP Guide →](/hermes/mcp/)

---

### bitrouter/bitrouter
⭐ **203** · `Rust` · [github.com/bitrouter/bitrouter](https://github.com/bitrouter/bitrouter)

Context-aware agentic LLM gateway and router that optimizes agentic workflows with every run. Works with any harness (Hermes Agent, Claude Code, Codex, OpenCode), any model (OpenAI-compatible, Anthropic-compatible, LiteLLM), and any loop. Features ACP-native routing, agent observability, guardrails, and MCP integration — all in a high-performance Rust binary.

**Maintainer:** [bitrouter](https://github.com/bitrouter)
**Key capabilities:** LLM gateway, agentic routing, ACP-native, multi-harness, multi-model, agent observability, guardrails, MCP integration, Rust
**Related:** [MCP Guide →](/hermes/mcp/) · [Orchestration →](#-orchestration-multi-agent--swarms)

---

### ThinkInAIXYZ/deepchat
⭐ **6,023** · `TypeScript` · [github.com/ThinkInAIXYZ/deepchat](https://github.com/ThinkInAIXYZ/deepchat)

Smart assistant connecting powerful AI models  --  universal chat interface that bridges multiple AI models into a single, intelligent conversation experience. Supports DeepSeek, Anthropic Claude, OpenAI GPT, Google Gemini, and open-source models with context-aware model switching, conversation history management, and multi-modal capabilities. Designed as a companion interface for Hermes Agent deployments, providing a polished chat experience with smart model selection that routes queries to the best available model.

**Key capabilities:** Multi-model chat, DeepSeek/Claude/GPT/Gemini, context-aware routing, conversation management, multi-modal, Hermes-compatible
**Related:** [UI & Dashboards →](#-ui--dashboards)

---

### netease-youdao/LobsterAI
⭐ **5,304** · `Python` · [github.com/netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI)

Desktop-grade AI agent for real work  --  NetEase Youdao's production AI agent designed for professional desktop workflows including document processing, data analysis, research synthesis, and automated reporting. Built with enterprise reliability standards for handling real business tasks with accuracy and reproducibility. Integrates with Hermes Agent for extended autonomous workflow capabilities in professional environments where quality and consistency are paramount.

**Maintainer:** NetEase Youdao
**Key capabilities:** Desktop AI agent, document processing, data analysis, research synthesis, enterprise-grade, NetEase Youdao, Hermes-compatible
**Related:** [Tools & Utilities →](#-tools--utilities)

---

### numman-ali/n-skills
⭐ **997** · [github.com/numman-ali/n-skills](https://github.com/numman-ali/n-skills)

Curated plugin marketplace for AI agents  --  discover, install, and manage plugins across agent frameworks. Works natively with Claude Code, Codex, and Hermes Agent, providing a unified plugin discovery layer for expanding agent capabilities. Browse community-vetted plugins organized by category with verified compatibility ratings for Hermes Agent production deployments.

**Key capabilities:** Plugin marketplace, curated plugins, Claude Code/Codex/Hermes compatible, plugin discovery, community-vetted, multi-framework
**Related:** Plugins

---

### data-goblin/power-bi-agentic-development
⭐ **707** · [github.com/data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)

Power BI AI skills and agents for business intelligence automation  --  teach Hermes Agent to build, manage, and optimize Power BI dashboards, reports, and data models. Autonomous BI development: from data source connection to visualization design, DAX optimization, and automated report generation. Transform your business intelligence workflow with agentic Power BI development that turns days of manual BI work into minutes of agent execution.

**Key capabilities:** Power BI automation, dashboard generation, DAX optimization, BI agents, report automation, data modeling, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### microsoft/power-platform-skills
⭐ **363** · [github.com/microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)

Official Microsoft Power Platform plugins for Claude Code and agents  --  Microsoft's own skill package extending agent capabilities across Power Automate, Power Apps, Power BI, and Power Virtual Agents. Enterprise-grade, Microsoft-maintained skills with native Hermes Agent compatibility for organizations building agentic workflows on the Power Platform ecosystem.

**Key capabilities:** Power Platform integration, Power Automate, Power Apps, Power BI, official Microsoft, enterprise-grade, Hermes-compatible
**Related:** [MCP Guide →](/hermes/mcp/) · [Skills Catalog →](/hermes/skills/catalog/)

---

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

Code graph and intelligence engine that cuts AI coding agent token usage up to 50×. Indexes 257 languages across multiple repos, exposes via CLI, MCP server, and web UI. Native Hermes integration with 20 built-in skills. Sub-millisecond impact analysis, cross-repo call chains, zero external dependencies  --  single Go binary.

**Status:** Production  
**Key capabilities:** Token optimization (50×), 257 languages, MCP server, Hermes native, cross-repo graph

---

### ivan-szz/hermes-newsletter-script
⭐ **1** · `Rust` · [github.com/ivan-szz/hermes-newsletter-script](https://github.com/ivan-szz/hermes-newsletter-script)

Zero-config Rust CLI for aggregating tech news from 11 sources with intelligent topic filtering  --  Hacker News, Reddit, Dev.to, Lobsters, and more. Compiles AI-curated newsletters with topic-aware article selection and formatting, ready for Hermes Agent integration into daily content workflows.

**Status:** Beta  
**Key capabilities:** Tech news aggregation, 11 sources, Rust CLI, topic filtering, AI newsletter generation

---

### thiswind/hermes-cursor-compressor
⭐ **1** · `Python` · [github.com/thiswind/hermes-cursor-compressor](https://github.com/thiswind/hermes-cursor-compressor)

Cursor-style context compression for Hermes Agent  --  fixes topic drift with minimal summarization that preserves semantic coherence. Intelligently compresses conversation context to reduce token consumption while maintaining task-relevant focus across long-running agent sessions and multi-topic conversations.

**Status:** Beta  
**Key capabilities:** Context compression, topic drift prevention, token optimization, semantic summarization, Cursor-style compression

---

### srmdn/hermes-agent-kit
⭐ **0** · `Python` · [github.com/srmdn/hermes-agent-kit](https://github.com/srmdn/hermes-agent-kit)

Production hardening pack for Hermes Agent  --  per-topic model routing, intelligent fallback chains, rate limiting, cost control, and operational guardrails. Essential toolkit for running Hermes reliably in production environments at scale with built-in reliability patterns.

**Status:** Beta  
**Key capabilities:** Production hardening, model routing, fallback chains, rate limiting, cost control, per-topic routing

---

### 0xNekr/hermes-topic-router
⭐ **0** · `Python` · [github.com/0xNekr/hermes-topic-router](https://github.com/0xNekr/hermes-topic-router)

Auto-route LLM models per chat topic for Hermes Agent  --  one bot, multiple models, zero manual switching. Intelligently selects the optimal language model based on conversation topic classification, balancing cost efficiency and capability automatically across all your agent conversations.

**Status:** Beta  
**Key capabilities:** Topic-based routing, model selection, automatic switching, multi-model orchestration, cost optimization

---

### robbyczgw-cla/hermes-topic-monitor
⭐ **2** · `Python` · [github.com/robbyczgw-cla/hermes-topic-monitor](https://github.com/robbyczgw-cla/hermes-topic-monitor)

Proactive topic monitoring with AI importance scoring on a schedule  --  continuously scans conversation topics and surfaces high-priority items before they're missed. Scheduled intelligence that keeps your Hermes Agent focused on what matters most across all active discussions.

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

Classify, rename, and tidy Hermes Agent session titles into coherent topic groups  --  automated session organization that turns messy chat histories into a well-structured, searchable knowledge base. Perfect for agents handling dozens of concurrent conversations across multiple topics.

**Status:** Beta  
**Key capabilities:** Session classification, topic grouping, auto-renaming, session organization, knowledge structuring

---

### lecharles/hermes-framework-lab
⭐ **0** · `Python` · [github.com/lecharles/hermes-framework-lab](https://github.com/lecharles/hermes-framework-lab)

Running and evaluating Hermes Agent in Telegram topic-based lanes  --  experimentation framework for testing agent performance across isolated discussion threads. Benchmark agent behavior in structured topic environments for production tuning and capability evaluation.

**Status:** Beta  
**Key capabilities:** Telegram topic lanes, agent evaluation, performance benchmarking, experimental framework, topic isolation

---

### VasiHemanth/tokentelemetry
⭐ **118** · `Python` · [github.com/VasiHemanth/tokentelemetry](https://github.com/VasiHemanth/tokentelemetry)

Token telemetry dashboard for autonomous AI agents  --  track token consumption, session costs, and tool call patterns across providers in real-time. Monitor Hermes Agent spend with per-session breakdowns, provider-level analytics, and usage trend visualization. Essential cost observability for production agent deployments running 24/7.

**Key capabilities:** Token tracking, cost monitoring, session analytics, multi-provider telemetry, tool call metrics, usage dashboards
**Related:** [Infrastructure →](/hermes/infrastructure/)

---

### OthmanAdi/planning-with-files
⭐ **23,451** · `Markdown` · [github.com/OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)

Persistent file-based planning for AI coding agents with crash-proof markdown state  --  the definitive planning pattern for Hermes Agent, Claude Code, Codex, and Cursor. Maintains structured task plans across sessions using filesystem-backed state that survives crashes, context loss, and session restarts. Enables long-running multi-session agent projects with full progress tracking, task decomposition, and plan continuity across agent restarts.

**Status:** Production
**Key capabilities:** File-based planning, crash-proof state, multi-session continuity, task decomposition, progress tracking, markdown-native, cross-agent compatible
**Related:** [Governance →](/hermes/governance/)

---

### stainlu/hermes-labyrinth
⭐ **286** · `Python` · [github.com/stainlu/hermes-labyrinth](https://github.com/stainlu/hermes-labyrinth)

Read-only observability plugin for Hermes Agent  --  journeys, crossings, guideposts, and reports. Zero-intrusion monitoring that tracks agent decision paths through conversation space without modifying agent behavior. Maps agent reasoning trails as navigable journeys with annotated crossing points, milestone guideposts, and comprehensive session reports for auditing, debugging, and performance optimization of autonomous agent workflows in production.

**Status:** Beta
**Key capabilities:** Read-only observability, agent journey tracking, decision path mapping, session reports, zero-intrusion monitoring, auditing, performance debugging, Hermes-native plugin
**Related:** [Infrastructure →](/hermes/infrastructure/)

---

### mksglu/context-mode
⭐ **17,610** · [github.com/mksglu/context-mode](https://github.com/mksglu/context-mode)

Context window optimization for AI coding agents  --  sandboxes tool output with 98% reduction across 15 platforms. Dramatically reduces context window consumption by intelligently filtering, summarizing, and compressing tool call outputs before they enter the agent's context. Supports Hermes Agent, Claude Code, Cursor, Windsurf, Copilot, and 10+ other AI coding platforms. Critical utility for long-running agent sessions, multi-file refactors, large codebase navigation, and any workflow where context window exhaustion limits agent performance. Achieves 98% token reduction while preserving actionable information.

**Key capabilities:** Context window optimization, 98% output reduction, tool output sandboxing, 15-platform support, token compression, long-session optimization, Hermes-compatible
**Related:** [Infrastructure →](/hermes/infrastructure/)

---

### chopratejas/headroom
⭐ **30,163** · [github.com/chopratejas/headroom](https://github.com/chopratejas/headroom)

Compress tool outputs, logs, files, and RAG chunks before reaching the LLM. 60-95% fewer tokens, same answers. Essential cost optimization for Hermes agent deployments  --  dramatically reduces API costs while preserving output fidelity.

**Key capabilities:** Output compression, 60-95% token reduction, tool output optimization, log compression, RAG chunk optimization, cost reduction, Hermes-compatible
**Related:** [Infrastructure →](/hermes/infrastructure/)

---

### jarrodwatts/claude-hud
⭐ **25,311** · [github.com/jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)

Claude Code plugin showing context usage, active tools, running agents, and system state in a heads-up display. Transparency patterns transferable to Hermes agent monitoring  --  provides real-time visibility into agent resource consumption, tool execution status, active sub-agent count, and system health metrics. An essential observability pattern for production Hermes deployments requiring deep agent introspection.

**Key capabilities:** Agent HUD, context usage monitoring, tool execution tracking, system state visibility, agent introspection, production observability, Hermes-applicable patterns
**Related:** [Infrastructure →](/hermes/infrastructure/) · [Architecture →](/hermes/architecture/)

---

### kwaozz/haha
⭐ **77** · [github.com/kwaozz/haha](https://github.com/kwaozz/haha)

Lightweight utility toolkit for AI coding agents  --  fun and practical tools for enhancing agent interactions with humor, creative outputs, and engaging user experiences. Compatible with Hermes Agent for adding personality and entertainment capabilities to autonomous agent workflows.

**Key capabilities:** Agent utility toolkit, creative tools, humor generation, entertainment, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### liyishu2626/aicode
⭐ **73** · [github.com/liyishu2626/aicode](https://github.com/liyishu2626/aicode)

AI-powered coding assistant and code generation tool  --  intelligent code completion, refactoring, and generation with support for multiple programming languages and frameworks. Integrates with Hermes Agent for autonomous coding workflows, code review automation, and AI-driven software development pipelines.

**Key capabilities:** AI coding assistant, code generation, multi-language support, code refactoring, autonomous coding, Hermes-compatible
**Related:** [Skills Catalog →](/hermes/skills/catalog/)

---

### safishamsi/graphify
⭐ **69,067** · [github.com/safishamsi/graphify](https://github.com/safishamsi/graphify)

Graphify  --  advanced graph visualization and analysis platform for AI agent ecosystems. Create interactive knowledge graphs, dependency visualizations, network topology maps, and relational data diagrams that illuminate agent workflows, code architectures, and data relationships. Generates publication-quality interactive visualizations with D3.js and WebGL rendering. Essential for Hermes Agent users building complex systems  --  map agent decision trees, skill dependency chains, MCP connection graphs, and multi-agent communication topologies in real-time with drag-and-drop exploration, zoom/pan navigation, and export to PNG, SVG, and interactive HTML.

**Key capabilities:** Graph visualization, knowledge graphs, dependency mapping, network topology, D3.js rendering, interactive exploration, Hermes-compatible
**Related:** [Architecture →](/hermes/architecture/)

---

### vercel-labs/agent-browser
⭐ **36,372** · [github.com/vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)

Agent Browser by Vercel  --  production-grade browser automation agent for autonomous web interaction. Headless browser agent built on Playwright capable of navigating complex websites, filling multi-step forms, extracting structured data from dynamic pages, authenticating with login flows, handling JavaScript-rendered content, and executing multi-page web workflows. First-class integration with Hermes Agent for automated web scraping, form submission, e2e testing, and any browser-based task. Powers agent-driven web research, data collection, competitive analysis, and UI testing pipelines with enterprise reliability from Vercel's infrastructure team.

**Key capabilities:** Browser automation, Vercel, web interaction, Playwright, form automation, data extraction, Hermes-compatible
**Related:** [Tools & Utilities →](#-tools--utilities)

---

### Panniantong/Agent-Reach
⭐ **34,227** · [github.com/Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

Agent Reach  --  multi-platform agent communication and reach platform that extends autonomous agent capabilities across messaging platforms, web interfaces, and API endpoints. Provides a unified communication layer enabling Hermes Agent to interact through Discord, Telegram, Slack, WhatsApp, webhooks, REST APIs, and custom channels with consistent message formatting, attachment handling, and response routing. Built for production agent deployments requiring omnichannel presence  --  one agent, every platform, unified response handling with delivery guarantees and retry logic.

**Key capabilities:** Multi-platform agent reach, messaging gateway, Discord/Telegram/Slack/WhatsApp, webhook integration, unified communication, Hermes-compatible
**Related:** Messaging Gateway

---

### simstudioai/sim
⭐ **28,812** · [github.com/simstudioai/sim](https://github.com/simstudioai/sim)

Sim  --  AI agent simulation and testing platform for creating controlled environments to test, train, and evaluate autonomous agents. Build realistic scenario simulations with configurable environments, synthetic users, and measurable outcomes. Run Hermes Agent through simulated production scenarios before deployment  --  test edge cases, evaluate decision quality, measure task completion rates, and benchmark agent performance across varied conditions. Essential for teams building production agent systems that need rigorous pre-deployment validation and continuous performance regression testing.

**Key capabilities:** Agent simulation, testing platform, scenario generation, performance benchmarking, pre-deployment validation, Hermes-compatible
**Related:** [Benchmarks →](#-research--benchmarks)

---

### dtyq/magic
⭐ **4,862** · [github.com/dtyq/magic](https://github.com/dtyq/magic)

Magic  --  AI agent development platform with integrated tools, workflows, and deployment capabilities. Provides a unified development environment for building, testing, and deploying agent-based applications with built-in MCP support, skill management, and model routing. Streamlines the agent development lifecycle from prototype to production with visual workflow designer, debugging tools, and one-click deployment options compatible with Hermes Agent infrastructure.

**Key capabilities:** Agent development platform, integrated tools, visual workflows, MCP support, model routing, Hermes-compatible
**Related:** [Infrastructure →](/hermes/infrastructure/)

---

### golutra/golutra
⭐ **3,693** · [github.com/golutra/golutra](https://github.com/golutra/golutra)

Golutra  --  agent workflow and automation platform for orchestrating complex multi-step autonomous agent operations. Design, execute, and monitor agent workflows with branching logic, conditional execution, parallel task distribution, and error recovery patterns. Compatible with Hermes Agent for building production automation pipelines that handle everything from data processing and content generation to system administration and DevOps workflows with built-in observability and audit trails.

**Key capabilities:** Agent workflow platform, automation pipeline, branching logic, parallel execution, error recovery, Hermes-compatible
**Related:** [Orchestration →](#-orchestration-multi-agent--swarms)

---

### kevinluosl/deepbot
⭐ **2,355** · [github.com/kevinluosl/deepbot](https://github.com/kevinluosl/deepbot)

DeepBot  --  deep learning-powered AI bot framework for autonomous task execution with advanced reasoning capabilities. Combines transformer-based language understanding with structured task planning, tool orchestration, and iterative refinement loops. Drop-in compatible with Hermes Agent for enhanced autonomous agent workflows requiring deep reasoning, multi-step planning, and adaptive execution strategies across complex problem domains.

**Key capabilities:** Deep learning bot, autonomous execution, task planning, tool orchestration, iterative refinement, Hermes-compatible
**Related:** [Architecture →](/hermes/architecture/)

---

### nikilster/clawflows
⭐ **1,660** · [github.com/nikilster/clawflows](https://github.com/nikilster/clawflows)

Claw Flows  --  workflow automation patterns and templates for agent-based task execution, designed as reusable building blocks for common agent automation scenarios. Collection of proven workflow templates covering data pipeline automation, content generation pipelines, deployment workflows, monitoring and alerting patterns, and cross-system integration flows. Each template includes configuration, dependencies, error handling, and real-world usage examples  --  drop-in compatible with Hermes Agent for rapid automation prototyping and production deployment of agent-driven workflows.

**Key capabilities:** Workflow automation, agent templates, pipeline patterns, deployment workflows, monitoring patterns, Hermes-compatible
**Related:** [Orchestration →](#-orchestration-multi-agent--swarms)

---

### labring/FastGPT
⭐ **28,553** · `TypeScript` · [github.com/labring/FastGPT](https://github.com/labring/FastGPT)

FastGPT  --  high-performance GPT platform optimized for rapid knowledge base construction, AI-powered Q&A, and enterprise knowledge management. Provides a complete pipeline for building, training, and deploying custom GPT-powered applications with built-in data preprocessing, vector storage, workflow orchestration, and API integration. Drop-in compatible with Hermes Agent for enhanced knowledge retrieval, automated customer support, and intelligent documentation workflows with sub-second response times at scale.

**Key capabilities:** Fast GPT platform, knowledge base, AI Q&A, enterprise knowledge, vector storage, workflow orchestration, Hermes-compatible
**Related:** [Knowledge Architecture →](/hermes/knowledge/) · [Tools →](#-tools--utilities)

---

### deepset-ai/haystack
⭐ **25,613** · `Python` · [github.com/deepset-ai/haystack](https://github.com/deepset-ai/haystack)

Haystack  --  production-grade NLP framework for building search, question answering, and conversational AI systems. Battle-tested pipeline architecture supporting retrieval-augmented generation (RAG), semantic search, document processing, and agent-based workflows. Integrates with all major LLM providers, vector databases, and embedding models  --  provides Hermes Agent with enterprise-ready NLP infrastructure for building sophisticated language understanding pipelines, knowledge-intensive applications, and intelligent search systems at production scale.

**Key capabilities:** NLP framework, RAG pipelines, semantic search, question answering, document processing, agent workflows, Hermes-compatible
**Related:** [Knowledge Architecture →](/hermes/knowledge/) · [Tools →](#-tools--utilities)

---

### can1357/oh-my-pi
⭐ **13,559** · [github.com/can1357/oh-my-pi](https://github.com/can1357/oh-my-pi)

Oh My Pi  --  Raspberry Pi management and automation toolkit for AI agents. Enables Hermes Agent to control, configure, and manage Raspberry Pi devices for IoT, home automation, edge computing, and hardware prototyping workflows through structured tool calls.

**Key capabilities:** Raspberry Pi management, IoT automation, edge computing, hardware control, home automation, Hermes-compatible
**Related:** [Tools & Utilities →](#-tools--utilities)

---

### tirth8205/code-review-graph
⭐ **18,705** · [github.com/tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph)

Code review graph tool  --  visual code review and analysis platform that maps code changes, dependencies, and review workflows into interactive graphs. Enables Hermes Agent to perform comprehensive code reviews with architectural impact analysis, dependency tracing, and automated review summaries.

**Key capabilities:** Code review, graph visualization, dependency tracing, architectural analysis, automated reviews, Hermes-compatible
**Related:** [Tools & Utilities →](#-tools--utilities)

---

### ToolJet/ToolJet
⭐ **38,037** · `JavaScript` · [github.com/ToolJet/ToolJet](https://github.com/ToolJet/ToolJet)

Low-code platform for building internal tools  --  extensible open-source platform for rapidly creating custom internal applications, dashboards, and admin panels with drag-and-drop UI builder. Connects to databases, APIs, and services. Compatible with Hermes Agent for automated tool generation and workflow integration in enterprise environments.

**Maintainer:** ToolJet
**Key capabilities:** Low-code platform, internal tools, drag-and-drop builder, dashboard creation, database integration, Hermes-compatible
**Related:** [Infrastructure →](/hermes/infrastructure/)

---

### wavetermdev/waveterm
⭐ **21,345** · `TypeScript` · [github.com/wavetermdev/waveterm](https://github.com/wavetermdev/waveterm)

Wave Terminal  --  open-source terminal workspace with graphical widgets, web rendering, and AI integration. Modern terminal environment that combines traditional CLI with rich graphical capabilities including charts, images, file previews, and web content. Hermes Agent users gain a powerful terminal workspace for agent-driven development with visual feedback and multi-pane workflows.

**Maintainer:** Wave Terminal
**Key capabilities:** Terminal workspace, graphical widgets, web rendering, AI integration, multi-pane, Hermes-compatible
**Related:** [Tools & Utilities →](#-tools--utilities)

---

### PatterAI/Patter
⭐ **967** · `Python` · [github.com/PatterAI/Patter](https://github.com/PatterAI/Patter)

Open-source voice-AI SDK. The Vapi/Retell alternative for builders who want to own the stack. Give your Hermes agent a voice — build real-time voice AI applications with self-hosted infrastructure.

**Key capabilities:** Voice AI SDK, real-time voice, self-hosted, Vapi alternative, Retell alternative, open-source, Hermes-compatible
**Related:** [Tools & Utilities →](#-tools--utilities)

---

## 🎯 Orchestration, Multi-Agent & Swarms

Frameworks and patterns for coordinating multiple agents.

### multica-ai/multica
⭐ **36,931** · `Python` · [github.com/multica-ai/multica](https://github.com/multica-ai/multica)

Open-source managed agents platform  --  turns coding agents into real teammates with task assignment, tracking, and orchestration. Deploy and manage fleets of Hermes Agent instances with built-in task queues, progress monitoring, dependency resolution, and collaborative workflows. Transforms autonomous agents from one-off tools into persistent, accountable team members that can be assigned complex multi-step projects with full visibility into progress, blockers, and results.

**Key capabilities:** Managed agents, task assignment, orchestration, progress tracking, dependency resolution, Hermes-compatible, collaborative workflows
**Related:** [Architecture →](/hermes/architecture/)

---

### CherryHQ/cherry-studio
⭐ **47,420** · `TypeScript` · [github.com/CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)

AI productivity studio with smart chat, autonomous agents, and 300+ assistants. Unified access to multiple AI models  --  Hermes-compatible.

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

### abhi1693/openclaw-mission-control
⭐ **4,050** · `TypeScript` · [github.com/abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control)

AI Agent Orchestration Dashboard  --  comprehensive mission control interface for managing fleets of OpenClaw and Hermes agents with real-time monitoring, task dispatch, cost tracking, and performance analytics. Provides a centralized command center for agent operations with visual dashboards showing agent status, task queues, completion rates, and resource utilization. Essential infrastructure for teams running multiple autonomous agents in production with full observability and control.

**Key capabilities:** Agent orchestration, mission control, real-time monitoring, task dispatch, cost tracking, performance analytics, OpenClaw/Hermes native
**Related:** [Orchestration →](#-orchestration-multi-agent--swarms)

---

### builderz-labs/mission-control
⭐ **3,700+** · [github.com/builderz-labs/mission-control](https://github.com/builderz-labs/mission-control)

Multi-agent fleet management  --  task dispatch and cost tracking at scale. Hermes-compatible orchestration.

---

### iOfficeAI/AionUi
⭐ **28,359** · `TypeScript` · [github.com/iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)

Free, local, open-source 24/7 Cowork app for OpenClaw, Hermes Agent, Claude Code, Codex, OpenCode, Cursor, and Windsurf.

---

### koozyapno1/alex-ai-empire
⭐ **3** · `Python` · [github.com/koozyapno1/alex-ai-empire](https://github.com/koozyapno1/alex-ai-empire)

AI Empire Builder  --  6-Brain Autonomous Agent Architecture. OpenClaw + Hermes multi-brain system.

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

### agent-of-empires/agent-of-empires
⭐ **2,816** · `Rust` · [github.com/agent-of-empires/agent-of-empires](https://github.com/agent-of-empires/agent-of-empires)

Manage multiple Claude Code, OpenCode agents from either TUI or Web for easy access on mobile. Multi-agent orchestrator supporting Hermes Agent, Claude Code, Codex CLI, Gemini CLI, Mistral Vibe, Copilot CLI, and Pi.dev — unified interface for managing coding agents across providers.

**Key capabilities:** Multi-agent orchestration, TUI + Web UI, cross-provider support, Hermes-compatible, mobile-ready, task management
**Related:** [Orchestration →](#-orchestration-multi-agent--swarms)

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

Telegram-first multi-agent operating system for Hermes Agent  --  role-based bots, topic routing, skill integration, profile management, and built-in safety guardrails. A complete agent OS that turns Telegram into a multi-agent command center with production-grade safety, modular architecture, and scalable multi-bot coordination.

**Status:** Beta  
**Key capabilities:** Multi-agent OS, Telegram-native, role bots, topic routing, skill integration, safety guardrails, profile management

---

### tale-project/tale
⭐ **12** · `TypeScript` · [github.com/tale-project/tale](https://github.com/tale-project/tale)

The Orchestrator for AI Agents  --  connect OpenClaw, Hermes Agent, Claude Code, Codex, Cursor, Gemini CLI, OpenCode, and Pi into a unified agent swarm. Pool knowledge across agents, delegate tasks intelligently, and build collaborative multi-agent workflows. TypeScript-native agent orchestration layer that bridges the fragmented coding agent ecosystem into a single coordinated workforce.

**Key capabilities:** Multi-agent orchestration, agent swarm, knowledge pooling, task delegation, OpenClaw/Hermes-native, TypeScript, cross-agent bridges
**Related:** [Orchestration →](#-orchestration-multi-agent--swarms)

---

### goyalk1307/openclaw-ai-agent
⭐ **89** · [github.com/goyalk1307/openclaw-ai-agent](https://github.com/goyalk1307/openclaw-ai-agent)

Autonomous AI agent built on the OpenClaw framework  --  self-directed agent with task planning, tool orchestration, and multi-step workflow execution. Compatible with Hermes Agent for cross-framework agent deployment and collaborative multi-agent workflows.

**Key capabilities:** Autonomous agent, OpenClaw framework, task planning, tool orchestration, multi-step workflows, Hermes-compatible
**Related:** [Orchestration →](#-orchestration-multi-agent--swarms)

---

### bytedance/deer-flow
⭐ **71,354** · `Python` · [github.com/bytedance/deer-flow](https://github.com/bytedance/deer-flow)

ByteDance's open-source long-horizon SuperAgent harness. Researches, codes, and creates with sandboxes, memories, and multi-agent coordination. Architecture patterns directly applicable to Hermes deployments  --  long-running autonomous workflows with persistent state and multi-agent orchestration.

**Maintainer:** ByteDance
**Key capabilities:** SuperAgent harness, long-horizon execution, sandboxed research/coding, memory persistence, multi-agent coordination, Hermes-applicable patterns
**Related:** [Architecture →](/hermes/architecture/)

---

### ruvnet/ruflo
⭐ **64,353** · [github.com/ruvnet/ruflo](https://github.com/ruvnet/ruflo)

Leading agent meta-harness for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows with skill-based execution. Patterns transferable to Hermes agent orchestration  --  swarm coordination, skill delegation, and workflow automation.

**Key capabilities:** Agent meta-harness, multi-agent swarms, autonomous workflow coordination, skill-based execution, Claude-native, Hermes-applicable patterns
**Related:** [Architecture →](/hermes/architecture/)

---

### langgenius/dify
⭐ **145,532** · `TypeScript` · [github.com/langgenius/dify](https://github.com/langgenius/dify)

Production-ready platform for agentic workflow development. Industry-leading example of agent orchestration at scale  --  visual workflow designer, RAG pipeline, model management, and multi-agent coordination serving millions of production deployments. Architecture patterns for Hermes users building large-scale agent systems: workflow composition, tool integration, knowledge base management, and enterprise-grade agent governance.

**Maintainer:** Dify (LangGenius)
**Key capabilities:** Agentic workflow platform, visual designer, RAG pipeline, model management, multi-agent orchestration, enterprise-scale, Hermes-applicable patterns
**Related:** [Architecture →](/hermes/architecture/) · [Infrastructure →](/hermes/infrastructure/)

---

### JuliusBrussee/caveman
⭐ **74,471** · [github.com/JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)

Caveman agent  --  a brutally effective multi-agent framework designed for maximum throughput with minimal configuration overhead. Minimalist yet powerful agent orchestration system that coordinates multiple autonomous agents through a streamlined task distribution protocol emphasizing speed, reliability, and simplicity. Designed for Hermes Agent deployments where overhead matters  --  strips away unnecessary abstraction layers to deliver raw agent coordination performance with sub-millisecond task routing, built-in retry logic, and automatic failure recovery. The "just works" approach to multi-agent orchestration: define tasks, launch agents, get results.

**Key capabilities:** Multi-agent framework, minimalist orchestration, high-throughput, task distribution, sub-millisecond routing, failure recovery, Hermes-compatible
**Related:** [Orchestration →](#-orchestration-multi-agent--swarms)

---

### code-yeongyu/oh-my-openagent
⭐ **62,692** · [github.com/code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)

Oh My OpenAgent  --  open-source autonomous agent framework for building, deploying, and orchestrating AI agents with pluggable skills, MCP integration, and multi-platform support. Provides a complete agent development toolkit including skill registry, model routing, conversation management, and deployment automation. Compatible with Hermes Agent for rapid agent prototyping and production deployment with built-in support for common agent patterns: RAG pipelines, tool-augmented reasoning, multi-agent collaboration, and autonomous task execution loops.

**Key capabilities:** Open-source agent framework, pluggable skills, MCP integration, model routing, multi-platform, Hermes-compatible
**Related:** [Architecture →](/hermes/architecture/)

---

### crewAIInc/crewAI
⭐ **53,905** · [github.com/crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)

CrewAI  --  production-grade multi-agent orchestration framework for role-based AI agent teams. Define agents with specific roles, goals, and tools, then orchestrate them through sequential, hierarchical, or collaborative task execution patterns. Each agent operates as a specialized crew member with defined responsibilities, domain expertise, and decision authority  --  the framework coordinates inter-agent communication, task handoffs, conflict resolution, and output synthesis. Essential infrastructure for Hermes Agent users building multi-agent systems where specialized agents collaborate on complex workflows requiring division of labor, peer review, and iterative refinement across knowledge domains.

**Key capabilities:** Multi-agent orchestration, role-based agents, sequential/hierarchical execution, inter-agent communication, task delegation, Hermes-compatible
**Related:** [Orchestration →](#-orchestration-multi-agent--swarms) · [Architecture →](/hermes/architecture/)

---

### seleman66eeddwegger3-art/hermes-agentmesh
⭐ **1/day trending** · `Python` · [github.com/seleman66eeddwegger3-art/hermes-agentmesh](https://github.com/seleman66eeddwegger3-art/hermes-agentmesh)

Peer-to-peer, 0-SSH, Redis-backed async message bus for multi-agent systems  --  designed by Bobo, a Hermes agent architect. Replaces synchronous HTTP coordination with Redis mailboxes: agents communicate by dropping tasks in named inboxes (`redis.lpush("inbox:<NODE_NAME>", task_json)`) instead of making blocking HTTP calls. Eliminates timeout anxiety (hours-long tasks OK), removes SSH requirements for remote workers, and ensures reports land naturally on the initiating machine. Framework-agnostic  --  works with Hermes, OpenClaw, LangGraph, AutoGen, and CrewAI.

**Key capabilities:** Async message bus, Redis mailboxes, 0-SSH deployment, multi-agent coordination, framework-agnostic, Hermes-native, cross-machine tasks
**Related:** [Orchestration →](#-orchestration-multi-agent--swarms) · [Deployment →](#-deployment--infrastructure)

---

### conductor-oss/conductor
⭐ **31,962** · `Java` · [github.com/conductor-oss/conductor](https://github.com/conductor-oss/conductor)

Conductor  --  Netflix-originated, battle-tested workflow orchestration engine now fully open-source under the Linux Foundation. Orchestrates complex microservice and agent workflows through a declarative JSON DSL with support for parallel execution, conditional branching, dynamic forks, wait states, and sub-workflows. Production-proven at Netflix scale (millions of concurrent workflows)  --  provides Hermes Agent with enterprise-grade workflow orchestration infrastructure for coordinating multi-step agent tasks, managing long-running autonomous processes, and ensuring fault tolerance across distributed agent deployments. Includes a visual UI for workflow design and real-time execution monitoring.

**Key capabilities:** Workflow orchestration, Netflix-origin, JSON DSL, parallel execution, fault tolerance, visual UI, enterprise-grade, Hermes-compatible
**Related:** [Orchestration →](#-orchestration-multi-agent--swarms) · [Architecture →](/hermes/architecture/)

---

### thestark77/cobalt-agent
⭐ **3** · `Python` · [https://github.com/thestark77/cobalt-agent](https://github.com/thestark77/cobalt-agent)

Modular orchestration plugin for Hermes Agent — model routing, tool guard, skill injection


---

### hugocarreira/agentrc
⭐ **2** · `Markdown` · [https://github.com/hugocarreira/agentrc](https://github.com/hugocarreira/agentrc)

Single source of truth for AI coding agents — share AGENTS.md, RTK.md, skills, and plugins across OpenCode, Codex, Claude, Copilot, Hermes & Gemini CLI. Powered by agentrc.

**Topics:** `ai`, `ai-agent`, `automation`, `claude`, `codex`, `developer-tools`, `opencode`, `productivity`

---

### Intelligent-Internet/zenith
⭐ **257** · `Python` · [github.com/Intelligent-Internet/zenith](https://github.com/Intelligent-Internet/zenith)

Zenith — a continuous-improvement harness for long-running agent tasks. Turns Claude Code, Codex, or Hermes into a multi-agent mission orchestrator via MCP/ACP. Supports agent-client-protocol, multi-agent orchestration, long-horizon tasks, and LLM-powered autonomous workflows.

**Topics:** `agent-client-protocol`, `agent-harness`, `ai-agents`, `claude-code`, `codex`, `llm`, `long-horizon-tasks`, `mcp`, `model-context-protocol`, `multi-agent`, `orchestration`
**Related:** [Orchestration →](#-orchestration-multi-agent--swarms)

---

## 🚀 Deployment & Infrastructure

Running Hermes in production  --  from Docker to Kubernetes.

### 1Panel-dev/1Panel
⭐ **35,898** · `Go` · [github.com/1Panel-dev/1Panel](https://github.com/1Panel-dev/1Panel)

Modern, open-source VPS control panel  --  the only one with native AI agent management. One-click Hermes deployment.

---

### paperclipinc/hermes-operator
⭐ **13** · `Go` · [github.com/paperclipinc/hermes-operator](https://github.com/paperclipinc/hermes-operator)

Production-grade Kubernetes operator for Hermes Agent  --  deploy, scale, and manage Hermes agents as K8s resources.

---

### JackTheGit/hermes-autonomous-server
⭐ **14** · `Shell` · [github.com/JackTheGit/hermes-autonomous-server](https://github.com/JackTheGit/hermes-autonomous-server)

Run Hermes Agent autonomously on your Linux server using systemd and nohup. Production-ready systemd service configuration.

---

### TheAiSingularity/hermesclaw
⭐ **53** · `Dockerfile` · [github.com/TheAiSingularity/hermesclaw](https://github.com/TheAiSingularity/hermesclaw)

Hermes Agent sandboxed by NVIDIA OpenShell  --  hardware-enforced security for autonomous agent deployment.

---

### H-Ali13381/hermes-linux-ricing
⭐ **16** · `Shell` · [github.com/H-Ali13381/hermes-linux-ricing](https://github.com/H-Ali13381/hermes-linux-ricing)

Desktop customization via Hermes  --  let your agent configure your Linux desktop environment.

---

### anomaliagent007-hue/hermes-mimo-bridge
⭐ **0** · `Python` · [github.com/anomaliagent007-hue/hermes-mimo-bridge](https://github.com/anomaliagent007-hue/hermes-mimo-bridge)

Production bridge between Hermes Agent and Xiaomi MiMo API  --  long-chain reasoning for IoT device control.

---

### yuluyangguang1/hermes-portable
⭐ **37** · `Python` · [github.com/yuluyangguang1/hermes-portable](https://github.com/yuluyangguang1/hermes-portable)

Plug-in-a-USB AI agent — zero-install, zero-trace, cross-platform portable Hermes Agent. Runs directly from a USB drive with no installation required, leaving no traces on the host machine. Ideal for air-gapped environments, demos, and secure portable deployments.

**Key capabilities:** USB portable, zero-install, zero-trace, cross-platform, self-contained, air-gap ready
**Related:** [Hermes Setup Guide →](/hermes/setup/)

---

### CorpusIQ Multi-Machine Architecture
[Deployment Guide →](/hermes/infrastructure/)

Multi-machine (primary + worker) production deployment. SSH orchestration, model routing (65% cost savings), production-cron reference.

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

### affaan-m/ECC
⭐ **217,699** · [github.com/affaan-m/ECC](https://github.com/affaan-m/ECC)

Enterprise Cloud Computing (ECC) platform  --  production-grade cloud infrastructure purpose-built for deploying and managing autonomous AI agent fleets at enterprise scale. Provides a complete cloud computing environment with built-in agent orchestration, resource allocation, cost optimization, monitoring dashboards, and fleet management capabilities. Designed for organizations running thousands of concurrent Hermes Agent instances  --  handles agent lifecycle management, auto-scaling based on workload demand, cross-region deployment, and centralized governance with role-based access control. The definitive enterprise infrastructure layer for production Hermes Agent deployments requiring five-nines reliability, compliance-ready audit trails, and predictable cloud economics.

**Key capabilities:** Enterprise cloud computing, agent fleet management, auto-scaling, cross-region deployment, cost optimization, compliance-ready, Hermes-compatible
**Related:** [Infrastructure →](/hermes/infrastructure/)

---

### HKUDS/nanobot
⭐ **44,435** · [github.com/HKUDS/nanobot](https://github.com/HKUDS/nanobot)

Nanobot  --  lightweight AI agent deployment framework from HKU Data Science Lab. A minimal-footprint agent runtime optimized for edge devices, containers, serverless functions, and resource-constrained environments. Runs Hermes Agent-compatible workloads with dramatically reduced memory and CPU requirements while maintaining full autonomous agent capabilities including skill execution, tool calling, and multi-turn conversation. Ideal for IoT deployments, embedded systems, mobile edge computing, and any scenario where traditional agent runtimes are too heavy  --  delivers autonomous intelligence in environments where every megabyte and milliwatt counts.

**Key capabilities:** Lightweight agent runtime, edge deployment, container-optimized, IoT-ready, low-resource, serverless, Hermes-compatible
**Related:** [Infrastructure →](/hermes/infrastructure/)

---

### markwang2658/hermes-windows-native
⭐ **20** · `Python` · [github.com/markwang2658/hermes-windows-native](https://github.com/markwang2658/hermes-windows-native)

Windows-native integrated package bundling Hermes Agent v0.16.0 + Hermes WebUI v0.51.454  --  no Docker, no WSL2 required. Shared Python venv, PowerShell launchers, and one-click startup via `hermes-start.ps1`. Runtime data redirected to `%USERPROFILE%\.hermes` keeping the source tree clean. The lightest local footprint on Windows  --  eliminates the ~4GB Docker Desktop overhead and WSL2 dependency that block many Windows users from running Hermes.

**Key capabilities:** Windows-native, no Docker, no WSL2, one-click startup, shared venv, PowerShell launchers, Hermes Agent + WebUI
**Related:** [Deployment →](#-deployment--infrastructure) · [Setup Guide →](/hermes/skills/catalog/hermes-windows-native/)

---

### pom11/hscc
⭐ **3** · `Python` · [https://github.com/pom11/hscc](https://github.com/pom11/hscc)

Hermes Spark Cluster Control — Install package, plugins, skills, templates


---

### aims1425-lab/hermes-deploy
⭐ **0** · `Shell` · [https://github.com/aims1425-lab/hermes-deploy](https://github.com/aims1425-lab/hermes-deploy)

Production-ready Hermes Agent deployment template with Docker, security hardening, Telegram integration, and OSS maintainer workflows

**Topics:** `ai-agent`, `deployment`, `devops`, `docker`, `docker-compose`, `hermes-agent`, `open-source`, `security-hardening`

---

### romdix/coolify-hermes-stack
⭐ **0** · `Unknown` · [https://github.com/romdix/coolify-hermes-stack](https://github.com/romdix/coolify-hermes-stack)

A production-ready Docker Compose stack to deploy Hermes Agent and Workspace UI on Coolify.


---

### varunlakshmaiah/hermes-compose
⭐ **0** · `Shell` · [https://github.com/varunlakshmaiah/hermes-compose](https://github.com/varunlakshmaiah/hermes-compose)

A zero-friction, production-ready Docker Compose architecture for instantly deploying the NousResearch Hermes AI Agent & Gateway on Dokploy, VPS, or locally.

**Topics:** `ai-agent`, `docker`, `docker-compose`, `hermes`, `nousresearch`, `openrouter`, `selfhosted`, `webhook`

---

## 🔒 Security & Governance

Security tools, governance frameworks, and safety systems.

### jnMetaCode/shellward
⭐ **109** · `Python` · [github.com/jnMetaCode/shellward](https://github.com/jnMetaCode/shellward)

AI Agent Security Middleware  --  8-layer defense, DLP data flow, prompt injection protection. Hermes-compatible security layer.

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

### codegraphtheory/chainforge
⭐ **8** · `Python` · [github.com/codegraphtheory/chainforge](https://github.com/codegraphtheory/chainforge)

Installable Hermes Agent profile for a security-first blockchain architect specializing in smart contracts, Solidity, Solana, DeFi, audits, governance, and tokenomics.

**Key capabilities:** Smart contracts, Solidity, Solana, DeFi, blockchain security, governance, tokenomics

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

Multi-dimensional evaluation framework for AI coding agents  --  Hermes Edition. Evaluates code generation, debugging, and refactoring.

---

### brianyazzz/HermesEval
⭐ **0** · `Python` · [github.com/brianyazzz/HermesEval](https://github.com/brianyazzz/HermesEval)

Continuous evaluation and benchmarking pipeline for Nous Research open-source models on Hermes Agent.

---

### am423/hermesbenchv0_1
⭐ **0** · `Python` · [github.com/am423/hermesbenchv0_1](https://github.com/am423/hermesbenchv0_1)

Hermes Agent benchmark v0.1  --  evaluate local models on actual tool-calling performance within Hermes.

---

### CogalNocloz/Hermes_evaluation
⭐ **0** · `Vue` · [github.com/CogalNocloz/Hermes_evaluation](https://github.com/CogalNocloz/Hermes_evaluation)

Benchmark Hermes  --  Hello World Nuxt 4 style evaluation framework.

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

Provider-neutral autonomous ML research paper writer  --  ideation to LaTeX compilation. Hermes-powered.

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

Turn any topic into tomorrow's front page with MiroFish simulation  --  AI-powered front page generation that transforms trending topics into newspaper-style editorial layouts. Creative content generation skill for Hermes Agent that visualizes what matters as professional front pages with automated layout and typography.

**Status:** Beta  
**Key capabilities:** Front page generation, MiroFish simulation, topic visualization, newspaper layout, content creation

---

### Delibread0601/askaipods
⭐ **2** · `TypeScript` · [github.com/Delibread0601/askaipods](https://github.com/Delibread0601/askaipods)

Search AI podcast quotes by topic across Lex Fridman, Dwarkesh Patel, No Priors, Latent Space, and more  --  semantic search engine for AI podcast knowledge discovery. Discover expert insights by topic across the top AI and tech podcast ecosystem, Hermes-compatible for research workflows and content curation.

**Status:** Beta  
**Key capabilities:** AI podcast search, quote discovery, topic search, semantic podcast engine, Lex Fridman, Dwarkesh Patel

---

## 🌏 Platform-Specific

Chinese, Japanese, Korean, and other language-specific Hermes resources.

### Chinese (中文) Resources

| Resource | Stars | Description |
|----------|-------|-------------|
| [alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book) | 4,443 | Complete tutorial  --  beginner to expert |
| [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | 15,046 | 216 AI expert roles for Hermes + 17 tools |
| [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | 5,450 | AI coding superpowers, Chinese edition |
| [AlexAnys/awesome-openclaw-usecases-zh](https://github.com/AlexAnys/awesome-openclaw-usecases-zh) | 4,324 | 50+ OpenClaw use cases in Chinese |
| [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | 2,842 | Multi-engine management panel |
| [Eynzof/Hermes-CN-Desktop](https://github.com/Eynzof/Hermes-CN-Desktop) | 617 | Windows-First desktop app built with Tauri + Rust |
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

Autonomous SRE agent built on Hermes  --  detects, heals, and learns from production incidents. Self-improving incident response.

---

### mrbooboo1987-creator/hermes-grok-trading-system
⭐ **0** · `Python` · [github.com/mrbooboo1987-creator/hermes-grok-trading-system](https://github.com/mrbooboo1987-creator/hermes-grok-trading-system)

Autonomous 24/7 AI trading agent powered by Grok 4.20. Hermes-based trading system.

---

### SergeySolovyev/sergei-brand-agent
⭐ **0** · `Python` · [github.com/SergeySolovyev/sergei-brand-agent](https://github.com/SergeySolovyev/sergei-brand-agent)

Autonomous AI agent (Hermes + Triad) promoting commercial brand  --  content creation, social media, engagement.

---

### Boatsure/PaperDigest
⭐ **0** · [github.com/Boatsure/PaperDigest](https://github.com/Boatsure/PaperDigest)

Hermes Agent Skill for ML researchers  --  personalized paper reading and digest generation.

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

Hermes agent configuration reference  --  OpenWrt + Hermes integration patterns.

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

### Bo1202/Aivy-OS
⭐ **21** · `Python` · [github.com/Bo1202/Aivy-OS](https://github.com/Bo1202/Aivy-OS)

Your own digital life form  --  local AI companion with persistent memory, IDE workspace, MCP support, and 30+ tools. Companion-first alternative to Hermes Agent, OpenClaw, and Claude Code with desktop/browser automation and local LLM support.

**Status:** Active  
**Key capabilities:** AI companion, persistent memory, IDE workspace, MCP integration, desktop automation, browser automation, local LLM (Ollama), 30+ tools, Electron UI  
**Related:** [Hermes Agent →](https://github.com/NousResearch/hermes-agent)

---

### santifer/career-ops
⭐ **54,555** · [github.com/santifer/career-ops](https://github.com/santifer/career-ops)

CareerOps  --  AI-powered career operations platform that automates end-to-end career management workflows. Covers job search optimization with intelligent matching algorithms, resume tailoring with ATS-optimized formatting, interview preparation with role-specific question banks and mock interview simulations, networking strategy with personalized outreach templates, salary negotiation guidance, and long-term career path planning with skills gap analysis. Drop-in compatible with Hermes Agent for building autonomous career management agents that handle the full professional development lifecycle  --  from job discovery through offer negotiation  --  with personalized strategies backed by labor market data and industry benchmarks.

**Key capabilities:** Career operations, job search automation, resume optimization, interview preparation, career planning, ATS optimization, Hermes-compatible
**Related:** [Domain Applications →](#-domain-applications)

---

### feder-cr/Jobs_Applier_AI_Agent_AIHawk
⭐ **29,913** · [github.com/feder-cr/Jobs_Applier_AI_Agent_AIHawk](https://github.com/feder-cr/Jobs_Applier_AI_Agent_AIHawk)

AIHawk  --  autonomous job application AI agent that automates the complete job application workflow from end to end. Discovers relevant job listings across multiple platforms (LinkedIn, Indeed, Glassdoor, company career pages), intelligently tailors resumes and cover letters to each position using semantic matching against job descriptions, auto-fills complex application forms with context-aware responses, manages application tracking with status dashboards, and follows up on pending applications with automated email reminders. Built with anti-detection measures to work naturally with applicant tracking systems. Deployable as a Hermes Agent skill for fully autonomous job hunting  --  set your preferences once and let the agent handle the rest 24/7 with detailed reporting on application status, response rates, and interview pipeline metrics.

**Key capabilities:** Autonomous job application, multi-platform job search, resume tailoring, cover letter generation, application tracking, ATS-compatible, Hermes-compatible
**Related:** [Domain Applications →](#-domain-applications)

---

### google-research/timesfm
⭐ **23,223** · `Python` · [github.com/google-research/timesfm](https://github.com/google-research/timesfm)

TimesFM (Time Series Foundation Model)  --  pretrained decoder-only foundation model for zero-shot time series forecasting. Feed it any univariate time series (sales, sensor readings, stock prices, energy demand, weather) and get point forecasts with calibrated quantile prediction intervals  --  no training required. Supports up to 16K context points, covariate forecasting (XReg) with exogenous variables, and fine-tuning via HuggingFace Transformers + PEFT (LoRA). Includes a first-party Agent Skills standard SKILL.md for drop-in integration with Hermes Agent, Claude Code, Cursor, and Codex CLI. Runs inside BigQuery (SQL), Google Sheets (spreadsheet formulas), and Vertex AI (API endpoints).

**Maintainer:** Google Research
**License:** Apache 2.0
**Key capabilities:** Zero-shot forecasting, time series foundation model, prediction intervals, covariate forecasting, Agent Skills integration, BigQuery/Sheets/Vertex deployment
**Model size:** 200M params (~800MB)

---

---

### jeecgboot/JeecgBoot
⭐ **46,795** · `Java` · [github.com/jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot)

JeecgBoot  --  enterprise-grade low-code development platform for rapidly building business applications, CRMs, ERPs, and management systems. Combines a visual low-code designer with code generation, workflow engines, form builders, and reporting tools  --  capable of reducing application development time by 80%+. Provides Hermes Agent with a powerful application development backend for autonomously constructing business software, generating database schemas, creating REST APIs, and deploying full-stack applications with minimal human intervention.

**Key capabilities:** Low-code platform, code generation, workflow engine, form builder, rapid application development, Hermes-compatible
**Related:** [Domain Applications →](#-domain-applications)

---

### yang1989haoa-gif/synapse-studio
⭐ **1** · `TypeScript` · [https://github.com/yang1989haoa-gif/synapse-studio](https://github.com/yang1989haoa-gif/synapse-studio)

a local-first visual orchestration workspace for AI agents, enabling users to design, connect, test, and observe multi-agent workflows with Hermes and OpenClaw integrations, execution traces, and secure per-agent configuration.


---

### kaankacar/stellar-agent-kit
⭐ **0** · `TypeScript` · [https://github.com/kaankacar/stellar-agent-kit](https://github.com/kaankacar/stellar-agent-kit)

Connect any AI agent to Stellar / Soroban — TypeScript SDK with plugin architecture for LangChain, Vercel AI SDK, OpenAI, and Anthropic tool-calling. Includes autonomous-agent runner, Telegram bot template, and Hermes Agent integration.


---

### muyezhu/YanCotta-enterprise_challenge_sprint_1_hermes_reply-20251003220334
⭐ **0** · `Unknown` · [https://github.com/muyezhu/YanCotta-enterprise_challenge_sprint_1_hermes_reply-20251003220334](https://github.com/muyezhu/YanCotta-enterprise_challenge_sprint_1_hermes_reply-20251003220334)

A production-grade, open-source SaaS platform for predictive maintenance. This project is built on a resilient and scalable stack including FastAPI, PostgreSQL/TimescaleDB , and Redis, all with Docker and with full cloud deployment. It implements a sophisticated Multi-Agent AI system and a MLOps lifecycle with MLflow to manage 17 distinct models

**Topics:** `jules-annotation-20251001`

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

### Sylinko/Everywhere
⭐ **6,072** · `C#` · [github.com/Sylinko/Everywhere](https://github.com/Sylinko/Everywhere)

On-screen aware AI assistant for your desktop. Uses current app context, multiple LLMs (Claude, DeepSeek, Gemini, OpenAI), and MCP tools with Hermes Agent integration to help you act across apps. Avalonia-based desktop app with skills, flow-state support, and on-screen awareness.

**Status:** Active · **Forks:** 374  
**Key capabilities:** On-screen awareness, multi-LLM, MCP tools, desktop AI, Hermes integration, flow-state  
**Related:** [MCP Guide →](/hermes/mcp/) · [Skills Catalog →](/hermes/skills/catalog/)

---

### beardthelion/hermes-skill-distillation
⭐ **community** · `Python` · [github.com/beardthelion/hermes-skill-distillation](https://github.com/beardthelion/hermes-skill-distillation)

Agentic training trajectories from Hermes sessions. Distill agent behavior into training data.

**Status:** Experimental  
**Key capabilities:** Skill distillation, training trajectories, agentic learning

---

### xiaojilele-glitch/WhyBuddy
⭐ **347** · `TypeScript` · [github.com/xiaojilele-glitch/WhyBuddy](https://github.com/xiaojilele-glitch/WhyBuddy)

A simple and universal product rehearsal engine — spec anything. Connect Hermes agents to a product rehearsal engine for speccing and iterating on product ideas. Multi-agent compatible.

**Status:** Active · **Forks:** 57  
**Key capabilities:** Product rehearsal, spec engine, Hermes integration, multi-agent, product iteration  
**Related:** [Orchestration →](#-orchestration-multi-agent--swarms)

---

### repolex-forx/NousResearch--hermes-paperclip-adapter
⭐ **0** · `Unknown` · [https://github.com/repolex-forx/NousResearch--hermes-paperclip-adapter](https://github.com/repolex-forx/NousResearch--hermes-paperclip-adapter)

RDF parse data for NousResearch/hermes-paperclip-adapter


---

### mage0535/hermes-memory-installer
⭐ **165** · `Python` · [github.com/mage0535/hermes-memory-installer](https://github.com/mage0535/hermes-memory-installer)

Production-grade memory sidecar for AI agents — gbrain + Hindsight + 3-tier recall. Agent-agnostic, battle-tested. Compatible with Hermes, Claude, Cursor, and any AI agent.

**Status:** Active · **Forks:** 9  
**Key capabilities:** Agent memory, knowledge graph, semantic search, vector memory, 3-tier recall, gbrain, production-grade  
**Related:** [Memory & Knowledge →](#-memory--knowledge)

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
| Total repos indexed | 411 |
| Categories | 18 |
| Official Nous Research repos | 4 |
| Community awesome lists | 21 |
| UI/Dashboard projects | 14 |
| Memory systems | 28 |
| MCP integrations | 32 |
| Skill collections & plugins | 69 |
| Tools & utilities | 39 |
| Research/benchmark projects | 12 |
| Deployment & infra projects | 21 |
| Domain applications | 22 |
| Forks & derivatives | 8 |
| Language-specific resources | 12 (10 CN, 1 JP, 1 EN) |
| Total community stars | 1M+ across all indexed repos |

---

## 🔗 Cross-Reference Index

| Topic | Resources |
|-------|-----------|
| **Getting Started** | [Setup Guide](/hermes/setup/) · [Official Docs](https://hermes-agent.nousresearch.com/docs/) · [Orange Book](https://github.com/alchaincyf/hermes-agent-orange-book) · [27-Chapter Tutorial](https://github.com/longyunfeigu/learn-hermes-agent) |
| **Memory** | [Knowledge Architecture](/hermes/knowledge/) · [GBrain](https://github.com/garrytan/gbrain) · [EverOS](https://github.com/EverMind-AI/EverOS) · [claude-mem](https://github.com/thedotmack/claude-mem) · [mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) |
| **MCP** | [MCP Guide](/hermes/mcp/) · [CorpusIQ](https://corpusiq.io) · [Kindly Search](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server) · [Kagi MCP](https://github.com/KSroido/Kagi-Session2API-MCP) |
| **Skills** | [Skills Catalog](/hermes/skills/catalog/) · [Marketing Skills](https://github.com/Ben-Home/marketingskills) · [Skill Factory](https://github.com/Romanescu11/hermes-skill-factory) · [372 Skills](https://github.com/BBridgeers/hermes-skills) |
| **UI** | [Hermes WebUI](https://github.com/nesquena/hermes-webui) · [Desktop](https://github.com/fathah/hermes-desktop) · [Studio](https://github.com/EKKOLearnAI/hermes-studio) · [Workspace](https://github.com/outsourc-e/hermes-workspace) · [Scarf](https://github.com/awizemann/scarf) |
| **Production** | [Deployment](/hermes/infrastructure/) · [Crons](/hermes/governance/scheduling/) · [K8s Operator](https://github.com/paperclipinc/hermes-operator) · [Autonomous Server](https://github.com/JackTheGit/hermes-autonomous-server) |
| **Research** | [Self-Evolution](https://github.com/NousResearch/hermes-agent-self-evolution) · [PawBench](https://github.com/agentscope-ai/PawBench) · [HermesBench](https://github.com/verkyyi/hermesbench) |
| **Security** | [Shellward](https://github.com/jnMetaCode/shellward) · [Skillguard](https://github.com/buzzicra/skillguard) · [NemoClaw](https://github.com/NVIDIA/NemoClaw) |

---

## 🎯 Operational Playbooks

Proven operational patterns for running Hermes in production.

- **Nightly self-evolution + guardrail verification**  --  Run self-evolution cycles during off-peak hours with automated regression testing to catch drift before it reaches production.
- **Memory pressure management with Honcho/Hindsight**  --  Monitor memory utilization, set retention policies, and archive stale context to prevent memory bloat and performance degradation.
- **Tune session timeout/expiry early**  --  Configure session timeouts appropriate to your workflow cadence. Too short breaks long-running tasks; too long wastes resources.
- **OpenClaw side-by-side migration strategy**  --  Run Hermes and OpenClaw in parallel during transition. Validate behavior parity before cutting over completely.
- **Treat USER.md and MEMORY.md as infrastructure**  --  Version control your agent personality and memory configuration. These files are as critical as production configs.

---

## 📈 Level-Up Blueprints

Progressive capability blueprints for advancing your Hermes deployment.

- **Memory stack that compounds (Hermes → Honcho → Hindsight → Plur)**  --  Layer memory systems progressively: start with Hermes built-in, add Honcho for peer modeling, Hindsight for long-term retention, and Plur for cross-agent shared memory.
- **Self-improvement without drift (evolution + linting + regression checks)**  --  Combine self-evolution with lintlang validation and benchmark regression tests to ensure improvements don't degrade reliability.
- **Operator cockpit (workspace + mission-control + webui)**  --  Build a unified operator interface combining Hermes Workspace for interaction, Mission Control for fleet management, and WebUI for monitoring.
- **Multi-agent execution layer (ACP + swarm + bigiron)**  --  Scale from single-agent to multi-agent with ACP delegation, swarm frameworks for parallel execution, and bigiron for AI-native SDLC.
- **Migration + deployment hardening (Nix + Docker + evey-setup)**  --  Productionize your deployment with Nix for reproducible builds, Docker for isolation, and evey-setup for automated environment provisioning.

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

> **📊 Ecosystem Stats:** 411 repos · 18 categories · 1M+ community stars · 48 skill collections · 20 MCP integrations · 15 domain applications

---

## FAQ

### What is the Hermes Ecosystem Directory?

The **Hermes Ecosystem Directory** is the most comprehensive collection of Hermes Agent resources in existence  --  **411+ repositories** organized across 18 categories including core tools, UIs, memory systems, MCP integrations, skills, deployment, research, and domain applications. It's the definitive map of the Hermes universe.

### How do I find tools and resources for Hermes Agent?

Browse the [Quick Navigation](#-quick-navigation) table above to jump to any of 18 categories: Core & Official, Documentation, UIs, Memory, MCP, Skills, Tools, Orchestration, Deployment, Security, Research, Content, Platform-Specific, Domain Applications, and more. Each entry includes star counts, maintainers, descriptions, and key capabilities.

### How do I submit my Hermes project to the ecosystem?

**[Submit a repo →](https://github.com/CorpusIQ/corpusiq-docs/issues/new?template=submit-repo.yml)**  --  takes 60 seconds. Include the repo URL, description, and suggested category. Submissions are reviewed within 48 hours and accepted repos appear in this directory with your GitHub handle credited. See the [Contributors page](/hermes/contributors/) for full guidelines.

### What are the most popular Hermes Agent tools?

Based on community stars: **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** (202K+), **[claude-mem](https://github.com/thedotmack/claude-mem)** (82K+), **[open-design](https://github.com/nexu-io/open-design)** (66K+), **[gbrain](https://github.com/garrytan/gbrain)** (23K+), **[NemoClaw](https://github.com/NVIDIA/NemoClaw)** (21K+), **[screenpipe](https://github.com/screenpipe/screenpipe)** (19K+), and **[hermes-webui](https://github.com/nesquena/hermes-webui)** (14.5K+).

### How does the ecosystem directory stay updated?

The directory is maintained by **[CorpusIQ](https://corpusiq.io)** with monitoring crons that scan GitHub, MCP directories, and community channels for new Hermes Agent resources. Community submissions are reviewed within 48 hours. The discovery engine runs nightly (10 PM - 2 AM Arizona time) to detect new entries.

## Related Pages

- [Hermes Knowledge Hub  --  Production Deployment](/hermes/)
- [Documentation Index  --  Complete Reference](/hermes/)
- [Agent Library  --  9 Role Configurations](/hermes/agents/)
- [Community Contributors  --  Join the Directory](/hermes/contributors/)
- [Skills Catalog  --  133+ Production Skills](/hermes/skills/catalog/)
- [CorpusIQ MCP Connectors  --  37+ Business Tools](/hermes/mcp/connectors/)
- [Submit a Repo →](https://github.com/CorpusIQ/corpusiq-docs/issues/new?template=submit-repo.yml)
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 115000 | 232 AI agent personalities across 16 divisions — marketing, engineering, design, QA, security, support. One-click install for Claude Code, Copilot, Cursor, Aider, OpenCode. MIT license. | agent-personality, multi-agent, marketing, engineering, design |
| [dontriskit/awesome-ai-system-prompts](https://github.com/dontriskit/awesome-ai-system-prompts) | 6019 | Curated collection of AI system prompts across multiple platforms — ChatGPT, Claude, Gemini, Copilot. Production-tested prompt engineering patterns. | prompt-engineering, system-prompts, agent-personality |
| [samber/cc-skills-golang](https://github.com/samber/cc-skills-golang) | 2261 | Claude Code skills for Go development — testing, linting, debugging, code generation. Golang-specific agent workflows. | golang, claude-code, development |
| [erikdarlingdata/PerformanceMonitor](https://github.com/erikdarlingdata/PerformanceMonitor) | 423 | SQL Server performance monitoring with AI agent integration. Production database observability. | database, monitoring, sql-server |
| [Karanjot786/agent-skills-cli](https://github.com/Karanjot786/agent-skills-cli) | 163 | CLI tool for managing AI agent skills — install, update, publish agent skills across platforms. | agent-skills, cli, developer-tools |
| [enescingoz/awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates) | 23236 | 280+ free n8n automation templates — ready-to-use workflows for Gmail, Telegram, Slack, Discord, WhatsApp, Google Drive, | agent, ecosystem |
| [triggerdotdev/trigger.dev](https://github.com/triggerdotdev/trigger.dev) | 15451 | Trigger.dev – build and deploy fully‑managed AI agents and workflows | agent, ecosystem |
| [nanobrowser/nanobrowser](https://github.com/nanobrowser/nanobrowser) | 13341 | Open-Source Chrome extension for AI-powered web automation. Run multi-agent workflows using your own LLM API key. Altern | agent, ecosystem |
| [waooAI/waoowaoo](https://github.com/waooAI/waoowaoo) | 12863 | 首家工业级全流程 AI 影视生产平台。Industry-first professional AI Agent platform for controllable film & video production. From shorts t | agent, ecosystem |
| [firerpa/lamda](https://github.com/firerpa/lamda) | 7834 |  The most powerful Android RPA agent framework, next generation mobile automation. | agent, ecosystem |
| [AIDC-AI/ComfyUI-Copilot](https://github.com/AIDC-AI/ComfyUI-Copilot) | 5300 | An AI-powered custom node for ComfyUI designed to enhance workflow automation and provide intelligent assistance | agent, ecosystem |
| [generalaction/emdash](https://github.com/generalaction/emdash) | 4963 | Emdash is the Open-Source Agentic Development Environment (🧡 YC W26). Run multiple coding agents in parallel. Use any pr | agent, ecosystem |
| [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | 4533 | Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom a | agent, ecosystem |
| [TracecatHQ/tracecat](https://github.com/TracecatHQ/tracecat) | 3688 | Open-source security automation platform for teams and AI agents | agent, ecosystem |
| [SmythOS/sre](https://github.com/SmythOS/sre) | 1279 | The SmythOS Runtime Environment (SRE) is an open-source, cloud-native runtime for agentic AI. Secure, modular, and produ | agent, ecosystem |
| [massgen/MassGen](https://github.com/massgen/MassGen) | 1063 | 🚀 MassGen is an open-source multi-agent scaling system that runs in your terminal, autonomously orchestrating frontier m | agent, ecosystem |
| [docker/compose-for-agents](https://github.com/docker/compose-for-agents) | 982 | Build and run AI agents using Docker Compose. A collection of ready-to-use examples for orchestrating open-source LLMs,  | agent, ecosystem |
| [bytechefhq/bytechef](https://github.com/bytechefhq/bytechef) | 775 | Open-source platform that unifies AI agent orchestration and workflow automation — autonomy and precision in one platfor | agent, ecosystem |
| [giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit) | 291 |  Modular plugin marketplace for Claude Code and agentic CLIs, with validated, spec-driven skills, agents, commands, and  | agent, ecosystem |
| [osovv/grace-marketplace](https://github.com/osovv/grace-marketplace) | 214 |  GRACE (Graph-RAG Anchored Code Engineering): open Agent Skills for contract-driven AI code generation with semantic mar | agent, ecosystem |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 141060 | FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, L | agent, ecosystem |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | 105512 | An open-source AI agent that brings the power of Gemini directly into your terminal. | agent, ecosystem |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 83445 | RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge | agent, ecosystem |
| [aaif-goose/goose](https://github.com/aaif-goose/goose) | 50069 | an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and  | agent, ecosystem |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | 48075 | Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, s | agent, ecosystem |
| [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | 15689 | MCP Toolbox for Databases is an open source MCP server for databases. | agent, ecosystem |
| [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector) | 10167 | Visual testing tool for MCP servers | agent, ecosystem |
| [0x4m4/hexstrike-ai](https://github.com/0x4m4/hexstrike-ai) | 9860 | HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, GPT, Copilot, etc.) a | agent, ecosystem |
| [refly-ai/refly](https://github.com/refly-ai/refly) | 7396 | The first open-source agent skills builder. Define skills by vibe workflow, run on Claude Code, Curs | agent, ecosystem |
| [steipete/agent-rules](https://github.com/steipete/agent-rules) | 5693 | Rules and Knowledge to work better with agents such as Claude Code or Cursor | agent, ecosystem |
| [intellectronica/ruler](https://github.com/intellectronica/ruler) | 2773 | Ruler — apply the same rules to all coding agents | agent, ecosystem |
| [ciembor/agent-rules-books](https://github.com/ciembor/agent-rules-books) | 1938 | AGENTS.md rules / skills for AI coding agents: Codex, Cursor & Claude Code. Inspired by Clean Code,  | agent, ecosystem |
| [IsHexx/system-prompts-and-models-of-ai-tools-chinese](https://github.com/IsHexx/system-prompts-and-models-of-ai-tools-chinese) | 1194 | AI编程工具中文提示词合集，包含Cursor、Devin、VSCode Agent等多种AI编程工具的提示词，为中文开发者提供AI辅助编程参考资源。持续更新中文编程Rules和最新AI编程提示词。 | agent, ecosystem |
| [instructa/ai-prompts](https://github.com/instructa/ai-prompts) | 1052 | Curated AI Prompts for Cursor Rules, Cline, Windsurf and Github Copilot | agent, ecosystem |
| [ModelEngine-Group/nexent](https://github.com/ModelEngine-Group/nexent) | 5265 | Nexent is a zero-code platform for auto-generating production-grade AI agents using Harness Engineer | agent, ecosystem |
| [EvoAgentX/EvoAgentX](https://github.com/EvoAgentX/EvoAgentX) | 3088 | 🚀 EvoAgentX: Building a Self-Evolving Ecosystem of AI Agents | agent, ecosystem |
| [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | 3891 | AI-assisted TradingView chart analysis — connect Claude Code to your TradingView Desktop for persona | agent, ecosystem |
| [SomeOddCodeGuy/WilmerAI](https://github.com/SomeOddCodeGuy/WilmerAI) | 817 | WilmerAI is one of the oldest LLM semantic routers. It uses multi-layer prompt routing and complex w | agent, ecosystem |
| [lofcz/LLMTornado](https://github.com/lofcz/LLMTornado) | 621 | The .NET library to build AI agents with 30+ built-in connectors. | agent, ecosystem |
| [timothy-odofin/agenthub-be](https://github.com/timothy-odofin/agenthub-be) | 570 | Open-source RAG platform with multi-LLM support. Build AI agents that connect to your data, tools, a | agent, ecosystem |
| [makafeli/n8n-workflow-builder](https://github.com/makafeli/n8n-workflow-builder) | 526 | AI assistant integration for n8n workflow automation through Model Context Protocol (MCP). Connect C | agent, ecosystem |

| [ruvnet/metaharness](https://github.com/ruvnet/metaharness) | 355 | 🛠️ The meta-harness for AI agents — scaffold your own focused, branded agent harness with its own np | agent, ecosystem |
| [zhu1090093659/spec_driven_develop](https://github.com/zhu1090093659/spec_driven_develop) | 909 | Spec-driven development workflow for AI coding agents: architecture-first planning, task decompositi | agent, ecosystem |
| [DjangoPeng/agent-hub](https://github.com/DjangoPeng/agent-hub) | 339 | This repository is a hub for AI Agent projects, including GitHub Sentinel, LanguageMentor, and ChatP | agent, ecosystem |
| [groupzer0/vs-code-agents](https://github.com/groupzer0/vs-code-agents) | 274 | A multi-agent workflow system for GitHub Copilot in VS Code that brings structure, quality gates, an | agent, ecosystem |
| [google-labs-code/jules-action](https://github.com/google-labs-code/jules-action) | 203 | Add a powerful cloud coding agent to your GitHub workflows | agent, ecosystem |
| [marcuspat/turbo-flow](https://github.com/marcuspat/turbo-flow) | 163 | Advanced Agentic Development Environment for DevPods, GitHub Codespaces, Rackspace Spot & more. Rufl | agent, ecosystem |
| [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | 1099 | Multi-AI MCP Server - Connect ChatGPT, Claude, Gemini & Perplexity to your coding tools without any  | agent, ecosystem |
| [iansinnott/obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp) | 309 | Connect Claude Code and other AI tools to your Obsidian notes using Model Context Protocol (MCP) | agent, ecosystem |
| [HarmonicSecurity/claudit-sec](https://github.com/HarmonicSecurity/claudit-sec) | 292 | Security audit tool for Claude Desktop and Claude Code on macOS — single-command visibility into MCP | agent, ecosystem |
| [Glade-tool/glade-mcp](https://github.com/Glade-tool/glade-mcp) | 167 | Connect any MCP-compatible AI client (Claude Code, Cursor, Windsurf) to Unity or Godot. 235+ granula | agent, ecosystem |
| [mixelpixx/SSH-MCP](https://github.com/mixelpixx/SSH-MCP) | 49 | A Model Context Protocol (MCP) server that provides SSH access to remote servers, allowing AI tools  | agent, ecosystem |

## New Additions — June 25, 2026

| Repository | Stars | Description |
|-----------|-------|-------------|
| [rolandpg/zettelforge](https://github.com/rolandpg/zettelforge) | 50 | Agentic memory for CTI — STIX knowledge graphs, threat-actor alias resolution |
| [QuantaSeal/mcp-server](https://github.com/QuantaSeal/mcp-server) | 0 | QuantaSeal MCP Server — 18 tools for AI agents |
| [invertible-statue269/colign](https://github.com/invertible-statue269/colign) | 2 | Align teams on specs before AI writes code |
| [Lucenx9/forktty](https://github.com/Lucenx9/forktty) | 6 | Linux-native workspace for coding agents — Ghostty terminals, git worktrees |
| [yun520-1/mark-heartflow-skill](https://github.com/yun520-1/mark-heartflow-skill) | 26 | 心虫 (HeartFlow) — Cognitive state encoder + autonomous decision engine via MCP |
