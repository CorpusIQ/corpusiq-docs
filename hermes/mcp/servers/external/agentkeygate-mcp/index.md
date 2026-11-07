---
title: "AgentKeyGate MCP - A Pass Instead of the API Key"
description: "Self-hosted gateway that gives an agent a temporary, owner-approved pass capped by time and call count, filters the fields it sees, and keeps the key."
category: Security & Agent Governance
stars: 0 (Apache-2.0, github.com/maximskorohod/agentkeygate, v1.0.2, pushed 2026-11-07)
added: 2026-11-07
source: "The chatmcp/mcpso submission #6899 (AgentKeyGate, io.github.maximskorohod/agentkeygate, named 2026-11-07T17:08:46Z); the official MCP registry record at v1.0.2 with a bearer-token Streamable HTTP remote at https://{host}/mcp; the repository README, server.json, docs/ARCHITECTURE.md MCP tool reference and docs/DEPLOY.md; and github.com/maximskorohod/agentkeygate, created 2026-11-05T09:54:02Z and pushed 2026-11-07T17:20:26Z"
relevance: ★★★★
tags: [agent-governance, secrets-management, api-keys, credential-broker, approval-gate, data-filter, pii-masking, audit-log, kill-switch, self-hosted, hermes, apache-2.0]
last_updated: "2026-11-07"
---

# AgentKeyGate MCP

**Every agent that files a report into a CRM, reads a payment account or posts to a support desk carries a long-lived key in its config. The agent can read that file, a prompt injection can ask it to send the key somewhere else, and the key keeps its full rights for as long as it lives.** AgentKeyGate is a self-hosted gateway that replaces the key with a pass: the agent says which service it needs, for how long, for how many calls, and why. A person approves with those facts in front of them. The gateway adds the real key on the way out, counts the calls, filters what comes back, and closes the pass when the time or the calls run out.

```
Server type: Self-hosted gateway, Streamable HTTP at https://{host}/mcp
Auth:        agent token gwa_... as Authorization: Bearer
License:     Apache-2.0 · Node.js 22 · SQLite · 1 vCPU / 1 GB RAM
Registry:    io.github.maximskorohod/agentkeygate 1.0.2
Repo:        github.com/maximskorohod/agentkeygate (created 2026-11-05, pushed 2026-11-07)
Pass format: gwt_... (the agent never receives the service key)
```

## The four tools

The MCP surface is deliberately small, and every one of the four is a step in the same loop:

| Tool | Input | What comes back |
| --- | --- | --- |
| `list_services` | none | The services this agent holds a key for, with each credential's label, `mode` (`always` or `ask`), `max_ttl`, `max_calls`, the compiled `filter` (method templates and field paths, never values) and the current `access` state with `expires_at` and `calls_left` |
| `request_access` | `service`, `credential_id?`, `ttl?`, `calls?`, `reason` | `{status: 'approved', credential_id, expires_at, max_calls}` or `{status: 'pending', request_id, poll_after: 5}` or `{error: 'denied', reason}` |
| `check_request` | `request_id` | `pending`, `approved`, `denied`, `expired` or `revoked` |
| `call` | `service`, `method`, `path`, `credential_id?`, `body?`, `headers?` | `{status, headers, body, truncated, bytes}` |

A foreign `request_id` returns `not_found` rather than a permission error, so a stray id learns nothing. `call` is bounded on every side: `method` must be one of the five verbs, concurrent calls per session are capped, `path` is split at the first `?` and a missing leading slash is `bad_path`, headers are capped at 20 entries of 1024 characters with no CR/LF, and the response body is read up to a byte limit, cut on a UTF-8 boundary, with the secret already scrubbed by a streaming redactor **before** truncation. The response headers that survive are an allowlist (`content-type`, `etag`, `retry-after`, `link`, `x-total-count`, `x-ratelimit-*` and a few others), not the service's full set.

