---
title: "Instagram Scraper Skill - Social Data Extraction"
description: "skillify-sh/skills on skills.sh: 8.0K combined installs; scrape public Instagram profiles, reels, comments and hashtags without login, via Apify."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/skillify-instagram-scraper-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "instagram", "scraping", "social data"]
---

# Instagram Scraper Skill - Setup Guide

**Source:** [skillify-sh/skills](https://www.skills.sh/skillify-sh/skills) via skills.sh - 8.0K combined installs across 1 indexed listing; first seen 2026-11-05 (Nov 5, 2026 morning sweep)
**GitHub:** 0 stars, MIT, last pushed 2026-08-23, one SKILL.md directory at `skills/instagram-scraper`
**Category:** Public social media data extraction: Instagram profiles, posts, reels, comments, hashtags and mentions
**Quality Tier:** 🟡 Beta - Snyk Fail on instagram-scraper; MIT; 0 stars.

Skillify Skills is a small publisher with a narrow promise: dependable agent skills for public social media data. The repository currently ships exactly one skill, `instagram-scraper`, and states three rules in its README: no logins ever, tell the user the cost before spending their money, and fail with an answer instead of an error.

The skill wraps Apify's `apify/instagram-scraper` actor, so it reads what Instagram serves to logged-out visitors. No Instagram password, cookie, session token or Meta developer account is involved. Profiles, posts, reels, stories, comments, hashtags, locations and mentions all come back from a single input schema, and the skill's own setup section checks for an Apify token before it makes any billable call.

## Installation

The README installs the skill cross-agent through skills.sh:

```bash
npx skills add skillify-sh/skills
```

It also documents a manual path: copy any `skills/<name>/` directory from the repository into your agent's skills directory. That is the way to install when you want to read the skill before it runs.

There is nothing else to configure up front. On first use the skill checks for credentials and, when none are present, walks the user through creating a free Apify account. The token is read from `APIFY_TOKEN` or from a logged-in Apify CLI session, so a headless agent can inject it as a secret instead of running the sign-up flow. The README discloses that sign-up links inside the skill are referral links, and that signing up at the Apify console directly works identically.

## What It Provides

One indexed listing, above the threshold.

| Skill | Installs | Use For |
|---|---|---|
| instagram-scraper | 7,997 | Public Instagram profiles, posts, reels, stories, comments, hashtags, locations and mentions without a login or Meta developer account |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

Social competitors, creator shortlists and audience research are all questions an agent gets asked, and the honest answer used to be "I cannot see Instagram". This skill turns that into a bounded, priced data call with a documented input schema.

The cost discipline is the interesting design choice. The skill ships a rule that `resultsType` of `details` costs one result per profile, while `posts` costs up to 100 times more for the same follower count question, and that `resultsLimit` must always be set because the provider default is 100 results per URL. That is the kind of default an agent left to itself gets wrong on the first call.

The failure behavior is also written down rather than improvised: an empty result is reported as empty, a rate limit is explained in plain words, and a missing account produces onboarding instead of a stack trace.

For Hermes agents specifically, the value is that the skill keeps credentials out of the conversation. The token lives in the environment or the Apify CLI config, and the skill is explicit that it should never ask the user to paste a token into chat.

## Usage

| You say | What happens |
|---|---|
| "How many followers does nasa have on Instagram?" | instagram-scraper runs a `details` call for the profile and returns follower, following and post counts |
| "Pull the last 20 posts from this competitor account" | instagram-scraper runs a bounded `posts` call with an explicit results limit |
| "Read the comments on this post" | instagram-scraper switches to `comments` for the post URL and returns the thread |
| "Find recent posts under this hashtag" | instagram-scraper searches the hashtag and reports the returned items |
| "Which accounts mention our brand this week?" | instagram-scraper uses `mentions` against the account and returns matching posts |
| "Export engagement numbers for these ten creators" | instagram-scraper loops the profile list with `details` and states the result cost before running |
| "Get the currently live stories for this account" | instagram-scraper runs a `stories` call and reports an empty result honestly when nothing is live |

## Verification

Fetch the skill file the installer pulls and read the frontmatter before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/skillify-sh/skills/main/skills/instagram-scraper/SKILL.md | head -20
```

It should open with `name: instagram-scraper` and a folded description naming profiles, posts, reels, stories, comments, hashtags, locations and mentions, and it should name the Apify actor it runs on. Then confirm the install landed as a directory in the skills folder your installer targets:

```bash
ls ~/.claude/skills | grep instagram
```

A single `instagram-scraper` entry should appear. Before the first data call, run the preflight from the skill's Setup section: it prints `AUTH_OK curl`, `AUTH_OK cli` or `AUTH_MISSING`, and the skill is written to stop at `AUTH_MISSING` and onboard the user rather than attempt a call.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| instagram-scraper | Pass | Pass | Fail |

The Snyk verdict for instagram-scraper is a Fail. Gen Agent Trust Hub and Socket both pass, but a single Fail on the one skill in the repository is a real finding, not a formality: read the skill source and the Snyk report before pointing it at production accounts.

Mitigations that are visible in the source: no social network login, no cookies or session tokens, API tokens kept on the user's machine, and a `User-Agent` header that names the skill so runs can be told apart in Apify logs (and can be removed). The remaining risk is the outbound data flow itself, which sends the query to Apify, and the referral links in the sign-up path.

## Limitations

- Snapshot data, verified 2026-11-05: 7,997 combined installs across 1 indexed listing; 0 GitHub stars; MIT; last pushed 2026-08-23. Counts drift over time.
- instagram-scraper carries a Snyk Fail, so treat install-and-run as a reviewed decision rather than a default.
- The skill needs a paid third-party account: Apify bills from $2.30 per 1,000 results, and the free tier is $5 of monthly credit, roughly 2,000 results. There is no free unlimited path.
- Public data only. Private accounts, follower-only stories and anything behind a login are out of scope by design.
- One skill, 0 GitHub stars, last pushed 2026-08-23: a small surface with little community review, so pin the version you install.
- Provider-side changes or rate limits surface as errors, and no local fallback exists when Apify is unavailable.

## Related

- [Apidojo Social Media Skills - X/Instagram/TikTok Scraper Suite Setup](/hermes/skills/catalog/apidojo-social-media-skills-setup)
- [Apify Ultimate Scraper - Universal Web Scraping for 15+ Platforms Setup](/hermes/skills/catalog/apify-ultimate-scraper-setup)
- [Bright Data Agent Skills - Web Scraping & Research Setup](/hermes/skills/catalog/brightdata-agent-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Always set `resultsLimit`. The provider default is 100 results per URL, so a five-URL call can cost 500 results when the user wanted 25.
- Use `resultsType: "details"` for follower, bio and post count questions. It returns one result per profile instead of a feed.
- Start with a small bounded run, show the user what came back, and only then scale. At $2.30 per 1,000 results a 5,000 result job is about $11.50.
- Never retry a `401` or `402` in a loop. Both are billable dead ends, and a token problem needs the user, not a second attempt.
- Pass the Apify token through the environment as a secret. The skill is written never to ask for a token in the conversation, and that property is worth keeping.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
