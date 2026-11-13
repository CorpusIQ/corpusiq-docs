---
title: "CalcBloc MCP - Payroll Numbers With a Source Attached"
description: "Driven locally: a $100,000 California salary decomposed to the cent, 2026 tax tables cited to the IRS and the FTB, and coverage stated three ways"
category: "Finance / HR"
stars: "0 (MIT code, CC BY 4.0 data, github.com/itmarkerz/calcbloc-mcp)"
added: 2026-11-13
source: "the submission queue entry #7260, the official registry records io.github.itmarkerz/calcbloc-mcp 0.1.0 and 0.1.1, npm calcbloc-mcp 0.1.1, the vendor page calcbloc.com/developers, and a local stdio session on this host: initialize, tools/list and nine tools/call requests against the published package"
relevance: ★★★
tags: [payroll, tax, salary, employer-cost, finance, hr, citations, stdio, keyless, mcp]
last_updated: "2026-11-13"
---

# CalcBloc MCP

**A payroll number without its source is a rumour with a decimal point.** Ask a language model what someone on $100,000 takes home in California and you get a fluent figure built from whatever tax year happened to be in the weights, with no way to tell which bracket set, which standard deduction, or which year it used. The person who has to defend that number in a hiring conversation - or a spreadsheet - cannot.

CalcBloc is a small tax and salary data product that does the opposite of guessing: every answer comes back with the **tax year**, the **official source** behind each figure, and the **date that source was checked**, and the same dataset is exposed as a remote REST API and as a local MCP server you run yourself. The MCP server is the surface measured here - installed from npm, driven over stdio, and re-checked by hand.

```text
Server type:   local stdio, TypeScript, npm calcbloc-mcp 0.1.1
Server:        calcbloc-mcp, title "CalcBloc tax and salary calculator",
               protocol 2025-06-18, capabilities: tools only
Registry:      io.github.itmarkerz/calcbloc-mcp 0.1.0 and 0.1.1
Licence:       MIT (code), CC BY 4.0 (data)
Tools:         5 - take-home pay, employer cost, compare, tax tables, countries
Coverage:      37 countries with tax tables, 12 with take-home calculations
Cost:          keyless to start (5 requests a minute, 50 a day);
               a free key lifts it to 5,000 a day
```

## The evidence tier

Installed and driven. `npm install calcbloc-mcp` pulled **0.1.1**, the stdio server answered `initialize` with `serverInfo` `calcbloc-mcp` **0.1.1**, title *CalcBloc tax and salary calculator*, protocol **2025-06-18**, `capabilities` carrying `tools` and nothing else. **Nine `tools/call` requests were run** across all five tools, including three deliberate failures.

`io.github.itmarkerz/calcbloc-mcp` answers in the official registry at **0.1.0** and **0.1.1**, and npm serves the same package with `mcpName` declaring that registry name - so the package, the registry record and the server identity agree, which is not guaranteed in this ecosystem.

The `instructions` string tells the caller the shape of the dataset before any tool is used: calculations exist for **some** countries and tax tables for **all listed countries**, the current tax year is used by default, and `list_countries` should be called when you are unsure which countries, regions or country-specific options are supported. That last sentence is load-bearing, and the reason is a schema limitation documented below.

## Coverage is stated three different ways

This is the first thing to fix in your head before asking it anything, because the counts do not agree across the vendor's own surfaces:

| Surface | Says |
|---|---|
| npm package description and registry record | *37 countries* |
| `list_countries` (measured) | **37** countries with tax tables, **12** with take-home pay, employer cost and compare |
| calcbloc.com/developers header | *13 countries* |

The MCP tool is the honest one, because it states both numbers and names which tools work per country. When the list was read, the twelve with full calculation coverage included the US, UK, Germany, France, Netherlands, Spain, Singapore, Australia, New Zealand, Canada, Ireland and India, while the rest - Iceland, Malta, Lithuania, Bulgaria, Cyprus, Croatia, Latvia, Greece, Estonia, Slovakia, Romania, Norway, Czechia, Luxembourg, Poland, Hungary, Finland, Slovenia, Austria, Sweden, Switzerland, Denmark, Portugal, UAE and Italy - carried **tax tables only**. The developers page still advertising *13 countries* against 37 tables and 12 calculators is drift, not a different measurement, and it is the kind of drift that makes a buyer distrust the one number they can check.

