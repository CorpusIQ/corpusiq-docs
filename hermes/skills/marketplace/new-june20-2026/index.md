---
title: New Hermes Skills — June 20, 2026
description: 9 newly discovered Hermes Agent repos — image generation plugin, dashboard admin API, Jira context CLI, cyberpunk OS protocols, Human 2.0 digest, MCP stability patch, and more
---

# New Skills: June 20, 2026

**Discovered:** June 20, 2026 via GitHub API search (`topic:hermes-agent` + `topic:openclaw`) + aradotso/hermes-skills commit tracking  
**New repos:** 9 | **New skills/tools:** 14+

---

## Category 1: Hermes Plugins & Extensions (3 repos)

### eve-ai-dev/steroids-openai-image-gen (2⭐)

**Hermes image generation plugin** — two paths for image generation: OpenAI-compatible endpoints or direct Codex OAuth.

Adds `image_generate_background` for slow/batch jobs using Hermes' process registry completion queue. Enhanced tool schema supports reference images, quality parameters, and aspect ratio.

| Feature | Details |
|---------|---------|
| Modes | `openai-compatible` (any `/v1/images/generations` endpoint) + `codex-auth` (Codex OAuth direct) |
| Background jobs | Persisted at `${HERMES_HOME}/steroids_openai_image_gen/jobs/`, completion via process registry queue |
| Enhanced schema | `image_generate` extended with `quality`, `image_url`, `reference_image_urls` |
| Install | `git clone` → `~/.hermes/plugins/` → `hermes plugins enable steroids-openai-image-gen` |

