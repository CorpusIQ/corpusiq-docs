---
title: "NMOS.NET Crawl Analytics MCP - Observed AI Bot Visits"
description: "Read-only crawl telemetry for your own site: which AI and search bots actually arrived, whether llms.txt gets fetched, and where robots conflicts start."
category: SEO
stars: n/a (new listing)
added: 2026-11-04
source: "chatmcp/mcpso issue #6739 (Nov 4, 2026 midday sweep)"
relevance: ★★★
tags: [seo, aeo, geo, ai-crawlers, crawl-analytics, llms-txt, robots-txt, remote-mcp]
last_updated: "2026-11-04"
---

# NMOS.NET Crawl Analytics MCP

**What bots actually did on your site, not what they should have been allowed to do.** NMOS.NET is a cookieless crawler-tracking service: you install a beacon on your own site, it records every search and AI crawler visit, and this MCP server exposes those records to an agent as six read-only tools.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.0 (PKCE S256, dynamic client registration + CIMD)
Endpoint: https://nmos.net/mcp
Tools: list_sites, list_bot_visits, get_crawl_stats,
       get_traffic_overview, get_robots_status, get_site_health
Scope: read-only; the vendor states it does not change site
       settings, tracking or billing
Pricing: Free tier, then $10 to $100 a month, yearly at 10x monthly
Category: SEO / AEO
Built by: NMOS.NET (nmos.net)
```

**Evidence tier: measured 401, no session.** A keyless `initialize` POST to `https://nmos.net/mcp` returned `HTTP 401` with the JSON-RPC body `-32001 Unauthorized. Connect via OAuth or send Authorization: Bearer ***`, so the endpoint is live and gated rather than open. No tool was called and no crawl record was read in this pass. Tool names and scope come from the vendor's own submission; the visitor-facing behaviour described below comes from the vendor's site and its pricing page, and is labelled as such.

## Why This Matters for Operators

Most AI-visibility surfaces in this catalogue measure the **output**: whether a brand appears in an AI answer, or whether a page is structurally legible to a crawler. The entries that do read visits, [IndexLinks](/hermes/mcp/servers/external/indexlinks-mcp/) most directly, prove a crawl for the pages you send to its own submission network, one page at a time, on a plan that starts at **$49** a month and is priced by submitted pages. NMOS.NET takes the other route: install a beacon once and it logs every crawler that reaches any page of the site, including the pages nobody submitted, which is the difference between checking the URLs you remembered and reading the whole log.

That distinction matters because the two failures look identical from the outside and have opposite fixes:

- A page is fetched and the assistant still does not cite it: a content and structure problem.
- A page is never fetched because a robots rule, a WAF rule or a broken redirect stopped the bot: an access problem that no amount of rewriting will fix.

The vendor's own framing is deliberately narrow and worth quoting, because it is the honest limit of the surface: NMOS "shows visit records and policy signals, not search rankings or model training proof". What it claims to answer is concrete:

- **Did Googlebot reach the important pages?** Visits, journeys and sitemap gaps for search crawlers.
- **What are AI bots reading?** AI visit trails plus `llms.txt` coverage, match or miss.
- **Which bots hit errors or policy blocks?** HTTP errors, robots conflicts and spoof risk in one panel.

The spoof check is the part operators underestimate. A crawler log full of requests claiming to be GPTBot is only useful if the requests are actually from OpenAI, and the Pro tier adds reverse-DNS authenticity on top of the user-agent claim.

## Tools & Capabilities

| Tool | Purpose | Plan |
|---|---|---|
| `list_sites` | List the tracked sites on the account, the entry point for every other call | Free includes crawl analysis |
| `list_bot_visits` | Recent crawler visits: which bot, which page, when | Free |
| `get_crawl_stats` | Crawl volume and the top bots over the period | Free |
| `get_traffic_overview` | Traffic summary including referral sources | Starter and up |
| `get_robots_status` | Latest `robots.txt` scan result for the site | Starter and up |
| `get_site_health` | SSL and general health summary | - |

