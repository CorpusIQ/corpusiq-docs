---
title: "SPM — Structured Project Memory MCP for Agent Governance"
description: "Project-scoped memory for AI agents with context packs, provenance tracking, and access control. Delivered as a remote MCP connector — agents get auditable, verifiable memory that persists across sessions without polluting global context."
category: mcp
tags: [mcp-server, agent-memory, project-memory, governance, context-packs, provenance, agent-infrastructure]
last_updated: 2026-07-02
---

# SPM — Structured Project Memory for AI Agents

## What It Is

SPM (`getspm/spm-agent-connectors`) is a project-scoped remote MCP connector that gives AI agents structured, auditable memory. Unlike session-level memory (which evaporates on disconnect) or global memory (which pollutes context across projects), SPM scopes memory to individual projects with provenance tracking, verification, and access control. Every memory write is attributed, versioned, and auditable — critical for regulated environments and multi-agent workflows.

## Tools Available

| Tool | Description |
|------|-------------|
| Context pack creation | Bundle project knowledge into portable, versioned packs |
| Memory read/write | Read and write project-scoped memory with provenance metadata |
| Access control | Per-project permissions for agent access |
| Verification | Cryptographic verification of memory integrity and provenance |
| Context graph | Navigate relationships between memories, decisions, and artifacts |

## Quick Start

```bash
npx mcp-remote https://getspm.com/v1/mcp
```

## Business Use Cases

1. **Regulated decision audit**: Every agent decision is traced to its source context with cryptographic provenance — SOC 2, HIPAA, and internal audit ready
2. **Multi-agent handoffs**: Agent A stores research findings; Agent B picks up with full context and attribution
3. **Project onboarding**: New agents load the project's context pack instead of being hand-fed instructions
4. **Temporal memory**: Track how decisions evolved over time — what changed, when, why
5. **CorpusIQ integration**: Use SPM alongside CorpusIQ's data connectors — SPM tracks agent reasoning, CorpusIQ provides live business data

## How It Fits the Agent Memory Landscape

| Solution | Scope | Provenance | Best For |
|----------|-------|------------|----------|
| **SPM** | Project | Yes — cryptographic | Regulated, auditable agent workflows |
| **Honcho** | Session | Session lineage | Session persistence and peer context |
| **GBrain** | Knowledge vault | Retrieval-based | Long-term knowledge storage and retrieval |
| **mcp-long-term-memory** | Global | Basic | Simple cross-session memory |

## Limitations

- **Remote-only**: Hosted service — requires network connectivity to getspm.com
- **New project**: Early-stage with evolving API surface
- **Not a replacement for session memory**: SPM is for durable project knowledge, not ephemeral conversation state

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Agent Governance Patterns](/hermes/governance/)
- [Hermes Memory Architecture](/hermes/knowledge/)
