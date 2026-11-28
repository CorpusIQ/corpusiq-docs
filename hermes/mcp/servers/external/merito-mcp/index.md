---
title: "Merito MCP - EB-1A and NIW Readiness From 6,501 AAO Cases"
description: "US immigration case intelligence: searches 6,501 published AAO decisions, scores EB-1A, O-1A and NIW readiness."
category: "IP/Legal"
stars: "n/a (hosted service; filing chatmcp/mcpso#8300 read on 2026-11-28T13:13:49Z, vendor docs meritoos.com/integrations/claude, no repository named in the filing)"
added: 2026-11-28
source: "queue filing chatmcp/mcpso#8300 read on 2026-11-28T13:13:49Z; keyless initialize 200 as merito 0.1.0 on protocol 2025-06-18, a 15-tool tools/list (12 with readOnlyHint), and six tools/call attempts: four AAO searches, one scoring call with an empty answer set, and one citation call that refused on authentication"
relevance: "★★"
tags: [immigration, eb-1a, niw, o-1a, uscis, aao, legal, case-intelligence, visa, hr]
last_updated: "2026-11-28"
---

# Merito MCP

**Immigration case work is the one legal process a founder or a hiring manager ends up reading personally, and the reading is brutal: the AAO publishes thousands of decisions where a petition failed, and each one turns on a finding about a criterion - national importance, authorship, judging, a leading role - that looks like the same phrase in every summary and means something different in every denial. This server turns that pile into something an agent can query, and then scores a candidate against the same criteria before a lawyer is paid to. It was driven for this entry; four searches and one scoring call answered without an account.**

```
Server type:  Remote (streamable HTTP, hosted)
Endpoint:     https://meritoos.com/api/mcp
Auth:         none for the search and scoring tools; OAuth for account and citation tools
Tools:        15 - 12 read-only, 3 that write to an account
Collection:   about 6,501 published AAO decisions, classified
Coverage:     EB-1A, O-1A, EB-2 NIW
```

`initialize` answered **200** with no credential as `merito` **0.1.0** on protocol **2025-06-18**, and `tools/list` returned **15** tools with `readOnlyHint: true` on twelve of them. The three with a write hint are `save_to_merito`, `create_upload_link` and `run_officer_simulator`, and the split is honest: everything that reads public case law is anonymous, everything that touches a person's own case needs an account.

## The searches answer, and the filters are real

`search_aao_decisions` takes a keyword string, then optional `visa`, `outcome`, `applicant`, `criterion` and `year` filters, and pages at 25. Four calls, all keyless:

- **`authorship` alone** returned **15** decisions. The first is `AUG182026_01B2203`, dated **2026-08-18**, `dismissed`, field `software_engineering`, self-petitioned: *"She claimed six criteria; USCIS found four met (judging, authorship, leadership role, high salary). The AAO affirmed dismissal because the totality of evidence does not demonstrate sustained national or international acclaim."* Each result carries per-criterion findings with a reason, so `awards` reads `not_met` with *"No major internationally recognized award received; alternate criteria required"* and `final_merits` reads `not_met`.
- **`authorship judging`** narrowed to **3**, which shows the description's "contains all of the words" is implemented as an AND rather than an OR.
- **`authorship judging` with `outcome: sustained`** returned **0** - a filter combination that is empty and says so, with a `countNote` explaining what the count describes.
- **`national importance startup` at `niw`** returned **54** across **3** pages, and this is the query that shows the product's value. The decisions are founders and operators who were refused on the first Dhanasar prong: a pilot building flight-planning software, a CEO of an eco-friendly manufacturing startup, a COO of an NSF-funded fire-suppression company, a telecommunications engineer at a connectivity startup. The summaries name the reason each failed - *"impact limited to startup company and private clientele without broader field or economic effects"*, *"routine company-specific benefit insufficient for NIW, distinguishing meaningful national importance from merely important work"* - which is exactly the distinction a founder writing a business plan needs to see before writing it.

