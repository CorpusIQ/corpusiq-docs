---
title: "Agent Coherence MCP — Multi-Agent File Conflict Prevention"
description: "Stop AI agents from silently overwriting each other's shared files — a single-host coherence guard, TLA+-verified."
category: mcp
tags: [mcp-server, agent-infrastructure, coherence, multi-agent, filesystem]
last_updated: 2026-07-12
---

# Agent Coherence MCP Server ★ New (July 12)

Stop AI agents from silently overwriting each other's shared files — a single-host coherence guard for multi-agent systems. Uses TLA+-verified algorithms to prevent file conflicts when multiple agents access the same filesystem concurrently.

**Source:** mcp.so (submitted July 12, 2026) · **Author:** Vlad Parakhin

## What It Is

Agent Coherence is an infrastructure MCP server that prevents multi-agent file corruption. When multiple AI agents share a filesystem (e.g., a project directory, a docs repo, a shared workspace), concurrent writes can silently overwrite each other. This server provides file-level locking, version tracking, and conflict detection — verified correct with TLA+ formal methods.

## Business Relevance

- **Platform operators** running multi-agent systems need file integrity guarantees
- **Dev teams** with multiple coding agents sharing a repo need write conflict prevention
- **Content operators** with multiple agents updating docs need version consistency
- **CorpusIQ complement** for any team running 2+ Hermes agents on shared infrastructure

## Tools Available

| Tool | Description |
|------|-------------|
| `acquire_lock` | Request exclusive write access to a file |
| `release_lock` | Release file lock after write completes |
| `check_conflicts` | Detect if any agent's changes conflict with current state |
| `list_locks` | Show all active file locks and their owners |
| `get_version` | Get current version/hash of a file |

## Quick Start

```bash
# Install via npx
npx @vparakhin/agent-coherence-mcp

# Or add to MCP client config
{
  "mcpServers": {
    "agent-coherence": {
      "command": "npx",
      "args": ["@vparakhin/agent-coherence-mcp"],
      "env": {
        "WATCH_DIR": "/path/to/shared/workspace"
      }
    }
  }
}
```

## Business Use Cases

1. **Multi-agent docs editing:** 3 agents updating the same knowledge base — Coherence ensures no silent overwrites
2. **Code generation pipelines:** Agent A generates code while Agent B reviews — Coherence prevents review of stale files
3. **Shared configuration management:** Multiple agents updating system configs — version tracking prevents drift
4. **Agent audit trail:** Track which agent wrote what, when, with full version history

## Limitations

- Single-host only (not distributed — one machine, multiple agents)
- File-level granularity (not line-level — whole file locks)
- Requires agents to use the lock/check/release protocol (cooperative, not enforced)
- New project; production hardening likely needed
- TLA+ verification covers the algorithm, not the implementation

## See Also

- [SPM Structured Project Memory](/hermes/mcp/servers/external/spm-structured-project-memory/) — Project memory management
- [MCP Long-Term Memory](/hermes/mcp/servers/external/mcp-long-term-memory/) — Agent memory persistence
