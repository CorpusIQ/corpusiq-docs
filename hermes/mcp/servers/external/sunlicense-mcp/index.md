---
title: "SunLicense MCP - License Keys for What You Sell"
description: "The hosted SunLicense connector: issue, suspend and revoke licence keys, free a machine and read licence stats from chat, on every plan including Free."
category: Commerce and Digital Goods
stars: ★★ (official vendor, OAuth gate, 401 measured, tools documented not driven)
added: 2026-11-03
source: "the chatmcp/mcpso submission #6679 filed 2026-11-03T16:42:22Z, a keyless probe of https://api.sunlicense.com/mcp answering HTTP 401 with protected-resource metadata and an RFC 9457 problem body, the vendor MCP page at docs.sunlicense.com/guide/remote-mcp, and the pricing page read directly"
relevance: ★★★
tags: [licensing, license-keys, entitlement, digital-goods, piracy, oauth, official, remote-mcp]
last_updated: "2026-11-03"
---

# SunLicense MCP

**You sell a plugin, a desktop app or a bot. One buyer posts the file, and from that afternoon every copy is free. The lock that stops it is a key check on launch, and the second problem is that the lock is only useful if issuing, moving and killing a key is faster than posting a support ticket.**

```
Server type:  Remote (Streamable HTTP)
Endpoint:     https://api.sunlicense.com/mcp
Auth:         OAuth, per person, signed in at the SunLicense dashboard
Discovery:    /.well-known/oauth-protected-resource/mcp
Plans:        every plan includes it, Free included
Call limits:  50 a day Free, 300 Lite, 3,000 Standard, shared with the CLI
Registry:     the submission names com.sunlicense/mcp; not re-probed here
```

## What it does

The hosted server exposes the same tools as the `sunlicense mcp` CLI, scoped to the role of the person who signed in and to the permissions they ticked on the consent page. The vendor lists the surface as products and policies, licences, customers, machines, access rules, API keys, statistics and the documentation. The vendor's own demo shows the calls by name:

| Call | What it does |
| --- | --- |
| `integration_status` | Reads the account before anything is created |
| `create_product` | Creates the product a key belongs to |
| `create_policy` | Creates a plan with its machine limit, for example `Pro` at `maxMachines: 2` |
| `sdk_snippet` | Returns the SDK code for a language, so the check goes into the build |
| `create_api_key` | Mints a build-time key to place in the project's git-ignored config |
| `issue_license` | Issues a key against a policy and a customer email |

Around those, the platform does the part an operator actually needs: a machine can be freed when a customer changes computer, a key can be suspended, reinstated, revoked, rotated or deleted, keys stay masked until someone asks to reveal one, leaked keys are blocked, and the account carries statistics on checks, versions and installs. Offline licences keep paying customers working when they are not online, which is the failure mode a naive key check creates.

## What this pass measured, and what it did not

A keyless `POST` to `https://api.sunlicense.com/mcp` returned **HTTP 401** with `WWW-Authenticate: Bearer resource_metadata="https://api.sunlicense.com/.well-known/oauth-protected-resource/mcp"` and an `application/problem+json` body: `{"title":"Unauthorized","status":401,"detail":"Connect SunLicense from your AI app to get a token for this server"}`. That is a live, auth-gated server that tells a client what to do next rather than returning an empty 401.

No tool was called, because the connection needs a SunLicense account. Everything below about behaviour comes from the vendor's documentation and pricing pages, read on 2026-11-03, and it is labelled that way rather than written as a driven session.

## The permission model, as documented

The consent screen is the part worth reading before connecting. It shows the app's name and where the answer goes, the organisation the connection will work in, and a list of permissions with the ones you do not want left unticked. Nobody can grant more than their own role holds. If you work in more than one organisation, the connection binds to the one you are signed in to, and switching means reconnecting.

Changes are attributed to you, and the licence page carries the attribution: **"Issued by AI assistant (Claude)"**. Disconnect lives in Settings, then Access tokens, then Connected AI apps, and takes effect within **30** seconds. A connection also ends after **30** days unused, when you leave the organisation, or when the connector is removed in the client.

The data statement is unusually specific, and it is the reason this entry is worth having: SunLicense receives the tool name and its arguments and nothing else, never prompts, chats, files or code. Tokens are stored as one-way hashes. What the client receives is bounded by the caller's role, and a full licence key only travels when someone explicitly asks to reveal it.

## Limits that bite on a small plan

