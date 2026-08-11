---
title: Polymarket — Prediction Market Integration Setup
description: Install and configure polymarket from nousresearch/hermes-agent. Real-world prediction market data for event forecasting, sentiment analysis, and probabilistic reasoning — 273 installs.
category: hermes-skills
publisher: nousresearch
installs: 273
source: https://skills.sh/nousresearch/hermes-agent/polymarket
---

# Polymarket — Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/polymarket) (273 installs)
**Category:** Data / Prediction Markets
**License:** MIT · **Platforms:** Linux, macOS, Windows
**Dependencies:** Polymarket API access (free tier available)

Agent skill for Polymarket — the world's largest prediction market platform. Gives Hermes access to real-time market prices, event probabilities, volume data, and market resolution history. 273 installs, making it one of the most popular data-integration skills for Hermes.

---

## What It Does

| Capability | How |
|-----------|-----|
| **Market prices** | Real-time buy/sell prices for all active markets |
| **Event probabilities** | Implied probability from market prices |
| **Volume tracking** | 24h, weekly, and lifetime volume per market |
| **Market resolution** | Historical data on resolved markets |
| **Category browsing** | Politics, crypto, sports, science, pop culture |
| **Trend detection** | Price movement and volume spike alerts |

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add nousresearch/hermes-agent --skill polymarket
```

### Direct from Hermes Agent Repo

```bash
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/data/polymarket ~/.hermes/skills/
```

---

## Usage Examples

### Check Event Probability

```
What's the current probability of a Fed rate cut in September according to Polymarket?
```

### Market Research

```
Compare Polymarket prices for the 2026 midterm elections across different outcome markets.
Show me which markets have the highest 24h volume.
```

### Trend Analysis

```
Track the price movement on the "AI regulation bill passes in 2026" market over the last 7 days.
```

---

## Available Market Categories

| Category | Example Markets |
|----------|----------------|
| Politics | Elections, legislation, geopolitical events |
| Crypto | BTC/ETH price targets, ETF approvals |
| Sports | Game outcomes, season championships |
| Science | Space launches, drug approvals |
| Pop Culture | Award shows, box office predictions |
| Economics | Fed decisions, inflation targets |

---

## API Access Tiers

| Tier | Rate Limit | Features |
|------|-----------|----------|
| Free | 10 req/min | Public market data, prices, volume |
| CLOB API | 100 req/min | Order book depth, trading (requires wallet) |

---

## Configuration

```yaml
polymarket:
  enabled: true
  api_tier: "free"              # or "clob" for trading access
  default_markets:
    - "politics"
    - "crypto"
  alert_thresholds:
    volume_spike_pct: 50        # Alert on 50%+ volume increase
    price_move_pct: 10          # Alert on 10%+ price movement
```

---

## Verification

After install, test with:

```
Hermes, show me the top 5 Polymarket markets by 24h volume.
```

The agent should return market names, current prices, and 24h volume data.

---

## Pitfalls

- **Not financial advice:** Polymarket prices reflect crowd sentiment — not guaranteed outcomes. The skill provides data, not trading recommendations.
- **API rate limits:** The free tier is limited to 10 requests/minute. Heavy polling or multi-market queries can trigger rate limiting.
- **Market liquidity:** Low-volume markets may have stale or unreliable prices. Always check 24h volume before relying on price data.
- **Geographic restrictions:** Polymarket is not available in all jurisdictions. The skill API may be restricted in certain regions.
- **CLOB API requires wallet:** For trading or order book access, a Polymarket wallet and CLOB API key are required.

---

## See Also

- [arxiv-setup.md](arxiv-setup.md) — Academic paper research
- [llm-wiki-setup.md](llm-wiki-setup.md) — LLM knowledge base queries

---

*Setup guide by CorpusIQ. Source: [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) (MIT).*
