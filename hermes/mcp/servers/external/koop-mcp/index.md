---
title: "Koop MCP - Security Compliance Work From the Chat"
description: "SOC 2, ISO 27001, ISO 42001 and CMMC compliance work inside the assistant, behind an OAuth gate with three scopes and dynamic registration."
category: "Business Operations & Compliance"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-23
source: "The mcp.so feed card `koop` stamped 2026-11-23T15:52:00Z, which names `mcp.koop.ai/client/mcp`; a keyless initialize on that endpoint that answered 401 with an in-band JSON-RPC error; the protected-resource document at `https://mcp.koop.ai/.well-known/oauth-protected-resource`; the authorization-server metadata at `https://mcp.koop.ai/.well-known/oauth-authorization-server`; and the vendor homepage at `https://www.koop.ai`, read 2026-11-23"
relevance: "★★★★"
tags: [compliance, soc2, iso27001, iso42001, cmmc, nist-800-171, grc, audit, oauth, remote-mcp]
last_updated: "2026-11-23"
---

# Koop MCP

**Compliance programmes fail on evidence, not on policy: the control exists in a spreadsheet, the auditor asks for the artefact, and nobody can say which version was live in March.** Koop sells the other half - the certification work itself, SOC 2, ISO 27001, ISO 42001, CMMC, NIST SP 800-171, DFARS 252.204-7012 and ISO 9001 - and now publishes an MCP endpoint so an assistant can drive the requirements, the evidence and the trust-centre page from inside the chat.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.koop.ai/client/mcp
Alt host:    https://audit-mcp.koop.ai/mcp
Auth:        OAuth 2.1, PKCE S256, dynamic client registration, or a Koop API key
Pricing:     from $299/month, read on the vendor site 2026-11-23
Tools:       not readable without an account (see below)
Registry:    no record found for `koop.ai` in the official registry on 2026-11-23
```

## What the gate says before it says anything else

An anonymous `initialize` on `https://mcp.koop.ai/client/mcp` answers **HTTP 401** and the body is not a bare status line. It is JSON-RPC with an in-band refusal:

```json
{"jsonrpc":"2.0","error":{"code":-32001,
 "message":"Sign in to Koop to use these tools: connect to Koop from your app
 (in Claude Code, run /mcp and choose koop). Scripts can send a Koop API key
 as 'Bearer <key>' instead."},"id":null}
```

That is the better half of the discovery story: a client that only renders `content` blocks still gets a usable sentence, because the refusal is the message. Two credential paths are named in the refusal itself - interactive OAuth and a bearer key for scripts - so an operator does not have to choose before connecting.

**The tool list could not be read.** `tools/list` is behind the same gate, so this guide describes the surface Koop publishes and the handshake it actually serves, and stops there. A guide that lists tools it never saw is a vendor brochure with a catalog number.

## The OAuth handshake, measured

`https://mcp.koop.ai/.well-known/oauth-protected-resource` answers **200**:

| Field | Value |
| --- | --- |
| `resource` | `https://mcp.koop.ai/client/mcp` |
| `authorization_servers` | `["https://mcp.koop.ai/"]` |
| `scopes_supported` | `koop:read`, `koop:write`, `koop:draft` |
| `bearer_methods_supported` | `header` |
| `resource_name` | `Koop` |

The same document is served at the suffixed path `/.well-known/oauth-protected-resource/client/mcp`, so both the bare and the resource-relative route resolve - the inverse of servers that only answer at one.

`https://mcp.koop.ai/.well-known/oauth-authorization-server` is a complete RFC 8414 document:

| Field | Value |
| --- | --- |
| `issuer` | `https://mcp.koop.ai/` |
| `authorization_endpoint` | `https://mcp.koop.ai/authorize` |
| `token_endpoint` | `https://mcp.koop.ai/token` |
| `registration_endpoint` | `https://mcp.koop.ai/register` (dynamic registration) |
| `revocation_endpoint` | `https://mcp.koop.ai/revoke` |
| `code_challenge_methods_supported` | `S256` |
| `token_endpoint_auth_methods_supported` | `none` (public client) |
| `grant_types_supported` | `authorization_code`, `refresh_token` |
| `authorization_response_iss_parameter_supported` | `true` |

