---
title: "Flightclaw Skills - Flight Agent Setup"
description: "Flight search, price tracking, and booking skill for AI agents via the mcp.flightclaw.com MCP server; ~1,082 installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/flightclaw-agents-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "travel", "mcp"]
---

# Flightclaw Skills - Setup Guide

**Source:** [flightclaw/agents](https://github.com/flightclaw/agents) (74⭐)
**Skill family:** `flightclaw/agents` (1 installable skill)
**Combined Installs:** ~1,082 across indexed listings (Sep 29, 2026 snapshot)
**Category:** Automation
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published - verified Sep 29, 2026)

Flightclaw provides flight search, price tracking, and booking for AI agents, delivered through a hosted MCP server (mcp.flightclaw.com) plus this open-source skill. The family consists of a single skill - `flightclaw` - with 1,082 indexed installs and a verified SKILL.md entry (1/1) in the Sep 29, 2026 snapshot. This guide covers installing the skill; server-side flight data is served by the hosted MCP endpoint.

---

## Installation

```bash
npx skills add flightclaw/agents
```

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Travel-concierge agent | Use the flightclaw skill to drive flight search and price tracking through mcp.flightclaw.com |
| Booking automation | Route booking flows through the hosted MCP server with the skill as the agent-side guide |

## Limitations / Verification

- The single skill has a verified SKILL.md entry on skills.sh (1/1, Sep 29, 2026 snapshot).
- The skill pairs with a hosted MCP server at mcp.flightclaw.com; access terms for the server are published by Flightclaw and were not reviewed here.
- The repo's default branch is `master`. No live install test has been run from Hermes yet.

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