Tool names and their scopes are taken from the vendor's published submission. Because this pass reached a `401`, the exact response shape of each tool is unverified here; an agent should call `list_sites` first and read the payload before trusting any assumed field name.

## How the Data Gets There

The MCP server reads what the tracking method can see, so the install choice decides what an agent can answer. The vendor publishes the trade-off explicitly:

| Method | What it does | Needs JavaScript | Plan |
|---|---|---|---|
| Meta tag | Identifies the site to NMOS (`tid`). Does not block or allow bots. | No | All plans |
| `tracking.js` | Cookieless; logs crawler visits with the richer signal set | Yes | All plans |
| Beacon CSS | Cookieless no-JS fallback ping for basic crawl hits | No | All plans |
| WordPress plugin | Injects meta tag and script from WP admin | Optional | Integrations panel, Pro+ |
| Google Tag Manager | Deploys the snippet through Tag Manager | Yes | Integrations panel, Pro+ |
| Cloudflare Worker | Edge-side capture and beacon routes | No | Integrations panel, Pro+ |

Two operational notes an operator should carry into the install:

- A **meta tag alone identifies the site; it does not record visits.** Any site that installs only the meta tag will produce empty crawl history and the agent will report nothing rather than report a problem.
- The **Cloudflare Worker** route is the one that does not depend on page JavaScript, which makes it the only method that sees bots on a site whose pages are cached, static, or served by an edge that never runs the script.

Recording is cookieless on every plan, and the vendor instructs installers to mention technical data processing (IP, user agent) in the site's privacy notice.

## Installation

```bash
claude mcp add nmos --transport http https://nmos.net/mcp
```

The server uses OAuth 2.0 with PKCE, dynamic client registration and a client ID metadata document, so a supporting client opens a browser sign-in against an NMOS.NET account and stores the session itself. There is no API key to paste.

```json
{
  "mcpServers": {
    "nmos": {
      "type": "http",
      "url": "https://nmos.net/mcp"
    }
  }
}
```

Three setup steps precede any useful call: copy the meta tag and snippet from **Dashboard, My Websites** into the site `<head>`, verify the install, then wait for crawlers to arrive. A freshly installed site has no history, so the first useful answer is a day or more after install.

## Pricing

| Plan | Price | Sites | Monthly crawl visits | Adds |
|---|---|---|---|---|
| Free | $0 | 1 | 100 | Overview and crawl analysis |
| Starter | $10 | 1 | 5,000 | Traffic and referral reports, `robots.txt` checks |
| Pro | $20 | 2 | 25,000 | Bot authenticity (rDNS), `llms.txt` / AI policy, sitemap coverage, crawl-like-a-bot simulation |
| Pro+ | $40 | 5 | 100,000 | Integrations panel (WordPress / GTM / Worker) |
| Ultra | $100 | 20 | 500,000 | High-volume analytics, priority support |
| Enterprise | Contact | Custom | Custom | Custom reports and limits |

Two details change the buying decision. **Crawl quota is counted separately from human traffic**, so a busy site does not spend its bot allowance on visitors. And the features that make the surface interesting to an AEO programme, `llms.txt` coverage, sitemap coverage, bot authenticity and the "crawl like a bot" simulation, all start at **Pro at $20 a month**, not on the free tier.

## Business Relevance

- **Content and SEO leads** get the missing half of an AEO report: which of the pages they wrote were actually fetched, by which crawler, and when the visits stopped.
- **Site owners recovering from an outage or a migration** can separate "the bot never came back" from "the bot came back and got a 403".
- **Agencies** run the same check across client sites from one agent session, since every tool is account-scoped and read-only.
- **Operators running an `llms.txt`** get a match-or-miss signal on whether the file is being fetched at all, which is the difference between a policy document and a policy document that nothing reads.
- **Anyone diagnosing a traffic decline** can rule the access layer out before spending on content, which is usually the more expensive hypothesis to test.

