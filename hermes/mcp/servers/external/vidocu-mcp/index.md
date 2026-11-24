---
title: "Vidocu MCP - Documents Turned Into Training Videos"
description: "A documentation platform with 146 tools behind 44 scopes: a PDF becomes a video, a video becomes a help article, and every operation draws credits."
category: "Content Creation & Creative"
stars: "n/a (vendor-hosted; no public repository for the server)"
added: 2026-11-24
source: "An mcp.so feed card at /servers/vidocu-96ba4d stamped 2026-11-24T08:11Z; keyless initialize on https://mcp.vidocu.ai/ answering 401 with a WWW-Authenticate resource_metadata pointer; the protected-resource document and the RFC 8414 authorization-server document read 2026-11-24; tool families, plan rules and the 146-tool count read from vidocu.ai/docs/mcp and plan prices from vidocu.ai/pricing, both on 2026-11-24"
relevance: "★★"
tags: [documentation, training-video, knowledge-base, subtitles, translation, voiceover, oauth, remote-mcp]
last_updated: "2026-11-24"
---

# Vidocu MCP

**Every company has the same orphaned asset: a screen recording of how something is done, sitting in a folder, watched by nobody.** Vidocu is built to convert that asset, and its MCP server exposes the conversion as tools: a PDF, DOCX, PPTX or Keynote becomes a finished video, a video becomes a step-by-step help article with subtitles, and either one gets translated or voiced into another language. The operator value is not that an assistant can write a script. It is that the training video a new hire needs can be produced from the document the company already wrote.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.vidocu.ai/
Auth:        OAuth (protected-resource metadata) or an API key as a Bearer token
Tools:       146 according to the vendor's docs; the mcp.so listing counts 168
Pricing:     free tier, then $19 to $149 a month; analysis draws 50 credits a minute
```

## The gate, measured

`initialize` with no credential answers **401** with a short body and a challenge that carries the documentation pointer:

```
www-authenticate: Bearer resource_metadata="https://mcp.vidocu.ai/.well-known/oauth-protected-resource"
body: {"error":"Unauthorized"}
```

The protected-resource document answers **200** on both the bare and the trailing-slash form of that route and declares a partial scope set:

```json
{"resource":"https://mcp.vidocu.ai",
 "authorization_servers":["https://api.vidocu.ai"],
 "scopes_supported":["videos:read","videos:write","projects:read","projects:write",
   "subtitles:read","subtitles:write","export:write","translate:write","voiceover:write",
   "article:read","article:write","analyze:write","tools:read","tools:write",
   "jobs:read","usage:read","process:write"],
 "resource_name":"Vidocu MCP Server",
 "resource_documentation":"https://vidocu.ai/docs/mcp"}
```

Seventeen scopes, and they are **resource-scoped rather than identity-scoped**, which is the opposite of the OIDC-only designs elsewhere in this catalogue: `videos:write` and `translate:write` say what the token can do to what, and a client can request the narrow set it needs.

The authorization-server document is where the interesting detail lives. Its issuer is **`https://api.vidocu.ai`** while the authorization endpoint is **`https://vidocu.ai/oauth/authorize`**, so the browser sign-in happens on the product domain and the token is issued on the API domain. That two-host split is common enough to be worth flagging: a client that validates that the authorization endpoint shares the issuer's origin will refuse this server, and the fix is the client's, not the vendor's. Registration and revocation endpoints are published, authorization code and refresh grants are supported, and **PKCE S256** is advertised, so a public client can complete the flow with no secret at all.

**And the scope lists disagree.** The protected-resource document names **17** scopes; the authorization-server document names **44**, adding `courses:*`, `studio:*`, `modules:*`, `remixes:*`, `manuals:*`, `recordings:*`, `knowledge_base:*`, `brand_kit:*`, `voices:*`, `avatars:*`, `webhooks:*`, `approvals:*`, `comments:*` and `locks:write`. Read both before requesting anything: a client that only knows the PRM document will never ask for the scopes the newer tools need, and the failure will look like a permissions bug on the vendor side.

## What the tool surface covers

The vendor's own documentation is specific in a way that makes the product legible. It lists **146 tools** across ten families, and a few of them are the ones that decide whether this is useful to a business:

