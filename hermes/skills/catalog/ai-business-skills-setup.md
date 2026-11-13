---
title: "AI Business Skills - 147-Skill Marketing Team for Agents"
description: "minhnv0807/ai-business-skills: 4.4K combined installs across 96 listings, 147 marketing skills in Vietnamese and English with six agent roles"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ai-business-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-12"
tags: ["hermes skill", "agent skill", "skill setup", "marketing", "vietnam", "content operations"]
---

# AI Business Skills - Setup Guide

**Source:** [minhnv0807/ai-business-skills](https://www.skills.sh/minhnv0807/ai-business-skills) via skills.sh - 4.4K combined installs across 96 indexed listings; first seen Nov 12, 2026 (this sweep)
**GitHub:** 669 stars, MIT license, `master` branch, last pushed 2026-11-05, 148 `SKILL.md` files split between `skills/vi` and `skills/en`, plus 6 agent roles and 19 workflows
**Category:** Marketing operations for small businesses, built for Vietnam first and usable elsewhere
**Quality Tier:** 🟡 Established - a large, actively pushed, bilingual marketing system with a real operating model behind it, held back by a `master` branch, a listing cap that hides part of the library and a Vietnamese-first default.

This is the most structured marketing collection in the catalog so far. It is not a folder of prompts. There is a context layer (`.agents/product-marketing-context.md`, written once by an interview that the `product-marketing-context` skill runs), a role layer (six agents: `mkt-strategist`, `content-producer`, `design-producer`, `channel-operator`, `performance-analyst`, `personal-brand-builder`), and a workflow layer of 19 chains for multi-day jobs and monthly loops. Skills read the context file before doing anything, so the operator does not restate the business every session.

Every module exists twice. `skills/vi` carries the Vietnamese version and `skills/en` the English one, and the set switches on which context file is present rather than on a setting. The numbered prefixes (00 through 21) are the operating sequence: plan, brief, produce, publish, measure, diagnose.

The library is large and recent. Version 3.8.1, last pushed 2026-11-05, 494 files, 148 `SKILL.md` files for a README claim of 147 skills. Install counts cluster tightly between 78 and 80 for most of the visible set, which is what a suite looks like when people install the collection rather than individual skills. The top listing, `04-script-video` at 168 installs, is the Vietnamese short-form video script skill.

## Installation

The README documents a Claude Code plugin install:

```text
/plugin marketplace add minhnv0807/ai-business-skills
/plugin install ai-business-skills
```

Manual installation from a clone:

```bash
git clone https://github.com/minhnv0807/ai-business-skills.git
```

Copy the skills you want into your agent skills directory, keeping the `skills/vi` or `skills/en` parent so the language variant stays visible. The first run should be the context interview: `product-marketing-context` writes `.agents/product-marketing-context.md` inside the project, and every other skill reads that file before acting.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| 04-script-video | 168 | Short-form video scripts for TikTok, Reels and Shorts with a three-part hook and a second-by-second structure. |
| 04-script-video-global | 97 | The English version of the short-form script workflow, same structure and hook rules. |
| 08-nghien-cuu-doi-thu | 80 | Competitor research across three layers: direct rivals, indirect substitutes and adjacent players. |
| product-marketing-context | 79 | Interviews the operator and writes the context file every other skill reads. |
| 21-ads-audit-global | 79 | Paid ad account configuration audit with 84 checkpoints across account, campaign and ad level. |
| 17-pricing-strategy | 79 | Pricing model choice, package tiers, anchoring and a discount ladder. |
| 12-brief-landing-page | 79 | Brief for a new landing page: section order, copy per block and the offer structure. |
| 09-insight-khach-hang | 79 | Customer insight work: three-layer personas, voice of customer and objection mapping. |
| 00-ke-hoach-mkt | 79 | Overall marketing plan for a period: goals, segments, channels, budget, timeline and KPIs. |
| 21-audit-ads-performance | 78 | Performance audit through six stages from account settings to creative and landing page. |
| 18-referral-program | 78 | Referral and affiliate programme design for existing customers and partners. |
| 16-marketing-psychology | 78 | Why people buy, translated into scarcity, proof, social proof and commitment mechanics. |
| 14-email-marketing | 78 | Email and Zalo OA sequences: welcome, nurture, promotion and win-back flows. |
| 13-phan-tich-du-lieu | 78 | Turns raw Meta, TikTok, GA4, CRM or sheet data into decisions instead of charts. |
| 10-tinh-kpi-nguoc | 78 | Reverse KPI math: revenue target to required leads, maximum CPL and the budget that follows. |
| 06-brief-ugc-egc | 78 | Briefs for people who film for you: customers as UGC, staff as EGC and paid creators. |
| 05-copy-quang-cao | 78 | Paid ad copy with six variants across top, middle and bottom of funnel. |
| 03-danh-gia-hieu-suat | 78 | Diagnoses bad numbers across five layers: tracking, delivery, creative, audience and offer. |
| 02-brief-chien-dich | 78 | Campaign brief for the executing team: goal, message, deliverables, timeline and owners. |
| 01-content-calendar-global | 78 | Monthly or weekly content calendar with per-channel cadence and funnel ratio. |

The remaining 76 indexed listings range from 17 to 77 installs.

## Why This Matters for Hermes Agents

Marketing is where agents produce the most confident garbage, because a generic model writes generic copy that reads like every other generic model's copy. The fix is context, and this repository makes context a file that is written once and read by every skill. That single design choice is worth copying into any agent marketing stack, whether or not you install the suite.

The second useful idea is the role split. A strategist agent, a content producer, a designer, a channel operator, an analyst and a personal brand builder are different jobs with different inputs. One agent doing all six produces work that is mediocre in six ways. Six narrow roles with shared context produce work that is at least reviewable.

The third is the reverse KPI skill. Most marketing plans start with a budget and hope; this one starts from the revenue target and derives the leads, the maximum cost per lead and the budget that follows. That is arithmetic an operator can check, and it makes the rest of the plan falsifiable.

The Vietnamese-first default is not a limitation for a Vietnam-based operator, and it is a working example of localising a skill library rather than translating it at the end.

## Usage

| You say | What happens |
|---|---|
| "Start a marketing plan for this business" | Runs `product-marketing-context` first, then `00-ke-hoach-mkt` against that context file. |
| "I need a month of content" | Runs `01-content-calendar-global` with per-channel cadence and a funnel ratio. |
| "Write three TikTok scripts for this product" | Runs `04-script-video` and returns scripts with the hook structure and timing beats. |
| "Our cost per lead doubled, find out why" | Runs `03-danh-gia-hieu-suat` across the five diagnostic layers before proposing a fix. |
| "How many leads do I need to hit this revenue target?" | Runs `10-tinh-kpi-nguoc` and returns leads, maximum CPL and required budget. |
| "Audit this ad account" | Runs `21-audit-ads-performance` through the six stages and returns the checkpoint failures. |
| "Brief a creator to film this" | Runs `06-brief-ugc-egc` and returns a brief written for a non-professional filmer. |

## Verification

Probe the two language trees before installing. Both return 200, and the second one is on `master`, not `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/minhnv0807/ai-business-skills/master/skills/vi/04-script-video/SKILL.md | head -8
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/minhnv0807/ai-business-skills/master/skills/en/21-ads-audit-global/SKILL.md
```

After installation, confirm that `.agents/product-marketing-context.md` exists in the project before running any marketing skill. Without it the skills answer from general knowledge, which is the failure mode this suite exists to remove.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-12) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| 04-script-video | Pass | Pass | Pass |
| 04-script-video-global | Pass | Pass | Pass |
| 08-nghien-cuu-doi-thu | Pass | Pass | Warn |
| product-marketing-context | Pass | Pass | Pass |
| 21-ads-audit-global | Pass | Pass | Warn |

