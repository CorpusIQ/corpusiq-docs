---
title: "AllClear Lending MCP - Named Lenders, Real Programs"
description: "Keyless MCP that names the lenders funding a business by industry and state, with each program's source page and the next option after a decline."
category: Finance
stars: n/a (hosted vendor server, no public repository yet)
added: 2026-11-04
source: "chatmcp/mcpso submission #6718 on 2026-11-04 at 10:02:28Z, plus a keyless driven session on https://fundingos.consultincllc.workers.dev/mcp: initialize 200 as allclear-lending 0.1.0, tools/list returning 8 tools, and five calls (find_lenders, industry_overview, state_rules, next_best_option twice, the first rejected against the decline enum)"
relevance: ★★★
tags: [smb-lending, working-capital, sba, lenders, decline-fallback, finance, remote-mcp]
last_updated: "2026-11-04"
---

# AllClear Lending MCP

**The question a business owner asks when the bank says no is not "what are the rates". It is "who actually funds a business like mine, and what do I do next". Search engines answer that question with affiliate listicles that rank by payout, and an assistant with no data answers it with generic advice about improving cash flow.**

AllClear Lending is a named-lender index built for that exact question. The MCP server exposes the index, each state's brokering rules, and a published fallback ladder for the moment a lender declines:

```
Server type: Remote (Streamable HTTP, stateless, JSON responses)
Endpoint:    https://fundingos.consultincllc.workers.dev/mcp
Health:      https://fundingos.consultincllc.workers.dev/mcp/health
Auth:        none (optional X-AllClear-Key header for a caller's own usage key)
serverInfo:  allclear-lending 0.1.0
Tools:       8 read-mostly tools (7 read, 1 outcome reporter)
Registry:    io.github.lunarpenguin214/allclear-lending
Directory:   dated 2026-11-03 at the time of this pass
Site:        fundingos.consultincllc.workers.dev/agents
```

A keyless `initialize` answered **HTTP 200** and `tools/list` returned all **8** tools, so nothing here is documented from a card.

## The directory answers with institutions and receipts

`find_lenders` takes an industry, a state, a product, an amount band, time in business, credit band and citizenship status, and returns named programs ranked cheapest-suitable first. Restaurants in Texas returned **12 matches** in the directory with **4** returned at the requested limit, and each row is a record rather than a link farm:

- **Celtic Bank**, a bank, for hotel and restaurant FF&E financing plus restaurant construction as special-use commercial real estate, national, up to **$2 million** for equipment at up to **100 percent LTV** on its own page, broker path `referral_partner` through a partner portal, `confidence: sourced`, with the institution's own URL attached.
- **Ready Capital**, an SBA lender, for SBA 7(a) restaurant acquisition lending including real estate, working capital and equipment, with a published restaurant spotlight deal cited as the source.

The confidence field is the detail that separates this from a lead-gen directory. A row is `sourced` when the institution's own page states the program, and the responses carry rows explicitly labelled **unverified** when only a single source exists. The server's own source note says it: directory facts come from the institutions' pages at the date shown, and unverified rows have one source, so confirm terms with the lender.

## The industry record is the part an owner should read first

`industry_overview` returns a per-industry page of the economics behind the question. For restaurants in Texas this pass returned ease tier **A** with an ease score of **88**, NAICS **7225 / 7224**, **7** product types that fit (MCA and revenue-based, business line of credit, term loan, SBA 7(a) and 504, equipment finance, business credit cards, owner-occupied CRE 504), SBA eligible **yes**, and **14** lenders serving against **0** restricting.

The named list is where the value sits, because it distinguishes routes that are genuinely available from routes that only exist inside a platform: **OnDeck**, **Bluevine**, **Fundbox**, **National Funding**, **Rapid Finance**, **Fora Financial**, **Credibly**, **Huntington**, **Newtek**, **Celtic Bank** and **Byline Bank**, with **Toast Capital** and **Square Loans** flagged as embedded and **not brokerable**, and a franchise-restaurant vertical marked status unverified for 2026.

The `why` field cites its own arithmetic rather than asserting a verdict: products **7** of a possible **28**, serving **14** and restricting **0** of **40**, SBA yes on **10**, and the claim that restaurant NAICS **722511** ranks first by 7(a) loan count with **16,354 loans** across FY20 to FY25 from a third-party FOIA tally. A `verifier_note` then carves out the exception: nightclubs are a restricted sub-segment. A tool that names its own exception is a tool whose data has been checked against something.

## The decline ladder is the product, and its input is a closed set

