---
title: OpenClaw XHS Setup — Xiaohongshu (RED) Integration for AI Agents
description: Install and configure zhjiang22/openclaw-xhs — Xiaohongshu (Little Red Book) MCP integration for OpenClaw and Hermes agents. Hot topic tracking, personal memory export, Chinese social media automation.
author: zhjiang22
repo: https://github.com/zhjiang22/openclaw-xhs
stars: 113
---

# OpenClaw XHS (Xiaohongshu) Setup Guide

**Source:** [zhjiang22/openclaw-xhs](https://skills.sh/zhjiang22/openclaw-xhs) (113 ⭐)
**Category:** Social Media / Growth

OpenClaw XHS integrates Xiaohongshu (小红书, "Little Red Book") — China's 300M+ user lifestyle and shopping platform — into your AI agent workflow. Built as an MCP server, it enables your Hermes or OpenClaw agent to read, monitor, and analyze Xiaohongshu content, track hot topics, and export personal memory banks.

---

## Quick Install

```bash
# Via skills.sh
npx skills add zhjiang22/openclaw-xhs@xiaohongshu

# Direct from GitHub
cd ~/.hermes/skills/
git clone https://github.com/zhjiang22/openclaw-xhs.git
cd openclaw-xhs
npm install
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | 18+ |
| **Hermes Agent** or **OpenClaw** | v0.16.0+ (Hermes) or latest OpenClaw |
| **Xiaohongshu account** | Required for authenticated API access |
| **MCP support** | Both Hermes and OpenClaw support MCP natively |

---

## Key Capabilities

### 1. Hot Topic Tracking (热点跟踪)
Monitor trending topics on Xiaohongshu in real-time:

```bash
# Start the MCP server
cd ~/openclaw-xhs && npm start

# Agent commands (via MCP tools):
# - get_trending_topics(category="tech", limit=20)
# - search_notes(keyword="AI agent", sort="hot")
# - get_note_detail(note_id="...")
```

### 2. Content Reading & Analysis
Your agent can read and analyze Xiaohongshu notes (posts):

| Tool | Description |
|---|---|
| `search_notes` | Search notes by keyword, category, or creator |
| `get_note_detail` | Full note content including images, comments, engagement |
| `get_creator_profile` | Creator stats, follower count, content history |
| `get_comments` | Comment thread with sentiment analysis |

### 3. Personal Memory Bank Export (个人记忆库导出)
Export your Xiaohongshu browsing history, saved notes, and interactions as structured data for your agent's memory:

```bash
# Export personal data
node export-memory.js --format json --output ~/xhs-memory.json

# Import into GBrain
gbrain import ~/xhs-memory.json --type xhs-notes
```

---

## MCP Server Configuration

Register the XHS MCP server with Hermes:

```yaml
# ~/.hermes/profiles/corpusiq/config.yaml
mcp_servers:
  xiaohongshu:
    transport: stdio
    command: node
    args:
      - ~/.hermes/skills/openclaw-xhs/server.js
    env:
      XHS_COOKIE: ${XHS_COOKIE}  # Your Xiaohongshu session cookie
```

### Authentication

Xiaohongshu requires browser cookies for API access:

1. Log into xiaohongshu.com in your browser
2. Export cookies (use browser dev tools or a cookie manager extension)
3. Set `XHS_COOKIE` environment variable with the cookie string
4. Cookies typically last 24-48 hours before needing refresh

---

## Use Cases

| Use Case | How It Works |
|---|---|
| **Competitive monitoring** | Track competitor brand mentions and sentiment on XHS |
| **Content research** | Analyze top-performing content in your niche |
| **Trend detection** | Identify emerging trends before they hit Western platforms |
| **Creator discovery** | Find and evaluate KOLs/KOCs for partnerships |
| **Market intelligence** | Understand Chinese consumer preferences and language |

---

## Why This Matters

Xiaohongshu has 300M+ monthly active users, predominantly young, affluent Chinese consumers. It's the #1 platform for:

- Product discovery and reviews
- Lifestyle trends and shopping decisions
- Brand perception in the Chinese market

For AI companies and SaaS products expanding into APAC, Xiaohongshu intelligence is critical — and this MCP integration makes it accessible directly from your agent workflow.

---

## Production Notes

- 113 GitHub stars, actively maintained (updated July 2026)
- Chinese-language README with English code comments
- Built as MCP server — compatible with any MCP client (Hermes, OpenClaw, Claude Desktop)
- Includes hot topic tracking, memory export, and content analysis tools
- Cookie-based auth (no API key required — uses standard web session)

---

## Limitations

- **Cookie expiry:** Session cookies expire every 24-48h and must be manually refreshed
- **Rate limiting:** Xiaohongshu may rate-limit aggressive scraping
- **Chinese-language content:** Most content is in Chinese — pair with translation tools for non-Chinese speakers
- **No posting:** Read-only at this time (posting requires additional anti-bot measures)

---

*← [Memory Merger Setup](/hermes/skills/catalog/memory-merger-setup/) | [Skills Catalog →](/hermes/skills/catalog/)*
*Powered by CorpusIQ*