Every result carries a stable `identifier` (`AUG032026_01B5203`, `MAY202026_03B5203`), a date, an outcome, a field, an applicant type and a link to the summary page, so a lawyer can be handed a list and check it.

## The scorer asks before it scores

`score_profile` with an empty answer object does not guess. It returned `status: needs_answers` and `step: {index: 1, of: 6}` with the first five questions and their exact option values - years active, scope of the most significant award, where the articles were published, whether independent third parties adopted the contribution, and what kinds of judging were done - plus `later: ["25 more question(s) in the next steps"]` and an instruction to ask only these questions and invent no others. For an agent, that is the right contract: it makes the assistant interview the person instead of filling gaps with assumptions, and the questions are phrased in evidence terms (`independent_third_party_adoption_documented` against `claimed_by_letters_only`) rather than in adjectives.

## Three defects worth naming

1. **`criteriaTotal` does not reconcile with the criteria the same record lists.** On `AUG182026_01B2203` the summary says six criteria were claimed, the `criteria` array carries five codes, and `criteriaTotal` reads **11**. On `FEB172026_02B2203` the array carries five and `criteriaTotal` reads **7**. A reader comparing `criteriaMet` across decisions is therefore comparing ratios with different denominators and no published definition of what the denominator counts.
2. **The gated tools refuse without saying how to authenticate.** `citation_quick_check` answered `401` with `{"code": -32001, "message": "Authentication required."}`, no `WWW-Authenticate` header and no pointer to a protected-resource document, while the filing describes citation metrics as one of the things the product does. A client cannot discover the route to a token from the refusal; it has to read the vendor's website.
3. **The returned links carry campaign parameters.** Each decision URL ends `?utm_source=mcp&utm_medium=mcp&utm_campaign=merito_ai_distribution&utm_content=aao_search`. It is honest attribution rather than a hidden redirect, but a link pasted into a client-facing document arrives with the vendor's campaign tag on it.

## Where it belongs

Nothing else on this shelf covers US immigration, and the placement matters more than the tool count: this is the only entry that answers *would this profile clear the first prong* with a rule-based score and a corpus of published refusals behind it. Two honest limits. It is **not** legal advice and says so on every response, in a `disclaimer` block and again in the `countNote`, which also states plainly that the counts describe the collection and are not a chance of approval - a sentence worth quoting to anyone who reads a count as a probability. And the search matches Merito's **summaries**, not the full decisions, so a criterion that appears only in the body of an opinion is invisible to it; `get_aao_decision` is the route for reading one record in full.

For a founder on an O-1 or EB-1A path, or a company sponsoring an NIW, the useful sequence is: search the refusals in your own field, read why the closest ones failed, then run the scorer to see which evidence the file is missing. The account tools - saving a Case, an officer-style review - are where the paid plan starts, and `run_officer_simulator` states that it asks for confirmation of the credit cost before it runs.

```json
{
  "mcpServers": {
    "merito": {
      "url": "https://meritoos.com/api/mcp"
    }
  }
}
```

## Also worth knowing

### What is free and what is not?

Free without any credential: the AAO search, the per-decision lookup, the readiness score, the pathway comparison, the evidence checklist and the RFE decoder - all of them read-only and stateless. Account-scoped and gated: the citation metrics lookup, the user's own cases, the officer simulator and the upload link, which is a one-use link valid fifteen minutes so a person adds documents without handing the assistant a file. The filing describes free anonymous tools with daily limits and one tool that needs a paid plan; `citation_quick_check` is the one that refused on authentication during this pass, and the exact plan boundary behind it was not measured because nothing in the refusal named it.

The one detail that dates the entry: the collection is described as *"about 6501 classified"* in the product's own count note, and the newest decision returned by these searches is dated **2026-08-18**, so the corpus is current to roughly late summer 2026. Treat the counts as a sample of published refusals rather than as an index of every AAO decision ever issued.
