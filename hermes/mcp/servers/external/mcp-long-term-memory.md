---
title: "MCP Long-Term Memory (GraphRAG) — Persistent Agent Memory"
description: "GraphRAG-backed long-term memory for AI agents via MCP. Neo4j knowledge graph storage for cross-session context persistence. First open-source GraphRAG MCP memory server."
category: mcp
tags: [mcp-server, graphrag, memory, neo4j, knowledge-graph, agent-infrastructure]
last_updated: 2026-07-02
---

# MCP Long-Term Memory — GraphRAG Memory Server

## What It Is

A Model Context Protocol (MCP) server that provides GraphRAG-based long-term memory to AI agents. Uses Neo4j for knowledge graph storage, enabling agents to persist, query, and evolve structured knowledge across sessions.

**GitHub**: https://github.com/null-create/mcp-long-term-memory (Python, new)

**Why GraphRAG**: Unlike simple vector stores that retrieve semantically similar chunks, GraphRAG builds a knowledge graph — entities, relationships, and communities — enabling multi-hop reasoning and structured recall that vectors alone cannot provide.

## Tools Available

| Tool | Description |
|------|-------------|
| `store_memory` | Persist a fact or observation into the knowledge graph |
| `query_memory` | Natural language query over the knowledge graph |
| `get_entity_context` | Retrieve all known facts about a specific entity |
| `find_relationships` | Discover relationships between entities |
| `summarize_topic` | Generate a structured summary of what the agent knows about a topic |

## Quick Start

```bash
# Prerequisites: Running Neo4j instance
docker run -d --name neo4j-mcp-memory \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/password \
  neo4j:latest

# Clone and install
git clone https://github.com/null-create/mcp-long-term-memory.git
cd mcp-long-term-memory
pip install -r requirements.txt

# Configure
export NEO4J_URI="bolt://localhost:7687"
export NEO4J_USER="neo4j"
export NEO4J_PASSWORD="password"

# Add to Hermes
hermes mcp add memory --command "python" --args "server.py" --workdir "$(pwd)" \
  --env NEO4J_URI NEO4J_USER NEO4J_PASSWORD
```

## Manual Configuration

```json
{
  "mcpServers": {
    "memory": {
      "command": "python",
      "args": ["server.py"],
      "workdir": "/path/to/mcp-long-term-memory",
      "env": {
        "NEO4J_URI": "bolt://localhost:7687",
        "NEO4J_USER": "neo4j",
        "NEO4J_PASSWORD": "password"
      }
    }
  }
}
```

## Architecture

```
AI Agent (Hermes/Claude/GPT)
    ↓ MCP Protocol
MCP Long-Term Memory Server
    ↓ Neo4j Driver
Neo4j Graph Database
    ↓
Knowledge Graph
├── Entities (people, companies, concepts, projects)
├── Relationships (works_at, depends_on, mentions)
└── Communities (clustered subgraphs for topic modeling)
```

## Business Use Cases

1. **Persistent Agent Assistants**: Agents that remember user preferences, past decisions, and project context across sessions
2. **Enterprise Knowledge Base**: Auto-building knowledge graphs from agent interactions — every question asked and answer found becomes structured knowledge
3. **Multi-Agent Memory**: Shared knowledge graph across a fleet of agents — "what did the research agent learn that the operations agent needs?"
4. **Audit Trail**: Every agent decision and its context stored as a queryable graph for compliance

## Comparison: Vector vs. GraphRAG Memory

| Feature | Vector Store (e.g., Mem0) | GraphRAG (this server) |
|---------|--------------------------|------------------------|
| Recall | Semantic similarity | Structured + semantic |
| Relationships | Implicit (chunk proximity) | Explicit (named edges) |
| Multi-hop Reasoning | No | Yes (graph traversal) |
| Entity Disambiguation | Weak | Strong (entity nodes) |
| Query Complexity | Simple retrieval | Complex graph queries |
| Setup | Simple (no DB) | Requires Neo4j |

## Limitations

- Requires running Neo4j instance (operational overhead)
- New server — GraphRAG integration may be incomplete
- GraphRAG quality depends on LLM extraction quality (garbage in, garbage out)
- Not a drop-in replacement for simpler vector memory solutions

## See Also

- Honcho MCP — for session-based agent memory and user modeling
- Mem0 — for vector-based agent memory (simpler, no graph DB required)
