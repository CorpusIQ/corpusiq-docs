---
title: "🆕 July 4, 2026 — agent-sessions (683⭐) + Hermes ArXiv Agent + 22 More"
description: "24 new Hermes-relevant repos discovered July 4, 2026: agent-sessions macOS session browser (683⭐), Hermes ArXiv Agent (91⭐), memoria-vault research OS, cinematic-scroll-skill (9⭐), Hermes Meshtastic adapter, and more."
---

# 🆕 July 4, 2026 — 24 New Repos Discovered

**Date:** July 4, 2026
**New Repos:** 24 | **New Skills/Tools:** 24 | **Combined Stars:** 1,316

A sweep of the `hermes-agent` and `hermes-skill` GitHub topics surfaced 24 repos not captured in the July 3 sweeps. The standout is **agent-sessions** — a local-first macOS app (683⭐) for browsing, searching, and resuming AI coding-agent session histories across Hermes Agent, Claude Code, Codex, and Cursor.

---

## New at a Glance

### Top Tier (50+ Stars)

| # | Project | Stars | Type | Category | Source |
|---|---------|:-----:|------|----------|--------|
| 1 | **agent-sessions** | 683 | macOS App | Session Mgmt | jazzyalex/agent-sessions |
| 2 | **Hermes ArXiv Agent** | 91 | Skill | Research | genggng/hermes-arxiv-agent |
| 3 | **mark-heartflow-skill** | 30 | Skill | AI/RL | yun520-1/mark-heartflow-skill |

### Mid Tier (3–13 Stars)

| # | Project | Stars | Type | Category | Source |
|---|---------|:-----:|------|----------|--------|
| 4 | **tale** | 13 | Orchestrator | Multi-Agent | tale-project/tale |
| 5 | **cinematic-scroll-skill** | 9 | Skill | Web/Design | MustBeSimo/cinematic-scroll-skill |
| 6 | **logion** | 9 | Platform | Education | nicolasmelo1/logion |
| 7 | **hermes-agent-self-evolution** | 5 | Plugin | Optimization | Ephesian-kingpost533/hermes-agent-self-evolution |
| 8 | **memoria-vault** | 4 | Research | PKM/Obsidian | eranroseman/memoria-vault |
| 9 | **hermes-meshtastic-adapter** | 4 | Plugin | IoT/Hardware | amscotti/hermes-meshtastic-adapter |
| 10 | **persona-agent** | 4 | Agent | Personal | Code-MonkeyZhang/persona-agent |
| 11 | **hermes-companion** | 3 | Agent | Assistant | bdhhsx/hermes-companion |

### Base Tier (0–2 Stars)

| # | Project | Stars | Type | Category | Source |
|---|---------|:-----:|------|----------|--------|
| 12 | **cua-desktop-automation-skills** | 2 | Skills | macOS/Automation | ChrisLamDev/cua-desktop-automation-skills |
| 13 | **hermes-optimization-guide** | 2 | Guide | Performance | Guilhermepelido/hermes-optimization-guide |
| 14 | **hermes-CCC** | 2 | Skill | Claude Code | Arseni6361/hermes-CCC |
| 15 | **hermes-hud** | 2 | Tool | Monitoring | Lucasdjs22/hermes-hud |
| 16 | **hermes-doctor** | 2 | Plugin | Diagnostics | 503496348-ops/hermes-doctor |
| 17 | **hermes-flight-recorder** | 1 | Tool | Eval | zwright8/hermes-flight-recorder |
| 18 | **hermes-health-apollo** | 1 | Plugin | Health | vsj4394/hermes-health-apollo |
| 19 | **omnilimb** | 1 | Plugin | Hardware | national-jamesii265/omnilimb |
| 20 | **agent-supervision-skills** | 1 | Skills | DevOps | drippy-passport968/agent-supervision-skills |
| 21 | **hermes-mod** | 1 | Tool | UI/Theming | Joello2925/hermes-mod |
| 22 | **hermes-devops-skills** | 0 | Skills | DevOps/CI | ChrisLamDev/hermes-devops-skills |
| 23 | **Noshy** | 0 | MCP Server | Knowledge | slickpurse464/Noshy |
| 24 | **wikix** | 0 | Tool | PKM/Wiki | akshajsrivastava-exe/wikix |

