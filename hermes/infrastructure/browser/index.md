---
title: Browser Automation Architecture
description: "Production browser automation for Hermes agents using Playwright stealth and persistent contexts."
canonical: "https://www.corpusiq.io/docs/hermes/infrastructure/browser/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Browser Automation Architecture

The platform runs browser-use on a dedicated worker node with Playwright, enabling robust web interaction while minimizing detection risk.

## Architecture

The primary compute node orchestrates tasks. A dedicated worker node executes browser operations. This separation prevents browser processes from competing with inference workloads on the primary compute node.

### Why Isolate Browsers?

- **Memory leaks**: Long-running browser sessions accumulate memory; isolation contains the damage
- **Crash containment**: A crashed browser takes down nothing but itself
- **Anti-bot considerations**: Browser fingerprinting runs from the worker's network context
- **Resource scheduling**: Video, inference, and browser workloads don't compete

## Key Components

### Playwright with Stealth

```python
from playwright_stealth import Stealth

stealth = Stealth()
await stealth.apply_stealth_async(page)
```

- Disables automation signals (`--disable-blink-features=AutomationControlled`)
- Realistic user agents per platform
- Human-like timing delays between actions

### Persistent Contexts

```python
browser = await p.chromium.launch_persistent_context(
    user_data_dir="~/.agent_browser",
    headless=False,
)
```

- Login sessions survive restarts
- Cookies + crypto-bound keys stored together (critical for anti-bot platforms)
- One profile per platform to avoid cross-contamination

## Platform Notes

| Platform | Approach |
|----------|----------|
| Cloudflare-protected | headful + residential context |
| Google OAuth flows | persistent context, never fresh incognito |
| React-heavy SPAs | vision-driven automation over selectors |
| Simple forms | plain Playwright, no LLM overhead |

## Cost Discipline

Vision-driven browser automation bills per LLM call. Use it only where selector automation fails. Everything else runs on plain Playwright — free.
