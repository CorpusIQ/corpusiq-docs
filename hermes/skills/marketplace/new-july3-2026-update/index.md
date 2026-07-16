---
title: "July 3, 2026 (Update) — Hermes Hybrid Memory + 5 More Skills"
description: "6 additional Hermes-relevant repos discovered in the late July 3 sweep: Hybrid Memory plugin (graph+vector+holographic), MCP ChatGPT bridge, Agent Bookmarks for Notion, MoA Synthesis decision discipline, BDH Graph Harness, and RedSeek Rescue."
---

# 🆕 July 3, 2026 (Update) — 6 Additional Repos Discovered

**Date:** July 3, 2026 (Late Sweep)
**New Repos:** 6 | **New Skills/Tools:** 6 | **Combined Stars:** 1

A follow-up sweep of the `hermes-agent` GitHub topic surfaced 6 repos not captured in the morning sweep. The standout is **Hermes Hybrid Memory** — a production-grade MemoryProvider plugin that replaces flat system-prompt memory with a unified graph + vector + holographic store in a single SQLite file.

---

## New at a Glance

| # | Project | Stars | Type | Category | Source |
|---|---------|:-----:|------|----------|--------|
| 1 | **Hermes Hybrid Memory** | 0 | Plugin | Memory/AI | sheldon904/hermes-hybrid-memory |
| 2 | **ChatGPT Web Prompt MCP** | 0 | Skill | Multi-Model | blankyname/chatgpt-web-prompt-mcp-skill |
| 3 | **Agent Bookmarks** | 0 | Skill | Productivity | noderguru/agent-bookmarks |
| 4 | **MoA Synthesis** | 0 | Skill | Safety/Routing | cryptyroot-ux/moa-synthesis |
| 5 | **BDH Graph Harness** | 1 | MCP Server | Knowledge Graph | albidev/bdh-graph-harness |
| 6 | **RedSeek Rescue** | 0 | Tool | System Recovery | rednicv/redseek-rescue |

---

## Category Breakdown

### Memory & Agent Infrastructure (1 project)

#### Hermes Hybrid Memory (0⭐) ⭐ Setup Guide Available

