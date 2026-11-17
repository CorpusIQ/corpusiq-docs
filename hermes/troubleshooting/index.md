---
title: "Troubleshooting Guide - CorpusIQ Docs"
description: "The six most common CorpusIQ problems and their fixes: connection errors, missing data, authentication failures, and assistants that cannot see your connectors."
canonical: "https://www.corpusiq.io/docs/hermes/troubleshooting/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Troubleshooting Guide

Production agent systems fail in predictable ways. This guide catalogs the most common failure modes across the Hermes stack and provides clear resolution paths.

Each section includes symptoms, diagnosis steps, and fixes - organized from most likely to least likely cause.

## MCP Connection Issues

MCP (Model Context Protocol) servers are the bridge between Hermes and external tools. When they fail, agents lose their capabilities silently.

### Symptom: Agent reports "Tool not available" or "MCP server unreachable"

**Diagnosis:**

```bash
# Check which MCP servers are running
hermes mcp list

# Check specific server health
hermes mcp test corpusiq

# Check if the MCP server process is alive
ps aux | grep mcp
```

**Common causes and fixes:**

| Cause | Diagnosis | Fix |
|---|---|---|
| MCP server process crashed | `hermes mcp list` shows status "offline" | Restart with `hermes gateway restart`, then re-run `hermes mcp test <server>` |
| Port conflict | Server starts then immediately exits | Check `lsof -i :<port>`, change port in config |
| Python dependency conflict | Server fails to import modules | Check `pip list` in the MCP server's venv, resolve conflicts |
| Memory exhaustion | Server runs but times out on requests | Check `htop`, increase swap or reduce concurrent connections |
| Configuration changed | Server starts but tools return errors | `hermes mcp test <server>`, and `hermes mcp configure` to re-check which tools are enabled |

### Symptom: Intermittent tool failures ("sometimes works, sometimes doesn't")

**Diagnosis:**

```bash
# Check MCP server logs for timeout patterns
hermes logs agent -n 100 | grep -i "timeout\|mcp\|error"

# Check network latency to MCP server
ping -c 10 <mcp-server-host>
```

**Common causes:**
- **Network instability:** MCP server on a different node with intermittent connectivity
- **Rate limiting:** External API the MCP server calls is rate-limiting
- **Connection pool exhaustion:** Too many concurrent agent threads exhausting MCP connection pool

**Fix:** Raise the timeouts on that server's own entry in `config.yaml` - `timeout` bounds each tool call and `connect_timeout` bounds the initial connection and the MCP `initialize` handshake. There is no global `mcp_timeout` key; timeouts are per server. Then let transient failures retry with backoff rather than retrying in a tight loop.

### Symptom: Specific tool always fails while others work

This usually means the tool's API credential is expired, its schema changed, or its external service is down.

```bash
# Test the server connection in isolation
hermes mcp test corpusiq

# Check credential status
hermes auth status google_ads
```

## OAuth Token Expiry

Token management is the most common operational issue in autonomous systems. Every external service uses OAuth, and tokens expire.

### Symptom: "401 Unauthorized" or "Authentication required" on previously working tools

**Diagnosis:**

```bash
# Check all connector auth states
hermes connectors list
hermes connectors accounts

# Check when a specific provider credential expires
hermes auth list
hermes auth status <provider>
```

### Token Lifecycle Management

| Stage | Action | Timing |
|---|---|---|
| Token issued | Store refresh token securely | Immediately |
| 80% of TTL | Proactive refresh attempt | ~48h before expiry for most services |
| Token expired | Auto-refresh fails, connector enters degraded mode | Immediately on 401 |
| Refresh token expired | Requires full re-auth | Typically 6 months for Google, varies |
| Re-auth completed | New tokens stored, connector restored | Within minutes if automated |

### Automated Re-Auth

There is no separate token-management config file. Credentials live in `~/.hermes/auth.json` (per-provider entries plus the `credential_pool`), and Hermes refreshes them from that store: an expired access token is refreshed with its refresh token on the next call, and a pool entry that hits a rate limit or auth failure is demoted and cooled down automatically.

To refresh on a schedule instead of waiting for the next failing request, drive the same command from a Hermes cron job:

```bash
hermes auth refresh openrouter      # refresh the pooled credential and clear its cooldown
hermes auth status openrouter       # confirm the new expiry
```

```bash
# cron: refresh the pooled credential before it expires
hermes cron create "0 4 * * *" \
  "Run: hermes auth refresh openrouter. Report only if it fails." \
  --name token-refresh
```

A refresh token that has itself expired cannot be refreshed - that needs a fresh `hermes auth add <provider>` round trip.

### Manual Token Reset

When automated refresh fails, reset the credential path:

