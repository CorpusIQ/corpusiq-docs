---
title: "Newsjack Skills - Setup Guide"
description: "elvisun/newsjack: open-source PR skills that turn an agent into a full PR team, from newsjacking to pitch drafting - 16.1K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/newsjack-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "public relations", "newsjacking", "media outreach", "journalism"]
---

# Newsjack Skills - Setup Guide

**Source:** [elvisun/newsjack](https://www.skills.sh/elvisun/newsjack) via skills.sh - 16.1K combined installs across 34 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 morning sweep)
**GitHub:** [elvisun/newsjack](https://github.com/elvisun/newsjack) - 1,702 stars, MIT licence, main branch, last pushed Nov 19, 2026. Skills live under `skills/<name>/SKILL.md`, mirrored under `plugins/newsjack/skills/<name>/SKILL.md`.
**Category:** Public Relations
**Quality Tier:** 🟡 Yellow - 9 Warn among 20 sampled verdicts (Snyk: news-search, story-origin-check, newsworthiness-check, journalist-fit-check, find-journalists, newsjack-detector, coverage-tracker, reactive-comment, pr-calendar); MIT licence.

Newsjack is a suite of open skills plus a small open-source CLI that turns an agent into a full PR team. The README frames four lanes: Detect (surface newsjacking opportunities and monitor coverage), Act (turn signal into angles, headlines, pitches and clips), Strategize (positioning, PR calendar and newsworthiness), and AI visibility (get facts into AI answers). Skills are plain-Markdown instructions that run anywhere the agent runs; a few reach for a live news index, journalist enrichment or locally saved monitoring state, so those work best in a local agent.

The suite is MIT licensed, actively maintained, and installs with one command plus a CLI on PATH. All 34 indexed listings map to a SKILL.md in the repository, mirrored under both `skills/<name>/` and `plugins/newsjack/skills/<name>/`.

## Installation

One line on macOS or Linux (review install.sh first if you like):

```bash
curl -fsSL newsjack.sh | bash
```

This installs the CLI at `~/.newsjack/bin/newsjack` plus the managed skill bundle, and drops skills into your detected runtime(s). Curl-installed Newsjack auto-updates from the latest GitHub Release before each run; set `NEWSJACK_AUTO_UPDATE=0` to disable. To install only the CLI:

```bash
npm i -g newsjack@latest
```

For Claude.ai and Cowork, install the Newsjack plugin: open Customize, go to Personal plugins, choose Create plugin, then Add marketplace, then Add from a repository, enter `elvisun/newsjack`, and install the `newsjack@newsjack` plugin. To unlock the skills that need an external connection (live news search, PR calendar lookup, journalist enrichment, media list research), connect a Medialyst account; in local agent harnesses run `newsjack login` and approve the printed link. For project setup in a local Claude Code plugin install, check `newsjack auth status` and run `newsjack login` if project tools are not enabled.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| fact-check | 829 | Extract claims, verify each, flag the shaky ones before you send |
| headline-generator | 786 | Headlines and pitch subject lines built from the story's raw facts |
| news-search | 774 | Dated, attributed articles on a topic, company or competitor |
| angle-generator | 771 | Turn one update into hooks framed for different beats |
| voice-extractor | 768 | Fingerprint your real writing and kill the AI tells |
| story-origin-check | 764 | Verify a story is still fresh: who broke it and what oxygen is left |
| crisis-holding | 764 | Holding statements and journalist Q&A with a hard legal-counsel gate |
| newsworthiness-check | 763 | Cold read on whether a story clears the bar before you act |
| meanest-editor | 763 | Roast your pitch against the rubric editors actually use |
| pr-strategist | 761 | Opinionated walkthrough: audience, positioning, news pegs, drumbeat |
| journalist-fit-check | 761 | Will this reporter actually care, or are you spamming |
| find-journalists | 761 | Build a fit-checked media list, optionally via Medialyst |
| newsjack-triage | 760 | Route surviving stories by whether you actually have standing |
| newsjack-detector | 760 | Find newsjacking opportunities before the wave breaks |
| relevance-coarse-filter | 759 | Cheap high-recall first pass that throws out obvious junk |
| coverage-tracker | 759 | Google Alerts-style keyword tracking, alerting only on new coverage |
| newsjack-monitor-setup | 758 | Build the monitoring profile: standing, topics, competitors, feeds |
| coverage-tracker-setup | 758 | Declare the keywords to watch and what each one means |
| reactive-comment | 757 | Triage inbound HARO-style source requests, draft only real fits |
| pr-calendar | 703 | Plan six months of source-backed hooks with prior-year patterns |
| press-clip | 702 | Turn a live article URL into a branded press-clip PDF |

The remaining 13 indexed listings range from 1 to 14 installs (ai-visibility-writing 14; prompt-proximity-architecture and buyer-job-intent-analysis 12 each; coverage-reel 8; citation-foodchain 2; transcript-to-stories and quote-forecast 1 each).

## Why This Matters for Hermes Agents

PR and media outreach is high-stakes, low-repetition work where a generic model's defaults do real damage: it fabricates claims, sprays the whole masthead, and writes in the tell-tale voice editors flag as AI slop. Newsjack is a complete pipeline for exactly that problem, from finding the news hook through the pitch that lands. The Detect lane runs the news cycle for the agent: monitor, filter, verify freshness, and decide standing before effort is spent. The Act lane turns signal into journalist-shaped output, fact-checked copy, and a voice fingerprint that removes the machine tells. The AI visibility lane extends the same discipline to AEO and GEO so facts survive into AI answers without invented evidence. Because the suite is plain Markdown plus a small MIT-licensed CLI, it installs anywhere a Hermes agent runs, and the setup and monitoring skills persist state locally so scheduled monitoring keeps working between sessions.

## Usage

| You say | What happens |
|---|---|
| Set up daily newsjacking monitoring for my company | newsjack-monitor-setup builds the profile, then newsjack-detector runs on schedule and reports opportunities |
| Turn this funding announcement into story angles | angle-generator produces 3-7 journalist-shaped angles and headline-generator drafts subject lines |
| Find journalists who cover enterprise AI | find-journalists builds a fit-checked media list, optionally through Medialyst |
| Fact-check this press release before we send it | fact-check extracts each claim, verifies it and flags the shaky ones |
| Is this news actually worth pitching? | newsworthiness-check cold-reads it against calibrated anchors and anti-inflation rules |
| Roast my pitch before I send it | meanest-editor critiques it against the rubric editors actually use |
| Turn this article into a press clip | press-clip renders a branded PDF keeping the outlet's layout and highlighting the mention |

## Verification

```bash
# after install, confirm the skills landed
ls ~/.newsjack/newsjack/
# review one skill before relying on it
curl -sL https://raw.githubusercontent.com/elvisun/newsjack/main/skills/fact-check/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| fact-check | Pass | Pass | Pass |
| headline-generator | Pass | Pass | Pass |
| news-search | Pass | Pass | Warn |
| angle-generator | Pass | Pass | Pass |
| voice-extractor | Pass | Pass | Pass |
| story-origin-check | Pass | Pass | Warn |
| crisis-holding | Pass | Pass | Pass |
| newsworthiness-check | Pass | Pass | Warn |
| meanest-editor | Pass | Pass | Pass |
| pr-strategist | Pass | Pass | Pass |
| journalist-fit-check | Pass | Pass | Warn |
| find-journalists | Pass | Pass | Warn |
| newsjack-triage | Pass | Pass | Pass |
| newsjack-detector | Pass | Pass | Warn |
| relevance-coarse-filter | Pass | Pass | Pass |
| coverage-tracker | Pass | Pass | Warn |
| newsjack-monitor-setup | Pass | Pass | Pass |
| coverage-tracker-setup | Pass | Pass | Pass |
| reactive-comment | Pass | Pass | Warn |
| pr-calendar | Pass | Pass | Warn |

## Limitations

- Snapshot data, verified Nov 20, 2026: 16,097 combined installs across 34 indexed listings; 1,702 GitHub stars; MIT licence; last pushed Nov 19, 2026. Counts drift over time.
- press-clip and coverage-reel need a local agent: press-clip drives a real Chrome/Edge browser via Playwright, and coverage-reel renders its video in that same browser, so chat apps cannot run those workflows. The two setup skills (newsjack-monitor-setup, coverage-tracker-setup) only save and schedule, so they also need a local agent.
- news-search, find-journalists and pr-calendar do their best work with the Medialyst API connected (newsjack login); without it they fall back to host search or best-effort local lists. Consumer ChatGPT runs the suite only in a degraded one-shot form because skills are unavailable on consumer accounts.
- Only 20 of the 34 indexed listings carry skills.sh security verdicts; the other 14 are unverified on that platform.
- Curl-installed Newsjack auto-updates from the latest GitHub Release before each run, so behavior can change without a manual upgrade; set NEWSJACK_AUTO_UPDATE=0 to pin it.

## Related

- [Journalism Agent Skills - Media Workflows Setup](/hermes/skills/catalog/claude-skills-journalism-setup)
- [News Aggregator Skill - Multi-Source News Digest](/hermes/skills/catalog/news-aggregator-skill-setup)
- [SEO GEO Claude Skills - SEO & Generative Engine Optimization Suite Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup)
- [Marketing Skills - Content Ops Setup](/hermes/skills/catalog/zc277584121-marketing-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with newsjack-monitor-setup and coverage-tracker-setup once, then let newsjack-detector and coverage-tracker run on schedule; the setup skills persist state locally.
- Run fact-check before any journalist-facing draft is sent, and voice-extractor before the first pitch so the AI tells are removed from day one.
- Use relevance-coarse-filter as the cheap first pass before story-origin-check so expensive research only runs on surviving stories.
- Connect Medialyst (newsjack login) to unlock live news search, the PR calendar and approval-gated media list research.
- Prefer a local agent for press-clip and coverage-reel; chat apps cannot drive the Playwright browser those skills require.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
