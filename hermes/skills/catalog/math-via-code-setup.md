---
title: Math via Code — Hermes Agent Skill Setup Guide
description: Install and configure tommulkins/hermes-skill-math-via-code — enforce all multi-step arithmetic through code execution to eliminate LLM math errors in financial analysis and data modeling
---

# Math via Code — Skill Setup

**Source:** [tommulkins/hermes-skill-math-via-code](https://github.com/tommulkins/hermes-skill-math-via-code)
**Stars:** 0 ⭐ | **License:** MIT
**Created:** June 24, 2026
**Category:** Development / Accuracy / Financial Analysis

---

## 1. What It Is

A Hermes Agent skill that enforces a hard rule: **all arithmetic with 3+ numbers goes through code execution.** No exceptions. Born from repeated errors in financial modeling — SDE calculations, P&L analysis, and facility rollups where a single transposed digit cascaded into incorrect deal evaluations.

**Core philosophy:** LLM arithmetic accuracy degrades sharply past ~150k context tokens and is unreliable even below that. Code is always right; in-head math is not.

### What It Handles

- Financial analysis: SDE, P&L, margins, royalties, annualizations
- Growth rates, ratios, percentages, weighted averages
- Unit conversions, projections, multi-facility rollups
- Reading data from files/APIs and computing derived values
- Excel-specific pitfalls (whitespace stripping, `data_only=True`, etc.)

### When NOT to Use

- Single-operation arithmetic on two numbers (`5 * 3`, `100 - 20`) — these are safe in-head
- Pure text manipulation or formatting tasks

---

## 2. Prerequisites

- Hermes Agent
- No additional packages required (uses built-in `execute_code`)

---

## 3. Installation

```bash
hermes skills install https://raw.githubusercontent.com/tommulkins/hermes-skill-math-via-code/main/SKILL.md --category software-development --name math-via-code -y
```

### Verify

```bash
hermes skills list | grep math-via-code
```

---

## 4. How It Works

### Decision Flow

```
Numbers provided? → Count them:
  ├── 0-2 numbers → Safe for in-head math (e.g., 5 * 3)
  └── 3+ numbers → ROUTE TO CODE (execute_code or Python script)
```

### Procedure

1. **Determine inputs** — Capture numbers as variables from conversation, files, or APIs. Never re-type from memory.
2. **Write the calculation** — Use `execute_code` for in-memory math; use `terminal` with project venv for packages (openpyxl, pandas).
3. **Self-check** — Include assertions or cross-checks against source data.

### Example: SDE Calculation

```python
# Instead of in-head math, the skill routes to:
revenue = 327158
direct_costs = 192193
gp = revenue - direct_costs

overhead_items = [960, 1351.92, 9000, 1440, 1137.24]
overhead_royalties = round(revenue * 0.07, 2)
total_overhead = sum(overhead_items) + overhead_royalties

sde = gp - total_overhead
print(f"SDE: ${sde:,.2f}")
```

---

## 5. Data Sources

| Source | Guidance |
|--------|----------|
| **Conversation** | Capture numbers as Python variables directly |
| **Excel/CSV** | Use `openpyxl` with `data_only=True`; strip whitespace from all cell values |
| **API responses** | Parse JSON, validate numeric fields, handle null/missing values |
| **Multi-file** | Cross-reference with assertions (e.g., `assert sum(details) == total, "Mismatch"`) |

---

## 6. CorpusIQ Use Cases

| Use Case | Application |
|----------|-------------|
| **Lead qualification math** | LTV calculations, churn projections, CAC payback periods |
| **Pricing analysis** | Margin calculations, tier comparisons, bundling economics |
| **Growth metrics** | MoM/ YoY growth rates, cohort retention math |
| **Agent cost tracking** | Token cost aggregation, per-agent cost allocation, budget burn rates |
| **Financial reporting** | Revenue rollups across multiple data sources |

---

## 7. Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Skill doesn't trigger | Calculation is simple (2 numbers) | Only 3+ number operations trigger the skill |
| Excel values wrong | `data_only=False` returns formulas | Use `openpyxl.load_workbook(file, data_only=True)` |
| Whitespace breaks numbers | Cells have trailing spaces | `.strip()` all cell values before conversion |
| Assertion fails | Source data inconsistent | Report the mismatch — don't silently proceed |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 24 Evening Discovery](/hermes/skills/marketplace/new-june24-2026-evening/) →*
