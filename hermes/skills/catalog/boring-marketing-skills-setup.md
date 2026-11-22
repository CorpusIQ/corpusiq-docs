---
title: "Boring Marketing Skills - Marketing Operator Suite Setup"
description: "boringmarketer/boring-marketing-skills: 32 free marketing skills for research, positioning, copy, SEO, ads and local clients - 6.4K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/boring-marketing-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "marketing", "seo", "copywriting", "local seo"]
---

# Boring Marketing Skills - Marketing Operator Suite Setup

**Source:** [boringmarketer/boring-marketing-skills](https://www.skills.sh/boringmarketer/boring-marketing-skills) via skills.sh - 6.4K combined installs across 32 indexed listings; first catalogued Nov 21, 2026 (Nov 21, 2026 evening sweep)
**GitHub:** [boringmarketer/boring-marketing-skills](https://github.com/boringmarketer/boring-marketing-skills) - 782 stars, MIT license, main branch, last pushed Nov 17, 2026; skills live under `skills/<name>/SKILL.md` with `references/` subfolders (some add `scripts/` or `modes/`), plus a `_system/` directory for shared conventions, schemas and scripts, an `agents/research.md` file, `automations/` hooks and workflows, and `.claude-plugin/` marketplace manifests.
**Category:** Marketing, SEO and Local Business Operations
**Quality Tier:** 🟠 Orange - 8 Fail cells in the 20-skill sample, all from Snyk: google-business-profile, find-local-clients, landing-page, performance-review, ads-incrementality-check, reviews, pitch-the-fix and meta-ads.

Boring Marketing Skills is James Dickerson's free marketing operator suite: 32 skills for Claude Code, Codex, Cursor and other agents, built from real campaigns and working without any paid tool. The repository groups them by the stage where a customer meets a business: start here (brand files and routing), get found (SEO, AI search and local pages), get chosen (copy, pages and lead magnets), get the call (ads, tracking and speed to lead), bring them back (email, newsletter and performance review), and win clients for agencies and freelancers.

The install counts run in a flat 194 to 207 band, and that is a shape rather than a defect: the 32 listings ship as one unit through a single `npx skills add boringmarketer/boring-marketing-skills` install, so every count moves together and none is an independent popularity signal. The suite's depth is in local business: a large share of the skills (google-business-profile, first-screen-check, find-local-clients, pitch-the-fix, service-area-pages, local-seo-plan, reviews and speed-to-lead) target local service businesses and the agencies that pitch them.

## Installation

Any agent (Claude Code, Codex, Cursor and others):

```bash
npx skills add boringmarketer/boring-marketing-skills
```

Claude Code plugin:

```
/plugin marketplace add boringmarketer/boring-marketing-skills
/plugin install boring-marketing@boring-marketing-skills
```

Then run `/start-here` and name the business. It reads the site and reviews, writes the brand files every other skill uses, and tells you which skill to run next. The first run takes about 3 minutes.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| competitive-intel | 207 | Tears down 3-6 competitors in parallel and writes exploitable gaps to competitors.md |
| positioning-angles | 206 | Finds the angle and offer that make something sell, with a local-service mode |
| audience-research | 206 | Mines reviews and communities into audience.md and voc.md brand files |
| ai-search | 206 | Checks whether ChatGPT, Perplexity and Google AI name and cite the business |
| google-business-profile | 205 | Audits the Google profile against the top 3 in Google Maps and writes a month of posts |
| start-here | 204 | Front door that reads the business, writes brand files and routes the next skill |
| keyword-research | 204 | Maps search and AI questions into a topic map instead of a huge keyword list |
| direct-response-copy | 203 | Writes copy that converts in the customer's own words, behind a claim gate |
| brand-voice | 203 | Extracts a falsifiable brand voice profile every other skill reads |
| first-screen-check | 202 | Checks the first phone screen for the number, promise and proof |
| find-local-clients | 202 | Ranks local businesses losing the most customers, for agencies to pitch |
| site-audit | 201 | Crawls a site like Google and AI crawlers do and returns a ranked fix list |
| landing-page | 201 | Turns an offer into a shipped landing page with section-by-section teardown |
| performance-review | 200 | Turns performance data into an honest diagnosis and ranked next actions |
| lead-magnet | 200 | Builds lead magnets including interactive quiz and calculator apps |
| ads-incrementality-check | 200 | Pause-tests an ad campaign against the phone log to prove incrementality |
| reviews | 199 | Finds stalled reviews, drafts owner replies and sets up the ask |
| pitch-the-fix | 199 | Finds the owner and writes a cold email about one broken thing |
| meta-ads | 199 | Launches and verifies Meta ad campaigns through the Marketing API |
| long-form-article | 199 | Plans and drafts a 3,000-5,000 word guide with named sources |
| local-seo-plan | 199 | Decides which services and towns get a page, a section or a skip |
| creative | 199 | Makes ad images and short videos with AI image and video models |
| content-atomizer | 199 | Turns one piece into posts for every platform |
| paid-ads | 198 | Writes Google and Meta ads plus the test plan |
| google-ads-tracking | 198 | Makes Google Ads count calls and form fills as conversions |
| seo-content | 197 | Writes articles and guides that answer real searches |
| email-sequences | 197 | Writes welcome, follow-up, review ask and seasonal emails |
| speed-to-lead | 196 | Finds missed calls and slow replies, then sets up text-back |
| social-content | 195 | Writes posts from your own best posts, not generic hooks |
| service-area-pages | 194 | Writes town and service pages that are not swapped-city duplicates |
| programmatic-seo | 194 | Builds many pages from one template and a data set |
| newsletter | 194 | Plans and writes a newsletter people open |

All 32 indexed listings clear the 100-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

The suite's real product is its brand-files architecture: start-here reads the business and writes the brand memory, audience and voice files that every other skill consumes, so downstream copy, pages and posts stay grounded in the customer's own words instead of drifting into generic model prose. The local-business depth matters for operators because several skills tie every channel's claimed results back to the business's own phone log: ads-incrementality-check pause-tests a campaign against the call log, performance-review reads each channel against the business's own count before giving credit, and speed-to-lead closes the missed-call gap. AI search is treated as a first-class distribution channel rather than an afterthought, with ai-search and seo-content checking whether ChatGPT, Perplexity and Google's AI answers name and cite the business and what to fix when they do not. The write-capable surfaces carry a review cost: 8 Snyk Fails across the 20 sampled skills, concentrated on the ads, landing page, reviews and local-client-pitching skills, so wire those behind a check before touching a live ad account or Google Business Profile.

## Usage

| You say | What happens |
|---|---|
| Run start-here for my business | Reads the site and reviews, writes the brand files, and routes the next skill |
| Is ChatGPT recommending my business? | Runs ai-search to check AI answer citations and what to fix |
| Write copy that makes the phone ring | Runs direct-response-copy with the claim gate and score-and-rewrite loop |
| Which local businesses are losing customers? | Runs find-local-clients to rank a trade and town by lost customers |
| Is my ad actually making the phone ring? | Runs ads-incrementality-check to pause-test against the phone log |
| Audit my Google Business Profile | Runs google-business-profile against the top 3 in Google Maps and writes posts |
| Turn this article into posts for every platform | Runs content-atomizer to split one piece across platforms |

## Verification

Review the front-door routing instructions before the first run:

```bash
curl -sL https://raw.githubusercontent.com/boringmarketer/boring-marketing-skills/main/skills/start-here/SKILL.md | head -60
```

Review the direct-response claim gate before wiring copy output:

```bash
curl -sL https://raw.githubusercontent.com/boringmarketer/boring-marketing-skills/main/skills/direct-response-copy/SKILL.md | head -60
```

Inspect the install script that stamps the shared brand context:

```bash
curl -sL https://raw.githubusercontent.com/boringmarketer/boring-marketing-skills/main/_system/scripts/install.sh | head -60
```

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| competitive-intel | Pass | Pass | Warn |
| positioning-angles | Pass | Pass | Warn |
| audience-research | Pass | Pass | Warn |
| ai-search | Pass | Pass | Warn |
| google-business-profile | Pass | Pass | Fail |
| start-here | Pass | Pass | Warn |
| keyword-research | Pass | Pass | Warn |
| direct-response-copy | Pass | Pass | Warn |
| brand-voice | Pass | Pass | Warn |
| first-screen-check | Pass | Pass | Warn |
| find-local-clients | Pass | Pass | Fail |
| site-audit | Pass | Pass | Warn |
| landing-page | Pass | Pass | Fail |
| performance-review | Pass | Pass | Fail |
| lead-magnet | Pass | Pass | Warn |
| ads-incrementality-check | Pass | Pass | Fail |
| reviews | Warn | Pass | Fail |
| pitch-the-fix | Pass | Pass | Fail |
| meta-ads | Pass | Pass | Fail |
| long-form-article | Pass | Pass | Warn |

The sample is Snyk-heavy: 8 Fails and 12 Warns across the 20 sampled skills, concentrated on the write-capable surfaces (ads, landing pages, reviews and local-client pitching), while Socket passes all 20 and Gen Agent Trust Hub warns only on reviews.

## Limitations

- Snapshot data, verified Nov 21, 2026: 6,406 combined installs across 32 indexed listings; 782 GitHub stars; MIT license; last pushed Nov 17, 2026. Counts drift over time.
- The 20-skill security sample carries 8 Snyk Fail cells (google-business-profile, find-local-clients, landing-page, performance-review, ads-incrementality-check, reviews, pitch-the-fix and meta-ads), so review the write-capable skills before wiring a live ad account or Business Profile.
- The flat 194 to 207 install band reflects single-unit installation, not per-skill popularity: installing the repository increments all 32 listings together, so individual counts are not an independent signal.
- The index and the tree line up cleanly here: all 32 indexed listings have a matching `skills/<name>/SKILL.md` directory, so there is no index-only drift to reconcile.
- The author discloses boringfunnels (his own paid tool) inline wherever a skill mentions it, and no skill requires it; the free path stays first.

## Related

- [Local SEO Skills](/hermes/skills/catalog/local-seo-skills-setup)
- [OpenClaudia Skills - 78-Skill Marketing Toolkit Setup](/hermes/skills/catalog/openclaudia-skills-setup)
- [Kostja94 Marketing Skills - Copywriting, SEO, Ads Setup](/hermes/skills/catalog/kostja94-marketing-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run start-here first and let it write the brand files; every other skill reads them, so skipping it makes downstream copy sound generic.
- Keep the write-capable skills (meta-ads, google-ads-tracking, landing-page, reviews) behind a review gate, since the Snyk Fails cluster on those surfaces.
- Tell each skill "new client" to keep a separate folder per client instead of mixing brand files across accounts.
- Tie every channel's claimed results back to the business's own phone log with ads-incrementality-check and performance-review before giving any channel credit.
- The suite runs on your agent's own web access first; the README's stack table names paid upgrades (DataForSEO, Firecrawl, Exa) only at the step where they help.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
