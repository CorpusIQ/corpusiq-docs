# Research Agent Configuration

## Role Description

The Research Agent is your autonomous market intelligence and competitive analysis engine. It monitors competitors, industry trends, academic literature, patent filings, news sources, and market data to deliver actionable insights — not just raw data dumps. Use it for competitive landscaping, market sizing, technology trend tracking, literature reviews, and strategic intelligence gathering. The agent synthesizes findings into structured briefs with cited sources, confidence levels, and recommended actions.

Unlike a one-off web search, the Research Agent maintains persistent monitoring threads. It watches competitor domains for SEO changes, product launches, pricing updates, and hiring signals. It tracks keywords and topics across news, academic databases, and patent offices. It builds knowledge graphs connecting companies, technologies, and market trends so insights compound over time.

## Recommended Model

**Claude Sonnet 4** or **DeepSeek V3** (with web search) — research demands strong synthesis capabilities and the ability to distinguish signal from noise across diverse sources. Claude's long context window is particularly valuable for literature reviews and multi-source synthesis. For ongoing monitoring and alert classification, **Claude Haiku** is sufficient.

## Key Skills to Load

- `competitive-intel` — Competitor domain monitoring (SEO, traffic, backlinks), product change detection, pricing tracking
- `market-intelligence` — Industry trend analysis, market sizing estimates, TAM/SAM/SOM calculations, funding and M&A tracking
- `literature-review` — Academic and technical paper discovery, summarization, citation graphing, research gap identification
- `news-monitor` — Topic-based news aggregation, sentiment analysis, emerging narrative detection
- `patent-tracking` — Patent filing alerts by company or technology area, IP landscape mapping
- `brief-generator` — Synthesis of multi-source research into structured executive briefs with citations

## MCP Connectors Needed

| Connector | Purpose |
|-----------|---------|
| **Ahrefs / Semrush** | Competitor SEO, traffic, backlink, and keyword monitoring |
| **Google Search Console** | Own-site SEO performance for competitive context |
| **GA4** | Own-site traffic for market share context |
| **YouTube** | Competitor video content, product demos, conference talks |
| **Notion / Airtable** | Research repository, competitive matrices, brief archives |
| **Slack** | Research alerts, brief distribution |
| **Email** | Newsletter monitoring, alert digests |

> **Note:** Web search, news APIs (NewsAPI, GDELT), academic databases (arXiv, Semantic Scholar, PubMed), patent databases (USPTO, WIPO, Google Patents), and financial data (Crunchbase, PitchBook) are accessed via custom skills and API integrations. Configure your API keys and search parameters in your Hermes profile.

## Sample Cron Schedule

```cron
# Competitor website monitoring every 12 hours
0 8,20 * * * hermes skill competitive-intel --competitors config --detect-changes

# Industry news scan every 4 hours during weekdays
0 8,12,16 * * 1-5 hermes skill news-monitor --topics config --format digest

# Weekly market intelligence brief every Monday at 9:00 AM
0 9 * * 1 hermes skill market-intelligence --period last_week --output brief

# Monthly patent landscape update on the 5th
0 8 5 * * hermes skill patent-tracking --companies config --since last_month

# Literature review sweep every Wednesday at 2:00 PM
0 14 * * 3 hermes skill literature-review --topics config --new-since 7d
```

## Quick-Start Command

```bash
hermes agent create research \
  --model claude-sonnet-4 \
  --skills competitive-intel,market-intelligence,literature-review,news-monitor,patent-tracking,brief-generator \
  --connectors ahrefs,semrush,ga4,search_console,youtube,notion,slack \
  --profile research \
  --description "Market intelligence and competitive research agent"
```

## Daily Workflow

The agent starts each day by checking competitor websites for changes — new pages, pricing updates, job postings that signal strategic moves — and posts a digest to the `#research` Slack channel. Throughout the day it monitors news sources for your tracked topics and companies, filtering noise and flagging only relevant developments. On Monday mornings it delivers a comprehensive weekly brief covering market moves, competitor activity, and emerging trends with cited sources and confidence ratings. Mid-week it sweeps academic databases for new papers in your research areas, summarizing key findings and methodology.

## Configuration Notes

Define your competitor list, tracked topics, and research areas in canonical facts. The agent builds persistent monitoring threads — the longer it runs, the better its change detection becomes. Configure which sources to prioritize and which to deprioritize. Set your brief format preferences (executive summary first, detailed analysis, source appendix). Define citation standards.

## Extending

Add `sentiment-tracking` that monitors brand and competitor sentiment across social media and news. Integrate with LinkedIn Sales Navigator for B2B intelligence. Add `technology-radar` for tracking emerging tech trends. Build a `due-diligence` skill for company and market research supporting investment or partnership decisions.