---

## Category Breakdown

### Session Management (1 project)

#### agent-sessions (683⭐) ⭐ Setup Guide Available

**Repo:** [jazzyalex/agent-sessions](https://github.com/jazzyalex/agent-sessions)
**Author:** jazzyalex
**Language:** Swift
**Platform:** macOS (native)

Local-first macOS app to browse, search, analyze, and resume supported AI coding-agent session histories. Works with Hermes Agent, Claude Code, Codex, and Cursor. All session data stays local — no cloud sync, no telemetry.

**Key features:**
- Browse session history across multiple agent runtimes
- Full-text search across all conversation history
- Resume sessions from any supported agent
- Analyze conversation patterns and agent behavior
- Local-first — all data stays on device
- Native SwiftUI macOS app

**Setup Guide:** [agent-sessions — Full Setup Guide](/hermes/skills/catalog/agent-sessions-setup/)

```bash
# Download from GitHub Releases
# https://github.com/jazzyalex/agent-sessions/releases

# Or build from source:
git clone https://github.com/jazzyalex/agent-sessions.git
cd agent-sessions
open agent-sessions.xcodeproj
```

**Why this matters:** Agent session management is the missing piece in most agent workflows. When you run 50+ sessions across Hermes, Claude Code, and Codex in a week, finding "that one session where we fixed the gateway" becomes a needle-in-a-haystack problem. agent-sessions solves this with a unified, searchable, local-first browser. At 683 stars, the community agrees this is essential infrastructure.

---

### Research & Papers (1 project)

#### Hermes ArXiv Agent (91⭐) ⭐ Setup Guide Available

**Repo:** [genggng/hermes-arxiv-agent](https://github.com/genggng/hermes-arxiv-agent)
**Author:** genggng
**Language:** Python

A Hermes Agent skill that automatically fetches papers from arXiv daily, generates Chinese summaries and author affiliations via AI, pushes notifications to Feishu (Lark), and provides a local static reading website.

**Key features:**
- Daily arXiv paper fetching by category
- AI-generated Chinese summaries with author affiliations
- Feishu/Lark notification push
- Local static website for reading papers
- Hermes Agent skill architecture
- Configurable categories and keywords

**Setup Guide:** [Hermes ArXiv Agent — Full Setup Guide](/hermes/skills/catalog/hermes-arxiv-agent-setup/)

```bash
git clone https://github.com/genggng/hermes-arxiv-agent.git
cd hermes-arxiv-agent
# Configure in hermes config.yaml
```

**Why this matters:** Keeping up with arXiv is a constant pain for researchers and engineers. This skill automates the entire pipeline — fetching, summarizing, notifying, and hosting — within the Hermes ecosystem. At 91 stars, it's one of the most popular domain-specific Hermes skills.

---

### AI & Cognitive Engines (1 project)

#### mark-heartflow-skill (30⭐)

**Repo:** [yun520-1/mark-heartflow-skill](https://github.com/yun520-1/mark-heartflow-skill)
**Author:** yun520-1

HeartFlow — an AI cognitive engine for Hermes Agent: multi-path judgment, self-correcting RL, 3-layer memory (working/semantic/episodic), and U/D/A/H filtering (Useful/Dangerous/Ambiguous/Harmless). A complete cognitive architecture as a Hermes skill.

**Key features:**
- Multi-path judgment with self-correction
- Self-correcting reinforcement learning
- 3-layer memory: working, semantic, episodic
- U/D/A/H content and action filtering
- Hermes Agent skill integration

```bash
# Install as Hermes skill
npx skills add yun520-1/mark-heartflow-skill
```

---

### Multi-Agent Orchestration (1 project)

#### tale (13⭐)

**Repo:** [tale-project/tale](https://github.com/tale-project/tale)
**Author:** tale-project

The Orchestrator for AI Agents — connects OpenClaw, Hermes Agent, Claude Code, Codex, Cursor, Gemini CLI, and more under a single orchestration layer. Route tasks, share context, and manage agent lifecycles.

```bash
git clone https://github.com/tale-project/tale.git
cd tale
# Configure agents in tale.yaml
```

---

### Web & Design (1 project)

#### cinematic-scroll-skill (9⭐) ⭐ Setup Guide Available

**Repo:** [MustBeSimo/cinematic-scroll-skill](https://github.com/MustBeSimo/cinematic-scroll-skill)
**Author:** MustBeSimo
**Language:** TypeScript

Agent skill for building cinematic, scroll-driven websites from a brief: visual systems, motion storyboards, performance budgets, and production-ready HTML/CSS/JS output. Tell your Hermes agent what kind of site you want, and it builds a scroll-driven cinematic experience.

**Key features:**
- Visual system generation from briefs
- Motion storyboards with scroll-triggered animations
- Performance budgets and optimization
- Production-ready HTML/CSS/JS output
- Hermes Agent and Claude Code compatible

**Setup Guide:** [cinematic-scroll-skill — Full Setup Guide](/hermes/skills/catalog/cinematic-scroll-skill-setup/)

```bash
npx skills add MustBeSimo/cinematic-scroll-skill
```

---

### Education & Marketplace (1 project)

#### logion (9⭐)

**Repo:** [nicolasmelo1/logion](https://github.com/nicolasmelo1/logion)
**Author:** nicolasmelo1

Agent-native course marketplace and skill registry for executable AI-agent curricula. Publish, discover, and install educational skills that teach agents new capabilities through structured curricula.

```bash
git clone https://github.com/nicolasmelo1/logion.git
```

---

### Self-Evolution & Optimization (2 projects)

#### hermes-agent-self-evolution (5⭐)

**Repo:** [Ephesian-kingpost533/hermes-agent-self-evolution](https://github.com/Ephesian-kingpost533/hermes-agent-self-evolution)

Automate the evolution and optimization of Hermes Agent's prompts, skills, and code using genetic algorithms. Iteratively improves agent performance through mutation, crossover, and selection.

```bash
git clone https://github.com/Ephesian-kingpost533/hermes-agent-self-evolution.git
```

#### hermes-optimization-guide (2⭐)

**Repo:** [Guilhermepelido/hermes-optimization-guide](https://github.com/Guilhermepelido/hermes-optimization-guide)

Structured guides, installable skills, and tailored configurations for optimizing Hermes Agent performance. Covers model selection, token optimization, skill architecture, and memory tuning.

```bash
git clone https://github.com/Guilhermepelido/hermes-optimization-guide.git
```

---

### Research & PKM (2 projects)

#### memoria-vault (4⭐) ⭐ Setup Guide Available

**Repo:** [eranroseman/memoria-vault](https://github.com/eranroseman/memoria-vault)
**Author:** eranroseman

A research operating system — seven AI agents that read, enrich, and write inside your Obsidian vault. Each agent has a specialized role: researcher, summarizer, linker, critic, archivist, publisher, and orchestrator. Turns your Obsidian vault into an active research laboratory.

**Key features:**
- Seven specialized AI agents operating on your vault
- Researcher — reads and extracts from sources
- Summarizer — distills findings into concise notes
- Linker — connects ideas across notes
- Critic — challenges assumptions and finds gaps
- Archivist — organizes and maintains the vault
- Publisher — formats for external sharing
- Orchestrator — coordinates agent workflows

**Setup Guide:** [memoria-vault — Full Setup Guide](/hermes/skills/catalog/memoria-vault-setup/)

```bash
git clone https://github.com/eranroseman/memoria-vault.git
cd memoria-vault
# Configure Obsidian vault path and agent settings
```

**Why this matters:** Most AI + Obsidian integrations are single-agent (one model reading/writing notes). Memoria-vault deploys a full research team — seven agents with distinct roles — coordinated inside your vault. This is the research lab model applied to personal knowledge management.

---

### IoT & Hardware (2 projects)

#### hermes-meshtastic-adapter (4⭐) ⭐ Setup Guide Available

**Repo:** [amscotti/hermes-meshtastic-adapter](https://github.com/amscotti/hermes-meshtastic-adapter)
**Author:** amscotti
**Language:** Python

Hermes Agent platform plugin that connects Hermes to a Meshtastic LoRa mesh network. Receives plain-text messages from the mesh and can send responses back — enabling Hermes agent interaction over long-range, low-power radio networks.

**Key features:**
- Meshtastic LoRa mesh integration
- Receive and respond to mesh messages
- Off-grid agent communication
- Hermes Agent plugin architecture
- Python-based, lightweight

**Setup Guide:** [Hermes Meshtastic Adapter — Full Setup Guide](/hermes/skills/catalog/hermes-meshtastic-adapter-setup/)

```bash
git clone https://github.com/amscotti/hermes-meshtastic-adapter.git
cd hermes-meshtastic-adapter
pip install -r requirements.txt
```

**Why this matters:** This is one of the first Hermes plugins bridging the physical world. Meshtastic LoRa networks operate without cell towers or WiFi — this adapter lets a Hermes agent communicate in off-grid, disaster, or remote field scenarios.

#### omnilimb (1⭐)

**Repo:** [national-jamesii265/omnilimb](https://github.com/national-jamesii265/omnilimb)

Connect Hermes agents to physical hardware with a modular device abstraction layer. Framework for bridging agent actions to real-world devices, sensors, and actuators.

```bash
git clone https://github.com/national-jamesii265/omnilimb.git
```

---

### Developer Tools & Diagnostics (8 projects)

#### hermes-hud (2⭐)

**Repo:** [Lucasdjs22/hermes-hud](https://github.com/Lucasdjs22/hermes-hud)

Monitor AI agent memory, skills, and behavior in a live terminal HUD for Hermes. Real-time visibility into what your agent is thinking, remembering, and doing.

```bash
git clone https://github.com/Lucasdjs22/hermes-hud.git
```

#### hermes-doctor (2⭐)

**Repo:** [503496348-ops/hermes-doctor](https://github.com/503496348-ops/hermes-doctor)

Hermes Doctor (白龙马医生) — Hermes Agent self-diagnosis and self-healing plugin. Health checkups, prescription matching, repair plans, medical record accumulation, and Feishu message routing. Diagnose and fix your agent automatically.

```bash
git clone https://github.com/503496348-ops/hermes-doctor.git
```

#### hermes-flight-recorder (1⭐)

**Repo:** [zwright8/hermes-flight-recorder](https://github.com/zwright8/hermes-flight-recorder)

Trace-based scorecards and static reports for Hermes Agent autonomy evals. Record agent sessions and generate evaluation reports with trace-level detail.

```bash
git clone https://github.com/zwright8/hermes-flight-recorder.git
```

#### agent-supervision-skills (1⭐)

**Repo:** [drippy-passport968/agent-supervision-skills](https://github.com/drippy-passport968/agent-supervision-skills)

Delegate coding tasks to agents, collect artifacts, and verify results locally with standalone supervision. A framework for managing agent sub-tasks with verification gates.

```bash
git clone https://github.com/drippy-passport968/agent-supervision-skills.git
```

#### hermes-mod (1⭐)

**Repo:** [Joello2925/hermes-mod](https://github.com/Joello2925/hermes-mod)

Manage Hermes CLI skins in a web UI. Edit live YAML fields and save or activate skins with built-in version management. Theming for your terminal agent.

```bash
git clone https://github.com/Joello2925/hermes-mod.git
```

#### hermes-CCC (2⭐)

**Repo:** [Arseni6361/hermes-CCC](https://github.com/Arseni6361/hermes-CCC)

Integrate Hermes Agent skills directly into Claude Code for native agentic operations without external tooling. Bridge Hermes skills into the Claude Code environment.

```bash
git clone https://github.com/Arseni6361/hermes-CCC.git
```

#### hermes-devops-skills (0⭐)

**Repo:** [ChrisLamDev/hermes-devops-skills](https://github.com/ChrisLamDev/hermes-devops-skills)

14+ macOS & GitHub DevOps skills for AI coding agents — CI/CD, tooling, automation, and system diagnostics. A comprehensive DevOps skill pack for Hermes agents on macOS.

```bash
npx skills add ChrisLamDev/hermes-devops-skills
```

#### cua-desktop-automation-skills (2⭐)

**Repo:** [ChrisLamDev/cua-desktop-automation-skills](https://github.com/ChrisLamDev/cua-desktop-automation-skills)

Router Learning System + macOS desktop automation skills for AI agents using Cua Driver. Task routing and desktop control through a learning router.

```bash
npx skills add ChrisLamDev/cua-desktop-automation-skills
```

---

### Personal & Productivity (4 projects)

#### hermes-companion (3⭐)

**Repo:** [bdhhsx/hermes-companion](https://github.com/bdhhsx/hermes-companion)

Hermes Agent 2026: AI Assistant That Learns & Adapts. An open-source companion agent built on Hermes that evolves with usage.

```bash
git clone https://github.com/bdhhsx/hermes-companion.git
```

#### persona-agent (4⭐)

**Repo:** [Code-MonkeyZhang/persona-agent](https://github.com/Code-MonkeyZhang/persona-agent)

User-friendly Personal Agent for all. A simplified Hermes agent experience designed for non-technical users.

```bash
git clone https://github.com/Code-MonkeyZhang/persona-agent.git
```

#### hermes-health-apollo (1⭐)

**Repo:** [vsj4394/hermes-health-apollo](https://github.com/vsj4394/hermes-health-apollo)

Sync Oura, calendar, and email data to provide local-first health insights for the Hermes agent. Wellness and productivity tracking through your agent.

```bash
git clone https://github.com/vsj4394/hermes-health-apollo.git
```

#### wikix (0⭐)

**Repo:** [akshajsrivastava-exe/wikix](https://github.com/akshajsrivastava-exe/wikix)

Curate a persistent personal wiki with an LLM agent that processes sources into structured notes, summaries, and cross-references. Build your personal knowledge base automatically.

```bash
git clone https://github.com/akshajsrivastava-exe/wikix.git
```

---

### Knowledge & MCP (1 project)

#### Noshy (0⭐)

**Repo:** [slickpurse464/Noshy](https://github.com/slickpurse464/Noshy)

Provide persistent knowledge storage for AI agents using ICM and MCP standards to manage facts and memories. A knowledge backend for agent memory persistence.

```bash
git clone https://github.com/slickpurse464/Noshy.git
```

---

## Why These Matter for Hermes Users

### Session Management Goes Mainstream
**agent-sessions** (683⭐) signals that the community is ready for production-grade session tooling. Browsing, searching, and resuming sessions across multiple agent runtimes is no longer a nice-to-have — it's infrastructure.

### Domain Specialization Accelerates
This sweep shows Hermes skills penetrating specific domains: academic research (arXiv Agent), hardware/IoT (Meshtastic adapter, omnilimb), health (Apollo), and design (cinematic-scroll). The ecosystem is growing beyond general-purpose coding agents into specialized vertical tools.

### Cognitive Architecture Emerges
**mark-heartflow-skill** and **hermes-agent-self-evolution** represent a new category: skills that modify HOW Hermes thinks, not just WHAT it can do. Multi-path judgment, self-correcting RL, genetic optimization — these are meta-skills that improve the agent itself.

### Multi-Agent Coordination
**tale** (13⭐) and **memoria-vault** (4⭐) both deploy multiple coordinated agents. The pattern is clear: single agents are giving way to agent teams with specialized roles and orchestration layers.

---

## Setup Guides Added

This sweep produced 5 detailed setup guides:

- **[agent-sessions Setup](/hermes/skills/catalog/agent-sessions-setup/)** — macOS install, session browsing, search, cross-agent support
- **[Hermes ArXiv Agent Setup](/hermes/skills/catalog/hermes-arxiv-agent-setup/)** — arXiv API config, Feishu integration, local website hosting
- **[cinematic-scroll-skill Setup](/hermes/skills/catalog/cinematic-scroll-skill-setup/)** — Skill install, brief format, visual system generation
- **[memoria-vault Setup](/hermes/skills/catalog/memoria-vault-setup/)** — Obsidian vault config, 7-agent orchestration, role customization
- **[Hermes Meshtastic Adapter Setup](/hermes/skills/catalog/hermes-meshtastic-adapter-setup/)** — Hardware pairing, mesh config, message routing

---

## Comparison

| Metric | Count |
|--------|:-----:|
| Previously documented in catalog | ~194 |
| New this sweep | 24 |
| New setup guides created | 5 |
| Combined new stars | 1,316 |

---

*← [July 3 Update Sweep](/hermes/skills/marketplace/new-july3-2026-update/) | [Marketplace Home](/hermes/skills/marketplace/) →*
*Powered by CorpusIQ*
