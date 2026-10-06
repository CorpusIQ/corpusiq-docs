---
title: "IndexLinks MCP - Page Submission and Crawl Receipts"
description: "Send new pages to search engines and AI crawlers, check how they see a site and read verified crawl receipts from your assistant."
category: SEO
stars: n/a (new listing)
added: 2026-10-06
source: "mcpservers.org /all"
relevance: ★★
tags: [seo, indexing, crawlers, indexnow, search-console, bing, remote-mcp]
---

# IndexLinks MCP

**Remote MCP server (Streamable HTTP, OAuth)** - indexing as a workflow, with receipts. IndexLinks pushes new and updated pages to Bing, Yandex, Naver, Seznam and Yep through IndexNow, to Google through Search Console, to Baidu through its push API, and to an AI crawler network; then it shows the exact minute each verified crawler visited each page. The connector puts check, send and prove in the chat.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (no API key to paste)
Endpoint: https://mcp.indexlinks.app/mcp
Tools: 12 (site checks, submission, receipts, setup)
Pricing: Solo $49/mo (1 site, 1,000 pages), Studio $299/mo (unlimited sites); 24-hour crawl guarantee
Built by: IndexLinks
```

## Why This Matters for Operators

"Published" and "findable" are different states, and the gap is where launches go to die: Google says "Discovered, currently not indexed" for weeks, and AI assistants can only recommend pages their crawlers have read. Classic tools say "submitted" and leave you guessing whether a crawler ever came.

**IndexLinks sells proof instead of a green badge: every verified crawler visit, with the time, per page.** The 24-hour crawl guarantee is concrete - if no verified search or AI crawler fetches a submitted page within 24 hours, that page does not count against the plan. The site check reads robots.txt rules for each named crawler (GPTBot, ClaudeBot, PerplexityBot), noindex, canonical, speed, structured data and llms.txt, with fixes; the receipt list answers "did GPTBot visit my pricing page" with a timestamp.

For agencies the reporting angle is the point: a per-site receipt you can forward to a client beats a screenshot of a dashboard. Everything runs through official channels - IndexNow, Search Console, Baidu's push API, an editorial discovery page - no link schemes and no fake traffic, and the connector asks before it sends because sends use your allowance and cannot be undone.

## Tools & Capabilities

| Tool | What it does | Type |
|---|---|---|
| `check_site` | Check how search engines and AI crawlers see any website or page | Read |
| `list_websites` / `add_website` / `get_website_setup` | List, add and get the setup checklist for a site (key file, Search Console, Cloudflare) | Read / Write |
| `verify_website` / `install_key_file` | Verify the IndexNow key file; host it via connected Cloudflare | Write |
| `link_search_console` / `set_baidu_token` | Link a GSC property; save the Baidu push token | Write |
| `submit_pages` | Send pages to the search engines and AI crawlers (uses your monthly allowance) | Sends to engines |
| `list_pages` / `get_page_status` | Tracked pages with per-engine delivery status; verified crawler visits for one page | Read |
| `request_feature` | Send feedback to the IndexLinks team, only when you ask | Write |

## Installation

```bash
claude mcp add --transport http indexlinks https://mcp.indexlinks.app/mcp
```

In Claude: Settings, Connectors, Add custom connector, name it IndexLinks, paste the URL. In ChatGPT: developer mode, Plugins, Create MCP app with the same URL. Sign-in uses OAuth; there is no key to paste.

## Configuration

An IndexLinks account is required. The site check works on any plan; sending pages uses your plan's monthly allowance. The connector cannot delete websites, change billing or manage API keys.

## Business Relevance

- **Founders and marketers** stop waiting on crawl luck: publish, send, read the receipt.
- **Agencies** push 14 client sites from one place and forward dated receipts instead of screenshots.
- **SEO teams** check robots.txt and AI-crawler access before blaming the index.
- **Content operations** watch the sitemap and send new URLs the moment they publish.

## Integration with CorpusIQ

CorpusIQ's Search Console and GA4 connectors show what happened after pages went live - impressions, clicks, queries, conversions. IndexLinks covers the step before: getting the page seen at all, by search engines and by the AI crawlers that feed assistant answers. Composed, a content team can close the loop from "sent to Bing and GPTBot at 14:07" to "first impressions logged two days later", all from the same conversation, with the UTM discipline carrying attribution into GA4.

## Limitations

- Sending is paid: Solo $49/mo or Studio $299/mo with monthly page allowances; overage billing can be capped.
- Indexing itself is never guaranteed - engines decide; the guarantee covers the verified crawl visit, not the index.
- Receipts depend on the engines and crawlers cooperating with verification.
- Requires an account and, for the full loop, Search Console access (read-only).
- Brand new listing: no track record from this catalog yet.

## FAQ

### Do you guarantee my pages get indexed?

No, and nobody honestly can - Google and the AI engines decide what enters their indexes. The guarantee is on the step most pages get stuck on: a verified crawler visit within 24 hours, or the page's credit returns to your plan.

### Which engines and crawlers are covered?

Bing, Yandex, Seznam, Naver and Yep through IndexNow; Google through Search Console; Baidu through its push API; and GPTBot, ClaudeBot and PerplexityBot through the AI crawler network, with each visit logged.

### Do I need to install anything on my site?

No code. Connect Cloudflare and IndexNow is set up in one click; elsewhere you upload one small key file. Search Console connects read-only.

### How is this different from Search Console's "Request indexing"?

Search Console covers Google only, manually and rate-limited. IndexLinks watches the sitemap and sends every new or changed page to every engine automatically, then shows which crawler visited and when.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Seomely MCP - Google Index Monitoring for Agents](/hermes/mcp/servers/external/seomely-mcp/)
- [LogNorm MCP - Growth Audit and Agent Backlog](/hermes/mcp/servers/external/lognorm-mcp/)
