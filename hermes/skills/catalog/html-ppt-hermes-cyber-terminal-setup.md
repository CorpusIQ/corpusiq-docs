---
title: html-ppt-hermes-cyber-terminal — Setup Guide
description: Cyber-terminal themed HTML/PPT presentation skill for Hermes Agent from the nexu-io/open-design repo (82.7K⭐). Generate slide decks and terminal-styled presentations.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/html-ppt-hermes-cyber-terminal-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# html-ppt-hermes-cyber-terminal — Setup Guide

**Source:** [nexu-io/open-design](https://github.com/nexu-io/open-design) (82,734 ⭐)
**Skill:** `html-ppt-hermes-cyber-terminal`
**Installs:** 192

A cyber-terminal themed HTML/PPT presentation skill. Part of the open-design ecosystem — the open-source Claude Design alternative. Generates slide decks, terminal-styled HTML presentations, and cyberpunk-themed visual output directly from Hermes Agent prompts.

## Installation

```bash
npx skills add https://github.com/nexu-io/open-design --skill html-ppt-hermes-cyber-terminal
```

After install, reload skills:
- Hermes CLI: `/reload-skills` or restart session
- Hermes gateway: `/restart` or `hermes gateway restart`

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v2.0+ |
| Node.js | v18+ (for npx) |
| Terminal access | Required for HTML/PPTX file generation |

## Capabilities

| Capability | Trigger | Output |
|-----------|---------|--------|
| Cyber-terminal slide deck | "Create a cyber-terminal presentation about X" | HTML/PPTX file |
| Honest-review deck | "Generate an honest-review deck for X" | HTML slides |
| Terminal-themed output | Any prompt requesting terminal-styled visuals | Styled HTML |

## CLI/Command Reference

The skill is invoked through Hermes Agent prompts, not standalone CLI. Once installed, Hermes agents can call the skill natively:

```
"Use the html-ppt-hermes-cyber-terminal skill to create a deck about..."
```

## CorpusIQ Use Cases

1. **Investor pitch decks** — Generate terminal-styled pitch decks for CorpusIQ fundraising
2. **Product walkthrough slides** — Create slide decks for CorpusIQ feature demonstrations
3. **Community presentation** — Generate talk slides for AI/tech community events
4. **Internal reporting** — Create terminal-themed internal status dashboards
5. **Marketing collateral** — Generate visually distinctive marketing presentations

## Troubleshooting

| Issue | Likely Cause | Resolution |
|-------|-------------|------------|
| Skill not found | Install not reloaded | Run `/reload-skills` or restart |
| HTML output empty | Prompt too vague | Provide specific topic and style guidance |
| PPTX generation fails | Missing dependencies | Ensure open-design runtime deps are installed |
| Terminal styling broken | CSS theme mismatch | Try specifying "dark terminal theme" in prompt |

## Verification

After installation, verify the skill is loaded:
```bash
hermes skills list | grep html-ppt-hermes-cyber-terminal
```

Test with a simple prompt:
```
"Generate a simple 3-slide cyber-terminal presentation about Hermes Agent features"
```
