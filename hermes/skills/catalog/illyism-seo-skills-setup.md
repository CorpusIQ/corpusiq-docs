---
title: "SEO Skills - 30 Workflow SEO Suite Setup"
description: "illyism/seo-skills: 7.8K combined installs across 32 listings, 30 output-first SEO workflows from daily autopilot to GEO citation tracking"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/illyism-seo-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "seo", "geo", "link building"]
---

# SEO Skills - Setup Guide

**Source:** [illyism/seo-skills](https://www.skills.sh/illyism/seo-skills) via skills.sh - 7.8K combined installs across 32 indexed listings; first seen Nov 13, 2026
**GitHub:** 1,186 stars, no licence file reported by GitHub although the README badge claims MIT, `main` branch, last pushed 2026-11-12, 30 `SKILL.md` files in `<category>/<skill-name>/` folders, 41 files in total
**Category:** SEO, GEO and link building workflows that run inside a repository
**Quality Tier:** 🟡 Yellow - 30 in-tree skills and a strong README, but no licence file and one failing trust verdict.

The README opens with the complaint that organises the whole pack: most AI SEO prompt collections produce checklists and health scores that sit in a folder forever. Every skill here is built to end in something shippable, which in a codebase means a diff: rewritten title tags, aligned H1s, refreshed MDX posts, a bot firewall, a verified 301 map, new `/vs/` routes.

The composition model is the strongest part. The README documents six chains, and they read like a real campaign rather than a feature list. Cluster keywords from live SERPs, ground the post in first-hand benchmarks, add real screenshots and charts, strip AI tells, route internal links to money pages, then syndicate. Or: map buyer prompts across five stages, scan live AI answers, write the report, then ship pages for the prompt clusters nobody owns.

Two skills are infrastructure rather than content. `seo-autopilot` runs daily repo SEO with persistent state in `seo/`, checking site health, fact-checking commits and opening reviewable PRs. `block-ai-scrapers` adds a bot firewall that blocks AI coding agents and headless scrapers from burning API credits while leaving Googlebot intact, which is the most unusual skill in the set.

GEO is treated as a first-class discipline, not a renamed version of SEO. `customer-journey` pairs classic keywords with the conversational prompts buyers type, and `aiseotracker`, `ai-seo-report` and `content-coverage` form a scan, report and ship loop against four named assistants plus Google AI Overviews.

## Installation

```bash
# Install all 30 skills
npx skills add Illyism/seo-skills

# Install a single skill, for example daily autonomous repo SEO
npx skills add Illyism/seo-skills --skill seo-autopilot

# List every available skill
npx skills add Illyism/seo-skills --list
```

The README carries a per-agent table as well:

| Environment | Where `SKILL.md` lives | Install |
|---|---|---|
| Claude Code | `.claude/skills/` or `~/.claude/skills/` | `npx skills add Illyism/seo-skills -a claude-code` |
| Cursor | `.cursor/skills/` or `.agents/skills/` | `npx skills add Illyism/seo-skills -a cursor` |
| Codex, OpenCode, Windsurf, Cline, Roo Code | `.agents/skills/` | `npx skills add Illyism/seo-skills` |

For ChatGPT, Claude.ai, Perplexity or Grok the README suggests copying the raw Markdown from the web catalog instead of installing anything.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| seo-autopilot | 735 | Daily end-to-end repo SEO with persistent state in `seo/`: health checks, commit fact-checking, Page 2 to Page 1 pushes, reviewable PRs. |
| seo-title-optimization | 555 | Bulk title tag, MDX frontmatter title and H1 rewrites calibrated against live SERP winners and truncation limits. |
| blog-refresher | 522 | Six-phase refresh that compares a slipping post against the current top ten and rewrites the weak sections. |
| blitz-seo | 514 | A 30-day sprint that concentrates technical fixes, internal links and authority on one money page. |
| customer-journey | 510 | A five-stage buyer map pairing Google keywords with the prompts buyers type into ChatGPT, Claude and Perplexity. |
| blitz-copy | 492 | Landing pages, hero headlines, cold outreach and SERP titles on a hook, spike, payoff structure. |
| understand-customers | 483 | A buyer-psychology brief covering pains, switching triggers, objections and verbatim phrasing before any copy is written. |
| diff-marketing | 480 | Reads recent commits and merged PRs to ship changelog entries, feature articles, launch posts and release emails. |
| intro | 470 | High-retention blog introductions tuned to listicle, how-to, comparison or definition intent. |
| linkdr | 446 | A managed backlink plan with a DR 30 to 60 target mix and an approval-gated checkout link. |
| scribiz | 441 | Transcript, on-screen text, summary and chapters for a video or audio file, then a video-to-post conversion. |
| block-ai-scrapers | 270 | A multi-layer bot firewall that blocks AI agents and scrapers while keeping Googlebot indexing intact. |

The remaining 20 indexed listings range from 1 to 138 installs.

## Why This Matters for Hermes Agents

Most SEO advice an agent produces is unactionable. It says to improve internal linking, tighten title tags and add schema, and then hands the work back to a human who now has a longer list than before.

The distinguishing property here is that the skills edit files. A title rewrite lands as a diff in `app/` or `content/blog/`. A refresh lands as changed MDX. A redirect map lands with a verify script. That makes the output reviewable in a pull request, which is the only review surface most small teams actually use.

The second property is state. `seo-autopilot` keeps its working notes in a `seo/` directory and runs on a schedule, so the agent accumulates a picture of the site instead of starting cold every session. An agent that remembers last month's Page 2 list is a different tool from one that re-audits from scratch.

The GEO chain matters for the same reason SEO did a decade ago. Being cited by an assistant is now a distribution channel, and the skills treat it as measurable: scan the prompts, record who gets cited, write the pages that are missing.

The honest caveat is that the highest-leverage skills need paid data. Ahrefs and DataForSEO credentials are not optional extras for those workflows.

## Usage

| You say | What happens |
|---|---|
| "Run seo-autopilot on this repo and open a PR with today's best fix" | Runs `seo-autopilot`, writes state under `seo/` and returns a reviewable diff. |
| "Diff our top pages against our five competitors and scaffold the biggest gap" | Runs `ahrefs-research` and returns a gap board plus scaffolded routes. |
| "Cluster these 40 keywords by live top-ten URL overlap" | Runs `dataforseo-serp` and writes a cluster file with intent locks. |
| "Refresh this post so it outranks the top three" | Runs `blog-refresher` and rewrites the weak sections against current SERP winners. |
| "Push /pricing from position 14 into the top three in 30 days" | Runs `blitz-seo` and returns the focused sprint plan for that one page. |
| "Which assistants cite us, and for what prompts?" | Runs `aiseotracker` and `ai-seo-report` for the weekly visibility brief. |
| "Our directory data is being scraped by agents and costing us money" | Runs `block-ai-scrapers` and returns the bot firewall with Googlebot exempted. |

## Verification

Probe two skills on the branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/Illyism/seo-skills/main/seo/seo-autopilot/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/Illyism/seo-skills/main/content/unslop-seo/SKILL.md
```

Read the first one in full before installing it. The paths matter too: skills live at `<category>/<skill-name>/SKILL.md` under `seo/`, `content/`, `marketing/` and `copywriting/`, not at `skills/<name>/SKILL.md`, so a verification script pointed at the wrong layout will report a false failure.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| seo-autopilot | Fail | Pass | Warn |
| seo-title-optimization | Pass | Pass | Pass |
| blog-refresher | Pass | Pass | Warn |
| blitz-seo | Pass | Pass | Pass |

`seo-autopilot` is the most installed skill in the pack and the only one with a failing trust verdict plus a Snyk Warn. It is also the skill that runs on a schedule and opens pull requests, so read that file line by line before you put it on a timer. The other 28 listings publish no verdict at all, which is not the same as a pass.

## Limitations

- Snapshot data, verified 2026-11-13: 7,845 combined installs across 32 indexed listings; 1,186 GitHub stars; no licence file reported by GitHub although the README badge claims MIT; last pushed 2026-11-12. Counts drift over time.
- The licence is unresolved and worth treating as unresolved. GitHub reports no licence file, the README badge says MIT, and the README footer repeats it. Those two facts disagree and nothing in the pack settles which one governs reuse.
- `seo-autopilot` carries the pack's only failing verdict. Read its SKILL.md before installing, and do not schedule it against a repo with secrets in the tree.
- Several of the higher-leverage skills need paid credentials. `ahrefs-research` needs Ahrefs MCP or API v3 access, `dataforseo-serp` needs DataForSEO, and `linkdr` is a commercial link service with a checkout at the end. Without those accounts the skills still run, but they run on guesswork.
- SERP data pulled through third-party providers is subject to those providers' terms, including how many queries you may run and whether you may store the results. The skills do not negotiate that for you.
- The install index runs ahead of the tree: 32 indexed listings against 30 `SKILL.md` files, with `extension-store-assets` and `eval` carrying install counts but no resolvable path in the tree snapshot.

## Related

- [Claude SEO - 31-Skill Universal SEO Suite Setup](/hermes/skills/catalog/claude-seo-setup)
- [SEO GEO Claude Skills - SEO & Generative Engine Optimization Suite Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup)
- [SEOJuice Skills - SEO Suite Setup](/hermes/skills/catalog/seojuice-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `seo-title-optimization`, not `seo-autopilot`. It is the lowest-risk skill in the pack, the output is a small diff you can read in a minute, and it tells you whether the agent understands your site before you hand it a schedule.
- Keep the `seo/` directory in version control. That state is the difference between a daily agent and a daily re-audit, and it is also your audit trail for what changed.
- Run `proof-kb` before `unslop-seo`. De-slopping a page with no first-hand facts underneath it just produces different slop.
- Give `block-ai-scrapers` a staging window first. It sits in front of real traffic, and a firewall that accidentally catches a legitimate crawler is expensive to discover on a Monday.
- Treat the `/vs/` and alternatives pages as a quarterly cadence, not a one-off. `vs-and-alternatives` builds them from verified switching triggers, and those triggers move as competitors reprice.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
