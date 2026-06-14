---
title: June 14, 2026 — 2 New Hermes-Agent Skills: X/Twitter Scraper + Agent Usage
description: Skills.sh sweep: 2 new Hermes-relevant skills — X/Twitter scraper with Hermes Tweet plugin (146 installs) and multi-agent usage/cost tracker supporting Hermes (32 installs).
---

# June 14, 2026 — 2 New Hermes-Agent Skills

Morning sweep of [skills.sh](https://skills.sh) on June 14 discovered **2 new skills** not in any previous catalog — an X/Twitter automation skill with native Hermes Agent plugin support, and a cross-agent usage and cost tracker with Hermes Agent support.

*Previously catalogued: 438 total (349 marketplace). This update adds 2 → **440 total (351 marketplace).** *

---

## sickn33/antigravity-awesome-skills — 1 new skill

### x-twitter-scraper (146 installs) 🐦

Full-spectrum X/Twitter automation skill for Hermes agents. Provides tweet search, follower export, posting, DMs, webhooks, MCP server, SDKs, and the **Hermes Tweet** Hermes Agent plugin with `tweet_explore`, `tweet_read`, and approval-gated `tweet_action` tools. Also covers TweetClaw for OpenClaw environments.

Built on the Xquik platform API. Supports 23 bulk extraction tools, account monitoring, HMAC-signed webhooks, giveaway draws, and real-time event delivery.

**Install:**
```bash
npx skills add sickn33/antigravity-awesome-skills --skill x-twitter-scraper
```

**Hermes Tweet plugin (optional):**
```bash
hermes plugins install Xquik-dev/hermes-tweet --enable
```

**Requires:** Xquik API key ([xquik.com](https://xquik.com)). Base URL: `https://xquik.com/api/v1`. MCP endpoint: `https://xquik.com/mcp` (StreamableHTTP).

**Key capabilities for Hermes agents:**
| Capability | Hermes Tweet Tool |
|---|---|
| Tweet search | `tweet_explore` |
| Read tweets/replies | `tweet_read` |
| Post, reply, like, DM | `tweet_action` (approval-gated) |
| User lookup | `tweet_read` |
| Follower export | `tweet_explore` → extraction |
| Account monitoring | `tweet_explore` → monitor setup |

---

## briqt/agent-usage — 1 new skill

### agent-usage (32 installs) 📊

Cross-agent usage and cost tracking. Query AI coding agent spending, token consumption, model costs, session history, and API call counts — all from within conversation. **Supports Hermes Agent, Claude Code, Codex CLI, OpenClaw, OpenCode, kiro, and Pi.**

Has two backends: a REST API server (preferred, accurate pricing) and a local JSONL parser (fallback, approximate pricing). Hermes Agent data is read directly from `~/.hermes/state.db` and `~/.hermes/profiles/*/state.db` SQLite databases, supporting multiple profiles automatically.

**Install:**
```bash
npx skills add briqt/agent-usage
```

**Key commands for Hermes agents:**
```bash
# Summary: total cost, tokens, sessions
bash SKILL_DIR/scripts/query-api.sh stats --source hermes --from 2026-06-01

# Cost breakdown per model
bash SKILL_DIR/scripts/query-api.sh cost-by-model --source hermes

# List all Hermes sessions
bash SKILL_DIR/scripts/query-api.sh sessions --source hermes

# Token usage trend
bash SKILL_DIR/scripts/query-api.sh tokens-over-time --source hermes --granularity 1d
```

**Natural language trigger:** "How much did I spend on Hermes this month?" or "Which model costs the most across all my agents?"

---

## Summary

| # | Skill | Installs | Source | Category |
|---|-------|----------|--------|----------|
| 1 | `x-twitter-scraper` | 146 | sickn33/antigravity-awesome-skills | Social / X/Twitter |
| 2 | `agent-usage` | 32 | briqt/agent-usage | Monitoring / Cost Tracking |

**New this update:** 2 skills
**Marketplace subtotal before:** 349 → **After:** 351
**Total skills:** 438 → **440**

---

*← [June 13 Update 3](/hermes/skills/marketplace/new-june13-2026-update3/) | [Skills Catalog](/hermes/skills/catalog/) →*
*↑ [Marketplace Home](/hermes/skills/marketplace/)*
