---
title: "PickFu MCP - Consumer Research Panels an Assistant Can Run"
description: "Create, price, target, publish and read real human consumer polls from Claude or ChatGPT: A/B concepts, packaging, names and ad creative tested on a paid panel, with a draft that costs nothing until approved."
category: Market Research / Consumer Panels
stars: n/a (pay per survey, account credits)
added: 2026-10-26
source: "live MCP probe on mcp.pickfu.com/mcp (initialize 401 authentication_required with a resource_metadata pointer, RFC 9728 protected-resource and RFC 8414 authorization-server documents read live behind WorkOS) + vendor documentation pickfu.com/docs/integrations/mcp-server (tool reference, question types, upload session, synthetic audiences) + mcp.so listing (Streamable HTTP, OAuth, submitted 2026-10-26)"
relevance: ★★★
tags: [consumer-research, survey, ab-testing, product-validation, packaging, market-research, ecommerce, panel]
last_updated: "2026-10-26"
---

# PickFu MCP

**The most expensive decision a small brand makes is building the wrong thing, and this is the first server in this catalog that puts a real consumer panel inside the conversation where that decision is being made.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.pickfu.com/mcp
Transport:   JSON-RPC over POST
Auth:        OAuth via WorkOS (authorization code with PKCE, client ID metadata
             document, device code grant) or a PickFu API key
Tools:       survey, project, media and synthetic-audience tools, read from the
             vendor's own MCP reference
Built by:    PickFu (pickfu.com)
Registry:    com.pickfu/mcp version 1.0.0, plus an mcp.so listing
```

## Why This Matters for Operators

Every operator has a version of the same story: a product name, a package, a price or an ad that was chosen by conviction, shipped, and quietly failed. The alternative is testing it on consumers first, which usually means a research agency, a two-week timeline and a budget nobody signs off on for a $30,000 decision.

A panel API inside the assistant collapses that to a conversation. The operator describes the choice, the assistant builds the poll, prices it, shows the targeting, and nothing is charged until the draft is approved. The output is a written explanation from every respondent, not a score.

That last part is the difference between this and prompting a model for an opinion. The reasons are what an operator can act on, and the vendor makes an explanation mandatory on every response.

## What It Actually Does

`initialize` without a token returned HTTP 401 with a body rather than a wall:

```
{"error":"authentication_required",
 "error_description":"Authentication required. Include a valid bearer token in the Authorization header.",
 "resource_metadata":"https://mcp.pickfu.com/.well-known/oauth-protected-resource"}
```

The discovery documents answer without an account:

- `/.well-known/oauth-protected-resource` returned HTTP 200 with `resource: https://mcp.pickfu.com`, its own authorization server, `jwks_uri` on AuthKit (`api.workos.com/sso/jwks/client_01K9A7KYMW6M8V0AVT626P0F74`) and scopes `openid`, `email`, `profile`, `offline_access`. Identity scopes only, so authorization over surveys and money lives in the account, not in the token.
- `/.well-known/oauth-authorization-server` returned HTTP 200 with the authorization endpoint on `auth.pickfu.com`, a **device authorization endpoint**, an introspection endpoint, `client_id_metadata_document_supported: true`, PKCE `S256` and grants for authorization code, refresh token and device code.

The tool reference, as the vendor documents it:

| Group | Tools |
|---|---|
| Survey management | `save_survey` (create or update; omit `surveyId` to create, pass a `template` to draft from one), `publish_survey`, `stop_survey` (unused responses refunded), `delete_survey`, `get_survey` (questions, options, AI summaries, per-question results with vote totals and the winner), `get_survey_responses` (paginated, with explanations, demographics and stored translations), `list_surveys`, `add_respondents`, `rate_response`, `pin_response`, `export_survey_results` (CSV, PDF, PNG) |
| Planning | `list_available_targeting`, `list_available_reporting`, `list_templates`, `get_template`, `list_tags`, `build_poll_url` |
| Projects | `save_project`, `get_project`, `list_projects` |
| Media | `upload_media`, `check_upload`, `generate_image`, `extract_images` |
| Synthetic (beta) | `get_synthetic_feedback`, `submit_synthetic_feedback`, `get_synthetic_feedback_results`, `list_synthetic_feedback`, `list_synthetic_audiences`, `get_synthetic_playbook` |
| Plan-gated | `mini_poll` for the plan-included daily mini-poll |

## The Money Path, Which Is the Point

`publish_survey` is a spending operation: it draws down the account's credit balance first and then charges the saved card for any shortfall, returning HTTP 402 only when there is no usable card. The vendor's documented flow puts the brakes in front of that:

- The assistant lists question types and targeting, and **reports the estimated cost for the chosen question types, sample size and targeting** before anything is published.
- The poll stays an unpublished draft, and nothing is charged, until the operator approves.
- In clients that implement MCP Apps (Claude, ChatGPT) the poll format, targeting and price render as inline interactive cards; other clients get the same information as text.

That is the right shape for an agent with spending reach: preview, price, approve, then spend, with the number visible before the commitment.

## How It Is Contained

- **Draft-until-approved.** Creating a survey is free; publication is the spending action.
- **Explanations are mandatory.** Every question type except screen recording requires the respondent to explain why in their own words, returned on each response as `explanation`.
- **Uploads are brokered, not pasted.** In web clients the assistant calls `upload_media` with no arguments and gets a short-lived upload session: a browser link, a `pfuh_` token and an expiry about fifteen minutes out. The assistant then picks up the CDN URLs. Terminal clients pass base64 directly.
- **Synthetic results are labelled as synthetic.** The beta synthetic-audience tools require an approved plan before running, must not be submitted without explicit user approval, and the vendor states synthetic results must not be mixed with human survey results.

## Limitations Recorded

- No tool call was executed: every path needs a PickFu account, so tool names come from the vendor's MCP reference rather than a live `tools/list`.
- **This spends real money.** An operator connecting it has given the assistant a surface where publishing costs money against a saved card; the approval step is in the client's behaviour, not enforced by scope.
- **Synthetic audiences are beta and feature-gated.** Those tools only appear in `tools/list` for accounts with the feature enabled, and there is a waitlist.
- **Multi-question surveys are priced per question**, and the vendor explicitly warns that adding an open-ended "why" question wastes a slot because the explanation is already collected.
- Results are consumer opinion on a presented concept, which is not demand. A winning A/B says which option people prefer, not how many will buy.
- `list_surveys` with `mine: true` requires OAuth and is not available to API-key callers, so the two credential paths are not identical in capability.

## FAQ

### Is this the same as asking a model what consumers think?
No. The respondents are real people from a paid panel, each required to explain their choice, and the result set carries demographics and per-question vote totals. A model's answer is a prior; this is a sample.

### Can the assistant spend money without asking?
Publishing draws on credits and then the saved card. The documented flow keeps the survey a draft and shows the price until the operator approves, but that gate lives in the client, so it is worth checking how your client handles approvals before connecting a card.

### What should be tested here?
The choices with a binary and expensive consequence: two names, two packagings, two price points, two landing-page headlines, two ad concepts. Anything answerable from your own analytics does not need a panel.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [POD Benchmark MCP - supplier cost comparison](/hermes/mcp/servers/external/podbenchmark-mcp/)
- [CorpusIQ connectors for commerce and marketing data](/hermes/mcp/)