Practical consequence: `get_tax_tables` works for any of the 37. `calculate_take_home_pay` and `calculate_employer_cost` work for 12. Ask for a calculation in a tax-table-only country and the tool has nothing to compute, which the instructions say plainly and the error text does not always repeat.

## What the five tools do

| Tool | Required | Optional | What comes back |
|---|---|---|---|
| `calculate_take_home_pay` | `country`, `gross_salary` | `region`, `year`, `options` | net pay, total deductions, effective rate, a line-by-line per-period and per-year breakdown, the inputs it used, and every official source with its check date |
| `calculate_employer_cost` | `country`, `gross_salary` | `region`, `year`, `options` | salary plus employer social security, payroll taxes, pension and other on-costs, broken out, with sources |
| `compare_countries` | `country_a`, `country_b`, `gross_salary` | `currency`, `region_a`, `region_b` | the same salary in two countries, converted at the European Central Bank reference rate, with a plain-English summary |
| `get_tax_tables` | `country` | `year`, `region`, `group`, `sections` | the brackets themselves - income tax, employee, employer and other - each band with its rate, plus the source and `status` |
| `list_countries` | none | `country` | coverage per country, and with a country, its regions and accepted options |

Every answer ends with an attribution line and a link tagged `utm_source=calcbloc-mcp`, which is the licence bargain: the data is CC BY 4.0 and the free API key requires a visible "Data by CalcBloc" link wherever the figures appear.

## Driving it: $100,000 in California

```json
{"country": "us", "region": "california", "gross_salary": 100000}
```

came back, tax year **2026**, as:

```text
Take-home pay:            USD 72,319.60 a year
Total deductions:         USD 27,680.40
Effective deduction rate: 27.68%

Per year, USD
- Gross pay:              100,000.00
- Federal income tax:     -13,170.04
- Social Security:         -6,200.00
- Medicare:                -1,450.00
- State income tax:        -5,560.36
- CA SDI:                  -1,300.00
- Take-home pay:           72,319.60
```

with a per-paycheck column on a biweekly frequency, the note that the federal side assumes a Form DE 4 status of *Single or Married (with two or more incomes)* with one withholding allowance, the resolved inputs (`region=ca`, `filing_status=single`, `frequency=biweekly`, `retirement_pct=0`), a link to the calculator page, a link to the tax tables, and four official sources with their check dates - the California Franchise Tax Board's 2026 indexing notice (checked **2026-11-09**) and the EDD's Publication DE 44 (checked **2026-10-16**) among them.

### The hand check

The numbers reproduce, and the reproduction is worth doing once because it shows what the four-cent difference is.

The federal brackets the tool itself returns for **2026 single** are 10% to 12,400, 12% to 50,400, 22% to 105,700, 24% to 201,775, then 32%, 35% and 37%, sourced to **Rev. Proc. 2025-32** and the 2026 Publication 1040 tax tables (early-release draft, checked 2026-10-20). A $100,000 salary less a **16,100** standard deduction leaves **83,900** of taxable income - which implies the deduction the engine applied, since it is not listed as a line item:

```text
1,240.00 + (50,400 - 12,400) x 12% + (83,900 - 50,400) x 22%
= 1,240.00 + 4,560.00 + 7,370.00
= 13,170.00
```

The tool reports **13,170.04**. That is not an error: it computes on a biweekly frequency and reports the per-period figure rounded to the cent, `506.54 x 26 = 13,170.04`. **Four cents a year is the price of paying in twenty-six instalments** - a small, honest artifact of the frequency parameter and a good reminder to read the per-year total rather than multiplying a paycheck by hand. Social Security at 6,200 is 6.2% and Medicare at 1,450 is 1.45% of the full salary, both matching their statutory rates.

The California side was **not** hand-verified: it depends on the state standard deduction and exemption credits, which the tool does not itemise. The 2026 Schedule X brackets it publishes do match the Franchise Tax Board's indexing notice it cites, band for band, with `status: verified`.

`get_tax_tables` with `group: "income-tax"` and `region: "california"` returned all three California schedules - single/married-filing-separately, married-filing-jointly, head of household - each band with its rate, each section sourced and dated, and the table marked *in force 2026-01-01 to 2026-12-31*. `group: "income-tax"` also accepts `employee`, `employer` and `other`.

