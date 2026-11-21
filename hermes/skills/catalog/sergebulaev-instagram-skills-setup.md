---
title: "Instagram Skills - Content and Growth Setup"
description: "sergebulaev/instagram-skills: ten Instagram content skills for captions, carousels, hooks, hashtags and weekly planning - 2.4K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sergebulaev-instagram-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "instagram", "social media", "content"]
---

# Instagram Skills - Content and Growth Setup

**Source:** [sergebulaev/instagram-skills](https://www.skills.sh/sergebulaev/instagram-skills) via skills.sh - 2.4K combined installs across 10 indexed listings; first seen Nov 21, 2026 (Nov 21, 2026 morning sweep)
**GitHub:** [sergebulaev/instagram-skills](https://github.com/sergebulaev/instagram-skills) - 890 stars, MIT license, main branch, last pushed Nov 18, 2026; a plugin-style bundle with nine skills under `skills/<name>/SKILL.md`, a root SKILL.md entry skill, and a generated nested Codex package under `.codex-marketplace/`.
**Category:** Social Media Content and Growth
**Quality Tier:** 🟡 Yellow - 10 of 10 sampled skills pass Gen Agent Trust Hub, with 1 Socket Warn (instagram-marketing) and 3 Snyk Warns (instagram-marketing, ig-profile-optimizer, ig-audience-insights); no Fails.

sergebulaev publishes this bundle from Creative Content Crafts, the team behind the linkedin-skills family. Ten indexed listings turn Claude Code, Codex and Hermes into an Instagram content team: captions with a first-125-character hook, slide-by-slide carousels, sized hashtags, a weekly plan, profile audits, and niche reads from real data via Apify. Every action skill follows a draft, then approval, then publish pattern.

The nine ig-* skills are single-purpose, and the instagram-marketing listing is the root SKILL.md entry skill that routes a request to the right one. This bundle automates posting: when the Publora API is connected, a skill uploads your media and schedules the post on approval. Instagram requires media on every post, so the skills write the words while you supply the image or video. First seen in the Nov 21, 2026 morning sweep.

## Installation

Pick your host. Codex CLI:

```bash
codex plugin marketplace add sergebulaev/instagram-skills
codex plugin add instagram-skills@instagram-skills
```

Claude Code (CLI, VS Code, JetBrains):

```text
/plugin marketplace add sergebulaev/instagram-skills
/plugin install instagram-skills@instagram-skills
```

On claude.ai or Claude Desktop, use Skills then Add from GitHub and paste `sergebulaev/instagram-skills`. Hermes Agent loads `skills/*/SKILL.md` directly:

```bash
git clone https://github.com/sergebulaev/instagram-skills.git ~/.hermes/skills/instagram-skills
```

Any other agent that reads SKILL.md files:

```bash
npx skills add sergebulaev/instagram-skills
```

Publishing is optional and takes about two minutes: sign up at Publora, connect a Business or Creator Instagram account, put `PUBLORA_API_KEY` and `INSTAGRAM_PLATFORM_ID` in a `.env` file in the bundle root, and run `pip install requests python-dotenv`. Without Publora, the skills return each draft as copy-paste text with a reminder to attach media in the app.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| instagram-marketing | 1,499 | the root entry skill that routes an Instagram request to the matching ig-* skill and carries the shared voice rules |
| ig-hashtag-strategist | 114 | sizing a 3 to 5 tag set (niche, mid, broad) matched to the post so a small or mid account can actually rank |
| ig-profile-optimizer | 112 | auditing and rewriting the profile end-to-end: name field, bio, link, highlights, first-9 grid and pinned posts |
| ig-carousel-planner | 111 | planning a carousel slide by slide, up to 10 slides, from hook slide through value slides to the payoff |
| ig-content-planner | 107 | generating a weekly per-day mix of Reels, carousels, images and stories with hooks, times and goals |
| ig-caption-writer | 105 | drafting a caption with the hook in the first 125 characters, a skimmable body and one CTA |
| ig-humanizer | 103 | stripping the AI tells from a caption or slide, with an audit mode for the pre-publish check |
| ig-hook-extractor | 103 | reverse-engineering the hook from a viral Reel or carousel into one of the 10 formulas and a blank template |
| ig-repurposer | 92 | rebuilding a LinkedIn post, blog, YouTube script or X thread into a native Instagram carousel or caption |
| ig-audience-insights | 86 | reading your niche and profile from real data via Apify: hashtag scans and follower or competitor stats, no login |

No indexed listings fall below the threshold; all 10 appear above.

## Why This Matters for Hermes Agents

Instagram content is where agents fail quietly in public: a caption that reads machine-made, a carousel that loses the reader on slide two, a hashtag wall that signals spam. This bundle attacks each failure mode with a single-purpose skill instead of one vague writing prompt. The humanizer is the standout: it strips the specific AI tells readers react to and caps em dashes at about one per 100 words rather than banning them, because it targets density, not the character.

The approval pattern is the operational safeguard. Every action skill shows a draft and waits for your OK before anything publishes, so a human decision stays a human decision even when the writing is automated. The content planner shifts an operator from ad-hoc posting to a weekly saves-and-shares goal, which the bundle treats as the lever that matters in 2026. The audience-insights skill reads real niche data through Apify instead of guessing, and it says plainly what it cannot see: Instagram hides likers and commenters, so it is discovery plus profile stats, not an engager list. Because Instagram requires media on every post, the skills never pretend a text-only post will ship.

## Usage

| You say | What happens |
|---|---|
| Write a caption for this Reel | ig-caption-writer drafts a caption with the hook in the first 125 characters and one clear CTA |
| Plan a week of Instagram posts for my niche | ig-content-planner produces a per-day Reel, carousel and story mix with hooks, times and goals |
| What is working in my niche right now? | ig-audience-insights scans a hashtag for trending posts via Apify, no login required |
| Turn my notes into a 10-slide carousel | ig-carousel-planner plans each slide and drafts the caption |
| Rewrite this caption so it does not sound like AI | ig-humanizer strips the AI tells and returns the cleaned draft |
| Give me 5 hashtags sized for my account | ig-hashtag-strategist builds a niche, mid and broad set matched to the post |
| Post this image to Instagram tomorrow | On approval, the skill runs the Publora draft, upload and schedule flow |

## Verification

Confirm the bundle landed, then review a skill's instructions before relying on it:

```bash
ls ~/.hermes/skills/instagram-skills/skills
```

```bash
curl -sL https://raw.githubusercontent.com/sergebulaev/instagram-skills/main/skills/ig-caption-writer/SKILL.md | head -40
```

If you connected Publora, test the write side with a post scheduled 24 hours out and cancel it in the Publora dashboard before it fires. A returned `postGroupId` means the API key and platform ID are correct.

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| instagram-marketing | Pass | Warn | Warn |
| ig-hashtag-strategist | Pass | Pass | Pass |
| ig-profile-optimizer | Pass | Pass | Warn |
| ig-carousel-planner | Pass | Pass | Pass |
| ig-content-planner | Pass | Pass | Pass |
| ig-caption-writer | Pass | Pass | Pass |
| ig-humanizer | Pass | Pass | Pass |
| ig-hook-extractor | Pass | Pass | Pass |
| ig-repurposer | Pass | Pass | Pass |
| ig-audience-insights | Pass | Pass | Warn |

This bundle automates posting: when Publora is connected, a skill uploads media and schedules posts on approval. The `PUBLORA_API_KEY` and `INSTAGRAM_PLATFORM_ID` live in a local `.env` file, and the read skill can use an `APIFY_TOKEN`. Instagram API access rules and account risk are the operator's responsibility: a Business or Creator account is required, and automated posting can trigger platform enforcement.

## Limitations

- Snapshot data, verified Nov 21, 2026: 2,432 combined installs across 10 indexed listings; 890 GitHub stars; MIT license; last pushed Nov 18, 2026. Counts drift over time.
- Index-versus-tree drift: the install index has 10 entries but `skills/` holds 9 directories; instagram-marketing is the root SKILL.md bundle entry with no `skills/` subdirectory of its own.
- The write side depends on the Publora API and needs a Business or Creator Instagram account; personal accounts are not supported by the publishing flow.
- Instagram API access rules and account risk are the operator's responsibility; automated posting can trigger platform enforcement, so schedule conservatively and keep publishing behind the approval gate.
- ig-audience-insights reads data through Apify actors, which need an `APIFY_TOKEN` (or the Apify MCP server on claude.ai) and incur per-run cost.

## Related

- [Apidojo Social Media Skills - X/Instagram/TikTok Scraper Suite Setup](/hermes/skills/catalog/apidojo-social-media-skills-setup)
- [Blacktwist Social Media Skills - 14-Skill Content Suite Setup](/hermes/skills/catalog/blacktwist-social-media-skills-setup)
- [Charlie Hills Social Media Skills - 17-Skill Content System Setup](/hermes/skills/catalog/charlie-hills-social-media-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Keep publishing manual until you trust the drafts: install and write captions first, connect Publora only after a few dry runs.
- Keep the `?actors=` filter when adding the Apify MCP server, so the agent cannot run arbitrary actors in the Apify store at your cost.
- Schedule a test post 24 hours out and cancel it in the Publora dashboard to confirm the API key and platform ID before any real posting.
- Store your voice and brand in `references/voice-profile.md` so every skill inherits the same rules instead of drifting.
- Treat the humanizer as a scrub pass, not a detector bypass: no edit reliably beats AI detectors, and the skill says so itself.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
