---
title: "ZeroBounce MCP - Email Validation Inside the Assistant"
description: "The official ZeroBounce server: validate one address or two hundred, score engagement, clean a CSV, run inbox placement, with credit spends and destroys flagged."
category: "Communication & Email"
stars: "n/a (official vendor server; open-source client at github.com/zerobounce/zerobounce-mcp)"
added: 2026-11-24
source: "An mcp.so feed card at 2026-11-24T16:18Z for /servers/zerobounce; keyless initialize on https://mcp.zerobounce.net/mcp answering 401 invalid_token with no WWW-Authenticate header; the tool inventory, annotations and the two deliberately unexposed endpoints read from the README at github.com/zerobounce/zerobounce-mcp on 2026-11-24; credits, minimum purchase and plan prices from https://www.zerobounce.net/pricing/ on 2026-11-24; the hosted-versus-self-run split from https://www.zerobounce.net/mcp and the repository README"
relevance: "★★★"
tags: [email-validation, deliverability, list-hygiene, email-scoring, email-finder, inbox-placement, warmup, account-signin, remote-mcp, communication]
last_updated: "2026-11-24"
---

# ZeroBounce MCP

**A bounced address costs a sender more than the send: reputation is scored per domain, so a list that is 8 percent dead poisons the 92 percent that is good.** ZeroBounce has sold list hygiene for a decade and now ships an official MCP server that puts validation, scoring, email finding, bulk file cleaning, inbox placement and warmup in front of an assistant. It is the rare case in this catalog of a vendor's own connector rather than a wrapper somebody built on its API, and the tool surface is deliberately annotated so a model can tell a read from a spend.

```
Server type: Remote (Streamable HTTP), account sign-in
Endpoint:    https://mcp.zerobounce.net/mcp
Auth:        sign in with the ZeroBounce account; no API key in the client config
Tools:       validation, account, bulk-file, scoring, finder, activity,
             list evaluator, allow/block filters, S3+SFTP, inbox placement, warmup
Pricing:     credits; pay as you go from $39 for 2,000 addresses
             (minimum purchase), ZeroBounce ONE $99 a month
```

## The gate, measured

A keyless `initialize` answers **401**:

```json
{"error": "invalid_token", "error_description": "Authentication required"}
```

No `WWW-Authenticate` header and no protected-resource document, so the refusal carries no pointer to an authorization server. The README's own description of the connect step is the useful part: **"You sign in with your ZeroBounce account, so there is nothing to install and no API key to copy."** The endpoint is account-gated and the sign-in happens in the client, which is the standard hosted-connector model and a dead end for any client that cannot open a browser.

There is a second path that removes the gate entirely: the same tools ship as **`@zerobounce/mcp` on npm, MIT licensed**, with the README stating that **tool names, titles and annotations match the hosted server**, so a model sees the same surface whichever one it is connected to. For an operator who does not want a vendor between the assistant and the mailbox, self-hosting with an API key is a supported first-class option rather than a downgrade. That is a distribution decision worth noting: most vendors in this catalog are hosted-only, and a few are local-only.

## What the assistant can actually do

The tool inventory is large, so the useful cut is by risk rather than by feature. Every tool carries a `title` and the four MCP annotations, and its description states in capitals whether it **spends credits** (`CREDITS:`) or **changes the account** (`WRITE:`). The tools that delete or overwrite (bulk file deletes, `delete_filter`, `delete_inbox_placement_test`, the warmup updates and deletes) are marked **`destructiveHint: true`**, so a compliant client asks before calling them.

| Group | Representative tools | The catch |
| --- | --- | --- |
| Validation | `validate` (alias `validate_email`), `validate_batch` | one address, or up to 200 in one call |
| Scoring and findings | AI engagement score, `validate` with `activityData`, `verifyPlus`, `domainInfo` | adds `domain_website_exists` and the **WHOIS registrant company name** |
| Bulk files | `send_file`, `file_status`, `get_file` | CSV in, file id out, results on the way back |
| Storage-native jobs | Amazon S3 and SFTP/FTP bulk jobs | validate, score and export files already in your bucket |
| Reputation | inbox placement test, warmup (accounts, engagement rules, seeds, statistics, SPF/DKIM/DMARC checks) | the reputation half of the product, not the validation half |
| Account | `get_credits`, `get_api_usage` | usage by status and sub-status over a date range |

