---
title: "OpenAccountants MCP - Tax Answers That Cite the Law"
description: "A keyless server with 12 tools over 2,132 tax skills in 249 jurisdictions, driven live: a VIES check that returned a real company, the authority-order"
category: "Finance and Compliance"
stars: "485 (GitHub, 2026-11-11)"
added: 2026-11-11
source: "the mcpservers.org listing openaccountants/openaccountants carrying a lastmod of 2026-11-11T11:15:29Z, the official registry records io.github.openaccountants/openaccountants 1.0.0 and openaccountants-mcp 0.1.1, the repository README and stats block, the PyPI metadata for openaccountants-mcp 0.1.1, and a live session on this host: initialize, tools/list and seven tools/call requests against https://www.openaccountants.com/api/mcp"
relevance: ★★★
tags: [tax, vat, gst, payroll, compliance, accounting, jurisdictions, vies, citations, mcp, remote, keyless]
last_updated: "2026-11-11"
---

# OpenAccountants MCP

**Every assistant answers a tax question from memory, and memory is the worst possible source.** Rates change on a budget day, thresholds move with an index, and the answer sounds exactly as confident whether it is current or three years stale. OpenAccountants is the opposite arrangement: a skill library where every figure is attached to the law that produced it, served as twelve MCP tools on a public endpoint with no account and no key.

```text
Server type:  remote Streamable HTTP, keyless
Endpoint:     https://www.openaccountants.com/api/mcp
Server:       openaccountants-mcp 1.4.0 (serverInfo), protocol 2025-03-26
Capabilities: tools, prompts (no resources)
Tools:        12 measured
Registry:     io.github.openaccountants/openaccountants 1.0.0, remote declared
Licence:      AGPL-3.0 for code, OpenAccountants Guide License for skill content
Rate limit:   x-ratelimit-limit 60, resetting each minute (read from the response headers)
Probe:        initialize, tools/list, and seven tools/call requests in one session
```

## What the server answered

`initialize` returned **200** with no credential, `serverInfo` `openaccountants-mcp` **1.4.0**, title `OpenAccountants`, protocol `2025-03-26`, and capabilities `tools` and `prompts` with `listChanged: false` on both. There is no `resources` capability, so a client should not render a resources panel. The instruction block is where the product states its own terms: every skill sets out the method, names the official source for its figures, and says whether a licensed accountant has reviewed it, across **190+ jurisdictions** including US states and Canadian provinces.

`tools/list` returned twelve:

```text
start                     entry point: intent + jurisdiction, or it asks for both
search_skills             find a skill by keyword or browse
get_skill                 open one skill by slug
search_rules              look up rates, thresholds and rules across jurisdictions
get_deadlines             filing and payment deadlines for a country or US state
list_jurisdictions        coverage list with skill counts and reviewer names
list_verifiers            the named licensed accountants behind the library
get_quote                 only when the user asks what OpenAccountants charges
validate_vat_number       live EU VAT number check
check_audit_exemption     audit threshold for a Malta private limited company
compute                   arithmetic through named, versioned engines
share_with_openaccountants  sends feedback or a review request, only on request
```

## Driven: the VAT check returned a real company

`validate_vat_number` on `LU26375245` came back **200** with `valid: true`, `country_code: "LU"`, business name **AMAZON EUROPE CORE S.A R.L.**, address **38, AVENUE JOHN F. KENNEDY L-1855 LUXEMBOURG**, `checked_at` to the millisecond, `source: "EU Commission VIES (real-time)"`, the VIES source URL, and `confirm_available: true`. The answer does not stop at the yes. It carries the next action in the server's own words: keep the VIES confirmation, number and date, as evidence for zero-rating or the reverse charge, and note that **the check confirms the number, not the treatment** of the supply.

That boundary is the reason this entry is worth a page rather than a line. A VAT lookup that returned `valid: true` and stopped would be an invitation for an assistant to then explain the treatment from memory. This one separates the verified fact from the inference and names the escalation path when the user asks for the second one.

## The preamble is the product

`search_rules` for the standard VAT rate in MT, IE and DE did **not** return a rate table. It returned a wrapper followed by **8 passages from 7 skills**, and the wrapper is the part to read:

```text
Guidance, not a certified current figure.
Official source for Germany: Bundesministerium der Finanzen.
Authority order: statute / directive > regulations > case law >
                 official rulings > commentary (persuasive only, never a
                 citation of record)
Values come from sources you fetch in this session, not from recall.
These are PASSAGES, not a rate table.
```

Two honest readings of that result. The good one: the server refuses to hand over a number without the citation machinery around it, tells the model to verify against the authority's own site, and names the authority for the jurisdiction it selected. The awkward one: a request phrased as a rate comparison came back with passages about **estimated-tax instalments in Malta**, not a MT/IE/DE rate table, so the retrieval matched the jurisdictions and not the intent. An operator asking "what is the VAT rate in Ireland" should expect the rate to arrive from `get_skill` on the VAT skill, with `search_rules` as the supporting citation rather than the answer.

## Coverage, and the field that reads zero

`list_jurisdictions` returned a per-country table. The top of it, read as counts of skills:

