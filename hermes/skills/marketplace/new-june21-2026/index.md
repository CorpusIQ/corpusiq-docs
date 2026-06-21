---
title: New Hermes Skills — June 21, 2026
description: 34 newly discovered Hermes Agent skill repos — knowledge graph discovery, 169-page community bible, workflow precipitation, sync, cybersecurity, deployment, copywriting, OCR, and personal setups
---

# New Skills: June 21, 2026

**Discovered:** June 21, 2026 via GitHub API search (`hermes+skill+in:name,description+created:>2026-06-19`)
**New repos:** 34 | **ECOSYSTEM ACCELERATION:** Largest single-day discovery since Hermes launch

---

## Category 1: Architectural Innovation (3 repos)

Pushing Hermes Agent capabilities forward with novel infrastructure patterns.

### nuffin/hermes-skill-graph — Knowledge Graph Skill Discovery (0⭐)

**Architectural innovation.** A knowledge-graph layer for Hermes skill discovery — FTS5 full-text search, term matching, and typed relationships between skills. Instead of flat `skills/` directories, skills are nodes in a graph with edges representing dependencies, conflicts, and synergies.

| Feature | Detail |
|---------|--------|
| Search | FTS5 full-text indexing across all installed skills |
| Relationships | Typed edges (depends_on, conflicts_with, supersedes, composes_with) |
| Discovery | Term matching + graph traversal for related-skill suggestions |
| Structure | SKILL.md compliant + plugin system |