The Warns land on the two skills that reach outside the machine: competitor research fetches pages, and the ad audit reads platform data. Everything else is instruction text. The context file is the sensitive asset in practice, since it holds positioning, proof points and customer detail, and it sits inside the project directory where it will be committed unless you ignore it.

## Limitations

- Snapshot data, verified 2026-11-12: 4,442 combined installs across 96 indexed listings; 669 GitHub stars; MIT license; last pushed 2026-11-05. Counts drift over time.
- 96 is the cap of the skills.sh search API and the repository carries 148 `SKILL.md` files against a README claim of 147 skills, so both the listing count and the combined total are floors.
- The default branch is `master`. Any raw URL or install command written against `main` will fail.
- Most skills are Vietnamese. The English set covers a subset of the modules, so a non-Vietnamese operator gets a smaller library than the 147 the README advertises.
- The suite is opinionated about channels: Zalo OA, Facebook and TikTok are first class, and email is a secondary path.
- `.agents/product-marketing-context.md` will contain commercial detail. Add it to `.gitignore` before the first interview.

## Related

- [Aaron Marketing Skills - Full Marketing Department Setup](/hermes/skills/catalog/aaron-marketing-skills-setup)
- [Digital Marketing Pro - AI Marketing OS Setup](/hermes/skills/catalog/digital-marketing-pro-setup)
- [AI Marketing Skills - 24-Skill Operator Toolkit](/hermes/skills/catalog/ai-marketing-claude-code-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the context interview before anything else. Every other skill reads the file, and a thin context file produces generic work regardless of which skill you invoke.
- Keep the `vi` and `en` trees separate on install. Mixing them means the agent picks a language by whichever file it loaded last.
- Use `10-tinh-kpi-nguoc` before the plan, not after. The budget it derives is a constraint the plan should be built inside.
- Treat `21-audit-ads-performance` as a checklist to run monthly. The six stages only work as a sequence, and skipping to creative is the usual mistake.
- The six agents map to six review gates. If one person reviews strategy, copy and creative in the same pass, the role split is not buying you anything.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