Two details inside `validate` are the ones an operator will actually notice. The `timeout` is settable from **3 to 60 seconds**: a long timeout is how a mail server that graylists gets a real answer instead of `unknown`. And `domainInfo` returns the **WHOIS registrant company name** for the domain, which turns "is this address real" into "is this address a company" without a second vendor.

The bulk path has a validation rule worth quoting because it fails before the request rather than after: a `returnUrl` must be **an HTTPS callback on a public host on port 443, with no credentials in the URL and no private or special-purpose address**, and the server refuses anything else before the upload starts. `send_file` also takes zero-based column indexes for the email, first name, last name, gender and IP columns, `removeDuplicate`, `allowPhase2`, and it sends `hasHeaderRow` **as `false` when the field is left out**, a default that silently skips the first line of a file that does have a header. Read the field, do not omit it.

## Two endpoints the vendor refuses to expose

The README names the omissions and the reason, and this is the most interesting paragraph in the whole server: **setting the Inbox Placement webhook** is not exposed because it applies to the **whole API key** and belongs in the dashboard, and the **Warmup SMS/application password test** is not exposed because it takes the mailbox's **SMTP password**, which would pass through the conversation. Both are correct calls. The first keeps a single tool call from reconfiguring every integration that shares the key; the second keeps a credential out of a chat transcript. A vendor shipping an MCP server is under commercial pressure to expose everything it has; this one published its refusals in the README.

## Pricing, measured on the pricing page

Read **2026-11-24**: **pay as you go starts at $39 for 2,000 addresses** and that is the **minimum purchase**; the **ZeroBounce ONE subscription is $99 a month** and the ONE block lists **10,000 credits**; there is a **free tier at $0**. Credit mechanics: **one credit validates one address**, **AI scoring is one credit per address on top**, and **Email Finder spends 20 credits per successful query** with nothing charged for a miss.

So the arithmetic an operator needs before pointing an assistant at a list is simple and slightly brutal: a 50,000-address list is **50,000 credits** to validate and another **50,000** to score, while a single `validate` in a conversation costs one credit and is effectively free. The expensive mistake is not the chat call, it is telling the assistant "clean this file" and letting it spend a month's credits on a list that was already clean. That is what `get_credits`, `get_api_usage` and the **free List Evaluator**, a quality estimate of a list **before** it is validated, exist to prevent, and the ordering matters: evaluate, then validate the segment that needs it.

## Where it earns its place in an operator's day

- **Before a campaign.** "Is this address deliverable?" asked of one address is a one-credit answer, and the answer includes whether the domain even resolves a website.
- **Before a quote or an invoice.** A sales assistant that finds a work address from a name and a domain (`Email Finder`), then validates it, stops a proposal from going to `info@` at a parked domain.
- **After a bounce.** `get_api_usage` over a date range reports validation counts by status and sub-status, which is the shape of a deliverability problem rather than an anecdote.
- **During a migration.** Bulk file validation through S3 or SFTP means the file never has to pass through a chat context to be cleaned.

## How to connect it

1. **Hosted:** add `https://mcp.zerobounce.net/mcp` to the client as a remote HTTP server, then sign in with the ZeroBounce account on first use. No key goes in the configuration.
2. **Self-run:** `npx -y @zerobounce/mcp` (or a local install of the npm package) with a ZeroBounce API key in the environment, for clients that cannot open a browser.
3. Ask `get_credits` first. Knowing the balance before a bulk job is the difference between a planned spend and a support ticket.
4. Run the free **List Evaluator** on any file before `send_file`. If the estimate is bad, the list needs a source fix rather than a validation run.
5. Set `timeout` explicitly on any validation of a domain known to graylist; the default is shorter than the 60 seconds the field allows.

## Boundaries recorded

- **No discovery document.** Like the Codixio entry, the 401 carries no `WWW-Authenticate` and no protected-resource document exists, so browser-less clients need the self-run path or a client that supports its own account flow.
- **The tool list here is the vendor's documented inventory**, read from the README on 2026-11-24, because the hosted endpoint refuses keyless. The README states the hosted and self-run surfaces match; that claim is the vendor's and was not measured in this pass.
- **Credits are spent by design, and the defaults are quiet.** `hasHeaderRow` defaults to `false` when omitted, and scoring can double the cost of a validation run. Both are the kind of default an operator should override explicitly rather than inherit.
- **The WHOIS company name is a personal-data surface.** `domainInfo` returns a registrant company name; whether that belongs in a conversation with an AI assistant is the operator's compliance question, not a server setting.
