---
title: "OpenClaudia Skills - 78-Skill Marketing Toolkit Setup"
description: "openclaudia/openclaudia-skills on skills.sh: 33.4K combined installs across 82 listings; 78 marketing skills for SEO, ads, email and social."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/openclaudia-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "marketing", "seo", "growth"]
---

# OpenClaudia Skills - Setup Guide

**Source:** [openclaudia/openclaudia-skills](https://www.skills.sh/openclaudia/openclaudia-skills) via skills.sh - 33.4K combined installs across 82 indexed listings; first seen 2026-11-07 (Nov 7, 2026 evening sweep)
**GitHub:** 731 stars, MIT, last pushed 2026-11-04, 78 SKILL.md files under `skills/`, one directory per skill, plus a `cli/` npm package that installs them and a `tools/` helper script
**Category:** Marketing execution for agents: SEO and site audits, paid ads, email, social publishing, conversion optimisation and analytics
**Quality Tier:** 🟡 Yellow - MIT with a LICENSE file at the repo root, but one sampled skill carries a Snyk Warn and several skills call paid third-party APIs with keys you supply.

OpenClaudia is a marketing toolkit built as agent skills rather than as a SaaS dashboard. The README is blunt about the comparison it wants: most marketing tools charge a monthly fee for suggestions, while this suite is free, runs locally, and is expected to actually write, publish and send. The pitch line is "78 modular skills that turn your AI coding agent into a full marketing department".

The suite is organised by job rather than by tool, in eleven groups from the README: SEO and site audit (9), content writing (9), email marketing (2), social media (6), ads and conversion (6), analytics and research (15), strategy and planning (8), messaging and notifications (5), content assets (4), growth and automation (11), and CRM and outreach (3). Coverage is broad for a repo this size: technical SEO audits, keyword research, paid search and paid social copy, drip sequences, Reddit and Bluesky publishing, landing page CRO, ICP definition, pricing and launch strategy. Several skills are thin wrappers over an API you already pay for, which is the honest way to read the install counts: `keyword-research` is a Semrush client, `ahrefs-research` is the Ahrefs Python SDK, and `email-sequence` sends through Resend.

## Installation

The README's prerequisite is Claude Code, installed and authenticated. The native installer pulls every skill:

```bash
npx openclaudia install --all
```

To install a subset, name the skills you want:

```bash
npx openclaudia install seo-audit write-blog email-sequence
```

The skills CLI route works without the OpenClaudia installer:

```bash
npx skills add OpenClaudia/openclaudia-skills
npx skills add OpenClaudia/openclaudia-skills --skill seo-audit
```

The README also documents a manual path, which is the one to use for a Hermes agent because it needs no Claude-specific wiring:

```bash
cp -r skills/seo-audit ~/.claude/skills/      # personal
cp -r skills/seo-audit .claude/skills/         # project-level
```

Each skill directory contains a single `SKILL.md` and nothing else, so one copy is a complete install. Point the same copy at whichever skills directory your Hermes agent reads, or keep the repository cloned and link the individual skill folders into it.

## What It Provides

Sixteen listings clear the 500-install threshold:

| Skill | Installs | Use For |
|---|---|---|
| feishu-lark | 1,618 | Posting messages and interactive cards to Feishu and Lark channels through a webhook or Bot API |
| facebook-ads | 1,052 | Facebook and Meta campaign structure, ad copy, audiences, budgets and retargeting |
| video-ad-analysis | 737 | Deconstructing a video ad creative into the reasons it works |
| content-calendar | 684 | Monthly and weekly content calendars, mix ratios, theme days and posting cadence |
| youtube-analytics | 621 | Channel and video performance through the YouTube Data API, including channel comparisons |
| google-ads | 569 | Google Ads copy and campaign structure, match types, Quality Score and bidding strategy |
| icp-builder | 548 | Ideal customer profiles and buyer personas from structured frameworks |
| copywriting | 540 | Marketing copy for landing, product, about and sales pages |
| reddit-marketing | 539 | Reddit community engagement and subreddit strategy that survives moderation |
| content-strategy | 531 | Topic clusters, editorial calendars and content mapped to buyer journey stages |
| google-analytics | 530 | GA4 traffic, acquisition, engagement and conversion reports through the Data API |
| search-console | 528 | Search Console clicks, impressions, CTR, index coverage and Core Web Vitals |
| social-content | 516 | Platform-specific posts for Reddit, X, LinkedIn, Instagram, Facebook and TikTok, with direct posting on some |
| page-cro | 512 | Landing page conversion audits, form and CTA optimisation, above-the-fold fixes |
| competitor-analysis | 511 | Competitor breakdowns across SEO, ads, social, email, pricing and positioning |
| telegram-bot | 502 | Telegram channel and group posts, polls and media through the Bot API |

The remaining 66 indexed listings range from 24 to 498 installs.

The shape of the tail matters more than its size. Below the threshold sit the specialist SEO skills (`seo-audit`, `keyword-research`, `serp-analyzer`, `backlink-audit`, `schema-markup`, `programmatic-seo`, `geo-query-finder`, `geo-difficulty`), the long-form writing set (`write-blog`, `write-landing`, `copy-editing`, `seo-content-brief`), and the channel clients (`bluesky`, `discord-bot`, `slack-bot`, `hubspot`, `apollo-outreach`). Install count here tracks search volume for the skill name, not usefulness. A skill called `seo-audit` competes with every other repo's `seo-audit`; a skill called `feishu-lark` does not.

## Why This Matters for Hermes Agents

The failure mode this suite fixes is the agent that produces marketing advice instead of marketing output. Ask a bare agent for a content calendar and you get a plausible table with no cadence, no mix ratio and no channel timing. `content-calendar` carries the ratios and the timing as rules, so the output is a schedule you can run rather than a template you have to fill.

The second gap is measurement. `google-analytics` and `search-console` are API clients, not copy generators, so an agent can pull the real numbers before it recommends anything. That turns "improve your SEO" into a specific set of queries with impressions and no clicks.

Third, the suite is unusually honest about routing. Skills declare trigger phrases in their descriptions, and the descriptions are written for the router rather than for a human reader: `page-cro` lists "why isn't my page converting" and "reduce bounce rate", `competitor-analysis` lists "who are my competitors" and "competitive matrix". A Hermes agent with this installed will match a plain request to the right skill without being told which one to use.

For a builder shipping a product, the practical value is the breadth of the launch surface: ICP, positioning, landing copy, ad copy on three platforms, an email sequence, a launch plan and a pricing page, all from one install and all written to files you can edit.

## Usage

| You say | What happens |
|---|---|
| "Audit the SEO on our site" | `seo-audit` walks technical and on-page checks and returns fixes, with `search-console` available for the query data behind them |
| "Write a launch sequence for the new plan" | `email-sequence` drafts the drip and can send it through Resend, with `email-subject-lines` for the subject variants |
| "Plan our content for next month" | `content-calendar` builds the schedule with mix ratios and timing, and `content-strategy` supplies the topic clusters behind it |
| "Who are our competitors and what are they doing" | `competitor-analysis` produces the SEO, ads, social, pricing and positioning breakdown, with `serp-analyzer` for the query-level view |
| "Our signup page is not converting" | `page-cro` audits the page and returns ranked changes, with `ab-test-setup` for the test design |
| "Post this to Feishu and Telegram" | `feishu-lark` and `telegram-bot` format the message per platform and send it through the Bot APIs |
| "Draft Meta ads for the spring campaign" | `facebook-ads` builds campaign structure, audiences, budgets and the ad copy itself |

## Verification

Read a skill before installing it. This path returned HTTP 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/openclaudia/openclaudia-skills/main/skills/competitor-analysis/SKILL.md | head -20
```

It should open with `name: competitor-analysis` and a description about breaking down competitors across SEO, ads, social, email, pricing and positioning.

After a full install, confirm the count in whichever skills folder your installer targets:

```bash
ls .claude/skills | wc -l
```

The README says the installer covers 78 skills, so a full install should land 78 directories. Anything less means a partial write.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| feishu-lark | Pass | Pass | Pass |
| facebook-ads | Pass | Pass | Pass |
| video-ad-analysis | Pass | Pass | Warn |

The instructions are markdown, but several skills ship their own scripts: `similarweb-traffic` and `competitor-traffic-report` include Node scripts, `gsc-portfolio-audit` a Python audit script, `podcast-edit` two Python media scripts, `task-banner` a macOS overlay script, and `github-stars` and `geo-difficulty` shell scripts. Read those before a skill runs them, particularly the two that cut or rewrite audio and video.

The real exposure beyond that is credentials. Several skills are API clients and expect keys: Semrush for `keyword-research`, Ahrefs for `ahrefs-research`, Resend for `email-sequence`, Google Ads and GA4 credentials for the advertising and analytics skills, and bot tokens for the chat platforms. Keep those in the environment or a secret store, never in the repository or in a skill file, and give each one the narrowest scope the platform allows.

The publishing skills are the second consideration. `social-content`, `thread-writer`, `discord-bot`, `slack-bot` and `telegram-bot` can post as you. Install those with a draft-only workflow first, and check the destination channel before any skill is allowed to send.

## Limitations

- Snapshot data, verified 2026-11-07: 33,390 combined installs across 82 indexed listings; 731 GitHub stars; MIT; last pushed 2026-11-04. Counts drift over time.
- The index outruns the tree by four. The repository holds 78 skill directories, so `unsplash-image` (376), `generate-image` (352), `brand-dev` (328) and `ahrefs-python` (320) carry install counts with no matching directory. Treat them as stale or renamed listings and confirm before relying on them.
- Several skills are wrappers, not engines. `keyword-research` needs a Semrush key, `ahrefs-research` needs Ahrefs, `email-sequence` needs Resend, and none of them work as a free tier.
- The install path is written for Claude Code. The `npx openclaudia install` flow targets Claude's skill directory, so a Hermes agent needs the manual copy or a symlink.
- The trigger-phrase approach is keyword matching. A request phrased far from the listed phrases can route to a neighbouring skill, and the agent may then run a pass you did not ask for.
- Nothing here is a scheduled job. These skills run when invoked, so a recurring calendar or monthly report needs your own scheduler around them.

## Related

- [Claude Ads - Paid Media Skill Suite Setup](/hermes/skills/catalog/claude-ads-setup)
- [Digital Marketing Pro - AI Marketing OS Setup](/hermes/skills/catalog/digital-marketing-pro-setup)
- [Content Strategy - Full Planning Framework for Hermes](/hermes/skills/catalog/content-strategy-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the four analytics and audit clients first (`seo-audit`, `search-console`, `google-analytics`, `competitor-analysis`). They produce the inputs that make every writing skill's output specific instead of generic.
- Read the trigger phrases before you install a skill. They are the router's contract, and they tell you exactly which request will wake it up.
- Keep API keys per-skill in the environment. One shared `.env` at the repository root across five platforms is how a token ends up in a commit.
- Run publishing skills in draft mode for the first week. `social-content` and `thread-writer` are the two that can speak in public on your behalf.
- Pair a writing skill with an audit skill in the same session. `write-blog` followed by `seo-audit` on the result catches the on-page gaps before publication rather than after.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