## The defects and the friction, recorded

**The schema cannot express per-country requirements, so the failure arrives late.** `calculate_take_home_pay` declares only `country` and `gross_salary` as required, but a US calculation **also needs a state**:

```json
{"country": "us", "gross_salary": 100000}
-> isError true
   CalcBloc API error [missing_parameter]: Parameter "region" is required.
   (API docs: https://calcbloc.com/developers?...)
```

The error is clear and carries a docs link, but the requirement is invisible in `tools/list`, which is why the instructions tell the caller to run `list_countries` first. An agent that skips that call gets one wasted round trip per country.

**Enum values use hyphens where the prose uses spaces.** `group: "income_tax"` was rejected with a validation error naming the four accepted values (`income-tax`, `employee`, `employer`, `other`); the correct form works. Good error, wrong first guess.

**Unknown countries return the whole list rather than a code.** `country: "atlantis"` came back `isError: true` with all 37 country codes and names in the message - helpful to a model, verbose to a program. `gross_salary: -5` was refused earlier, by local Zod validation, with *Too small: expected number to be >0*, which is the right place to catch it.

**The keyless allowance is small and it is per minute.** Without a key the API allows **5 requests a minute and 50 a day**; the fifth call in a fast session came back `rate_limited` with a 45-second retry hint and instructions for setting `CALCBLOC_API_KEY` in the MCP client's `env` block. A free key raises it to **5,000 a day**, issued instantly, no email. The key goes in the `X-API-Key` header - the vendor explicitly refuses keys in the query string because URLs end up in logs - and the free tier carries an attribution obligation.

## Connecting it

```json
{
  "mcpServers": {
    "calcbloc": {
      "command": "npx",
      "args": ["-y", "calcbloc-mcp"],
      "env": { "CALCBLOC_API_KEY": "your-free-key" }
    }
  }
}
```

On Hermes:

```bash
hermes mcp add calcbloc --command npx --args "-y calcbloc-mcp"
```

Run it locally rather than trusting a hosted calculator: the engine is the same code the vendor's own pages run, and the sources come back with the answer, so the audit trail travels with the number.

## Questions this answers that a chat window alone cannot

### What does this hire actually cost?

`calculate_employer_cost` is the one operators skip and then get surprised by: salary plus employer social security, payroll taxes, pension and other on-costs, itemised. On a $100,000 US salary the employee side is the famous number and the employer side is the one that hits the budget.

### Same salary, two countries - who really pays more?

`compare_countries` runs both engines and converts at the European Central Bank reference rate. It returns both tax years and both source sets, so a comparison between a 2026-27 UK figure and a 2026 US figure says so instead of pretending the years align.

### Which bracket produced this number?

`get_tax_tables` returns the bands themselves, with the official notice each band came from and the date it was checked. That is the difference between a figure you can put in a board deck and a figure you have to caveat.

### Can I use it in a product?

The data is CC BY 4.0 and the code MIT; the free API key requires a visible link back. Read the licence page before shipping the figures inside a customer-facing calculator, because the attribution requirement is a condition, not a courtesy.

## Verdict

Three stars, earned on the thing this catalog keeps rewarding: **the answer carries its own provenance**. Every calculation returns the tax year, the resolved inputs, the official source per line and the date that source was checked, and every tax table publishes its bands with a status of `verified`. The coverage is large for tax tables and deliberately modest for calculations, and the tool says which is which when asked.

The defects are friction, not dishonesty: a requirement the schema cannot express, an enum that is hyphenated one way and written another, a coverage claim that has drifted to a third number on the developers page, and a keyless ceiling low enough that a real session needs the free key within minutes.

Not for you if the question is international payroll withholding on an equity package - this is salary, tax and on-cost arithmetic with a citation, not a payroll engine. Very much for you if you price roles, quote employer cost, or answer "what do they actually take home" and need the number to survive being questioned.

See also: [Worth Leaving MCP](/hermes/mcp/servers/external/worth-leaving-mcp/) for equity walk-away math, [Casus MCP](/hermes/mcp/servers/external/casus-mcp/) for French tax and legal text, and [PagoFix MCP](/hermes/mcp/servers/external/pagofix-mcp/) for EU late-payment interest.
