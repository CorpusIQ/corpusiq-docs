---
title: AIHawk MCP - Anti-Detect Browser Agent
description: "AIHawk MCP server: an open-source anti-detect browser and web browsing agent for coding agents. Stealth browsing, no captchas, plain-language tasks, proxy and profile support."
category: "MCP Servers"
tags: ["aihawk", "stealth browser", "anti-detect", "web automation", "mcp server", "browser agent"]
last_updated: "2026-09-22"
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/aihawk-mcp"
robots: "index,follow"
---

# AIHawk MCP - Anti-Detect Browser Agent

**31K+ stars · actively maintained · featured in TechCrunch, Wired, The Verge, Business Insider**

AIHawk is an open-source anti-detect browser and web browsing agent with an MCP server for coding agents: undetected browsing, no captchas, no blocks. You tell it what you want in plain language and it drives a real browser the way a person would.

## What makes it different

Standard browser automation gets flagged by fingerprinting and captcha walls. AIHawk runs a hardened engine that passes bot checks, with a seed-based identity system so the same seed reproduces the same browser fingerprint, locale, timezone, and preferences every run.

The family:

- **aihawk** - the MCP server and the web UI. `aihawk` alone runs the server, `aihawk ui` runs the interface on 127.0.0.1:8765.
- **invisible_playwright** - the engine as a Python library. The API is Playwright's, so existing Playwright code runs with anti-detect behavior.
- **invisible_core** - seed to fingerprint to preferences, proxy, and geolocation mapping.

## Install

Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
```

Claude Code:

```bash
claude plugin marketplace add feder-cr/aihawk_mcp_server
claude plugin install aihawk@feder-cr
```

Codex:

```bash
codex plugin marketplace add feder-cr/aihawk_mcp_server
codex plugin add aihawk@feder-cr
```

Gemini CLI:

```bash
gemini extensions install https://github.com/feder-cr/aihawk_mcp_server
```

## Options

| Option | Purpose |
|--------|---------|
| `--openrouter-key` | Agent model key, or `OPENROUTER_API_KEY` env var |
| `--model` | OpenRouter model id, defaults to `z-ai/glm-5.3-flash` |
| `--proxy` | `http://user:pass@host:port` or `socks5://host:port`. Timezone, locale, and egress follow the proxy |
| `--seed` | Same seed, same browser identity every run |
| `--profile-dir` | Persist logins and cookies across restarts |
| `--headed` | Show the browser window |

The `.env` file beside the command is read at startup and never overrides flags or environment variables. Keys passed as flags end up in shell history and process lists; use the environment or `.env` instead.

## Why it matters for CorpusIQ

Community and social operations hit captcha walls on proxy IPs. r/MCP self-posts are captcha-gated on datacenter proxies, and Reddit's spam filter silently drops automated comments. A stealth engine with seeded, proxy-anchored identities is the missing layer for those lanes, and `invisible_playwright` keeps the existing Playwright codebase without a rewrite.

## Source

- **GitHub:** [feder-cr/aihawk_mcp_server](https://github.com/feder-cr/aihawk_mcp_server)
- **Engine:** [feder-cr/invisible_playwright](https://github.com/feder-cr/invisible_playwright)
- **Identity core:** [feder-cr/invisible_core](https://github.com/feder-cr/invisible_core)
- **Wiki:** [AI browser-agent guides](https://github.com/feder-cr/aihawk_mcp_server/wiki)
