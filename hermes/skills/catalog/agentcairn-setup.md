---
title: "AgentCairn — Obsidian-Based Long-Term Agent Memory"
description: "Set up AgentCairn to give Hermes agents persistent cross-project memory using your Obsidian vault as the source of truth."
---

# AgentCairn Setup Guide

**Repo:** [ccf/agentcairn](https://github.com/ccf/agentcairn)
**Stars:** ⭐20 | **License:** Apache-2.0 | **Language:** Python
**Install:** `pip install agentcairn`

## Overview

AgentCairn provides long-term, cross-project memory for AI coding agents. Instead of opaque vector databases, it uses your own Obsidian vault as the source of truth — your memory, your files, your control. Includes a native Hermes plugin, DuckDB for fast retrieval, and MCP server for agent integration.

**Key capabilities:**
- Obsidian vault as memory source (markdown-native)
- Cross-project context — learnings from one project help others
- DuckDB-powered semantic search (no external vector DB)
- Hermes plugin for auto-memory injection
- MCP server for any agent harness
- Daemonless — no background processes

## Prerequisites

- Hermes Agent v0.15.0+
- Python 3.10+
- Obsidian vault (existing or new)
- 500MB+ free disk space

## Installation

```bash
# Via pip
pip install agentcairn

# Install Hermes plugin
agentcairn install-hermes-plugin

# Or clone and install manually
git clone https://github.com/ccf/agentcairn.git
cd agentcairn
pip install -e .
```

## Configuration

```yaml
# ~/.hermes/config.yaml  
plugins:
  agentcairn:
    vault_path: "~/Documents/Obsidian"  # Path to your Obsidian vault
    auto_index: true                     # Index vault on Hermes start
    injection_mode: context              # context | prompt | both
    max_tokens: 4000                     # Max tokens to inject per session
```

## Usage

AgentCairn auto-injects relevant memories at session start. You can also query manually:

```bash
# Index your vault
agentcairn index --vault ~/Documents/Obsidian

# Search memories
agentcairn search "python async patterns"

# See what AgentCairn knows about a topic
agentcairn context "CorpusIQ deployment"

# Start MCP server for other agents
agentcairn serve --port 9090
```

## Verification

```bash
# Test indexing
agentcairn index --vault ~/Documents/Obsidian --dry-run

# Test search
agentcairn search "test query"

# Check plugin status
hermes plugins list | grep agentcairn
```

## Pitfalls

- Large vaults (>10K notes) may take 2-3 minutes for initial indexing
- Obsidian vault must be on local disk (no network mounts)
- DuckDB database at `~/.agentcairn/` can grow to 1-2GB
- Markdown files should have YAML frontmatter for best indexing results
