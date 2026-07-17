---
title: browser-act — Record-and-Replay Browser Automation for Hermes
description: Install and use browser-act/skills@browser-act (99K installs) for agent-native browser automation. Record interactions as reusable templates, replay with parameter substitution, and evade bot detection.
---

# browser-act — Setup Guide

**Source:** [browser-act/skills](https://github.com/browser-act/skills) (99,500 installs)
**Category:** Browser Automation
**Languages:** Python + Playwright

Agent-native browser automation framework. Unlike selector-based or accessibility-tree approaches, browser-act uses a "record-and-replay" paradigm — agents record browser interactions as reusable skill templates, then replay them with parameter substitution. Includes browser-act-skill-forge (78.7K installs) for visual template editing.

---

## Installation

```bash
# Core browser automation
npx skills add browser-act/skills@browser-act

# Skill forge for creating templates (optional)
npx skills add browser-act/skills@browser-act-skill-forge
```

Verify:
```bash
npx skills list | grep browser-act
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python** | 3.10+ |
| **Playwright** | `pip install playwright && playwright install` |
| **Hermes Agent** | Any version |
| **Chrome/Firefox** | Installed via Playwright |

Install Playwright if missing:
```bash
pip install playwright
playwright install chromium
```

---

## Key Capabilities

### Record-and-Replay Workflow

```
┌─────────────────────┐     ┌──────────────────────┐     ┌─────────────────────┐
│  Record Interaction │ ──▶ │  Save as Skill       │ ──▶ │  Replay with Params │
│  (browser-act record)│     │  Template (.yaml)    │     │  (browser-act run)  │
└─────────────────────┘     └──────────────────────┘     └─────────────────────┘
```

### Core Commands

| Command | Purpose | Example |
|---|---|---|
| `browser-act record` | Record a new interaction | `browser-act record --name "check-twitter-mentions"` |
| `browser-act run` | Replay a recorded template | `browser-act run check-twitter-mentions --account CorpusIQ` |
| `browser-act forge` | Open visual template editor | `browser-act forge check-twitter-mentions` |
| `browser-act list` | List saved templates | `browser-act list --category social` |
| `browser-act params` | Show template parameters | `browser-act params check-twitter-mentions` |

### Parameter Substitution

Record once, replay with different values:

```yaml
# Template: check-twitter-mentions.yaml
steps:
  - action: navigate
    url: "https://twitter.com/{{ account }}"
  - action: click
    selector: "[data-testid='mentions-tab']"
  - action: extract
    selector: "[data-testid='tweet']"
    fields:
      - author: "[data-testid='User-Name']"
      - text: "[data-testid='tweetText']"
      - time: "time"

# Replay for different accounts:
browser-act run check-twitter-mentions --account CorpusIQ
browser-act run check-twitter-mentions --account nousresearch
```

### Anti-Detection Features

| Feature | Purpose | Config |
|---|---|---|
| **Fingerprint rotation** | Randomize browser fingerprint per session | `--fingerprint random` |
| **Human-like timing** | Random delays between actions (150-800ms) | `--human-timing true` |
| **Proxy rotation** | Route through different IPs | `--proxy pool:residential` |
| **CAPTCHA handling** | Auto-detect and pause for manual solve | `--captcha pause` |
| **Session isolation** | Separate browser profiles per template | Default; configurable |

### Skill Forge (Visual Editor)

```bash
browser-act forge check-twitter-mentions
```

The visual editor lets you:
1. **View recorded steps** as a flowchart
2. **Edit selectors** with live element highlighting
3. **Add assertions** (element visible, text contains, URL matches)
4. **Test parameter substitution** with sample values
5. **Debug failures** with step-by-step replay and screenshots

---

## Common Templates for CorpusIQ

### Social Media Monitoring
```bash
# Record: Login → check notifications → extract mentions → reply
browser-act record --name "social-check" --start-url "https://twitter.com/notifications"
```

### Competitive Research
```bash
# Record: Visit competitor page → screenshot pricing → extract features
browser-act record --name "competitor-analysis" --params "url,company_name"
```

### Platform Health Check
```bash
# Record: Login to Postiz → check scheduled posts → verify publishing status
browser-act record --name "postiz-health" --start-url "https://app.postiz.com"
```

---

## Comparison: browser-act vs agent-browser

| Feature | browser-act | agent-browser |
|---|---|---|
| **Interaction model** | Record-and-replay | Accessibility tree (refs) |
| **Best for** | Repeated workflows, social media | One-off exploration, scraping |
| **Template reuse** | Yes — parameter substitution | No — manual each time |
| **Anti-detection** | Built-in (fingerprint, timing, proxy) | Minimal (Chrome for Testing) |
| **Learning curve** | Moderate (record once) | Low (snap + ref) |
| **Speed** | Slower (human timing) | Fast (native Rust) |
| **Install base** | 99.5K | 553.6K |
| **CorpusIQ use case** | Daily social checks, competitor monitoring | Web scraping, data extraction |

**Recommendation:** Use both. browser-act for recurring workflows (daily social monitoring, competitive checks). agent-browser for ad-hoc research and scraping.

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `browser-act: command not found` | Skill not installed | `npx skills add browser-act/skills@browser-act` |
| Template replay fails on login | Session expired | Re-record with fresh login, save cookies |
| CAPTCHA blocks recording | Anti-bot detection | Enable `--human-timing` and `--fingerprint random` |
| Selector not found on replay | Site structure changed | Use `browser-act forge` to update selectors |
| Recorded template too brittle | Overly specific selectors | Use `--robust-selectors` flag when recording |

---

## See Also

- [agent-browser](/hermes/skills/catalog/agent-browser-setup/) — Accessibility-tree browser automation (553K installs)
- [browser-use-automation](/hermes/skills/catalog/) — Python browser automation framework (85K installs)
- [Apify Agent Skills](/hermes/skills/catalog/apify-agent-skills-setup/) — Web scraping Actors (2.2K⭐)
