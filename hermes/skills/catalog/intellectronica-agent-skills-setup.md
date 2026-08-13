---
title: Intellectronica — 22-Skill Agent Toolkit for Hermes
description: Versatile agent skills collection covering Notion API, YouTube transcripts, Anki flashcards, Context7 docs lookup, Tavily search, Copilot SDK, Mermaid diagrams, Todoist tasks, Google Workspace (gog CLI), Upstash Redis, and more. 63.1K+ combined installs.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/intellectronica-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Intellectronica — Agent Skills Setup Guide

**Source:** [intellectronica/agent-skills](https://skills.sh/intellectronica/agent-skills) (63.1K+ combined installs)
**GitHub:** [intellectronica/agent-skills](https://github.com/intellectronica/agent-skills) (279 ⭐)
**Category:** Agent Tools / Multi-Utility
**Quality Tier:** 🟡 Beta (high installs, low GitHub stars)

A personal agent skills toolkit with 22 skills covering knowledge management (Notion, Anki, Raindrop), content tools (YouTube transcripts, Mermaid diagrams, markdown conversion), developer utilities (Context7 docs, Copilot SDK, code search), and infrastructure (Upstash Redis, Tavily search, Google Workspace). Despite low GitHub visibility (279 stars), install counts are substantial — 63.1K+ combined — driven by practical, well-scoped skills that solve specific agent needs.

---

## Installation

```bash
# Core productivity skills:
npx skills add intellectronica/agent-skills --skill notion-api
npx skills add intellectronica/agent-skills --skill youtube-transcript
npx skills add intellectronica/agent-skills --skill tavily
npx skills add intellectronica/agent-skills --skill context7

# Knowledge management:
npx skills add intellectronica/agent-skills --skill anki-connect
npx skills add intellectronica/agent-skills --skill raindrop-api
npx skills add intellectronica/agent-skills --skill todoist-api

# Developer tools:
npx skills add intellectronica/agent-skills --skill copilot-sdk
npx skills add intellectronica/agent-skills --skill gog-cli
npx skills add intellectronica/agent-skills --skill mgrep-code-search
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **notion-api** | 60.0K | Full Notion API integration — read/write pages, databases, blocks |
| **youtube-transcript** | 3.1K | Fetch and process YouTube video transcripts |
| **anki-connect** | — | Interact with Anki flashcards via AnkiConnect |
| **beautiful-mermaid** | — | Render Mermaid diagrams as SVG/PNG |
| **context7** | — | Retrieve up-to-date library documentation via Context7 API |
| **copilot-sdk** | — | GitHub Copilot SDK across Node.js, Python, Go, .NET, Java |
| **gog-cli** | — | Google Workspace CLI (Gmail, Calendar, Drive, Docs, Sheets) |
| **gpt-image-1-5** | — | Image generation via GPT Image 1.5 |
| **here-be-git** | — | Advanced Git operations and workflows |
| **lorem-ipsum** | — | Generate placeholder text for designs and mocks |
| **markdown-converter** | — | Convert between markdown and other formats |
| **mgrep-code-search** | — | Fast multi-repo code search and analysis |
| **monologue-notes-api** | — | Interact with Monologue notes platform |
| **nano-banana-2** | — | Lightweight image processing |
| **nano-banana-pro** | — | Advanced image processing and manipulation |
| **promptify** | — | Optimize and refine prompts for better AI output |
| **raindrop-api** | — | Bookmark management via Raindrop.io API |
| **ray-so-code-snippet** | — | Generate beautiful code snippet images (ray.so) |
| **tavily** | — | AI-optimized web search via Tavily API |
| **todoist-api** | — | Task management via Todoist API |
| **ultrathink** | — | Deep reasoning and analysis framework |
| **upstash-redis-kv** | — | Serverless Redis key-value store via Upstash |

---

## Key Capabilities

### Knowledge & Productivity (Highest Impact)
- **notion-api** (60K installs — flagship skill): Full CRUD on Notion pages, databases, blocks, and comments. Supports searching, filtering, and rich text. Most-installed skill in the toolkit by a wide margin.
- **youtube-transcript** (3.1K installs): Fetch transcripts with timestamps, multi-language support. Useful for content analysis and video summarization.
- **anki-connect**: Create, update, and review Anki flashcards programmatically — ideal for spaced repetition learning automation
- **raindrop-api**: Search, organize, and manage bookmarks across collections

### Developer & Search
- **context7**: Retrieve current documentation for any library/framework — avoids stale training data
- **copilot-sdk**: Build custom Copilot extensions with streaming, tools, agents, and MCP servers
- **gog-cli**: Full Google Workspace automation from the command line — Gmail, Calendar, Drive, Docs, Sheets, Slides
- **mgrep-code-search**: Search across multiple codebases with regex and structured output

### Creative & Visual
- **beautiful-mermaid**: Render Mermaid diagrams to SVG/PNG for documentation and presentations
- **ray-so-code-snippet**: Generate styled code screenshots for social media and docs
- **gpt-image-1-5**: Programmatic image generation and editing

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | 18+ |
| **Notion API Key** | For notion-api (integration token + page access) |
| **Tavily API Key** | For tavily search |
| **Context7 API Key** | For context7 docs lookup |
| **Google Cloud** | For gog-cli (OAuth credentials) |
| **Anki + AnkiConnect** | For anki-connect (desktop app + plugin) |

---

## Quick Start

```bash
# 1. Install the flagship skill
npx skills add intellectronica/agent-skills --skill notion-api

# 2. Install YouTube and search tools
npx skills add intellectronica/agent-skills --skill youtube-transcript
npx skills add intellectronica/agent-skills --skill tavily

# 3. Verify
npx skills list | grep intellectronica

# 4. Use in Hermes — skills load on trigger
# "Search Notion for the Q3 roadmap" → notion-api
# "Get the transcript of this YouTube video" → youtube-transcript
```

---

## Verification

```bash
# Check installed skills
npx skills list | grep -E "notion-api|youtube-transcript|tavily"

# Test Notion — requires NOTION_API_KEY in environment
# "List my Notion databases"

# Test YouTube transcript
# "Get transcript from https://youtube.com/watch?v=dQw4w9WgXcQ"
```

---

## Notes

- **notion-api** dominates at 60K installs (95% of the toolkit's total) — it's the primary motivation for most users
- Low GitHub stars (279) despite high install counts suggests the repo is personal/niche but the skills solve real problems
- The **gog-cli** skill overlaps with the existing `google-workspace` catalog entry — prefer gog-cli for CLI-centric workflows, Google Workspace skill for API-centric
- **context7** and **tavily** are useful complements to existing `web-search` and `web-extract` capabilities — they provide structured, AI-optimized search results
- **copilot-sdk** is valuable if you're building custom GitHub Copilot extensions alongside Hermes agents
- Most skills require API keys — configure in environment variables before first use
