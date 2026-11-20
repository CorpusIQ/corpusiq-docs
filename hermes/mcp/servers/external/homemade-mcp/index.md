---
title: "Homemade MCP - Cloud Dev VMs for Coding Agents"
description: "Cloud Linux VMs with Claude Code and Codex signed in, priced per second, and one MCP tool for every API operation."
category: "Development / Cloud Dev Environment"
stars: "n/a (hosted vendor endpoint; no MCP wrapper published)"
added: 2026-11-20
source: "the mcp.so feed card filed 2026-11-20T18:01Z plus the mcp.so detail page (marked Verified and Featured, submitted by the founder), an anonymous initialize answering 401 with a complete WWW-Authenticate, both OAuth metadata documents, the vendor's OpenAPI 3.1.0 document at api.homemade.dev/openapi.json (28 paths, 41 operations), docs.homemade.dev/remote-mcp, homemade.dev/llms.txt and the pricing page"
relevance: ★★
tags: [cloud-vms, coding-agents, claude-code, codex, dev-environments, preview-environments, sandboxes, oauth, per-second-billing]
last_updated: "2026-11-20"
---

# Homemade MCP

**A coding agent that runs on the operator's laptop stops when the laptop closes. This is the version where it does not: one VM per project, an agent signed in inside it, and a preview URL for every port.**

```text
Server type:   remote Streamable HTTP
Endpoint:      https://api.homemade.dev/mcp   (also https://www.homemade.dev/mcp)
Server name:   Homemade
Auth:          OAuth 2.0 (authorization code with PKCE S256, dynamic registration)
               or a Bearer API key created in the account
Tool surface:  one tool per public API operation
API shape:     OpenAPI 3.1.0, "Homemade API 1.0.0", 28 paths, 41 operations
Registry:      no record under any Homemade search (see Name collision, below)
Vendor:        https://homemade.dev, docs at https://docs.homemade.dev
```

## What the server is

Homemade sells cloud Linux VMs by the second. Its own `llms.txt` states the product in one paragraph:

> Homemade gives every project Linux VMs in the cloud. Each VM starts from your repo with dependencies installed and services running, has a preview URL for every port, and has Claude Code, Codex, OpenCode, pi, Kimi and Grok installed and signed in. VMs sleep when idle and wake where you left them.

That is the whole offer, and it is the reason the MCP endpoint matters: the same account that holds the VM holds the agent running inside it, so a chat client can create the machine, run commands on it, message the agent, and read the result back, without the operator owning a terminal on that host.

The docs describe the MCP surface as one tool for every public API operation. The public API document is the checked form of that claim.

## The tool surface, from the vendor's own OpenAPI

`GET https://api.homemade.dev/openapi.json` answers **200** without a key and serves **97,790** bytes of OpenAPI **3.1.0** (title *Homemade API*, version *1.0.0*, one server, `apiKey` security). It declares **28** paths and **41** operations, in six families:

| Family | Paths | Operations | What the family covers |
|---|---|---|---|
| Projects | 4 | 6 | `listProjects`, `createProject`, `getProject`, `deleteProject`, `listProjectBranches`, `updateProjectSettings` |
| VMs | 13 | 17 | `listVms`, `createVm`, `getVm`, `deleteVm`, `updateVm`, `sendToAgent`, `listChatSessions`, `createChatSession`, `deleteChatSession`, `listTerminalSessions`, `deleteTerminalSession`, `dismissVmSignal`, `execVm`, `getVmRuntime`, `sleepVm`, `extendVmSleep`, `wakeVm` |
| Sandboxes | 4 | 8 | `listSandboxes`, `createSandbox`, `getSandbox`, `deleteSandbox`, `extendSandbox`, `execSandbox`, `readSandboxFile`, `writeSandboxFile` |
| API keys | 2 | 4 | `listApiKeys`, `createApiKey`, `deleteApiKey`, `renameApiKey` |
| SSH keys | 2 | 3 | `listSshKeys`, `createSshKey`, `deleteSshKey` |
| Utility | 3 | 3 | `getMe`, `validateConfig`, `reportAgentSetup` |

The three columns reconcile: **28** paths and **41** operations, and the VM family is the one that carries the product, because `execVm` and `sendToAgent` are what let an agent act inside the machine rather than only manage it. A `path` can carry more than one method (the API-key paths take GET and POST on one, DELETE and PATCH on another), which is why the operation count is the larger number.

## Authentication, measured

An anonymous `initialize` answers **401** with a complete challenge:

```text
WWW-Authenticate: Bearer resource_metadata="https://api.homemade.dev/.well-known/oauth-protected-resource/mcp",
                  scope="api offline_access"
```

The body names the two accepted paths rather than a generic refusal:

```json
{"error":"unauthorized","message":"Sign in with OAuth, or send a Homemade API key as a Bearer token."}
```

Both protected-resource routes answer **200** and agree: `resource` is `https://api.homemade.dev/mcp`, `resource_name` is *Homemade*, `bearer_methods_supported` is `["header"]`, and `scopes_supported` is `["api","offline_access"]`. The same document is served at the apex with `resource` set to `https://www.homemade.dev`, which is the address the docs give for browser-bound clients.

