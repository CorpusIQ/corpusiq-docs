---
title: "Hail MCP - A Phone Number and an Inbox for an Agent"
description: "A hosted MCP that gives an agent a real phone number, SMS and an email inbox, with consent and price checks built into the schema across a 46-tool surface."
category: "Communications / Voice"
stars: "34 (github.com/hail-hq/hail, AGPL-3.0; the hosted endpoint needs no install)"
added: 2026-11-18
source: "the mcp.so submission queue entry #7604 filed 2026-11-18T18:01:11Z, a live handshake and full tools/list on 2026-11-18, and the vendor's own MCP and pricing documentation"
relevance: ★★★
tags: [telephony, voice, sms, email, phone-number, customer-support, inbound-routing, oauth, remote, mcp]
last_updated: "2026-11-18"
---

# Hail MCP

**A business that wants an agent answering its phone needs three vendors before it needs a tool.** A carrier for the number, a voice stack for the calls, an SMS provider for the texts, and something else again for the mail. Hail collapses that into one prepaid account behind one MCP endpoint: numbers, calls, texts, an email domain, and saved agents that answer inbound traffic.

The engineering decision worth noticing is not the channel coverage. It is that the dangerous parts are parameters. Consent to contact a person is a required boolean. Buying a number requires the exact total in cents. Retrying a send requires the idempotency key from the first attempt. Those are checked server side, not left to prompt discipline.

```text
Server type:   remote Streamable HTTP (hosted), self-hostable under AGPLv3
Endpoint:      https://mcp.hail.so        (root path, no /mcp suffix)
Server:        hail, version 0.1.3, protocol 2025-06-18
Auth:          OAuth 2.1, dynamic client registration
               issuer https://hail.so/api/auth
               self-host: HAIL_API_KEY sent as a bearer token
Tools:         46 live      27 read-only · 12 write · 7 destructive
Resources:     0            Prompts: 0
Registry:      io.github.hail-hq/hail-mcp, 0.1.2 active
Regions:       us-east, eu-west, ap-south (vendor)
Queue:         mcp.so #7604, filed 2026-11-18T18:01:11Z
License:       AGPL-3.0, github.com/hail-hq/hail (34 stars, Python)
```

## The evidence tier

Discovery-open, execution-gated. `initialize` answered **200** with no credential and returned an `instructions` block written for a model rather than a person: the rules, then a four-step start order, then the paging convention. `tools/list` returned **all 46 schemas**, each carrying `readOnlyHint`, `destructiveHint`, `idempotentHint` and `openWorldHint`, plus `execution.taskSupport` on every tool that can run a task.

`tools/call` returned **401** on four separate calls, with a `WWW-Authenticate` header naming `https://mcp.hail.so/.well-known/oauth-protected-resource`. That document answers **200** and is complete for its purpose:

```json
{"resource":"https://mcp.hail.so/",
 "authorization_servers":["https://hail.so/api/auth"],
 "bearer_methods_supported":["header"]}
```

The authorization server document lives on the **other host**, at `https://hail.so/.well-known/oauth-authorization-server/api/auth`, and is the fuller of the two: issuer `https://hail.so/api/auth`, authorization, token, jwks, registration, introspection and revocation endpoints, `response_types_supported: ["code"]`, and grant types including `authorization_code`, `client_credentials` and `refresh_token`. The same well-known route **404s on the MCP host**, which is correct for a split deployment and is the shape to expect rather than an error.

No live business record was read, because no account was opened. Everything measured here is the surface a reader can re-measure in two requests.

## The safety envelope is in the schema

Hail ships 27 read-only tools, 12 that write and 7 flagged destructive. The seven destructive ones are `acquire_number`, `release_number`, `submit_verification`, `resubmit_verification`, `amend_sms_application`, `cancel_verification` and `delete_agent`, and the first three carry their own confirmation argument: `confirm_total_cents`, `confirm_e164`, `confirm_name`.

The instructions state the same contract in model-facing words:

