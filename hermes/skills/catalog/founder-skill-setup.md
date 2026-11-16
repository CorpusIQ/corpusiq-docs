---
title: "Founder Skills - Validate Your Business Before Launch"
description: "jakeschincariol/founder-skill - 7.9K combined installs across 11 indexed listings: a board, a CFO and a 100-buyer panel that pressure-test an idea."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/founder-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "founder", "business validation", "startup"]
---

# Founder Skills - Setup Guide

**Source:** [jakeschincariol/founder-skill](https://www.skills.sh/jakeschincariol/founder-skill) via skills.sh - 7.9K combined installs across 11 indexed listings; first seen Nov 16, 2026 (Nov 16 morning sweep)
**GitHub:** 3,840 stars, MIT license, `main` branch, last pushed 2026-10-07, `SKILL.md` files under `skills/founder-<name>/`, one folder per skill
**Category:** Business validation - pressure-testing a business before launch
**Quality Tier:** 🟡 Yellow - eleven of eleven sampled; founder-competitors carries a Socket warn and founder-plan a Gen Agent Trust Hub warn, the rest pass cleanly.

The Founder skill is a suite of eleven Claude skills by Jake Schincariol that stress-test a business before you launch it. Each skill is a named role: a three-member board of directors reading the idea through the Offers lens from Alex Hormozi's $100M Offers, the Monopoly lens from Peter Thiel's Zero to One and the Product lens from Walter Isaacson's Steve Jobs biography; a marketing director; a CFO that computes unit economics; and a consumer panel that spins up 100 buyer agents trained on your target customer. Free, MIT, no signup, no API key.

The eleven skills are built to run in order, each reading what the earlier ones wrote into a `founder/` folder in your project, ending in `/founder-plan`, which compiles a business plan whose verdict is computed from the numbers rather than written by hand. The four tools are standard-library Python, need Python 3.8 or newer, and touch the network not at all.

## Installation

Install as a plugin in Claude Code:

```
/plugin marketplace add Jakeschincariol/founder-skill
/plugin install founder-skill@founder-skill
```

Claude Code namespaces plugin skills, so they show up as `/founder-skill:founder-board` and so on. Copy the folders instead if you want plain `/founder-board`:

```bash
git clone https://github.com/Jakeschincariol/founder-skill.git
cp -r founder-skill/skills/founder-* ~/.claude/skills/
```

Project-local instead of global: copy the same folders into your repo's `.claude/skills/`. No Claude Code at all? Paste any single `SKILL.md` at the top of a chat and it runs as a mode, though you lose the sub-agents and the Python tools. The tools need Python 3.8 or newer; nothing to pip install.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| founder-consumer | 731 | Consumer panel: 100 buyer sub-agents (or 20 in quick mode) run your pitch through buyer scenarios and tally buy rates by segment. |
| founder-cfo | 729 | Unit economics: contribution, margin, break-even per day, year 1 month by month, cash needed and payback. |
| founder-pricing | 728 | Van Westendorp price range from the panel's four price answers per buyer, set against competitors and the CFO's margin. |
| founder-competitors | 725 | Maps direct, indirect and substitute competitors from public sources only, every fact with a link. |
| founder-board | 723 | Three-member board scores the idea through the Offers, Monopoly and Product lenses, then votes fund, fund with conditions, or pass. |
| founder-offer | 716 | Builds an offer stack of bonuses, guarantee, urgency and a name, scored on the value equation and re-tested on a quick panel. |
| founder-marketing | 712 | Positioning, the channels buyers actually use, a 30-day launch campaign, ten hooks and a budget split. |
| founder-plan | 710 | Compiles every skill's output into a business plan whose verdict is computed from the numbers, never written by hand. |
| founder-launch | 708 | A dated launch plan: a cheap real-world test first, then a countdown, the launch-day run sheet and the first 30 days. |
| founder-brand | 706 | Names the business with the trademark, domain and handle checks to run, plus a voice, promise and look brief. |
| founder-ops | 705 | Suppliers, staffing, day-one routines, permits and a risk register, feeding real costs back to the CFO. |

No indexed listings fall below 700 installs; all 11 appear above.

## Why This Matters for Hermes Agents

The suite's strongest idea is sequencing: eleven skills run in a fixed order, each reading what the earlier ones wrote into a shared `founder/` folder, so the plan at the end is assembled from real intermediate outputs rather than generated whole. For an agent working a business idea end to end, a board verdict conditions the competitor map, which conditions the buyer panel, which conditions pricing and the offer.

The consumer panel is the unusual piece: 100 buyer sub-agents, each dealt a different income, age, habit and objection, all shown the same pitch. The tally is segment-level buy rates plus the reasons people pass in their own words, which is exactly the objection list the marketing and offer skills then answer. The README is explicit that this is a simulation, not a forecast, and treats the buy rate as an upper bound to confirm with real people.

founder-cfo keeps every number traceable to an input; a missing field is an error, never a guess. founder-plan's verdict is computed, not written: Profitable only if every unit earns money, year 1 makes a profit, break-even fits capacity and enough of the panel buys. For builders, that is a rare example of an agent pipeline whose summary is arithmetic, not prose.

## Usage

| You say | What happens |
|---|---|
| "Test my business idea" | founder-board scores the idea through three frameworks and votes fund, fund with conditions, or pass. |
| "Would people buy this?" | founder-consumer runs the pitch through 100 buyer agents and reports buy rates by segment. |
| "Do the numbers" | founder-cfo builds unit economics: margin, break-even, year 1 and cash needed. |
| "How much should I charge?" | founder-pricing derives a Van Westendorp price range and a price ladder. |
| "Who are my competitors?" | founder-competitors maps direct, indirect and substitute competitors with links. |
| "Put it all together" | founder-plan compiles the `founder/` folder into a business plan with a computed verdict. |

## Verification

Review the skill files before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/jakeschincariol/founder-skill/main/skills/founder-board/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/jakeschincariol/founder-skill/main/skills/founder-cfo/SKILL.md | head -20
```

Skills live under `skills/founder-<name>/`; confirm the path exists in the current tree before installing a specific one. After a plugin install, list them with `/skills`.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| founder-consumer | Pass | Pass | Pass |
| founder-cfo | Pass | Pass | Pass |
| founder-pricing | Pass | Pass | Pass |
| founder-competitors | Pass | Pass | Warn |
| founder-board | Pass | Pass | Pass |
| founder-offer | Pass | Pass | Pass |
| founder-marketing | Pass | Pass | Pass |
| founder-plan | Warn | Pass | Pass |
| founder-launch | Pass | Pass | Pass |
| founder-brand | Pass | Pass | Pass |
| founder-ops | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 16, 2026: 7,893 combined installs across 11 indexed listings; 3,840 GitHub stars; MIT; last pushed 2026-10-07. Counts drift over time.
- The consumer panel is simulated buyers, not customers: the README notes language models lean agreeable, so read the buy rate as an upper bound and confirm the big calls with real people.
- The board applies published frameworks in the author's own words; it never speaks as Hormozi, Thiel or Jobs, and the project is not affiliated with any of them.
- The numbers are only as good as the inputs: the CFO marks estimates as estimates and directs users to real supplier quotes and an accountant.
- Not financial, legal or tax advice: permits, trademarks and claims depend on where you are.
- The tools need Python 3.8 or newer, though nothing requires pip install.

## Related

- [Startup Founder Skills](/hermes/skills/catalog/startup-founder-skills-setup)
- [Startup Validation Skills](/hermes/skills/catalog/startup-validation-skills-setup)
- [Startup OS Skills](/hermes/skills/catalog/startup-os-skills-setup)
- [AI Business Skills](/hermes/skills/catalog/ai-business-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the eleven skills in the README's order: board -> competitors -> consumer -> pricing -> offer -> cfo -> marketing -> brand -> ops -> launch -> plan. Each reads what the earlier ones wrote.
- Use `/founder-consumer --quick` on a half-formed idea for a fast 20-buyer signal before committing to the full 100.
- Keep every intermediate output in the `founder/` folder; founder-plan compiles from them and its verdict is only as good as those files.
- Install as a plugin for namespaced commands (`/founder-skill:founder-board`) or copy the folders for plain `/founder-board`.
- Treat panel answers as research, never as testimonials, and confirm pricing and cost assumptions with real suppliers.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