The REST route is the same model without the agent protocol: `POST /v1/grants` returns `200` approved, `202` pending with a `poll_after` of 5 seconds, or `403` denied; then `GET /v1/proxy/<service>/...` forwards the path as-is with the key injected. `ttl` is **300 to 86400** seconds, capped by the key's own limit, and `reason` is up to **200** characters, shown to the owner on the approval screen.

## The data filter is the part operators actually need

An approval screen answers "should the agent do this". It does not answer "what will the model see from my CRM", and that is the question that stops most agent deployments in a business.

The filter works on the response, so it applies to every agent that uses that key. Types and fields are chosen explicitly and everything else is **cut from the JSON before it reaches the agent**, with routes outside the chosen types returning `403`. `readOnly` passes only reads, which means `GET` and `HEAD` plus listed search routes for REST and a fixed list of read methods for Bitrix24 and Telegram, and it is **on by default for CRM and support keys** (HubSpot, Pipedrive, Zendesk, Bitrix24, amoCRM). A blocked write returns `403 write_not_allowed` and **does not consume quota**. `mask` replaces e-mail addresses, phone numbers written with a `+` or separators, card numbers that pass a Luhn check, and IBANs with `****` in every string value. Names are not detected, and a bare digit string is deliberately left alone because it looks identical to an ID or an amount.

The vendor's own example is the clearest statement of intent. A Bitrix24 lead returns `ID`, `TITLE`, `STATUS_ID`, `OPPORTUNITY`, `NAME`, `PHONE`, `COMMENTS`; with a field filter the agent receives `ID`, `STATUS_ID`, `OPPORTUNITY` and nothing else. The deal stage and the amount survive because the weekly report needs them, and the client's name, phone number and sales note do not.

Two details raise this above a checkbox. Weakening a filter, whether that is turning off `readOnly` or `mask` or adding a type or a field, requires a **fresh TOTP code** and then shows a "was, now" page before the change applies. And "Check on one call" makes one real read request as the owner, outside the agents' limits, written to the audit log, and shows field names only, never values.

Filters exist for Bitrix24, HubSpot, Pipedrive and Zendesk. The HubSpot and Pipedrive field lists were checked against live accounts; the Zendesk list comes from the provider's documentation and is marked `unverified` in `providers.yaml`. Every other service gets the gateway's limits and masking without a field filter, so the vendor's own advice applies: use keys with the narrowest scope the provider offers.

## What it supports, and the honest gaps

The provider catalog ships OpenAI, Anthropic, Google Gemini, OpenRouter, Groq, Mistral, GitHub, Slack, Notion, Linear, Stripe, HubSpot, Pipedrive, Zendesk, Atlassian (Jira and Confluence Cloud), Airtable, Resend, SendGrid, Twilio, Deepgram, ElevenLabs, the Telegram Bot API, Bitrix24 (cloud and self-hosted), amoCRM, and an "Other" entry for any public HTTPS API that takes a key in a header you name. The "Other" entry is what keeps this from being a fixed list: the CRM or ERP nobody wrote a connector for still works through the proxy.

Client coverage is where the vendor is straight about its state. Claude Code, Codex, Cursor, VS Code, Gemini CLI, **Hermes** (the agent YAML `mcp_servers` block) and **OpenClaw** (`mcp.servers`) are documented as Streamable HTTP; Claude Desktop goes through `mcp-remote` because native header support in the app is a closed beta; ChatGPT needs an Actions schema because the gateway does not offer OAuth yet. The vendor publishes a `Checked live` column beside that table and **every row reads `no`**: the snippets follow each client's documentation and have not been verified against a running client. That honesty is recorded here rather than smoothed over, and it is also the reason this guide documents the gateway instead of driving it: a self-hosted gateway has no public endpoint to probe until someone stands one up.

The roadmap names the same gaps: check every snippet against the live client, a public demo instance, OAuth so ChatGPT and claude.ai connectors can use the MCP endpoint, and multiple owners with separate policies.

## Where it sits against the rest of this catalog

