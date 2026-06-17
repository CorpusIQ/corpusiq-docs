# Error codes & troubleshooting reference

When something goes wrong, CorpusIQ or a vendor returns an error code or message. This page maps those errors to causes and fixes.

## CorpusIQ errors

### Authentication & token errors

| Error | Cause | Fix |
|-------|-------|-----|
| `401 Unauthorized: Token invalid` | Connector token expired or was revoked. | Disconnect the connector and reconnect. CorpusIQ will fetch a fresh token. |
| `401 Unauthorized: Token revoked by vendor` | The vendor (Google, Shopify) or an admin removed the app from their connected apps panel. | Disconnect from CorpusIQ, then reconnect. |
| `403 Forbidden: Insufficient scopes` | The token was granted but some permission scopes were unchecked during OAuth. | Disconnect, reconnect, and leave all scopes checked during the consent screen. |
| `403 Forbidden: Admin approval required` | Your workspace admin has blocked third-party apps. | Ask your IT/workspace admin to pre-approve "CorpusIQ" in your org's admin console (Google Workspace, Microsoft 365, Shopify Plus). |
| `MFA/2FA prompt not handled` | You enabled MFA on your account after connecting, or the OAuth flow timed out during 2FA verification. | Use an incognito browser, disconnect, then reconnect while keeping only the right account logged in. |

### Data & query errors

| Error | Cause | Fix |
|-------|-------|-----|
| `404 Not Found: Resource doesn't exist` | The query asked for data that doesn't exist (e.g., Shopify order #999 that was never placed). | Verify the ID or date range in your question. Ask CorpusIQ to "show the data sources" so you see what's actually there. |
| `Empty results / No data returned` | Either (a) the connector is authenticated but has no data, or (b) the query is valid but returned zero matches. | See [connector-shows-no-data.md](connector-shows-no-data.md). Start by asking a simple question like "Show me my account info" to verify the connector works. |
| `Type mismatch in results` | The connector returned a different data type than expected (e.g., a date field as a string). | Usually transparent to users; CorpusIQ handles conversion. If the answer looks wrong, ask "Show me the raw data." |
| `Permission denied on query` | A permission scope was unchecked, or the vendor account doesn't have access to the resource. | See [connector-auth-failed.md](connector-auth-failed.md), Cause 2 (unchecked scopes). Or verify the account you're querying actually has admin access to the data you're asking for. |

### Rate limit & quota errors

| Error | Cause | Fix |
|-------|-------|-----|
| `429 Too Many Requests: Rate limit exceeded` | The vendor (Google, Shopify, Klaviyo) is blocking requests because you've hit their rate limit. | Wait 60 seconds, then retry. For frequent queries, break them into smaller date ranges or filter by account/product subset. See [../how-it-works/rate-limits-and-quotas.md](../how-it-works/rate-limits-and-quotas.md). |
| `quota exceeded` | Your account or the connector has hit a daily/monthly API call quota. | Check the vendor's dashboard for quota status. For example, Google Ads has a 60k calls/day limit. Contact support for guidance on optimizing queries or upgrading. |
| `request throttled` | The vendor is slowly rejecting requests to manage load. | This usually resolves itself. CorpusIQ will retry with backoff. If it persists, try the query at a different time (e.g., off-peak hours). |

### Timeout & performance errors

| Error | Cause | Fix |
|-------|-------|-----|
| `Timeout: Query exceeded 60 seconds` | The vendor was slow to respond or the query involves a large date range or many records. | Try querying a shorter date range (e.g., last week instead of last year). Or ask a more specific question (e.g., "Top 10 products" instead of "All products"). |
| `Timeout: No response from vendor` | The vendor's API was unreachable or offline. | Wait a minute and retry. If this is persistent, the vendor may have an outage. Check their status page. |
| `Partial results: X of Y records returned` | The query hit a record limit and returned a subset. | The data you got is real but not complete. Ask a more specific question or break it into smaller chunks (by date, by product, by region). |

## Vendor-specific errors

### Google (Workspace, Ads, Analytics, Search Console)

| Error | Cause | Fix |
|-------|-------|-----|
| `google_auth_token_invalid` | Your Google account session expired. | Sign in again at google.com, then reconnect the connector in CorpusIQ. |
| `No accounts found` (Google Ads) | The Google user you signed in with has no access to any Ads account. | Go to google.com/ads, click Settings → Access and Security, and add yourself. |
| `login_customer_id required` (Google Ads MCC) | You're using a manager account but didn't specify which client account to query. | See [../connectors/google_ads.md](../connectors/google_ads.md) Troubleshooting section. Add the client customer ID to your query. |
| `Permission denied: read_analytics` | Your Google user doesn't have access to the GA4 property. | Add your account to the GA4 property in Google Analytics → Admin → User management. Requires Editor+ role. |
| `Search Console: Site not verified` | Your site isn't verified in Google Search Console. | Go to search.google.com/search-console, verify ownership, and try again. |

