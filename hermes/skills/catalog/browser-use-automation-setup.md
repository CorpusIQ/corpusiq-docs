---
title: Browser-Use — AI-Powered Browser Automation for Anti-Bot Sites
description: Set up browser-use (97K+ GitHub stars) for AI vision-driven browser automation. Navigate, fill forms, and extract data from LinkedIn, TikTok, Product Hunt, and Cloudflare-protected sites that block traditional automation.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/browser-use-automation-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Browser-Use Automation — Setup Guide

**Source:** [browser-use/browser-use](https://github.com/browser-use/browser-use) — 97,000+ ★ | Python
**Category:** Automation / Browser-Use
**Quality Tier:** 🟢 Production (97K+ GitHub stars, active development)

Browser-use replaces Playwright/Selenium for sites defended by anti-bot systems. Instead of writing brittle selectors, you describe the task in natural language and a vision-capable LLM drives the browser like a human. It handles CAPTCHAs, JS-heavy rendering, and anti-bot detection natively.

---

## How It Works

1. You describe a goal ("log in to this site, navigate to the pricing page, extract the plans")
2. A vision-capable model (Claude Sonnet, GPT-4 class) screenshots the page
3. The model decides the next action: click, type, scroll, navigate
4. Actions execute through a real browser until the task completes

This closed loop is why browser-use succeeds where selector-based automation fails: it adapts to dynamic DOMs, obfuscated class names, and layout shifts.

---

## Installation

```bash
python3 -m venv venv-browser
source venv-browser/bin/activate
pip install browser-use
python3 -m playwright install chromium   # browser-use drives Playwright under the hood
```

## Quick Start

```python
import asyncio, os
from browser_use import Agent, ChatAnthropic

async def main():
    llm = ChatAnthropic(
        model="claude-sonnet-4-20250514",
        api_key=os.getenv("ANTHROPIC_API_KEY"),
    )
    agent = Agent(
        task="Go to linkedin.com/login, log in, navigate to jobs",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
```

Requirements:
- Python 3.11+
- A vision-capable LLM API key (browser-use is LLM-agnostic: Anthropic, OpenAI, Gemini, or local Ollama models)
- ~5 GB free disk for browser binaries

---

## When to Use Browser-Use

| Use browser-use for | Stick with plain Playwright for |
|---------------------|---------------------------------|
| Sites with Cloudflare / anti-bot walls | Simple form filling on undefended sites |
| Dynamic SPAs with obfuscated selectors | API-authenticated platforms |
| CAPTCHA-protected flows | Bulk scraping (LLM calls add cost) |
| Multi-step logins with security checkpoints | Speed-critical extraction |

**Cost note:** Every action costs an LLM call. For high-volume scraping, plain Playwright or direct APIs are far cheaper. Browser-use shines on flows where automation gets blocked, not where it merely works.

---

## Headless Limitations

Anti-bot systems fingerprint headless browsers. Browser-use works best when the runtime environment looks like a real user:

- Residential or mobile IPs pass Cloudflare checks where datacenter IPs get challenged
- Headful mode with persistent profiles survives platform login flows (cookies + crypto-bound session keys persist together)
- On headless servers, pair with Xvfb for a virtual display

```bash
Xvfb :99 -screen 0 1920x1080x24 -ac &
export DISPLAY=:99
```

---

## Verification

```bash
python3 -c "import browser_use; print('browser-use ready')"
```

A successful smoke test: run the Quick Start against a public site and confirm the agent extracts the expected data.

---

## Notes

- **Production-grade**: 97K+ GitHub stars, used across the AI automation ecosystem
- **Vision-first**: No CSS selectors needed — the model sees the page like a human
- **Best for**: Anti-bot-defended platforms, dynamic SPAs, CAPTCHA flows
- **Complementary**: Use alongside plain Playwright — browser-use for vision tasks, Playwright for cheap API-level control
- **Related**: See [Playwright Social Media Automation](/hermes/skills/catalog/playwright-social-media-automation-setup) and [Midscene](/hermes/skills/catalog/midscene-skills-setup)

*Setup guide by CorpusIQ. Source: [browser-use/browser-use](https://github.com/browser-use/browser-use).*
