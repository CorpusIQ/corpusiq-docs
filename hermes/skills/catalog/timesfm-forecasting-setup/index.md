---
title: TimesFM Forecasting — Full Setup Guide for Hermes Agents
description: Install and use Google's TimesFM for zero-shot time series forecasting from Hermes agents. Predict revenue, usage, growth — no training required.
---

# TimesFM Forecasting — Setup Guide

**Source:** [k-dense-ai/scientific-agent-skills](https://github.com/k-dense-ai/scientific-agent-skills) (699 installs)
**Also available from:** google-research/timesfm (153), eturkes/claude-scientific-skills (23)
**Category:** Data Science / Forecasting

Google Research's TimesFM is a decoder-only foundation model for time series forecasting. Unlike traditional statistical models (ARIMA, Prophet), TimesFM requires zero training — pass historical data and get predictions immediately. The skill wraps this into a Claude Code / Hermes agent workflow.

---

## Installation

```bash
npx skills add k-dense-ai/scientific-agent-skills --skill timesfm-forecasting
```

For the Google Research variant:

```bash
npx skills add google-research/timesfm --skill timesfm-forecasting
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python 3.10+** | `python3 --version` — TimesFM requires 3.10+ |
| **Historical data** | CSV or JSON with timestamp + value columns |
| **Hermes Agent** | Any version with skills support |

Install TimesFM Python package:

```bash
pip install timesfm
```

The skill will install this automatically on first use, but pre-installing avoids cold-start latency.

---

## Key Capabilities

### Core Features

| Capability | How to Trigger | Notes |
|---|---|---|
| Point forecasting | "Forecast next 30 days of this revenue data" | Zero-shot — no model training |
| Uncertainty intervals | "Forecast with 90% confidence intervals" | Built-in quantile prediction |
| Multi-horizon | "Predict 7-day, 30-day, and 90-day forecasts" | Variable horizon from single call |
| Seasonal decomposition | "Decompose this time series" | Trend + seasonal + residual |
| Anomaly detection | "Find anomalies in this usage data" | Flags points outside prediction intervals |

### CLI Command Reference

```bash
# Point forecast
python3 SKILL_DIR/scripts/forecast.py --input data.csv --horizon 30

# With confidence intervals
python3 SKILL_DIR/scripts/forecast.py --input data.csv --horizon 90 --ci 0.95

# Anomaly detection
python3 SKILL_DIR/scripts/forecast.py --input data.csv --detect-anomalies
```

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Revenue forecasting** | Predict monthly revenue from Stripe/QuickBooks export data |
| **Usage growth prediction** | Forecast agent session growth, API call volume |
| **Churn risk detection** | Identify accounts with declining usage patterns |
| **Capacity planning** | Predict compute/storage needs from historical metrics |
| **ROI projection** | Model expected returns from growth campaigns |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| `ModuleNotFoundError: timesfm` | `pip install timesfm` — package not auto-installed |
| `CUDA not available` | TimesFM runs on CPU. Add `--device cpu` flag for non-GPU environments. |
| Out-of-memory on large datasets | TimesFM context window is 512 points. Batch longer series or downsample. |
| Prediction looks flat | Input series may lack clear trend/seasonality. Add exogenous features or extend history. |

---

## Verification

```bash
# Verify skill installed
hermes skills list | grep timesfm-forecasting

# Quick test with sample data
python3 -c "
import pandas as pd
import numpy as np
dates = pd.date_range('2026-01-01', periods=100, freq='D')
values = np.sin(np.arange(100) * 0.3) + np.random.normal(0, 0.1, 100) + np.arange(100) * 0.05
pd.DataFrame({'ds': dates, 'y': values}).to_csv('/tmp/test_series.csv', index=False)
print('Sample data written to /tmp/test_series.csv')
"
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 30 Update 2 Discovery](/hermes/skills/marketplace/new-june30-2026-update2/) →*
*Powered by CorpusIQ*
