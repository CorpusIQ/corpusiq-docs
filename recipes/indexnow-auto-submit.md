# Recipe: Auto-submit changed URLs to IndexNow

**Connectors:** indexnow, shopify, ga4, search-console, semrush
**Category:** alerting
**Complexity:** multi-source

---

## Use Case

Every time a product page, blog post, or landing page changes on your site, search engines
need to discover the update. By default they find it during their next crawl — which can take
days. This recipe uses IndexNow to push the updated URL the moment it changes, cutting
discovery lag from days to minutes.

Works across any combination of Shopify (product + collection pages), your blog/docs, or
any URL you name manually. Pairs naturally with Search Console and Semrush to close the loop
on ranking improvement.

Ideal for: ecommerce operators updating product pages frequently, SaaS teams shipping
changelog entries, content teams publishing blog posts on a schedule.

---

## Prerequisites

- CorpusIQ connectors connected: **IndexNow** (required), plus any of:
  **Shopify** (to surface updated product URLs), **GA4** (to find zero-impression pages),
  **Search Console** (to measure post-submission ranking lift)
- IndexNow key file hosted at your domain root (see [IndexNow connector](../connectors/indexnow.md))
- Frequency: on-demand after any content publish/update event, or daily batch

---

## Queries

### 1 — Submit a single updated URL

```
Submit https://www.yoursite.com/blog/post-slug to IndexNow.
```

### 2 — Submit all Shopify products updated today

```
List all Shopify products updated in the last 24 hours and submit their URLs to IndexNow.
```

Expected flow: CorpusIQ queries Shopify for recently modified products, extracts their
canonical URLs, and POSTs them in a single IndexNow batch.

### 3 — Surface unindexed pages and push them

```
Which pages on our site have zero impressions in Search Console over the last 90 days?
Submit the top 20 to IndexNow.
```

Expected flow: Search Console query → filter for zero-impression pages → batch submit to
IndexNow. Useful for pages that have never been crawled.

### 4 — Full SEO closed-loop

```
Step 1: Submit our 5 most recent blog posts to IndexNow.
Step 2: In 48 hours, check Search Console for impression changes on those URLs.
Step 3: If any still have zero impressions, resubmit them.
```

### 5 — Discover low-traffic pages, submit, and track

```
Find all GA4 pages with fewer than 10 sessions in the last 30 days.
Submit them to IndexNow.
Then pull their current Search Console average position.
```

---

## Sample Output

```
IndexNow submission complete.

Host: www.example.com
URLs submitted: 12
Endpoint: https://api.indexnow.org/indexnow
Response: HTTP 200 OK

URLs submitted:
  https://www.example.com/products/widget-pro
  https://www.example.com/products/widget-lite
  https://www.example.com/blog/q2-update
  ... (9 more)

Next step: check Search Console impressions for these URLs in 48 hours.
```

---

## Notes

- IndexNow `HTTP 200` means the engine received your list, not that re-indexing is complete.
  Check Search Console 24–72 hours later for confirmation.
- The same key file is reused across all submissions — no per-request key rotation needed.
- If you see `HTTP 403`, the key file is either unreachable or its contents do not match the
  submitted key. Verify with: `curl -s https://your-domain.com/your-key.txt`
- Maximum 10,000 URLs per POST. For larger batches, CorpusIQ will split into multiple
  requests automatically.
- All submitted URLs must share the same `host` value. Cross-domain batch submission is
  not supported by the protocol.

---

## Variations

- **Scheduled daily batch:** Run this at 11 PM to submit everything published that day.
- **On-publish webhook:** Trigger via Shopify webhook → CorpusIQ API call → IndexNow submit.
- **Deleted page handling:** Submit deleted URLs too — IndexNow notifies engines to deindex.
- **Semrush pair:** After submission, pull Semrush ranking snapshots weekly to measure
  position improvement tied to the IndexNow push.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