**Repo:** [sheldon904/hermes-hybrid-memory](https://github.com/sheldon904/hermes-hybrid-memory)
**Author:** sheldon904
**Language:** Python
**License:** MIT

A custom `MemoryProvider` plugin for Hermes Agent that replaces flat system-prompt memory with a unified store combining **structured facts**, **semantic vector recall (sqlite-vec)**, and a **knowledge graph** — all in one SQLite file. Includes Hofstadter-inspired mechanisms: analogy slot, emergent chunking, usage-driven forgetting (never age-driven), and a brain visualization tool.

**Key features:**
- FTS5 full-text search + sqlite-vec (384-dim) vector search
- Knowledge graph with nodes/edges maintained incrementally
- Hofstadter-inspired analogy-making ("structurally similar but superficially different")
- Emergent chunking — compresses raw experience into reusable categories
- Usage-driven forgetting — naturally decays unused memories
- Brain visualization tool (`brain_viz.py`) — interactive graph explorer
- Production-tested (several weeks of real agent use)
- MIT licensed, Python 3.11+

**Setup Guide:** [Hermes Hybrid Memory — Full Setup Guide](/hermes/skills/catalog/hermes-hybrid-memory-setup/)

```bash
# Clone into your Hermes plugins directory
git clone https://github.com/sheldon904/hermes-hybrid-memory.git
cd hermes-hybrid-memory
pip install -r requirements.txt

# Configure in hermes config.yaml:
# memory_provider: hybrid_memory
# memory_store_path: ~/.hermes/memory/memory_store.db
```

**Why this matters:** Most agent memory is either a system-prompt scratchpad or a vector dump. Hybrid Memory adds a real knowledge graph underneath, maintained incrementally for free, and makes retrieval intentional about structural similarity (analogy) as well as semantic similarity. This is the kind of memory infrastructure that separates forgetful agents from ones that build compound understanding over time.

---

### Multi-Model & MCP Bridges (1 project)

#### ChatGPT Web Prompt MCP Skill (0⭐)

**Repo:** [blankyname/chatgpt-web-prompt-mcp-skill](https://github.com/blankyname/chatgpt-web-prompt-mcp-skill)
**Author:** blankyname
**Language:** JavaScript

Hermes/Claude MCP bridge skill for forwarding image prompts and reference images to ChatGPT Web via real Chrome CDP. Allows Hermes agents to leverage ChatGPT's image generation capabilities through browser automation.

**Key features:**
- MCP bridge between Hermes and ChatGPT Web
- Chrome CDP-based browser automation
- Image prompt forwarding with reference images
- Compatible with Hermes Agent and Claude Code

```bash
git clone https://github.com/blankyname/chatgpt-web-prompt-mcp-skill.git
# Install as Hermes MCP server — see repo README
```

---

### Productivity & Notion Integration (1 project)

#### Agent Bookmarks (0⭐)

**Repo:** [noderguru/agent-bookmarks](https://github.com/noderguru/agent-bookmarks)
**Author:** noderguru
**Language:** Python

Save any link to a Notion database with your AI agent — auto-classified, deduped, mirrored to Obsidian. A skill for Hermes Agent and any shell-capable agent.

**Key features:**
- Notion API integration for bookmark storage
- Auto-classification and deduplication
- Obsidian mirroring
- Telegram interface
- Self-hosted, Python-based

```bash
git clone https://github.com/noderguru/agent-bookmarks.git
# Configure Notion API token + database ID — see repo README
```

---

### Agent Safety & Decision Discipline (1 project)

#### MoA Synthesis (0⭐)

**Repo:** [cryptyroot-ux/moa-synthesis](https://github.com/cryptyroot-ux/moa-synthesis)
**Author:** cryptyroot-ux

A Hermes Agent skill for high-stakes decision escalation. Normal tasks stay fast and single-model; risky architecture, security, production, deployment, and research decisions are routed through a structured multi-model advisor panel, synthesized by an aggregator, and verified before final output.

**Key features:**
- Decision gate — classifies tasks for escalation
- Multi-model reference advisors (independent analysis, no tool execution)
- Aggregator synthesizes, reconciles disagreements, chooses path
- Verification step — smoke-test, red-team, or render-check
- Built on Hermes native MoA provider (not a replacement)
- Escalation discipline, not a generic multi-AI wrapper

```bash
# Install as Hermes skill
npx skills add cryptyroot-ux/moa-synthesis
```

**Why this matters:** As agents gain more autonomy and access (code, servers, credentials, deployment), knowing when NOT to trust the first answer becomes critical. MoA Synthesis gives Hermes a formal escalation discipline for high-stakes decisions.

---

### Knowledge Graph & Obsidian (1 project)

#### BDH Graph Harness (1⭐)

**Repo:** [albidev/bdh-graph-harness](https://github.com/albidev/bdh-graph-harness)
**Author:** albidev
**Language:** Python

Graph-based retrieval for Obsidian vaults with Hebbian synaptic plasticity. An MCP server that builds a knowledge graph from your Obsidian notes and uses neurogenesis-inspired algorithms for retrieval.

**Key features:**
- Graph-based retrieval (not just vector search)
- Hebbian learning — frequently co-activated nodes strengthen connections
- BM25 + ChromaDB + semantic search
- MCP server for Hermes Agent and Claude Desktop
- Ollama-compatible for local embeddings
- Neurogenesis-inspired graph maintenance

```bash
git clone https://github.com/albidev/bdh-graph-harness.git
cd bdh-graph-harness
pip install -r requirements.txt
# Configure as MCP server in hermes config.yaml
```

---

### System Recovery (1 project)

#### RedSeek Rescue (0⭐)

**Repo:** [rednicv/redseek-rescue](https://github.com/rednicv/redseek-rescue)
**Author:** rednicv
**Language:** Shell

AI-powered bootable USB for Windows repair. Built with Hermes Agent + DeepSeek. A live ISO that boots a minimal Linux environment with Hermes Agent pre-configured for diagnosing and repairing Windows systems.

```bash
git clone https://github.com/rednicv/redseek-rescue.git
# Build the live ISO — see repo README
```

---

## Why These Matter for Hermes Users

### Memory Infrastructure Maturation
The standout find is **Hermes Hybrid Memory** — it represents a step-change in agent memory architecture. Instead of dumping text into a system prompt or a vector store, it builds a real knowledge graph. The Hofstadter-inspired analogy mechanism is particularly interesting: it allows the agent to recall "structurally similar but superficially different" memories — the kind of associative recall humans excel at.

### Decision Discipline for Autonomous Agents
**MoA Synthesis** addresses a growing concern: as Hermes agents get more capable and autonomous, how do they know when to escalate? This skill formalizes the escalation decision, routing routine tasks through single-model paths while high-stakes decisions get multi-model review.

### Cross-Tool Bridges
**ChatGPT Web Prompt MCP** and **BDH Graph Harness** show the ecosystem building bridges — connecting Hermes to ChatGPT Web, Obsidian vaults, and Notion databases. These aren't just skills; they're infrastructure that extends what a Hermes agent can reach.

---

## Setup Guides Added

This sweep produced one detailed setup guide:
- **[Hermes Hybrid Memory Setup](/hermes/skills/catalog/hermes-hybrid-memory-setup/)** — Installation, configuration, memory ingestion pipeline, brain visualization, and production tuning

---

## Comparison

| Metric | Count |
|--------|:-----:|
| Previously documented in catalog | ~187 |
| New this sweep (morning) | 7 |
| New this sweep (update) | 6 |
| New setup guides created | 1 |
| Combined new stars | 1 |

---

*← [July 3 Morning Sweep](/hermes/skills/marketplace/new-july3-2026/) | [Marketplace Home](/hermes/skills/marketplace/) →*
*Powered by CorpusIQ*