**Repo:** [nuffin/hermes-skill-graph](https://github.com/nuffin/hermes-skill-graph) | **Stars:** 0 | **Created:** June 21, 2026
**Install:** `git clone` → `./install.sh` → registers as Hermes plugin

---

### luxuguang-leo/hermes-skill-precipitator — Workflow Pattern Discovery (⭐1)

**Self-improving agent capability.** Automatically discovers reusable workflow patterns from Hermes Agent session history and "precipitates" them into new skills. Watches your sessions, identifies repeated multi-step patterns, extracts them as SKILL.md templates.

| Feature | Detail |
|---------|--------|
| Input | Hermes session history / Honcho session DB |
| Output | SKILL.md files with discovered workflow patterns |
| Pipeline | Observe → Cluster → Extract → Template → Validate |
| Install | `python3 install.py` |

**Repo:** [luxuguang-leo/hermes-skill-precipitator](https://github.com/luxuguang-leo/hermes-skill-precipitator) | **Stars:** 1 | **Created:** June 20, 2026

---

### Liminal0426/hermes-sync — Multi-Device Sync (0⭐)

**Infrastructure utility.** Sync skills, config, cron jobs, and memory across multiple Hermes Agent devices. Designed for operators running Hermes on DGX + Mac Mini + laptop.

| Feature | Detail |
|---------|--------|
| Sync targets | Skills, config, cron, memory, Honcho sessions |
| Transport | SSH / rsync |
| Conflict | Last-write-wins with backup |
| Install | `pip install -e .` from repo |

**Repo:** [Liminal0426/hermes-sync](https://github.com/Liminal0426/hermes-sync) | **Stars:** 0 | **Created:** June 20, 2026

---

## Category 2: Community Knowledge Base (1 repo)

### DeployFaith/hermes-bible-skill — 169-Page Community Knowledge Base (⭐3)

**LARGEST community contribution to the Hermes ecosystem.** 169 pages of documentation covering 25+ real-world agent flows, hidden features, SOUL.md patterns, and operational playbooks gathered from production Hermes deployments.

| Section | Pages | Topics |
|---------|-------|--------|
| Flows | 25+ | Autonomous coding, research pipelines, email operations, social media, infrastructure |
| SOUL.md | Deep dive | Profile architecture, personality engineering, constraint systems |
| Hidden Features | 30+ | Undocumented CLI flags, config tricks, tool edge cases |
| Bundles | 5 | Pre-packaged skill bundles for common use cases |
| References | 40+ | Command reference, error codes, model routing, token optimization |

**Repo:** [DeployFaith/hermes-bible-skill](https://github.com/DeployFaith/hermes-bible-skill) | **Stars:** 3 | **Created:** June 21, 2026
**Install:** `npx skills add DeployFaith/hermes-bible-skill`

---

## Category 3: Domain-Specific Tools (7 repos)

### vmamuaya/shodan-integration-skill — Cybersecurity/OSINT (0⭐)

Shodan integration for cybersecurity workflows: attack surface management, OSINT reconnaissance, vulnerability enrichment, asset discovery, and incident response. Hermes Agent skill.

**Repo:** [vmamuaya/shodan-integration-skill](https://github.com/vmamuaya/shodan-integration-skill) | **Stars:** 0 | **Created:** June 20, 2026

---

### edgarstool/deploy-pilot — Deployment Workflow (0⭐)

Compose-first deployment workflow: detect → compose → healthcheck → rollback. Supports PM2 and systemd as advanced modes. SKILL.md compliant.

**Repo:** [edgarstool/deploy-pilot](https://github.com/edgarstool/deploy-pilot) | **Stars:** 0 | **Created:** June 20, 2026

---

### nineinfra/ninchat-skills — Real-Time Search Infrastructure (0⭐)

Real-time information retrieval and search infrastructure for Hermes Agent and OpenClaw. Ninchat integration for live data pipelines.

**Repo:** [nineinfra/ninchat-skills](https://github.com/nineinfra/ninchat-skills) | **Stars:** 0 | **Created:** June 21, 2026

---

### Asmadey/twenty-crm-skill — Twenty CRM CLI (0⭐)

Twenty CRM integration via openapi-to-cli (ocli). Hermes skill for CRM operations.

**Repo:** [Asmadey/twenty-crm-skill](https://github.com/Asmadey/twenty-crm-skill) | **Stars:** 0 | **Created:** June 20, 2026

---

### kyzqdcs1968-dcs/hermes-skill-local-ocr — Chinese Legal OCR (⭐1)

Offline OCR for Chinese legal documents via macOS Vision framework. Privacy-preserving — all processing local.

**Repo:** [kyzqdcs1968-dcs/hermes-skill-local-ocr](https://github.com/kyzqdcs1968-dcs/hermes-skill-local-ocr) | **Stars:** 1 | **Created:** June 20, 2026

---

### HenryArinaga/ios-simulator-capture — iOS Screenshots (0⭐)

Hermes skill for iOS Simulator screenshots and screen recordings. Useful for mobile testing workflows.

**Repo:** [HenryArinaga/ios-simulator-capture](https://github.com/HenryArinaga/ios-simulator-capture) | **Stars:** 0 | **Created:** June 20, 2026

---

### bolin8017/retail-price-tracker-mcp — Retail Price Tracking (0⭐)

MCP server and Hermes skill for tracking retail product prices, starting with UNIQLO Taiwan.

**Repo:** [bolin8017/retail-price-tracker-mcp](https://github.com/bolin8017/retail-price-tracker-mcp) | **Stars:** 0 | **Created:** June 20, 2026

---

## Category 4: Content, Writing & Cognition (5 repos)

### cobibean/website-copywriting-skill — Proof-Backed Copywriting (0⭐)

Hermes-compatible skill for proof-backed, trust-preserving website copywriting. Conversion-focused with evidence requirements.

**Repo:** [cobibean/website-copywriting-skill](https://github.com/cobibean/website-copywriting-skill) | **Stars:** 0 | **Created:** June 20, 2026

---

### thanhan-a17/vietnamese-writer-skill — Native Vietnamese Writing (0⭐)

Forces LLMs to think in Vietnamese before generating content. Native-quality Vietnamese writing skill.

**Repo:** [thanhan-a17/vietnamese-writer-skill](https://github.com/thanhan-a17/vietnamese-writer-skill) | **Stars:** 0 | **Created:** June 20, 2026

---

### lunkerchen/li-chiada-perspective — Decision Intelligence Framework (0⭐)

Minerva 78 Thinking Habits + Decision Intelligence cognitive framework for Hermes Agent. Structured critical thinking.

**Repo:** [lunkerchen/li-chiada-perspective](https://github.com/lunkerchen/li-chiada-perspective) | **Stars:** 0 | **Created:** June 20, 2026

---

### yinbing-666/hermes-frontend-skills — UI Engineering Skills (0⭐)

Hermes frontend design skill collection: UI engineering, web design, design system references, UI refactoring. Chinese-language.

**Repo:** [yinbing-666/hermes-frontend-skills](https://github.com/yinbing-666/hermes-frontend-skills) | **Stars:** 0 | **Created:** June 20, 2026

---

### moeacgx/hermes-red-team-mode-skills — Red Team Operations (0⭐)

Red team mode skills for adversarial testing and security validation. No description provided.

**Repo:** [moeacgx/hermes-red-team-mode-skills](https://github.com/moeacgx/hermes-red-team-mode-skills) | **Stars:** 0 | **Created:** June 20, 2026

---

## Category 5: Health & Niche Domains (2 repos)

### navyxiong/family-health-os-skill — Family Medical Records (0⭐)

Hermes Agent skill for managing family lifetime medical records. Bilingual (EN/ZH) documentation with examples and install scripts.

**Repo:** [navyxiong/family-health-os-skill](https://github.com/navyxiong/family-health-os-skill) | **Stars:** 0 | **Created:** June 21, 2026

---

### sharpcj/wechat-article-skills-for-hermes — WeChat Articles (0⭐)

WeChat article skills for Hermes Agent. Chinese social media content pipeline.

**Repo:** [sharpcj/wechat-article-skills-for-hermes](https://github.com/sharpcj/wechat-article-skills-for-hermes) | **Stars:** 0 | **Created:** June 21, 2026

---

## Category 6: Personal Setup & Config Repos (14 repos)

Community members sharing their personal Hermes configurations, skills collections, and setup backups.

| Repo | Description | Created |
|------|-------------|---------|
| [shivang2000/personal-hermes-agent-setup](https://github.com/shivang2000/personal-hermes-agent-setup) | Sanitized config, skills, setup backup | June 21 |
| [seraprotocol-ship-it/hermes-setup-pack](https://github.com/seraprotocol-ship-it/hermes-setup-pack) | Migration pack for clean Mac Mini install | June 20 |
| [oniondai/hermes_awesome](https://github.com/oniondai/hermes_awesome) | Reusable skills + scripts (Tavily, GitHub Hub) | June 21 |
| [light-saber/hermes-agent-portfolio](https://github.com/light-saber/hermes-agent-portfolio) | Portfolio showcasing 79 skills | June 21 |
| [Nuparu55/hermes-shared-skills](https://github.com/Nuparu55/hermes-shared-skills) | Shared skills for Hermes Agent | June 21 |
| [devirayib/hermes-extensions](https://github.com/devirayib/hermes-extensions) | Custom Hermes skills and plugins | June 21 |
| [Phantasmaa/hermes-backup](https://github.com/Phantasmaa/hermes-backup) | Skills, memories, scripts, cron, config backup | June 21 |
| [Wandersonjack/avocado-skills](https://github.com/Wandersonjack/avocado-skills) | Model-aware skill templates for Super Agent | June 21 |
| [AveryLemon/Hermes_V2](https://github.com/AveryLemon/Hermes_V2) | Hermes Agent v2 — skills, config, memory, cron | June 20 |
| [david-internal/hermes-obsidian-self-organizing-vault](https://github.com/david-internal/hermes-obsidian-self-organizing-vault) | Obsidian vault curator + starter templates | June 21 |
| [mmansillaf/hermes-skills](https://github.com/mmansillaf/hermes-skills) | Token-optimization + context-engineering (Spanish) | June 20 |
| [reclaw17/hermes-skills](https://github.com/reclaw17/hermes-skills) | Human 2.0 chat-digest + misc (Russian) | June 20 |
| [nxz1026/Hermes_Skills](https://github.com/nxz1026/Hermes_Skills) | Skills collection | June 21 |
| [khuchinque-app/hermes-chinque2](https://github.com/khuchinque-app/hermes-chinque2) | Multi-agent pipeline setup | June 20 |

---

## Category 7: Edge Cases & Adjacent (2 repos)

### erza-di/urban-oracle-frontend-style — Codex Frontend Design (⭐1)

Codex frontend design skill mimicking the Hermes Agent visual language. Adjacent ecosystem — Codex skill, not Hermes-native.

**Repo:** [erza-di/urban-oracle-frontend-style](https://github.com/erza-di/urban-oracle-frontend-style) | **Stars:** 1 | **Created:** June 20, 2026

---

### vdgbcrypto/cockpit-ws-skill — Cockpit Web Server (0⭐)

Containerized Cockpit web server management with bastion mode, SSH access. Hermes Agent compatible.

**Repo:** [vdgbcrypto/cockpit-ws-skill](https://github.com/vdgbcrypto/cockpit-ws-skill) | **Stars:** 0 | **Created:** June 20, 2026

---

## Setup Guides

Dedicated setup guides created for the 3 highest-impact skills:

| Skill | Guide | Why |
|-------|-------|-----|
| **hermes-skill-graph** | [Setup →](/hermes/skills/catalog/hermes-skill-graph-setup/) | Architectural innovation: knowledge graph for skill discovery |
| **hermes-bible-skill** | [Setup →](/hermes/skills/catalog/hermes-bible-skill-setup/) | Largest community contribution: 169 pages of operational knowledge |
| **hermes-skill-precipitator** | [Setup →](/hermes/skills/catalog/hermes-skill-precipitator-setup/) | Self-improving: auto-discover workflows from session history |

---

## Ecosystem Pattern

**34 new repos in 2 days (June 20-21)** — the Hermes Agent ecosystem is accelerating. Key trends:

1. **Architecture infra** emerging — skill graphs, sync tools, workflow discovery
2. **Domain specialization** — cybersecurity (Shodan), CRM (Twenty), health (medical records)
3. **Internationalization** — Chinese, Vietnamese, Russian, Spanish, Korean skills appearing
4. **Personal config sharing** — 14 personal setup repos as community normalizes sharing
5. **169-page knowledge base** signals maturation — community is codifying operational knowledge

---

*← [Previous Discoveries](/hermes/skills/marketplace/new-june20-2026-update/) | [Next Page →](/hermes/skills/marketplace/)*
*↑ [Marketplace Home](/hermes/skills/marketplace/)*
