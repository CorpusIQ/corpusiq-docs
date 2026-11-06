---
title: "Instagram Agent Skill - Thirteen Account Skills"
description: "jakeschincariol/instagram-agent-skill on skills.sh: 12.5K combined installs across 13 listings; Claude skills for Reels, captions, carousels and DMs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/instagram-agent-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "instagram", "social media", "content"]
---

# Instagram Agent Skill - Setup Guide

**Source:** [jakeschincariol/instagram-agent-skill](https://www.skills.sh/jakeschincariol/instagram-agent-skill) via skills.sh - 12.5K combined installs across 13 indexed listings; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 5,054 stars, MIT licence (LICENSE in the repo root), last pushed 2026-09-13, 13 SKILL.md directories under skills/, plus a .claude-plugin manifest and templates/voice.md
**Category:** Instagram operations for agents: reel hooks, caption linting, carousels, DM and comment replies, weekly planning
**Quality Tier:** 🟡 Review - MIT licence and a small install surface, but one sampled skill (ig-reply) carries a Snyk Warn and every skill ends in a copy-ready block that a human posts by hand.

The Instagram agent skill is a thirteen-skill set by Jake Schincariol for running one Instagram account from a coding agent. It is free, MIT, needs no signup, no API key and nothing connected. The skills divide into the writing work (Reels off 26 scored hook formulas, captions, carousels, Stories, comments, replies, DMs, profile copy, a weekly plan, repurposing one long asset) and the reading work (viral research, a post-mortem on what already went out).

What makes the set worth reading is the number of its parts that actually compute something. `skills/ig-reel/hooks.json` holds the 26 formulas with a match regex each, `hookscore.py` scores a hook on a five-property panel, `beats.py` turns a script into a timed beat sheet, `caption.py` prints the first 125 characters the way the feed cuts them, and `skills/ig-human/slop.json` carries 154 stock terms, 18 invisible character classes and 16 structural tells. The README is also unusually candid about the measurement: a corpus of 74 real short-form hooks, AUC 0.83 at catching deliberately bad hooks, and AUC 0.56 at separating a creator's hits from the same creator's misses.

## Installation

The README offers three routes. The slowest and most portable is a clone plus copy:

```bash
git clone https://github.com/Jakeschincariol/instagram-agent-skill.git
cp -r instagram-agent-skill/skills/ig-* ~/.claude/skills/
```

As a Claude Code plugin, using the manifest the repository ships in `.claude-plugin/`:

```
/plugin marketplace add Jakeschincariol/instagram-agent-skill
/plugin install instagram-agent
```

Or paste this into Claude and let it do the work:

```
https://github.com/Jakeschincariol/instagram-agent-skill

Install this skill, then confirm /ig-reel works.
```

Project-local instead of global means copying the same folders into the repository's `.claude/skills/`. There is one setup step that is not optional in practice: copy `templates/voice.md` to `~/.claude/instagram/voice.md` and fill it in, because every skill reads that file. The README suggests sending the agent three of your own reels and asking it to write the file from them.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ig-reel | 1,028 | One idea into a Reel: three hooks scored off 26 formulas, then the script, on-screen text and a timed beat sheet |
| ig-viral | 990 | Finds what is working in a niche, ranks each reel by its multiple over that account's own median, names the formula and writes the swipe file |
| ig-caption | 990 | Writes the caption and lints it, showing the 125 characters the feed actually shows before the tap |
| ig-carousel | 989 | Swipe posts: the cover that earns the swipe, slide copy and the 1080x1350 files |
| ig-human | 972 | Strips invisible characters, typography and slop vocabulary, then scores the draft against a five-check panel |
| ig-audit | 959 | Post-mortem on what was already posted: ranks by outlier multiple and reports sends per reach rather than raw views |
| ig-plan | 956 | The week: what to post, which format, when, and the accounts to engage with |
| ig-story | 952 | The daily Story sequence, which sticker does which job, and the DM funnel that starts with them moving first |
| ig-profile | 946 | Scores a profile out of 100 against a 12-part rubric, then rewrites in fix-first order |
| ig-dm | 940 | Keyword delivery, the first message to someone who engaged, the collab pitch and two follow-ups |
| ig-repurpose | 939 | One video, podcast or newsletter into a week of reels and carousels that each stand alone |
| ig-comment | 935 | Comments on other people's posts: nine types, picked by what the post actually is |
| ig-reply | 928 | The thread under your own post, sorted into keyword, lead, substance, question, support and noise, then answered in that order |

All 13 indexed listings clear the 500-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Most agent-written social copy fails in the same place: it is grammatically fine, structurally generic, and it opens with a greeting the algorithm has no reason to reward. This suite treats that as a scoring problem rather than a taste problem. The hook panel names its five properties, the caption linter prints the truncation window, and the humanizer flags the specific shapes (rule-of-three triads, "it is not just X, it is Y", uniform sentence length) that make a draft read as machine output.

The local tools are the part a Hermes agent cannot get from a prompt. Zero-width characters, byte-order marks, soft hyphens and Unicode tag characters survive copy-paste and are invisible in every editor; `humanize.py` removes them and `detect.py` scores what is left. That is a checkable operation with a before-and-after number, not an opinion.

The measurement discipline is the second reason. Ranking reels by multiple over each account's own median rather than by absolute views is the difference between finding a format that worked and finding an account that is simply large. The same logic shows up in `ig-audit`, which orders past posts by outlier multiple and by sends per reach.

Finally, the suite respects the platform boundary instead of hiding it. These skills never post, never log in as you and never scrape at volume; the README says plainly that every other route violates Instagram's terms and gets accounts action-blocked. An agent that hands back a copy-ready block and waits for approval is a safer default than one wired to a publishing API you would have to defend in app review.

## Usage

| You say | What happens |
|---|---|
| "Write me a reel about the contract clause that cost me money" | ig-reel generates three hooks, scores them on the panel, then writes the script, on-screen text and beat sheet |
| "What is working in my niche right now" | ig-viral reads public reels at human speed, ranks by multiple over each account's median and writes the swipe file |
| "Caption this carousel and check the truncation" | ig-caption writes the caption, prints what the feed shows before the tap, and lints hashtags, length and search terms |
| "Does this sound like ChatGPT" | ig-human removes invisible characters and slop terms, then scores burstiness, specificity, slop density, fingerprint and voice |
| "Why did last week's posts flop" | ig-audit post-mortems past posts by outlier multiple and reach per send |
| "Handle the comments on my last reel" | ig-reply sorts the thread into six buckets and drafts replies in that order |
| "Turn this podcast into a week of posts" | ig-repurpose cuts the asset into standalone reels and carousels |

## Verification

Fetch two SKILL.md files before installing, to read what the agent will actually load:

```bash
curl -fsSL https://raw.githubusercontent.com/jakeschincariol/instagram-agent-skill/main/skills/ig-reel/SKILL.md | head -5
curl -fsSL https://raw.githubusercontent.com/jakeschincariol/instagram-agent-skill/main/skills/ig-human/SKILL.md | head -5
```

Both return 200 on the `main` branch. The first should open with `name: ig-reel` and a description naming the 26 hook formulas, the spoken script, the on-screen text and the beat sheet. The second should name the invisible characters, the slop lexicon and the five-check panel.

Then install and confirm the skills landed with their data files, not just their instructions:

```bash
git clone https://github.com/Jakeschincariol/instagram-agent-skill.git
cp -r instagram-agent-skill/skills/ig-* ~/.claude/skills/
ls ~/.claude/skills/ig-reel ~/.claude/skills/ig-human
```

`ig-reel` should show SKILL.md next to `hooks.json`, `hookscore.py` and `beats.py`; `ig-human` should show `slop.json`, `humanize.py` and `detect.py`. A skill folder with only SKILL.md means you pasted a file instead of installing the skills, and the scoring tools are gone.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ig-reel | Pass | Pass | Pass |
| ig-carousel | Pass | Pass | Pass |
| ig-plan | Pass | Pass | Pass |
| ig-dm | Pass | Pass | Pass |
| ig-reply | Pass | Pass | Warn |

The ig-reply Warn is the one to read first, since replying to comments is where a draft goes out under your name fastest. On the code side the surface is small and local: the five Python tools ship no dependencies, make no network calls and upload nothing, and the JSON files they read are plain data. The skills themselves never authenticate to Instagram, never post and never ask for a password or token.

The risk that remains is editorial rather than executable. These skills write in your voice to your audience, and the approval gate is the design, not a setting you can turn off. Read the copy-ready block before it goes anywhere.

## Limitations

- Snapshot data, verified 2026-11-06: 12,524 combined installs across 13 indexed listings; 5,054 GitHub stars; MIT; last pushed 2026-09-13. Counts drift over time.
- The skills do not post. Instagram's Content Publishing API needs a Meta developer app, a linked Page, a long-lived token and app review, and nothing in this repository does that. Every skill ends in a block you paste.
- The hook scorer kills weak hooks, it does not pick winners. The README reports AUC 0.83 against deliberately bad hooks and AUC 0.56 against a creator's own hits versus misses, where 0.50 is a coin flip.
- The measurement corpus is 74 YouTube Shorts, not Reels. The README says so directly: Instagram does not hand out collectable view counts without account access, and scraping would break the terms the repository tells you not to break.
- The five detection checks are local heuristics modelled on public detectors. They are not GPTZero, Originality, Copyleaks or Turnitin and cannot promise those verdicts.
- Platform numbers go stale. The hashtag cap moved from 30 to 5 in December 2025 and the linter carried the old number until it was checked; if the repository contradicts Instagram, Instagram is right.

## Related

- [Apidojo Social Media Skills - X/Instagram/TikTok Scraper Suite Setup](/hermes/skills/catalog/apidojo-social-media-skills-setup)
- [Instagram Scraper Skill - Social Data Extraction](/hermes/skills/catalog/skillify-instagram-scraper-setup)
- [Charlie Hills Social Media Skills - 17-Skill Content System Setup](/hermes/skills/catalog/charlie-hills-social-media-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Fill in `voice.md` before the first reel. Every skill reads it, and the difference between a generic script and one you would say out loud is that file.
- Run `hookscore.py` before `beats.py`. A hook that scores weak on stakes or frontload will not be saved by a tighter edit.
- Ask for the caption window, not just the caption. The first 125 characters decide whether the rest is read at all.
- Treat the humanizer flags as a rewrite list, not a fix list. It repairs invisible characters and typography automatically and hands back the structural tells for judgement, which is the correct split.
- Let ig-audit set the next month. Ranking your own posts by outlier multiple over your own median tells you which format to repeat without guessing.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