`next_best_option` takes *why* the business was declined rather than *that* it was. The reason is an enum, and the server enforces it: a call with `"credit"` was rejected with `MCP error -32602` listing all fifteen accepted values, from `low_personal_credit`, `debt_load`, `under_6_months_in_business`, `low_revenue`, `no_collateral` and `too_many_existing_advances` through `sba_quality_declined`, `deal_too_big`, `non_citizen_owner` and `other`.

The valid call for `low_personal_credit` on a Texas restaurant returned the situation it recognised, low personal FICO below roughly 570 with revenue above $15k a month, and then two rungs: a **Bitty micro advance**, and **Credibly** at a 500 to 550 floor if revenue and time in business fit, with the instruction to show the true cost in math and never to call an MCA a loan, plus a dated come-back plan of CreditStrong, Self and a secured card if both decline. The industry fallback line added a kitchen equipment lease, a small Bitty advance, a nonprofit 0 percent loan for low-income borrowers and a 0 percent business card.

The stated principle is the whole design in one paragraph: every decline comes with a next step, options are ordered cheapest for the business owner first, a revenue-based advance is a purchase of future sales rather than a loan, and it is shown last with its full cost. That ordering is a policy decision against the industry default, where the highest-payout product tends to be presented first.

## State rules, and the honest gap inside them

`state_rules` returns what an unlicensed out-of-state broker would need in a state, by lane: investor real estate, consumer home loans, working capital, SBA and cards. For Texas the general block is specific and dated: **HB 700** requires brokers of sales-based financing to register with the OCCC through NMLS by **2026-12-31** with filings open since 2026-09-01; SBA 7(a) and 504 lender-paid referral fees go on Form 159; and since 2026-03-01 any non-citizen ownership makes a business SBA-ineligible.

The gap is equally explicit. The same response carried `researched: false` with each lane's status returned as `unknown` and the phrase "not researched yet", so the tool states which parts of a state it has not covered rather than implying a complete answer. A caveat field labels the whole block as research notes and not legal advice. That is the failure mode of every compliance surface, incompleteness presented as coverage, and it is reported here instead of hidden.

## The outcome graph, and the conflict it carries

`report_outcome` writes one submission result into a shared graph: which lender, what kind of file by bands, the decision, the decline reason code, days to decision and a `reporter_key`. No names, no amounts. `lender_stats` reads it back as approval rate, funded rate and median days to decision per program, institution, industry or state.

That closes a loop nothing else in this catalogue closes, because approval rates by lender and industry are otherwise folklore traded between brokers. It also creates a conflict worth naming: the same operator can report outcomes and read statistics, the sample is whoever chooses to report, and a `reporter_key` is self-declared. Early statistics from a thin graph are a signal about the reporters as much as about the lenders. Treat the field as evidence of direction, never as a measured market rate, until the graph is deep.

`estimate_match` is the softer sibling and its output shows why: it returns program *types* with typical ranges from category data rather than named institutions, and every response carries the disclaimer that this is an estimated match from the answers and not an offer of credit. The notice is blunt about the vendor's own position: AllClear Capital is not a lender or a broker, nothing is an approval or pre-approval, and lenders decide.

## FAQ

### Does calling it cost anything or need an account?

No. `initialize`, `tools/list` and five tool calls ran keyless in this pass. An `X-AllClear-Key` header is accepted for a caller who wants their own usage key, and it is optional.

### Is this a lender or a lead broker?

Neither, on the server's own statement. It returns directory facts from institutions' published pages and an outcome graph from reported results, and every answer restates that it is not an offer, approval or pre-approval.

### What if my industry or state is not in the directory?

`find_lenders` returns the industries it matched and the total available, so a miss is visible as zero matches rather than a vague answer, and `industry_overview` states the ease tier and the lenders serving it where the vertical is covered. The directory is US-focused.

### Can an agent trust the approval-rate numbers?

Only as direction. The graph is fed by whoever chooses to report with a self-declared key, so rates reflect the reporter population before they reflect the lender. The per-lender directory record, with a source URL and a confidence label, is the more defensible half of the server.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [MonitorBankRates MCP - Deposit and Loan Rate Benchmarks](/hermes/mcp/servers/external/monitorbankrates-mcp/)
- [Hercules MCP - US Property Records and Investor Leads](/hermes/mcp/servers/external/hercules-property-mcp/)
- [ExitValue.ai M&A Multiples MCP](/hermes/mcp/servers/external/exitvalue-ai-mcp/)
- [DFX Intelligence MCP - Private Credit With Citations](/hermes/mcp/servers/external/dfx-intelligence-mcp/)
