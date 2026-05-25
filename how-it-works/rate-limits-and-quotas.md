# Rate limits & quotas

Every connector has constraints. This page maps them so you know what to expect in production and how to optimize queries.

## What you need to know

**Three layers of rate limiting can affect your queries:**

1. **Vendor rate limits** — The underlying API (Shopify, QuickBooks, Google Ads) has per-second or per-day request limits.
2. **CorpusIQ query limits** — How many records can one query return? How long can a query run?
3. **Plan limits** (if applicable) — Some vendors (Shopify Plus, Google Workspace enterprise) enforce stricter limits.

You don't usually hit these limits in normal use. But if you're running large-scale queries or automated dashboards, knowing them helps you avoid surprises.

---

## CorpusIQ-level limits

These apply to all queries, regardless of connector.

| Limit | Value | Notes |
|-------|-------|-------|
| Query timeout | 60 seconds | If a connector doesn't respond in 60s, the query fails. |
| Max result records per query | 10,000 | Queries returning >10k records will be truncated. Ask for specific filters (by date, by product, by status) to get subsets. |
| Concurrent queries per account | No hard limit | CorpusIQ queues requests. If you fire 100 queries simultaneously, they'll run sequentially, but you won't be rate-limited. |
| Refresh token validity | Vendor-dependent, 30–90 days | Tokens are automatically refreshed; you shouldn't see this unless a token is not used for a very long time. |

---

## Vendor rate limits by connector

### E-commerce & Storefronts

#### Shopify

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per second** | 2 req/sec (standard plan); higher on Shopify Plus | Batch requests. If you're hitting this, stagger queries by 500ms. |
| **Daily API call limit** | None; instead, rate-limited by second | Not a concern for typical use. |
| **Historical data retention** | Orders: 6 months (standard); 3 years (Plus) | Ask for recent orders. For older data, you'll get no results. |
| **Result limit per API call** | 250 records | If you need >250 orders, paginate. CorpusIQ handles this automatically. |
| **Webhook limits** | Not applicable (CorpusIQ is read-only) | — |

**Optimization:** Asking "Orders from last 30 days" is much faster than "All orders ever."

#### eBay

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per day** | 5,000 calls/day (standard seller) | Large batch operations may hit this. Break into smaller queries by date or item. |
| **Concurrent requests** | 2 simultaneous | Run queries sequentially, not in parallel. |
| **Historical data** | Last 90 days for some endpoints | Ask for recent activity. |

**Optimization:** Don't ask "Show me all my sales ever." Ask "Show me sales from the last 30 days."

#### Amazon Seller

| Limit | Value | Strategy |
|-------|-------|----------|
| **API call rate** | 1 req/sec (orders); 0.1 req/sec (inventory) | CorpusIQ respects this. Expect inventory queries to be slower. |
| **Daily request limit** | 50k calls/day (varies by operation) | Unlikely to hit in normal use. If you do, reach out to Amazon support. |

#### GunBroker

| Limit | Value | Strategy |
|-------|-------|----------|
| **Listing data** | Real-time | No delay; queries run instantly. |
| **Sales history** | Last 1 year | Older sales aren't available. |

---

### Financial & Accounting

#### QuickBooks Online

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per minute** | 120 requests/minute | Very generous. Unlikely to hit. |
| **Query complexity** | No explicit limit | Large date ranges and complex filters are fine. |
| **Historical data** | Full history (all years) | No retention limit. |
| **Batch operations** | Not applicable (read-only) | — |

**Optimization:** QuickBooks is very fast. No special optimization needed.

#### Stripe (if accessed via QuickBooks or database)

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per second** | 100 req/sec | Very high. No concern for CorpusIQ use. |
| **Data retention** | Full history | No limit. |

---

### Advertising Platforms

#### Google Ads

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per day** | 60,000 calls/day | Significant. For large accounts with hundreds of keywords/campaigns, you may approach this. |
| **Queries per second** | No explicit per-second limit; batched. | CorpusIQ queues requests. |
| **MCC (Manager Account)** | 60,000 calls/day per manager account | If you manage 100 client accounts, you have 60k across all of them, not per client. Plan accordingly. |
| **Historical data** | Last 2 years | Can't query pre-2022 data. |
| **Keyword/campaign count** | No limit | You can have thousands. CorpusIQ handles pagination. |

**Optimization:** 
- If you have >500 active keywords, don't ask "All keywords." Ask "Top 50 keywords by spend" or "Keywords with <5% CTR."
- Asking for daily breakdowns ("Sales by day last month") costs more API calls than "Total sales last month." Reserve daily breakdowns for important analyses.

#### Meta Ads (Facebook, Instagram)

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per day** | 120 calls/min (standard); higher for large accounts | Reasonable. You can fire 2 calls/sec. |
| **Concurrent requests** | No explicit limit | Queue requests. |
| **Historical data** | Last 28 days (most endpoints) | Can't query campaigns from 2 months ago. |
| **Conversion data latency** | 6–12 hours | Data is not real-time. Yesterday's conversions may not be visible yet. |