## Integration with CorpusIQ

The crawl log is the input side of a question CorpusIQ already answers from the output side. A useful pairing:

1. Pull the crawl picture: `get_crawl_stats` and `get_bot_visits` for the month, looking for pages with zero AI-bot visits.
2. Pull the business picture for the same pages through CorpusIQ connectors: Search Console clicks and impressions, GA4 sessions, and revenue by landing page.
3. Compare. A page with no crawl visits and no conversions is an access question; a page with crawl visits, impressions, and no conversions is a content and offer question.

CorpusIQ stays read-only and source-cited, and so does this server, which is why the two can be joined in one agent turn without either side writing to the other.

## Limitations

- **Measurement, not control.** NMOS records visits and policy signals; it does not block, allow or change a crawler's access, and it does not report rankings or prove model training.
- **Unverified tool behaviour.** This pass reached a measured `401`, so the six tool names are the vendor's and the response schemas are unconfirmed. Claims about field-level detail are not made here.
- **Installation is a prerequisite, not a step you can skip.** No beacon means no data, and a meta-tag-only install means no visit records at all.
- **The interesting signals are paid.** `llms.txt` coverage, sitemap coverage, rDNS authenticity and the crawl simulation are all Pro and above; the free plan is 1 site and 100 crawls a month, which on a real site is a sample rather than a trend.
- **Small numbers early.** Crawl visits are counted in the hundreds to thousands, not the millions, so a week of data is a signal and a day of data is noise.
- **Privacy work is on the installer.** Cookieless does not mean no processing: IP and user agent are recorded and the vendor asks for a notice update.

## FAQ

### What does this server answer that an AI-visibility tracker does not?

Whether the crawler arrived. Trackers read what an assistant said about you; this reads the visit records that decide what the assistant could have read. The two are complements, and a page that is never fetched cannot be cited no matter how it is written.

### Do I need an account and a beacon on the site?

Yes to both. The MCP server is a read surface over an NMOS.NET account, and the account only holds data for sites where the meta tag and snippet (or the Worker) are installed and verified.

### Which tools are available on the free plan?

`list_sites`, `list_bot_visits` and `get_crawl_stats` cover the free plan's crawl analysis. `get_traffic_overview` and `get_robots_status` start at Starter, and the `llms.txt`, sitemap and authenticity signals start at Pro.

### Can it tell a real GPTBot from an impostor?

On Pro and above the vendor applies reverse-DNS bot authenticity on top of the user agent, which is the standard way to separate a genuine crawler from a scraper wearing its name. Below Pro the log shows the claimed user agent only.

### Does it change anything on the site?

No. The vendor states the server is read-only and does not change site settings, tracking or billing, and the scope of the six tools is listing, reading stats, reading the robots scan and reading health.

### What is the fastest useful question to ask it?

For a site with a week of data: "which pages had zero crawler visits in the last seven days, and which bots returned a non-200". That single answer usually separates an access problem from a content problem before any other work starts.

## See Also

- [IndexLinks MCP - Page Submission and Crawl Receipts](/hermes/mcp/servers/external/indexlinks-mcp/) - the nearest neighbour: per-page crawl receipts for pages sent to its own submission network
- [AI Crawler Index MCP - Robots.txt Control for AI Bots](/hermes/mcp/servers/external/pathwren-ai-crawler-index/) - identifies a crawler by user agent or IP and writes the robots.txt that matches your stance
- [NM Signals MCP - AI Crawler Visibility Audits](/hermes/mcp/servers/external/nm-signals-mcp/) - audits how AI crawlers see a URL on demand
- [AIO.GEO MCP](/hermes/mcp/servers/external/aio-geo-mcp/) - structural AI search readiness, dry-run fixes and rescoring
- [Encited MCP](/hermes/mcp/servers/external/encited-mcp/) - Search Console mining and AI answer-engine visibility
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
