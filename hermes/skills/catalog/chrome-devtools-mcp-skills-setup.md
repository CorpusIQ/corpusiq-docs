---
title: Chrome DevTools MCP Skills — Browser Debugging & Automation Setup Guide for Hermes Agents
description: "chromedevtools/chrome-devtools-mcp — the official Google Chrome DevTools skills: chrome-devtools (5,934 installs) for MCP-driven browser debugging and automation, chrome-devtools-cli (2,572 installs) for terminal browser scripting. Works with any MCP-capable agent including Hermes."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/chrome-devtools-mcp-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes skill", "agent skill", "skill setup", "browser automation", "chrome devtools", "mcp"]
---

# Chrome DevTools MCP Skills — Setup Guide

**Source:** [chromedevtools/chrome-devtools-mcp](https://skills.sh/chromedevtools/chrome-devtools-mcp)
**GitHub:** [chromedevtools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)
**Skills:** `chrome-devtools` (5,934 installs) · `chrome-devtools-cli` (2,572 installs)
**Category:** Browser Automation & Debugging
**First Seen:** August 14, 2026 sweep
**Quality Tier:** 🟢 Production

The official Google Chrome DevTools skills let an agent drive a real Chrome browser through the Chrome DevTools Protocol (CDP) — navigate pages, click and fill forms via accessibility-tree snapshots, read console output and network requests, capture performance traces, and debug JavaScript. Because the transport is an MCP server (`npx chrome-devtools-mcp`), any MCP-capable agent can use it, including Hermes via its native MCP client. Two skills ship in the repo: `chrome-devtools` for agent-driven tool calling, and `chrome-devtools-cli` for browser automation from shell scripts.

---

## Installation

Install both skills from skills.sh:

```bash
npx skills add chromedevtools/chrome-devtools-mcp
```

Register the MCP server in Hermes (`~/.hermes/config.yaml` under `mcp_servers`):

```yaml
mcp_servers:
  chrome-devtools:
    command: npx
    args: [chrome-devtools-mcp@latest]
```

Optional capability flags (add to `args`):
- `--categoryExtensions` — enable extension tooling (install/list/inspect extensions)
- `--memoryDebugging` — enable memory debugging tools
- `--browserUrl http://127.0.0.1:9222` — attach to an existing Chrome instead of auto-launching

The server starts Chrome automatically on first tool call using a persistent profile. The skill does not apply in `--slim` mode (no MCP configuration).

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js 20.19+ / 22.12+** | Required by chrome-devtools-mcp (Node version check enforced) |
| **Google Chrome** | Stable or Canary — the server launches it automatically on first call |
| **Hermes Agent** | Any recent version with the native MCP client (see `hermes mcp` / config.yaml `mcp_servers`) |
| **npx** | Bundled with Node.js — used to run the MCP server |

## What It Provides

### chrome-devtools (MCP tools, agent-driven)

| Capability | Tools | Notes |
|---|---|---|
| Page navigation | `navigate_page`, `new_page`, `list_pages`, `select_page` | Tools operate on the currently selected page |
| Interaction | `take_snapshot`, `click`, `fill`, `hover`, `press_key` | Snapshot returns `uid` refs — always re-snapshot before acting |
| Script evaluation | `evaluate_script` | Run JS in the page, return JSON |
| Network inspection | `list_network_requests`, `get_network_request` | Request/response headers and bodies |
| Console & errors | `list_console_messages`, `get_console_message` | Catch client-side errors |
| Performance | `performance_start_trace`, `performance_stop_trace` | Core Web Vitals + insight highlights |
| Extension tooling | `install_extension`, `list_extensions` (requires flag) | For testing your own extensions |

### chrome-devtools-cli (terminal automation)

```bash
chrome-devtools list_pages
chrome-devtools take_snapshot          # uid-based element snapshot
chrome-devtools click --uid 1_3
chrome-devtools fill --uid 1_4 --value "hello@example.com"
chrome-devtools navigate_page --url https://www.corpusiq.io/docs/
chrome-devtools evaluate_script --function "() => document.title"
```

The CLI starts the background server implicitly — do not run `start`/`status`/`stop` before each use. State persists across commands.

## Quick Start

1. `npx skills add chromedevtools/chrome-devtools-mcp`
2. Add the `mcp_servers.chrome-devtools` block to `~/.hermes/config.yaml` and restart Hermes
3. In session: "list my open Chrome pages and take a snapshot of the active one"
4. "Run an accessibility snapshot of https://www.corpusiq.io/docs/ and click the pricing link"
5. For scripted work: `chrome-devtools take_snapshot | grep "Sign in"`

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Docs site QA** | Take snapshots and screenshots of docs.corpusiq.io pages after deploys to verify rendering, catch console errors |
| **Frontend debugging** | Inspect console messages and network requests on www.corpusiq.io to trace failed API calls |
| **Form-flow testing** | Automate signup/demo-request flows with `click`/`fill` to verify conversion paths end-to-end |
| **Performance auditing** | Run performance traces against landing pages to catch LCP/CLS regressions before launch |
| **Competitor page teardown** | Snapshot competitor pricing/dashboard flows headlessly for structured research notes |

## Limitations / Verification

- File access is restricted to the OS temp dir by default; unrestricted paths need `--allowUnrestrictedPaths=true`
- Single browser instance per server — parallel page work must be serialized through the same server
- MCP tools require a full Hermes restart after config.yaml changes

```bash
# Verify the MCP server is registered
hermes mcp list | grep chrome-devtools

# Functional test via CLI
chrome-devtools navigate_page --url "https://example.com" && chrome-devtools take_snapshot
```

## Security

- [MCP security best practices](/hermes/best-practices/security/) — official guidance on MCP tool exposure
- [chrome-devtools-mcp security policy](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/SECURITY.md) — Google's vulnerability reporting
- [MCP auth docs](https://modelcontextprotocol.io/docs/learn/security) — server trust boundaries

## Related

- [MCP & API Integration catalog section](/hermes/skills/catalog/)
- [Hermes browser automation skills](/hermes/skills/catalog/) — `agent-browser`, `browser-use-automation`, `playwright-social-media-automation`
- [Chrome DevTools MCP repo](https://github.com/ChromeDevTools/chrome-devtools-mcp)

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
