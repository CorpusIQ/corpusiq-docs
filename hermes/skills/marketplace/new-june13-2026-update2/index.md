---
title: June 13, 2026 — Update 2: nousresearch/hermes-agent Massive Expansion (77 new skills)
description: Skills.sh sweep: 77 new skills — 72 from nousresearch/hermes-agent (now 184 total skills), plus 5 from wihy, aradotso, hermess, and aradotso/ai-agent-skills.
---

# June 13, 2026 — Update 2: Massive Hermes Agent Expansion

Second sweep of skills.sh on June 13 discovered **77 new skills** not in any previous catalog. The `nousresearch/hermes-agent` repository has exploded from ~10 catalogued variants to **184 total skills** — covering creative media, developer tools, platform integrations, macOS utilities, and AI infrastructure.

*Previously catalogued: 360 total. This update adds 77 → **437 total**.*

---

## nousresearch/hermes-agent — 72 new skills

The official Nous Research Hermes Agent skill repository now has 184 skills (15.1K total installs). These 72 were not present in any previous CorpusIQ sweep:

### Creative & Design — 12 skills

| Skill | Installs | Use Case |
|-------|----------|----------|
| `humanizer` | 190 | Strip AI-isms from text, add real human voice |
| `excalidraw` | 152 | Excalidraw diagram creation from descriptions |
| `architecture-diagram` | 151 | System architecture diagram generation |
| `ascii-art` | 148 | ASCII art generation for terminal output |
| `design-md` | 147 | Markdown design documents and UI specs |
| `sketch` | 145 | Hand-drawn style sketch generation |
| `ascii-video` | 141 | ASCII video/animation generation |
| `baoyu-infographic` | 139 | Infographic generation via Baoyu |
| `p5js` | 137 | Creative coding with p5.js |
| `pixel-art` | 87 | Pixel art sprite and scene generation |
| `baoyu-comic` | 80 | Comic strip generation via Baoyu |
| `baoyu-article-illustrator` | 78 | Article illustration via Baoyu |

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill humanizer
npx skills add nousresearch/hermes-agent --skill excalidraw
npx skills add nousresearch/hermes-agent --skill architecture-diagram
npx skills add nousresearch/hermes-agent --skill ascii-art
```

### Developer Tools — 16 skills

| Skill | Installs | Use Case |
|-------|----------|----------|
| `codex` | 135 | OpenAI Codex CLI integration |
| `opencode` | 134 | OpenCode editor integration |
| `systematic-debugging` | 131 | Structured debugging methodology |
| `github-repo-management` | 131 | GitHub repo: clone, create, fork, remotes |
| `github-code-review` | 131 | PR review with diffs, inline comments |
| `github-pr-workflow` | 130 | Full PR lifecycle: branch, commit, open, merge |
| `codebase-inspection` | 130 | Codebase analysis: LOC, languages, ratios |
| `github-issues` | 128 | Create, triage, label, assign issues |
| `github-auth` | 127 | GitHub auth: HTTPS tokens, SSH keys, gh CLI |
| `test-driven-development` | 126 | TDD methodology and workflow |
| `requesting-code-review` | 126 | How to request effective code review |
| `spike` | 125 | Spike/prototype rapid exploration |
| `python-debugpy` | 120 | Python debugging with debugpy |
| `node-inspect-debugger` | 123 | Node.js debugging via inspector |
| `subagent-driven-development` | 83 | Multi-agent development patterns |
| `codebase-inspection` | 130 | Code analysis toolkit |

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill codex
npx skills add nousresearch/hermes-agent --skill systematic-debugging
npx skills add nousresearch/hermes-agent --skill github-pr-workflow
npx skills add nousresearch/hermes-agent --skill test-driven-development
```

### Platform & API Integrations — 13 skills

| Skill | Installs | Use Case |
|-------|----------|----------|
| `google-workspace` | 131 | Gmail, Calendar, Drive, Docs, Sheets |
| `obsidian` | 131 | Obsidian vault integration |
| `notion` | 125 | Notion pages, databases, blocks |
| `airtable` | 124 | Airtable bases, tables, records |
| `xurl` | 124 | X/Twitter via xurl CLI |
| `blogwatcher` | 130 | Blog and RSS/Atom feed monitoring |
| `huggingface-hub` | 128 | HuggingFace model and dataset hub |
| `polymarket` | 131 | Polymarket prediction markets |
| `linear` | 80 | Linear issue tracking |
| `spotify` | 75 | Spotify music control and playback |
| `comfyui` | 129 | ComfyUI stable diffusion workflows |
| `touchdesigner-mcp` | 132 | TouchDesigner via MCP |
| `heartmula` | 122 | Heart rate / health monitoring |

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill google-workspace
npx skills add nousresearch/hermes-agent --skill notion
npx skills add nousresearch/hermes-agent --skill xurl
npx skills add nousresearch/hermes-agent --skill spotify
```

### Media & Content — 7 skills

| Skill | Installs | Use Case |
|-------|----------|----------|
| `youtube-content` | 144 | YouTube transcripts, summaries, threads |
| `ocr-and-documents` | 144 | OCR extraction from documents/images |
| `manim-video` | 141 | Mathematical animation videos |
| `songwriting-and-ai-music` | 138 | AI music generation and songwriting |
| `songsee` | 123 | Music visualization |
| `gif-search` | 124 | GIF search and retrieval |
| `pokemon-player` | 78 | Pokémon game player (fun/recreation) |

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill youtube-content
npx skills add nousresearch/hermes-agent --skill manim-video
```

