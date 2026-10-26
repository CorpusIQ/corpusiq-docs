---
title: "New Term Radar MCP - New Names Before Keyword Tools"
description: "MIT Python radar that catches new AI model, product and repo names on X, Hugging Face, GitHub and sitemaps before keyword tools list them."
category: SEO
stars: 1218
added: 2026-10-20
source: "mcpservers.org /all page 2 via the r.jina.ai reader proxy (zhuyansen/new-term-radar)"
relevance: ★★★
tags: [seo, keyword-research, trend-detection, ai-search, github, huggingface, reddit, mcp-server, python]
last_updated: "2026-10-20"
---

# New Term Radar MCP

**The names that are starting to surge, caught where they are said first** - a daily radar over X, Hugging Face trending, GitHub breakouts, directory sitemaps, Reddit asks and your own Search Console, then a keyword table that sizes the demand behind each new name and decides whether to build for it.

```
Server type: Local stdio (Python), installed as an extra of the CLI package
Package: new-term-radar 0.4.0 on PyPI (Python 3.10 or newer, MIT)
Install: pip install "new-term-radar[mcp]"
Command: new-term-radar-mcp
Env: AISA_API_KEY, RADAR_CONFIG (absolute path to config.json), RADAR_STATE (absolute path to the state directory)
Repo: github.com/zhuyansen/new-term-radar, default branch main, created 2026-10-12, last push 2026-10-18, 1,218 stars, 436 forks, 2 open issues
Tools: 3 - recent_leads, keyword_table, run_radar
```

## Why This Matters for Operators

Keyword tools read the last step of a trail, not the first. A new name appears in a lab announcement or on a well-followed X account, enters Hugging Face trending, gets a GitHub repo that takes off, then starts showing up in directory sitemaps and in your own Search Console impressions - and only then, days or weeks later, in Google Trends and the tools built on it.

The radar reads steps one through four every day and uses Trends only to check itself. The worked example it was built around is public and checkable: `Niko1221/Strata` was created on 2026-09-24 and had 7,700 stars nine days later. People were searching "niko strata" from 9/26 while no second repo carried the name and no keyword tool listed it. A single repo gaining 800 stars a day is the whole signal, and it costs nothing to watch.

For anyone publishing pages, posts or products around new terms, the difference between the day a name appears and two weeks later is the difference between owning the query and writing the eleventh article about it.

## Tools & Capabilities

| Tool | What it returns | Cost and time |
|---|---|---|
| `recent_leads` | What the radar kept, with review verdicts and the hit rate per signal | free, instant |
| `keyword_table` | The keyword table for names you give it | about $0.05 a name plus $0.09 a call, 40 to 90 seconds a name |
| `run_radar` | One `sources` or `daily` run and its report | paid, minutes. Schedule it in cron or Actions rather than calling it inline |

The eight signals, and what each costs:

| Signal | What it catches | Needs |
|---|---|---|
| X | Names the accounts in your list used for the first time in 60 days | AIsa key, about $0.003 per account per run |
| Hugging Face | Models and Spaces new to the trending top 50, with quantised copies and a model's own demo grouped under the base name | nothing, free |
| GitHub breakout | A repo under 14 days old averaging 200+ stars a day, or +400 since yesterday, plus the search variants people use | nothing, free (a GitHub token raises the rate limit) |
| Sitemaps | Words that several new URLs on a watched site share and its older URLs rarely carried | the sitemaps you list, free |
| New sites | Domains registered and first indexed in the last 90 days that already rank for 20+ keywords | AIsa key, about $0.13 a query, weekly |
| Asks | What people ask for on Reddit across twelve phrasings, turned into the job a person would search | AIsa key, about $0.12 a week |
| Revenue | Products people pay for, from TrustMRR's verified revenue, newest and fastest growing first | TrustMRR key, free at 6 requests weekly |
| Search Console | Queries your site got impressions for for the first time | your own Google token, free |
| Review | Each lead checked in Google Trends 14 days later against its own baseline | AIsa key, about $0.0012 per search variant |

The keyword table is the output worth reading. For each new name it writes the generic search terms behind it - what people do with the new thing, not the brand - sizes each one, checks page one for room, and gives a decision: prioritize, watch, or skip.

## Installation

```bash
pip install "new-term-radar[mcp]"
```

```json
{
  "mcpServers": {
    "new-term-radar": {
      "command": "new-term-radar-mcp",
      "env": {
        "AISA_API_KEY": "...",
        "RADAR_CONFIG": "/absolute/path/to/config.json",
        "RADAR_STATE": "/absolute/path/to/state"
      }
    }
  }
}
```

The same two commands exist on the command line: `python -m radar keywords "name"` and `python -m radar leads`.

