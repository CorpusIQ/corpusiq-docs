---
title: Talaria Plugin — Hermes Dashboard Admin API Setup Guide
description: Install and configure the Talaria Hermes dashboard plugin — programmatic admin API for model switching, toolset toggling, and config management.
---

# Talaria Plugin — Setup Guide

**Plugin:** `devpoole2907/talaria-plugin`  
**Purpose:** Programmatic admin API for Hermes Agent — model switching, toolset toggling, config management  
**License:** MIT | **Language:** Python | **Author:** James Poole

---

## What It Does

Mounts a FastAPI router at `/api/plugins/talaria/` on the Hermes dashboard (port 9119) with 9 endpoints that read/write `config.yaml` directly. Powers the Talaria iOS app but works with any HTTP client.

**Why it exists:** The Hermes API Server exposes chat endpoints but no admin operations. This plugin bridges that gap for external clients.

---

## Installation

### Quick Install

```bash
mkdir -p ~/.hermes/plugins
git clone https://github.com/devpoole2907/talaria-plugin.git ~/.hermes/plugins/talaria
hermes gateway restart
```

### Docker (Hermes in container)

Assume container mounts `~/.hermes` to `/opt/data`:

```bash
git clone https://github.com/devpoole2907/talaria-plugin.git ~/.hermes/plugins/talaria
docker restart hermes
```

---

## Endpoints

All at `http://<host>:9119/api/plugins/talaria/`

| Method | Path | Description |
|--------|------|-------------|
| GET | `/status` | Health check + current model, provider, terminal backend, max turns, memory state |
| GET | `/model` | Current model (`default`, `provider`, `base_url`, `context_length`) |
| POST | `/model` | Switch model. Body: `{"model":"...", "provider":"..."}` |
| GET | `/tools` | List all platform toolsets with enabled/disabled arrays |
| POST | `/tools` | Enable/disable a toolset. Body: `{"toolset":"web","action":"enable","platform":"api_server"}` |
| GET | `/skills` | Installed skills (name + path) |
| GET | `/memory` | Memory config (`enabled`, `user_profile_enabled`, `provider`, `storage_path`) |
| GET | `/config` | Safe config subset (model, agent, terminal, memory, compression, display; secrets redacted) |
| POST | `/session/reset` | Instructions for creating a fresh session |

---

## Authentication

Uses **session-cookie auth**, not Bearer tokens:

```bash
# Login to get session cookie
curl -c cookies.txt -X POST http://localhost:9119/auth/password-login \
  -H "Content-Type: application/json" \
  -d '{"provider":"basic","username":"<user>","password":"<pass>"}'

# Hit endpoint
curl -b cookies.txt http://localhost:9119/api/plugins/talaria/status
```

**Dual-port architecture (Talaria iOS):**
- Port **8642** → Hermes API Server (chat, sessions, runs) — **Bearer token**
- Port **9119** → Talaria plugin (admin commands) — **Session cookie**

---

## Usage Examples

### Check Status
```bash
curl -b cookies.txt http://localhost:9119/api/plugins/talaria/status
```

### Switch Model
```bash
curl -b cookies.txt -X POST http://localhost:9119/api/plugins/talaria/model \
  -H "Content-Type: application/json" \
  -d '{"model":"claude-sonnet-4-20250514","provider":"anthropic"}'
```

### Enable a Toolset
```bash
curl -b cookies.txt -X POST http://localhost:9119/api/plugins/talaria/tools \
  -H "Content-Type: application/json" \
  -d '{"toolset":"web","action":"enable","platform":"api_server"}'
```

### List Skills
```bash
curl -b cookies.txt http://localhost:9119/api/plugins/talaria/skills
```

---

## Architecture

```
┌─────────────────────────────────────────┐
│  Talaria iOS App                        │
│                                         │
│  Chat ────► :8642/v1/runs (Bearer)      │
│  Admin ───► :9119/api/plugins/talaria/   │
│              (Session cookie)            │
└────────────┬────────────────────────────┘
             │
    ┌────────▼────────┐
    │  Hermes Gateway │
    │                 │
    │  Dashboard ─────┤
    │  Plugin Router  │
    │       │         │
    │  Talaria API ───┤  reads/writes config.yaml
    │  (FastAPI)      │  reads skills/ dir
    └─────────────────┘
```

---

## Verification

```bash
# Login and verify
curl -c cookies.txt -X POST http://localhost:9119/auth/password-login \
  -H "Content-Type: application/json" \
  -d '{"provider":"basic","username":"admin","password":"<your-password>"}'

curl -b cookies.txt http://localhost:9119/api/plugins/talaria/status | python3 -m json.tool
```

Expected response includes `{"model": "...", "provider": "...", "memory": {...}}`.

---

*Repo: [devpoole2907/talaria-plugin](https://github.com/devpoole2907/talaria-plugin)*
