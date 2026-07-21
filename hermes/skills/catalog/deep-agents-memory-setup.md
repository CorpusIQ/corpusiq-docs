---
title: Deep Agents Memory — LangChain Persistent Memory for Hermes Agents
description: Pluggable memory backends for LangChain Deep Agents. StateBackend (ephemeral), StoreBackend (persistent), FilesystemMiddleware, and CompositeBackend for routing. 12.8K+ installs.
---

# Deep Agents Memory — Setup Guide

**Source:** [langchain-ai/langchain-skills](https://skills.sh/langchain-ai/langchain-skills/deep-agents-memory) (12,800+ installs)
**Category:** Agent Infrastructure / Memory
**Quality Tier:** 🟡 Beta

LangChain's pluggable backend system for Deep Agents — providing short-term (ephemeral), long-term (persistent), and hybrid memory architectures. When your agent needs to remember state across threads, sessions, or invocations.

---

## Installation

```bash
# Python
pip install deepagents

# TypeScript
npm install deepagents
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python 3.10+** | For Python SDK |
| **Node.js 18+** | For TypeScript SDK |
| **LangChain** | `pip install langchain` or `npm install langchain` |

---

## Key Capabilities

### Backend Selection

| Use Case | Backend | Persistence |
|---|---|---|
| Temporary working files | **StateBackend** | Lost when thread ends |
| Local development CLI | **FilesystemBackend** | Direct disk access |
| Cross-session memory | **StoreBackend** | Persists across threads |
| Hybrid storage | **CompositeBackend** | Mix ephemeral + persistent |

### FilesystemMiddleware

Provides agent tools: `ls`, `read_file`, `write_file`, `edit_file`, `glob`, `grep`

---

## Quick Start

### Python

```python
from deepagents import create_deep_agent

# Default: StateBackend (ephemeral, within thread)
agent = create_deep_agent()
result = agent.invoke({
    "messages": [{"role": "user", "content": "Write notes to /draft.txt"}]
}, config={"configurable": {"thread_id": "thread-1"}})
# /draft.txt is lost when thread ends

# StoreBackend: persistent across threads
from deepagents.backends import StoreBackend
agent = create_deep_agent(backend=StoreBackend())

# CompositeBackend: route paths to different backends
from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
agent = create_deep_agent(backend=CompositeBackend({
    "/tmp/": StateBackend(),      # Ephemeral temp files
    "/data/": StoreBackend(),     # Persistent data
}))
```

### TypeScript

```typescript
import { createDeepAgent } from "deepagents";
import { StoreBackend, CompositeBackend, StateBackend } from "deepagents/backends";

// Persistent memory
const agent = createDeepAgent({ backend: new StoreBackend() });

// Hybrid: temp ephemeral, data persistent
const agent = createDeepAgent({
  backend: new CompositeBackend({
    "/tmp/": new StateBackend(),
    "/data/": new StoreBackend(),
  })
});
```

---

## Hermes Integration

For CorpusIQ Hermes agents, the StoreBackend pattern provides session-persistent memory:

### Architecture Recommendation

```
┌─────────────────────────────────────────┐
│              Hermes Agent                │
├─────────────────────────────────────────┤
│  CompositeBackend                        │
│  ┌─────────────┐  ┌──────────────────┐  │
│  │ StateBackend │  │  StoreBackend    │  │
│  │ /tmp/session │  │  /data/persist   │  │
│  │ (ephemeral)  │  │  (cross-session) │  │
│  └─────────────┘  └──────────────────┘  │
└─────────────────────────────────────────┘
```

### Use Cases

- **Session working files** → StateBackend (auto-cleaned)
- **Research findings** → StoreBackend (persist to GBrain)
- **Lead database** → StoreBackend (survives sessions)
- **Temporary scrapes** → StateBackend (disposable)

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Thread isolation | Each `thread_id` gets its own StateBackend namespace |
| Data loss after restart | Use StoreBackend for anything that must persist |
| Performance (large files) | Route large files to FilesystemBackend for direct disk I/O |
| TypeScript type errors | Ensure `deepagents` version matches LangChain version |

---

## See Also

- [[agentmemory-setup]] — AgentMemory integration for Hermes
- [[hermes-memory-stack-setup]] — Hermes native memory stack
- [[hermes-hybrid-memory-setup]] — Hybrid memory architecture
- [LangChain Deep Agents Docs](https://docs.langchain.com) — Official documentation
