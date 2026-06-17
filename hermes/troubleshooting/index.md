---
title: Troubleshooting Guide
description: Common failures and fixes — MCP connections, OAuth tokens, cron jobs, browser automation, model routing, gateway crashes
---

# Troubleshooting Guide

Production agent systems fail in predictable ways. This guide catalogs the most common failure modes across the Hermes stack and provides clear resolution paths.

Each section includes symptoms, diagnosis steps, and fixes — organized from most likely to least likely cause.

## MCP Connection Issues

MCP (Model Context Protocol) servers are the bridge between Hermes and external tools. When they fail, agents lose their capabilities silently.

### Symptom: Agent reports "Tool not available" or "MCP server unreachable"

**Diagnosis:**

```bash
# Check which MCP servers are running
hermes mcp list

# Check specific server health
hermes mcp health corpusiq

# Check if the MCP server process is alive
ps aux | grep mcp
```

**Common causes and fixes:**

| Cause | Diagnosis | Fix |
|---|---|---|
| MCP server process crashed | `hermes mcp list` shows status "offline" | `hermes mcp restart <server>` or restart via systemd |
| Port conflict | Server starts then immediately exits | Check `lsof -i :<port>`, change port in config |
| Python dependency conflict | Server fails to import modules | Check `pip list` in the MCP server's venv, resolve conflicts |
| Memory exhaustion | Server runs but times out on requests | Check `htop`, increase swap or reduce concurrent connections |
| Configuration changed | Server starts but tools return errors | `hermes mcp config validate`, check for schema changes |

### Symptom: Intermittent tool failures ("sometimes works, sometimes doesn't")

**Diagnosis:**

```bash
# Check MCP server logs for timeout patterns
hermes mcp logs corpusiq --last 100 | grep "timeout\|error\|retry"

# Check network latency to MCP server
ping -c 10 <mcp-server-host>
```

**Common causes:**
- **Network instability:** MCP server on a different node with intermittent connectivity
- **Rate limiting:** External API the MCP server calls is rate-limiting
- **Connection pool exhaustion:** Too many concurrent agent threads exhausting MCP connection pool

**Fix:** Increase MCP timeout in config (`mcp_timeout: 60`), implement retry with backoff, or add connection pooling.

### Symptom: Specific tool always fails while others work

This usually means the tool's API credential is expired, its schema changed, or its external service is down.

```bash
# Test the specific tool in isolation
hermes mcp test corpusiq --tool google_ads_connector

# Check credential status
hermes auth status google_ads
```

## OAuth Token Expiry

Token management is the most common operational issue in autonomous systems. Every external service uses OAuth, and tokens expire.

### Symptom: "401 Unauthorized" or "Authentication required" on previously working tools

**Diagnosis:**

```bash
# Check all connector auth states
hermes auth list

# Check when a specific token expires
hermes auth status google_workspace --verbose
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

For services that support it, configure automated token refresh:

```yaml
# hermes/config/auth.yaml
token_management:
  proactive_refresh: true
  refresh_before_expiry_hours: 24
  alert_on_refresh_failure: true
  max_retry_attempts: 3

  connectors:
    google_workspace:
      refresh_interval_hours: 24
      alert_channel: "ops-alerts"
    microsoft:
      refresh_interval_hours: 24
      alert_channel: "ops-alerts"
    slack:
      refresh_interval_hours: 48
```

### Manual Token Reset

When automated refresh fails, reset the connector:

```bash
# Reset a specific connector token
hermes auth reset google_workspace

# This returns a re-auth URL — open it in a browser
# After re-auth, verify
hermes auth verify google_workspace
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
hermes cron history --last 20

# Check a specific job's full execution log
hermes cron log <job_name> --last 5

# Look for jobs that "succeeded" but produced no output
hermes cron history --last 50 | grep "status: ok" | grep "output_lines: 0"
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
# Check for concurrent execution
hermes cron status <job_name> --check-concurrency

# Check system resources at scheduled time
journalctl --since "2026-06-16 03:00" --until "2026-06-16 03:05" | grep -i "memory\|oom"

# Check rate limit logs
hermes cron log <job_name> --filter "rate_limit\|backoff"
```

**Fix:** Set appropriate concurrency policies per job:

```yaml
# hermes/cron/<job_name>.yaml
concurrency_policy: "skip"     # skip if already running (default)
# or
concurrency_policy: "queue"    # queue and run after current finishes
# or
concurrency_policy: "replace"  # kill current, start new
```

### Symptom: Upstream dependency failed (context_from chain broken)

Jobs that depend on other jobs (`context_from`) fail when the upstream fails.

**Fix:** Make chains resilient:

```yaml
# Instead of hard dependency
context_from: "daily_data_sync"

# Use fallback chain
context_from:
  primary: "daily_data_sync"
  fallback: "daily_data_sync_cached"  # Uses yesterday's data
  max_staleness_hours: 48             # Alert if fallback is too stale
```

### Cron Monitoring Setup

```yaml
# hermes/cron/monitor_all_crons.yaml
name: cron_health_monitor
schedule: "*/15 * * * *"  # Every 15 minutes
task: monitor.check_all_crons
params:
  alert_on:
    - "consecutive_failures >= 2"
    - "last_run > 2x schedule_interval"
    - "output_size_decreased > 80%"
  alert_channel: "ops-alerts"
