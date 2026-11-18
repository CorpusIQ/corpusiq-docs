---
title: "Craig Hewitt Skills - Founder, Sales and Creator Setup"
description: "thecraighewitt/skills: 5.8K combined installs across 64 listings; 47 founder, sales, and creator skills for any agent that reads markdown."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/craighewitt-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "sales", "youtube", "founder"]
---

# Craig Hewitt Skills - Setup Guide

**Source:** [thecraighewitt/skills](https://www.skills.sh/thecraighewitt/skills) via skills.sh - 5.8K combined installs across 64 indexed listings; first seen Nov 18, 2026 (this sweep)
**GitHub:** 175 stars, MIT license, `main` branch, last pushed 2026-05-22. Skills are grouped into `ceo/`, `sales/`, `youtube/`, `coding/`, `cowork/`, and `general/` directories, one SKILL.md per skill.
**Category:** Founder, sales and creator skills
**Quality Tier:** 🟢 Green - all 60 sampled verdict cells pass; MIT licence.

Craig Hewitt's skills teach an agent to operate as a founder, seller, and creator. The suite spans CEO, Sales, YouTube, and General categories plus a coding pipeline and a cowork set, and the same markdown files work in Claude Code, Cursor, Codex, Windsurf, and any agent that reads markdown. Each skill is a standalone prompt with no API keys and no dependencies.

The sales skills run the full deal cycle, from defining context and researching prospects through cold outreach, discovery, objection handling, and pricing. The YouTube skills cover scripting, packaging, and retention. Skills share context through per-category files: sales skills read a `sales-context.md` file, YouTube skills read a `youtube-context.md` file, and CEO skills read a `BUSINESS_CONTEXT.md` file created on first run.

## Installation

The README installs everything with one command:

```bash
npx skills@latest add TheCraigHewitt/skills --full-depth
```

To install one category only, point at the category directory:

```bash
npx skills@latest add TheCraigHewitt/skills/ceo
npx skills@latest add TheCraigHewitt/skills/sales
npx skills@latest add TheCraigHewitt/skills/youtube
```

To install a single skill, pass `-s` with the skill name:

```bash
npx skills@latest add TheCraigHewitt/skills/ceo -s strategic-sparring
```

For agents other than Claude Code (Cursor, Windsurf, Codex), clone the repository into an agent skills directory:

```bash
git clone https://github.com/TheCraigHewitt/skills.git .agents/skills
```

For Claude Projects on the web, copy a SKILL.md file's content into the project's custom instructions.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| retention-editing | 195 | Editing guidance for YouTube retention: pattern interrupts, pacing, and re-engagement so viewers keep watching. |
| hook-writing | 154 | Writes the first 30 seconds of a YouTube video: retention hooks, openings, and fixes for early drop-off. |
| linkedin-outreach | 139 | Writes LinkedIn connection requests, InMails, and DM sequences for social selling and Sales Navigator prospecting. |
| proposal-pricing | 138 | Builds proposals, SOWs, and pricing presentations to present a deal to a prospect. |
| thumbnail-design | 134 | Creates YouTube thumbnail concepts and styles that improve click-through rate. |
| script-structure | 134 | Writes YouTube video scripts with structure, pacing, and retention beats. |
| sales-context | 132 | Defines the sales context, ICP, value proposition, and sales motion that other sales skills read. |
| discovery-call | 132 | Plans discovery calls with qualification questions to prep for a first prospect meeting. |
| cold-call | 132 | Writes cold call scripts, phone objection handlers, dial blocks, and voicemails. |
| objection-handling | 131 | Builds objection playbooks and responses for price, timing, and competition pushback. |

The remaining 54 indexed listings range from 40 to 126 installs.

## Why This Matters for Hermes Agents

The suite encodes a full operating playbook rather than one-off prompts. Sales skills check for a `sales-context.md` file and every other sales skill reads it automatically, so an agent that runs `sales-context` first keeps one ICP, value prop, and set of proof points across every deal conversation. YouTube skills do the same with `youtube-context.md`, and CEO skills walk through creating `BUSINESS_CONTEXT.md` on first run.

For a Hermes agent, that means a single setup step seeds the shared context the rest of the suite depends on, and the individual skills then behave like a coached specialist instead of a generic assistant. The coding pair (`shape` and `ralph`) adds a planning-then-execution pipeline that carries an idea from PRD to implemented, tested code.

## Usage

| You say | What happens |
|---|---|
| "Set up my sales context and ICP" | Uses $sales-context to define value prop, sales motion, and proof points the other sales skills read. |
| "Write a cold call script for a new prospect" | Uses $cold-call to draft an opener, gatekeeper navigation, and voicemail. |
| "Prep me for tomorrow's discovery call" | Uses $discovery-call to build qualification questions for the first prospect meeting. |
| "They pushed back on price, how do I respond?" | Uses $objection-handling to draft a response from the objection playbook. |
| "Draft a LinkedIn connection request" | Uses $linkedin-outreach to write the connection request or InMail. |
| "Write the opening hook for my next video" | Uses $hook-writing to produce the first 30 seconds and a retention hook. |
| "Help me structure this video script" | Uses $script-structure to build pacing and retention beats. |

## Verification

Probe one skill on the `main` branch before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/thecraighewitt/skills/main/sales/sales-context/SKILL.md | head -12
```

Then install everything and open a skill file to confirm it landed:

```bash
npx skills@latest add TheCraigHewitt/skills --full-depth
```

The README documents no test suite. Each skill is a markdown prompt, so verification means reading the SKILL.md content and running one skill once.

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| retention-editing | Pass | Pass | Pass |
| hook-writing | Pass | Pass | Pass |
| linkedin-outreach | Pass | Pass | Pass |
| proposal-pricing | Pass | Pass | Pass |
| thumbnail-design | Pass | Pass | Pass |
| script-structure | Pass | Pass | Pass |
| sales-context | Pass | Pass | Pass |
| discovery-call | Pass | Pass | Pass |
| cold-call | Pass | Pass | Pass |
| objection-handling | Pass | Pass | Pass |
| lead-research | Pass | Pass | Pass |
| demo-script | Pass | Pass | Pass |
| negotiation | Pass | Pass | Pass |
| title-craft | Pass | Pass | Pass |
| outbound-sequence | Pass | Pass | Pass |
| call-debrief | Pass | Pass | Pass |
| buyer-persona | Pass | Pass | Pass |
| cold-email | Pass | Pass | Pass |
| referral-intro | Pass | Pass | Pass |
| channel-strategy | Pass | Pass | Pass |

The sample covers 20 of the 64 indexed listings, and every cell is Pass.

## Limitations

- Snapshot data, verified Nov 18, 2026: 5,765 combined installs across 64 indexed listings; 175 GitHub stars; MIT license; last pushed 2026-05-22. Counts drift over time.
- Each skill is a standalone markdown prompt with no framework, no runtime, and no dependencies, so quality rests on the prompt text rather than tested code.
- Sales, YouTube, and CEO skills depend on a shared context file (`sales-context.md`, `youtube-context.md`, or `BUSINESS_CONTEXT.md`) that you create on first run; until that file exists the dependent skills have less to work with.
- Installing by category pulls the whole directory, so a category install lands more skills than the single one you may want.
- The `watch` skill needs external binaries (`yt-dlp` and `ffmpeg`), unlike the rest of the suite which has no dependencies.

## Related

- [GTM Agents - Go-to-Market Sales Skills Setup](/hermes/skills/catalog/gtm-agents-setup)
- [Claude GTM Plugin Skills - GTM Teams Setup](/hermes/skills/catalog/claude-gtm-plugin-setup)
- [Kostja94 Marketing Skills - Copywriting, SEO, Ads Setup](/hermes/skills/catalog/kostja94-marketing-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `sales-context` before any other sales skill; it writes the `sales-context.md` file the rest of the suite reads.
- Do the same with `youtube-context` for the YouTube set, and let CEO skills walk you through `BUSINESS_CONTEXT.md` on first run.
- Install by category to pull a coherent set, or use `-s` to grab one skill without the rest.
- For YouTube retention, pair `hook-writing` (the opening) with `retention-editing` (the cut) and `script-structure` (the beats).

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