## Configuration

`config.json` holds no secrets. The decisions that matter:

- **The X account list.** The X signal is only as good as the list: it will not see a name none of your accounts says. The example config reads 35 accounts three times a day.
- **The sitemaps you watch.** The example watches eight AI tool directories and four MCP and skill directories. A sitemap surge is counted per distinct URL against the site's own baseline, so one page with a long slug cannot fake a wave.
- **Cost ceilings.** `usecases.per_day` caps the keyword table, and `--skip usecases` turns it off. With the example config a month costs about $15, of which roughly $10 is the X reads and $5 is the keyword table.

A GitHub Actions workflow (`.github/workflows/radar.yml`) runs `sources` every 8 hours and `daily` once a day, keeps state in the Actions cache, and writes each report to the run summary. It is off until `RADAR_ENABLED` is set to true.

## Business Relevance

**Publishing cadence without guessing.** The radar answers "what should we write about this week that nobody has covered well" with a dated list of names and the searches behind them, instead of an editorial meeting.

**The generic term is the asset.** The project's own example is the sharpest part: "SynthID Detector" has a short life as a keyword and belongs to Google, while the job it does, "ai image detector" at about 2,500 searches a day, belongs to nobody. The table always carries both rows and marks which is which.

**Reddit asks as a product backlog.** Once a week it reads a dozen "is there an AI tool that" phrasings, keeps the requests and complaints a tool could answer, and writes each one as a search. Most are too specific to have volume yet, which is exactly why they are worth seeing early.

**A review loop, not a claim.** Each lead is re-checked in Trends 14 days later against its own baseline, and the report shows the hit rate per signal. The vendor states plainly that hit rates are not yet published and that any signal should be treated as unproven until your own numbers accumulate.

## Integration with CorpusIQ

This is a research input, not a data source a customer connects - and it maps directly onto how we choose what to publish. The gap it closes in this catalog is real: every SEO entry here reads demand that already exists (rankings, volumes, backlinks, crawl data), and none of them watch for a term before it has a volume series.

Two practical uses: feed `keyword_table` names into the SEO brief queue so a page exists in the first week of a term rather than after a competitor's, and read the 14-day review to decide whether to keep watching a class of signal or drop it.

## Limitations

- **The "new sites" signal is broken upstream.** The vendor's known issues record that AIsa's validation for `post_dataforseo_domains_whois_overview_live` rejects the filter format DataForSEO requires. Use `--skip newsites` until it is fixed.
- **Volumes are estimates, and two-thirds of the table may be one signal.** A generic term's searches come from Google Ads volume moved along its own Trends curve; a name with no volume history is sized against a benchmark keyword. Google Ads volumes run about two months behind.
- **Trends' last two days are not settled.** The code drops them and requires a rise to last two days, but a flat worldwide reading does not prove a term did not move.
- **The paid path is per call.** About $15 a month on the example config, and a run that fails still costs the calls it made.
- **TrustMRR's terms forbid republishing its data.** Use those leads for your own research; do not build public pages from the list.
- **It is eight days old.** Created October 12, 2026, with a fast-growing star count and no published hit rate. Read the code, which is small and MIT, before wiring it into a paid loop.

## FAQ

### Is this a keyword research tool?

Only in its last step. It detects names early from eight public signals and then sizes the demand behind them, which is the complement of a keyword tool: one tells you what people already search, this tells you what they are about to.

### Why not just check Google Trends?

Trends is the fifth step of the trail and it is the one that lags. The project's own measured example caught `Strata` three days ahead of its Trends rise, and it uses Trends afterwards only to score its own accuracy.

### Does it need a paid key to be useful?

Two of the strongest signals are free: Hugging Face trending and GitHub breakouts need nothing, and sitemap surges and Search Console need only what you already have. The AIsa key buys the X reads, Reddit asks and the keyword table's sizing.

### What does it do when a source is down?

It still writes the table and says which part is missing, in a line under it. A thin table is not a quiet day, and the vendor is explicit that you should read those lines before concluding nothing moved.

### Can I run it on a schedule instead of through an agent?

Yes, that is the intended shape. The GitHub Actions workflow runs `sources` every 8 hours and `daily` once a day, or call it from cron and point `RADAR_STATE` at the directory those runs write to, which is what `recent_leads` reads.

## See Also

- [Créavores AEO Audit MCP - Page-Level AEO Scoring](/hermes/mcp/servers/external/creavores-aeo-mcp/)
- [AI Visibility Analytics MCP - Brand Monitoring Across AI Search Engines](/hermes/mcp/servers/external/ai-visibility-analytics)
- [Prognosite MCP - SEO and AEO Intelligence for Publishers](/hermes/mcp/servers/external/prognosite-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