The scope split is the interesting part for an operator: **`koop:read`**, **`koop:write`** and a separate **`koop:draft`**. A draft scope that is not the write scope is how a compliance tool should be built, because the most common internal request is "show me what the auditor would see if I marked this control as implemented" and the answer must not file it.

## The frameworks, as the vendor lists them

Read off `koop.ai` on 2026-11-23, the certification surface covers:

- **SOC 2** - continuous monitoring for security, availability, confidentiality
- **ISO 27001** - information security management system
- **ISO 42001** - artificial intelligence management system
- **CMMC** Level 1 and Level 2 - US government cybersecurity for controlled unclassified information
- **NIST SP 800-171** - the control set CMMC assesses against
- **DFARS 252.204-7012** - the contractual clause that pulls 800-171 in
- **ISO 9001** - quality management

Around the certification work the vendor sells a Trust Centre (publishing credentials to buyers), Requirements Management (contractual requirements from enterprise customers in one place), Third-Party Risk Management, a "Housekeeper" agent that runs recurring compliance and insurance tasks, and professional services.

**Adjacent, and worth naming because it changes the buyer:** Koop also sells insurance - general liability, technology E&O, cyber liability, excess and umbrella, inland marine, on-road AV liability - including a package written with Lloyd's of London. An operator who starts at "we need SOC 2 to close this deal" often discovers the deal also wants a cyber policy, and one vendor quoting both is a different conversation from two.

## Pricing

The homepage states **from $299 a month** for the MCP product, read 2026-11-23. That figure is a floor and the vendor does not publish the ladder on the page this guide read, so treat $299 as the entry point and ask for the tiers rather than assuming one price.

## What an assistant can actually be trusted to do here

Compliance work is evidence work, and three failure modes matter more than tool count:

1. **A wrong answer is a certification risk, not a bad response.** The `koop:draft` scope is the structural answer: an agent proposing an evidence request should write a draft a human files, not a filing.
2. **The audit trail is the deliverable.** Ask the vendor whether every MCP-originated change carries the actor and timestamp into the same log the auditor reads. The published surface does not say, and this guide does not guess.
3. **Insurance and certification share facts** - entity name, revenue, subprocessors - and duplicated facts drift. One vendor for both is only an advantage if there is one record.

## FAQ

### Is Koop MCP a free connector?

No free tier is published. The homepage reads **from $299 a month**, so any test costs money; the only thing measurable without an account is the handshake, which is what this guide measured.

### Does it work with Claude, ChatGPT or Cursor?

The refusal message names Claude Code's `/mcp` flow explicitly, and the transport is standard Streamable HTTP with OAuth 2.1 and dynamic registration, so any client that implements the spec can connect. The two documented credential paths are interactive OAuth and a bearer API key for scripts.

### Can I read the tool list before paying?

Not from the public endpoint. `initialize` and `tools/list` are both behind the 401, so the tool list has to come from the vendor's documentation or from an account. That is a genuine limitation of this entry and it is stated rather than papered over.

### What is the difference between koop:read, koop:write and koop:draft?

The scope names are the evidence. `read` is visibility, `write` files changes, `draft` prepares a change without filing it. For an agent, asking for `read` plus `draft` is the smallest grant that still lets it do useful work, and an operator should refuse `write` until the draft path has produced something they agreed with.

## Verdict

**A first-of-class entry for security compliance** - the catalog had legal compliance (GoldLegal) and MCP audit proxies (Agent Warden, Auditspark) but nothing that runs SOC 2 and ISO certification work. Four stars rather than five for one reason: the tools are unreadable without a paid account, so the guide can certify the gate, the scope model and the framework list, and not the work. Operators who already pay for compliance tooling are the audience; anyone else should start at the pricing page and the draft scope, not at the tool list.
