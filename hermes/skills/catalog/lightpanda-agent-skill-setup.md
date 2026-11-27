---
title: "Lightpanda Agent Skill - Headless Browser for Agents"
description: "lightpanda-io/agent-skill: 1.8K combined installs. Headless browser and PandaScript replay skills for agent data extraction and automation."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/lightpanda-agent-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "headless browser", "web automation", "data extraction"]
---

# Lightpanda Agent Skill - Setup Guide

**Source:** [lightpanda-io/agent-skill](https://www.skills.sh/lightpanda-io/agent-skill) via skills.sh - 1.8K combined installs across 2 indexed listings; first documented 2026-11-27 (morning sweep)

**GitHub:** [lightpanda-io/agent-skill](https://github.com/lightpanda-io/agent-skill) - 121 stars, Apache-2.0, branch main, last pushed 2026-11-26; the main skill is a root SKILL.md, the pandascript sub-skill lives at pandascript/SKILL.md, and scripts/install.sh plus a Claude Code plugin manifest round out the tree

**Category:** Headless browser automation and deterministic replay scripts for agents, as a drop-in replacement for Chrome/Chromium

**Quality Tier:** 🟠 Orange - the pandascript sub-skill carries a Socket Fail and the main lightpanda skill a Snyk Warn, although the repository ships only Markdown plus one install shell script

Lightpanda is a headless browser built from scratch for AI agents, and this skill teaches an agent to use it as a drop-in replacement for Chrome/Chromium on data-extraction and automation tasks that do not need graphical rendering. The SKILL.md states the headline numbers directly: 9x faster and 16x less memory than Chrome, with JavaScript execution, a native MCP server with agent-optimized tools, a CLI for quick fetches, and a CDP server for Playwright/Puppeteer. A WebDriver server covers Selenium and BiDi clients.

The repository carries two skills. The main `lightpanda` skill documents the interfaces and when to use each: MCP server for interactive agent workflows, CLI fetch for one-off page extraction, CDP for custom Playwright/Puppeteer automation, WebDriver for Selenium, and agent mode for natural-language tasks or authoring a script. The companion `pandascript` sub-skill covers writing PandaScript, the deterministic replay-script format that runs token-free with `lightpanda run`. Lightpanda Cloud hosts the MCP and CDP servers plus an HTTP API for agents that cannot install a binary or keep a process running.

## Installation

The README documents one skills.sh route, a Claude Code plugin route, and a manual binary install:

```bash
npx skills add lightpanda-io/agent-skill
```

It prompts for the skills and target agent; pick `lightpanda`, plus `pandascript` if you will write replay scripts. Claude Code users can install the plugin, which also wires in the MCP server:

```bash
/plugin marketplace add lightpanda-io/agent-skill
/plugin install lightpanda@lightpanda
```

The skill does not install the binary on its own. Run the install script once before first use, then confirm the binary is present:

```bash
bash scripts/install.sh
command -v lightpanda
```

The MCP server is optional. For any MCP client that is not the Claude Code plugin, add it to the config:

```json
{ "mcpServers": { "lightpanda": { "command": "lightpanda", "args": ["mcp"] } } }
```

Platform support is Linux (x86_64, aarch64) and macOS (x86_64, arm64), with Windows only via WSL2.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| lightpanda | 1,734 | The main skill: Lightpanda browser interfaces (MCP server, CLI fetch, CDP, WebDriver, agent mode) for extraction and automation without graphical rendering. |
| pandascript | 34 | Writing PandaScript agent scripts (.js), the replayable browser-automation format run token-free with `lightpanda run script.js`. |

All 2 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

Browsing in an agent usually means a heavy Chrome/CDP stack or a hosted browser service. Lightpanda offers a native headless option that is far lighter and faster, which matters on constrained hosts and when one agent fans out many browsing tasks. The replay angle is the part most agents miss: capture a working automation as a PandaScript once, then rerun it deterministically with no model call, cutting both latency and cost on repeat work. The skill is interface-complete, so it fits different harness styles: MCP tools for conversational flows, CDP for Playwright/Puppeteer code, and WebDriver for Selenium. It also positions its own `search` MCP tool as an alternative when built-in web search is unavailable or when you need to follow links to full page content. For builders, the notable wrinkle is the install split: the skill and the binary are separate steps, and the plugin installer does not run install.sh automatically.

## Usage

| You say | What happens |
|---|---|
| "Fetch this page and give me the text" | Uses CLI fetch for a quick one-off extraction. |
| "Fill in this form and click submit" | Uses MCP server tools against a persistent browsing session. |
| "Run my Playwright automation" | Connects over the CDP server. |
| "Re-run this scraping job every hour" | Saves the flow as a PandaScript and reruns it with `lightpanda run`, no model call. |
| "I cannot install a binary here" | Points at Lightpanda Cloud's hosted MCP and CDP endpoints. |
| "Drive it through Selenium" | Uses the WebDriver server (Classic or BiDi). |

## Verification

The raw paths below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/lightpanda-io/agent-skill/main/SKILL.md

curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/lightpanda-io/agent-skill/main/pandascript/SKILL.md
```

Both print 200. After installing, confirm the binary and skill together:

```bash
command -v lightpanda
lightpanda --version
```

If `command -v lightpanda` comes back empty, the binary step did not run; run `bash scripts/install.sh` again.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| lightpanda | Pass | Pass | Warn |
| pandascript | Pass | Pass | Fail |

The pandascript Fail is what makes this guide orange. Both sampled listings pass the Gen Agent Trust Hub and Socket audits; pandascript fails Snyk and lightpanda warns. The repository ships Markdown plus one install shell script, so nothing executes on load beyond what the agent is told to run. The install script downloads the Lightpanda binary from the project's release channel, which is the main supply-chain surface to review before use. Run the installer once, from the skill's own scripts directory, rather than trusting a relocated copy.

## Limitations

- Snapshot data, verified 2026-11-27: 1,768 combined installs across 2 indexed listings; 121 GitHub stars; Apache-2.0; last pushed 2026-11-26. Counts drift over time.
- The binary install is a separate step and the plugin installer does not run scripts/install.sh automatically; a skill that loads without the binary fails at the first `lightpanda` command.
- Windows is supported only through WSL2, so a native Windows host has no direct path.
- The pandascript sub-skill sits far below the main skill in installs (34 versus 1,734), so most indexed usage is the browser skill rather than the replay format.
- pandascript carries a Socket Fail with no published reason; check the security page on skills.sh before adopting the replay format in production.

## Related

- [Agent Browser - Vercel Labs CLI for AI Agents Setup](/hermes/skills/catalog/agent-browser-setup)
- [Scrapling - Web Scraping Framework Skill](/hermes/skills/catalog/scrapling-setup)
- [Browser-Use Automation - AI Browser for Anti-Bot Sites Setup](/hermes/skills/catalog/browser-use-automation-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `lightpanda` only unless you write replay scripts; pandascript is the token-free format and most tasks never need it.
- Run `command -v lightpanda` before the installer each time; the install script downloads the latest release and re-running it is the documented fix for crashes.
- Save a repeat automation as a PandaScript early; the next run is a `lightpanda run` call with no model tokens.
- Prefer built-in web search when it is available and sufficient, and reach for the `search` MCP tool only when you need to follow links to full page content.
- Keep the MCP server optional: interactive browsing needs it, but one-off extraction is a CLI fetch with no persistent session.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
