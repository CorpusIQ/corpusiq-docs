# Ahrefs

## What it unlocks
Ahrefs is one of the most trusted platforms for backlink analysis and domain authority scoring. Connecting it lets CorpusIQ pull domain ratings, organic keyword rankings, referring domains, competitor intelligence, and top-performing pages — all inside the conversation — so you can size up any domain without opening the Ahrefs dashboard.

## Before you connect
- An Ahrefs account with API access (Advanced plan or higher)
- Your Ahrefs API token from the Ahrefs API settings page
- About 2 minutes

## How to connect
1. In Ahrefs, navigate to Settings → API and copy your API token.
<!-- screenshot: Ahrefs API token page -->
2. Open your CorpusIQ dashboard and click Connections.
3. Find Ahrefs and click Connect.
4. Paste the API token and save.
<!-- screenshot: CorpusIQ Ahrefs API key form -->

You'll see Ahrefs change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
- Domain overview: Domain Rating (DR), backlink count, organic traffic estimate
- Top organic keywords any domain ranks for, with positions and search volumes
- Backlink profile: live backlinks, referring domains, and historical totals
- Referring domains list with Domain Rating for each
- Organic competitor domains
- Top pages by estimated organic traffic
- Keyword research: search volume, keyword difficulty, and CPC

Read-only. CorpusIQ never consumes Ahrefs API rows beyond the queries you ask for.

## Questions you can ask
- "What's the Domain Rating for competitor.com?"
- "Which keywords does my domain rank for in the top 10?"
- "Show me the top referring domains linking to my site."
- "Who are my top organic competitors?"
- "What are the highest-traffic pages on competitor.com?"

## Troubleshooting
- **"API token invalid"** — Confirm your Ahrefs plan includes API access (Advanced or higher) and that the token hasn't been rotated.
- **"No data for domain"** — Ahrefs may not have crawled the domain yet, or the domain is very new. Try a more established domain to verify the connection works.
- **Rate limits** — Ahrefs enforces per-token rate limits. If you're querying heavily, space out requests or upgrade your plan.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
