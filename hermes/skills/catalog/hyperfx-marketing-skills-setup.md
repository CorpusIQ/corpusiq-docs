---
title: "HyperFX Marketing Skills - Paid Media and Audience Playbooks"
description: "hyperfx-ai/marketing-skills on skills.sh: 4.2K combined installs; 20 indexed marketing skills for paid ads, social publishing, research and creative"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hyperfx-marketing-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "marketing", "paid ads", "social media", "seo research"]
---

# HyperFX Marketing Skills - Setup Guide

**Source:** [hyperfx-ai/marketing-skills](https://www.skills.sh/hyperfx-ai/marketing-skills) via skills.sh - 4.2K combined installs across 20 indexed listings; first seen 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 112 stars, MIT via LICENSE, `main` branch, last pushed 2026-11-10, 30 SKILL.md files under `skills/`, `.mcp.json` at the repository root, README.md at the repository root
**Category:** Growth marketing: audience research, ad library analysis, campaign planning and creative briefs
**Quality Tier:** 🟡 Solid with caveats - MIT licensed, but twelve Warn verdicts across eleven sampled skills.

HyperFX publishes a marketing skill library that assumes a second component: the Hyper MCP. Each skill is a markdown playbook that names the tools it needs, and those tools arrive through one hosted MCP endpoint rather than per-provider SDKs. The README states that the skills run on the Hyper MCP, that the endpoint carries 100+ direct integrations and built-in scrapers, image generators and video generators, and that approval rules can be set action by action. The repository's own `.mcp.json` points at `https://backend.hyperfx.ai/mcp/`, and the README sends you to `app.hyperfx.ai/mcp` to build and customize the endpoint.

The tree carries 30 SKILL.md files under `skills/`, every one in its own directory with its own frontmatter. The suite spans paid media on eight ad platforms (Google, Meta, Amazon, TikTok, Pinterest, Reddit, Snapchat, OpenAI), organic publishing on three social networks, research (SEO, competitors, customers), creative generation, lifecycle email and cold outreach, plus a brand-context skill that the rest read first. skills.sh indexes 20 of the 30. The README's own install comment still says "install all 24", which the tree has outgrown.

## Installation

The documented default installs every skill in the repository and lets the skills CLI detect your agent:

```bash
npx skills add hyperfx-ai/marketing-skills
```

Single skills install by name, and the README shows both a targeted install and the all-in-one form:

```bash
# install one
npx skills add hyperfx-ai/marketing-skills --skill google-ads

# install all
npx skills add hyperfx-ai/marketing-skills --all
```

The README's other install options cover a global install, a Claude Code plugin, a manual copy and a git submodule:

```bash
# install globally (available across every project)
npx skills add hyperfx-ai/marketing-skills -s seo-research -g

# manual copy
cp -r skills/google-ads ~/.claude/skills/         # Claude Code
cp -r skills/google-ads ~/.agents/skills/         # Cursor / Codex / generic

# git submodule
git submodule add https://github.com/hyperfx-ai/marketing-skills.git .agents/marketing-skills
```

The Claude Code plugin route is two slash commands, quoted from the README:

```text
/plugin marketplace add hyperfx-ai/marketing-skills
/plugin install hyper-marketing@hyperfx-marketing-skills
```

Installing the markdown is the easy half. The skills call named tools on the Hyper MCP, so the endpoint has to exist and the integrations each skill names have to be connected before the playbook can do anything. The README's required-integration column is the checklist: Google Ads, Meta Business, TikTok Marketing, Pinterest Ads, Amazon Ads, Instagram Business Login, LinkedIn, Gmail, Apollo, Klaviyo, Resend, Beehiiv, GA4, Search Console, BigQuery, Firecrawl, Apify, plus the HyperSEO and image and video generation toolkits. A skill without its integration loads and reasons but cannot act.

## What It Provides

The threshold for this guide is zero installs, so all 20 indexed listings appear below with the install integers exactly as skills.sh reports them:

| Skill | Installs | Use For |
|---|---|---|
| instagram | 274 | Publishing photos, Reels, Stories and carousels, moderating comments and mentions, sending DMs and pulling account and media insights over Instagram Business Login |
| meta-ads-library | 253 | Scraping competitor Facebook and Instagram ads from the Meta Ads Library, pulling creative and contact metadata and monitoring new ads by category |
| meta-ads | 230 | Planning and launching Meta campaigns across Facebook and Instagram with Advantage+ defaults, conversion tracking, account audits and performance dashboards |
| ad-creative-generation | 222 | On-brand ad visuals and copy variants, including RSA headlines, Meta and display creative, built from a brand profile extracted from the site |
| tiktok | 222 | Publishing organic TikTok videos, photos and carousels through the TikTok-compliant interactive posting form |
| video-generation | 221 | Text to video and image to video with Veo or Seedance, scene chaining, captions, voiceover, stitching and text overlays |
| google-ads | 213 | Search, Display, Performance Max, Shopping, Demand Gen and App campaign builds plus GAQL-backed reports and conversion tracking diagnosis |
| tiktok-ads | 211 | TikTok ad campaigns by objective, creative upload and ad performance analysis with objective-specific parameter validation |
| analytics-insights | 209 | GA4, Tag Manager, Search Console and BigQuery work: tracking plans, key-event setup, custom dimensions, GTM audits and search performance |
| seo-research | 208 | Keyword research, SERP and AI Overview analysis, competitor benchmarks, backlink trends, Core Web Vitals and full site audits |
| competitor-intel | 206 | End-to-end competitor monitoring across site, social, search rank and AI citations, with diffs and battle cards, weekly digests or board updates |
| email-lifecycle | 204 | Welcome, nurture, re-engagement, win-back and abandoned-cart sequences across Klaviyo, Resend, Beehiiv or Gmail |
| cold-email-outreach | 201 | B2B outbound: Apollo enrichment, per-prospect signals, personalized drafts, Gmail sending with safe defaults and reply routing |
| image-generation | 201 | Text to image, image to image and branded ad creative across model choices including nano-banana, seedream and gpt-image |
| pinterest-ads | 198 | Pinterest campaign builds across awareness, consideration, conversion and catalog objectives with microcurrency budgeting and keyword targeting |
| linkedin | 197 | LinkedIn text posts, article and link previews, document and PDF posts, company page posts and AI-built carousels |
| customer-research | 197 | Voice-of-customer mining across Reddit, YouTube comments, G2 and Capterra, building personas, quote banks and jobs-to-be-done maps |
| amazon-ads | 192 | Amazon Sponsored Products campaigns: keyword and ASIN targeting, bids, negatives, budget rules, plus ACoS and ROAS reporting |
| hyper-cli | 175 | Running Hyper skills from a terminal with `hyperai`, inspecting live tool schemas and calling tools by canonical name |
| brand-context | 159 | Building the single `brand-context.md` every other skill reads: positioning, personas, customer language, voice and proof points |

The tail is arithmetic rather than judgement: no indexed listing falls below zero, so nothing is summarised away. The spread is narrow, 159 to 274, which makes the ordering useless as a quality signal. Ten skills in the tree carry no install count at all: `reddit-ads`, `snapchat-ads`, `openai-ads`, `reddit`, `youtube`, `blog-generation`, `gmail`, `google-sheets`, `slack` and `twilio`. They are described in the README table and installable with `--skill`, but skills.sh does not index them yet, so there is no adoption number to compare.

The composition claim in the README is worth reading closely, because it explains why the suite exists as many small skills rather than one large one. The example campaign that learns a brand, scrapes 412 Instagram posts and 287 TikToks, generates six images and two videos, then pauses four campaign builds for approval is described as seven skills running against one MCP. Small skills plus a shared tool layer means the agent picks a playbook per step instead of loading a monolith.

## Why This Matters for Hermes Agents

Marketing work is where an agent most often has credentials and spend authority, and that combination is where careful structure pays. This library encodes the structure as separate skills: one for building the brand file, one per ad platform, one per research discipline, one per publishing surface. A Hermes agent that loads only `google-ads` and `analytics-insights` gets two focused playbooks and a small context cost, which is the right default for a standing job like a weekly search report.

The most reusable idea here is the `brand-context.md` contract. Every other skill in the suite reads that one document before asking the user to re-explain the business, and it can be drafted from a site via Firecrawl or built through a short interview. Any agent that produces marketing copy for more than one brand hits the same problem, and a single shared context file is a cheap fix that transfers whether or not you keep the rest of the suite.

The second transferable piece is the approval boundary. The README states that every action can require approval before it runs, so an agent cannot delete a campaign or send a DM without a green light. That is the right shape for a build-then-pause workflow: the agent assembles campaigns, creatives and schedules in a paused state and a human sets them live. An agent that launches directly is one bad keyword match away from spending real money.

The third is the tool-name canonicalisation. Skills name tools by a single canonical name and the MCP exposes `search`, `describe`, `call_read`, `call_write` and `call_destructive`, with the access class deciding which call tool runs. The skill body therefore does not depend on a specific client surface: chat, MCP client and CLI all resolve the same name. That is a durable pattern for any agent tooling that has to survive a client change.

The honest counterweight is that almost none of the value lives in the markdown. The skills are 2.9KB to 16.6KB of instructions, and every one of them assumes a paid or credentialed integration behind the MCP. Read the brand-context and cold-email-outreach skills for the decision rules, and treat the rest as a checklist of what to connect before promising a working campaign.

## Usage

| You say | What happens |
|---|---|
| "Plan a Google Ads Search campaign for acmebakes.com at $100 a day" | Builds the campaign structure, keyword themes, match types and negative list, sets the budget, and leaves the campaign paused for approval before launch |
| "Show me what competitors are running on Meta right now" | Queries the Meta Ads Library by keyword, pulls full ad creative and metadata, enriches advertiser pages with contact details and returns a structured ad-intelligence summary |
| "Build the brand context file for this new client" | Drafts `brand-context.md` from the client site through Firecrawl, or falls back to a short interview, and writes positioning, personas, customer language, voice and proof points |
| "Turn last week's webinar into a LinkedIn carousel and a TikTok post" | Writes the LinkedIn carousel from the transcript text, publishes it to the chosen profile or company page, and posts the short version to TikTok through the compliant posting form |
| "Which pages lost clicks last month, and what should we do about it" | Pulls Search Console performance and GA4 reports, isolates the pages and queries that moved, and proposes fixes against the affected templates |
| "Write a three-email welcome flow for the new store" | Plans the welcome sequence, picks the provider that matches the stack, writes the copy and builds the automation in Klaviyo or the configured alternative |
| "What do customers actually complain about in our category" | Mines Reddit, YouTube comments, G2 and Capterra, then returns personas, a verbatim quote bank and a jobs-to-be-done map |

## Verification

The layout is `skills/<name>/SKILL.md`, so every raw path carries that segment. This one is the file the table lists last and returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/hyperfx-ai/marketing-skills/main/skills/brand-context/SKILL.md | head -8
```

It opens with YAML frontmatter holding `name: brand-context`, a one-line description that starts "Create and maintain a single brand-context.md", then the heading `# Brand Context`. A 404 here means the `skills/` layout moved and every path in this guide needs a new segment.

After an install, confirm the skills landed where the agent reads them. The README's manual-copy lines name the two directories that matter:

```bash
ls ~/.agents/skills | grep -E '^(brand-context|google-ads|meta-ads|instagram)$'
ls ~/.claude/skills | grep -E '^(brand-context|google-ads|meta-ads|instagram)$'
```

An empty result on both lines means the CLI wrote somewhere else, which happens when it detects an agent other than the one you meant to target. The count check is the cheapest way to see how much of the tree skills.sh is not indexing:

```bash
curl -fsSL "https://api.github.com/repos/hyperfx-ai/marketing-skills/git/trees/main?recursive=1" | grep -c '"path": ".*SKILL.md"'
```

That returns 30 against 20 indexed listings.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| instagram | Pass | Pass | Warn |
| meta-ads-library | Pass | Pass | Warn |
| meta-ads | Warn | Pass | Warn |
| ad-creative-generation | Pass | Pass | Warn |
| tiktok | Pass | Pass | Pass |
| video-generation | Pass | Pass | Pass |
| google-ads | Pass | Pass | Warn |
| tiktok-ads | Pass | Pass | Pass |
| analytics-insights | Pass | Pass | Pass |
| seo-research | Pass | Pass | Pass |
| competitor-intel | Pass | Pass | Warn |
| email-lifecycle | Pass | Pass | Pass |
| cold-email-outreach | Pass | Pass | Warn |
| image-generation | Pass | Pass | Warn |
| pinterest-ads | Pass | Pass | Pass |
| linkedin | Pass | Pass | Pass |
| customer-research | Pass | Pass | Warn |
| amazon-ads | Pass | Pass | Pass |
| hyper-cli | Pass | Warn | Pass |
| brand-context | Pass | Pass | Warn |

Twelve Warn verdicts spread across Snyk, Socket and one Gen Agent Trust Hub, and no Fail. The Warns cluster where you would expect them: skills that take user-supplied URLs or text into a scraper or a generator, skills that hold a publish token, and `meta-ads`, which both writes campaigns and reads account data. A Warn on a skill that publishes to a social account is a reason to read the skill body and its file and network references before install, not a reason to skip the whole suite.

The permission surface is the real risk, and it is larger than the markdown suggests. Paid media skills hold OAuth grants for Google Ads, Meta Business, TikTok Marketing, Pinterest, Amazon Ads and LinkedIn, and the same token that reads performance can create a campaign. The README's per-action approval rules are the control that matters here. Turn them on for every write and destructive class before connecting a production ad account, and connect a test account first if the platform allows it.

Two structural notes belong in the open. The tools run on a hosted third-party endpoint (`backend.hyperfx.ai`), so account data, creative briefs and scraped competitor data leave your machine and land in a vendor's service; the README does not describe a self-hosted path. And the MIT licence at the repository root covers the skill text, not the MCP service, which has its own terms and billing.

## Limitations

- Snapshot data, verified 2026-11-09: 4,193 combined installs across 20 indexed listings; 112 GitHub stars; MIT; last pushed 2026-11-10. Counts drift over time.
- The skills.sh source page renders at most 20 listings, while the repository carries 30 SKILL.md files. Ten skills have no published install count, so the table understates the suite and any comparison against it leans on a two-thirds sample.
- The install counts sit between 159 and 274 with no functional grouping behind them. A narrow spread on a young repository means the ordering says nothing about which skill is better built.
- Nothing here runs standalone. Every skill names tools on the Hyper MCP, and most name a specific integration (Google Ads, Meta Business, TikTok Marketing, Pinterest, Amazon Ads, Apify, Firecrawl, Klaviyo, GA4). Without the endpoint and the credentials, the skills describe work rather than perform it.
- The README's install comment says "install all 24" while the tree holds 30 SKILL.md files and the README's own skills table lists 30 rows. Treat the tree as the source of truth and do not read 24 as a scope statement.
- The repository's last push reads 2026-11-10 in UTC, which is the evening of 2026-11-09 in US Mountain time. The snapshot date follows the sweep clock, so the two dates differ by a timezone boundary rather than by a future commit.

## Related

- [Aaron Marketing Skills - Full Marketing Department Setup](/hermes/skills/catalog/aaron-marketing-skills-setup)
- [ClawFu Skills - 175 Marketing Methodologies for AI Agents Setup](/hermes/skills/catalog/clawfu-skills-setup)
- [Digital Marketing Pro - AI Marketing OS Setup](/hermes/skills/catalog/digital-marketing-pro-setup)

## Pro Tips

- Start with `brand-context` and write the file before anything else. Every sibling skill reads it, and a half-filled context file shows up later as generic ad copy that ignores the actual customer language.
- Install by name, not with `--all`, unless you really want 30 skills in the context window. `npx skills add hyperfx-ai/marketing-skills --skill google-ads` keeps the tool surface small and the routing obvious.
- Read the required-integration column in the README before promising a demo. `meta-ads` wants Meta Business plus Firecrawl, `competitor-intel` wants Firecrawl plus HyperSEO or an Apify scraper, and `cold-email-outreach` wants Gmail plus Apollo. A missing integration is the most common reason a marketing skill looks broken.
- Keep approval rules on for every write class and rehearse on a paused campaign. The skills are built to build-then-pause, so the human step is part of the designed flow rather than an interruption.
- When a skill names a tool you do not recognise, run `describe` on it before calling it. The canonical name resolves on chat, MCP client and CLI, and the access class returned by `describe` tells you whether the call is read, write or destructive.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
