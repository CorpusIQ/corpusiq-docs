---
title: "effectsize MCP - A Product Analytics Case Archive"
description: "A keyless archive of 365 experiment, causal-inference and forecasting cases from company engineering blogs, searchable in one call."
category: "Analytics / Research"
stars: "0 (hosted Streamable HTTP at https://mcp.effectsize.io/mcp/public, keyless public route; two tools, both driven, full cards gated behind free sign-in)"
added: 2026-11-18
source: "the mcp.so submission queue entry #7582 filed 2026-11-18T11:08:07Z, and a driven session on 2026-11-18 against the public route with no credential"
relevance: ★★★
tags: [analytics, experimentation, ab-testing, causal-inference, forecasting, metrics, case-studies, keyless, remote, mcp]
last_updated: "2026-11-18"
---

# effectsize MCP

**The most expensive analytics mistake is not a wrong calculation. It is solving a problem that another company already solved twice and wrote down.**

An engineer designing an experiment has read maybe five of the three hundred articles that answer their exact question. The knowledge exists - in engineering blogs, conference talks, papers - and it is unfindable, because the search terms that describe the problem are not the words the companies used.

effectsize is that archive turned into a retrieval surface. Every entry is a reviewed card with a problem, a solution, a method, the results, the limitations and a link to the original. The design decision worth noting is that the retrieval is not a text search: the model is asked to describe the *shape* of the problem, and the results come back with an explicit statement of whether the match is close or merely adjacent.

```text
Server type:   remote Streamable HTTP (hosted, two routes)
Endpoint:      https://mcp.effectsize.io/mcp/public   (no sign-in)
               https://mcp.effectsize.io/mcp          (OAuth, full cards)
Server:        effectsize-cases-public, version v0.4
Protocol:      2025-06-18
Auth:          none on /public (rate-limited per IP)
Tools:         2 (search_cases, get_cards)
Ranker:        v0.4
Website:       https://effectsize.io
Listed on:     the mcp.so submission queue as #7582
```

## The evidence tier

Keyless public route, driven. `initialize` answered **200** with no credential and returned an unusually long `instructions` block that is itself the product brief: search the archive **before** answering from general knowledge, describe the decision and the constraint rather than the company, read the passports, judge relevance yourself, and tell the user when the archive has no close case instead of citing weak matches.

`tools/list` returned two schemas. Both were driven: **two** `search_cases` calls on different task types, one `get_cards` call with two real slugs, and one `get_cards` call with an invented slug to measure the refusal. Five of the six calls returned data.

The full card is behind a free sign-in - the public route returns `problem`, `solution` and `tools` only. No sign-in was performed, no OAuth flow was started, and nothing below quotes a section the public route withheld.

## The search takes a problem description, not keywords

`search_cases` requires a `task` sentence and a `phrasings` array, with an optional `task_types` filter over a fixed vocabulary. The instruction is explicit that the input must be abstract - no company, no product, no internal numbers.

A checkout test where the two arms contaminate each other:

```text
task    "measure whether a new checkout flow increased completed orders,
         but test and control users share the same household and
         promotions leak between them"
types   design-experiment

full_matches  104     candidates  365
search_id     a641c839dd6b      snapshot  e6945c5405c47d74
```

The reply is a ranked candidate list with a structure designed to be judged rather than trusted. Each result carries a `tldr`, a `how` line phrased as the question it answers, an `evidence` grade, an `adjacent` slug, and a `why` object naming the task type it matched. The top three for that query:

| Company | Year | Case | Evidence grade |
|---|---|---|---|
| Apple | 2023 | Sample-size calculations for A/B testing, novel extensions | simulation |
| Lyft | 2022 | Challenges in experimentation | case-anecdote |
| Spotify | 2023 | Sequential testing with longitudinal data, the peeking problem | simulation |

A different task type, a different result set, and the same snapshot identifier:

```text
task    "forecast weekly demand for a new market with only eight weeks
         of history and a promotion calendar"
types   forecast

full_matches  52      candidates  306
search_id     0e4da0bbc879      snapshot  e6945c5405c47d74
```

Top of that list: Uber on forecasting airport demand and time-to-request, Yandex Lavka on reconciling forecasts across teams, Otto on dynamic pricing, Avito on forecasting the effect of a paid listing promotion. The `snapshot` is identical across both calls, which means the archive is versioned and two agents querying the same day are answering from the same corpus.

### What does a card actually contain?

`get_cards` takes up to five slugs and a section list. The Lyft card's `problem` section, returned on the public route, is the reason this server is worth a guide:

> Lyft tests every product change, but a standard user-level A/B test fails in a ride-sharing marketplace. Riders and drivers share one pool of supply, so one user's treatment changes what another user gets. The independence assumption between groups breaks.

That is a real methodological answer with the mechanism named, and its `solution` section names the remedy - choose the randomisation unit to fit the interference, then wrap it in process: pre-registered hypothesis, Benjamini-Hochberg correction across many primary metrics, an experiment scheduler, a decision log.

The Apple card answers a different failure: randomise users but compute the metric per session or per event, and the rows of one user are correlated, so the standard independent-samples formula understates the variance, asks for too few observations, and leaves the test underpowered.

Each card also carries a `materials` block declaring what exists and whether it can be fetched. Lyft's original is marked `access: bot-blocked` with a note to ask the user to paste it; Apple's paper is marked `open`. That distinction is the difference between a citation and a dead end, and stating it up front saves the fetch.

## The refusal is a success envelope

An invented slug came back like this:

```json
{"cards": [{"slug": "definitely-not-a-real-slug-xyz",
            "error": "unknown slug", "materials": {}}],
 "approx_tokens": 0}
```

HTTP 200, `isError` false, and the failure carried per card. A client that renders only the content block and not the inline error will show an empty result as if it were an answer. Callers should check each card object for an `error` key before treating the batch as complete.

## Where it fits

This is a research surface, not a data source. It does not hold your metrics and it will not compute your experiment. What it does is put two hundred reviewed cases in front of the model at the moment a question is being designed, with an explicit confidence signal and an honest "no close case" state.

For an operator, the value is narrow and real: the question "how have other companies measured this" gets an answer with a company, a year, a method and a link, instead of a confident generalisation.

### Is the archive behind a paywall?

No, but it is split. `search_cases` and the problem/solution/tools sections of each card are free on the `/public` route, rate-limited per IP. The full card - core idea, how to apply, results, limitations, code, talk transcripts - needs a free sign-in through OAuth on `/mcp`, or an account on the website. Nothing in this page relies on a gated section.

### Does it train on the query?

The server says the search arguments are stored to improve coverage and asks the caller not to include company names, people, internal figures or other confidential details. Treat the task sentence as a public input.

## Sources

- Public endpoint: https://mcp.effectsize.io/mcp/public
- Full endpoint: https://mcp.effectsize.io/mcp
- Homepage: https://effectsize.io
- Skill and source: https://github.com/vzhyvov/effectsize-skill
- Submission: the mcp.so queue as #7582 on 2026-11-18
