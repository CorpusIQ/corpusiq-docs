---
title: "Memory Architecture Guide for Hermes Agent"
description: "Hermes Agent memory architecture guide covering the triple stack: Honcho peer memory, GBrain organizational knowledge, memcore-cloud cross-session recall"
category: knowledge
tags: [hermes-agent, memory, honcho, gbrain, memcore-cloud, graphrag, persistent-memory, knowledge-management]
last_updated: 2026-10-27
canonical: "https://www.corpusiq.io/docs/hermes/knowledge/"
robots: "index,follow"

---

# Hermes Agent Memory Architecture  --  The Triple Stack for Persistent AI Memory

## Why Three Systems?

| Problem | Without Memory | Solution | System |
|---------|---------------|----------|--------|
| "Who am I talking to?" | Agent forgets users between sessions | Peer identity, preferences, bans | **Honcho** |
| "Where is that file?" | Agent can't find code/docs it created | Organizational knowledge indexing | **GBrain** |
| "What happened last session?" | Agent repeats work, misses context | Cross-session context injection | **memcore-cloud** |

These aren't competitors  --  they solve different problems. Run all three.

---

## Layer 1: Honcho  --  Peer Memory

**What it solves:** Persistent identity. Who the user is, what platforms are banned, what decisions were made, what rules apply.

**Setup (2 minutes):**

```bash
# Register the hosted Honcho MCP endpoint (Bearer auth via headers)
hermes mcp add honcho --url https://mcp.honcho.dev --auth header
```

Then supply the three headers in the server block of `config.yaml`:

```yaml
mcp_servers:
  honcho:
    url: https://mcp.honcho.dev
    headers:
      Authorization: Bearer YOUR_HONCHO_KEY
      X-Honcho-Workspace-ID: your-workspace
      X-Honcho-User-Name: your-agent-name
    enabled: true
```

**What it stores:**

```
Peer: user
├── Preferences: stored and retrieved across sessions
├── Platform bans: tracked per platform
├── Rules: business rules and communication preferences
├── Decisions: dated decision log
└── Context: role, autonomy level, communication style

Peer: corpusiq-agent
├── Self-conclusions: What I learned, what I fixed
├── Session summaries: Previous session handoffs
└── Improvement log: Skills patched, patterns discovered
```

**Key Honcho tools in Hermes:**

```
mcp__honcho__get_peer_context     --  Load everything about a peer
mcp__honcho__chat                 --  Ask questions about peer knowledge
mcp__honcho__search               --  Semantic search across conversations
mcp__honcho__schedule_dream       --  Queue memory consolidation
```

**Pattern: Pre-flight gate**

```python
# Before EVERY external action, check Honcho
peer = honcho_get_peer_context(target_peer_id="user")
# Check: Is this platform banned?
# Check: Any rules about this action?
# Check: Was this already done?
```

---

## Layer 2: GBrain  --  Organizational Knowledge

**What it solves:** Where are the files, what code does what, what was built when. Organizational knowledge that persists.

**Setup (10 minutes):**

```bash
# Requires Bun 1.4.4+. GBrain is not on npm - install from the repo:
bun install -g github:garrytan/gbrain
gbrain init --pglite --no-embedding
# GBrain indexes your project files into pglite with 768d embeddings
```

**What it stores:**

```
Organization: CorpusIQ
├── Pages: 6,000+ indexed (code, docs, configs, scripts)
├── Embeddings: nomic-embed-text, 768-dimension
├── Categories: infrastructure, video, governance, email, social
└── Relationships: "heygen-video-generator.py" → depends on → "heygen.json"
```

**Query pattern:**

```python
# "What videos did we generate this week?"
gbrain.search("video pipeline generated files MP4 week June 2026")

# "Where is the email template?"
gbrain.search("HTML email template operator time waste campaign")
```

**Dream Cycle (3 AM daily):**

```
Nightly consolidation:
├── Merge duplicate observations
├── Strengthen frequently-accessed paths
├── Prune stale/irrelevant entries
└── Update peer cards with new conclusions
```

---

## Layer 3: memcore-cloud  --  Cross-Session Recall

**What it solves:** "What happened last session?" Full conversation recall with raw source tracking.

**Setup (5 minutes):**

