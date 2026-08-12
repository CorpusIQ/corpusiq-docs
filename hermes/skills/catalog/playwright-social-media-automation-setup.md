---
title: Playwright Social Media Automation — API-First, Browser Fallback
description: Automate social posting and comment monitoring with Playwright when APIs are unavailable. Reddit, Discord, and generic web forms — with anti-bot patterns, reliability waits, and a fallback decision tree.
---

# Playwright Social Media Automation — Setup Guide

**Source:** [microsoft/playwright](https://github.com/microsoft/playwright) — 74,000+ ★ | Python/JS
**Category:** Automation / Social Media
**Quality Tier:** 🟢 Production (official Microsoft project)

Playwright drives real browsers for posting and comment monitoring on platforms where direct APIs are missing, rate-limited, or require interactive authentication. It is a fallback layer, not the primary tool: use APIs first, browser automation second.

---

## Core Principle: API-First, Browser-Fallback

```
Can you use the platform's API directly?
├─ YES (credentials configured, client installed) → Use the API
└─ NO
   ├─ Webhook available (Discord) → Use the webhook
   └─ Use Playwright browser automation
       └─ Failure → Manual mode (leave browser open, copy-paste)
```

Browsers are slower, flakier, and more detectable than APIs. Reach for Playwright only when the API path is genuinely closed.

---

## Installation

```bash
python3 -m pip install playwright
python3 -m playwright install
python3 -c "import playwright; print('Playwright ready')"
```

## Browser Choice by Platform

| Browser | Reddit | Discord | X/Twitter | Notes |
|---------|--------|---------|-----------|-------|
| Firefox | ✅ Best | ✅ Good | ⚠️ Risky | Better user-agent reputation on Reddit |
| Chromium | ✅ Works | ✅ Works | ✅ Best | Fast startup; Reddit may detect |
| WebKit | ⚠️ Limited | ⚠️ Limited | ❌ Bad | Avoid for production |

---

## Reliability Patterns

### 1. Wait for visibility before filling

```python
element = await page.wait_for_selector(selector, timeout=10000)
await element.wait_for_element_state('visible', timeout=10000)
await element.fill(text)
```

### 2. Fuzzy selector matching for dynamic forms

```python
async def find_element_fuzzy(page, selectors, timeout=5000):
    for selector in selectors:
        element = await page.query_selector(selector)
        if element:
            return element
    raise Exception(f"No element found: {selectors}")
```

### 3. Retry with exponential backoff

```python
async def retry_action(async_fn, max_attempts=3, delay=2):
    for attempt in range(max_attempts):
        try:
            return await async_fn()
        except Exception as e:
            if attempt == max_attempts - 1:
                raise
            await asyncio.sleep(delay)
            delay *= 2
```

### 4. Reduce bot detection

- Use a realistic user-agent string (never "Playwright")
- Headful mode on first deployment; go headless only after it works
- Add human-like delays between actions (500–2000 ms)
- Use `launch_persistent_context()` so login sessions survive restarts

### 5. Wait for JavaScript to settle

```python
await page.goto(url, wait_until="networkidle")
# or wait for a specific element instead of a fixed sleep
await page.wait_for_selector('button[class*="create"]', timeout=10000)
```

---

## Persistent Sessions for Anti-Bot Platforms

Some platforms cryptographically bind session cookies to the browser's local keychain. Copying cookies to another browser profile fails with HTTP 403 because the encryption keys no longer match. The fix: log in once inside a persistent profile and reuse that same profile forever.

```python
# One-time setup: headful login
ctx = p.firefox.launch_persistent_context(
    "/tmp/ff_profile",
    headless=False,               # user logs in manually
)
page = ctx.new_page()
page.goto("https://platform.com/login")

# All later runs: same profile, cookies AND keys intact
ctx = p.firefox.launch_persistent_context("/tmp/ff_profile", headless=True)
```

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `ElementHandle.fill: Timeout 30000ms exceeded` | Element not visible or not rendered | Wait for `visible` state before `.fill()` |
| Redirected to login page | Not authenticated | Log in first; keep the session open |
| Create-post button not found | Selector changed or JS still loading | Fuzzy selector matching + longer waits |
| HTTP 403 after copying cookies | Crypto-bound session keys | Persistent profile, never copy cookies |

---

## Notes

- **API-first**: Playwright is slower and more detectable than any API. Use it as a fallback.
- **Best for**: Reddit forms, comment monitoring that needs JS rendering, one-off blog/forum comments
- **Skip Playwright when**: a platform has a working API, a Discord webhook exists, or volume exceeds ~100 actions
- **Related**: See [Browser-Use Automation](/hermes/skills/catalog/browser-use-automation-setup) and [Midscene](/hermes/skills/catalog/midscene-skills-setup)

*Setup guide by CorpusIQ. Source: [microsoft/playwright](https://github.com/microsoft/playwright).*
