---
title: "🆕 July 1, 2026 — Official Hermes Gap Sweep: 11 New Core Skills + Hermes Ecosystem Expansion (49 total)"
description: "New Hermes skills discovered July 1, 2026: 11 official Hermes Agent skills, 23 Hermes ecosystem skills, 15 ClawSec security skills. First discovery of these core utilities missed in previous sweeps."
---

# 🆕 July 1, 2026 — 49 New Hermes Skills Discovered

**Date:** July 1, 2026
**New Skills:** 49 | **Sources:** 3 repos

Comprehensive gap sweep of skills.sh comparing the official `nousresearch/hermes-agent` repo against our catalog. Found 11 core Hermes utility skills that were previously undocumented — utilities that have been available but overlooked in prior sweeps. Also discovered 23 new skills from `aradotso/hermes-skills` (Hermes ecosystem expansion) and 15 from `prompt-security/clawsec` (agent security suite).

---

## New Skills at a Glance

### Official Hermes Agent (11 skills — nousresearch/hermes-agent)

| # | Skill | Description |
|---|-------|-------------|
| 1 | **blogwatcher** | Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool |
| 2 | **cloudflare-temporary-deploy** | Deploy Workers live with `wrangler --temporary` (no account needed) |
| 3 | **codex** | Delegate coding tasks to OpenAI Codex CLI (features, PRs) |
| 4 | **computer-use** | Drive the user's desktop in the background — clicking, typing |
| 5 | **creative-ideation** | Generate ideas via named methods from creative practice |
| 6 | **here.now** | Publish static sites to `{slug}.here.now` and store files for agent-to-agent handoff |
| 7 | **himalaya** | IMAP/SMTP email from terminal via Himalaya CLI |
| 8 | **honcho** | Cross-session user modeling, multi-profile peer isolation, dialectic reasoning |
| 9 | **petdex** | Install and select animated petdex mascots for Hermes |
| 10 | **research-paper-writing** | Write ML papers for NeurIPS/ICML/ICLR — design through submit |
| 11 | **yuanbao** | Yuanbao (元宝) groups: @mention users, query info/members |

---

### Hermes Ecosystem (23 skills — aradotso/hermes-skills)

These are community-contributed skills from the dedicated Hermes Agent skills repository.

#### Agent Infrastructure & Control

| # | Skill | Description |
|---|-------|-------------|
| 1 | **hermes-agent-control-room** | Centralized control room for managing Hermes agent operations |
| 2 | **hermes-agent-framework** | Hermes Agent framework — architecture and conventions |
| 3 | **hermes-agent-guide** | Comprehensive guide for setting up and using Hermes Agent |
| 4 | **hermes-agent-mission-control** | Mission control dashboard for monitoring active agents |
| 5 | **hermes-agent-architecture** | Architecture patterns and system design for Hermes deployments |
| 6 | **hermes-agent-optimization** | Performance optimization and tuning for Hermes agents |
| 7 | **hermes-agent-self-evolution** | Autonomous improvement and self-modification patterns |
| 8 | **hermes-atlas-ecosystem-map** | Visual map of the entire Hermes ecosystem |
| 9 | **hermes-labyrinth-observability** | Observability and monitoring for Hermes agent deployments |
| 10 | **hermes-lcm-context-management** | Lifecycle context management for long-running agents |

#### Desktop & UI

| # | Skill | Description |
|---|-------|-------------|
| 11 | **hermes-cn-desktop** | Hermes desktop client with Chinese localization |
| 12 | **hermes-control-interface-dashboard** | Web dashboard for controlling Hermes agents |
| 13 | **hermes-desktop-os1-native-macos-client** | Native macOS Hermes client with OS-level integration |
| 14 | **hermes-hudui-consciousness-monitor** | HUD UI for monitoring agent consciousness/state |

#### Integrations & Connectors

| # | Skill | Description |
|---|-------|-------------|
| 15 | **hermes-ide-terminal** | IDE-integrated terminal for Hermes agent interaction |
| 16 | **hermes-kanban-obsidian-integration** | Obsidian-based kanban board for agent task management |
| 17 | **hermes-paperclip-adapter** | Paperclip adapter — connects Hermes to external tools |
| 18 | **hermes-feishu-streaming-card** | Feishu/Lark streaming card integration for real-time updates |
| 19 | **deepseek-openclaw-config-generator** | Auto-generate OpenClaw configs from DeepSeek model specs |
| 20 | **deepseek-openclaw-integration** | DeepSeek model integration for OpenClaw agents |

#### Education & Discovery