```bash
# Clear exhaustion state for a provider's pooled credentials
hermes auth reset <provider>

# Refresh a pooled OAuth credential and clear its cooldown
hermes auth refresh <provider>

# Re-authenticate one OAuth MCP server (or every server with --all)
hermes mcp reauth corpusiq

# This runs the re-auth flow - complete it in the browser
# After re-auth, verify
hermes mcp test corpusiq
```

### Common OAuth Pitfalls

- **Wrong Google account:** OAuth flow defaults to the browser's logged-in account. Use incognito mode for re-auth.
- **Scope changes:** If you added new Google API scopes, existing tokens don't include them. Full re-auth required.
- **Refresh token revocation:** Google revokes refresh tokens after 6 months of non-use. Keep connectors active.
- **Rate limit on token endpoint:** Aggressive refresh can hit OAuth provider rate limits. Space refreshes out.

## Cron Failures

Scheduled processes are critical. When they fail silently, days of content or data can be lost before anyone notices.

### Symptom: Cron job reports success but didn't execute

The most dangerous failure mode. Cron tracks process exit, not outcome.

**Diagnosis:**

```bash
# List recent cron executions with actual output
hermes cron runs --limit 20

# Check a specific job's full execution log
hermes cron runs --limit 5 <job_id>

# Look for jobs that "succeeded" but produced no output
hermes cron runs --limit 50 | grep "status: ok" | grep "output_lines: 0"
```

**Fix:** Every cron job must include an outcome validation step:

```python
# Bad: Just tracks exit code
def my_cron_job():
    result = do_something()
    # If do_something() returned None due to an error it caught,
    # cron sees exit 0 and marks success

# Good: Validates actual output
def my_cron_job():
    result = do_something()
    if not result or not result.get("success"):
        raise CronFailureError("Job produced no valid output")
    return result
```

### Symptom: Job skipped silently

**Causes:**
1. **Concurrency cap:** Another instance of the same job is still running
2. **Rate limit:** The job's external service hit a rate limit and the job backed off
3. **Resource constraint:** Not enough memory/CPU to start the job

**Diagnosis:**

```bash
# Check whether a job is still running
hermes cron status

# Check system resources at scheduled time
journalctl --since "2026-06-16 03:00" --until "2026-06-16 03:05" | grep -i "memory\|oom"

# Check rate limit logs
hermes cron runs --limit 20 <job_id> | grep -i "rate_limit\|backoff"
```

**Fix:** There is no per-job concurrency policy to set. A job that is still mid-run when its next occurrence comes due is refused with "already running" instead of double-firing, so the fix is to make the job finish inside its own period: shrink the work, raise the interval, or move long work to a `--script` job that exits fast. Confirm the overlap in the run history before changing anything:

```bash
hermes cron runs --limit 20 <job_id>     # look for back-to-back runs with no gap
hermes cron edit <job_id>                # widen the schedule if runs are colliding
```

### Symptom: Upstream dependency failed (context_from chain broken)

Jobs that depend on other jobs (`context_from`) fail when the upstream fails.

**Fix:** `context_from` takes one job id or a list of them, nothing else - there is no `primary:`/`fallback:`/`max_staleness_hours:` mapping. List the upstream jobs in priority order so the second one covers when the first has no output, and check the upstream job's own state before blaming the chain:

```text
context_from: ["daily_data_sync", "daily_data_sync_cached"]
```

Outputs are concatenated in the order listed, silent ticks and empty outputs are skipped when the context is assembled, and error documents stay eligible so the next run still gets recovery context. If the upstream really is stale, `hermes cron runs --limit 5 <job_id>` reports `last_error` / `last_fire_error` for it - fix that job rather than teaching the consumer to guess.

### Cron Monitoring Setup

There is no separate cron monitor config file and no `alert_channel:` key. Jobs live in one flat `~/.hermes/cron/jobs.json` table, so the monitor is itself a cron job - a no-agent script job whose only job is to look at the others:

```bash
# Script is a file under $HERMES_HOME/scripts/, never a command line
hermes cron create "*/15 * * * *" \
  --no-agent \
  --script cron-health.sh \
  --name cron-health \
  --deliver local
```

The script prints nothing while every job's `last_status` is `ok` (empty stdout is a silent tick, so a healthy fleet stays quiet) and prints one line per problem job. A non-zero exit or a timeout raises its own alert, so a broken watchdog cannot fail silently. `hermes cron doctor` runs the built-in consistency checks over the same table, and `--failure-deliver` keeps failure notices pointed at a channel that survives when a job's normal delivery target is broken.

## Browser Automation Failures

Browser automation is inherently fragile. Websites change, CAPTCHAs appear, and network conditions vary.

### Symptom: "Browser executable doesn't exist"

