---
title: "browser-harness Setup Guide - CorpusIQ Docs"
description: "Complete setup guide for browser-harness - AI agent browser automation skill from David Ondrej's skills collection."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/browser-harness-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# browser-harness Setup Guide

**Skill:** `browser-harness` · **Installs:** 971 (skills.sh, 2026-11-27) · **Source:** [browser-use/browser-harness](https://github.com/browser-use/browser-harness)

Browser harness gives AI agents control of a real Chrome browser over the DevTools Protocol - navigate pages, click elements, extract data, fill forms, and take screenshots, signed in as the user. It is now the engine inside [Browser Use](https://github.com/browser-use/browser-use): the `browser-use` CLI ships the same helpers and daemon, and the `browser-harness` command keeps working. On servers without a GUI, it drives a headless Chrome the same way.

---

## Capabilities

- Page navigation and URL management
- Element clicking, typing, and form filling
- Content extraction and data scraping
- Screenshot capture for visual verification
- Cookie and session management, using the browser's existing logins

## Prerequisites

`uv` (Python 3.12 toolchain), Chrome or Chromium with a DevTools endpoint, and write access to the agent's skills directory.

## Installation

```bash
uv tool install --python 3.12 --upgrade --force browser-harness
browser-harness skill > "${CODEX_HOME:-$HOME/.codex}/skills/browser-harness/SKILL.md"
```

Or register the skill through the skills CLI:

```bash
npx skills add browser-use/browser-harness --skill browser-harness
```

## Usage

Smoke-test the harness first:

```bash
browser-harness <<'PY'
print(page_info())
PY
```

If `page_info()` prints, open `chrome://inspect/#remote-debugging` in your browser and tick the allow checkbox so the harness can attach. Then load the skill in your agent session and it provides the browser automation tools through natural language commands. Run `browser-harness recordings` once to set the local screenshot and action-trace preference.

## Troubleshooting

| Issue | Fix |
|---|---|
| Skill not found | Re-run `browser-harness skill` and write its output to the agent's skills directory; remove any stale user-installed `browser` or `browser-use` skill directory that shadows it |
| Browser not launching | Open `chrome://inspect/#remote-debugging` and tick the allow checkbox, or start Chrome with a DevTools port on a headless server |
| Permission errors on VPS | Check that the agent user can execute the browser binary and read its profile directory |

## Related Skills

- [vps-server-management](/hermes/skills/catalog/vps-server-management-setup) - VPS server management and monitoring
- [distribute-skill-to-all-agents](/hermes/skills/catalog/distribute-skill-to-all-agents-setup) - Sync skills across multiple agent instances
- [Skills Catalog](/hermes/skills/catalog)
