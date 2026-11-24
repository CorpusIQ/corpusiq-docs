---
title: "Persado MCP - Score Marketing Copy Before You Send"
description: "An enterprise language model behind a complete OAuth chain: a 0-100 predicted-response score, ranked rewrites with predicted lift, and brand voice on Enterprise."
category: "Marketing"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-24
source: "An mcp.so feed card at 2026-11-24T11:00Z for /servers/persado-mcp; keyless initialize on https://api.persado.com/mcp answering 401 with a WWW-Authenticate bearer challenge naming resource_metadata and the scope openid offline_access mcp:tools; the protected-resource document and the RFC 8414 authorization-server document read 2026-11-24; product capability, the two tool names, the trial terms and the Enterprise boundary read from https://www.persado.com/mcp on 2026-11-24; the 17-article connector help library listed at https://library.persado.com/en/collections/19694551-persado-mcp on 2026-11-24"
relevance: "★★★"
tags: [marketing, copy-scoring, subject-lines, aem, brand-voice, compliance, oauth, keycloak, remote-mcp, enterprise]
last_updated: "2026-11-24"
---

# Persado MCP

**Two subject lines, four words apart: one gets opened and one does not. Nobody knows which until the send.** Persado sells a language model trained on campaign response rather than on the internet, and its MCP server asks that model for a prediction in the window where the copy is being written. You paste an email, a banner or a subject line into the assistant you already use, get a **0-100 score** with the words moving it, and ask for ranked alternatives with predicted lift.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://api.persado.com/mcp
Auth:        OAuth 2.1, scopes openid offline_access mcp:tools
             issuer https://myaccount.persado.com/realms/persado-portal
Tools:       score_marketing_content, rank_variants (named on the product page;
             the schema is not readable without an account)
Pricing:     14-day free trial, no card
```

## The gate, measured

`initialize` with no credential answers **401** and the refusal is a complete bearer challenge:

```
www-authenticate: Bearer resource_metadata=
  "https://api.persado.com/.well-known/oauth-protected-resource",
  scope="openid offline_access mcp:tools"
```

The protected-resource document at that exact path answers **200**:

```json
{"resource":"https://api.persado.com/mcp",
 "resource_name":"Persado MCP Gateway (Production)",
 "authorization_servers":["https://myaccount.persado.com/realms/persado-portal"],
 "scopes_supported":["openid","offline_access","mcp:tools"],
 "bearer_methods_supported":["header"],
 "token_endpoint_auth_methods_supported":["none"]}
```

And the RFC 8414 document answers **200** with the whole flow:

```json
{"issuer":"https://myaccount.persado.com/realms/persado-portal",
 "authorization_endpoint":"https://myaccount.persado.com/realms/persado-portal/protocol/openid-connect/auth",
 "token_endpoint":"https://myaccount.persado.com/realms/persado-portal/protocol/openid-connect/token",
 "jwks_uri":"https://myaccount.persado.com/realms/persado-portal/protocol/openid-connect/certs",
 "registration_endpoint":"https://api.persado.com/register",
 "response_types_supported":["code"],
 "grant_types_supported":["authorization_code","refresh_token"],
 "code_challenge_methods_supported":["S256"],
 "token_endpoint_auth_methods_supported":["none"]}
```

Read that as an operator rather than as a client author. **`mcp:tools` is the only permission the token can express**, and it is a single scope for the whole tool surface; there is no read-versus-write split to grant because there is nothing here to write. The three OIDC scopes are identity and refresh. `token_endpoint_auth_methods_supported: none` with a registration endpoint means a public client with **PKCE S256** and no client secret, which is exactly what a desktop assistant needs and what a strict enterprise IdP is usually persuaded to allow last. The realm is **Keycloak**, and the path says `persado-portal`, so the sign-in screen an employee sees is the company account they already have rather than a new password.

One routing detail that will cost an integrator an afternoon: **the issuer is `myaccount.persado.com` and the MCP host is `api.persado.com`**. Two hosts, one chain, and the discovery document is served from the MCP host so the client can find the identity host. Clients that assume issuer equals the host they connected to will fail at validation rather than at sign-in.

## What the tool actually returns

The tool schema is not readable without an account, so this section is the vendor's published product description and the two tool names visible on it, `score_marketing_content` and `rank_variants`, rather than a measured response.

- **A 0-100 score** for a piece of copy, with the contributing elements named. The vendor's own demo shows an email scored **82/100** with *"Strong on safety. The CTA is what holds it back"*, then breaks the score into **Emotion · Safety +6.1** and **CTA "See your rate" −2.2**. A number with a per-element breakdown is a different product from a number, because the operator can act on the -2.2 without touching the +6.1.
- **Ranked alternatives with predicted lift.** The banner example shows a top performer at **+9.2%** with a **Performance 88**, a **5/5 brand** mark and a **Compliance: clear** flag. Asking for "five better versions, ranked" is the second tool.
- **Answers from your own campaign results.** The vendor lists this as running in the trial: plain questions about what has worked, answered from the account's own history rather than from a public model.

Three markings on that page are worth separating, because two of them are not in the trial. The page says **"The trial covers the first three"**, predicted performance on your own content, ranked rewrites, and the question-answering over campaign results. **Brand voice and the 20+ regulatory frameworks are labelled Enterprise**, which is where the compliance story actually lives. An operator in a regulated industry should read that boundary before promising a compliance benefit: on the trial the assistant predicts response, and on Enterprise it also constrains itself to a brand voice and a set of named regulatory frameworks.

The assistant shown on the page also displays a **Compliance: clear** field beside the score, which is the kind of signal that sounds reassuring and should be treated as one input, not a sign-off.

## The rollout evidence most vendors skip

The help library carries **17 articles** for this one connector, and their shape is the reason to trust it past a demo: separate **admin installation** and **user installation** guides for **Claude**, for **ChatGPT Business and Enterprise**, and for **Gemini Enterprise**, plus user guides for **Copilot**, **MS Teams** and **MS Word**, and separate articles for **personal or individual accounts** on Gemini and ChatGPT. That is a vendor that has understood the difference between an enterprise tenant where an admin enables a connector and a single professional who turns it on themselves. It is also a realistic map of who will actually use it: the copy is written in Word and Teams far more often than in a chat window.

## How to connect it

1. Start the **14-day free trial** at `persado.com/mcp`. No card is taken.
2. In **Claude**, add a custom connector with `https://api.persado.com/mcp` and complete the OAuth sign-in. The client registers itself through `https://api.persado.com/register`.
3. In **ChatGPT Business or Enterprise**, an admin enables the connector for the workspace and each user signs in with their own account; the vendor publishes both halves of that procedure.
4. Point the first test at **copy you already sent and already have results for**. A score that agrees with a known outcome is evidence; a score on fresh copy is an opinion with a number.
5. Ask for the breakdown, not just the total. The element-level movement is the actionable output.

## Boundaries recorded

- **The tool schema is unmeasured.** A keyless `initialize` is refused, so no `tools/list` exists in this pass. The two tool names and every capability statement above come from the vendor's product page on 2026-11-24. Re-probe with an account before publishing a schema.
- **No public pricing.** The trial is 14 days with no card; what happens on day 15 is a sales conversation, not a published number. Recorded as unknown rather than guessed.
- **The compliance surface is Enterprise.** Brand voice and the 20+ regulatory frameworks are labelled Enterprise on the page, so a trial evaluation should not be read as an evaluation of the compliance controls.
- **A predicted lift is a model output.** The vendor's page frames it as a prediction and the catalog records it the same way: useful for choosing between two drafts, not a guarantee of campaign performance.
