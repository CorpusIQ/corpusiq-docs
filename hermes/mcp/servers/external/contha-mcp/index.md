---
title: "Contha MCP - Small-Business Books Read by an Agent"
description: "A keyless demo of small-business books over MCP: 22 read tools across personal and business money, a Schedule C worksheet and a tax estimate you can check."
category: "Finance / Accounting"
stars: "0 (github.com/noahowsh/contha-claude, MIT; the hosted endpoint needs no install)"
added: 2026-11-18
source: "the mcp.so submission queue entry #7627 filed 2026-11-18T02:34:39Z, fourteen of twenty-two tools driven against the vendor's no-login demo endpoint on 2026-11-18, and the live protected-resource and authorization-server documents on the production host"
relevance: ★★★
tags: [accounting, bookkeeping, small-business, sole-proprietor, schedule-c, cash-flow, budget, net-worth, personal-finance, oauth, remote, mcp]
last_updated: "2026-11-18"
---

# Contha MCP

**A sole proprietor keeps two sets of money in one life.** The personal card buys the laptop. The business account pays the contractor. The tax return wants the second sorted by line, the household wants the first sorted by category, and most tools pick one side.

Contha keeps both sides in one set of books and exposes the whole thing over MCP: 22 read tools that answer what is left to spend, what is owed in tax, where the money went, and which charges were filed on the wrong side. The write tools exist on the production endpoint and are deliberately absent from the demo.

```text
Server type:   remote Streamable HTTP (hosted)
Demo:          https://demo.contha.com/api/mcp   no credential, sample books
Production:    https://app.contha.com/api/mcp    OAuth 2.1
Server:        contha-demo, version 0.4.0, protocol 2025-06-18
Auth:          demo none; production OAuth with PKCE S256
               scopes read, write; dynamic client registration open
Tools:         22 exposed on the demo, all read-only
               22 read and 6 write on the production service, per the vendor
Registry:      no official registry entry this pass
Queue:         mcp.so #7627, filed 2026-11-18T02:34:39Z
License:       MIT, github.com/noahowsh/contha-claude
```

## The evidence tier

Keyless and driven, which is rare on this class. `initialize` answered **200** on the demo host with no header of any kind and returned `serverInfo` `contha-demo` **0.4.0** on protocol **2025-06-18**. `tools/list` returned **22** schemas. Fourteen of the twenty-two were called and answered with live data, and three failure paths were called on purpose.

The production host is the opposite shape and states it plainly:

```text
POST https://app.contha.com/api/mcp     401
www-authenticate: Bearer realm="contha", error="invalid_token",
  resource_metadata="https://app.contha.com/.well-known/oauth-protected-resource"
```

Both documents resolve on the same host, which is the cleanest OAuth deployment seen on this surface for weeks: the protected-resource document names scopes `read` and `write` with `bearer_methods_supported: ["header"]`, and the authorization-server document carries `authorization_endpoint`, `token_endpoint`, `registration_endpoint`, `response_types_supported: ["code"]`, `code_challenge_methods_supported: ["S256"]` and `token_endpoint_auth_methods_supported: ["none"]`, which is a public client with dynamic registration and no secret to paste.

No customer books were read, because no account was opened. Everything below is either the demo's own sample books or a surface any reader can re-measure in two requests.

## Two books, and the audit that proves it

`get_overview` answers the operator question first: **$40,380.70** free to use, against **$60,875.91** of net worth split into **$45,509.84** cash, **$17,244.34** invested and **−$1,878.27** owed on cards. The tool prints its own working, and the arithmetic closes to the cent:

```text
cash 45,509.84  −  cards 1,878.27 − goals set aside 1,595.50
                − bills due in 30 days 296.38 − tax due on the return 1,358.99
              = 40,380.70
```

This month splits the same way: **$6,500.00** in business income against **$366.94** of business spend, and **$508.79** of personal spend, for **$875.73** spent on both sides together.

The tool that earns the integration is `audit_misfiled_business`. It returns charges from known business vendors that are either uncategorised or filed on the personal side, largest first, and on the demo books it returns **five** findings totalling **$115.98**: one OfficeMax charge at **$55.98** and four Figma charges at **$15.00** each, every one with a null category and the matched vendor named. Fifty-five ninety-eight plus four times fifteen is one hundred and fifteen ninety-eight, and that is the whole point of the tool: a business expense that never reaches the Schedule C is a deduction an operator pays tax on.

## The tax worksheet, and the one number that does not close

`get_schedule_c` returns a 2026 Schedule C built from the transactions: gross receipts **$71,500.00**, total expenses **$11,213.65**, tentative profit **$60,286.35**. Four lines carry the expenses and they sum exactly:

```text
line 9   car and truck          91.20    2 transactions
line 11  contract labor      7,258.99   10 transactions
line 18  office expense        166.32   11 transactions
line 27a other expenses      3,697.14   55 transactions
                             ---------
                            11,213.65
```

