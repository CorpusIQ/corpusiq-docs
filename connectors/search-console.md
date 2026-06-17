# Google Search Console

## What it unlocks
Google Search Console is the ground truth for how your site performs in Google Search — clicks, impressions, average position, and the queries that drive them. Connecting it lets CorpusIQ pull search performance data and line it up next to GA4 traffic, so you can see exactly which search queries turn into engaged visitors.

## Before you connect
- A Google account that is a verified owner of the Search Console property you want to read
- About 2 minutes

## How to connect
1. In CorpusIQ, open Settings → Connectors and find Google Search Console.
2. Click Connect.
3. Sign in with the Google account that manages your Search Console properties.
4. <!-- screenshot: Google Search Console OAuth consent screen -->
5. Approve read access and you'll be returned to CorpusIQ.

You'll see Google Search Console change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- All verified sites (properties) in your Search Console account
- Search performance data: clicks, impressions, CTR, and average position
- Breakdowns by query, page, country, device, and search type
- Sitemaps: submitted URLs, indexed URLs, and last-submitted dates
- URL inspection: index status, coverage state, mobile usability, and rich results

CorpusIQ never submits sitemaps, requests indexing, or modifies properties.

## Questions you can ask
- "Which search queries drove the most clicks to my site last month?"
- "What's my average position for brand keywords?"
- "Show me pages that dropped in impressions week over week."
- "How many URLs are indexed vs submitted in my sitemap?"
- "Inspect the index status of our new landing page."

## Troubleshooting
- **"No properties found"** — Your Google account isn't a verified owner of any Search Console property. Add your account in Search Console → Settings → Users and Permissions.
- **"Property not available"** — The property may be a Domain property rather than a URL-prefix property. Both are supported; confirm the exact URL in Search Console.
- **Performance data returns zero** — Google Search Console data can lag by 2–3 days. Try a slightly older date range.
- **Inspect URL says "URL is not on property"** — The URL must belong to the property you're querying. Double-check the site URL and the inspection URL match.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