### Shopify

| Error | Cause | Fix |
|-------|-------|-----|
| `Shopify: Invalid API access scope` | The OAuth consent screen was skipped or incomplete. | Disconnect and reconnect; approve all scopes. |
| `Shopify: Admin API is disabled` | Your Shopify admin has blocked custom app access. | Log into Shopify Admin → Settings → Apps and Integrations → App and sales channel settings, and enable "Allow custom app connections." |
| `Shopify: Shop is on Plus plan with custom permissions` | Shopify Plus enforces per-user scope management. | Ask your Shopify admin to grant the "CorpusIQ" app access to Orders, Products, Customers scopes. |
| `Could not connect to Intuit` (if QuickBooks via Shopify sync) | Intuit's OAuth is temporarily rate-limited. | Wait 60 seconds and retry. |

### QuickBooks

| Error | Cause | Fix |
|-------|-------|-----|
| `Wrong company file connected` | You authorized the wrong QuickBooks company during OAuth. | Go to Settings → Connected apps in your Intuit account and revoke CorpusIQ. Disconnect from CorpusIQ, reconnect, and choose the correct company. |
| `No invoice data found` | The QuickBooks company has no invoices yet, or the permission scopes don't include invoices. | Verify the company actually has invoices. Or reconnect and ensure "Invoices" scope is checked. |
| `Numbers don't match my accountant's report` | CorpusIQ is on a different accounting basis (accrual vs. cash) than you expected. | Ask CorpusIQ: "Show me P&L on accrual basis" or "Show me P&L on cash basis." Check your QuickBooks default in Settings. |

### Klaviyo

| Error | Cause | Fix |
|-------|-------|-----|
| `Klaviyo: API key invalid` | The Klaviyo API key was revoked or regenerated. | Go to Klaviyo Account → API Keys, confirm the current key. Disconnect CorpusIQ and reconnect. |
| `List not found` | You asked about a list that was deleted or is in a different workspace. | Go to Klaviyo and verify the list exists. Or ask CorpusIQ: "Show me all my lists." |

### HubSpot

| Error | Cause | Fix |
|-------|-------|-----|
| `HubSpot: Private app scope insufficient` | If using a private app, not all scopes are granted. | Go to HubSpot Settings → Integrations → Private apps, and grant "read" scopes for contacts, deals, pipelines. |
| `Deal not found in pipeline` | The deal was deleted or moved to a different pipeline. | Verify it exists in HubSpot. Ask CorpusIQ: "Show me all deals in [pipeline name]." |

### Meta Ads (Facebook, Instagram)

| Error | Cause | Fix |
|-------|-------|-----|
| `Meta: Account restriction detected` | Your ad account is under review or has spending limits. | Go to facebook.com/business/help and check your ad account status. Revert any violations and wait for review. |
| `Campaign archived` | The campaign you asked about is archived. | Ask about active campaigns, or ask CorpusIQ to "Show me archived campaigns" if needed. |

### Zapier / Make / other connectors

| Error | Cause | Fix |
|-------|-------|-----|
| `Connection timeout` | The vendor's API is slow or offline. | Wait 1 minute and retry. Check the vendor's status page for outages. |
| `Invalid API key or credentials` | The credentials were revoked or incorrect. | Regenerate the API key in the vendor's settings, disconnect from CorpusIQ, and reconnect. |

## Error codes by HTTP status

| HTTP Status | Common Causes | Action |
|-------------|---------------|--------|
| 400 Bad Request | Malformed query, invalid date format, unsupported filter | Check your question for typos or unsupported fields. Ask CorpusIQ: "Show me what fields are available." |
| 401 Unauthorized | Token invalid, expired, revoked | Disconnect and reconnect the connector. |
| 403 Forbidden | Insufficient permissions, scopes unchecked | Reconnect and ensure all scopes are approved. |
| 404 Not Found | Resource doesn't exist (order, product, account) | Verify the resource exists in the vendor's dashboard. Try a broader query. |
| 429 Too Many Requests | Rate limit exceeded | Wait 60 seconds, then retry. Optimize your query for smaller date ranges. |
| 500 Internal Server Error | Vendor's API is broken | Wait a few minutes. If it persists, contact the vendor's support. |
| 503 Service Unavailable | Vendor is down for maintenance | Check the vendor's status page. Retry in a few minutes. |

## How to escalate to support

If your error isn't on this page, gather this info and email support:

1. **Exact error text** (screenshot or copy-paste)
2. **Which connector** (e.g., "Shopify," "Google Ads," "Klaviyo")
3. **What you asked** (your exact question to Claude/ChatGPT)
4. **Timestamp** (when did it happen?)
5. **Connector auth status** (is it showing "Connected" in CorpusIQ?)
6. **Steps to reproduce** (can you make it happen again?)

---

## Powered by CorpusIQ

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
