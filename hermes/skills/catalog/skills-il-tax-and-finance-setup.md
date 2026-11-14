---
title: "Israeli Tax and Finance Skills - 50-Skill Setup"
description: "skills-il/tax-and-finance: 2.4K combined installs across 50 listings, 45 skills for Israeli tax, VAT, invoicing, payroll and payment gateways."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/skills-il-tax-and-finance-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "israeli tax", "finance", "vat", "payments"]
---

# Israeli Tax and Finance Skills - Setup Guide

**Source:** [skills-il/tax-and-finance](https://www.skills.sh/skills-il/tax-and-finance) via skills.sh - 2.4K combined installs across 50 indexed listings; first seen Nov 13, 2026 (evening sweep)

**GitHub:** 39 stars, MIT licence, `master` branch, last pushed 2026-11-11, 45 `SKILL.md` files in one-directory-per-skill folders at the repo root, 491 files in total

**Category:** Israeli tax, VAT, invoicing, payroll and payment gateway workflows

**Quality Tier:** 🟡 Yellow - 45 in-tree skills with an MIT licence and no failing sampled verdicts, but small per-skill install counts and six listings with no resolvable SKILL.md.

The tax and finance pack from Skills IL, a GitHub organisation that curates AI agent skills for Israeli developers, covers the operational surface of Israeli money: VAT reports, invoicing, payroll, pension, tax withholding, bank data and six local payment gateways. The install index counts 50 listings against 45 resolved SKILL.md files on the `master` branch.

The ten most-installed skills span freelancer operations, VAT reporting, bank transaction analysis, pension navigation, currency conversion and three payment gateways. Many of these skills open with their own "Not tax advice" or "Not a filed return" disclaimer, so the pack produces working figures and draft documents rather than filing anything on your behalf.

## Installation

The README keeps installation to two commands: install a single skill through Claude Code, or clone the whole repository.

```bash
# Install one skill via Claude Code
claude install github:skills-il/tax-and-finance/israeli-payroll-calculator

# Or clone the full repo
git clone https://github.com/skills-il/tax-and-finance.git
```

The README also documents per-skill helper scripts, for example `calculate_vat.py` for VAT reporting and `categorize_invoices.py` for invoice organising, so several skills ship executable helpers alongside their SKILL.md.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| israeli-freelancer-ops | 190 | Daily operations for Israeli freelancers: invoice aging, collection reminders, VAT and Bituach Leumi deadline alerts, osek patur threshold monitoring and accountant packages. |
| israeli-vat-reporting | 189 | Preparing and validating Israeli VAT reports (Doch Maam) for monthly, bi-monthly and annual cycles, including zero-rated exports and exempt transactions. |
| israeli-bank-connector | 181 | Analysing Israeli bank transactions and spending patterns, categorising merchants and pairing with bank MCP servers for financial-analysis workflows. |
| israeli-pension-advisor | 180 | Navigating keren pensia, bituach menahalim and keren hishtalmut, with Form 161 severance handling, Tikun 190 deposits and retirement planning. |
| shekel-currency-converter | 170 | Converting to and from the shekel at Bank of Israel representative rates (shaar yatzig), including which date's rate applies to a transaction. |
| israeli-arnona-optimizer | 170 | Estimating municipal property tax (arnona) by municipality, zone and usage type, checking discount eligibility and drafting appeal letters. |
| israeli-crypto-tax-reporter | 169 | Computing cryptocurrency capital gains tax with FIFO cost basis, classifying DeFi income and generating Form 1399 advance-payment data. |
| cardcom-payment-gateway | 168 | Integrating Cardcom payment processing with tokenization, recurring billing and automatic Israeli tax invoice creation. |
| tranzila-payment-gateway | 161 | Integrating Tranzila payments: iframe flow, tokenization, tashlumim installments, refunds, 3D Secure and Bit wallet. |
| israeli-payment-orchestrator | 159 | A unified routing and fallback layer across Cardcom, Tranzila, PayMe, Meshulam, iCredit and Pelecard. |

The remaining 40 indexed listings range from 1 to 34 installs.

## Why This Matters for Hermes Agents

Israeli tax and payments are dense with Hebrew-specific acronyms and forms: Doch Maam, nikui mas, shaar yatzig, arnona, tashlumim. A generic agent asked about these invents plausible-sounding answers. These skills encode the actual thresholds, forms, deadlines and gateways, so an agent produces a real VAT worksheet or a real payroll breakdown instead of a confident guess.

The payment gateway skills are the clearest example. Six local processors, Cardcom, Tranzila, PayMe, Meshulam, iCredit and Pelecard, each have their own tokenization and installment conventions, and the orchestrator skill layers a unified routing and fallback abstraction over them. A general-purpose coding agent knows none of these names.

The disclaimers are the honest signal. Several skills state up front that they are not tax advice, not a filed return, not a licensed appraisal. That is the right contract for agent work: the output is working figures and drafts that a human or an accountant reviews, not a filing the agent submits.

## Usage

| You say | What happens |
|---|---|
| "Prep my bimonthly VAT report for this period" | Runs `israeli-vat-reporting` and returns a validated Doch Maam worksheet. |
| "Categorize my bank transactions and flag merchant spending" | Runs `israeli-bank-connector` and groups Israeli bank and card data into categories. |
| "How much arnona will this apartment cost and can I appeal it?" | Runs `israeli-arnona-optimizer` and returns a zone-based estimate plus a draft appeal letter. |
| "What is the crypto capital gains tax on these trades?" | Runs `israeli-crypto-tax-reporter` and computes FIFO gains with Form 1399 advance-payment data. |
| "Which Israeli payment gateway should I integrate, and how?" | Runs `israeli-payment-orchestrator` and compares Cardcom, Tranzila, Pelecard and the rest. |
| "Convert this invoice amount to shekels at the right rate" | Runs `shekel-currency-converter` and applies the Bank of Israel representative rate. |
| "I am a US citizen freelancing in Israel, what do I owe?" | Runs `american-freelancer-israel-tax` and projects US self-employment tax on top of Bituach Leumi. |

## Verification

Probe three skills on the branch before installing. All three return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-freelancer-ops/SKILL.md | head -20
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-vat-reporting/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/skills-il/tax-and-finance/master/israeli-payment-orchestrator/SKILL.md
```

The path layout is one directory per skill at the repo root on the `master` branch, for example `israeli-freelancer-ops/SKILL.md`. Point verification scripts at `master`, not `main`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| israeli-freelancer-ops | Pass | Pass | Warn |
| israeli-vat-reporting | Pass | Pass | Warn |
| israeli-bank-connector | Pass | Warn | Pass |
| israeli-pension-advisor | Pass | Pass | Pass |

All four sampled skills pass the Gen Agent Trust Hub, and none carry a failing verdict. The two most-installed skills carry a Snyk Warn and israeli-bank-connector carries a Socket Warn, so read those files before scheduling anything. The other 46 listings publish no verdict, which is not the same as a pass.

## Limitations

- Snapshot data, verified 2026-11-13: 2,426 combined installs across 50 indexed listings; 39 GitHub stars; MIT licence; last pushed 2026-11-11. Counts drift over time.
- Many skills carry their own "Not tax advice", "Not a filed return" or "Not a licensed appraisal" disclaimer. The pack produces working figures and drafts, not filed documents, and nothing here replaces an accountant.
- Six indexed listings resolve to no SKILL.md in the current tree: israeli-payroll-calculator, israeli-e-invoice, israeli-annual-reports, green-invoice, gws-israeli-business-sheets and tase-stock-analyzer. They are index-only.
- The default branch is `master`, not `main`. Keep it in any raw URL or verification script.
- Several skills depend on external services: israeli-bank-connector pairs with bank MCP servers, and the payment gateway skills need merchant accounts with Cardcom, Tranzila, Pelecard or the others before they can do anything live.

## Related

- [Finance Skills - Financial Analysis for Hermes Agents](/hermes/skills/catalog/finance-skills-setup)
- [Open Accountant Skills - Bookkeeping and Tax Setup](/hermes/skills/catalog/openaccountant-skills-setup)
- [Awesome Finance Skills - Market Analysis Pack](/hermes/skills/catalog/awesome-finance-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `israeli-vat-reporting` or `shekel-currency-converter`. They are self-contained, produce a single document or number, and show you whether the agent's output matches the Tax Authority's rules before you hand it anything bigger.
- Keep the `master` branch in every raw URL and clone command. A script that defaults to `main` will 404 on this repo.
- Treat the disclaimers literally. The outputs are working figures for an accountant, not filings, so route anything that will actually be submitted through a human.
- The payment gateway skills expect merchant accounts. Set up sandbox or test credentials with Cardcom, Tranzila or Pelecard before wiring in production keys.
- Pair `israeli-bank-connector` with the bank MCP servers it names if you want live transaction data instead of pasted CSVs.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