**Diagnosis:** Hermes picks the first Chromium that exists, in this order: `browser.executable_path` in `config.yaml`, the Chromium installed by the package manager, `/etc/hermes/chromium-executable-path` (official Docker image), then a system `chromium` / `chromium-browser` on `PATH`. `agent-browser` is a retired package name that now maps to `chromium`, so a `~/.agent-browser/config.json` from an older install is not read at all.

**Fix:** Install or repair the packaged Chromium, then point at an explicit binary only if you need a different build:

```bash
hermes pm install chromium        # also undoes an earlier --skip-browser choice
npx playwright install-deps chromium   # Debian/Ubuntu system libraries
```

```yaml
# ~/.hermes/config.yaml
browser:
  executable_path: ""     # "" = the packaged Chromium
  chromium_args: ["--no-sandbox", "--disable-dev-shm-usage"]
  headed: false
```

`browser.executable_path` accepts a path or a bare command name. On aarch64 Linux where no packaged build exists, install a system Chromium and leave `executable_path` empty so the `PATH` fallback finds it.

### Symptom: Browser times out on navigation

**Diagnosis:**

```bash
# Check if the target site is reachable
curl -I --max-time 10 https://target-site.com

# Check DNS resolution
nslookup target-site.com
```

**Common causes:**
- **DNS issues on worker node:** Configure fallback DNS (8.8.8.8, 1.1.1.1)
- **Site uses heavy JavaScript:** Increase navigation timeout to 60s
- **Site blocks datacenter IPs:** Use residential proxy or different exit node

**Fix:**

```python
# Configure browser with appropriate timeouts
browser_config = {
    "navigation_timeout": 60000,  # 60 seconds
    "action_timeout": 30000,       # 30 seconds per action
    "wait_until": "networkidle",   # Wait for network to settle
    "retry_on_timeout": true,
    "max_retries": 2
}
```

### Symptom: CAPTCHA or anti-bot detection

**Diagnosis:** Browser screenshot shows CAPTCHA or "unusual traffic" page.

**Prevention strategies (in order of effectiveness):**

1. **Persistent browser profiles:** Use `userDataDir` so the browser has cookies, history, and appears human
2. **Stealth techniques:** Enable Playwright stealth plugin to mask automation signals
3. **Human-like behavior:** Add random delays (500ms-3s) between actions, vary typing speed, scroll naturally
4. **Rotating user agents:** Change user agent periodically to avoid fingerprinting
5. **Residential proxies:** For high-value targets, route through residential IPs

**When CAPTCHA appears:** The task fails and is retried. If CAPTCHA persists across 3 retries, the task is escalated for human review. The browser automation cannot solve CAPTCHAs by design - attempting to would violate most platforms' terms of service.

### Symptom: "Target closed" mid-operation

The page navigated away or closed unexpectedly.

**Fix:** Re-navigate and snapshot before interacting:

```python
def safe_interact(url: str, action: callable):
    for attempt in range(3):
        try:
            page = browser.navigate(url)
            snapshot = browser.snapshot()  # Verify we're on the right page
            return action(page)
        except TargetClosedError:
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)
```

## Model Routing Issues

### Symptom: Wrong model used for task type

**Diagnosis:**

```bash
# Check which model was used for recent tasks
hermes insights --days 7

# Check routing rules
hermes config show
```

**Common routing problems:**

Hermes does not have a task-type routing table: the model is whatever `model.default` / `model.provider` resolve to, a per-job cron pin, or the active fallback chain. That makes every one of these a configuration question, not a rule to add:

| Problem | Cause | Fix |
|---|---|---|
| Premium model for simple classification | The session is running the default model | Set a cheaper default, or pin just that job: `hermes cron edit <job_id> --model <cheap-model>` |
| Lightweight model for complex reasoning | No per-task escalation exists | Switch that conversation with `/model`, or pin a stronger model on the job that needs it |
| Model from the wrong provider | `model.provider` and `model.default` disagree | Run `hermes model` - it writes both keys together |

### Symptom: "Model not found" or provider errors

**Diagnosis:**

```bash
# Verify provider connection
hermes doctor
hermes auth status deepseek
hermes auth status anthropic
hermes auth status openai

# Check rate limit status
hermes usage
```

**Fixes:**

- Provider API key expired → Re-add the credential with `hermes auth add <provider>`, or switch provider with `hermes model`
- Rate limit hit → Implement exponential backoff in router
- Model deprecated → Update to newer model version in config
- Provider outage → Configure fallback provider chain

### Symptom: High token costs

**Diagnosis:**

```bash
# Token and cost breakdown for the last 7 days
hermes insights --days 7

# Same view filtered to one platform
hermes insights --days 7 --source cli
```

**Optimization:**

```bash
# What the last 7 days actually cost, and which sessions drove it
hermes insights --days 7

# Shrink the fixed prompt before a single token is billed
hermes prompt-size
hermes tools disable <toolset>

# Keep the scheduled fleet on a cheap model without touching your chat model
hermes config set cron.model <cheap-model>

# Cheap primary, stronger provider takes over only on failure
hermes fallback add
```