### Apple/macOS Ecosystem — 7 skills

| Skill | Installs | Use Case |
|-------|----------|----------|
| `imessage` | 124 | iMessage sending and reading |
| `apple-reminders` | 124 | Apple Reminders integration |
| `apple-notes` | 123 | Apple Notes integration |
| `findmy` | 123 | Find My device tracking |
| `macos-computer-use` | 120 | macOS system control and automation |
| `maps` | 123 | Apple Maps navigation and search |
| `himalaya` | 121 | Terminal email client (Himalaya CLI) |

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill imessage
npx skills add nousresearch/hermes-agent --skill macos-computer-use
npx skills add nousresearch/hermes-agent --skill himalaya
```

### Hermes-Specific — 4 skills

| Skill | Installs | Use Case |
|-------|----------|----------|
| `hermes-agent` | 160 | Core Hermes Agent reference and configuration |
| `jupyter-live-kernel` | 167 | Jupyter live kernel inside Hermes |
| `debugging-hermes-tui-commands` | 76 | Debug Hermes TUI commands and interface |
| `hermes-s6-container-supervision` | 75 | S6 container supervision for Hermes services |

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill hermes-agent
npx skills add nousresearch/hermes-agent --skill jupyter-live-kernel
npx skills add nousresearch/hermes-agent --skill debugging-hermes-tui-commands
npx skills add nousresearch/hermes-agent --skill hermes-s6-container-supervision
```

### AI & MCP Infrastructure — 6 skills

| Skill | Installs | Use Case |
|-------|----------|----------|
| `claude-design` | 160 | Claude-powered design generation |
| `native-mcp` | 79 | MCP client: connect servers, register tools |
| `kanban-orchestrator` | 124 | Multi-agent kanban task orchestration |
| `kanban-worker` | 123 | Kanban task worker agent |
| `godmode` | 128 | Godmode agent exploration mode |
| `webhook-subscriptions` | 80 | Webhook subscription management |

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill native-mcp
npx skills add nousresearch/hermes-agent --skill kanban-orchestrator
```

### Research & Planning — 7 skills

| Skill | Installs | Use Case |
|-------|----------|----------|
| `research-paper-writing` | 156 | Academic paper writing and formatting |
| `plan` | 148 | Project planning and roadmap generation |
| `ideation` | 103 | Brainstorming and idea generation |
| `writing-plans` | 87 | Writing and planning methodology |
| `pretext` | 127 | PreTeXt academic document authoring |
| `nano-pdf` | 127 | Minimal PDF generation |
| `teams-meeting-pipeline` | 120 | Teams meeting scheduling and pipeline |

---

## Community Standalone — 5 new skills

### hermes-agent (wihy/hermes-agent-skill) — 493 installs 🤖

Third-party Hermes Agent skill wrapper from wihy. Provides Hermes agent configuration and management utilities.

**Install:**
```bash
npx skills add wihy/hermes-agent-skill --skill hermes-agent
```

---

### hermes-marketing-dashboard (aradotso/marketing-skills) — 414 installs 📊

Marketing performance dashboard specifically for Hermes agents. Tracks campaigns, analytics, and growth metrics.

**Install:**
```bash
npx skills add aradotso/marketing-skills --skill hermes-marketing-dashboard
```

---

### hermes-agent-framework (aradotso/ai-agent-skills) — 146 installs 🏗️

Alternative Hermes agent framework implementation (separate from the hermes-skills version). Broader AI agent focus with Hermes-specific adapters.

**Install:**
```bash
npx skills add aradotso/ai-agent-skills --skill hermes-agent-framework
```

---

### hermes-agent-self-evolution (aradotso/ai-agent-skills) — 130 installs 🔄

Self-improvement loops for AI agents with Hermes integration. Alternative to the hermes-skills version with broader agent compatibility.

**Install:**
```bash
npx skills add aradotso/ai-agent-skills --skill hermes-agent-self-evolution
```

---

### ppt-director (hermess/ppt-director) — 84 installs 📽️

PowerPoint presentation director — create, edit, and manage presentations programmatically.

**Install:**
```bash
npx skills add hermess/ppt-director --skill ppt-director
```

---

## Summary

| Repository | Skills | Total Installs | Category |
|-----------|--------|----------------|----------|
| nousresearch/hermes-agent | 72 | ~8,300 | Full Hermes Ecosystem |
| wihy/hermes-agent-skill | 1 | 493 | Agent Wrapper |
| aradotso/marketing-skills | 1 | 414 | Marketing |
| aradotso/ai-agent-skills | 2 | 276 | Agent Framework |
| hermess/ppt-director | 1 | 84 | Presentation |
| **Total** | **77** | **~9,567** | — |

**Marketplace subtotal before:** 271 → **After:** 348
**Total skills:** 360 → **437**

---

*← [June 13 Morning Update](/hermes/skills/marketplace/new-june13-2026/) | [Skills Catalog](/hermes/skills/catalog/) →*
*↑ [Marketplace Home](/hermes/skills/marketplace/)*