```text
- place_call, send_sms and send_email need recipient_consent=true. Set it only
  when the user confirms the recipient agreed to be contacted. Marketing also
  needs consent_source.
- acquire_number charges the workspace at once. Call quote_numbers, show the
  user the price, and buy only after they agree.
- release_number and delete_agent cannot be undone. Ask the user first.
- submit_verification files with the carrier and cannot be undone...
- To retry a send or a purchase, pass the idempotency_key it returned, so the
  retry does not send or buy twice.
```

Two details make that more than prose. `recipient_consent` is validated as the JSON boolean `true`, and the vendor documentation says strings such as `"true"` and numbers such as `1` are refused **before any request is sent**, which closes the usual hole where a model writes a truthy string and the API accepts it. And `acquire_number` re-checks the arithmetic: pass a `confirm_total_cents` that does not equal the offer's `monthly_cents + setup_cents` and the call fails **409** having charged nothing. A price confirmation that is compared against the quote is a different control from a price quoted in chat.

The rest of the money path is equally explicit. `quote_numbers` returns `monthly_cents`, `setup_cents` and a `quote_id`, and those quotes **expire in ten minutes**, so a purchase needs a fresh quote rather than a remembered one.

## The vendor's three tool counts, and the live one

Documentation drift is normal; four different numbers on one product is worth recording:

| Surface | Count |
|---|---|
| MCP docs prose, "The server exposes N tools" | **36** |
| The same page's tool table, rows | **38** |
| The marketing page at hail.so/mcp | **37** |
| Live `tools/list` | **46** |

The eight tools the docs table does not carry are `create_file_upload`, `route_email_domain`, `check_verification`, `check_verification_documents`, `resubmit_verification`, `get_sms_application`, `preview_sms_application` and `amend_sms_application`. Three of those are read-only helpers for the carrier registration flow, and one is a genuine capability an operator should notice: `create_file_upload` returns a **one-time upload link** an agent can hand to a shell, so bytes can enter the account without passing through the model's context.

Version drift runs the other way from the usual direction: the endpoint reports **0.1.3** while the registry carries **0.1.2**, so the public record is one release behind what a client actually speaks.

## What the surface actually covers

Five families, in the order the vendor tells an agent to use them.

**Numbers.** `quote_numbers` searches live carrier offers by country, capabilities, type, area code, city or region; `list_number_regions` returns the US state and Canadian province codes the search accepts; `list_numbers` and `get_number` read what the workspace holds; `route_number` points a number's inbound calls at one saved agent and its inbound texts at another; `release_number` gives it back.

**Calls.** `place_call` originates with `to` and `recipient_consent`, and takes a `system_prompt`, a saved `agent_id`, a `from_`, a first message, a language, `ai_disclosure`, `recording_enabled` and `tools`. `get_call` returns status, timing and transcript; `list_calls` pages the recent set by status or destination.

**Messages.** `send_sms` and `send_email` take the same consent gate, with `idempotency_key`, `metadata`, and for mail `body_text`, `body_html`, attachments and a reply-to. The read side is the deeper half: `get_email_events` returns a delivery and engagement timeline per message, `get_email_stats` aggregates counts and rates over a window and a bucket, and `get_email_raw` plus `get_email_attachment` hand back presigned URLs for the original MIME and its files.

**Agents.** `create_agent` saves a brain (instructions, greeting, disclosure line, voice, tools, duration limits), `route_email_domain` decides which agent answers a domain and for whom, and `update_agent` changes fields while keeping the rest.

**Carrier verification.** This is the family that decides whether an international number is usable at all, and the vendor exposes the whole legal path: `get_verification_requirements` returns the fields, the document slots and whether an address is required for a given country, number type and subject type; `check_verification` and `check_verification_documents` dry-run the form without filing; `submit_verification` files with `attest_authorized: true`; `get_verification` is polled for `approved`, `rejected` or a next step; `confirm_verification` enters the code a carrier texts to a person.