| # | Skill | Description |
|---|-------|-------------|
| 21 | **awesome-hermes-agent-ecosystem** | Curated list of Hermes Agent tools, skills, and resources |
| 22 | **hermes-edu-skills** | Educational skills for learning Hermes Agent development |
| 23 | **hermes-dec-bytecode-reverse-engineering** | DEC bytecode reverse engineering toolkit for Hermes |

---

### ClawSec Security Suite (15 skills — prompt-security/clawsec)

Comprehensive security toolkit for the OpenClaw/Clawbot agent ecosystem. Many skills are directly applicable to Hermes agent security.

| # | Skill | Description |
|---|-------|-------------|
| 1 | **clawsec-suite** | Umbrella security suite — vulnerability scanning and posture assessment |
| 2 | **soul-guardian** | Guards agent personality against prompt injection and identity drift |
| 3 | **clawsec-clawhub-checker** | Security checks for ClawHub package submissions |
| 4 | **clawsec-feed** | Security intelligence feed for agent threats |
| 5 | **clawsec-scanner** | Vulnerability scanner for agent deployments |
| 6 | **clawsec-nanoclaw** | Lightweight security checks for resource-constrained agents |
| 7 | **clawtributor** | Supply chain security verification for agent dependencies |
| 8 | **claw-release** | Secure release management for agent software |
| 9 | **prompt-agent** | Prompt injection detection and mitigation |
| 10 | **openclaw-audit-watchdog** | Continuous security audit monitoring for agents |
| 11 | **openclaw-traffic-guardian** | Network traffic monitoring and anomaly detection |
| 12 | **picoclaw-security-guardian** | Minimal security guardian for lightweight agent deployments |
| 13 | **picoclaw-self-pen-testing** | Autonomous penetration testing for agent deployments |
| 14 | **picoclaw-traffic-guardian** | Lightweight traffic monitoring for pico agents |
| 15 | **nanoclaw-traffic-guardian** | Nano-scale traffic monitoring for embedded agents |

---

## Category Breakdown

### Developer Utilities (11 official Hermes skills)

These 11 skills from the official `nousresearch/hermes-agent` repo fill important gaps in our catalog. They cover email (himalaya), content monitoring (blogwatcher), deployment (cloudflare-temporary-deploy), coding delegation (codex), desktop automation (computer-use), creative tools (creative-ideation), publishing (here.now), memory (honcho), personalization (petdex), academic writing (research-paper-writing), and Chinese platform integration (yuanbao).

**Key finds:**
- **honcho** — Cross-session memory is the backbone of persistent agent identity. This skill was inexplicably missing from the catalog.
- **blogwatcher** — RSS/Atom feed monitoring enables automated content discovery without API keys.
- **himalaya** — Terminal-based email is essential for headless agent email operations.
- **petdex** — Animated mascots add personality to the agent experience.

### Hermes Ecosystem (23 skills)

The `aradotso/hermes-skills` repo is a dedicated community hub for Hermes Agent extensions. These 23 skills span agent infrastructure (control room, mission control, self-evolution), desktop interfaces (macOS native client, HUD UI), integrations (Obsidian kanban, Feishu streaming), and education (ecosystem maps, edu skills).

**Key finds:**
- **hermes-agent-self-evolution** — Autonomous improvement patterns for Hermes agents
- **hermes-labyrinth-observability** — Production-grade monitoring for agent deployments
- **hermes-desktop-os1-native-macos-client** — Full native macOS Hermes experience
- **deepseek-openclaw-integration** — Integration for DeepSeek models with agent operations

### Security (15 ClawSec skills)

The `prompt-security/clawsec` repo provides the first comprehensive security toolkit for agent ecosystems. While targeting Claw/OpenClaw, the prompt injection detection, supply chain verification, and traffic monitoring are universally applicable to Hermes deployments.

---

## Installation

All skills are installable via the skills.sh CLI:

```bash
# Official Hermes skills
npx skills add nousresearch/hermes-agent --skill blogwatcher
npx skills add nousresearch/hermes-agent --skill honcho
npx skills add nousresearch/hermes-agent --skill himalaya

# Hermes ecosystem
npx skills add aradotso/hermes-skills --skill hermes-agent-control-room
npx skills add aradotso/hermes-skills --skill hermes-agent-self-evolution

# Security
npx skills add prompt-security/clawsec --skill soul-guardian
```

---

## Comparison

| Metric | Count |
|--------|:-----:|
| Official Hermes skills on skills.sh | 192 |
| Previously documented in catalog | 129 |
| New this sweep | 49 |
| Total skills.sh catalog | 192 |
