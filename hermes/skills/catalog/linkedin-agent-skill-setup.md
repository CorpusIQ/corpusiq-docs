---
title: "LinkedIn Agent Skills - Run a LinkedIn Account"
description: "jakeschincariol/linkedin-agent-skill - 4.1K combined installs across 11 indexed listings: eleven skills to write, plan, and humanize LinkedIn posts."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/linkedin-agent-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "linkedin", "social content"]
---

# LinkedIn Agent Skills - Setup Guide

**Source:** [jakeschincariol/linkedin-agent-skill](https://www.skills.sh/jakeschincariol/linkedin-agent-skill) via skills.sh - 4.1K combined installs across 11 indexed listings; first seen Nov 16, 2026 (Nov 16 evening sweep)
**GitHub:** 3,651 stars, MIT license, `main` branch, last pushed 2026-09-17, eleven skills under `skills/li-*/SKILL.md` plus `templates/voice.md`
**Category:** Social content - LinkedIn posts, comments, replies, profile, and weekly planning
**Quality Tier:** 🟢 Green - all 11 sampled skills pass the Gen Agent Trust Hub, Socket, and Snyk.

Eleven free Claude skills run a LinkedIn account end to end, with no signup, no API key, and nothing to connect. One writes posts off 21 hook formulas, one comments on other people's posts, one handles the replies under yours, one scores a profile out of 100 against a 12-part rubric, and one plans the week: what to post, when, and who to engage with.

The humanizer is what makes the rest usable: it strips the machine fingerprint out of any draft (em dashes, slop vocabulary, invisible watermark characters) and scores what is left against a five-check detection panel before anything is shown. Nothing gets posted until you say yes; the skills write, you post.

## Installation

With the skills CLI:

```sh
npx skills add jakeschincariol/linkedin-agent-skill
```

Or by hand, as the README suggests:

```bash
git clone https://github.com/Jakeschincariol/linkedin-agent-skill.git
cp -r linkedin-agent-skill/skills/li-* ~/.claude/skills/
```

Or as a plugin: `/plugin marketplace add Jakeschincariol/linkedin-agent-skill` then `/plugin install linkedin-agent`. Then spend ten minutes on `templates/voice.md`: copy it to `~/.claude/linkedin/voice.md` and fill it in, or paste three of your own posts and ask Claude to write it. Every skill reads that file, and skipping it flattens the account's voice.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| li-profile | 384 | Score a profile out of 100 against a 12-part rubric and rewrite the parts that lose points. |
| li-post | 381 | Write a post from a raw idea using 21 hook formulas, humanized before you see it. |
| li-human | 379 | Strip the machine fingerprint from any draft and score it against a five-check detection panel. |
| li-plan | 368 | Build the week: what to post, when, and who to engage with. |
| li-comment | 368 | Write comments on other people's posts that read as a person with an opinion. |
| li-reply | 367 | Draft answers to the comments under your own posts, sorted by which are worth answering. |
| li-carousel | 367 | Build a document post (carousel) with slide-by-slide copy and a PDF to upload. |
| li-audit | 366 | Post-mortem on what already published: which posts worked, why, and what to stop. |
| li-dm | 365 | Write connection notes and DM follow-ups: the invite, first message, and two follow-ups. |
| li-repurpose | 364 | Turn one long asset into a week of standalone LinkedIn posts. |
| li-inbox | 357 | Triage the inbox into leads, recruiters, peers and spam, and draft the replies worth sending. |

All 11 indexed listings appear in the table above; none sits below 300 installs.

## Why This Matters for Hermes Agents

The eleven skills cover a whole account without any API integration, and that is the point: no skill posts to LinkedIn. Every skill ends in a copy-ready block and an explicit approval gate, because automating a personal profile violates the platform's User Agreement and gets accounts restricted. The humanizer is the differentiator for builders: two dependency-free Python scripts run locally on the user's text and return a 0-100 score weighted 60% on the mean and 40% on the weakest single check, since a detector needs only one signal to fire. The five checks (burstiness, specificity, slop density, fingerprint, voice) are local heuristics modeled on public detectors, not calls to GPTZero or similar services. Nothing fabricates: a draft that needs a number the user has not given returns a placeholder and a flag, every time. Every skill reads one voice file, so the whole account speaks consistently.

## Usage

| You say | What happens |
|---|---|
| "/li-post about our new release" | Three hook options, one full draft, and a copy-ready block; nothing posts without an explicit yes. |
| "/li-human rewrite this draft" | Strips em dashes, slop words, and invisible characters, then scores the result across five checks. |
| "/li-profile here is my profile" | Scores it out of 100 against a 12-part rubric and rewrites what lost points, fix-first. |
| "/li-plan my week" | Plans what to post, when, and the ten people to engage with, writing ~/.claude/linkedin/plan.md. |
| "/li-repurpose this podcast transcript" | Turns the asset into a week of posts that each stand alone. |
| "/li-inbox triage these DMs" | Sorts messages into leads, recruiters, peers and spam, and drafts the replies worth sending. |

## Verification

Check the skill files before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/jakeschincariol/linkedin-agent-skill/main/skills/li-post/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/jakeschincariol/linkedin-agent-skill/main/templates/voice.md | head -20
```

Each skill is one `SKILL.md` under `skills/li-*/`; the humanizer adds `detect.py`, `humanize.py`, and `slop.json` in `skills/li-human/`.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| li-profile | Pass | Pass | Pass |
| li-post | Pass | Pass | Pass |
| li-human | Pass | Pass | Pass |
| li-plan | Pass | Pass | Pass |
| li-comment | Pass | Pass | Pass |
| li-reply | Pass | Pass | Pass |
| li-carousel | Pass | Pass | Pass |
| li-audit | Pass | Pass | Pass |
| li-dm | Pass | Pass | Pass |
| li-repurpose | Pass | Pass | Pass |
| li-inbox | Pass | Pass | Pass |

All 11 sampled skills pass all three scanners.

## Limitations

- Snapshot data, verified Nov 16, 2026: 4,066 combined installs across 11 indexed listings; 3,651 GitHub stars; MIT; last pushed 2026-09-17. Counts drift over time.
- The skills do not post to LinkedIn; every output is a copy-ready block you paste, by design.
- The five checks are local heuristics, not detector APIs; they cannot promise GPTZero, Originality, or Turnitin verdicts.
- The humanizer ships two Python scripts, so the tools drop out if you run a single SKILL.md as a plain chat mode.
- Skipping the voice.md setup makes every output sound generic.

## Related

- [LinkedIn Skills](/hermes/skills/catalog/sergebulaev-linkedin-skills-setup)
- [AI Marketing Skills](/hermes/skills/catalog/ai-marketing-claude-code-skills-setup)
- [YouTube Agent Skills](/hermes/skills/catalog/youtube-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Set up templates/voice.md first; every skill reads it and skipping it flattens your voice.
- Run /li-human before anything goes out, even drafts the other skills already humanized.
- With no Claude Code, paste a single SKILL.md at the top of a chat; you lose the two Python tools but keep the rest.
- Never let a skill post; the approval gate is the design, not a setting.
- Edit skills/li-human/slop.json to add your own banned terms and phrases.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