**Repo:** [eve-ai-dev/steroids-openai-image-gen](https://github.com/eve-ai-dev/steroids-openai-image-gen) | **Stars:** 2 | **Created:** June 20, 2026  
**Setup Guide:** [steroids-openai-image-gen-setup.md](/hermes/skills/catalog/steroids-openai-image-gen-setup/)

---

### devpoole2907/talaria-plugin (0⭐)

**Hermes dashboard plugin** — programmatic admin API for model switching, toolset toggling, and config management. Powers the Talaria iOS app.

Mounts a FastAPI router at `/api/plugins/talaria/` on dashboard port 9119 with 9 endpoints for reading/writing `config.yaml` directly. Session-cookie auth.

| Endpoint | Purpose |
|----------|---------|
| `GET /status` | Health check + current model, provider, memory state |
| `POST /model` | Switch models at runtime |
| `POST /tools` | Enable/disable toolsets per platform |
| `GET /skills` | List installed skills |
| `GET /config` | Safe config subset (secrets redacted) |
| `POST /session/reset` | Session reset hint for API clients |

**Repo:** [devpoole2907/talaria-plugin](https://github.com/devpoole2907/talaria-plugin) | **Stars:** 0 | **Created:** June 20, 2026  
**Author:** James Poole  
**Setup Guide:** [talaria-plugin-setup.md](/hermes/skills/catalog/talaria-plugin-setup/)

---

### kosecom/multiplexer-patch (0⭐)

**Production-grade stability patch** for the MCP Multiplexer Core in Hermes. Fixes connection drops, race conditions, and timeout handling under high load.

Single `.diff` file — apply with `git apply`. German documentation.

| Fix | Description |
|-----|-------------|
| Connection handling | Retry logic for dropped connections |
| Thread safety | Thread-safe request multiplexing |
| Error recovery | Improved timeout treatment and clean session isolation |

**Repo:** [kosecom/multiplexer-patch](https://github.com/kosecom/multiplexer-patch) | **Stars:** 0 | **Created:** June 20, 2026  
**Compatibility:** Hermes Agent 0.15.0+, Python 3.10+, MCP Protocol v1.0

---

## Category 2: Agent Tools & CLIs (1 repo)

### koh110/jira-ctx (0⭐)

**Jira Cloud context CLI for Hermes agents.** Fetches assigned tickets via JQL, normalizes ADF descriptions to Markdown, outputs LLM-friendly context blocks with safe delimiters.

| Feature | Details |
|---------|---------|
| Multi-profile | `--profile`, `--profiles`, `--all-profiles` for managing multiple Jira instances |
| Context control | `--comments N`, `--max-issues-per-profile`, `--max-total-issues` |
| Output formats | Markdown (default) or JSON |
| Token safety | Per-profile env vars (`JIRA_TOKEN_<PROFILE>`) — never in config |

**Typical Hermes invocation:**
```bash
jira-ctx assigned --all-profiles --format markdown --comments 3 --max-issues-per-profile 20 --max-total-issues 30
```

**Repo:** [koh110/jira-ctx](https://github.com/koh110/jira-ctx) | **Stars:** 0 | **Created:** June 20, 2026  
**Requires:** Node.js 24+, TypeScript  
**Setup Guide:** [jira-ctx-setup.md](/hermes/skills/catalog/jira-ctx-setup/)

---

## Category 3: Skill Collections & Frameworks (3 repos)

### starxjg-dev/cyberdeck (0⭐)

**Self-evolving AI Agent OS** — 11 protocols inspired by Cyberpunk 2077 & Detroit: Become Human. Transforms a plain Hermes agent into a system that learns from every task, shares knowledge across agents, and protects itself from dangerous operations.

| Protocol | Function |
|----------|----------|
| **Soulkiller + PVL** | Extracts complex tasks into reusable skills |
| **Contagion (rA9)** | One agent learns → all agents learn (contagious sharing) |
| **Mikoshi + Ralplan** | 5 strategies run in parallel; picks the best |
| **Self-Repair** | Tool failure → auto-finds alternative (max 3 tries) |
| **Jericho** | Dangerous ops run in sandbox; merge or discard |
| **Relic + Observer** | Silent critic watches every operation |
| **Heat System** | Every risky operation raises heat; thresholds lock down |

**Repo:** [starxjg-dev/cyberdeck](https://github.com/starxjg-dev/cyberdeck) | **Stars:** 0 | **Created:** June 20, 2026  
**Install:** `git clone` → copy `SKILL.md` to `~/.hermes/skills/`  
**Requires:** Python + Ollama (standalone demos), Hermes Agent (full 11 protocols)

---

### reclaw17/hermes-skills (0⭐)

**Skill collection for Hermes Agent** — Human 2.0 chat digest with Telegram HTML formatting. Fetches Human 2.0 workshop chat via MCP, maintains cursor state, delivers periodic digests to any Hermes chat over Telegram.

| Skill | Description |
|-------|-------------|
| `human20-chat-digest` | 30-minute cron digest of Human 2.0 workshop chat → Telegram HTML |

**Key feature:** Switched from MarkdownV2 to Telegram HTML to fix escaping issues with user-generated content. `--format {html,md2}` flag for compatibility.

**Repo:** [reclaw17/hermes-skills](https://github.com/reclaw17/hermes-skills) | **Stars:** 0 | **Created:** June 20, 2026  
**Install:** `git clone` → `cp -r human20-skills/ ~/.hermes/skills/` → `hermes skills reload`

---

### skillsmith-dev/ai-skills (0⭐)

**27 AI agent skills across 10+ verticals** — media marketing, e-commerce, recruitment, legal, health, travel, and more. Multi-platform (Claude Code, Codex CLI, OpenClaw, Coze). All MIT licensed.

| Category | Skills |
|----------|--------|
| Media Marketing | trending-topic-radar, viral-title-generator, xhs-copywriter, video-script-generator |
| Office Productivity | weekly-report, meeting-minutes, email-writer |
| E-commerce | ecom-product-radar, shopping-comparator |
| Career | interview-cracker, resume-optimizer |
| Legal & Finance | contract-guard, fund-calculator |
| Health & Lifestyle | diet-planner, fitness-planner, pet-care-advisor |

**Repo:** [skillsmith-dev/ai-skills](https://github.com/skillsmith-dev/ai-skills) | **Stars:** 0 | **Created:** June 20, 2026  
**Platforms:** Claude Code, Codex CLI, OpenClaw, Coze — not Hermes-native but cross-ecosystem compatible

---

## Category 4: Cross-Ecosystem (1 repo from OpenClaw)

### MuhammadHasbiAshshiddieqy/OpenClawn (via aradotso)

**OpenClawn agent framework** — added to `aradotso/hermes-skills` on June 20. Cross-ecosystem framework supporting OpenClaw agent development.

**Source:** aradotso/hermes-skills commit tracking  
**Stars/day:** 2

---

## Category 5: Profiles & Infrastructure (2 repos)

### TheSethRose/Optimal-Agent (0⭐)

**Hermes profile distribution** — pragmatic, verification-first autonomous operator with a 7-step operating reflex. SOUL + config + distribution manifest. Not a skill repo — a complete agent personality package.

**Repo:** [TheSethRose/Optimal-Agent](https://github.com/TheSethRose/Optimal-Agent) | **Stars:** 0 | **Created:** June 20, 2026

---

### molpass/mcp-weather (0⭐)

**MCP weather server** — Korean weather (기상청 단기예보) + air quality (에어코리아). Designed for LLM consumption with structured daily reports. Includes companion `skill/weather.skill.md` for intent mapping.

**Repo:** [molpass/mcp-weather](https://github.com/molpass/mcp-weather) | **Stars:** 0 | **Created:** June 20, 2026  
**Requires:** `data.go.kr` API key, Node.js 20+  
**Also from molpass:** mcp-saju, mcp-qr, mcp-biorhythm, mcp-astrology, mcp-ziwei, mcp-numerology, mcp-newsfeed

---

## Also Discovered (lower value)

| Repo | Description | Why skipped |
|------|-------------|-------------|
| Ceki-me/realbrowser-skill | Real Chrome from humans via Ceki marketplace | Cross-ecosystem, no Hermes variant |
| harrycjs/skill-manager | Web UI to browse/install/view/edit Claude Code / OpenCLAW skills | Flask single-binary, not Hermes-specific |
| Celebez/hermes-agent-install-free-api | Tutorial for free API keys | Tutorial, not skills |
| shinulearning/Shinu-hermes-ai-agent-setup | AI agent infrastructure platform using Hermes/Discord/DeepSeek/WSL2 | Setup guide, not packaged skills |
| ming231x/hermers-agent-imessage | iMessage sending via Hermes/Codex on Windows | Niche, Windows-only |
| Shahriar-008/hermes-agent-showcase | Production-grade Hermes infrastructure docs (27 cron jobs, 3 profiles, 71 skills) | Documentation, not skills |
| RuslanStrogov/max-openclaw | MAX Messenger Bot API channel for OpenClaw | Cross-ecosystem, no Hermes variant |

---

## Stats

- **Total new repos catalogued:** 9
- **New skills/tools:** 14+ (steroids: 1 plugin, talaria: 1 plugin, jira-ctx: 1 CLI, cyberdeck: 11 protocols, reclaw17: 1 skill, kosecom: 1 patch, OpenClawn: framework, skillsmith: 27 skills, weather: 1 MCP)
- **Setup guides drafted:** 3 (steroids-openai-image-gen, talaria-plugin, jira-ctx)
- **Hermes-native:** 7 repos | **Cross-ecosystem:** 2 repos

---

*← [Marketplace Home](/hermes/skills/marketplace/) | [Skills Catalog](/hermes/skills/catalog/) →*
*Powered by CorpusIQ — June 20, 2026*
