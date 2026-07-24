---
name: "Altronis MCP"
description: "Singapore AI consulting MCP — AI consultant, grant-matched transformation plans, curated SG AI events"
category: "Developer Tools"
source: "mcp.so"
discovered: "2026-07-23"
verified: true
repository: "https://github.com/sypherin/altronis"
---

# Altronis MCP — Singapore AI Consulting Access

Altronis provides MCP access to Singapore-focused AI consulting services. Agents can interact with the Lyra AI consultant, generate grant-matched AI transformation plans, and pull curated Singapore AI events and news. Read-only, wraps altronis.sg.

## What It Does

- **Lyra consultant** — AI assistant specialized in Singapore business AI adoption
- **Transformation plans** — Generate AI adoption roadmaps matched to Singapore government grants
- **Events & news** — Curated Singapore AI industry events and news feed
- **Read-only** — All tools are read-only; no write operations

## Quick Start

```bash
# Clone and install
git clone https://github.com/sypherin/altronis
cd altronis
npm install

# Add to Claude Code
claude mcp add altronis -- npx tsx src/index.ts

# Or Hermes Agent
hermes mcp add altronis -- npx tsx /path/to/altronis/src/index.ts
```

**Prerequisites:** Node.js 20+

## Key Tools

| Tool | Description |
|------|-------------|
| `ask_lyra` | Query the Lyra AI consultant about Singapore AI adoption |
| `generate_plan` | Generate grant-matched AI transformation roadmap |
| `get_events` | Pull curated Singapore AI events and conferences |
| `get_news` | Latest Singapore AI industry news |
| `find_grants` | Search Singapore government AI/tech grants |

## Use Cases

- **Singapore market entry** — Research AI adoption landscape and available grants
- **Grant applications** — Generate AI transformation plans tailored to specific grant schemes
- **Event monitoring** — Track Singapore AI events for networking opportunities
- **Competitive intelligence** — Monitor Singapore AI industry developments

---

*Discovered via [mcp.so](https://mcp.so) sweep. Listed in the [CorpusIQ MCP Catalog](https://corpusiq-docs/hermes/mcp/).*