```

## Browser Automation Failures

Browser automation is inherently fragile. Websites change, CAPTCHAs appear, and network conditions vary.

### Symptom: "Browser executable doesn't exist"

**Diagnosis:**

```bash
# Check installed browsers
npx playwright install --dry-run

# Check current config
cat ~/.agent-browser/config.json
```

**Fix (ARM64/DGX):**

```json
// ~/.agent-browser/config.json
{
  "executablePath": "/path/to/chromium-1223/chrome",
  "args": ["--headless=new", "--no-sandbox", "--disable-dev-shm-usage"]
}
```

On aarch64 systems, standard Chrome/Chromium paths don't work. Use Playwright's bundled Chromium and specify the path explicitly.

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

**When CAPTCHA appears:** The task fails and is retried. If CAPTCHA persists across 3 retries, the task is escalated for human review. The browser automation cannot solve CAPTCHAs by design — attempting to would violate most platforms' terms of service.

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
hermes model usage --last 50

# Check routing rules
hermes config list models
```

**Common routing problems:**

| Problem | Cause | Fix |
|---|---|---|
| Premium model for simple classification | No routing rule for classification tasks | Add `task_type: classification → tier: lightweight` |
| Lightweight model for complex reasoning | Task complexity underestimated | Add `min_complexity: 7 → tier: premium` rule |
| Model from wrong provider | Provider priority misconfigured | Set `provider_preference` in routing config |

### Symptom: "Model not found" or provider errors

**Diagnosis:**

```bash
# Verify provider connection
hermes model test deepseek
hermes model test anthropic
hermes model test openai

# Check rate limit status
hermes model limits
```

**Fixes:**

- Provider API key expired → Update in `hermes config set provider_key`
- Rate limit hit → Implement exponential backoff in router
- Model deprecated → Update to newer model version in config
- Provider outage → Configure fallback provider chain

### Symptom: High token costs

**Diagnosis:**

```bash
# Daily cost breakdown by model tier
hermes model cost --daily --last 7

# Cost per task type
hermes model cost --by-task --last 7
```

**Optimization:**

```yaml
# hermes/config/models.yaml
routing:
  default_tier: "standard"  # Don't default to premium
  cost_ceiling_daily: 5.00  # Hard stop at $5/day

  rules:
    - task_type: "classification"
      tier: "lightweight"
    - task_type: "formatting"
      tier: "lightweight"
    - task_type: "summarization"
      tier: "standard"
    - task_type: "strategic_analysis"
      tier: "premium"
      max_daily_calls: 20  # Cap premium calls
```

## Gateway Crashes

The API gateway is the entry point for all agent requests. When it goes down, everything stops.

### Symptom: All requests failing with 502/503

**Diagnosis:**

```bash
# Check gateway process
systemctl status hermes-gateway

# Check gateway logs
journalctl -u hermes-gateway --since "5 minutes ago"

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
| Config parse error | Gateway fails to start after config change | `hermes config validate`, revert last change |
| Upstream LLM provider down | Gateway can't reach any model provider | Check provider status pages, enable degraded mode with local models |

### Symptom: Gateway running but requests hang

**Diagnosis:**

```bash
# Check active connections
ss -tunap | grep <gateway_port>

# Check for hung threads
kill -3 $(pgrep -f hermes-gateway)  # Thread dump (Java)
# or
pystack $(pgrep -f hermes-gateway)   # Python stack trace
```

**Common causes:**
- **Connection pool exhaustion:** All connections to an upstream service are in use
- **Deadlock in model router:** Two requests waiting on each other
- **GC pause (Java backend):** Garbage collection blocking all threads

**Fix:** Restart gateway with `systemctl restart hermes-gateway`. For recurring issues, tune connection pool size or GC settings.

### Gateway Recovery Procedure

```bash
# 1. Check what's wrong
systemctl status hermes-gateway
journalctl -u hermes-gateway --since "10 minutes ago" -n 50

# 2. Attempt graceful restart
systemctl reload hermes-gateway

# 3. If reload fails, hard restart
systemctl restart hermes-gateway

# 4. Verify recovery
curl -f http://localhost:<gateway_port>/health

# 5. Check all downstream services recovered
hermes health full

# 6. Re-queue any failed requests
hermes queue retry --since "15 minutes ago"
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

```yaml
# hermes/cron/worker_health.yaml
name: worker_node_health
schedule: "*/5 * * * *"
task: health.check_worker_node
params:
  host: "worker-node.local"
  checks:
    - ssh_connectivity
    - disk_usage
    - memory_usage
    - browser_driver_status
    - content_queue_depth
  alert_on_failure: true
  alert_channel: "ops-alerts"
```

## Quick Reference: Recovery Commands

```bash
# Full system health check
hermes health

# Restart all services in correct order
hermes restart --all

# Check what's consuming resources
hermes diagnostics

# View recent errors across all components
hermes errors --last 50

# Test critical path (orchestration → tool → response)
hermes test e2e

# Re-queue failed tasks
hermes queue retry --failed-only --since "1 hour ago"
```

## When All Else Fails

1. **Check the logs:** `hermes diagnostics` gives you a system-wide view
2. **Isolate the failure:** Test each component independently
3. **Check for recent changes:** `hermes config diff` shows what changed
4. **Roll back:** If a config change caused the issue, `hermes config rollback`
5. **Escalate:** Some failures genuinely need human intervention. The system is designed to degrade gracefully — individual features may fail while the core continues operating.

---

*↑ [Architecture](/hermes/architecture/) · [Setup Guide](/hermes/setup/) · [Home](/hermes/)*


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
