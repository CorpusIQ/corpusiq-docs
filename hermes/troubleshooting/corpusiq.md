# CorpusIQ MCP Troubleshooting

Common issues when connecting CorpusIQ to Hermes Agent.

## "Chat not found" or 401 errors on cron jobs

**Symptom:** Crons that use CorpusIQ fail with 401 or "Chat not found" delivery errors.

**Root cause:** The CorpusIQ JWT token expires after 1 hour. Cron jobs that run infrequently will have an expired token.

**Fix:** Use the token refresh guard before every cron run:

```bash
python3 /path/to/token_refresh_guard.py && hermes run "your cron task"
```

The guard script checks token validity and refreshes if needed.

## "mcpServer not found"

**Symptom:** Hermes reports the CorpusIQ MCP server is not found.

**Fix:** Verify the MCP config entry:

```yaml
mcp_servers:
  corpusiq:
    url: "https://mcp2.corpusiq.io/mcp"
    transport: "streamable-http"
```

Run `hermes mcp list` to verify it's registered.

## OAuth device link expired

**Symptom:** The device auth URL opened in browser says "link expired."

**Fix:** The device auth link is valid for 15 minutes. Run `hermes mcp connect corpusiq` again to get a fresh link. Open immediately.

## Tools not showing up

**Symptom:** CorpusIQ connects but no tools appear.

**Fix:** 
1. Verify you've connected at least one business tool in the CorpusIQ dashboard
2. Tools are dynamically registered — you need an active tool connection
3. Run `hermes mcp tools corpusiq` to see available tools

## "Rate limit exceeded" on GitHub API

**Symptom:** GitHub API calls return 403 with rate limit headers.

**Fix:** 
1. Check current rate: `curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/rate_limit`
2. Rate limit resets at the top of each hour
3. Use authenticated requests — unauthenticated gets 60/hr, authenticated gets 5,000/hr

## Fork restriction (403 on fork)

**Symptom:** `403: "You cannot fork this repository at this time"`

**Root cause:** GitHub anti-automation blocks on accounts that make rapid API calls.

**Fixes:**
1. Wait 1-2 hours — restriction auto-lifts
2. Use a different GitHub account
3. Reduce API call frequency (sub-1/sec)

---

*More help: [github.com/CorpusIQ/corpusiq-docs](https://github.com/CorpusIQ/corpusiq-docs)*
