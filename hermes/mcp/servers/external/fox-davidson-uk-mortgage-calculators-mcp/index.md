---
title: "Fox Davidson MCP - UK Property Finance Calculators"
description: "Fifteen UK property finance tools: stamp duty across three tax regimes, bridging costs, buy-to-let stress tests and dated market rates."
category: "Finance"
stars: n/a (vendor-hosted)
added: 2026-11-22
source: "mcp.so feed card stamped 2026-11-22 10:49 (UTC) for slug fox-davidson-uk-mortgage-calculators; keyless initialize, tools/list and eight tools/call requests on 2026-11-22"
relevance: ★★★★★
tags: [uk, mortgage, stamp-duty, property, calculators, fca, keyless, remote-mcp]
last_updated: "2026-11-22"
---

# Fox Davidson UK Mortgage Calculators MCP

**Remote MCP server (Streamable HTTP, no authentication)** - fifteen property finance calculators run by a UK mortgage brokerage authorised and regulated by the Financial Conduct Authority (FRN 1056214). Every answer ships with the band table, the reviewed date and the regulatory disclaimer attached.

```
Server type: Remote (Streamable HTTP, no auth)
Endpoint:    https://mcp.foxdavidson.co.uk/mcp
Server:      fd-property-mortgage 0.6.0, protocol 2025-06-18
Tools:       15 (calculators, lender criteria, dated market rates, case studies)
Publisher:   Fox Davidson Ltd, Companies House 08430288, FCA FRN 1056214
```

## Why This Matters for Operators

Most property calculators answer one question and hide the arithmetic. This one returns the band breakdown, so the number can be checked against the tax it claims to apply, and it separates the three UK regimes that people routinely confuse: SDLT in England and Northern Ireland, LBTT in Scotland, LTT in Wales.

The second thing it does is date itself. Rates and lender criteria carry a reviewed date, and the response warns which figures are market averages rather than offers. An agent quoting a rate to a client that morning is quoting a dated figure, not a live one.

## Measured Behaviour

Eight calls were driven on 2026-11-22, all keyless. Every figure is quoted from the response.

### Stamp duty, and the five-band check

| Input | Answer | Effective rate |
|---|---|---|
| GBP 450,000, England, standard buyer | **GBP 12,500** | 2.78% |
| GBP 450,000, Scotland, first-time buyer | **GBP 17,750** | 3.94% |

Both reproduce by hand from the returned bands. England: nothing on the first 125,000, 2% on the next 125,000 (2,500), 5% on the remaining 200,000 (10,000), total **12,500**. Scotland with first-time relief: nothing to 175,000, 2% to 250,000 (1,500), 5% to 325,000 (3,750), 10% to 450,000 (12,500), total **17,750**. The arithmetic is exposed, so an operator can check it rather than trust it.

### Buy-to-let stress test, verified three ways

A GBP 250,000 loan against GBP 1,400 monthly rent at a 4.49% product rate returned:

```text
annual rent                       16,800
interest at product rate          11,225   (250,000 x 4.49%)
interest at stress rate           13,750   (250,000 x 5.5%)
ICR at product rate                1.50    (16,800 / 11,225)
ICR at stress rate                 1.22    (16,800 / 13,750)
gross yield                       6.72%
stress rate used                   5.5% personal name, notional
```

Then the verdict, with the ceiling per threshold: 125% ICR allows a maximum loan of **244,364**, 145% allows **210,658**, 170% allows **179,679**, and the case fails all three at its current size. Each maximum reproduces from the rent divided by the threshold divided by the 5.5% stress rate, to the pound. The response names the binding constraint rather than leaving the reader to find it: *reduce loan to approximately GBP 210,658 to pass 145% ICR.*

### Bridging cost, with the high net worth test attached

A GBP 300,000 facility against a GBP 600,000 property at 0.85% a month for 12 months, with a 2% arrangement fee added to the loan:

```text
gross facility        306,000     arrangement fee added to the loan
arrangement fee         6,000
total interest         32,713
repay at exit         338,713
total cost of finance  38,713     6,000 + 32,713
annualised cost        12.9%      on the 300,000 released
HNW term check         regulated, income limb false, net assets limb false,
                       high net worth qualifies false, max regulated term 12 months
```

It also returns a month by month schedule, so the interest figure can be re-added line by line.

### Lender criteria, with the boundaries named

`fd_lender_criteria_lookup` on contractor day rates returned 19 lenders held for that topic, two of which were shown:

| Lender | Weeks used | Basis | Condition |
|---|---|---|---|
| Coventry | 41 | day rate x 5 x 41 | minimum GBP 50,000 gross annualised to use the route |
| Halifax | 46 | daily rate x 5 x 46 | uses the lower of that figure and actual payslip income |

The dataset holds 27 lenders across all topics, and the response states when they were reviewed: 2026-08-31. A five-week difference between two lenders is the kind of detail that changes which case goes where.

### Dated market rates

`fd_market_rates` returned a reviewed date of 2026-11-18 and these figures with their own dates and sources:

- Bank of England Bank Rate **4.00%**, last changed 2026-11-05 (*raised from 3.75% to 4%, 8 to 1 vote*), next decision **2026-12-17**
- Residential averages, early November 2026 (Moneyfacts): all fixes 5.89%, two-year 5.97%, five-year 6.00%, ten-year 6.32%, standard variable 7.13%
- Buy-to-let averages, mid October 2026 (Moneyfacts): two-year 5.63%, five-year 6.01%
- Bridging, Q3 2026 (Bridging Trends): average monthly rate 0.77%, average LTV 59%, average completion 41 days, regulated share 45%

### It refuses outside its enums

Three argument errors, each naming the accepted set:

```text
buyer_type: Invalid enum value. Expected 'standard' | 'ftb' | 'additional' |
            'nonresident' | 'corporate' | 'commercial', received 'first_time_buyer'
ownership:  Invalid enum value. Expected 'personal' | 'ltd', received 'individual'
topic:      Invalid enum value. Expected 'contractor_day_rate' | 'retained_profit' |
            'one_year_accounts' | 'no_credit_scoring' | 'bonus_commission' |
            'foreign_currency' | 'income_multiples' | 'max_age' | 'private_banks'
```

The refusals are more useful than a guess would be: an agent learns the vocabulary from the error.

## What It Cannot Do

- It is not advice, a quote or a lending decision. The disclaimer ships inside every payload.
- The firm does not advise on lifetime mortgages or standalone regulated second charge mortgages, and the `fd_about_fox_davidson` tool says so.
- Lender criteria are published figures at a review date, not live feeds from the lenders.
- `fd_request_callback` prepares a link the person opens themselves; the model does not book anything.

## Frequently Asked Questions

### Can this calculate stamp duty for all four UK nations?

Three regimes are covered: SDLT for England and Northern Ireland, LBTT for Scotland, LTT for Wales. The response names which regime it applied and itemises every band, including first-time buyer relief.

### How current are the mortgage rates?

They are dated. The Bank Rate carried a last-change date of 2026-11-05 and a next-decision date of 2026-12-17, the Moneyfacts averages were marked early November and mid October 2026, and the whole set had a reviewed date of 2026-11-18. Treat them as a snapshot.

### Does an agent need an API key?

No. All fifteen tools answered keyless on 2026-11-22, including the calculators, the lender criteria and the rate table.

## See Also

- [Finance and property data sources in the external catalogue](/hermes/mcp/servers/external/)