`get_tax_estimate` then walks the same income through self-employment tax and reproduces the standard arithmetic: net profit **$60,286.35**, self-employment taxable earnings **$55,674.44**, Social Security at **12.4%** giving **$6,903.63**, Medicare at **2.9%** giving **$1,614.56**, combined self-employment tax **$8,518.19**, half of it deducted at **$4,259.10**, adjusted gross income **$56,027.25**, the qualified business income deduction **$7,985.45**, federal taxable income **$31,941.80**, federal tax **$3,585.02** and New York State tax **$2,428.47** on the 2026 IT-2105-I rates with the recapture worksheet.

The ambiguity is worth an operator's attention rather than a gloss. Three figures sit in the same response and they disagree:

```text
headline       $1,358.99 due with the return on Apr 15   (and repeated in get_overview)
balanceDue    −$1,668.32        tax on income so far, less $16,200 paid
quarterly     toPay 0.00 on all four installments, $1,511,232 required,
              $1,620,000 paid, sum of installments $1,511,232 against
              requiredAnnual $1,511,233
```

The headline is internally consistent: `get_overview` and `get_tax_estimate` both print **$1,358.99**. It is not reproducible from the fields published beside it, and a fourth reading (projected full-year **$16,791.48** less **$16,200.00** already paid, which is **$591.48**) fits neither. Recorded as measured, not reconciled. The tool says its own limits in every tax response: these are estimates from the transactions and the situation on record, not tax advice, and the exact figure belongs with an accountant before anything is paid or filed.

## Units, defaults and the budget header

Three conventions are worth knowing before wiring this into an agent, because each one changes an answer.

Money arrives twice: bare integers in cents, and a `readable` string. `12345` is **$123.45**, and most objects carry both, so an agent that quotes the integer reports a hundredfold error. The tools that matter state the rule in a `units` field rather than leaving it to the reader.

`get_budget` pools carried-in money into its header. Planned **$1,695.00**, spent **$875.73**, and `leftToSpend` **$1,869.27**, which is not the subtraction: the Equipment line carries **$1,050.00** in from earlier months, and **875.73 + 1,869.27 = 2,745.00 = 1,695.00 + 1,050.00**. A reader who checks the header against `planned − spent` finds a figure **$1,050.00** too high and concludes the tool is wrong. It is right, and the `carriedIn` field on the individual line is where the extra money is declared.

Defaults are dated rather than lifetime. `get_cashflow` with no arguments returned **2026-08-21 to 2026-11-18**, income **$19,500.00**, spend **$4,200.33**, net **$15,299.67**, with the first and last months marked `partial` and their covered ranges printed. `get_spending_trends` with no arguments returned January 1 to today across **eleven** months. A question asked without a range gets ninety days of cash and a year of categories, which is two different windows from one conversation.

`get_year_end_package` takes a `kind` and returns CSV text with the filename on line one and the line descriptions in column two, so a Schedule C export reads `1,Gross receipts,,71500.00,71500.00`. The enum is exact: `transactions`, `schedule-c`, `mileage`, `k1`, `1099`, `pnl`.

### Can an agent see both sides of the books?

Yes, and that is the design. Every tool that reports money carries a `side` or a `scope`: `get_transactions` filters on the side of the books, `get_budget` returns both sides with a `side` per line, `get_cashflow` and `get_spending_trends` take `combined` as the default scope. The Schedule C tools read the business side only, and `get_profit_and_loss` states its own basis: cash basis from the business books, which differs from the Schedule C profit because the return adds mileage and leaves out charges never filed to it.

### What does it cost, and what does the free plan cover?

The vendor publishes a free plan with Personal at **$5** a month and Business at **$10** a month. The Business plan is the one that carries the personal and business split, the profit and loss, and the Schedule C worksheet. The demo endpoint used in this guide is open with no login and reads sample books only, so every number above is reproducible without an account and without a payment method.

### What can the agent actually change?

On the production service, six write tools file transactions, add cash transactions, and maintain rules, budgets, mark bills and goals. The vendor states the boundary directly: it can never move money. The demo exposes none of them, and a call to a production-only name returns `Unknown tool: add_cash_transaction` rather than a permission error, which is the cleanest way to see the two surfaces are genuinely different builds.

## Connecting

The demo, for evaluation with no account:

```json
{"mcpServers": {"contha-demo": {"type": "http", "url": "https://demo.contha.com/api/mcp"}}}
```

The production endpoint, for real books:

```json
{"mcpServers": {"contha": {"type": "http", "url": "https://app.contha.com/api/mcp"}}}
```

In Claude, Settings then Connectors then Add custom connector, paste the URL, and press Allow on the page Contha opens. The consent screen offers `read` and `write` separately, and the vendor says write needs explicit consent at that page. Dynamic client registration is open, so there is no client id and no secret to request first.

Two cautions for an operator. The demo answers with a full set of books that are not yours: state that plainly in any answer an agent builds from it. And the tax tools are estimates with a fixed prompt to say so, which is the right behaviour and still a statement that needs a human signature before money moves.

## Sources

- Demo endpoint: https://demo.contha.com/api/mcp
- Production endpoint: https://app.contha.com/api/mcp
- Protected resource metadata: https://app.contha.com/.well-known/oauth-protected-resource
- Authorization server metadata: https://app.contha.com/.well-known/oauth-authorization-server
- Vendor AI documentation: https://contha.com/ai
- Repository: https://github.com/noahowsh/contha-claude
- Submission: the mcp.so queue as #7627 on 2026-11-18
