---
title: nousresearch/hermes-agent — Complete Setup Guide
description: Install all 184 skills from the official Nous Research Hermes Agent repository. Category-by-category setup with prerequisites, install commands, and verification.
---

# nousresearch/hermes-agent — Complete Setup Guide

The official Hermes Agent skill repository from Nous Research now contains **184 skills** across 12 categories. This guide covers installation, prerequisites, and verification for the most impactful skills.

## Quick Start — Install All Skills

```bash
# Install the entire nousresearch/hermes-agent repository
npx skills add nousresearch/hermes-agent

# Individual skill installs:
npx skills add nousresearch/hermes-agent --skill <skill-name>
```

## Category 1: Creative & Design (12 skills)

```bash
# Core creative tools
npx skills add nousresearch/hermes-agent --skill humanizer        # 190 installs — strip AI-isms
npx skills add nousresearch/hermes-agent --skill excalidraw       # 152 installs — diagrams
npx skills add nousresearch/hermes-agent --skill architecture-diagram  # 151 installs
npx skills add nousresearch/hermes-agent --skill ascii-art        # 148 installs
npx skills add nousresearch/hermes-agent --skill design-md        # 147 installs
npx skills add nousresearch/hermes-agent --skill sketch           # 145 installs

# Media generation
npx skills add nousresearch/hermes-agent --skill ascii-video      # 141 installs
npx skills add nousresearch/hermes-agent --skill baoyu-infographic # 139 installs
npx skills add nousresearch/hermes-agent --skill p5js             # 137 installs
npx skills add nousresearch/hermes-agent --skill pixel-art        # 87 installs
npx skills add nousresearch/hermes-agent --skill baoyu-comic      # 80 installs
npx skills add nousresearch/hermes-agent --skill baoyu-article-illustrator  # 78 installs
```

**Prerequisites:** None for most. Baoyu skills may require API keys.

---

## Category 2: Developer Tools (16 skills)

```bash
# GitHub ecosystem (essential)
npx skills add nousresearch/hermes-agent --skill github-auth           # 127 installs
npx skills add nousresearch/hermes-agent --skill github-repo-management # 131 installs
npx skills add nousresearch/hermes-agent --skill github-pr-workflow     # 130 installs
npx skills add nousresearch/hermes-agent --skill github-code-review     # 131 installs
npx skills add nousresearch/hermes-agent --skill github-issues          # 128 installs

# Code quality
npx skills add nousresearch/hermes-agent --skill codebase-inspection    # 130 installs
npx skills add nousresearch/hermes-agent --skill systematic-debugging   # 131 installs
npx skills add nousresearch/hermes-agent --skill test-driven-development # 126 installs
npx skills add nousresearch/hermes-agent --skill requesting-code-review  # 126 installs
npx skills add nousresearch/hermes-agent --skill spike                  # 125 installs

# Debuggers
npx skills add nousresearch/hermes-agent --skill python-debugpy         # 120 installs
npx skills add nousresearch/hermes-agent --skill node-inspect-debugger  # 123 installs

# External editors
npx skills add nousresearch/hermes-agent --skill codex              # 135 installs — OpenAI Codex CLI
npx skills add nousresearch/hermes-agent --skill opencode           # 134 installs
npx skills add nousresearch/hermes-agent --skill subagent-driven-development # 83 installs
```

**Prerequisites:**
- GitHub skills: `gh` CLI installed and authenticated
- `codex`: OpenAI API key + Codex CLI
- Debuggers: Corresponding language runtime

---

## Category 3: Platform & API Integrations (13 skills)

```bash
# Productivity platforms
npx skills add nousresearch/hermes-agent --skill google-workspace   # 131 installs
npx skills add nousresearch/hermes-agent --skill notion             # 125 installs
npx skills add nousresearch/hermes-agent --skill airtable           # 124 installs
npx skills add nousresearch/hermes-agent --skill obsidian           # 131 installs
npx skills add nousresearch/hermes-agent --skill linear             # 80 installs

# Social & communication
npx skills add nousresearch/hermes-agent --skill xurl               # 124 installs — X/Twitter
npx skills add nousresearch/hermes-agent --skill blogwatcher        # 130 installs — RSS
npx skills add nousresearch/hermes-agent --skill himalaya           # 121 installs — Email

# AI & data platforms
npx skills add nousresearch/hermes-agent --skill huggingface-hub    # 128 installs
npx skills add nousresearch/hermes-agent --skill polymarket         # 131 installs
npx skills add nousresearch/hermes-agent --skill spotify            # 75 installs
npx skills add nousresearch/hermes-agent --skill comfyui            # 129 installs
npx skills add nousresearch/hermes-agent --skill touchdesigner-mcp  # 132 installs
```

