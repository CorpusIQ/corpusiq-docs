---
title: "Giulioco Skills - Social Growth and Sales Setup"
description: "giulioco/skills: 2.1K combined installs across 8 listings, a curated Claude Code skill set for viral social growth, image prompts and sales coaching."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/giulioco-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "social media", "sales", "growth"]
---

# Giulioco Skills - Setup Guide

**Source:** [giulioco/skills](https://www.skills.sh/giulioco/skills) via skills.sh - 2.1K combined installs across 8 indexed listings; first seen Nov 13, 2026 (evening sweep)
**GitHub:** 11 stars, Apache-2.0 license, `master` branch, last pushed 2026-07-02, 8 `SKILL.md` files in `skills/<name>/SKILL.md` folders
**Category:** Social media growth, sales coaching and image-prompting workflows
**Quality Tier:** 🟡 Yellow - 8 in-tree skills, a detailed README and four clean verdicts, but a small install base and little recent activity.

Giulio's collection ships eight Claude Code skills aimed at marketers and founders: a TikTok and Instagram short-form video growth coach, a viral app growth playbook, sales and growth-hacker coaches drawn from six and three foundational books respectively, a Scott Galloway storytelling rewriter, an image prompt engineer, a Codex image generator and a book-grounded skill builder.

The flagship is `postbridge-social-growth`, a growth coach built on the Post Bridge methodology (500M+ views, 132K+ downloads, $33K+ revenue, zero paid ads). It holds 1,498 of the 2,121 combined installs; nano-banana-prompt and social-growth-engineer follow in the hundreds, and the remaining five listings range from 13 to 34 installs.

## Installation

```bash
# Install all skills
npx add-skill giulioco/skills

# List available skills first
npx add-skill giulioco/skills --list

# Install a single skill
npx add-skill giulioco/skills --skill social-growth-engineer
```

The tool installs into `~/.claude/skills/`. There is also a global flag (`npx add-skill -g giulioco/skills`) and a non-interactive `-y` mode. Invoke a skill manually with `/social-growth-engineer`, or let Claude activate it from the question.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| postbridge-social-growth | 1,498 | Organic growth coach for TikTok and Instagram short-form video using the Post Bridge methodology. |
| nano-banana-prompt | 285 | Craft prompts for Nano Banana Pro (Gemini) image generation: portraits, product shots, mockups, era aesthetics. |
| social-growth-engineer | 238 | Viral app growth playbook from 100+ case studies: hooks, UGC networks, formats, monetization and scaling. |

The remaining 5 indexed listings range from 13 to 34 installs.

## Why This Matters for Hermes Agents

The core of this collection is a set of coaches, not tools. `ultimate-sales`, `growth-hacker` and `social-growth-engineer` each condense a stack of books into a diagnose-first loop: the agent works out where you are before it prescribes a move. That makes them useful to an agent that needs judgment, not just a template.

The growth skills are grounded in quantified claims: the Post Bridge methodology's 500M+ views and the social-growth-engineer's 100+ case studies with verified revenue ranges. For a builder planning a consumer app launch, that is the difference between generic advice and a playbook with benchmarks.

Two skills extend the agent's own output. `nano-banana-prompt` and `codex-imagegen` make image generation concrete, and `galloway-storytelling` is a reusable writing sharpener that names the move it applied, so a Hermes agent can rewrite a flat draft and explain what changed.

`learn-craft` is the meta-skill: it researches the canonical books on any subject and synthesizes them into a new SKILL.md, so the collection can grow itself.

## Usage

| You say | What happens |
|---|---|
| "How do I grow my app virally?" | Activates social-growth-engineer and returns hooks, formats and a scaling plan. |
| "Help me launch my TikTok account from zero in 30 days" | Activates postbridge-social-growth and returns the 30-day roadmap with an account warmup protocol. |
| "Draft a cold email for this prospect" | Activates ultimate-sales and returns a diagnose-first draft plus a follow-up sequence. |
| "We're stuck at a revenue plateau, what channel next?" | Activates growth-hacker and diagnoses the stage before prescribing a channel. |
| "Generate a photorealistic product shot of this watch" | Activates nano-banana-prompt and returns a Nano Banana Pro prompt. |
| "Rewrite this newsletter intro so it hits harder" | Activates galloway-storytelling and returns the rewrite plus which moves it applied. |
| "Create a skill for mastering negotiation" | Activates learn-craft and synthesizes the canonical books into a SKILL.md. |

## Verification

Probe two skills on the branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/giulioco/skills/master/skills/postbridge-social-growth/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/giulioco/skills/master/skills/social-growth-engineer/SKILL.md
```

Skills live at `skills/<name>/SKILL.md` on the `master` branch, not `main`. A raw URL pointed at `main` returns 404.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| postbridge-social-growth | Pass | Pass | Pass |
| nano-banana-prompt | Pass | Pass | Pass |
| social-growth-engineer | Pass | Pass | Pass |
| codex-imagegen | Pass | Pass | Pass |

All four sampled skills pass all three auditors. That is a clean result, but it covers only half the pack: the other four listings publish no verdict, which is not the same as a pass. The repo carries 2 Python files; the one the README names is `learn-craft`'s `libgen.py` downloader, which fetches book PDFs, so read that file before you let the skill reach the network.

## Limitations

- Snapshot data, verified 2026-11-13: 2,121 combined installs across 8 indexed listings; 11 GitHub stars; Apache-2.0; last pushed 2026-07-02. Counts drift over time.
- The default branch is `master`, not `main`. Keep that in every raw URL; a `main` URL returns 404.
- Install counts are concentrated in one skill: `postbridge-social-growth` holds 1,498 of the 2,121 combined installs.
- `learn-craft` bundles a `libgen.py` downloader that fetches book PDFs. That is a network-capable script inside an otherwise markdown-heavy repo.
- The repo has not been pushed since 2026-07-02, so the skills have not tracked 2026 platform changes. Treat the TikTok and Instagram specifics as a snapshot, not current playbooks.
- The README's roadmap lists data-analyst, design-system, devops-expert and technical-writer as coming soon. Those do not exist in the tree yet.

## Related

- [Apidojo Social Media Skills - 3-Skill Scraper Suite Setup](/hermes/skills/catalog/apidojo-social-media-skills-setup)
- [Social Media Marketing - Agent-Driven Social Strategy](/hermes/skills/catalog/social-media-marketing-setup)
- [Charlie Hills Social Media Skills - 17-Skill Content System](/hermes/skills/catalog/charlie-hills-social-media-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `postbridge-social-growth`. It is the most-installed skill and the smallest in file size, so it is quick to read and quick to trust.
- Use `social-growth-engineer` for strategy and `postbridge-social-growth` for execution. The former is the case-study playbook, the latter the day-to-day coach.
- Run `learn-craft` on a subject you actually need. It downloads the canonical books, so point it at a topic you would read about anyway.
- Pair `galloway-storytelling` with any drafting skill. Its output names the move it applied, which is the cheapest way to learn the craft while you get the edit.
- Do not expect the roadmap skills yet. data-analyst, design-system, devops-expert and technical-writer are listed as coming soon and are not in the tree.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
