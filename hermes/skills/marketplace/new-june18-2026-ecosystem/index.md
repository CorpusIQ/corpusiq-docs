---
title: "New Skills"
description: 12 newly catalogued Hermes ecosystem skills from plastic-labs/honcho (memory/context) and garrytan/gbrain (agent brain operations)  --  essential infrastructure for production Hermes agents.
---

# New Skills  --  June 18, 2026 (Ecosystem Tools)

**Source:** [plastic-labs/honcho](https://skills.sh/plastic-labs/honcho) and [garrytan/gbrain](https://skills.sh/garrytan/gbrain) via [skills.sh](https://skills.sh)
**Date:** June 18, 2026
**Total new:** 12 skills (4 Honcho + 8 GBrain)

These skills were previously uncatalogued despite being widely used in the Hermes agent ecosystem. Honcho provides persistent memory and context derivation for agents; GBrain provides the brain layer for agent knowledge management.

---

## Honcho  --  Agent Memory & Context (4 skills)

Honcho is the persistent memory system used by CorpusIQ Hermes agents for context preservation across sessions, conversation derivation, and peer-aware memory.

| # | Skill | Installs | Description |
|---|-------|----------|-------------|
| 1 | `honcho-integration` | 534 | Core Honcho MCP integration  --  connect agents to persistent memory, sessions, and peer context |
| 2 | `honcho-cli` | 243 | Honcho CLI for managing workspaces, peers, sessions, and conclusions from the terminal |
| 3 | `migrate-honcho` | 235 | Migrate Honcho data between deployments  --  schema migrations, backup/restore |
| 4 | `migrate-honcho-ts` | 235 | TypeScript Honcho migration toolkit  --  same as migrate-honcho for TS codebases |

### Installation

```bash
# Core integration
npx skills add plastic-labs/honcho/honcho-integration

# CLI management
npx skills add plastic-labs/honcho/honcho-cli

# Migration tooling
npx skills add plastic-labs/honcho/migrate-honcho
```

### Relevance to Hermes Agents

Honcho is the memory backbone of CorpusIQ's Hermes agent infrastructure. Every session starts with `honcho_get_peer_context()` to recover channel status, token state, and active rules. The `honcho-integration` skill provides the MCP tools that make this possible: `honcho_chat`, `honcho_get_peer_context`, `honcho_create_conclusions`, and session management.

---

## GBrain  --  Agent Brain Layer (8 skills)

GBrain is Garry Tan's agent brain layer  --  a markdown-based knowledge management system for AI agents using vault-based storage and retrieval.

| # | Skill | Installs | Description |
|---|-------|----------|-------------|
| 1 | `brain-ops` | 221 | Core brain operations  --  search, ingest, maintain the knowledge vault |
| 2 | `idea-ingest` | 178 | Capture and structure ideas into the brain's vault format |
| 3 | `meeting-ingestion` | 163 | Process meeting transcripts into structured knowledge entries |
| 4 | `enrich` | 162 | Enrich existing brain entries with cross-references, tags, and metadata |
| 5 | `citation-fixer` | 131 | Validate and fix citations in brain entries  --  source verification |
| 6 | `data-research` | 130 | Research-oriented data ingestion with structured extraction |
| 7 | `media-ingest` | 130 | Process media files (audio, video, images) into brain knowledge |
| 8 | `daily-task-manager` | 129 | Daily task tracking and prioritization integrated with the brain |

### Installation

```bash
# Core brain operations
npx skills add garrytan/gbrain/brain-ops

# Specialized ingestion
npx skills add garrytan/gbrain/idea-ingest
npx skills add garrytan/gbrain/meeting-ingestion
npx skills add garrytan/gbrain/enrich

# Research and media
npx skills add garrytan/gbrain/data-research
npx skills add garrytan/gbrain/media-ingest
```

### Relevance to Hermes Agents

CorpusIQ uses GBrain as the persistent knowledge layer for Hermes agents  --  session handoff pages, system state documentation, and operational knowledge all live in GBrain vaults. The `brain-ops` skill enables searching and maintaining this knowledge; `idea-ingest` and `meeting-ingestion` feed new information into the agent's persistent memory.

---

## Quick Reference

| Category | Skills | Top Install | Key Use Case |
|----------|--------|-------------|--------------|
| Honcho | 4 | honcho-integration (534) | Agent memory & session persistence |
| GBrain | 8 | brain-ops (221) | Agent knowledge vault management |
| **Total** | **12** | | |

---

*← [Marketplace Home](/hermes/skills/marketplace/) | [Previous Discovery (June 18 Batch 2)](/hermes/skills/marketplace/new-june18-2026-batch2/) →*
