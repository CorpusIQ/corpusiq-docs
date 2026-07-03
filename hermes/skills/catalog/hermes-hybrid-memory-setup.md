---
title: "Hermes Hybrid Memory — Full Setup Guide"
description: "Install and configure the Hybrid Memory plugin for Hermes Agent — graph + vector + holographic memory in one SQLite file with Hofstadter-inspired analogy and emergent chunking."
---

# Hermes Hybrid Memory — Setup Guide

**Repo:** [sheldon904/hermes-hybrid-memory](https://github.com/sheldon904/hermes-hybrid-memory)
**Author:** sheldon904
**License:** MIT
**Requires:** Python 3.11+, Hermes Agent, sqlite-vec

## Overview

Hybrid Memory replaces flat system-prompt memory with a unified store combining:

1. **Structured facts** (FTS5 full-text search)
2. **Semantic vector recall** (sqlite-vec, 384-dim embeddings)  
3. **Knowledge graph** (nodes + edges, incrementally maintained)

Plus Hofstadter-inspired mechanisms: analogy slot, emergent chunking, and usage-driven forgetting. All in one SQLite file.

## Architecture

```
documents in ──▶ memory_ingest.py ──▶ entity_resolve.py
                       │
                       ▼
              memory_store.db (SQLite)
              ┌──────────────────────────┐
              │ facts + FTS5 + trust     │
              │ sqlite-vec vectors       │
              │ graph (nodes/edges)      │
              └──────────────────────────┘
                       │
                       ▼
              memory_retrieve.py
              (keyword / vector / graph / analogy)
```

## Step 1: Prerequisites

```bash
# Verify Python version
python3 --version  # must be 3.11+

# Install sqlite-vec extension
pip install sqlite-vec

# Verify Hermes Agent is installed
hermes --version
```

## Step 2: Clone and Install

```bash
# Clone into your Hermes plugins directory
mkdir -p ~/.hermes/plugins/
cd ~/.hermes/plugins/
git clone https://github.com/sheldon904/hermes-hybrid-memory.git
cd hermes-hybrid-memory

# Install Python dependencies
pip install -r requirements.txt

# Verify installation
python3 -c "import hybrid_memory; print('OK')"
```

## Step 3: Configure Hermes Agent

Add to your `~/.hermes/config.yaml`:

```yaml
# Memory provider configuration
memory:
  provider: hybrid_memory
  store_path: ~/.hermes/memory/memory_store.db
  
  # Optional: custom embedding model
  embedding:
    model: all-MiniLM-L6-v2  # default, 384-dim
    # Or use any sentence-transformers compatible model
    
  # Optional: tuning
  hybrid:
    graph_weight: 0.3        # graph traversal weight in retrieval
    vector_weight: 0.4       # semantic similarity weight
    keyword_weight: 0.3      # FTS5 keyword weight
    analogy_threshold: 0.7   # minimum similarity for analogy match
    chunking_interval: 50    # facts before emergent chunking triggers
    forgetting_decay: 0.95   # per-day decay factor (1.0 = no decay)
```

## Step 4: Initialize the Memory Store

```bash
# Create the memory directory
mkdir -p ~/.hermes/memory/

# Initialize the database
python3 ~/.hermes/plugins/hermes-hybrid-memory/scripts/init_store.py \
  --db-path ~/.hermes/memory/memory_store.db

# Expected output:
# ✓ Created facts table with FTS5 index
# ✓ Created vector store (384-dim)
# ✓ Created graph tables (nodes, edges)
# ✓ Memory store ready at ~/.hermes/memory/memory_store.db
```

## Step 5: Memory Ingestion Pipeline

Hybrid Memory uses an ingestion pipeline that runs as a side effect of normal memory writes:

```bash
# Manual ingestion (for testing / backfill)
python3 ~/.hermes/plugins/hermes-hybrid-memory/memory_ingest.py \
  --db-path ~/.hermes/memory/memory_store.db \
  --input-dir ~/.hermes/memory/inbox/ \
  --llm-model sonnet

# The ingest pipeline:
# 1. LLM distills facts + graph nodes/edges from documents
# 2. entity_resolve.py canonicalizes entity names
# 3. Facts written to FTS5 + vector store
# 4. Graph nodes/edges updated incrementally
```

Documents can be placed in `~/.hermes/memory/inbox/` as:
- `.txt` files (plain text)
- `.md` files (markdown notes)
- `.json` files (structured facts)
- `.jsonl` files (pre-distilled facts from upstream agents)

The ingestion runs automatically during Hermes sessions when `memory_provider: hybrid_memory` is configured.

## Step 6: Verify Memory Is Working

```bash
# Start Hermes with hybrid memory
hermes --profile corpusiq

# In a Hermes session, test memory operations:
# "Remember: the API key for Stripe is sk_live_xxx"
# "What's our Stripe API key?"
# "What else do you know about our payment infrastructure?"

# Check the memory store directly
python3 ~/.hermes/plugins/hermes-hybrid-memory/scripts/query_store.py \
  --db-path ~/.hermes/memory/memory_store.db \
  --query "Stripe payment" \
  --mode hybrid  # uses keyword + vector + graph
```

## Step 7: Brain Visualization

Hybrid Memory ships with a visualization tool:

```bash
# Generate interactive brain graph
python3 ~/.hermes/plugins/hermes-hybrid-memory/brain_viz.py \
  --db-path ~/.hermes/memory/memory_store.db \
  --output ~/.hermes/memory/brain_snapshot.html

# Open in browser
open ~/.hermes/memory/brain_snapshot.html
```

The brain visualization is a self-contained HTML file showing:
- All entity nodes (color-coded by type)
- Edge connections (weight = relationship strength)
- Search and filter by entity type
- Click any entity to see its facts and connections
- Prospect leaves can be hidden

## Key Mechanisms

### Analogy Slot
The Hofstadter-inspired analogy mechanism finds memories that are **structurally similar but superficially different**. Example: "Which of our leads looks most like our best client?" — the system matches on relationship patterns (lead→discovery→trial→purchase) rather than surface text similarity.

### Emergent Chunking
After every ~50 facts, the system looks for patterns that can be compressed into reusable categories. A chunk is a named concept that replaces the raw facts it subsumes, saving retrieval cost and improving recall quality.

### Usage-Driven Forgetting
Memory decay is driven by usage frequency, not age. A fact accessed daily never decays. A fact never accessed decays slowly (configurable `forgetting_decay` rate). Facts that drop below a threshold are pruned. This is a deliberate departure from the common "recency-weighted" approach.

## Production Tuning

```yaml
# For agents with high memory volume (>10K facts)
hybrid:
  graph_weight: 0.4        # more graph, less keyword
  vector_weight: 0.35
  keyword_weight: 0.25
  chunking_interval: 100   # chunk less frequently
  forgetting_decay: 0.98   # slower decay

# For agents with sparse memory (<1K facts)  
hybrid:
  graph_weight: 0.2
  vector_weight: 0.5       # rely more on semantic similarity
  keyword_weight: 0.3
  chunking_interval: 30    # chunk more aggressively
  forgetting_decay: 0.90   # faster decay to keep store lean
```

## Troubleshooting

### "sqlite-vec extension not found"
```bash
pip install sqlite-vec
# If that fails, install from source:
pip install git+https://github.com/asg017/sqlite-vec.git
```

### "Memory store locked"
The store uses WAL mode for concurrent reads. If you get a lock error:
```bash
# Check for stale locks
sqlite3 ~/.hermes/memory/memory_store.db "PRAGMA wal_checkpoint(TRUNCATE);"
```

### "Empty retrieval results"
1. Verify facts are being ingested: `python3 scripts/query_store.py --mode stats`
2. Check embedding dimension matches (384-dim default)
3. Ensure the Hermes session has write access to `memory_store.db`

### "Slow retrieval with large stores"
1. Run VACUUM: `sqlite3 memory_store.db "VACUUM;"`
2. Increase `chunking_interval` to reduce fact count
3. Consider archiving old, never-accessed facts

## Integration with Other Memory Systems

Hybrid Memory can coexist with Honcho or other memory systems. Configure Hermes to use Hybrid Memory as the primary `memory_provider` while Honcho handles session-level context:

```yaml
memory:
  provider: hybrid_memory
  store_path: ~/.hermes/memory/memory_store.db

# Honcho still handles session context
honcho:
  enabled: true
  session_db: ~/.hermes/honcho/sessions.db
```

---

*Setup guide created by CorpusIQ. Repo maintained by [sheldon904](https://github.com/sheldon904). Contributions welcome.*