- **Videos and projects** - `get_upload_url`, `upload_video`, `list_videos`, `get_video`, `update_video`, `delete_video`, plus project folders for organising a library.
- **Processing** - `analyze_video` produces subtitles and a narration script; `generate_article` turns a video into a step-by-step help article; `get_article` reads one back without regenerating it, which is the difference between a cheap read and an expensive re-run; `translate_video`, `generate_voiceover`, `export_video` with burned-in subtitles; and `process_video` as a one-shot pipeline across analyse, voiceover, article, export and translate.
- **AI Recorder** - `start_recording` takes a plain-language description of a flow and drives a browser to record it. `list_recorder_sessions` and `update_recorder_session` hold saved logins so a recording behind a login does not have to sign in again, and `answer_recording_prompt` supplies a value when the agent pauses to ask. The vendor states this needs a paid plan.
- **Knowledge Center** - the hosted help centre layer, published on the customer's own domain, and gated behind an add-on rather than a plan tier.
- **Pricing a job before starting it** - `get_credit_costs` exists, and the vendor says to call it first. That single tool is the difference between an agent that spends an operator's credits and one that quotes a job.

Plan rules carry over MCP rather than being flattened by it: the Knowledge Center tools need the add-on, the AI Recorder needs a paid plan, and **every operation draws the same credits it would draw in the app**. An operator wiring this into an assistant should assume an assistant will be more expensive than a person clicking, because a person waits for the preview and an agent does not.

## The count that does not agree

The mcp.so listing says **168 tools**. The vendor's documentation, read the same day, says **146**. Neither number is verified by this pass, because the endpoint refuses keyless and there is no published schema to enumerate without a token. Both numbers are recorded rather than reconciled: a 22-tool gap is either a listing that counts an internal surface or a documentation page that lags a release, and the next pass with a credential should settle it by calling `tools/list` once.

## Pricing, as published

Read from `vidocu.ai/pricing` on 2026-11-24, monthly billing first with the yearly rate after it:

| Plan | Monthly | Yearly, per month | Credits | Help articles and exports |
| --- | --- | --- | --- | --- |
| Free | $0 forever | $0 | 200 one-time (about 4 minutes of analysis) | 1 article, 1 export |
| Starter | $19 | $13 ($156 a year) | 400 a month | Unlimited |
| Pro | $49 | $33 ($396 a year) | 1,500 a month | Unlimited |
| Business | $149 | $100 ($1,200 a year) | 4,000 a month | Unlimited |
| Enterprise | Custom | Custom | Custom | Unlimited |

**Analysis costs 50 credits a minute**, so a 10-minute walkthrough consumes a Starter plan's entire month in one video, and the Business plan covers about 80 minutes of analysis a month. Translation costs credits equal to the source duration per target language, and the **Knowledge Center add-on is $100 a month on paid plans** (Pro and above, not Free), with 1,000 AI credits included and $0.05 a credit beyond that.

Two procurement facts a team will care about. Free-plan exports carry **a Vidocu watermark** and paid plans remove it automatically, which matters for any customer-facing training material. And the AI Recorder, the feature most likely to justify the spend, is not on the free or entry plan, so a trial on Free will not show the product's best trick.

## How to use it

1. Add `https://mcp.vidocu.ai/` as a remote MCP server. Clients with OAuth support handle the sign-in; the docs also publish the JSON snippet for the standard config file shape.
2. If your client cannot do OAuth, create an API key in the Vidocu dashboard and send it as `Authorization: Bearer vdo_live_...`. The key is a full-plan credential, not a scoped one, so treat it like a password.
3. Call `get_credit_costs` before the first real job and price the video you actually have. A 12-minute recording is 600 credits, which is a fact worth knowing before a batch run.
4. Start with the read and cheap-write pair: `list_videos` to confirm the workspace, then `generate_article` on one existing video. That produces a help article from an asset the team already owns, with no new recording and no purchase decision.
5. Check the plan before promising the AI Recorder or the Knowledge Center to a stakeholder. Both are paid-tier features and the assistant will fail in a way that reads like a bug if the plan does not include them.

## Boundaries recorded

- **No keyless tool schema.** This guide describes tool families from the vendor's documentation, not a measured `tools/list`. The 146-versus-168 gap is open.
- **The scope sets disagree between the two discovery documents** (17 against 44). Recorded as a defect a client will hit, not smoothed over.
- **Analysis is the cost driver**: 50 credits a minute is the only metered figure a buyer needs before committing, and it makes short clips cheap and long recordings expensive.
- The audio and voice work is a vendor feature, and the watermark on free-tier exports is the vendor's own branding. Neither is a claim about output quality, which this pass could not test without a credential.
