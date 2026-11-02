---
title: "News Aggregator Skill - Multi-Source News Digest"
description: "cclank/news-aggregator-skill: 6.0K combined installs. One Python skill that pulls 44+ RSS and community sources, with deep fetch and Chinese reports."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/news-aggregator-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "news aggregation", "rss", "research"]
---

# News Aggregator Skill - Setup Guide

**Source:** [cclank/news-aggregator-skill](https://www.skills.sh/cclank/news-aggregator-skill) via skills.sh - 6.0K combined installs across 1 indexed listing; first seen 2026-11-01 (evening sweep)

**GitHub:** [cclank/news-aggregator-skill](https://github.com/cclank/news-aggregator-skill) - 1,317 stars, no license: the repository root has no `LICENSE` file, branch main, last pushed 2026-05-27; one `SKILL.md` at the root, with `instructions/`, `scripts/`, `templates.md`, `requirements.txt` and `user_sources.opml.example` beside it

**Category:** Multi-source news aggregation for agents: 44+ RSS and community sources, deep fetch and briefing presets

**Quality Tier:** 🟡 Yellow - 1,317 stars and one of the broader free news pipelines on skills.sh, but the repository ships no LICENSE file and the single sampled listing carries a Snyk warning

The repository is published by cclank and its README and `SKILL.md` are written in Chinese, which is not decoration: the skill is built to emit Simplified Chinese reports and says so as its first strict rule. What it actually ships is a Python fetch layer plus a formatting contract. `scripts/fetch_news.py` knows about roughly 44 source keys across global tech (Hacker News, Product Hunt, GitHub Trending, V2EX, Lobsters, Dev.to), Chinese business and social (36Kr, Tencent News, WallStreetCN, Weibo hot search), AI papers and newsletters (Hugging Face Daily Papers, arXiv, AIHOT, TLDR AI, Import AI, Ben's Bites, ChinAI, Memia, One Useful Thing, Interconnects), international desks (BBC, The Guardian, Al Jazeera, France 24, and Reuters through a Google News `site:` fallback), essays and podcasts (Paul Graham, Wait But Why, James Clear, Farnam Street, Scott Young, Dan Koe, Lex Fridman, Latent Space, 80,000 Hours), and any RSS or Atom feed the operator adds through OPML.

The workflow is three steps and it is the same for every source. Fetch to JSON, format each item into one report template, then save to `reports/YYYY-MM-DD/<source>_report.md` before displaying anything. Sources can be combined in one call, a keyword filter expands automatically (asking for AI also matches LLM, GPT, Claude, Agent, RAG and DeepSeek), and `--deep` downloads the article body for richer analysis, using Playwright to get past Cloudflare on the sites that block plain requests. Six briefing profiles sit on top of that for morning runs, and the README's menu trigger opens a numbered list of 53 options for operators who would rather reply with a number than write a sentence.

## Installation

The README documents three routes. The Openskills CLI handles path and config sync:

```bash
openskills install git@github.com:cclank/news-aggregator-skill.git
openskills sync
```

The skills CLI adds the repository straight from the URL:

```bash
npx skills add https://github.com/cclank/news-aggregator-skill
```

The third route is a clone into an agent skills directory, which is the one that fits Hermes. The README examples clone into `.claude/skills/news-aggregator-skill`; the same command works against a Hermes profile:

```bash
git clone https://github.com/cclank/news-aggregator-skill.git \
  ~/.hermes/profiles/corpusiq/skills/news-aggregator-skill
cd ~/.hermes/profiles/corpusiq/skills/news-aggregator-skill
pip install -r requirements.txt
playwright install chromium
```

Two dependencies behave differently. `requirements.txt` lists only `requests` and `beautifulsoup4`, while `playwright install chromium` fetches the browser that the Hugging Face Papers and Ben's Bites paths need; skip it and those two sources fail at runtime. The README badge says Python 3.10 or newer and `SKILL.md` says 3.8 or newer, so treat 3.10 as the floor the README tests against.

No API key is needed for any built-in source, which is the point of the pack: the README states there is no third-party key to configure. The only credential surface is optional, and it is a file: copy `user_sources.opml.example` to `user_sources.opml` in the skill folder, or to `~/.config/news-aggregator/user_sources.opml`, add outlines with an `xmlUrl`, and fetch them with `--source user`. Exports from Feedly, Inoreader or NetNewsWire drop straight in.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| news-aggregator-skill | 6,015 | The whole pipeline in one skill: fetch 44+ sources with `scripts/fetch_news.py`, deep-read article bodies, filter by keyword, then format every item into the shared report template and save it under `reports/YYYY-MM-DD/`. |

The single indexed listing clears the 0-install threshold and appears in the table above.

One listing understates the pack. The breadth is inside the one skill: ten Python scripts in `scripts/` (`fetch_news.py`, `daily_briefing.py`, `rss_parser.py`, `fetch_user_feeds.py`, `fetch_generic_playwright.py`, `fetch_hf_papers_playwright.py`, `fetch_bensbites.py`, `process_general_json.py`, `test_all_sources.py`, `debug_hf_detail.py`), six instruction files in `instructions/` for the briefing profiles, a `templates.md` behind the 53-option menu, and `user_sources.opml.example` for custom feeds. skills.sh indexes one name because there is one `SKILL.md`; the surface you install is closer to a small application.

## Why This Matters for Hermes Agents

Most research skills assume a paid search API and a key. This one assumes neither: the sources are public RSS, JSON endpoints and HTML pages, so an agent can run it on a host with no vendor account, and the failure mode is a stale feed rather than an exhausted quota. For a nightly cron that has to produce something every day, that difference decides whether the job runs at all.

The report contract is where the value sits, and it is stricter than most. Time is a mandatory field and must be marked unknown rather than omitted; output may only come from the fetched JSON, with invented items and fabricated causal links forbidden; when a window returns fewer than five items the skill may backfill from a wider range but must mark those items, and international sources are excluded from backfill because their window is a hard 24 hours. The report is written to `reports/YYYY-MM-DD/` before it is shown, so a run leaves an artifact instead of a scroll of chat.

The three-step split also suits an agent's context budget. `fetch_news.py --no-save` prints JSON to stdout and writes nothing, so a Hermes job can fetch, filter in code, and only hand the surviving items to the model. That keeps a broad scan of 44 sources from turning into a 44-source prompt.

The briefing profiles are the practical entry point. `daily_briefing.py --profile finance` runs its own source set and then points the agent at `instructions/briefing_finance.md`, which asks for at least 20 distinct items grouped by macro, sector and crypto, with a market insight that has to name a mechanism rather than a mood. That is a specification an agent can be held to, which is more than most summarisation prompts offer.

## Usage

| You say | What happens |
|---|---|
| "Run today's finance briefing" | daily_briefing.py runs the finance source set, the agent reads `instructions/briefing_finance.md`, and the report lands in `reports/YYYY-MM-DD/` with at least 20 items grouped by macro, sector and crypto. |
| "Grab 5 GitHub trending repos and read their READMEs" | fetch_news.py pulls the `github` source with `--limit 5 --deep`, downloads each repository page, and reports stars and language alongside the summary. |
| "What did Hugging Face publish today" | The `huggingface` source goes through the Playwright fetcher, and each paper gets a deep read rather than a translated abstract. |
| "BBC, Reuters and Al Jazeera from the last 24 hours" | The three keys run in one call and the international rule applies: only items from the last 24 hours, no backfill from older windows, original outlet and link kept. |
| "Hacker News, WallStreetCN and Weibo top ten, merged" | The three keys run comma separated with `--limit 10`, and the merged report keeps the per-source adaptations, such as Weibo's original heat string. |
| "Filter all sources for agent frameworks this week" | fetch_news.py scans `all`, applies the keyword filter with its automatic expansion, and returns only matching items with their source and time intact. |
| "Add the feeds I already follow in Feedly" | You export an OPML file, the skill reads `user_sources.opml`, and `--source user` fetches those feeds like any built-in source. |

## Verification

Probe the three files that matter before installing. All three returned 200 on branch main when this guide was written on 2026-11-01:

```bash
for p in SKILL.md scripts/fetch_news.py scripts/rss_parser.py; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/cclank/news-aggregator-skill/main/$p"
done
```

After the clone and the two install commands, ask the script what it can actually reach. This is the check that catches a renamed source key, and it needs no network round trip to a news site:

```bash
cd ~/.hermes/profiles/corpusiq/skills/news-aggregator-skill
python3 scripts/fetch_news.py --list-sources
```

Then run one cheap real fetch before trusting a briefing profile:

```bash
python3 scripts/fetch_news.py --source hackernews --limit 3 --no-save
```

Expect JSON on stdout and no file written, because `--no-save` suppresses the report directory. A single-source run that returns an empty list is usually a feed that moved, not a broken install.

Two documentation gaps are worth knowing at this point. `SKILL.md` documents `--limit` as defaulting to 15, while `fetch_news.py` defaults it to 10, so pass the flag explicitly when the count matters. `--list-sources` and `--no-save` exist in the script and are absent from the argument table, which is why the check above runs the script rather than quoting its docs.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| news-aggregator-skill | Pass | Pass | Warn |

The licensing position is the first thing to settle, and the repository does not settle it. There is no `LICENSE` file anywhere in the root of the clone, while the README carries an MIT badge and a closing line that says MIT License. A README sentence is not a license grant, so absent a file the default is all rights reserved, and the 1,317 stars do not change that. If you plan to fork it, ship it inside a product or vendor it into a client environment, get the terms in writing first.

The code is a scraper, and one detail deserves reading before you run it. The generic RSS path in `scripts/rss_parser.py` fetches with `requests.get(url, headers=headers, timeout=15, verify=False)`, which turns off TLS certificate verification for everything that goes through it, and it sends a desktop Chrome user agent. The same path retries three times before giving up. Article bodies for `--deep` go through the Playwright fetchers instead, run as subprocesses from `fetch_news.py`, and several of the hard-coded feed URLs are plain `http` rather than `https`. None of that is malicious, and all of it is the kind of thing a Snyk Warn is pointing at: content arriving over an unverified channel lands in a report that an agent will then summarise as fact.

The prompt surface is the other consideration. `--deep` pulls arbitrary page text into the model's context, and the strict rules in `SKILL.md` cover language, mandatory time, no invented items, keyword expansion, backfill marking and saving, but they do not instruct the agent to treat fetched article text as data rather than instructions. If you run deep fetches unattended, add that instruction to the skill or to the calling job, and keep the run pointed at a feed list you chose.

Operationally the blast radius is small. Nothing in the repository executes on clone; there is no install hook, no credential is stored, and the scripts reach only public endpoints. The writes are local: JSON and Markdown under `reports/`, which is where a cron should point its output directory.

## Limitations

- Snapshot data, verified 2026-11-01: 6,015 combined installs across 1 indexed listing; 1,317 GitHub stars; no LICENSE file in the repository root; last pushed 2026-05-27. Counts drift over time.
- The README claims MIT through a badge and a footer, but there is no `LICENSE` file in the root of the clone. Reuse, redistribution and commercial embedding are unresolved until the publisher adds one.
- The one indexed listing is also the only one sampled for security, and it carries a Snyk Warn. There is no broader sample to average, so treat the warning as the whole verdict rather than as an outlier.
- Output language is Simplified Chinese by rule, not by option. `SKILL.md` rule 1 requires every report in Simplified Chinese, so an English briefing means overriding that rule deliberately and checking the result, since source names and headlines arrive in mixed languages.
- The docs drift from the code: `--limit` defaults to 10 rather than the documented 15, `--list-sources` and `--no-save` are undocumented, and the README badge asks for Python 3.10 while `SKILL.md` says 3.8. Only `requests` and `beautifulsoup4` are in `requirements.txt`, and Playwright is a separate install the two hardest sources need.
- The fetchers are HTML scrapes for several sources (36Kr, Weibo, WallStreetCN, Tencent), a Playwright path that works around Cloudflare, and a Reuters source that is really a Google News `site:reuters.com` search. That breaks quietly when a site changes, and the last push was 2026-05-27, about five months before this snapshot. `scripts/test_all_sources.py` exists to check every source at once.

## Related

- [Tavily Research - AI-Powered Deep Research Setup](/hermes/skills/catalog/tavily-research-setup)
- [Firecrawl Skills - Web Scraping, Research & Workflow Suite Setup](/hermes/skills/catalog/firecrawl-skills-setup)
- [AI Research Skills - 100-Skill ML Research Library Setup](/hermes/skills/catalog/ai-research-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `--list-sources` after every update instead of trusting the table in `SKILL.md`. Source keys are the thing that breaks first in a scraper, and the script is the authority.
- Pass `--limit` every time. The documented default and the code's default differ, and a briefing that quietly returns 10 items per source reads as a thin news day rather than a misconfiguration.
- Use `--no-save` for anything an agent will post-process, and let the report be written once, at the end, by the step that produces the final text. Otherwise a cron leaves a folder of half-reports that nobody reads.
- Check one source by hand before a briefing profile. A profile fans out to six sources at once, and a single dead feed is easier to spot in a three item fetch than in a merged 20 item report.
- Treat article text as data in the prompt. Deep fetch brings in whatever the page says, and the pack does not tell the agent to ignore instructions found inside a fetched page, so add that line to the job.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
