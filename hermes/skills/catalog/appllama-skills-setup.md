---
title: "Appllama Skills - Mobile App Design Patterns Setup"
description: "Setup guide for appllama/appllama-skills - 7.6K combined installs. Skills that turn top-grossing app patterns into native-quality screens."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/appllama-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "mobile app design", "ui patterns"]
---

# Appllama Skills - Setup Guide

**Source:** [appllama/appllama-skills](https://www.skills.sh/appllama/appllama-skills) via skills.sh - 7.6K combined installs across 3 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [appllama/appllama-skills](https://github.com/appllama/appllama-skills) (2,537 stars, MIT; pushed Sep 6, 2026; `skills/<name>/SKILL.md` layout)
**Category:** Mobile App Design / Research
**Quality Tier:** 🟡 Beta - company-backed (appllama.io); MIT; 2,537 stars; all sampled verdicts Pass

Appllama (appllama.io) is a company-backed design library of top-grossing mobile apps - their real screens, flows, and UI patterns, with revenue and download context. Its skills turn that library into an agent's working method: study the screens of the apps that already win, extract the category's design language, then build screens that hold up next to them. The README frames the pair deliberately: `appllama-usage` is the research engine that runs on the Appllama MCP, while `appllama-app-design-skill` is the build bar for native-feeling Expo and React Native screens.

The pair is opinionated in a useful way. The design skill enforces Apple HIG fidelity, semantic colors, native controls, and navigation that behaves (push vs replace, sheets and overlays, no back-navigation into a paywall), plus a strict motion bar: decide whether something should animate at all, use springs that carry the finger's velocity, and keep animation off the JS thread. The loop only ends in a simulator, with whole flows recorded and scrubbed frame by frame rather than screenshots.

---

## Installation

```bash
# One command from your project root; works with Claude Code, Cursor, Codex, and 70+ agents
npx skills@latest add appllama/appllama-skills

# Non-interactive install for specific agents
npx skills@latest add appllama/appllama-skills -a claude-code -a cursor -y

# Install user-wide instead of per-project
npx skills@latest add appllama/appllama-skills -g

# Install only the build-bar skill; the same flag works for appllama-usage
npx skills@latest add appllama/appllama-skills --skill appllama-app-design-skill
```

Manual install: clone the repository and copy `skills/*` into your agent's skills folder (`~/.claude/skills/` user-wide or the harness equivalent). `appllama-usage` runs on the Appllama MCP at `https://mcp.appllama.io/mcp`, added as a custom connector in Claude, Cursor, Codex, or any MCP client. MCP access is part of the Pro plan, credits reset monthly, and each call spends one credit.

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| appllama-app-design-skill | 4,144 | Native-feeling Expo / React Native screens: HIG fidelity, motion bar, simulator-verified build loop |
| appllama-usage | 3,484 | Appllama MCP research: tool map plus playbooks for building, improving, and researching screens |

The remaining 1 indexed listing, appllama-design-skill, is a 6-install stub.

## Why This Matters for Hermes Agents

Mobile UI is where generic coding agents quietly underperform: screens render, but they do not feel native, animations run on the wrong thread, and navigation edge cases break in ways only real apps expose. This suite gives a builder agent an external quality bar - the patterns of top-grossing apps, extracted with revenue and download context - instead of asking it to invent taste from scratch. The pairing matters: one skill decides what to study, the other decides how to build, and both insist that a screen is not done until it survives a simulator comparison. The anti-slop discipline transfers beyond mobile: semantic tokens, native controls, and deliberate motion are the same habits that separate shippable UI from generated-looking UI. Because the content is plain `SKILL.md` over a documented MCP endpoint, everything is auditable, vendorable, and trimmable to fit a context budget. For agents that already juggle tool calls and files, the setup is one `npx` command and the payoff is a repeatable design workflow instead of a prompt gamble.

## Usage

| You say | What happens |
|---|---|
| "Build a habit tracker; study the top-grossing habit apps first" | appllama-usage extracts the category patterns, then appllama-app-design-skill builds and runs the simulator comparison loop |
| "Make this screen better" (with a screenshot or a Copy Screen ID) | The agent researches comparable screens and rebuilds against the category's design language |
| "How do the best fitness apps structure onboarding?" | A research answer on length, what each step earns, and where the paywall sits |
| "Wire up the checkout flow" | Navigation rules applied: which screens push, which present as sheets, and no back-path into the paywall |
| "Review the animations in this app" | A motion audit: what to delete, what is on the wrong thread, and what is missing velocity |
| "Extract the design language for this category" | Flow and element research from the Appllama library before any code is written |

## Verification

```bash
# Confirm the skills are installed for your agent
npx skills list | grep appllama

# Review the layout-verified skill straight from GitHub before installing
curl -sL https://raw.githubusercontent.com/appllama/appllama-skills/main/skills/appllama-app-design-skill/SKILL.md | head -20
```

Manual installs land in your agent's skills directory. `appllama-usage` additionally needs the Appllama MCP connector approved with your account before its research playbooks return data.

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| appllama-app-design-skill | Pass | Pass | Pass |
| appllama-usage | Pass | Pass | Pass |
| appllama | - | - | - |

The two scored samples are clean; the third entry is unrated, so extend your own review to anything you plan to run unattended.

## Limitations

- The research skill depends on the Appllama MCP: access is part of the Pro plan, and calls spend credits that reset monthly.
- Two working skills plus a 6-install stub; this is a focused suite, not a broad component library.
- MIT covers the code, but the Appllama name, llama, and logo are trademarks of Antmind Ventures Private Limited and are not granted for reuse.
- Verdict sampling covers 2 of 3 listings; the stub entry has no third-party review.
- Snapshot data, verified Oct 10, 2026: 7,634 combined installs across 3 indexed listings; 2,537 GitHub stars; MIT; last pushed Sep 6, 2026. Counts drift over time.

## Related

- [Mobile App UI Design Skill - Mobile Interface Setup](/hermes/skills/catalog/mobile-app-ui-design-skill-setup) - the closest single-skill counterpart for mobile interface work
- [Sleek Design Mobile Apps - AI Mobile App Design Skill Setup](/hermes/skills/catalog/sleek-design-mobile-apps-setup) - a mobile design skill with an AI-generation angle
- [Argent Skills - Mobile Dev Agent Toolkit Setup](/hermes/skills/catalog/argent-mobile-agent-skills-setup) - broader mobile development tooling for agents
- [Limrun Skills - Cloud iOS & Android Simulator Setup](/hermes/skills/catalog/limrun-skills-setup) - cloud simulators to pair with the simulator-verified loop
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the pair as intended: appllama-usage first to pick what to study, appllama-app-design-skill second to build; installing just one halves the method.
- The design skill works without the MCP: the simulator loop and anti-slop bar stand alone, so evaluate the workflow before committing to a Pro plan.
- Use the `--skill` flag when you only need one side of the pair and want to keep context lean.
- Paste a screenshot or a Copy Screen ID from appllama.io into "make this screen better" requests; the skill is built around that reference.
- Ask for the motion review before a flow is finished; deleting wrong-thread animations late is expensive.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
