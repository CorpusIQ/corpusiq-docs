---
title: "LinkedIn Skills - 13-Skill Content Engine Setup"
description: "sergebulaev/linkedin-skills: 3.8K combined installs across 13 listings, a content engine for drafting, humanizing and publishing LinkedIn content."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sergebulaev-linkedin-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "linkedin", "social media", "content marketing"]
---

# LinkedIn Skills - Setup Guide

**Source:** [sergebulaev/linkedin-skills](https://www.skills.sh/sergebulaev/linkedin-skills) via skills.sh - 3.8K combined installs across 13 indexed listings; first seen Nov 13, 2026 (evening sweep)
**GitHub:** 5,905 stars, MIT license, `main` branch, last pushed 2026-11-10, 26 `SKILL.md` files across a `skills/` tree and a `.codex-marketplace/` mirror
**Category:** LinkedIn content marketing, posting and engagement workflows
**Quality Tier:** 🟡 Yellow - a thorough README and 13 indexed listings, but the largest listing has no resolved SKILL.md path and carries two Warn verdicts in the security sample.

This is a LinkedIn content engine from Creative Content Crafts. Twelve skills write posts, comments and replies, plan a week of content, audit a profile, strip AI tells from drafts, monitor comment threads and run a team advocacy program. Every skill drafts first and stops, and nothing publishes until you approve it or paste it yourself.

The repo ships 13 indexed listings but 26 `SKILL.md` files, because a `.codex-marketplace/` mirror duplicates the skill set. The `linkedin-marketing` listing, the largest at 1,996 installs, has no resolved SKILL.md path in the tree snapshot, so this guide does not describe what it contains.

## Installation

```bash
# Install every skill in the bundle
npx skills add sergebulaev/linkedin-skills

# Or install as a Codex plugin
codex plugin marketplace add sergebulaev/linkedin-skills
codex plugin add linkedin-skills@linkedin-skills

# Or clone into the Hermes skills folder
git clone https://github.com/sergebulaev/linkedin-skills.git ~/.hermes/skills/linkedin-skills
```

For Claude Code the README gives the slash-command form:

```
/plugin marketplace add sergebulaev/linkedin-skills
/plugin install linkedin-skills@linkedin-skills
```

Skills activate on matching prompts. Optional layers are opt-in: Apify reads post bodies, comments and engagers, and Publora publishes directly (free tier 15 posts per month). `python3 scripts/selftest.py` reports which layers are connected.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| linkedin-marketing | 1,996 | No resolved SKILL.md path in the tree snapshot; not described in the pack. |
| linkedin-post-writer | 173 | Draft a LinkedIn post from 20 2026 hook formulas plus a founders angle library, then humanize and schedule via Publora on approval. |
| linkedin-profile-optimizer | 169 | Audit and rewrite a LinkedIn profile end to end: headline, About, Featured, banner, photo, Experience, Skills, URL and recommendations. |
| linkedin-content-planner | 163 | Generate a 7-day LinkedIn content plan from a theme, audience and pillars, with per-day pillar, format, hook, CTA and comment targets. |
| linkedin-hook-extractor | 161 | Reverse-engineer the hook formula behind a viral LinkedIn post and return a blank template to reuse. |
| linkedin-humanizer | 157 | Remove AI tells from posts and comments, with a post auditor and a profile voice builder. |
| linkedin-comment-drafter | 155 | Draft a comment or a reshare on another post from its URL, in the user's voice, published via Publora on approval. |
| linkedin-reply-handler | 154 | Draft a reply to one comment, or sweep a whole thread and draft replies to every comment worth answering. |
| linkedin-thread-monitor | 147 | Track which of your comments earned author replies, flag warm threads in the 6-24h window and route them to reply-handler. |
| linkedin-engager-analytics | 146 | Pull likers and commenters on any post and segment them by ICP fit into an outbound action list. |
| linkedin-employee-advocacy | 145 | Stand up and run a team LinkedIn advocacy program: 14-day launch playbook, governance, cadence and ROI tracking. |
| linkedin-repurposer | 135 | Rebuild existing content from another platform into a native LinkedIn post, re-hooked and humanized. |
| linkedin-interviewer | 114 | Interview the user into a lasting Story Bank of roles, numbers and turning points that other skills draw on. |

No indexed listings fall below the 100-install threshold; all 13 appear in the table above.

## Why This Matters for Hermes Agents

LinkedIn posting is repetitive, and the drafting is the part most people outsource badly. These skills collapse the write-a-post loop into prompts: pick a hook, draft in your voice, strip the AI tells, then stop and wait for approval.

Two properties set the bundle apart. The approval card means nothing posts until a human says so, which is what makes the optional Publora publish path safe to hand an agent. The Apify read side turns posts and comment threads into structured data the agent can act on instead of asking you to paste everything.

The surrounding skills close the loop around a single post. The profile optimizer fixes the profile, the content planner schedules the week, and the thread monitor flags warm comment threads and routes them to the reply handler. An agent that keeps that cadence running turns LinkedIn from a chore into a pipeline.

## Usage

| You say | What happens |
|---|---|
| "Write me a LinkedIn post about why AI agencies are replacing traditional ones" | Runs linkedin-post-writer, picks a hook formula and drafts the post, then runs the humanizer. |
| "Comment on this post, I want to add a thoughtful take" | Runs linkedin-comment-drafter and returns 1-3 comment variants in your voice. |
| "Audit this draft for AI tells before I post it" | Runs linkedin-humanizer in audit mode and lists the AI tells. |
| "Create a 7-day content plan, I'm a B2B SaaS founder" | Runs linkedin-content-planner and returns per-day pillars, formats, hooks and CTAs. |
| "Optimize my LinkedIn profile for inbound leads" | Runs linkedin-profile-optimizer and rewrites headline, About and Experience. |
| "Which of my comment threads need follow-up?" | Runs linkedin-thread-monitor and routes warm threads to reply-handler. |
| "Who liked my last post and who should I message?" | Runs linkedin-engager-analytics and returns a segmented engager list. |

## Verification

Probe two skills on the branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/sergebulaev/linkedin-skills/main/skills/linkedin-post-writer/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/sergebulaev/linkedin-skills/main/skills/linkedin-interviewer/SKILL.md
```

Skills live at `skills/<name>/SKILL.md`, mirrored under `.codex-marketplace/linkedin-skills/skills/<name>/SKILL.md`. The `linkedin-marketing` listing has no resolvable path to probe.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| linkedin-marketing | Warn | Pass | Warn |
| linkedin-post-writer | Pass | Pass | Pass |
| linkedin-profile-optimizer | Pass | Pass | Pass |
| linkedin-content-planner | Pass | Pass | Pass |

`linkedin-marketing` carries the pack's only non-pass verdicts, a Warn from Gen Agent Trust Hub and a Warn from Snyk, with a Socket Pass. It is also the most-installed listing and the one with no resolved SKILL.md path, so there is no file to audit before you trust it. The other three sampled skills pass all three auditors. The remaining nine listings publish no verdict at all, which is not the same as a pass.

## Limitations

- Snapshot data, verified 2026-11-13: 3,815 combined installs across 13 indexed listings; 5,905 GitHub stars; MIT; last pushed 2026-11-10. Counts drift over time.
- The repo holds 13 indexed listings but 26 `SKILL.md` files, because a `.codex-marketplace/` mirror duplicates the skill set. The file count is not the skill count.
- The `linkedin-marketing` listing, the most installed at 1,996, has no resolved SKILL.md path in the tree snapshot. Neither this guide nor the pack describes what it contains.
- Five skills read LinkedIn data through Apify: comment drafter, reply handler, hook extractor, thread monitor and engager analytics (the README's "Engagement Monitor" covers the last two). Without an Apify token they fall back to asking you to paste the relevant text.
- Direct publishing needs a Publora account (free tier 15 posts per month). Without it, every skill drafts for you to paste, which is the default.
- The README documents 12 skills where the install index counts 13 listings, so a README table row and a directory do not always line up one-to-one.

## Related

- [Charlie Hills Social Media Skills - 17-Skill Content System](/hermes/skills/catalog/charlie-hills-social-media-skills-setup)
- [Social Media Marketing - Agent-Driven Social Strategy](/hermes/skills/catalog/social-media-marketing-setup)
- [Digital Marketing Pro - AI Marketing OS Setup](/hermes/skills/catalog/digital-marketing-pro-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `linkedin-post-writer` and `linkedin-humanizer`. The humanizer's audit mode tells you whether the agent writes in your voice before you hand it a week of posts.
- Run `python3 scripts/selftest.py` once after install. It reports which optional layers (Apify, Publora, Pixfaro) are connected and names what is missing.
- Keep the approval flow. The skills draft and wait by design, so do not wire Publora publishing into a schedule with no human in the loop.
- On claude.ai, use the Apify MCP connector with the `?actors=` filter rather than a token, so the agent sees only the four read actors and nothing that picks an actor on its own.
- On Windows, the `.claude/skills/` symlink mirror checks out as text files unless symlinks are enabled. Use directory junctions instead if you clone rather than install.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