**Optimization:** 
- Don't ask "All campaigns ever." Ask "Active campaigns from the last 28 days."
- Expect conversion data to be 1 day behind.

#### TikTok Ads

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per day** | 1,000 calls/day (varies by tier) | Tighter than Google or Meta. Don't fire hundreds of queries in rapid succession. |
| **Rate limiting** | 429 status if exceeded | CorpusIQ retries automatically. |
| **Historical data** | Last 90 days | Can't query older campaigns. |

**Optimization:** Batch your queries. Ask 1 question per hour rather than 10 questions per minute.

---

### Analytics & SEO

#### Google Analytics 4 (GA4)

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per day** | 50,000 requests/day per property | High. Won't hit this. |
| **Rows per report** | 100,000 rows | Asking for "All page paths ever" will return the top 100k. Use filters for specific sections. |
| **Unique values (dimensions)** | 10 million+ | Not a concern. |
| **Real-time data** | 30-minute delay typical | Real-time visitor count is available, but conversion data has a ~30 min lag. |

**Optimization:** 
- GA4 is very fast. No special optimization needed.
- If you need a breakdown by hundreds of dimensions (e.g., traffic by city, device, browser, source), you might hit row limits. Ask for top 50 or top 100 instead.

#### Google Search Console

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per second** | 10 req/sec | High. No concern. |
| **Data retention** | Last 16 months | Can't query older than 16 months. |
| **Pages indexed** | No limit | You can have millions. |

**Optimization:** Search Console is very fast.

#### Semrush

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per subscription** | Depends on plan (100–100k calls/month) | Check your Semrush plan. If you hit limits, upgrade. |
| **Rate limiting** | 10 req/sec | Fast. No concern. |
| **Data freshness** | 1–2 weeks | Keyword data is not real-time. |

**Optimization:** Don't run Semrush reports daily. Weekly or monthly is typical.

#### YouTube

| Limit | Value | Strategy |
|-------|-------|----------|
| **API quota** | 1,000,000 units/day | Very high. Won't hit. |
| **Concurrent requests** | No explicit limit | Queue requests. |
| **Search limit** | 20 results per search | Pagination handled by CorpusIQ. |

**Optimization:** YouTube is fast and generous.

---

### Email & SMS Marketing

#### Klaviyo

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per second** | 3 req/sec (standard); 10 req/sec (Plus) | Moderate. If you're hitting this, space out queries by 300–500ms. |
| **List size** | No limit | Can have lists with millions of subscribers. |
| **Historical data** | Full history | No retention limit. |

**Optimization:** Klaviyo is fast. No special tuning needed for typical use.

#### Mailchimp

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per second** | 10 req/sec | High. No concern. |
| **Historical data** | Full history | No retention limit. |

**Optimization:** Mailchimp is fast.

#### Constant Contact & ActiveCampaign

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per second** | 10–20 req/sec (varies) | High. No concern. |
| **Historical data** | Full history | No retention limit. |

---

### CRM & Pipeline

#### HubSpot

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per second** | 10 req/sec | High. No concern. |
| **Contacts limit** | No explicit limit | Can query millions. CorpusIQ paginates automatically. |
| **Historical data** | Full history | No retention limit. |

**Optimization:** HubSpot is generous. No tuning needed.

#### LeadConnector / GoHighLevel

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per second** | 5 req/sec (standard) | Moderate. Stagger queries if needed. |
| **Contacts limit** | No explicit limit | Paginated. |

---

### Productivity & Files

#### Google Workspace (Gmail, Drive, Calendar, Sheets)

| Limit | Value | Strategy |
|-------|-------|----------|
| **Gmail API** | 1M emails/day (standard); higher for enterprise | Won't hit. |
| **Drive API** | 1M files/day listed | Won't hit. |
| **Sheets API** | 300 read/write requests/min per project | Reasonable. |
| **Calendar API** | 1M events/day per calendar | Won't hit. |

**Optimization:** Google Workspace connectors are fast. No special tuning.

#### Microsoft 365 (Outlook, OneDrive, Calendar)

| Limit | Value | Strategy |
|-------|-------|----------|
| **Microsoft Graph API** | 1,000 requests/minute per tenant | Very high. Won't hit. |
| **Email API** | 1M messages/day | Won't hit. |

**Optimization:** Microsoft 365 is fast.

#### Slack

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per second** | 1 req/sec (standard); higher for enterprise | Moderate. Stagger if needed. |
| **Message history** | Last 90 days (free tier); full history (paid) | On free tier, can't search older messages. |
| **File uploads/retention** | Not applicable (read-only) | — |

**Optimization:** Space out queries on free tier Slack workspaces if you're hitting rate limits.

#### Dropbox

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per second** | 2–10 req/sec (varies) | Moderate. |
| **File listing** | No limit | Pagination handled. |

