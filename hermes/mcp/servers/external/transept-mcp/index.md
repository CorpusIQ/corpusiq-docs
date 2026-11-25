---
title: "Transept MCP - Document Translation With Review Gates"
description: "42 tools readable without a key: a translation workspace of documents, glossaries, style guides, translation memory and runs priced before they bill."
category: "Content"
stars: "n/a (vendor-hosted; registry metadata and docs at github.com/Transept-AI/transept-mcp)"
added: 2026-11-24
source: "A chatmcp/mcpso queue filing #8016 read 2026-11-25T02:20Z; keyless initialize 200 on https://app.transept.ai/api/public/v1/mcp answering transept 1.0.0 on protocol 2025-06-18 over SSE, and a keyless tools/list returning 42 tools on 2026-11-25; execution refusal measured on me_get, project_list and run_estimate the same day (JSON-RPC error -32001, no content block); billing model, credit-to-word ratio and review-gate semantics read from the server's own initialize instructions; plan prices read from https://transept.ai/pricing on 2026-11-25; registry records ai.transept/transept 1.0.0 and 1.0.1 read the same day"
relevance: "★★★"
tags: [localization, translation, documents, glossaries, style-guides, translation-memory, review-gates, credits, xliff, tmx, remote-mcp]
last_updated: "2026-11-24"
---

# Transept MCP

**Every company that translates a document has the same failure: the second version disagrees with the first.** A term becomes two terms, the product name changes case, a legal sentence loses its hedge, and nobody can point at which decision broke it. Transept's MCP server exposes a translation workspace rather than a translate endpoint, and its whole tool surface is readable without a key.

```
Server type: Remote (Streamable HTTP, SSE responses)
Endpoint:    https://app.transept.ai/api/public/v1/mcp
Auth:        API key for execution (Settings -> Developer); discovery is keyless
Tools:       42 on tools/list, measured
Billing:     1 credit per source word, 3 in Pro mode; estimates are free
Pricing:     Free 5,500 credits/month without API access;
             Lite EUR 9 / USD 10 a month for 25,000 credits and MCP
Languages:   68
```

## The gate, measured

Two calls answer with no credential at all. `initialize` returns **200** over `text/event-stream`:

```json
{"result":{"protocolVersion":"2025-06-18",
 "capabilities":{"tools":{"listChanged":true}},
 "serverInfo":{"name":"transept","version":"1.0.0"},
 "instructions":"Transept is a translation workspace: documents are split into
  blocks, workflows (translate / proofread / review steps) run over them per
  target language, and results read back per block. ..."}}
```

`tools/list` returns **42** tools. Execution is where the wall is, and the refusal is worth reading because of its shape:

```
{"jsonrpc":"2.0","id":11,"error":{"code":-32001,
 "message":"Authenticate with a Transept API key: Authorization: Bearer ***
  (mint one under Settings -> Developer)."}}
```

There is **no `content` block and no `isError` field**: the refusal arrives as a JSON-RPC protocol error, so a client that renders only tool results will show nothing at all and the agent will look broken rather than unauthorised. That is a defect worth recording, and it is the reason this guide names the fix in the agent's own words: the key is minted under **Settings -> Developer**.

## The loop the server describes itself

The `initialize` instructions are the product brief, and they are unusually complete. Two sentences carry the design:

> *"The loop: document_create (or strings_import for key-value corpora) -> run_estimate (free) -> run_start / group_run_start with confirm:true -> poll run_get / group_run_get -> document_content_get. Multi-language work uses group_* (one lane per language); single-version work uses run_*."*

> *"Billing is in credits (1 per source word in standard mode, 3 in premium). run_start / group_run_start / run_gate_approve without confirm:true return the estimate and start NOTHING; me_get shows the balance. Estimates with is_upper_bound are ceilings, unused reserve is released."*

Three things follow from that, and each is a reason an operator can authorise this where they would not authorise a translate button. **Price before spend** is built into the tool contract rather than bolted on. **Two calls to spend** means an agent cannot bill a client's account by accident on a single retry. And **the estimate is a ceiling, not a guess**, with the unused reserve returned.

## The 42 tools, by family

| Family | Tools |
| --- | --- |
| Account | `me_get` |
| Projects | `project_list`, `project_create` |
| Documents | `document_list`, `document_get`, `document_create`, `document_update`, `document_delete`, `document_add_languages`, `document_content_get`, `document_attach_resources`, `document_resync_source` |
| Blocks | `block_update`, `block_translation_update` |
| Strings corpora | `strings_import`, `strings_reimport`, `processing_job_get` |
| Workflows | `workflow_list`, `workflow_template_list` |
| Runs | `run_estimate`, `run_start`, `run_get`, `run_list`, `run_cancel`, `run_gate_approve`, `run_gate_acknowledge` |
| Group runs | `group_run_estimate`, `group_run_start`, `group_run_get`, `group_run_list`, `group_run_cancel` |
| Glossaries | `glossary_list`, `glossary_get`, `glossary_create`, `glossary_terms_add` |
| Style guides | `styleguide_list`, `styleguide_get` |
| Translation memory | `tm_query`, `tm_import` |
| Webhooks | `webhook_list`, `webhook_create`, `webhook_delete` |

