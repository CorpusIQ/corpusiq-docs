---
title: "Agent Flywheel Mega-Toolkit Setup Guide"
description: "Install and configure the Agent Flywheel — 25+ production-grade ClawDBot/Hermes skills covering SSH, deployment, browser automation, multi-agent orchestration, Discord, email, and terminal workflows."
---

# Agent Flywheel Mega-Toolkit Setup Guide

**Published by:** [dicklesworthstone](https://github.com/dicklesworthstone) | **Repo:** [agent_flywheel_clawdbot_skills_and_integrations](https://github.com/dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations)
**Skills:** 25+ | **Combined installs:** 2,201 | **Compatible with:** Hermes Agent, ClawDBot, OpenClaw

---

## Overview

The Agent Flywheel is the most comprehensive single-publisher ClawDBot/Hermes toolkit discovered to date. It covers the complete agent operations lifecycle — from SSH server access to multi-agent swarming, browser automation, code quality enforcement, Discord/email communication, and terminal workflows. Built by a developer who also maintains pi_agent_rust, beads_rust, and eidetic_engine_cli (agent infrastructure repos), these skills are production-tested and designed for real workload automation.

**What makes this different:** Most skill collections focus on a single domain (marketing, coding, deployment). The Agent Flywheel covers ALL domains — infrastructure, orchestration, communication, development, design, and terminal — under one publisher with consistent conventions.

### Skill Categories

| Category | Skills | Use Case |
|----------|--------|----------|
| **Infrastructure** | ssh (652), gcloud (208), vercel (54) | Server access, cloud deployment |
| **Orchestration** | agent-swarm-workflow (156), planning-workflow (142), agent-fungibility (51) | Multi-agent coordination |
| **Communication** | agent-mail (77), flywheel-discord (57) | Email + Discord messaging |
| **Development** | github (89), cursor (84), tanstack-integration (55) | Git workflows, IDE integration |
| **Browser** | claude-chrome (81) | Web browsing and automation |
| **Design** | ui-ux-polish (202), de-slopify (88) | UI refinement, content cleanup |
| **Terminal** | ghostty (57), wezterm (54), building-glamorous-tuis (67*) | Terminal emulators and TUIs |
| **Database** | supabase (61) | Database operations |
| **Security** | csctf (56) | CTF and security workflows |
| **Utilities** | cass (80), bv (70), ubs (64), cm (62), ntm (58), dcg (56), caam (53), slb (51), giil (50), ru (51) | Code quality, workflows, helpers |

*Note: building-glamorous-tuis is from dicklesworthstone/meta_skill (67 installs), compatible with the same agent setup.

---

## Prerequisites

- Hermes Agent or ClawDBot installed
- `npx` (Node.js) for skills.sh installation
- SSH key configured (for ssh, gcloud, vercel skills)
- Discord bot token (for flywheel-discord)
- Gmail API credentials (for agent-mail)
- Supabase project (for supabase skill)

---

## Quick Start

Install the most-used skills in one batch:

```bash
# Core infrastructure
npx skills add dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations --skill ssh
npx skills add dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations --skill gcloud
npx skills add dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations --skill vercel

# Multi-agent orchestration
npx skills add dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations --skill agent-swarm-workflow
npx skills add dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations --skill planning-workflow

# Communication
npx skills add dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations --skill agent-mail
npx skills add dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations --skill flywheel-discord

# Development
npx skills add dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations --skill github
npx skills add dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations --skill claude-chrome

# Quality
npx skills add dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations --skill de-slopify
npx skills add dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations --skill ui-ux-polish
```

---

## Key Skills in Detail

### ssh (652 installs)
SSH server access and command execution for Hermes agents. Enables agents to connect to remote servers, run commands, transfer files, and manage infrastructure.

**Configuration:**
```bash
# SSH key must be available in agent's environment
export SSH_KEY_PATH=~/.ssh/id_rsa
```

**Hermes use:** Server maintenance, deployment verification, log retrieval from production.

### agent-swarm-workflow (156 installs)
Multi-agent coordination pattern. Enables Hermes to spawn and manage sub-agents for parallel task execution — research in parallel, divide-and-conquer code generation, multi-perspective analysis.

**Hermes use:** Complex research tasks, parallel data processing, multi-source content generation. Pairs with CorpusIQ's own [supervisor-agent](/hermes/orchestration/) patterns.

### claude-chrome (81 installs)
Browser automation through Chrome. Enables Hermes agents to navigate websites, fill forms, extract data, and interact with web UIs.

**Hermes use:** Web scraping, form automation, SaaS tool interaction without APIs, competitive research.

### agent-mail (77 installs)
Email sending and receiving through Gmail API. Agents can read inbox, send replies, and manage email workflows autonomously.

**Configuration:**
```bash
# Requires Gmail API OAuth credentials
export GMAIL_CLIENT_ID=your_client_id
export GMAIL_CLIENT_SECRET=your_client_secret
export GMAIL_REFRESH_TOKEN=your_refresh_token
```

**Hermes use:** Automated email monitoring, customer support triage, newsletter drafting.

### supabase (61 installs)
Database operations through Supabase. CRUD operations, real-time subscriptions, and auth management.

**Configuration:**
```bash
export SUPABASE_URL=https://your-project.supabase.co
export SUPABASE_ANON_KEY=your_anon_key
export SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
```

**Hermes use:** Application backend, data storage for agent workflows, user management.

---

## Installation Strategy

**Tier 1 — Core Infrastructure (install first):**
- ssh, gcloud, vercel — server and deployment access
- github — code management

**Tier 2 — Agent Capabilities (high value):**
- agent-swarm-workflow, planning-workflow — multi-agent orchestration
- claude-chrome — web browsing
- agent-mail, flywheel-discord — communication channels

**Tier 3 — Quality and Polish:**
- de-slopify, ui-ux-polish — content and design refinement
- cass, csctf — code quality and security

**Tier 4 — Specialized Tools (install as needed):**
- supabase — database access
- ghostty, wezterm — terminal customization
- tanstack-integration — frontend development

---

## CorpusIQ Use Cases

1. **Growth Operations:** Use `claude-chrome` + `de-slopify` for competitive research and content refinement. Use `agent-mail` for automated outreach monitoring.

2. **Multi-Agent Research:** `agent-swarm-workflow` + `planning-workflow` for parallel market research across multiple data sources.

3. **Infrastructure Automation:** `ssh` + `gcloud` for managing CorpusIQ's DGX Spark and Mac Mini worker nodes.

4. **Community Management:** `flywheel-discord` for Discord community engagement, `agent-mail` for email support.

5. **Code Quality:** `github` + `cass` for automated PR review and code quality enforcement.

---

## Troubleshooting

### SSH connection failures
Verify the SSH key is in the agent's environment and has correct permissions (`chmod 600`). Test with `ssh -T user@host` before delegating to the agent.

### Discord bot not responding
Ensure `DISCORD_BOT_TOKEN` is set and the bot has been invited to the target server with appropriate permissions (Send Messages, Read Message History).

### Gmail API quota exceeded
Gmail API has a 1,000,000 unit/day quota for free tier. Batch email operations and use push notifications instead of polling.

### Agent swarm spawning too many sub-agents
The `agent-swarm-workflow` skill supports a `--max-agents` parameter. Set to a reasonable limit for your hardware (start with 3-5).

---

*← [June 28 Update 3 Discovery](/hermes/skills/marketplace/new-june28-2026-update3/) | [Skills Catalog Home](/hermes/skills/catalog/) →*

---

*This guide is part of the Hermes Skills Library, curated by [CorpusIQ](https://www.corpusiq.io) — one MCP endpoint, all your business tools. Content remains attributed to original authors and repositories.*
