---
title: "browser-harness Setup Guide"
description: "Complete setup guide for browser-harness — AI agent browser automation skill from David Ondrej's skills collection. Control browsers through your agent on VPS and remote servers."
---

# browser-harness Setup Guide

**Skill:** `browser-harness` · **Installs:** 1,200+ · **Source:** [davidondrej/skills](https://github.com/davidondrej/skills)

Browser harness gives AI agents browser automation capabilities — navigate pages, click elements, extract data, fill forms, and take screenshots. Designed for headless operation on VPS and remote Linux servers where GUI browsers aren't available.

---

## Capabilities

- Page navigation and URL management
- Element clicking, typing, and form filling
- Content extraction and data scraping
- Screenshot capture for visual verification
- Cookie and session management

## Prerequisites

Node.js 18+, Playwright or Puppeteer installed on the system.

## Installation

```bash
npx skills add davidondrej/skills --skill browser-harness
```

## Usage

Load the skill in your agent session:

```
/ browser-harness
```

The skill activates and provides browser automation tools accessible through natural language commands.

## Troubleshooting

| Issue | Fix |
|---|---|
| Skill not found | Verify `npx skills add` completed successfully and the skill appears in `npx skills list` |
| Browser not launching | Ensure Playwright/Puppeteer is installed system-wide |
| Permission errors on VPS | Check that the agent user has access to the browser binary |

## Related Skills

- [vps-server-management](/hermes/skills/catalog/vps-server-management-setup/) — VPS server management and monitoring
- [distribute-skill-to-all-agents](/hermes/skills/catalog/distribute-skill-to-all-agents-setup/) — Sync skills across multiple agent instances
- [Skills Catalog](/hermes/skills/catalog/)
