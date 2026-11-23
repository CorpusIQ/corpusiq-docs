---
title: "HumanizerAI - AI Detection and Humanization Skills Setup"
description: "humanizerai/agent-skills: AI detection and text humanization skills for Claude Code and Codex - 7.3K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/humanizerai-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "ai detection", "humanization", "writing"]
---

# HumanizerAI - AI Detection and Humanization Skills Setup

**Source:** [humanizerai/agent-skills](https://www.skills.sh/humanizerai/agent-skills) via skills.sh - 7.3K combined installs across 7 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 morning sweep)
**GitHub:** [humanizerai/agent-skills](https://github.com/humanizerai/agent-skills) - 58 stars, MIT license, main branch, last pushed Feb 5, 2026; six skills under skills/<name>/SKILL.md plus detect-ai stubs in per-agent directories (.agents, .claude, .codex, .cursor, .gemini and .opencode).
**Category:** AI Content Detection and Humanization
**Quality Tier:** 🟡 Yellow - no Fail cells and 1 Warn cell across the 7-skill sample: Snyk Warns on humanizerai.

HumanizerAI ships a small set of agent skills for detecting AI-written text and rewriting it into natural prose, aimed at Claude Code, Cursor and other AI coding assistants. The two headline skills are detect-ai, which scores text 0-100 for AI authorship, and humanize, which rewrites text to pass detectors such as GPTZero, Turnitin and Originality.ai.

Four supporting skills round out the suite: cold-email and follow-up write outreach with proven frameworks, readability reports Flesch-Kincaid and other readability metrics, and word-stats returns quick text statistics. The humanize skill is credit-based at one credit per word and needs a HumanizerAI API key plus a paid Pro or Business plan; detection is free.

## Installation

Install the whole suite through the skills CLI:

```bash
npx skills add humanizerai/agent-skills
```

Manual install for the two headline skills, if you only need the core pair:

```bash
git clone https://github.com/humanizerai/agent-skills.git
cp -r agent-skills/skills/detect-ai .claude/skills/
cp -r agent-skills/skills/humanize .claude/skills/
```

Then set the API key before using the humanize skill:

```bash
export HUMANIZERAI_API_KEY="hum_your_api_key_here"
```

Detection is always free and unlimited; humanization spends one credit per word.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| humanize | 4,149 | rewriting AI text into natural prose that passes GPTZero, Turnitin and Originality.ai (credit-based) |
| detect-ai | 1,016 | scoring text 0-100 for AI authorship with detailed metrics |
| readability | 599 | scoring readability with Flesch-Kincaid, Gunning Fog and SMOG metrics |
| follow-up | 524 | writing follow-up emails that re-engage without being annoying |
| cold-email | 524 | writing cold emails with AIDA, PAS and BAB frameworks and a 50-125 word limit |
| word-stats | 519 | word count, character count, reading time and text statistics |

The remaining 1 indexed listing is humanizerai (3 installs), the umbrella package name with no matching skill directory in the current tree.

## Why This Matters for Hermes Agents

An agent that drafts copy for publishing has no way to know whether its output reads as machine-written, and stock models lean on the same constructions that detectors flag. detect-ai gives a concrete 0-100 score with metrics, so a builder can screen content before it ships, and humanize rewrites flagged passages toward natural prose. The workflow the README recommends is a loop: score, humanize, re-score, until the output clears the bar. The outreach pair matters for any agent that sends email, enforcing a 50-125 word limit and proven frameworks instead of rambling drafts, and readability and word-stats are the low-cost checks to run on anything public. The main constraint is cost and setup: humanization is credit-based and needs an API key and a paid plan, so treat it as a paid capability while detection and the outreach skills are free.

## Usage

| You say | What happens |
|---|---|
| Check this text for AI | Runs detect-ai and returns a 0-100 score with detailed metrics |
| Make this AI text sound human | Runs humanize to rewrite it, spending one credit per word |
| Humanize this aggressively | Runs humanize with the aggressive intensity level for maximum bypass |
| How readable is this draft? | Runs readability and returns Flesch-Kincaid, Gunning Fog and SMOG scores |
| Write a cold email to this prospect | Runs cold-email with AIDA, PAS or BAB and a 50-125 word limit |
| Follow up on my last email | Runs follow-up with a re-engage sequence |

## Verification

Confirm the headline skills resolve on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/humanizerai/agent-skills/main/skills/humanize/SKILL.md | head -30
```

```bash
curl -sL https://raw.githubusercontent.com/humanizerai/agent-skills/main/skills/detect-ai/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| humanize | Pass | Pass | Pass |
| detect-ai | Pass | Pass | Pass |
| readability | Pass | Pass | Pass |
| follow-up | Pass | Pass | Pass |
| cold-email | Pass | Pass | Pass |
| word-stats | Pass | Pass | Pass |
| humanizerai | Pass | Pass | Warn |

The sample is nearly clean - the only non-Pass cell is a Snyk Warn on the humanizerai umbrella listing - and all 7 indexed listings carry a published verdict.

## Limitations

- Snapshot data, verified Nov 23, 2026: 7,334 combined installs across 7 indexed listings; 58 GitHub stars; MIT license; last pushed Feb 5, 2026. Counts drift over time.
- The humanizerai listing (3 installs) is the umbrella package name and has no matching skill directory in the current tree.
- Humanization requires a HumanizerAI account with a paid Pro or Business plan and an API key, and it is credit-based at one credit per word.
- The index and tree carry detect-ai in several per-agent directories (.agents, .claude, .codex, .cursor, .gemini, .opencode), but only the skills/detect-ai and .agents copies include a SKILL.md.
- The repository was last pushed Feb 5, 2026, well before the snapshot date, so it has been quiet for months.

## Related

- [Humanizer - Anti-AI-Slop Text Humanizer Setup Guide](/hermes/skills/catalog/humanizer-setup)
- [Ultimate Humanizer - Anti-AI-Slop Skill Setup Guide](/hermes/skills/catalog/ultimate-humanizer-setup)
- [Avoid AI Writing - AI-Pattern Audit & Rewrite Setup](/hermes/skills/catalog/avoid-ai-writing-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run detect-ai before publishing anything, then humanize and re-score to confirm the rewrite actually moved the score.
- Detection is free and unlimited; humanization is the paid part, so only spend credits on text that fails the score.
- Set HUMANIZERAI_API_KEY in your shell profile before invoking the humanize skill, or it will not authenticate.
- Choose the intensity level deliberately: light preserves voice, medium is the default, and aggressive is for strict detectors.
- Install the whole suite with npx skills add humanizerai/agent-skills, or copy just detect-ai and humanize manually if you only need the core pair.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
