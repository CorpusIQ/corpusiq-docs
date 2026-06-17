---
title: New Skills Discovery — June 9, 2026
description: 25 newly discovered skills.sh marketplace skills relevant to Hermes agents. Communication bots, Hermes variants, agent infrastructure, DevOps, and platform integrations.
---

# New Skills Discovery — June 9, 2026

Batch scan of [skills.sh](https://skills.sh) discovered **25 new skills** not previously cataloged. All are relevant to Hermes agent operations across 5 new categories.

---

## 1. Nous Research Hermes Agent Variants (5)

Additional variants of `nousresearch/hermes-agent` beyond the base `hermes-agent` skill.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `nousresearch/hermes-agent@dogfood` | 3.6K | Dogfood/edge build of Hermes Agent — latest features |
| `nousresearch/hermes-agent@yuanbao` | 443 | Hermes + Yuanbao (Tencent AI) integration |
| `nousresearch/hermes-agent@popular-web-designs` | 169 | Web design generation patterns via Hermes |
| `nousresearch/hermes-agent@llm-wiki` | 156 | LLM knowledge base / wiki integration |
| `nousresearch/hermes-agent@powerpoint` | 153 | PowerPoint/presentation generation via Hermes |

Install: `npx skills add nousresearch/hermes-agent@<variant>`

---

## 2. Communication Platform Bots (4)

Turn Hermes agents into interactive bots on major messaging platforms.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `claude-office-skills/skills@telegram-bot` | 3.1K | Telegram bot with full messaging API |
| `claude-office-skills/skills@whatsapp-automation` | 3.4K | WhatsApp messaging and workflow automation |
| `claude-office-skills/skills@slack-workflows` | 2.8K | Slack app with message sending, channels, reactions |
| `claude-office-skills/skills@discord-bot` | 2.8K | Discord bot with channels, messaging, moderation |

Install: `npx skills add claude-office-skills/skills@<platform>-<action>`

**Relevance to CorpusIQ**: Deploy CorpusIQ agents as interactive bots in operator communities (Slack, Discord).

---

## 3. Agent Infrastructure — Orchestration & RAG (6)

New orchestration patterns and RAG implementations for multi-agent systems.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `wshobson/agents@rag-implementation` | 9.5K | Production RAG pipeline: chunking, embedding, retrieval |
| `langchain-ai/langchain-skills@langchain-rag` | 8.6K | LangChain-native RAG with vectorstores |
| `wshobson/agents@workflow-orchestration-patterns` | 8.2K | Agent workflow patterns: fan-out, pipeline, DAG |
| `wshobson/agents@saga-orchestration` | 7.1K | Saga pattern for distributed agent transactions |
| `qodex-ai/ai-agent-skills@multi-agent-orchestration` | 1.7K | Multi-agent coordination and task delegation |
| `sickn33/antigravity-awesome-skills@ai-agents-architect` | 1.1K | AI agent system architecture design |

Install: `npx skills add <owner/repo>@<skill>`

**Relevance to CorpusIQ**: Directly applicable to CorpusIQ's CrewAI + LangGraph orchestration layer and GBrain knowledge retrieval.

---

## 4. Infrastructure & DevOps (5)

Production infrastructure skills for deploying and monitoring agent systems.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `neondatabase/agent-skills@neon-postgres` | 40.3K | Serverless Postgres — ideal for agent state storage |
| `sickn33/antigravity-awesome-skills@docker-expert` | 18.9K | Docker containerization for agent services |
| `jeffallan/claude-skills@kubernetes-specialist` | 10.2K | K8s deployment patterns for agent clusters |
| `wshobson/agents@deployment-pipeline-design` | 9.2K | CI/CD pipeline design for agent deployments |
| `jeffallan/claude-skills@monitoring-expert` | 3K | Monitoring and observability for production agents |

Install: `npx skills add <owner/repo>@<skill>`

**Relevance to CorpusIQ**: Neon Postgres for session DB, Docker/K8s for Mac Mini + DGX infrastructure, monitoring for cron audit.

---

## 5. Platform Integrations & Automation (5)

Direct integrations with platforms CorpusIQ agents interact with.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `intellectronica/agent-skills@notion-api` | 42.1K | Full Notion API: pages, databases, blocks |
| `claude-office-skills/skills@notion-automation` | 2.7K | Automated Notion workflows for agents |
| `resend/resend-skills@agent-email-inbox` | 3.3K | Email inbox for AI agents via Resend |
| `claude-office-skills/skills@browser automation` | 3K | Cross-platform browser automation patterns |
| `heygen-com/skills@create-video` | 946 | HeyGen video creation for agents |
| `alirezarezvani/claude-skills@social-media-analyzer` | 1.2K | Analyze social media content programmatically |

Install: `npx skills add <owner/repo>@<skill>`

**Relevance to CorpusIQ**: Notion for knowledge management, Resend for agent email ops, HeyGen for UGC video pipeline.

---

## Summary

| Category | New Skills | Top Install |
|----------|:---------:|-------------|
| Hermes Variants | 5 | dogfood (3.6K) |
| Communication Bots | 4 | WhatsApp (3.4K) |
| Agent Infrastructure | 6 | RAG Implementation (9.5K) |
| Infrastructure & DevOps | 5 | Neon Postgres (40.3K) |
| Platform Integrations | 6 | Notion API (42.1K) |
| **Total New** | **26** | |

**Catalog impact**: Marketplace skills grow from 85 → 111. Total catalog from 158 → 184.

All skills installable via `npx skills add <owner/repo>@<skill>`. No additional configuration required beyond Hermes agent's existing tool access.

*← [Skills.sh Marketplace](/hermes/skills/marketplace/) | [Skills Catalog](/hermes/skills/catalog/) →*

*↑ [Skills Home](/hermes/skills/)*


---
*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*


---
*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
