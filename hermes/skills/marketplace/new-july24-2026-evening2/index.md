---
title: "New Skills — July 24, 2026 Evening Sweep #2"
description: "4 new Hermes-relevant skills discovered on skills.sh — Claude Code, OpenAI Codex, Superpowers, Clerk Auth. 1.5M+ combined installs across 4 publishers."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-july24-2026-evening2/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "skill marketplace", "skills.sh"]

---

# New Skills — July 24, 2026 (Evening Sweep #2)

## Summary

| Metric | Count |
|---|---|
| New publishers found | 4 |
| Setup guides created | 4 |
| Combined installs | ~1.5M+ |
| Combined GitHub stars | 445K+ |
| Quality: 🟢 Production | 4 |
| Quality: 🟡 Beta | 0 |
| Quality: 🔵 Community | 0 |

## New Skills

### Agent Infrastructure

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **Claude Code Skills** | anthropics/claude-code | 73K+ | 139K⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/claude-code-skills-setup/) |
| **OpenAI Codex Skills** | openai/skills | 38K+ | 24K⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/openai-codex-skills-setup/) |
| **Superpowers** | obra/superpowers | 1.2M+ | 261K⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/superpowers-setup/) |

### Development

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **Clerk Auth Skills** | clerk/skills | 156K+ | 61⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/clerk-auth-skills-setup/) |

## 🔑 Standout Find: obra/superpowers (1.2M+ installs, 261K⭐)

The most-installed agent skills framework on skills.sh. Superpowers provides battle-tested development methodology for AI coding agents: brainstorming (294K installs), systematic debugging (199K), TDD (177K), writing plans (196K), and code review (178K). For Hermes agents doing implementation work, this is the missing methodology layer that enforces engineering rigor.

## Other Highlights

- **anthropics/claude-code** (73K installs, 139K⭐): Skills for building Claude Code extensions — agent development, skill creation, plugin authoring, and hook rules
- **openai/skills** (38K installs, 24K⭐): Codex CLI extensibility — PDF generation, CI/CD fixes, security auditing, Playwright testing, Figma design-to-code
- **clerk/skills** (156K installs): The most-installed authentication skill set — Next.js patterns, custom UI, backend API, webhooks, testing

## Discovery Method

Bulk sweep: 55 search terms via `npx skills search` → 114 unique repo/publisher entries → cross-referenced against 232 existing catalog entries → publisher-level verification against 138 known publishers → 4 confirmed new, 57 matched existing, 53 filtered (non-Hermes or already catalogued under different names).

## Notes

- Google/skills returned empty from skills.sh search (redirected to googleworkspace/cli which is already catalogued)
- larksuite/cli found (1.9M installs) but Feishu-only — skipped as China-market-specific
- This sweep completes the July 24 discovery cycle (morning sweep found 4, noon sweep found 5, evening sweep #1 found 3, evening sweep #2 found 4 = 16 total new publishers documented today)