Every tool call counts toward the organisation's daily AI assistant allowance: **50** a day on Free, **300** on Lite, **3,000** on Standard, shared with the CLI. Over the limit the client gets a short message with the reset time, which is **00:00 UTC**, and the running count with the last thirty days sits on the billing page. An agent that iterates on a policy in a loop will spend that allowance in minutes, so the operator should expect to state the change once rather than let the model converge by trial.

Plans read directly from the pricing page on the same day: Free at **$0** with **3** products, **100** licences and **10,000** checks a month; Lite at **$4.17** a month billed **$50** yearly, **5** products, **2,500** licences, **250,000** checks, customer portal, Sentinel and automations; Standard at **$16.67** a month billed **$200** yearly, unlimited products, licences, checks and seats. Code obfuscation is on every plan at a run allowance, and product downloads appear at Standard.

## Where it ships into, which is the operator argument

SunLicense is a sales-channel adapter as much as a key server, and the vendor publishes the per-store mechanics: BuiltByBit writes the key into the download, SpigotMC issues a key per buyer, Gumroad and Lemon Squeezy use their own key from the receipt, Payhip and itch.io and Ko-fi use a redeem page, Stripe shows the key on the checkout page, WooCommerce revokes on refund, and Envato turns CodeCanyon purchase codes into licences. Seven SDKs cover Java, JavaScript, Python, .NET, PHP, Lua and Rust.

That matters for the same reason the checkout entries in this catalog matter: the gap between a sale and an entitlement is where refunds, chargebacks and shared files leak revenue.

## Where this sits in the catalog

Two neighbours touch licences and neither does this job:

- [GumroadDNA MCP](/hermes/mcp/servers/external/gumroad-dna-mcp/) reads and toggles licence keys inside one store, Gumroad, as part of store operations. It cannot issue a policy, free a machine, or serve a customer who bought through Stripe or Tebex.
- [LicenseGuard MCP](/hermes/mcp/servers/external/license-guard-mcp/) evaluates open-source dependency licences against how you ship. That is compliance for code you consume, not entitlement for code you sell.

The payment entries ([Stripe MCP](/hermes/mcp/servers/external/stripe-mcp/), [RevClamp MCP](/hermes/mcp/servers/external/revclamp-mcp/)) answer what was charged and what leaked from it. None of them answers whether the copy running on a machine right now was paid for.

## Connect it

OAuth on an interactive client:

```json
{
  "mcpServers": {
    "sunlicense": {
      "type": "http",
      "url": "https://api.sunlicense.com/mcp"
    }
  }
}
```

Claude Code, as the vendor documents it:

```bash
claude mcp add --transport http sunlicense https://api.sunlicense.com/mcp
```

Then run `/mcp` and choose Authenticate. ChatGPT identifies itself with a metadata document and signs its token request with its own key; the vendor's note is that if the connection is refused, the client needs dynamic client registration enabled rather than a second attempt.

## Do not use it as

- **A payment check.** The key proves entitlement. It does not prove the money arrived, and a refund reverses it only where the store integration says so.
- **A piracy detector on its own.** Shared keys are found by the platform's own signals, not by asking an agent to guess from a list.
- **A bulk migration tool.** The call allowance is small on Free and Lite, and bulk imports are a platform feature, not a chat loop.
- **A read of your customers' details.** Names and emails come back within the caller's role, and full keys only on request.

## FAQ

### Does it cost extra for the MCP connection?
No. The vendor states it is included in every plan, Free included, and bills it as AI assistant calls per day rather than as an add-on.

### Can an agent issue a key without me seeing it?
It can, if the permission is ticked and your role allows it, and the licence page records the change as issued by the AI assistant. Ticking fewer permissions is the control, not a prompt instruction.

### What happens to a paying customer when a key is suspended?
Suspension stops the checks on that licence. Because licences can be signed for offline use, an already-activated customer keeps working until the signed licence expires or is revoked, which is the vendor's stated design against locking out paying users.

### Is the key stored in my project?
The `create_api_key` flow returns a build key intended for a git-ignored config file, and the licence keys themselves are checked at runtime rather than committed.

### Does it work for a desktop app, not just a plugin?
Yes. The SDK list covers .NET and JavaScript for desktop and Electron builds, and the vendor names WPF, WinForms and Avalonia explicitly.

## See Also

- [GumroadDNA MCP](/hermes/mcp/servers/external/gumroad-dna-mcp/)
- [LicenseGuard MCP](/hermes/mcp/servers/external/license-guard-mcp/)
- [Stripe MCP](/hermes/mcp/servers/external/stripe-mcp/)
- [RevClamp MCP](/hermes/mcp/servers/external/revclamp-mcp/)
