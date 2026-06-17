# SEO and content prompts

Powered by **Google Search Console**, **Semrush**, and **YouTube**. Joined
with **GA4** for traffic and **Shopify/QuickBooks** for revenue attribution.

---

### "Which pages lost organic traffic this week?"

**What this does:** Search Console diff — pages where clicks or
impressions dropped most.
**Connectors used:** Search Console.
**Behind the scenes:** `get_search_console_performance` with a
period-over-period framing.
**Sample answer shape:** Pages list with old vs new clicks/impressions
and delta.

---

### "What's my organic revenue?"

**What this does:** Joins Search Console organic traffic to GA4 to
Shopify/QuickBooks revenue. Tells you how much money SEO is actually
making.
**Connectors used:** Search Console, GA4, Shopify or QuickBooks.
**Behind the scenes:** `seo-authority-tracker` skill.
**Sample answer shape:** Organic sessions, organic conversions,
attributed revenue, and top organic landing pages by revenue.

---

### "Find me keyword opportunities I can win quickly."

**What this does:** Striking-distance keywords — ones ranking on page 2
with real impression volume — plus competitor keywords you're missing.
**Connectors used:** Search Console, Semrush (optional).
**Behind the scenes:** `keyword-opportunity-finder` skill.
**Sample answer shape:** Ranked keyword list with current position,
impressions, and recommended content angle per keyword.

---

### "What are my top search queries?"

**What this does:** Search Console queries by clicks.
**Connectors used:** Search Console.
**Behind the scenes:** `get_search_console_performance` grouped by query.
**Sample answer shape:** Query list with clicks, impressions, CTR,
average position.

---

### "Did my Google rankings change this week?"

**What this does:** Position diff across top queries.
**Connectors used:** Search Console.
**Behind the scenes:** `get_search_console_performance` over two
windows.
**Sample answer shape:** Movers list — biggest gains and biggest losses
by position.

---

### "How does my domain compare to my competitors organically?"

**What this does:** Semrush domain comparison.
**Connectors used:** Semrush.
**Behind the scenes:** `get_semrush_domain_overview` +
`get_semrush_competitors`.
**Sample answer shape:** Side-by-side domain metrics — traffic, keyword
count, authority score.

---

### "What keywords are competitors ranking for that I'm not?"

**What this does:** Competitor gap analysis.
**Connectors used:** Semrush.
**Behind the scenes:** `get_semrush_competitors` +
`get_semrush_organic_keywords` per competitor.
**Sample answer shape:** Keyword gap list with competitor positions.

---

### "How's my YouTube channel performing?"

**What this does:** Channel-level YouTube analytics — views,
subscribers, watch time, top videos.
**Connectors used:** YouTube.
**Behind the scenes:** `get_my_youtube_analytics` +
`get_my_youtube_videos`.
**Sample answer shape:** Channel topline plus top-10 videos by views.

---

### "Where are my YouTube viewers coming from geographically?"

**What this does:** Viewer geography breakdown.
**Connectors used:** YouTube.
**Behind the scenes:** `get_my_youtube_geography`.
**Sample answer shape:** Country list with viewer share and watch time.

---

### "Inspect this URL — is it indexed properly?"

**What this does:** Runs Google's URL Inspection API on a specific URL.
**Connectors used:** Search Console.
**Behind the scenes:** `inspect_search_console_url`.
**Sample answer shape:** Index status, coverage state, mobile usability,
last-crawl info.


---
*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*


---
*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