**Prerequisites:**
- `google-workspace`: GCP OAuth credentials
- `notion`: Notion API token
- `xurl`: X/Twitter API keys (v2)
- `spotify`: Spotify Developer app credentials
- `huggingface-hub`: HF token

---

## Category 4: Apple/macOS Ecosystem (7 skills)

```bash
npx skills add nousresearch/hermes-agent --skill imessage            # 124 installs
npx skills add nousresearch/hermes-agent --skill apple-reminders     # 124 installs
npx skills add nousresearch/hermes-agent --skill apple-notes         # 123 installs
npx skills add nousresearch/hermes-agent --skill findmy              # 123 installs
npx skills add nousresearch/hermes-agent --skill macos-computer-use  # 120 installs
npx skills add nousresearch/hermes-agent --skill maps                # 123 installs
```

**Prerequisites:** macOS only. Requires Full Disk Access permissions for some skills.

---

## Category 5: Hermes-Specific (4 skills)

```bash
npx skills add nousresearch/hermes-agent --skill hermes-agent                   # 160 installs
npx skills add nousresearch/hermes-agent --skill jupyter-live-kernel            # 167 installs
npx skills add nousresearch/hermes-agent --skill debugging-hermes-tui-commands   # 76 installs
npx skills add nousresearch/hermes-agent --skill hermes-s6-container-supervision # 75 installs
```

**Prerequisites:**
- `jupyter-live-kernel`: Python + Jupyter installed
- `hermes-s6-container-supervision`: s6-overlay or s6 supervision suite
- Hermes Agent installed and configured

---

## Category 6: AI & MCP Infrastructure (6 skills)

```bash
npx skills add nousresearch/hermes-agent --skill claude-design         # 160 installs
npx skills add nousresearch/hermes-agent --skill native-mcp            # 79 installs
npx skills add nousresearch/hermes-agent --skill kanban-orchestrator   # 124 installs
npx skills add nousresearch/hermes-agent --skill kanban-worker         # 123 installs
npx skills add nousresearch/hermes-agent --skill godmode               # 128 installs
npx skills add nousresearch/hermes-agent --skill webhook-subscriptions # 80 installs
```

**Prerequisites:**
- `native-mcp`: MCP server config in Hermes `config.yaml`
- `claude-design`: Anthropic API key

---

## Category 7: Media & Content (7 skills)

```bash
npx skills add nousresearch/hermes-agent --skill youtube-content          # 144 installs
npx skills add nousresearch/hermes-agent --skill ocr-and-documents        # 144 installs
npx skills add nousresearch/hermes-agent --skill manim-video              # 141 installs
npx skills add nousresearch/hermes-agent --skill songwriting-and-ai-music # 138 installs
npx skills add nousresearch/hermes-agent --skill songsee                  # 123 installs
npx skills add nousresearch/hermes-agent --skill gif-search               # 124 installs
```

**Prerequisites:**
- `manim-video`: Python + Manim library
- `youtube-content`: `yt-dlp` or YouTube Data API key

---

## Category 8: Research & Planning (7 skills)

```bash
npx skills add nousresearch/hermes-agent --skill research-paper-writing  # 156 installs
npx skills add nousresearch/hermes-agent --skill plan                    # 148 installs
npx skills add nousresearch/hermes-agent --skill ideation                # 103 installs
npx skills add nousresearch/hermes-agent --skill writing-plans           # 87 installs
npx skills add nousresearch/hermes-agent --skill pretext                 # 127 installs
npx skills add nousresearch/hermes-agent --skill nano-pdf                # 127 installs
npx skills add nousresearch/hermes-agent --skill teams-meeting-pipeline  # 120 installs
```

**Prerequisites:** Most are zero-dependency. `pretext` requires PreTeXt CLI.

---

## Repository Totals

| Category | Skills | Key Skill |
|----------|--------|-----------|
| Creative & Design | 12 | humanizer (190) |
| Developer Tools | 16 | github-repo-management (131) |
| Platform Integrations | 13 | google-workspace (131) |
| Apple/macOS | 7 | imessage (124) |
| Hermes-Specific | 4 | jupyter-live-kernel (167) |
| AI & MCP | 6 | claude-design (160) |
| Media & Content | 7 | youtube-content (144) |
| Research & Planning | 7 | research-paper-writing (156) |
| **Total** | **72** | — |

Combined with previously catalogued variants (dogfood, yuanbao, arxiv, claude-code, popular-web-designs, llm-wiki, powerpoint, hermes-agent-skill-authoring), the total is **80 nousresearch/hermes-agent skills**.

*← [Discovery Report](/hermes/skills/marketplace/new-june13-2026-update2/) | [Skills Catalog](/hermes/skills/catalog/) →*

*Powered by CorpusIQ*
