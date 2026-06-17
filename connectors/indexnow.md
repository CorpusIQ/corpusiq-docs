# IndexNow

Automatically notify search engines (Bing, Yandex, Seznam, Naver) the moment your URLs
change — without waiting for a crawler to find them. IndexNow is a push protocol: you submit,
search engines act, discovery lag drops from days to minutes.

CorpusIQ pairs IndexNow with your existing connectors. When a Shopify product goes live, a
blog post publishes, or a docs page updates, CorpusIQ can surface those URLs and hand them
to IndexNow in one step.

## What it unlocks

- **Instant crawl triggers** — submit new/updated/deleted URLs the moment they change
- **Batch submission** — up to 10,000 URLs per POST, mixing http and https
- **Verified ownership** — host a single text file once; search engines cache it
- **Multi-engine reach** — one submission propagates to all IndexNow-compatible engines
- **SEO closed-loop** — combine with Search Console or Semrush to track ranking improvement
  after submission

## Before you connect

- Your website domain (e.g. `www.corpusiq.io`)
- An IndexNow API key — minimum 8 characters, alphanumeric + dashes
  - Generate a key at [indexnow.org](https://www.indexnow.org) or create your own
    random hex string (e.g. `openssl rand -hex 16`)
- Ability to host a `.txt` file at your domain root **or** at a custom path
- About 5 minutes

No account signup required. IndexNow is an open protocol.

## How to connect

### Step 1 — Generate your key

```bash
# Generate a 32-hex-character key (recommended length)
openssl rand -hex 16
# Example output: a3f9b2c1d4e5f678901234abcdef5678
```

### Step 2 — Host the key file

Create a UTF-8 text file named `{your-key}.txt` containing only the key on the first line.

**Option A — Root directory (simplest):**

```
https://www.corpusiq.io/a3f9b2c1d4e5f678901234abcdef5678.txt
```

File contents:
```
a3f9b2c1d4e5f678901234abcdef5678
```

**Option B — Custom path (specify `keyLocation` in each request):**

Place the file anywhere on the same host and include the full URL as `keyLocation` in your
IndexNow requests.

### Step 3 — Verify the file is live

```bash
curl -s https://www.corpusiq.io/a3f9b2c1d4e5f678901234abcdef5678.txt
# Should return the key string
```

### Step 4 — Add credentials to CorpusIQ

1. Open your CorpusIQ dashboard and click Connections.
2. Find IndexNow and click Connect.
3. Enter your domain and API key.
4. Save. CorpusIQ validates the key file before storing.

## How IndexNow works

IndexNow is a one-way push protocol. You call the search engine's endpoint; they crawl your
key file to verify ownership; then they re-index your URL.

**Single URL (GET):**
```
https://api.indexnow.org/indexnow?url=https://www.example.com/page&key=your-key
```

**Batch URLs (POST JSON):**
```json
POST https://api.indexnow.org/indexnow
Content-Type: application/json

{
  "host": "www.example.com",
  "key": "your-key",
  "urlList": [
    "https://www.example.com/page1",
    "https://www.example.com/page2"
  ]
}
```

A `200` response means the engine received your submission. It is not a guarantee of
immediate indexing — it removes the discovery bottleneck.

Supported engines (all reachable via `api.indexnow.org`): Bing, Yandex, Seznam, Naver.

## What CorpusIQ can do with it

| Action | Example prompt |
|--------|----------------|
| Submit a single URL | "Submit https://www.corpusiq.io/blog/new-post to IndexNow" |
| Submit a batch | "IndexNow the 12 Shopify product pages I updated today" |
| Cross-source submit | "Find GA4 pages with zero impressions and submit them to IndexNow" |
| SEO loop | "Submit our new blog posts to IndexNow, then check Search Console in 48h" |

## Questions you can ask

```
Submit https://www.corpusiq.io/changelog to IndexNow so Bing picks it up today.
```

```
I updated 5 product pages on Shopify. Submit them all to IndexNow.
```

```
Which of our pages have never appeared in Search Console? Submit them to IndexNow.
```

```
After submitting to IndexNow, remind me to check Search Console impressions in 2 days.
```

## Troubleshooting

- **HTTP 400** — URL is malformed or not on the declared host. Verify the `host` field
  matches the domain in every URL exactly (including `www` prefix if used).
- **HTTP 403** — Key file not found or content mismatch. Re-check the file is publicly
  accessible and contains only the key string (no trailing spaces or extra lines).
- **HTTP 422** — Too many URLs in one request (max 10,000) or key format invalid
  (must be 8–128 alphanumeric/dash characters).
- **HTTP 429** — Rate limited. IndexNow guidelines allow up to 10,000 URLs/day per domain.
  Spread submissions if you have a large site.
- Key file caching — search engines cache your key file. If you rotate the key, allow
  up to 24 hours for the new file to be picked up before submissions resume.

## Notes

- IndexNow is read-write from the network's perspective (you are pushing to external
  endpoints), but CorpusIQ never writes to your CMS or website.
- Submission acknowledges receipt only — actual re-crawl timing is at the search engine's
  discretion.
- Combine with [Search Console](search-console.md) and [Semrush](semrush.md) to measure
  ranking lift after submission.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
