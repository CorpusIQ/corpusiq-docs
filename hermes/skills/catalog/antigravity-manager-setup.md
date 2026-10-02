---
title: "Antigravity Manager - Multi-Account LLM Proxy & Rotation"
description: Setup guide for antigravity-manager, the Agent Skills skill for Antigravity Manager (31K-star Tauri/Rust tool) that proxies Google and Anthropic accounts as OpenAI/Anthropic/Gemini API endpoints with rotation and quota tracking. 1,396+ installs.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/antigravity-manager-setup/"
robots: "index,follow"
last_updated: "2026-09-13"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Antigravity Manager - Setup Guide

**Source:** [reason-machines/trending-skills](https://github.com/reason-machines/trending-skills) (1,396+ installs)
**Category:** Agent Infrastructure / LLM Operations
**Quality Tier:** 🔵 Community

Antigravity Manager is a professional AI account manager and proxy gateway (Tauri v2 + Rust desktop app, plus a headless Docker/server mode). It takes Google (Gemini) and Anthropic (Claude) web session accounts and exposes them as standard OpenAI-compatible, Anthropic-native, and Gemini-native API endpoints with intelligent multi-account rotation, quota tracking, and automatic failover. This skill (from the [ara.so](https://ara.so) Daily 2026 Skills collection) walks an agent through installing, configuring, and operating the gateway.

---

## Installation

### Step 1 - Install the skill

```bash
npx skills add reason-machines/trending-skills --skill antigravity-manager
```

The publisher org was renamed `aradotso` → `reason-machines` on Sep 12, 2026. The legacy `aradotso/trending-skills` install path still resolves (GitHub 301 redirect), but `reason-machines` is canonical.

### Step 2 - Install Antigravity Manager itself

| Method | Command |
|---|---|
| One-line installer (Linux/macOS) | `curl -fsSL https://raw.githubusercontent.com/lbjlaq/Antigravity-Manager/v4.1.30/install.sh | bash` |
| Homebrew | `brew tap lbjlaq/antigravity-manager https://github.com/lbjlaq/Antigravity-Manager && brew install --cask antigravity-tools` |
| Docker (headless server) | `docker run -d --name antigravity-manager -p 8045:8045 -e API_KEY=$ANTIGRAVITY_API_KEY -e WEB_PASSWORD=$ANTIGRAVITY_WEB_PASSWORD -v ~/.antigravity_tools:/root/.antigravity_tools lbjlaq/antigravity-manager:latest` |
| Manual | Download `.dmg` / `.msi` / `.deb` / `.rpm` / `.AppImage` from [GitHub Releases](https://github.com/lbjlaq/Antigravity-Manager/releases) |

## Prerequisites

| Requirement | Notes |
|---|---|
| Google account(s) with Gemini access | Authorized via the OAuth 2.0 URL generated in the app |
| Anthropic account(s) with Claude access | Same OAuth flow |
| Docker (server mode) or desktop OS | Headless server mode is built from source with `--features headless` |
| `API_KEY` | Authenticates proxy API calls |
| `WEB_PASSWORD` (recommended) | Separate web UI admin password; falls back to `API_KEY` |

## Capabilities

| Capability | Trigger / Detail |
|---|---|
| Multi-account rotation | Auto-rotates accounts on 429/401 errors with millisecond failover |
| Protocol conversion | Web sessions → OpenAI (`/v1/chat/completions`), Anthropic (`/v1/messages`), Gemini (`generateContent`) |
| Model routing | Regex remaps in `gui_config.json`, e.g. `gpt-4.*` → `gemini-2.5-pro` |
| Tiered routing | Prioritizes accounts Ultra → Pro → Free; fast-reset accounts consumed first |
| Background-task demotion | Background requests auto-redirected to Flash-tier models to preserve premium quota |
| Quota dashboard | Live Gemini Pro/Flash, Claude, and Imagen 3 quotas with smart recommendation |
| 403 detection | Banned accounts flagged and skipped during rotation |
| Batch account import | JSON import of `{token, type, label}` records |

## API Endpoints

The proxy listens on port **8045** by default.

| Protocol | Endpoint | Compatible with |
|---|---|---|
| OpenAI-compatible | `POST http://localhost:8045/v1/chat/completions` | Any OpenAI SDK client |
| Anthropic-native | `POST http://localhost:8045/v1/messages` | Claude Code |
| Gemini-native | `POST http://localhost:8045/v1/models/{model}:generateContent` | Gemini clients |

Example (OpenAI SDK - Gemini through the gateway):

```python
import os
from openai import OpenAI

client = OpenAI(
 api_key=os.environ["ANTIGRAVITY_API_KEY"],
 base_url="http://localhost:8045/v1",
)
resp = client.chat.completions.create(
 model="gemini-2.5-pro",
 messages=[{"role": "user", "content": "Hello"}],
)
```

## Connecting Agent Clients

**Claude Code** - point the Anthropic env vars at the gateway:

```bash
export ANTHROPIC_API_KEY=$ANTIGRAVITY_API_KEY
export ANTHROPIC_BASE_URL=http://localhost:8045
claude
```

**Any OpenAI-compatible client** (Cherry Studio, Cursor, Continue.dev, or an OpenAI-compatible provider in an agent config): base URL `http://localhost:8045/v1` plus the gateway API key.

## CorpusIQ Use Cases

- **Agent fleet failover** - point OpenAI-compatible agents at the gateway for automatic 429/401 rotation across accounts.
- **Model-cost arbitrage** - remap hard-coded model names to cheaper tiers (`gpt-4.*` → `gemini-2.5-flash`) without touching client code.
- **Quota monitoring** - one dashboard for every Gemini/Claude account an agent fleet consumes.
- **Premium-quota protection** - background tasks auto-demote to Flash-tier models.
- **Provider experimentation** - test OpenAI/Anthropic/Gemini protocols against one local gateway before committing to a provider.

## Security & Compliance Notes

- **No skills.sh security audits published** for this skill (no Trust Hub / Socket / Snyk verdicts render on the publisher page) - review before production use.
- The upstream tool repo ([lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager), 31K+ stars, pushed Sep 12 2026) ships **no standard license** (GitHub API: NOASSERTION).
- The gateway proxies **web session tokens**, not official API keys. Upstream providers may flag or ban accounts used this way (the built-in 403 detection exists for exactly this case). Review Google/Anthropic terms before production use.

## Troubleshooting

| Issue | Fix |
|---|---|
| Port 8045 in use | `lsof -ti:8045 | xargs kill -9` or change `proxy.port` in `~/.antigravity_tools/gui_config.json` |
| Forgotten credentials | `docker logs antigravity-manager` or grep `gui_config.json` for `api_key` / `admin_password` |
| Account 403 / banned | Marked in UI and skipped; add a fresh account and remove the banned one |
| All accounts 429 | Rotation exhausted - add accounts or wait for quota reset; check the dashboard |
| macOS Gatekeeper | `xattr -d com.apple.quarantine /Applications/Antigravity\ Tools.app` |
| Claude Code not connecting | Verify the proxy responds and env vars are exported |

## Verification

```bash
# Gateway responds on the models endpoint
curl -s http://localhost:8045/v1/models -H "Authorization: Bearer ${ANTIGRAVITY_API_KEY}"

# Full round-trip through the OpenAI-compatible endpoint
curl -s http://localhost:8045/v1/chat/completions \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ${ANTIGRAVITY_API_KEY}" \
 -d '{"model":"gemini-2.5-pro","messages":[{"role":"user","content":"ping"}]}'
```

---

## Notes

- From the [ara.so](https://ara.so) Daily 2026 Skills collection - auto-generated from trending GitHub repos.
- Sibling guides from the same publisher: [OpenClaw Control Center](/hermes/skills/catalog/openclaw-control-center-setup) and [Hermes Labyrinth Observability](/hermes/skills/catalog/hermes-labyrinth-observability-setup).
