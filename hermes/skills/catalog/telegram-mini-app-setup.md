---
title: telegram-mini-app - Telegram Mini App Builder
description: "sickn33/agentic-awesome-skills - telegram-mini-app skill, 1.5K installs: build Telegram Mini Apps (TWA) - web apps inside Telegram covering the Web App API, TON Connect, in-app payments, user auth, and viral mechanics - from the 45.6K-star agentic-awesome-skills catalog."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/telegram-mini-app-setup/"
robots: "index,follow"
last_updated: "2026-08-28"
tags: ["hermes skill", "agent skill", "skill setup", "telegram", "mini-app", "ton", "web-app", "bot"]
---

# telegram-mini-app - Setup Guide

**Source:** [sickn33/agentic-awesome-skills/telegram-mini-app](https://skills.sh/sickn33/agentic-awesome-skills/telegram-mini-app)
**GitHub:** [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) (45.6K stars, Apache 2.0; skill content sourced from vibeship-spawner-skills)
**Skill:** `telegram-mini-app`, 1.5K installs
**Category:** Telegram / Web Apps
**First Seen:** Jan 19, 2026 on skills.sh; discrete guide created Aug 28, 2026 (the skill sits above the 100-install bar but was missing from the Aug 21 cluster roster)
**Quality Tier:** 🟡 Trusted - Gen Agent Trust Hub Pass, Socket Pass, Snyk Warn (verified Aug 28, 2026)

telegram-mini-app is a role-based playbook ("Telegram Mini App Architect") for building Telegram Mini Apps (TWA) - web apps that run inside Telegram with a native-like experience. It covers the Telegram Web App API, the TON ecosystem, TON Connect wallet integration, in-app payments, Telegram user authentication, and viral growth mechanics. Mini Apps run where 800M+ Telegram users already are, making them a zero-install distribution surface: users open the app inside a chat with no store download.

The skill is a single SKILL.md knowledge playbook - agent-agnostic procedural knowledge with no bundled CLI or service dependency. Any agent with web development capability can execute its patterns.

---

## Installation

Install just this skill via the skills.sh CLI:

```bash
npx skills add https://github.com/sickn33/agentic-awesome-skills --skill telegram-mini-app
```

Manual install (the skill lives under the repo's Claude-plugin skill tree):

```bash
mkdir -p ~/.hermes/skills/aas/telegram-mini-app
curl -sL https://raw.githubusercontent.com/sickn33/agentic-awesome-skills/main/plugins/agentic-awesome-skills-claude/skills/telegram-mini-app/SKILL.md \
  -o ~/.hermes/skills/aas/telegram-mini-app/SKILL.md
```

Install the full 2,000+ skill catalog instead:

```bash
npx skills add sickn33/agentic-awesome-skills
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Agent harness** | Any skills.sh-compatible agent (Hermes, Claude Code, Codex, Cursor) |
| **Telegram account** | A bot via @BotFather for bot-backed Mini Apps |
| **Web hosting** | Any static host serves a Mini App - they are plain web apps loaded in Telegram's webview |
| **TON Connect wallet** | Only for crypto payments / TON blockchain features |
| **Dependencies** | None - the playbook ships no scripts; the only runtime asset is Telegram's official `telegram-web-app.js` |

## What It Provides

**Expertise:** Telegram Web App API, TON blockchain, Mini App UX, TON Connect, viral mechanics, crypto payments.

**Capabilities:** Mini App architecture, TON Connect integration, in-app payments, Telegram user authentication, Mini App UX patterns, viral Mini App mechanics, TON blockchain integration.

**Patterns** (from the SKILL.md):

```html
<!-- Mini App Setup - basic structure -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="https://telegram.org/js/telegram-web-app.js"></script>
<script>
  const tg = window.Telegram.WebApp;
  tg.ready();
  tg.expand();
  const user = tg.initDataUnsafe.user;   // user auth, no OAuth flow
</script>
```

The playbook walks the full lifecycle: bootstrapping the webview, authenticating users from `initDataUnsafe`, wiring TON Connect for wallet actions, handling Telegram Stars payments, and designing for the Telegram UX paradigm rather than traditional web.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Zero-install distribution surface** | A CorpusIQ Mini App puts operator answers inside Telegram. User identity comes from `initDataUnsafe`, so there is no separate signup |
| **Bot-backed quick answers** | Pair the Mini App with a bot in the CorpusIQ community chat so questions resolve in-chat instead of bouncing to the web app |
| **In-app payments** | Telegram Stars / TON payments for premium CorpusIQ features without web checkout friction |
| **Viral mechanics** | The playbook's growth patterns (invites, share flows) applied to CorpusIQ community expansion |
| **TON ecosystem presence** | If CorpusIQ explores crypto-adjacent distribution, the TON Connect patterns are the entry point |

## Limitations / Verification

- **Snyk Warn** on the skills.sh audit page (Trust Hub and Socket are Pass) - the flag is why this is 🟡 Trusted, not 🟢. Review the [Snyk findings](https://skills.sh/sickn33/agentic-awesome-skills/telegram-mini-app/security/snyk) before shipping anything user-facing.
- **Knowledge-only playbook:** a single SKILL.md with no scripts, tests, or CI - all execution is on the agent.
- **TON/crypto emphasis:** the playbook leans on TON blockchain monetization; skip those sections if CorpusIQ stays fiat-only.
- **Publisher core tool targets Codex/Claude:** the AAS Core MCP is Claude/Codex-oriented, but this playbook itself is agent-agnostic procedural knowledge (same basis as the Aug 21 cluster guide).
- **Repo path caveat:** the skill lives under `plugins/agentic-awesome-skills-claude/skills/` (Claude-plugin tree), not the root `skills/` directory - use the paths in this guide, not the cluster guide's root-path example.

Verification after install:

```bash
ls ~/.hermes/skills/aas/telegram-mini-app/SKILL.md
head -3 ~/.hermes/skills/aas/telegram-mini-app/SKILL.md   # frontmatter: name, description
```

## Related

- [Agentic Awesome Skills - 2,000+ Skill Catalog Setup](/hermes/skills/catalog/agentic-awesome-skills-setup/) - the parent 45.6K-star catalog and its cluster guide
- [Skills Marketplace](/hermes/skills/marketplace/) - marketplace index for more discovery batches