```text
GLOBAL 83   US 73   AU 60   ES 53   CA 47   GB 34   MT 34   DE 30
NL 28   FR 23   DO 22   ZA 22   IT 21   IN 20   GI 19   MA 19   PT 19
```

Named reviewers appear beside some of them: **Edgar Lautsyus** for Canada, **James Power** for Great Britain, **Michael Cutajar, CPA (Malta)** for Malta, **Miguel Lantigua** for the Dominican Republic, **Werner Britz** for South Africa and **Mayur Deokar** for India. And then the field that does not agree with any of it: **`accountant_verified_skills` reads 0 on every single jurisdiction**, including the six with a named lead verifier. The README's own banner claims **33 accountant-reviewed** skills. Whatever the intended meaning of the field, a per-country approved count that is zero everywhere is not an answer to "who reviewed this", and the guide records it as a defect of the listing rather than as an absence of reviewers, because `lead_verifier` and `lead_verifier_credential` carry real names.

`start` with no arguments asked for an `intent` and a `jurisdiction` and returned both lists: **16 intents** from income tax and VAT/GST through payroll, formation, crypto, transfer pricing, capital gains, tax residency, non-dom and remittance, special tax regimes and exit tax, and roughly **180 jurisdiction codes**, including sub-national ones (`CA-AB`, `EG-AE`, `EG-SA`, `EU-27`, and US states).

## Deadlines: exact where it is exact

`get_deadlines` for `DE` with the default 120-day horizon returned `upcoming_deadlines: []` and a single `recurring_rhythms` entry, `de-ustva-monthly` for the monthly Umsatzsteuer-Voranmeldung, with a link to the public tax calendar. That is the right shape for a jurisdiction whose monthly filing has no fixed calendar date inside the window, and it is honest output rather than a filled table. Asking again with a longer horizon is the documented move; a client that renders an empty list as "no obligations" would misread it, so the response carries its own `next_action` telling the model to widen the horizon or report the rhythm instead.

## The calculator is public code and a broken door

`compute` is the most interesting tool and the one that does not work over MCP today. It exposes **15 named engines** with explicit versions (`de_est_tariff_2026`, `us_federal_income_tax_2026`, `us_se_tax`, `uk_paye_take_home_2026_27`, `ca_income_tax_2026`, `au_resident_tax_2026_27`, `mt_income_tax_2026`, `nl_vpb_2026` and others), and each `needs_input` reply carries an `inspect` block with the engine's `code_url`, `tests_url`, `figures_url` and the exact command to rerun its tests, so the arithmetic is auditable rather than asserted.

The instruction on that tool is the design decision worth copying: *never compute the figure yourself instead.* The model is told to ask for the missing fact and to stop, not to estimate.

The defect is reproducible. Called as `compute(engine="de_est_tariff_2026", taxable_income_zve=60000, assessment="single", tax_year="2026")` it returned `needs_input` with `what: "missing input 'tax_year'"`. Called as `compute(engine="us_se_tax", schedule_c_net_profit=60000, tax_year="2026")` it returned the same message naming the same field. Two engines, the field supplied both times as the string the schema's own enum demands, the same refusal. So the calculation path is not reachable through the hosted MCP in **1.4.0**; the engines themselves are in `calculators/engines/` with tests and can be run with `node --test`. Recorded as a defect with the reproducer, not as a missing feature.

One smaller inconsistency from the same session: the slug `de-ustva-monthly` returned by `get_deadlines` is not a skill slug, and `get_skill` on it answered `No published skill 'de-ustva-monthly'`. The two tools use different slug namespaces, so a client chaining them will fail until it routes through `search_skills` first.

## The licence decides who can use it

Code is **AGPL-3.0-only**. Skill content is under its own **OpenAccountants Guide License**, with commercial options documented in the repository. The README states its status plainly: *general reference, not advice*, and skills may be incomplete, outdated or wrong for the facts of a particular filing. For an agent workflow the honest use is a cited first pass that a qualified person signs off, which is exactly what the server's own instruction block tells the model to say.

## What it changes for an operator

The gap it fills is narrow and real: an assistant that can say **"the standard rate for this jurisdiction is X, under article Y, as published at Z, checked on this date"** instead of a remembered figure. Beside the existing accounting entries here, the division of labour is clean. [mighty-accounting-mcp](/hermes/mcp/servers/external/mighty-accounting-mcp/) works a company's own books, [pagofix-mcp](/hermes/mcp/servers/external/pagofix-mcp/) drafts the late-payment interest a client owes, [honest-vies-mcp](/hermes/mcp/servers/external/honest-vies-mcp/) validates a VAT number against VIES with its own evidence standard, and [casus-mcp](/hermes/mcp/servers/external/casus-mcp/) holds a French tax and legal corpus. OpenAccountants is the cross-border rulebook the others do not carry: 249 jurisdictions, every figure required to name its law, and a reviewer named where one exists.

**The limits, stated the way the server states them.** Keyless means rate-limited (60 requests a minute read from the headers), the library is guidance and not advice, every figure should be confirmed against the authority named in the passage, `accountant_verified_skills` reads zero per jurisdiction, the `compute` path is broken in 1.4.0, and two tools disagree about what a slug is. What remains is still the strongest answer in this catalogue to a tax question that must be cited rather than recalled.
