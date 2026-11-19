---
title: "Ootto Content Skills - Instagram Reels Factory Setup"
description: "ootto-ai/claude-content-skills: 7.0K combined installs across 55 listings; copy-paste Claude skills that run an Instagram content growth factory."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ootto-content-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "content marketing", "instagram reels", "short-form video"]
---

# Ootto Content Skills - Setup Guide

**Source:** [ootto-ai/claude-content-skills](https://www.skills.sh/ootto-ai/claude-content-skills) via skills.sh - 7.0K combined installs across 55 indexed listings; first seen Nov 18, 2026 (Nov 18, 2026 evening sweep)
**GitHub:** 514 stars, MIT licence, `main` branch, last pushed 2026-11-07. The 55 skills live as one `SKILL.md` per directory under `skills/`, plus a Claude Code plugin manifest under `.claude-plugin/`.
**Category:** Instagram content marketing and short-form video
**Quality Tier:** 🟡 Yellow - 3 Warns among 12 sampled skills (reel-analyzer, hook-mining, cover-thumbnail-brief); MIT licence.

Ootto Content Skills is a free, copy-paste suite of 55 Claude skills from Ootto that run an Instagram content growth factory. Each skill is a plain prompt you can paste into claude.ai or install as a Claude Code plugin, and each does one job in a pipeline: study a viral reel, write the hook, script the reel, build the shot list, write the caption, and turn comments into leads.

The set is arranged as a factory. Content Factory runs the whole pipeline in order, AI Brain gives Claude persistent memory in a local Obsidian vault, and the remaining skills each handle one step, from Virality (the hook strategy) through Reel Analyzer, Viral Hook Writer, Reel Scripter, and Reel Builder to Caption & Hashtags and Comment Responder.

## Installation

The README offers three ways to install. As a Claude Code plugin, since the repo doubles as a plugin marketplace:

```bash
/plugin marketplace add Ootto-AI/claude-content-skills
/plugin install claude-content-skills@ootto-content-skills
```

Manually on macOS or Linux:

```bash
git clone --depth 1 https://github.com/Ootto-AI/claude-content-skills.git
bash claude-content-skills/install.sh
```

Both copy the skills into `~/.claude/skills/`. With no Claude Code, every skill file is a plain prompt: open it on GitHub, copy it, and paste it into claude.ai.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| reel-analyzer | 157 | Feed any viral reel (a link or file) and Claude studies it frame by frame plus the transcript, then breaks down the hook, beat structure, pacing, and on-screen visuals so you can model what works. |
| reel-scripter | 156 | Turn an idea or hook into a full 30-45 second reel script: hook, value beats, payoff, and CTA, with on-screen text. |
| viral-hook-writer | 153 | Write scroll-stopping hooks for the first 1-3 seconds of a short-form video, ranked for what to test first. |

The remaining 52 indexed listings range from 45 to 149 installs.

## Why This Matters for Hermes Agents

For an agent producing short-form video content, the default output is generic: hooks that sound like every other reel, scripts with no structure, and captions stuffed with irrelevant tags. These skills replace that with a pipeline built from real results, including the Virality skill distilled from 262 posts and 3.5M views on a working account.

Because each skill is a single self-contained prompt, they compose well in any harness that loads skill files, including Hermes, even though the one-line installers target Claude Code. The factory pattern matters: one skill drives the others in order, so an agent can run idea to finished reel and the lead loop from a single request, then compound by saving winners back into memory.

The skills also encode rules that resist AI slop, such as front-loading the hook, modelling the format rather than copying the words, and keeping the public reply link-free with the link going to the DM instead.

## Usage

| You say | What happens |
|---|---|
| "Analyze this viral reel" | reel-analyzer studies it frame by frame and returns the hook, beat structure, pacing, and visual breakdown. |
| "Write me a hook for this idea" | viral-hook-writer returns scroll-stopping openings for the first few seconds, ranked. |
| "Turn this idea into a full reel script" | reel-scripter writes a 30-45 second script with value beats, payoff, and CTA. |
| "Run my whole content pipeline" | content-factory drives the full flow from idea to finished reel plus the lead loop. |
| "Save this session to my vault" | ai-brain writes a markdown note to your Obsidian vault and recalls relevant notes next session. |
| "Turn my comments into leads" | comment-responder drafts a warm public reply plus a DM with the resource. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/ootto-ai/claude-content-skills/main/skills/reel-analyzer/SKILL.md
```

Then install the whole set as a plugin or copy a single skill:

```bash
/plugin marketplace add Ootto-AI/claude-content-skills
/plugin install claude-content-skills@ootto-content-skills
```

After install, ask your agent to analyze a reel or write a hook and check the next response changes.

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| reel-analyzer | Pass | Pass | Warn |
| reel-scripter | Pass | Pass | Pass |
| viral-hook-writer | Pass | Pass | Pass |
| virality | Pass | Pass | Pass |
| caption-and-hashtags | Pass | Pass | Pass |
| reel-builder | Pass | Pass | Pass |
| going-viral | Pass | Pass | Pass |
| on-screen-text-writer | Pass | Pass | Pass |
| hook-mining | Pass | Pass | Warn |
| b-roll-shot-list | Pass | Pass | Pass |
| cover-thumbnail-brief | Pass | Pass | Warn |
| carousel-builder | Pass | Pass | Pass |

The sample covers 12 of the 55 indexed listings; every Gen Agent Trust Hub and Socket cell passes, with three Snyk Warns.

## Limitations

- Snapshot data, verified Nov 18, 2026: 6,986 combined installs across 55 indexed listings; 514 GitHub stars; MIT licence; last pushed 2026-11-07. Counts drift over time.
- The three skills shown above carry the top of the install volume; the other 52 indexed listings sit between 45 and 149 installs and are long-tail.
- Two skills are bundled from other repos: Agent Reach (from Panniantong/Agent-Reach) and Humanizer (from blader/humanizer), both MIT.
- The AI Brain memory loop is built around an Obsidian vault plus the Filesystem connector; without those, the recall step does not run.
- The one-line installers target Claude Code; elsewhere you copy individual `SKILL.md` prompts into your agent's skills directory.

## Related

- [Marketing Skills - Content Ops Setup](/hermes/skills/catalog/zc277584121-marketing-skills-setup)
- [Content Strategy - Full Planning Framework Setup](/hermes/skills/catalog/content-strategy-setup)
- [Kostja94 Marketing Skills - Copywriting, SEO, Ads Setup](/hermes/skills/catalog/kostja94-marketing-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with content-factory to see the whole pipeline, then run individual skills once you know the flow.
- Give reel-analyzer the actual video as a link or file; it needs the real thing to break down, not a description.
- Feed hook-mining a CSV of hooks that actually performed; it remixes proven structure rather than inventing from nothing.
- Run humanizer over every script and caption before posting to strip AI-sounding tells.
- Install a single skill by copying its SKILL.md, or pull the whole set with the plugin marketplace.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