The issuer document at `/.well-known/oauth-authorization-server` (identical to `/.well-known/openid-configuration`) is complete enough for a client to register itself:

```text
authorization_endpoint  https://api.homemade.dev/api/auth/oauth2/authorize
token_endpoint          https://api.homemade.dev/api/auth/oauth2/token
registration_endpoint   https://api.homemade.dev/api/auth/oauth2/register
grant_types_supported   authorization_code, client_credentials, refresh_token
code_challenge_methods  S256
token auth methods      none, client_secret_basic, client_secret_post, private_key_jwt
scopes_supported        openid, profile, email, offline_access, api
dpop algs               EdDSA, ES256, ES512, PS256, RS256
```

`client_credentials` being offered matters on a surface where a server-side script is the expected client: a CI job can hold a machine without a browser in the loop. The docs list the API-key path for exactly that case (`claude mcp add --transport http homemade https://api.homemade.dev/mcp --header "Authorization: Bearer <key>"`), and note that an app connected over OAuth cannot mint API keys.

## What it costs, and the rates checked by hand

The pricing page gives three plans and five machine sizes. Reproduced from its own rate table at **730** hours a month:

| Size | Spec | Rate | Always on, 730 h |
|---|---|---|---|
| nano | 0.5 vCPU, 1 GB, 10 GB disk | $0.012/h | **$8.76** |
| tiny | 2 vCPU, 4 GB, 20 GB disk | $0.0162/h | **$11.83** |
| small | 4 vCPU, 8 GB, 30 GB disk | $0.0324/h | **$23.65** |
| medium | 8 vCPU, 16 GB, 60 GB disk | $0.0648/h | **$47.30** |
| large | 16 vCPU, 32 GB, 100 GB disk | $0.18/h | **$131.40** |

Every figure matches the page's own "always on" column to the cent.

- **Hobby**, $0 a month: **25** computer-hours a month, **one** computer at a time, nano or tiny only, up to 10 GB disk, sleeping computers kept **7** days.
- **Pro**, $20 a month: **$20** of running time included every month, then pay per second, no cap on hours or on computers at once, every size up to 16 vCPU / 32 GB, **1 TB** of egress, sleeping computers kept **30** days (forever with an add-on), each additional team member **$20** a month.
- **Enterprise**: dedicated hosts, custom sizes, sleeping computers never deleted, an SLA.

Sleeping time is free and billed per second, so the honest model is a rate per running hour against a monthly allowance rather than a flat seat.

## Where it fits, in the vendor's own words

The `llms.txt` states the fit and the non-fit, which is more than most listings do:

- **Good fit:** running coding agents in the cloud on a machine per task, a cloud dev environment per branch, preview environments for a running dev server, a sandbox where an agent can run any command.
- **Not a fit:** thousands of short code snippets per second inside your own product (the vendor points at E2B, Daytona and Modal for that), GPU work (no GPU sizes), Windows development (Linux only), and dev environments that must run inside your own cloud account (self-hosted Coder).

That list does useful work for us: it places Homemade next to, not on top of, the SDK-sandbox class.

## Name collision worth recording

The official registry has a product called **homemade**, and it is not this one. `com.homemade-global/homemade` (versions to **1.3.2**, website `homemade-global.com`, remote `homemade-global.com/api/mcp/public`) is a weekly home-cooked lunch service in Israel: menu, prices, coverage, quotes. Three registry searches for this product (`api.homemade.dev`, `homemade.dev`, `Homemade API`) returned **zero** records, so the cloud-VM vendor is unlisted there and the name is taken by an unrelated business.

## Evidence, and what was not measured

The surface was measured to the metadata and no further: **401** with a full challenge, both protected-resource documents, the issuer document, the public OpenAPI document, the docs page, `llms.txt` and the pricing page. **No tool was called and no tool response was read**, because both accepted paths need a credential this host does not hold. Nothing in this guide is inferred from the MCP tool names; the API operations, rates and limits are quoted from documents the vendor publishes unauthenticated.

## Why it earns a place in this catalog

The catalog already carries a sandbox entry, superserve-sandbox, catalogued in the June sweep as a Firecracker microVM you run one command in. Homemade is a different object: persistent **projects** with branches and PR previews, a **coding agent signed in** inside the machine, chat sessions against that agent, and sleep/wake as a first-class cost control. The distinct slice is the hosted coding agent plus the preview URL, not the sandbox primitive.

## Connect it

```json
{
  "mcpServers": {
    "homemade": {
      "url": "https://api.homemade.dev/mcp"
    }
  }
}
```

Claude Code takes `claude mcp add --transport http homemade https://api.homemade.dev/mcp`, Codex takes `codex mcp add homemade --url https://api.homemade.dev/mcp`, Cursor needs the `mcp.json` block above, and ChatGPT reaches it as a developer-mode custom connector with OAuth. The first connection opens a browser consent page; an approved app appears under *Connected apps* in the account and loses access the moment it is disconnected.
