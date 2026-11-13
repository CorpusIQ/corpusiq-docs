---
title: "Open Accountant Skills - Bookkeeping and Tax Setup"
description: "openaccountant/skills: 21.0K combined installs across 44 listings, open-source bookkeeping and tax skills: bank sync, close, tax prep, invoicing"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/openaccountant-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "bookkeeping", "tax", "finance"]
---

# Open Accountant Skills - Setup Guide

**Source:** [openaccountant/skills](https://www.skills.sh/openaccountant/skills) via skills.sh - 21.0K combined installs across 44 indexed listings; first seen Nov 13, 2026
**GitHub:** 120 stars, MIT license, `main` branch, last pushed 2026-04-09, 44 `SKILL.md` files across three top-level folders, 62 files in total
**Category:** Bookkeeping, tax and personal finance procedures for agents
**Quality Tier:** 🟢 Green - a clean 44-for-44 listing tree, an MIT licence and documented installs for every major agent.

Forty-four skills, one for each listing in the index, split into three folders that describe the audience rather than the technology: ten personal finance skills, eighteen for business and freelancers, sixteen shared. The count matches the tree exactly, which is rarer than it sounds and means the index and the repository agree on what exists.

The design decision worth copying is that every skill runs in two modes. With the publisher's own Wilson CLI installed, a skill calls its tools (`transaction_search`, `spending_summary`, `anomaly_detect`) and queries a database directly. Without it, the same skill walks the agent through working from an exported CSV, a spreadsheet or manual entry, which is why the pack advertises compatibility with a dozen agents rather than one.

The install band runs from 417 to 699, a spread of 282 across 44 listings, so the ordering inside the pack carries some signal rather than describing a single install event.

## Installation

The README documents one command for every agent that reads `SKILL.md` files:

```bash
npx skills add openaccountant/skills
```

A single skill:

```bash
npx skills add openaccountant/skills --skill tax-prep
```

List what is available before choosing:

```bash
npx skills add openaccountant/skills --list
```

Pi installs from the git URL:

```bash
pi install git:github.com/openaccountant/skills
```

The Wilson CLI discovers skills from a fixed path, so a clone is enough:

```bash
git clone https://github.com/openaccountant/skills.git ~/.openaccountant/skills
```

The README also carries a compatibility table with the config directory and discovery path per platform: Claude Code (`.claude/skills/`), Cursor (`.cursor/skills/`), OpenAI Codex (`.agents/skills/`), Gemini CLI (`.gemini/skills/`), GitHub Copilot (`.github/skills/`), Pi, OpenCode, Kiro, Trae, Rovo Dev and Paperclip. Several rows name a fallback directory, which is how Cursor and Copilot find skills installed for another agent.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| bank-sync | 699 | Connecting bank accounts for automatic transaction import through Plaid. |
| contractor-tracking | 586 | Monitoring 1099 contractor payments and flagging the $600 threshold. |
| rental-property | 553 | Rental income, expenses, ROI and cap rate per property. |
| cash-flow-forecast | 544 | Projecting future cash flow from historical trends and recurring patterns. |
| spending-review | 537 | A categorised spending breakdown with month-over-month trends. |
| month-end-close | 536 | A monthly bookkeeping close checklist with reconciliation. |
| import-transactions | 517 | Importing CSV, OFX or QIF bank exports and deduplicating them. |
| zero-based-budget | 515 | Allocating every dollar of income to a category. |
| profit-loss | 511 | A profit and loss statement for any date range. |
| invoice-aging | 511 | Unpaid invoices by age bucket, with overdue payments flagged. |
| subscription-audit | 501 | Finding recurring subscriptions, totalling the cost and flagging unused ones. |
| smart-categorize | 496 | Auto-categorising uncategorised transactions by vendor pattern. |
| expense-optimizer | 494 | Finding recurring expenses and subscriptions to cut or reduce. |
| net-worth | 486 | Net worth from assets and liabilities as a formatted statement. |
| debt-payoff | 481 | Avalanche or snowball payoff plans with payment schedules. |
| monthly-digest | 480 | A monthly financial summary with metrics, trends and anomalies. |
| insurance-audit | 479 | Insurance payments, total annual premiums and a comparison to benchmarks. |
| custom-report | 479 | Financial reports with user-defined date ranges and categories. |

The remaining 26 indexed listings range from 417 to 476 installs.

## Why This Matters for Hermes Agents

Accounting is the domain where an agent's confidence is most expensive, because a plausible number that is wrong looks exactly like a plausible number that is right. What this pack gets right is that it does not pretend to be a ledger. Each skill is a procedure: what to read, which categories apply, which checks to run, what the output should look like.

The two-mode design is the interesting engineering. A skill that can query a local database and a skill that can only read a CSV export are different documents, and most publishers pick one. These carry both, with the Wilson tools named so a capable agent can use them and a plain one can still follow the fallback path.

The tax coverage is narrower than the folder names suggest and should be read as US-specific: Schedule C categorisation, MACRS depreciation and Section 179 expensing, quarterly estimates with safe harbour rules, 1099 contractor thresholds, standard mileage rates, home office methods at federal level, and economic nexus by state. Teams outside the United States will use the structure and replace the rules.

The business folder is where the practical value sits for a small operator: month end close, invoice aging, client profitability, revenue concentration and runway calculation are the five numbers a freelancer or small agency needs and rarely has time to build.

## Usage

| You say | What happens |
|---|---|
| "Where did last month's money actually go?" | Runs `spending-review` and returns a categorised breakdown with month-over-month movement. |
| "Close the books for October" | Runs `month-end-close` and walks the checklist, including reconciliation steps. |
| "Which invoices are past due?" | Runs `invoice-aging` and returns unpaid invoices bucketed by age. |
| "Organise this year's expenses for my tax return" | Runs `tax-prep` and sorts expenses into Schedule C categories. |
| "Can I afford to hire a contractor at $2,000 a month?" | Runs `contractor-tracking` and `cash-flow-forecast` and reports the threshold and the projected runway. |
| "What subscriptions am I paying for that I never use?" | Runs `subscription-audit` and returns the recurring list with total cost. |
| "Which clients are actually profitable?" | Runs `client-profitability` and returns revenue and cost per client. |

## Verification

Two skills on the branch, both returning 200:

```bash
curl -fsSL https://raw.githubusercontent.com/openaccountant/skills/main/shared/bank-sync/SKILL.md | head -10
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/openaccountant/skills/main/business/profit-loss/SKILL.md
```

After installation, confirm the three folders arrived: `personal/`, `business/` and `shared/`, with 44 skill directories between them and one `SKILL.md` in each. The repository holds 62 files in total, so 18 files sit alongside the skill definitions.

If you are using Wilson, confirm discovery from `~/.openaccountant/skills/` before trusting a skill's tool calls; the README lists that path as the only one Wilson reads.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| bank-sync | Pass | Warn | Pass |
| contractor-tracking | Pass | Pass | Pass |
| rental-property | Pass | Pass | Pass |
| cash-flow-forecast | Pass | Pass | Pass |

Four of the 44 listings carry published verdicts, so this is a sample rather than a clearance. The Socket Warn on `bank-sync` is the one to read closely: the skill describes connecting an account through Plaid, which means credentials and a third-party data flow, and no instruction file can make that safe on its own. Do the account connection through the vendor's own flow and give the agent exports instead.

## Limitations

- Snapshot data, verified 2026-11-13: 21,037 combined installs across 44 indexed listings; 120 GitHub stars; MIT license; last pushed 2026-04-09. Counts drift over time.
- The last push was April 2026. Nothing here is stale in a way that breaks, but tax thresholds, mileage rates and nexus rules change annually, so treat the numbers in the tax skills as starting points to verify against the current year.
- The account-specific skills assume a bookkeeping workflow rather than any particular accounting platform. There is no platform connector in the tree, so the agent works from exports or from Wilson's own data layer.
- The agent does the arithmetic. Every figure a skill produces is a prompt-level calculation over data you supplied, so reconcile anything that will be filed or sent before it leaves the building.
- Tax content is US federal and state. Schedule C, MACRS, Section 179, safe harbour estimates and state nexus are named explicitly, and nothing maps to another jurisdiction's rules.
- The README points to a paid Pro tier for chain orchestration and premium tools. The 44 skills here are the open part.

## Related

- [Finance Skills - Financial Analysis for Agents Setup](/hermes/skills/catalog/finance-skills-setup)
- [Awesome Finance Skills - Market Analysis Pack](/hermes/skills/catalog/awesome-finance-skills-setup)
- [Metabase Skills - BI and Dashboard Agent Suite](/hermes/skills/catalog/metabase-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `import-transactions`, `smart-categorize` and `month-end-close` together. The three form the loop that everything else assumes has already run.
- Run `--list` first and install by name. Forty-four skills is more surface than most agents need, and every installed skill is context the agent carries.
- Keep a `references/` folder of your own categories and entity names beside the tax skills. The procedures are generic; the chart of accounts is not.
- Ask for the working, not just the number. These skills will show the calculation if you ask, and that is the difference between a figure you can defend and one you cannot.
- Do a full month by hand once before automating it. The close checklist is a good map of what your bookkeeping actually involves, and it will show you which skills you do not need.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