#### Monday.com

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per month** | Complexity-based rate limiting (not per-call) | Query complexity matters more than count. Aggressive queries use more "points." |
| **Board size** | No explicit limit | Can have thousands of items. Paginated. |

**Optimization:** Keep queries reasonably scoped. Don't ask for "All fields on all 100k items." Filter by date or status.

#### Airtable

| Limit | Value | Strategy |
|-------|-------|----------|
| **API calls per second** | 5 req/sec (standard); higher (enterprise) | Moderate. Stagger if needed. |
| **Record limit per view** | 100k visible; paginated by CorpusIQ | No concern. |

---

### Databases (PostgreSQL, MSSQL, MongoDB, Cosmos DB)

These are self-hosted or your own cloud accounts, so rate limits depend on your infrastructure.

| Database | Rate Limit | Strategy |
|----------|-----------|----------|
| **PostgreSQL** | Self-hosted; depends on your server | Optimize queries. Large SELECTs on 100M+ row tables will be slow. |
| **MSSQL** | Self-hosted; depends on your server | Same as PostgreSQL. |
| **MongoDB** | Cloud-dependent (Atlas) | Atlas M0 (free) is slow; M10+ is reasonable. |
| **Azure Cosmos DB** | RUs (Request Units) per sec | Monitor your RU consumption. Large queries cost more. Scale up if needed. |

**Optimization:** Write efficient SQL. Avoid SELECT *. Use indexes on heavily queried columns.

---

## Tips for avoiding rate limit errors

### 1. Check the error code first

If you see `429 Too Many Requests`, a vendor rate limit was hit. See [troubleshooting/error-codes-reference.md](troubleshooting/error-codes-reference.md).

### 2. Narrow your query scope

Instead of:
> "Show me all orders from the past 10 years"

Ask:
> "Show me orders from the past 30 days"

### 3. Filter early

Instead of:
> "Get all products, then show me only the top 10 by revenue"

Ask:
> "Top 10 products by revenue"

### 4. Batch large analyses

If you're running a daily dashboard across 100 questions:
- Spread them out over time (don't fire all 100 at once)
- Refresh the most important questions more frequently
- Refresh lower-priority questions once a week

### 5. Stagger concurrent queries

Don't fire 50 queries in parallel. Fire 5, wait for them, then fire the next 5.

### 6. Check your vendor plan

Some vendors tier limits by plan (e.g., Shopify Plus has higher API limits). Verify you're on a plan that supports your use case.

### 7. Reach out to support

If you consistently hit rate limits on a connector, email support with:
- Which connector
- How many queries/day
- Typical query type (e.g., "5 years of order history")
- Your vendor plan/tier

CorpusIQ may be able to optimize the connector or advise on query strategy.

---

## Data freshness & latency

Knowing how old the data is matters when interpreting results.

| Connector | Data Latency | Notes |
|-----------|--------------|-------|
| **Shopify** | 1–2 minutes | Real-time. Orders visible immediately. |
| **QuickBooks** | 5–10 minutes | Small lag. AP/AR visible within a few minutes. |
| **Stripe** | Instant | Real-time via Stripe API. |
| **Google Ads** | 3–6 hours | Not real-time. Yesterday's spend visible by morning. |
| **Meta Ads** | 6–12 hours | Conversions lag significantly. |
| **GA4** | 24–48 hours | Standard. "Today's data" is usually yesterday's data. |
| **Search Console** | 16 months | Data refreshed weekly, not real-time. |
| **Klaviyo** | 1–5 minutes | Near real-time. |
| **HubSpot** | 1–2 minutes | Near real-time. |
| **Gmail / Outlook** | Instant | Real-time. |

**Implication:** Don't ask "What's my conversion rate today?" if you have Meta or GA4 as the source. Ask about yesterday.

---

## FAQ

**Q: Can I increase my rate limits?**  
A: Vendor rate limits are set by them. Upgrading to a higher plan tier usually increases limits (e.g., Shopify Plus, Google Ads higher spend, Klaviyo Plus). Check with the vendor.

**Q: What if I hit a rate limit mid-query?**  
A: CorpusIQ retries automatically with exponential backoff (1s, 2s, 4s, etc.). If retries exhaust, the query fails. You'll see a `429 Too Many Requests` error. Wait a minute and retry.

**Q: Do I use up my vendor API quota just by authenticating a connector?**  
A: No. Authenticating uses only the OAuth handshake (one call). Actual API quota consumption only happens when you ask a question.

**Q: Can I see my API usage / quota remaining?**  
A: Yes, in most vendor dashboards (Google, Shopify, etc.). CorpusIQ doesn't expose a unified quota view, but you can check your vendor dashboard. If you need a formal report, email support.

**Q: If I hit a rate limit, will future queries be slow?**  
A: No. Each query is independent. If one query hits a rate limit, it fails or is delayed. The next query resets.

---

**Powered by CorpusIQ**