There is no `cost_ceiling_daily` or `routing:` block in a `models.yaml` - a hard spend stop is a provider-side budget on the API key, not a Hermes config key. Hermes itself gives you the per-session cost breakdown, the per-job cron model pin, and the fallback chain.

## Gateway Crashes

The API gateway is the entry point for all agent requests. When it goes down, everything stops.

### Symptom: All requests failing with 502/503

**Diagnosis:**

```bash
# Check gateway process
hermes gateway status

# Check gateway logs
hermes logs gateway -n 50

# Check system resources
free -h
df -h
htop
```

**Common causes and fixes:**

| Cause | Diagnosis | Fix |
|---|---|---|
| Memory exhausted | `free -h` shows 98%+ used | Restart gateway, increase swap, investigate memory leak |
| Disk full | `df -h` shows 100% on any partition | Clean logs (`journalctl --vacuum-size=500M`), remove temp files |
| Port conflict | Another process bound to gateway port | `lsof -i :<port>`, kill conflicting process, restart gateway |
| Config parse error | Gateway fails to start after config change | `hermes config check`, revert last change |
| Upstream LLM provider down | Gateway can't reach any model provider | Check provider status pages, enable degraded mode with local models |

### Symptom: Gateway running but requests hang

**Diagnosis:**

```bash
# Check active connections
ss -tunap | grep <gateway_port>

# Check for hung threads on the Python gateway process
py-spy dump --pid $(pgrep -f "hermes gateway")
```

**Common causes:**
- **Connection pool exhaustion:** All connections to an upstream service are in use
- **Deadlock in model router:** Two requests waiting on each other
- **Blocked event loop:** A synchronous tool call holding the loop, starving every other request

**Fix:** Restart the gateway with `hermes gateway restart`. For recurring issues, tune connection pool size and move blocking work off the event loop.

### Gateway Recovery Procedure

```bash
# 1. Check what's wrong
hermes gateway status
hermes logs gateway -n 50

# 2. First try a graceful ensure (starts the local runtime if it is down)
hermes gateway ensure

# 3. If ensure fails, hard restart
hermes gateway restart

# 4. Verify recovery
curl -f http://localhost:<gateway_port>/health

# 5. Check all downstream services recovered
hermes status --full

# 6. Re-run the affected cron job
hermes cron run <job_id>
```

## SSH & Worker Node Connectivity

### Symptom: "Connection refused" to worker node

```bash
# Check if SSH is running on the worker
ssh user@worker-node.local "echo 'SSH is alive'"

# If not, check worker node status
ping worker-node.local
```

**Fix path:**
1. If ping works but SSH doesn't → SSH daemon stopped. Restart via out-of-band access (physical, KVM, or management interface).
2. If ping doesn't work → Network issue. Check switch, cables, Wi-Fi, firewall rules.
3. If both fail → Worker node may be powered off. Check power.

### Symptom: "Host key verification failed"

This usually means the worker node was re-imaged or its SSH host key changed.

```bash
# Remove the old host key
ssh-keygen -R worker-node.local

# Accept the new key
ssh user@worker-node.local
```

### Worker Node Health Check

Cron jobs are created through the CLI (or the `cronjob_manage` tool), not by dropping a YAML file into a directory. A worker check is a no-agent script job: the script runs on the worker-facing host and stays silent while everything is healthy.

```bash
hermes cron create "*/5 * * * *" \
  --no-agent \
  --script worker-health.sh \
  --name worker-health \
  --deliver local
```

Put the checks in the script itself (`ssh`, `df`, `free`, browser driver, queue depth) and make it exit non-zero on failure - a non-zero exit or timeout is delivered as an alert, while empty stdout is a silent tick. `--failure-deliver` routes those failure notices to a channel that survives when the job's normal delivery target is down.

## Quick Reference: Recovery Commands

```bash
# Full system health check
hermes status --full

# Restart the messaging gateway
hermes gateway restart

# Check what's consuming resources
hermes status --deep

# View recent errors across all components
hermes logs errors -n 50

# Test the project's build/test/start recipe end to end
hermes verify

# Re-run a failed cron job
hermes cron run <job_id>
```

## When All Else Fails

1. **Check the logs:** `hermes status --full` and `hermes logs errors` give you a system-wide view
2. **Isolate the failure:** Test each component independently
3. **Check for recent changes:** `hermes config check` and a `git diff` of the file at `hermes config path` show what changed
4. **Roll back:** If a config change caused the issue, restore a known-good config (backups come from `hermes backup`, restored with `hermes import`)
5. **Escalate:** Some failures genuinely need human intervention. The system is designed to degrade gracefully - individual features may fail while the core continues operating.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