The id discipline is stated in the instructions and it is the trap for a naive integration: **`document_id` is a language version, not a document**, and siblings share a `language_group_id`; `translation.id` inside `document_content_get` blocks is what feeds `block_translation_update`; `unit_id` is a stable string key and equals the Figma node id for Figma documents.

## The two mechanisms that make it a workspace

**Review gates.** A run can finish with `gate_pending: true`, and then `run_get` carries a gate digest with `finding_count` and `has_continuation`. Approving continues downstream steps and bills them: omit `block_ids` for all of the run's blocks, pass `[]` to close without continuing and pay nothing, and call `run_gate_approve` once to see the price before calling it again with `confirm: true`. With no downstream steps it answers `no_continuation`, and `run_gate_acknowledge` dismisses the gate. A human review step therefore has a price and a state, which is the difference between a translation pipeline and a translate call.

**Delta translation on re-import.** `strings_reimport` resubmits the whole corpus, diffs it by `unit_id`, and answers with `delta_block_ids` (document id to block ids). Passing that object verbatim as `group_run_start.block_ids` translates only what changed, and unchanged units keep their translations. That is the mechanism a product team needs when a price list changes monthly in twelve languages, and it is the reason the corpus has a memory at all.

## What it costs, from the vendor's own page

| Plan | Price | Credits/month | Pages (standard) | MCP |
| --- | --- | --- | --- | --- |
| Free | 0 | 5,500 | about 11 | no |
| Lite | EUR 9 / USD 10 | 25,000 | about 50 | yes |
| Starter | EUR 29 / USD 33 | 80,000 | about 170 | yes |
| Pro | EUR 79 / USD 90 | 240,000 | about 510 | yes |
| Max | EUR 149 / USD 170 | 500,000 | about 1,080 | yes |

A page is about **300 words**, and Pro mode costs **three credits per source word** against one in standard, so the Pro-mode column is roughly a third of the page count. Credit packs start at **EUR 19 / USD 22** and never expire. Teams are free to create and seats are unlimited on every paid plan, which is a pricing decision an agency will notice before a freelancer will. **MCP and API access start at Lite**, so the free plan cannot be evaluated through this server at all; that is the single most important sentence in this section.

## Where it stops

- **Binary formats are not on the MCP surface.** The instructions are explicit: *"Binary formats (docx/xliff/tmx exports, file uploads) live on the REST API."* `document_create` takes inline text, markdown or html, so an agent handed a `.docx` must call the REST API rather than the MCP server. Word and EPUB layout preservation is a product feature, but it is not reachable from the 42 tools listed here.
- **Execution is unmeasured.** Every tool call without a key returns the same `-32001`, so no returned translation, no credit charge and no gate digest exists in this pass. What is measured is the discovery surface, the pricing page and the server's own contract; the arithmetic of a real run is not.
- **The instructions and the pricing page disagree in one word.** The server says **"3 in premium"**, the pricing page says **Pro mode**, and the catalog records both rather than choosing. An integrator should price a run with `run_estimate` instead of multiplying words by a remembered ratio.
- **The Glama listing is a connector, not a category.** `ai.transept/transept` appears in the official MCP registry at **1.0.0** and **1.0.1**, and on Glama as a connector record. Neither is a review count or a usage signal.
- **Figma import exists but is not a tool here.** The instructions mention Figma node ids and a Figma import route on REST, so an agent working from a design file is again outside the MCP surface.

## How to connect it

1. Create an account at `transept.ai`, then mint a key under **Settings -> Developer**. MCP requires **Lite** or above.
2. Add the server: `https://app.transept.ai/api/public/v1/mcp` with `Authorization: Bearer <key>` in Claude Code (`claude mcp add --transport http transept ...`) or as a custom connector.
3. Call `me_get` first. It returns the account, the key's scopes and the credit balance, which is the number every later decision depends on.
4. Create a project, then a document from text you already have, then `run_estimate` before `run_start`. Never let a prompt call `run_start` without `confirm: true`, because it will only estimate and your agent will believe it translated.
5. Attach a glossary and a style guide before the first paid run rather than after the first bad one. `document_attach_resources` takes glossary and style-guide versions; `document_resync_source` re-parses the stored source and keeps the translations of unchanged blocks.