The shelf splits cleanly. [1Password](/hermes/mcp/servers/external/1password-mcp/) stores secrets and lets an agent *use* a variable without reading its value; that solves the file-on-disk problem for a team that already runs 1Password. [lookfirst](/hermes/mcp/servers/external/lookfirst-mcp/) gates an **action**: a named human approves a specific call and its exact arguments, the write is verified by read-back, and a signed hash chain records it. AgentKeyGate gates a **credential** instead: the agent never holds the key at all, the pass is bounded by time and call count, and the response is filtered on the way back.

Those are three different questions and an operator with a real agent deployment eventually needs all three. If the worry is "the key is in a file", start here. If the worry is "the agent will do the wrong thing with a key it legitimately holds", lookfirst answers that. If the worry is "the model sees the client's phone number", this gateway's field filter answers it and nothing else in this catalog does.

The vendor's own comparison table names OneCLI, TAP and Infisical Agent Vault, read on 7 November 2026, and the distinguishing row is the **call-count cap**: TAP and OneCLI are not described as bounding a pass by number of calls, Infisical's sessions are time-bound. That matters because a leaked pass with 20 calls and 10 minutes of life is a much smaller incident than a leaked token with a month of life.

## Does the agent ever see the key?

No. The gateway holds the key, the agent holds a pass `gwt_...` that stops working when the TTL expires or the call count runs out, and `list_services` returns the service names and the filter shape without a key value or a host. The residual risk is stated by the vendor and repeated here: anyone with root on the server, or administrator access to the AWS account behind the `ssm` vault, can read every key.

## What does the model actually receive from my CRM?

Only the types and fields the owner allowed. With a Bitrix24 lead filter that keeps the stage and the amount, the agent receives `ID`, `STATUS_ID` and `OPPORTUNITY` and the client's name, phone number and sales note are cut from the JSON before it is returned. `mask` then replaces e-mails, separated phone numbers, Luhn-valid card numbers and IBANs with `****`. Read-only is on by default for the CRM and support providers, and a blocked write does not use up the quota.

## Is it a replacement for lookfirst or 1Password?

No, they answer different questions. 1Password stores a secret so an agent can use it without reading it. lookfirst holds an action until a named human approves the exact arguments and then verifies the write. This gateway bounds a credential: what the agent may call, for how long, how many times, and what comes back. An operator running agents against real business systems usually ends up wanting all three.

## Limits Recorded

- **0 stars, created 2026-11-05, single owner, no external security audit.** This is a two-day-old project that the maintainer is actively pushing (last commit 2026-11-07T17:20Z). Treat it as a design worth adopting and a dependency to read before you run it.
- Anyone with root on the server, or administrator access to the AWS account behind the `ssm` vault, can read every key. The gateway reduces what an *agent* can do; it does not remove trust in the server or in the approval channel.
- An agent can still search by a hidden field and learn from the result count whether a value exists. Masking has no ML and does not find names.
- If someone takes over the owner's Telegram or e-mail, they can approve requests.
- Without a data filter, an approved pass allows any call the key allows.
- The `ssm` vault, Docker with a real Caddy certificate, certificate renewal behind Cloudflare, macOS and Safari are listed by the vendor as **not tested**. Verified: install and setup wizard on Ubuntu 24.04, requests and approvals over REST and MCP, HubSpot, Pipedrive, Stripe and Twilio keys, read-only mode and field filters on real responses, and a backup with a full restore.
- Zendesk stopped issuing new API tokens on **27 October 2026**; existing tokens work until **30 April 2027**, so the Zendesk card suits existing tokens only.
- Read on **2026-11-07** at `v1.0.2`. Deployment details and the environment table live in `docs/DEPLOY.md` and the README.

## See Also

- [lookfirst MCP](/hermes/mcp/servers/external/lookfirst-mcp/) - the human approval gate for agent writes, with read-back verification and a signed hash chain
- [1Password MCP Server](/hermes/mcp/servers/external/1password-mcp/) - secret storage where the agent uses a variable and never reads its value
- [CorpusIQ Runbook V1 - Governance](/hermes/mcp/runbook-governance) - the governed workflow contract these gates sit under
- [CorpusIQ Runbook V1 - Veto Power](/hermes/mcp/runbook-veto-power) - who can stop a run, and what that costs
