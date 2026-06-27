---
title: Skills Gallery Setup Guide
description: Install and configure the Skills Gallery — 1,672+ AI agent skills across 49 categories, compatible with Hermes Agent and 60+ other tools. One command, every skill.
skill_name: skills-gallery
repo: uthumany/Skills-Gallery
compatibility: Hermes Agent, Claude Code, Codex, Gemini CLI, OpenClaw, Cursor, Windsurf, and 50+ more
installs: New (June 2026)
---

# Skills Gallery — Setup Guide

## Overview

Skills Gallery is the largest single collection of AI agent skills ever published. One command installs access to **1,672+ skills** organized across **49 categories** — frontend development, security auditing, creative coding, multi-agent orchestration, and everything in between.

**Key Facts:**
- **1,672+ skills** across **49 categories**
- Compatible with **60+ AI agent tools** including Hermes Agent
- Install via npm, yarn, pnpm, bun, pip, uv, or curl
- MIT licensed by uthuman Inc.
- Created June 27, 2026

---

## Prerequisites

- Node.js 18+ (for npm/yarn/pnpm/bun install)
- **OR** Python 3.11+ (for pip/uv install)
- Hermes Agent v0.17.0+ (for Hermes-native integration)

---

## Installation

### Option 1: npx (No Install — Recommended for Hermes)

```bash
npx skills-gallery
```

This downloads and runs the gallery CLI without permanent installation. Skills are browsed and loaded on demand.

### Option 2: Global npm Install

```bash
npm install -g skills-gallery
skills-gallery
```

### Option 3: pip Install (Python)

```bash
pip install skills-gallery
# or
uv tool install skills-gallery

skills-gallery
```

### Option 4: curl (Any System)

```bash
curl -fsSL https://raw.githubusercontent.com/uthumany/Skills-Gallery/master/scripts/install.sh | bash
```

---

## Hermes Agent Integration

Skills Gallery is explicitly compatible with Hermes Agent. After installation:

### Method 1: Load Skills via CLI

```bash
# List all available categories
skills-gallery categories

# Browse skills in a category
skills-gallery browse --category "Agent Systems"

# Search for specific skills
skills-gallery search "memory context"

# Install a specific skill to Hermes
skills-gallery install --skill memory-bridge --agent hermes

# Install all skills from a category
skills-gallery install --category "Security" --agent hermes
```

### Method 2: Programmatic API

```javascript
// In your own tooling
import { catalog } from 'skills-gallery';

// Get all skills compatible with Hermes Agent
const hermesSkills = catalog.filterByAgent('hermes-agent');

// Search skills
const memorySkills = catalog.search('memory management');

// Get category breakdown
const categories = catalog.getCategories();
```

---

## Key Categories for CorpusIQ Operators

| Category | Skills | Top Picks for Growth Ops |
|----------|:------:|--------------------------|
| 📱 Social & Media | 69 | Social posting, content scheduling, engagement analytics |
| 💼 Business & Productivity | 119 | CRM integration, sales automation, project management |
| 📊 Data & Analytics | 85 | Data visualization, pipeline automation, reporting |
| 🔗 APIs & Automation | 148 | API integration, webhook handlers, workflow automation |
| 📝 Content & Docs | 221 | Content creation, SEO optimization, copywriting |
| 🧠 Agent Systems | 178 | Memory management, multi-agent coordination, planning |
| 🤖 AI & ML | 187 | Model evaluation, prompt engineering, RAG pipelines |

---

## CLI Reference

```bash
# Core commands
skills-gallery                      # Launch interactive browser
skills-gallery categories           # List 49 categories
skills-gallery browse <category>    # Browse skills in a category
skills-gallery search <query>       # Full-text search across all skills
skills-gallery info <skill-name>    # Show skill details and metadata
skills-gallery install <skill>      # Install a skill to your agent
skills-gallery update               # Update the catalog to latest

# Agent integration
skills-gallery install --agent hermes --skill <name>
skills-gallery install --agent hermes --category <name>
skills-gallery list --agent hermes  # List Hermes-installed skills
```

---

## Use Cases for CorpusIQ

### 1. Growth Operations Automation
Install marketing, social media, and content creation skills to automate growth workflows:

```bash
skills-gallery install --agent hermes --category "Social & Media"
skills-gallery install --agent hermes --category "Content & Docs"
```

### 2. Lead Qualification Pipeline
Combine CRM, data analysis, and automation skills:

```bash
skills-gallery search "CRM lead qualification"
skills-gallery search "data enrichment"
```

### 3. Agent Infrastructure
Enhance Hermes with memory, coordination, and evaluation skills:

```bash
skills-gallery install --agent hermes --category "Agent Systems"
skills-gallery install --agent hermes --category "AI & ML"
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `npx skills-gallery` fails | Ensure Node.js 18+ is installed: `node --version` |
| Skills don't appear in Hermes | Verify install path: `skills-gallery list --agent hermes` |
| Category not found | Update catalog: `skills-gallery update` |
| pip install fails | Use `uv tool install skills-gallery` as alternative |

---

## Verification

```bash
# Verify installation
skills-gallery --version

# Check skill count
skills-gallery stats

# Verify Hermes integration
skills-gallery list --agent hermes

# Test search
skills-gallery search "context window"
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Skills Gallery on GitHub](https://github.com/uthumany/Skills-Gallery) →*

*Curated by CorpusIQ — one MCP endpoint, all your business tools.*