The limits are stated rather than discovered: JPG, PNG or PDF at 10 MiB each and 29 MiB in total, at most 20 files and 20 fields, slot names of letters, digits, hyphen and underscore up to 64 characters, and a second submission for the same country, type, subject and name returned as **409** while one exists.

## What it costs, as published

Prepaid, no subscription, one invoice:

```text
voice            $0.10 / min      US and Canada, line + voice + transcription + model
                 +$0.01 / min     when recorded
SMS              $0.018 US        $0.035 Canada        $0.20 elsewhere
email            $1 / 1,000       sending and receiving at the same rate
dedicated number from $0.50 / month (calls), $1.15 (calls and texts), no markup
pooled numbers   no rental fee, for outbound only
```

The comparison the vendor makes is the interesting one, and it is arithmetic rather than a slogan: a common voice-agent stack bills the AI platform, the model, the text-to-speech and the phone line separately for **$0.149** a minute, while the same four parts inside Hail are quoted from **$0.10**. The vendor labels that comparison an estimate built from vendor pages read in October 2026, which is the right way to present it.

## Where it fits, and what to watch

An operator can now give an agent a business line: answer inbound calls with a saved agent, take a message by SMS, reply to mail on the company's own domain, and hand a call back to a person when the agent is out of its depth. The read surfaces matter as much as the write ones, because `get_email_events`, `get_email_stats` and `get_events` turn a communications tool into something that can be measured.

Three cautions belong in any deployment.

This server **spends money and contacts real people**. The consent parameter and the price confirmation are real controls, but they are arguments to a tool, and a client that does not surface approvals will send them without a human in the loop. Keep the approval prompt on for `place_call`, `send_sms`, `send_email`, `acquire_number` and `submit_verification`.

Verification documents **pass through the model's context** and stay in the client's transcript; the vendor says so directly and recommends having the user hand over each value and file in conversation. That is a privacy decision an operator should make before filing anything.

And the vendor's own retention terms are worth reading before a number is registered: the pricing page states that recordings are kept for **30 days**, or **7 days** or **1 year** if chosen, and that recording is best effort, with the per-minute rate applying even when a recording is unavailable.

### Can it be used without an account?

No. The discovery surface is open, the execution surface is not: every tool call needs an OAuth token, and the token comes from a Hail account. For a self-hosted deployment the auth mode changes to a bearer API key rather than disappearing, and the carrier and channel providers remain external services.

### How does it differ from a voice-only agent platform?

Voice is one of five families here. The same account provisions the number, registers it with the carrier, routes inbound calls and texts to different agents, and runs a real mailbox with delivery events. The verification flow is the part no voice-only platform exposes over MCP, and it is the part that decides whether a number in a given country works at all.

## Connecting

Hosted, any MCP client over Streamable HTTP:

```json
{"mcpServers": {"hail": {"type": "http", "url": "https://mcp.hail.so"}}}
```

In Claude, Settings then Connectors then Add custom connector, paste `https://mcp.hail.so` and click Allow on first use. In ChatGPT the connector sits behind Developer Mode. Access tokens last 30 days and refresh tokens 180 days, per the vendor, and each authorized client appears in the console at `hail.so/console/apps` where revoking deletes every token for that client.

Self-hosted, from `github.com/hail-hq/hail` (AGPL-3.0, Python):

```bash
# the MCP service selects its auth mode from the environment at boot
export HAIL_API_KEY=...
curl -H "Authorization: Bearer ${HAIL_API_KEY}" http://localhost:8081/
```

A stdio entry point exists for hosts that require one: `docker compose run --rm -T mcp python -u -m hailhq.mcp.stdio`.

## Sources

- Endpoint: https://mcp.hail.so
- Protected resource metadata: https://mcp.hail.so/.well-known/oauth-protected-resource
- Authorization server metadata: https://hail.so/.well-known/oauth-authorization-server/api/auth
- MCP reference: https://hail.so/docs/mcp
- Pricing: https://hail.so/pricing
- Repository: https://github.com/hail-hq/hail
- Submission: the mcp.so queue as #7604 on 2026-11-18
