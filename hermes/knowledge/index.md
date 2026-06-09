---
title: Knowledge Architecture
description: Persistent memory for autonomous agents — GBrain, GraphRAG, Dream Cycle, and Honcho integration
---

# Knowledge Architecture

Autonomous agents need memory that persists beyond a single conversation. The knowledge architecture combines four systems: GBrain for long-term storage, GraphRAG for relationship retrieval, Dream Cycle for nightly consolidation, and Honcho for conversation continuity.

## GBrain — Organizational Memory

Persistent knowledge layer with 729 indexed files, pglite database, nomic-embed-text embeddings at 768 dimensions, and semantic retrieval. Knowledge is retained and continuously expanded — it compounds over time rather than resetting between sessions.

### Capabilities
- Semantic search with vector and keyword hybrid retrieval
- Entity and relationship tracking
- Timeline entries for chronological context
- Tag-based organization
- Multi-source federation
- Code-aware search (callers, callees, definitions)

### Schema
Pages organized by type with frontmatter metadata, wikilinks between related pages, and embedded code-aware chunks. The schema pack defines page types, link types, and routing rules.

## GraphRAG — Relationship Intelligence

Traditional RAG retrieves documents. GraphRAG retrieves relationships. The implementation creates entities, relationships, communities, and knowledge clusters enabling contextual understanding beyond keyword similarity.

### Structure
- **Entities**: people, companies, projects, concepts
- **Relationships**: works at, invested in, depends on, reports to
- **Communities**: clustered groups of related entities
- **Knowledge clusters**: topics that span multiple entities

### Retrieval
Query expansion across related entities, community-level summarization, and graph traversal for multi-hop reasoning.

## Dream Cycle — Nightly Consolidation

At 03:00 daily, a consolidation process runs. Objectives: consolidate learned information, eliminate duplicate concepts, create semantic connections, update memory structures, and strengthen retrieval quality. Knowledge compounds over time — the system gets smarter daily.

### Process
1. Extract facts from the day's conversations
2. Deduplicate against existing knowledge
3. Create cross-references between related facts
4. Update embedding vectors for new and changed content
5. Generate summary takes for important patterns

## Honcho — Conversation Memory

Honcho provides session continuity, semantic search across conversations, and peer modeling. The platform develops persistent contextual understanding of users, organizations, and workflows. Conclusions derived from conversations feed into GBrain for long-term storage.

## Integration Flow

```
Conversation → Honcho (session memory)
    ↓
Dream Cycle (nightly consolidation)
    ↓
GBrain (long-term knowledge)
    ↓
GraphRAG (relationship retrieval)
    ↓
Agent Context (next conversation)
```

Knowledge flows from conversation to long-term memory and back. Each cycle enriches the agent's understanding without requiring manual updates.

---

*Powered by CorpusIQ — knowledge architecture for autonomous agents*
