---
title: MongoDB Agent Skills — Database Skills for Hermes Agents
description: MongoDB's official agent skills — schema design, natural language querying, search and AI, Atlas Stream Processing. 3.5K+ combined installs across 6 skills for building with MongoDB.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mongodb-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# MongoDB Agent Skills — Setup Guide

**Source:** [mongodb/agent-skills](https://skills.sh/mongodb/agent-skills) (3.5K+ combined installs)
**GitHub:** [mongodb/agent-skills](https://github.com/mongodb/agent-skills) (163 ⭐)
**Category:** Database / Data Infrastructure
**Quality Tier:** 🟢 Production

MongoDB Agent Skills is the official agent skills collection for MongoDB. It covers schema design, natural language querying, vector search with AI, Atlas Stream Processing, MCP server setup, and query optimization. These skills teach Hermes agents to design, query, and optimize MongoDB databases using idiomatic patterns and best practices.

---

## Installation

```bash
# Core database skills
npx skills add mongodb/agent-skills --skill mongodb-schema-design
npx skills add mongodb/agent-skills --skill mongodb-natural-language-querying
npx skills add mongodb/agent-skills --skill mongodb-search-and-ai

# Infrastructure and optimization
npx skills add mongodb/agent-skills --skill mongodb-atlas-stream-processing
npx skills add mongodb/agent-skills --skill mongodb-connection
npx skills add mongodb/agent-skills --skill mongodb-mcp-setup
npx skills add mongodb/agent-skills --skill mongodb-query-optimizer
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **mongodb-schema-design** | 3.5K | Document schema patterns — embedding, referencing, indexing strategies |
| **mongodb-natural-language-querying** | 2.8K | Natural language to MongoDB query translation with aggregation pipeline generation |
| **mongodb-search-and-ai** | 2.7K | Atlas Vector Search for semantic search and RAG applications |
| **mongodb-atlas-stream-processing** | 1.8K | Real-time stream processing with Atlas Stream Processing for event-driven apps |
| **mongodb-connection** | — | Connection string patterns, driver setup, and connection pooling |
| **mongodb-mcp-setup** | — | MCP server deployment for MongoDB with tool definitions and resource exposure |
| **mongodb-query-optimizer** | — | Query performance analysis, index recommendations, and explain plan interpretation |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **MongoDB Atlas account** | Free tier at https://www.mongodb.com/atlas (M0 cluster, 512MB storage) |
| **MongoDB driver** | Node.js: `npm install mongodb` / Python: `pip install pymongo` |
| **mongosh (optional)** | MongoDB Shell: `npm install -g mongosh` |
| **Atlas CLI (optional)** | `brew install mongodb-atlas-cli` |

---

## Key Capabilities

### Schema Design
Document model patterns for JSON data. Embedding versus referencing decisions with performance tradeoffs. Index strategies including compound, multikey, text, and geospatial indexes. Schema versioning patterns for evolving data models. The single most-installed MongoDB skill for a reason.

### Natural Language Querying
Convert natural language questions into MongoDB queries and aggregation pipelines. Covers `$match`, `$group`, `$lookup`, `$unwind`, and `$facet` stages. Useful for building natural language interfaces to MongoDB data that Hermes agents can use directly.

### Vector Search and AI
Atlas Vector Search for semantic search, recommendation engines, and RAG applications. Index and query vector embeddings using `$vectorSearch`. Integrate with embedding models from OpenAI, Cohere, and Hugging Face. Build retrieval-augmented generation pipelines with MongoDB as the vector store.

### Stream Processing
Atlas Stream Processing for real-time data pipelines. Process change streams, aggregate windows, and emit to sinks. Ideal for event-driven agent architectures that need to react to database changes in real time.

### MCP Server Setup
Deploy MongoDB as an MCP server with tool definitions for database operations. Expose collections as resources with JSON Schema validation. Enable agents to query, insert, update, and aggregate directly through MCP tool calls.

---

## Quick Start

```bash
# 1. Create a free MongoDB Atlas cluster at atlas.mongodb.com

# 2. Install the Node.js driver
npm install mongodb

# 3. Add schema design and query skills
npx skills add mongodb/agent-skills --skill mongodb-schema-design
npx skills add mongodb/agent-skills --skill mongodb-natural-language-querying

# 4. Connect and verify
mongosh "mongodb+srv://<cluster>.mongodb.net" --username <user>
```

---

## Hermes Integration Notes

- **Session storage:** Use MongoDB for persistent Hermes session state with flexible document schemas
- **Vector memory:** Atlas Vector Search as a semantic memory backend for agent context retrieval
- **Real-time triggers:** Stream Processing for event-driven growth operations that react to database changes
- **MCP integration:** MCP server setup enables MongoDB as a first-class tool provider for Hermes agents
- **Natural language analytics:** Query session data and metrics using natural language through Hermes

---

## Links

- **skills.sh:** https://skills.sh/mongodb/agent-skills
- **GitHub:** https://github.com/mongodb/agent-skills
- **MongoDB Docs:** https://www.mongodb.com/docs
- **Atlas Vector Search:** https://www.mongodb.com/docs/atlas/atlas-vector-search
- **Atlas Stream Processing:** https://www.mongodb.com/docs/atlas/atlas-stream-processing
