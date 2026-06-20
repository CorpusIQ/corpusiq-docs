---
title: Browser Automation Architecture
description: Production browser automation for Hermes agents using Playwright stealth and persistent contexts
---

# Browser Automation Architecture

The platform runs browser-use on the Mac Mini worker node with Playwright, enabling robust web interaction while minimizing detection risk.

## Architecture

The primary compute node orchestrates tasks. A dedicated worker node executes browser operations. This separation prevents browser processes from competing with inference workloads on the primary compute node.

## Playwright Setup

```bash
pip install playwright
playwright install chromium
```

## Stealth Configuration

```python
from playwright.sync_api import sync_playwright
browser = p.chromium.launch(
    headless=False,
    args=['--disable-blink-features=AutomationControlled']
)
context = browser.new_context(
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...',
    viewport={'width': 1280, 'height': 720}
)
```

## Persistent Contexts

Browser sessions persist across agent runs. Cookies, local storage, and authentication states survive restarts. Essential for platforms that enforce login sessions (LinkedIn, TikTok, Instagram).

## Detection Avoidance

| Technique | Purpose |
|-----------|---------|
| Custom user agent | Avoid default automation UA flags |
| Disable automation flags | Hide WebDriver markers |
| Human-like timing | Random delays between actions |
| Viewport variety | Match real device dimensions |
| Cookie persistence | Maintain login sessions across runs |

## Supported Platforms

LinkedIn, TikTok, Instagram, Product Hunt, web forms, and application submissions. Each platform has its own automation profile with platform-specific timing and interaction patterns.

## DGX Workaround

For aarch64 systems without Chrome, Playwright chromium-1223 with explicit executable path in `~/.agent-browser/config.json` provides a fallback. Curl-based DuckDuckGo Lite search fills in when full browser automation is unavailable.


*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*


*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
