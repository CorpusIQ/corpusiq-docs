---
title: New Skills Discovery — July 15, 2026
description: 6 new Hermes/OpenClaw ecosystem skills discovered via skills.sh API sweep. Memory hygiene, systemd/launchd deployment, security analysis, LLM ops, and customization tools.
---

# New Skills — July 15, 2026

Evening sweep across 18 broad queries surfaced **6 new skills** not previously catalogued in the Hermes docs. These span agent memory management, system service deployment, Web3 security analysis, LLM operations, and agent customization. Combined install base: **622+ installs**.

## Skills Discovered

| Skill | Installs | Source | Category |
|-------|----------|--------|----------|
| [memory-hygiene](#memory-hygiene) | 365 | aaaaqwq/claude-code-skills | Memory Management |
| [llm-ops](#llm-ops) | 70 | sickn33/antigravity-awesome-skills | LLM Operations |
| [linux-systemd](#linux-systemd) | 61 | alphaonedev/openclaw-graph | Deployment |
| [macos-launchd](#macos-launchd) | 56 | alphaonedev/openclaw-graph | Deployment |
| [openclaw-customizer](#openclaw-customizer) | 36 | petekp/claude-code-setup | Setup / Customization |
| [metamask-openclaw-desktop-security-analysis](#metamask-openclaw-desktop-security-analysis) | 34 | aradotso/hermes-skills | Security |

---

## memory-hygiene

**Source:** [aaaaqwq/claude-code-skills](https://github.com/aaaaqwq/claude-code-skills) · **365 installs** · **Homepage:** [xdylanbaker/memory-hygiene](https://github.com/xdylanbaker/memory-hygiene)

Audit, clean, and optimize Clawdbot/OpenClaw vector memory (LanceDB). Use when memory is bloated with junk, token usage is high from irrelevant auto-recalls, or setting up memory maintenance automation.

### Capabilities
- **Audit:** Check what's in vector memory with `memory_recall query="*" limit=50`
- **Wipe:** Clear all vector memory by removing the LanceDB directory
- **Reseed:** Store key facts after wipe using `memory_store`
- **Config:** Disable auto-capture (the main source of memory junk) while keeping auto-recall active

### Installation
```bash
npx skills add aaaaqwq/claude-code-skills/memory-hygiene
```

### Hermes/CorpusIQ Relevance
Directly applicable to Hermes agent memory management. Prevents the "memory bloat → token waste → degraded performance" cycle that plagues long-running agents. The `autoCapture: false` + `autoRecall: true` pattern preserves useful recall without accumulating garbage.

**Setup guide:** [memory-hygiene-setup.md](/hermes/skills/catalog/memory-hygiene-setup/)

---

## llm-ops

**Source:** [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) · **70 installs**

LLM Operations — RAG, embeddings, vector databases, fine-tuning, prompt engineering, LLM cost management, quality evals, and production AI architectures. Portuguese-language skill by renat.

### Capabilities
- RAG pipeline implementation
- Embeddings creation (Pinecone, Chroma, pgvector)
- Fine-tuning workflows
- Prompt engineering
- LLM cost reduction strategies
- Quality evaluations
- Semantic caching
- Streaming and agent architectures

### Installation
```bash
npx skills add sickn33/antigravity-awesome-skills/llm-ops
```

### Hermes/CorpusIQ Relevance
Covers the full LLM ops stack that CorpusIQ agents depend on: model routing, cost tracking, embedding pipelines, and production deployment patterns. The Portuguese content is machine-translatable and the technical patterns are language-agnostic.

**Setup guide:** [llm-ops-setup.md](/hermes/skills/catalog/llm-ops-setup/)

---

## linux-systemd

**Source:** [alphaonedev/openclaw-graph](https://github.com/alphaonedev/openclaw-graph) · **61 installs**

Deploy OpenClaw agents as Linux systemd services with proper supervision, logging, and restart policies. Part of the OpenClaw Graph ecosystem — a collection of deployment and infrastructure skills.

### Capabilities
- Systemd unit file generation for agent processes
- Restart policy configuration (on-failure, always)
- Journald log integration
- Resource limits (MemoryMax, CPUQuota)
- Environment variable injection
- User-level vs system-level service choice

### Installation
```bash
npx skills add alphaonedev/openclaw-graph/linux-systemd
```

### Hermes/CorpusIQ Relevance
CorpusIQ runs Hermes agents on DGX Spark (Linux). This skill provides canonical patterns for systemd service management — directly applicable to the gateway service, cron workers, and long-running agent processes.

**Setup guide:** [linux-systemd-setup.md](/hermes/skills/catalog/linux-systemd-setup/)

---

## macos-launchd

**Source:** [alphaonedev/openclaw-graph](https://github.com/alphaonedev/openclaw-graph) · **56 installs**

Deploy OpenClaw agents as macOS launchd services. The macOS equivalent of linux-systemd — provides plist generation, KeepAlive configuration, and launchctl management for agent processes.

### Capabilities
- LaunchAgent plist generation
- KeepAlive and RunAtLoad configuration
- StandardOutPath / StandardErrorPath log routing
- Environment variable dictionary
- launchctl bootstrap/bootout management

### Installation
```bash
npx skills add alphaonedev/openclaw-graph/macos-launchd
```

### Hermes/CorpusIQ Relevance
The Mac Mini worker node runs Hermes processes. This skill enables proper launchd supervision — replacing fragile cron-only or manual-start approaches with OS-native process management.

**Setup guide:** [macos-launchd-setup.md](/hermes/skills/catalog/macos-launchd-setup/)

---

## openclaw-customizer

**Source:** [petekp/claude-code-setup](https://github.com/petekp/claude-code-setup) · **36 installs**

Portable, version-controlled configuration for Claude Code and OpenAI Codex — fork, customize, sync across machines. Symlinks skill directories, scripts, and settings into the `~/.claude/` and `~/.codex/` directories.

### Capabilities
- Single-command setup via `./setup.sh`
- Symlink-based skill syncing across machines
- Shared MCP configuration (`.mcp.json`)
- Codex skill exclusion list
- Git-based version control for agent configs

### Installation
```bash
git clone https://github.com/petekp/claude-code-setup.git
cd claude-code-setup && ./setup.sh
```

### Hermes/CorpusIQ Relevance
Useful pattern for teams running multiple Hermes/Claude instances across machines. The symlink approach to skill management is directly applicable to CorpusIQ's multi-machine agent deployment (DGX + Mac Mini).

**Setup guide:** [openclaw-customizer-setup.md](/hermes/skills/catalog/openclaw-customizer-setup/)

---

## metamask-openclaw-desktop-security-analysis

**Source:** [aradotso/hermes-skills](https://github.com/aradotso/hermes-skills) · **34 installs** · **Author:** [ara.so](https://ara.so)

⚠️ **Security-focused skill.** Analyzes the Metamask Openclaw desktop executable distribution for security risks. Identifies impersonation patterns, suspicious binaries, and cryptocurrency scam red flags. This is a defensive security tool — it helps agents evaluate suspicious Web3 desktop software before execution.

### Capabilities
- Impersonation detection (Metamask has no official "Openclaw" product)
- Binary analysis of Windows `.exe` installers
- Brand misuse identification
- Web3 scam pattern recognition
- Security recommendation generation

### Installation
```bash
npx skills add aradotso/hermes-skills/metamask-openclaw-desktop-security-analysis
```

### Hermes/CorpusIQ Relevance
As Hermes agents gain more autonomous execution capabilities, security analysis skills become critical. This skill exemplifies the pattern of using agent skills for defensive security — evaluating external tools before granting them execution access.

**Setup guide:** [metamask-openclaw-security-analysis-setup.md](/hermes/skills/catalog/metamask-openclaw-security-analysis-setup/)

---

*Discovered via skills.sh API sweep — 18 broad queries across hermes, openclaw, clawdbot, honcho, gbrain ecosystems. Cross-referenced against all existing docs at corpusiq-docs/hermes/skills/.*
