---
title: "Creator Marketing Skills - 34-Skill Program Setup"
description: "archive-dot-com/creator-marketing-skills: 2.1K combined installs across 34 listings, skills for creator briefs, vetting, outreach and reporting."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/archive-dot-com-creator-marketing-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "creator marketing", "influencer marketing", "content marketing", "marketing automation"]
---

# Creator Marketing Skills - Setup Guide

**Source:** [archive-dot-com/creator-marketing-skills](https://www.skills.sh/archive-dot-com/creator-marketing-skills) via skills.sh - 2.1K combined installs across 34 indexed listings; first seen Nov 13, 2026 (evening sweep)

**GitHub:** 22 stars, no licence file (GitHub reports no licence and no LICENSE file ships in the tree, although the README footer claims MIT), `main` branch, last pushed 2026-04-30, 37 `SKILL.md` files across `skills/` and `internal/`, 50 files in total

**Category:** Creator and influencer marketing workflows for consumer brands and agencies

**Quality Tier:** 🟡 Yellow - a broad 34-skill program with an all-pass sampled verdict set, but no licence file and the whole pack tops out at 82 installs.

Built by Archive.com for creator marketing teams at consumer brands and agencies, this pack automates the repetitive manual work of running a creator program: writing briefs, vetting creators, generating reports and crafting outreach. It ships 34 indexed listings against 37 SKILL.md files, the extra three being internal meta-skills under `internal/`. The repository has no description on GitHub and reports no licence.

The README is explicit that the skills are designed to work as one system: run brand-context first to build a shared brand file that every other skill reads, then branch into discovery, vetting, outreach, briefing, review, metrics and reporting. The highest install count in the pack is 82, so this is a small but broad set rather than a heavily adopted one.

## Installation

The README offers a no-code Cowork path and a CLI path. For the CLI:

```bash
# Install all skills
npx skills add archive-dot-com/creator-marketing-skills

# Install specific skills only
npx skills add archive-dot-com/creator-marketing-skills --skill brand-context creator-outreach-sequence-generator

# List available skills
npx skills add archive-dot-com/creator-marketing-skills --list
```

Skills land in `.claude/skills/`. To clone and copy manually instead:

```bash
git clone https://github.com/archive-dot-com/creator-marketing-skills.git
cp -r creator-marketing-skills/skills/* .claude/skills/
```

The Cowork path skips the terminal: download the ZIP from the repo, add the folder in Claude Desktop Cowork mode, and type "Install the skills from this folder".

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| multi-platform-format-adapter | 82 | Adapting a master creator brief into TikTok, Instagram Reels and YouTube Shorts versions with correct specs and safe zones. |
| creator-content-concept-generator | 75 | Generating 5-10 content concepts that feel native to a creator's style rather than brand-dictated. |
| paid-social-creative-brief | 71 | Turning a whitelisted or Spark Ad creator post into a paid social brief with hook analysis, targeting and placement recommendations. |
| creator-outreach-sequence-generator | 69 | Generating a multi-touch outreach sequence across email, Instagram DM, TikTok DM, YouTube email and X DM. |
| campaign-roi-calculator | 68 | Calculating influencer campaign ROI and building a leadership-ready narrative from raw performance data. |
| brand-context | 68 | Building the shared brand context file that every other skill reads before starting. |
| organic-repost-caption-writer | 66 | Turning a creator caption, handle and brand voice into three ready-to-post repost captions with credit. |
| reply-triage-classifier | 65 | Classifying influencer replies into interested, negotiating, declined, needs info and ghosted, with a next action each. |
| niche-fit-scorer | 65 | Scoring a creator's niche fit for a brand on a 1-10 scale with written rationale. |
| campaign-brief-generator | 65 | Generating a complete ready-to-send campaign brief from product, platforms, deliverables, messaging and audience. |

The remaining 24 indexed listings range from 22 to 64 installs.

## Why This Matters for Hermes Agents

Creator marketing is a workflow-heavy discipline: the same briefs, vetting checks, disclosure reviews and reports repeat across every campaign, and teams usually do them by hand in spreadsheets and DMs. These skills encode that process so an agent can run the repetitive parts end to end.

The composability is the strong point. brand-context builds one shared file, and the other 33 skills read it, so the agent does not re-ask the brand's audience, platforms and goals on every task. The README even lists plain-language trigger phrases that map to the right skill, which makes the pack easy to drive without memorising names.

Compliance is handled as a first-class step rather than an afterthought. FTC disclosure spot-checking and brand safety screening are built into the workflow, which are easy checks to skip when a human is moving fast.

## Usage

| You say | What happens |
|---|---|
| "Write outreach DMs for these 5 creators" | Runs `creator-outreach-sequence-generator` and returns a multi-touch sequence with personalization hooks. |
| "Is this creator's audience a good fit for our brand?" | Runs `audience-demographic-analyzer` and returns a pass/fail alignment verdict. |
| "Check if this caption is FTC compliant" | Runs `ftc-disclosure-spot-checker` and flags disclosure issues with concrete fixes. |
| "Turn our team's feedback into a revision request for the creator" | Runs `content-approval-feedback-formatter` and returns a ready-to-send request. |
| "Score these creators for our niche" | Runs `niche-fit-scorer` and returns 1-10 scores with written rationale. |
| "Build a KPI framework from our campaign goal" | Runs `campaign-goal-to-kpi-framework-builder` and maps objectives to primary and secondary KPIs. |
| "What is the ROI on this campaign so far?" | Runs `campaign-roi-calculator` and returns a leadership-ready summary. |

## Verification

Probe three skills on the `main` branch before installing. All three return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/archive-dot-com/creator-marketing-skills/main/skills/multi-platform-format-adapter/SKILL.md | head -20
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/archive-dot-com/creator-marketing-skills/main/skills/brand-context/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/archive-dot-com/creator-marketing-skills/main/skills/campaign-roi-calculator/SKILL.md
```

The layout is `skills/<name>/SKILL.md`, with three internal meta-skills under `internal/`. Confirm a skill exists in the current tree before scripting around it, since the repo has been quiet since April 2026.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| multi-platform-format-adapter | Pass | Pass | Pass |
| creator-content-concept-generator | Pass | Pass | Pass |
| paid-social-creative-brief | Pass | Pass | Pass |
| creator-outreach-sequence-generator | Pass | Pass | Pass |

All four sampled skills pass all three auditors. The other 30 listings publish no verdict, which is not the same as a pass. The repo reports no licence file, so confirm reuse terms before redistributing anything. The pack is overwhelmingly Markdown (45 of 50 files), with a single JavaScript file and a few YAML and JSON config files, so most skills are prompt-only but a couple ship helper code worth reading.

## Limitations

- Snapshot data, verified 2026-11-13: 2,067 combined installs across 34 indexed listings; 22 GitHub stars; no licence file; last pushed 2026-04-30. Counts drift over time.
- The licence is unresolved. GitHub reports no licence and no LICENSE file ships in the tree, although the README footer claims MIT. Treat reuse as uncertain until the maintainer clarifies.
- The repository has no description on GitHub, so the pack is defined only by its README and skill files.
- The pack is small: the highest install count is 82, and install counts fall off quickly from there. It is broad but lightly adopted.
- The repo has been quiet since 2026-04-30, while TikTok, Reels and Shorts specs change often, so format and safe-zone guidance may have drifted from current platform rules.
- 37 SKILL.md files back 34 indexed listings; the three internal meta-skills (skill-builder, skill-reviewer, voice-reviewer) are in-tree but not part of the indexed creator-marketing set.

## Related

- [Social Media Marketing - Agent-Driven Social Strategy](/hermes/skills/catalog/social-media-marketing-setup)
- [AI Marketing Skills - 24-Skill Operator Toolkit](/hermes/skills/catalog/ai-marketing-claude-code-skills-setup)
- [marketingskills - Complete Marketing Suite (160K+ installs)](/hermes/skills/catalog/marketingskills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run brand-context before anything else. It builds the shared context file the other 33 skills read, so the agent only learns your brand once instead of re-asking per task.
- Drive the pack with plain language, not skill names. The README maps phrases like "write outreach DMs" and "is this audience a fit" to the right skill automatically.
- Check FTC disclosure on every sponsored post before it ships. ftc-disclosure-spot-checker is cheap to run and catches a compliance miss before the creator publishes.
- Confirm a skill's current-tree path before scripting around it. The repo has been quiet since April 2026, so treat the file layout as authoritative over the README.
- Set up a UTM convention early. utm-parameter-builder keeps attribution consistent across creators, and retrofitting tracking URLs after a campaign is messy.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