```bash
# memcore ships as a Hermes plugin (read-only recall of raw sources via a
# pre-turn hook). It is not distributed on PyPI - enable it as a plugin:
hermes plugins enable memcore_yifanchen

# The cross-session layer used in this deployment is Sibyl, which registers
# as the memory provider and stores everything in local SQLite (FTS5):
pip install sibyl-memory-hermes
# Store: ~/.hermes/profiles/<profile>/sibyl/profiles/<profile>/memory.db
```

**Architecture:**

```
Session N-1                    Session N
    │                              │
    ▼                              ▼
memcore-cloud ──► injects ──► Hermes turn
    │                            
    ├── Raw sources: What files were read, what URLs were fetched
    ├── FTS5 recall: Search past conversations instantly
    └── Context window: Relevant history injected automatically
```

**What it enables:**

| Without memcore-cloud | With memcore-cloud |
|----------------------|-------------------|
| "What did I do yesterday?" → Blank stare | "You generated a video, posted 3 tweets, replied to 2 emails" |
| Repeats the same research | "Already researched this  --  here's what we found" |
| Forgets tool quirks | "HeyGen background URLs are broken, use default" |
| Requires user to re-explain | Remembers preferences across sessions |

---

## Layer 4: GraphRAG  --  Relationship Memory

**What it solves:** How entities and concepts connect  --  not just what documents say.

**When to use:**
- Complex codebases where files reference each other
- Business operations with multiple connected systems
- Multi-agent architectures with dependencies

**Setup (30 minutes):**

```bash
pip install graphrag
graphrag init --root ./graphrag-data
# Index your knowledge base
graphrag index --root ./graphrag-data
```

**Query pattern:**

```
"Which cron jobs depend on the Gmail API token?"
→ Returns: Email Monitor, Email Responder, Forward Handler, Job Reply Forwarder
→ With: Token location, refresh schedule, failure handling per cron
```

---

## Layer 5: Session DB  --  Hermes Built-In

**What it is:** SQLite database at `~/.hermes/profiles/<profile>/state.db` with FTS5 full-text search. Every conversation, every tool call, every result.

**How to use:**

```bash
# List recent sessions from the CLI
hermes sessions list

# Browse and search session history interactively
hermes sessions browse

# From within a session, use the session_search tool
session_search(query="email campaign June")
```

**What's stored:**
- Every message (user + assistant)
- Every tool call + result
- Session metadata (model, profile, timestamps)
- Auto-summarized session handoffs

---

## The Complete Memory Flow

```
SESSION START
    │
    ├── 1. Honcho: Load peer context
    │       └── Who is the user? What are the rules? What platforms are banned?
    │
    ├── 2. GBrain: Query organizational knowledge
    │       └── Where are the files? What was built? What's the architecture?
    │
    ├── 3. memcore-cloud: Inject cross-session context
    │       └── What happened last session? What was decided? What's pending?
    │
    ├── 4. Session DB: Load today's conversation
    │       └── What have we already discussed this session?
    │
    ▼
AGENT OPERATES WITH FULL CONTEXT
    │
    ▼
DURING SESSION
    │
    ├── Every action: Log to Session DB (automatic)
    ├── New observations: Write to Honcho
    ├── New files: GBrain picks up on next index
    └── memcore-cloud: Continuously updating context window
    │
    ▼
SESSION END (or every 30 min)
    │
    ├── 1. Honcho: Queue dream for consolidation
    ├── 2. GBrain: Re-index changed files
    ├── 3. memcore-cloud: Save raw sources
    └── 4. Session DB: Auto-compact if needed
```

---

## Why Not Just One Memory System?

| Approach | Good For | Fails At |
|----------|----------|----------|
| Single Vector DB | Semantic document search | Peer identity, conversation history, cross-session context |
| Honcho only | Peer modeling, conversations | Code/document indexing, file relationships |
| GBrain only | File/code knowledge | "Who is the user?"  --  no peer modeling |
| memcore-cloud only | Cross-session recall | Organizational knowledge indexing |
| **All three** | Complete agent memory | Nothing  --  this is the production stack |

**The cost of NOT running all three:** Your agent forgets who it's talking to, can't find its own files, and repeats the same research every session.

---

## Production Numbers

From our deployment (verified October 27, 2026):

| System | Data Volume | Query Speed |
|--------|------------|-------------|
| Honcho | 200+ peer conclusions, 50+ sessions | <100ms semantic search |
| GBrain | 6,133 indexed pages / 14,293 chunks, 768d vectors | <200ms search |
| memcore-cloud | Cross-session context auto-injected | Per-turn, transparent |
| Session DB | 50K+ messages across sessions | FTS5 instant |
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
