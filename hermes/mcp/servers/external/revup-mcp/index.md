---
title: "Revup MCP - Promotions, Forms and Giveaways"
description: "Create and edit giveaways, contests, forms and surveys from chat, with scoped OAuth, previews and performance reports - hosted MCP."
category: Marketing
stars: n/a (hosted platform, revup.com)
added: 2026-10-05
source: "mcpservers.org /all"
relevance: ★★
tags: [promotions, giveaways, contests, surveys, marketing, oauth, reports, remote-mcp]
---

# Revup MCP

**Launch and run promos without leaving the conversation.** Revup is a hosted promotions platform - giveaways, contests, forms, instant wins, purchase promotions and surveys - and its MCP server exposes the whole workflow to an assistant: discover what the account can do, find and read a promotion, create or duplicate one with a schema the server itself describes, import images, validate, render desktop and mobile previews, then read aggregate performance reports. Edits are revision-checked and idempotent, and every call respects the scopes you approved.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (authorization code with PKCE S256; automatic client registration)
Endpoint: https://revup.com/mcp
Scopes: account:read, promotions:read, promotions:write, analytics:read, offline_access
Types: giveaway, contest, form, instant_win, purchase, survey
Built by: Revup
```

## Why This Matters for Operators

Promotions are a growth channel that punishes sloppy setup: the dates, the rules, the entry fields, the page itself. Revup's MCP server turns each of those into something the assistant can read back and check before it goes public: `get_promotion_schema` describes the supported settings, `validate_promotion` returns blockers and warnings, and `render_preview` returns a revision-bound image so the operator sees what entrants will see. Creation and edits are explicit about consequences - there is no separate publication approval step, so changes can reach the public page immediately - which is why the server models scopes and idempotency keys carefully.

**Reports close the loop.** `get_promotion_report` returns aggregate metrics with metric definitions, denominators and freshness limits, filterable by period, comparison range and breakdowns (device, source, campaign, landing). Participants stay anonymous: no identities or raw paths in reports.

## Tools

| Tool | What it does |
|---|---|
| `get_account_capabilities` | The connected account, plan and allowed operations |
| `list_promotions`, `get_promotion` | Find promotions; read saved details by section |
| `get_promotion_schema` | Discover supported settings (content, fields, colors, assets, schedule) before writing |
| `create_promotion` | Create by type (giveaway, contest, form, instant_win, purchase, survey) with schedule and idempotency key |
| `update_promotion` | Ordered, revision-checked edits with the same idempotency discipline |
| `duplicate_promotion` | Copy supported configuration; participants and results are not copied |
| `get_operation_status` | Poll asynchronous work like duplication |
| `list_assets`, `import_image`, `get_asset_status` | The account's image library and import flow (PNG, JPEG, WebP, GIF up to 5 MiB) |
| `validate_promotion` | Readiness blockers and warnings; advisory, not a gate |
| `render_preview`, `preview_promotion` | A revision-bound JPEG preview per viewport; the standard, public and share links |
| `get_promotion_report` | Aggregate metrics with periods, comparisons and breakdowns |
| `submit_feedback` | Report a bug or missing capability to Revup from any connection, read-only included |

Writes expect local dates with a timezone, reuse the same idempotency key only for exact retries, and refuse stale revisions: read the current promotion, reconcile, then submit. Successful writes are replayable for up to seven days on the same connection.

## Installation

Claude Code style clients add the remote server and sign in:

```bash
claude mcp add --transport http revup https://revup.com/mcp
```

Codex:

```bash
codex mcp add revup --url https://revup.com/mcp
codex mcp login revup --scopes account:read,promotions:read,promotions:write,analytics:read,offline_access
```

Claude (web and desktop): Customize, Connectors, Add custom connector, paste the URL; Revup supports automatic OAuth client registration, so no client ID is needed. ChatGPT connects through developer mode using the same URL. Connections can be removed any time under Revup Account, Integrations, MCP Connections.

## Business Relevance

- **E-commerce and DTC marketers** run giveaways and contests with dates, rules and page design under agent-assisted setup and preview.
- **Teams running surveys and forms** create a feedback survey with no email field in one conversation, then read aggregate results.
- **Agencies** duplicate a proven promo structure for the next client campaign, idempotently, without rebuilding it by hand.
- **Analysts** pull aggregate reports per period and source to see which channels actually drove entries.

## Integration with CorpusIQ

A promotion is a campaign run outside the standard ad stack, and its effect shows up inside it. Revup answers how the promo itself performed (entries, completions, source breakdowns); CorpusIQ reads the surrounding business (GA4 traffic, ad performance, Shopify orders) to show what the promotion did to the rest of the funnel. The agent compares the two read-only surfaces in one answer, while all promotion changes stay behind Revup's OAuth scopes and your approval.

## Limitations

- MCP does not expose participant identities or exports, winner selection, participant messaging, payments or purchase-entry authoring; those stay in the app.
- There is no draft or publication approval step: creating or editing can affect the public page immediately.
- Participant-facing design is limited to supported schemas; custom CSS is sanitized and scoped.
- Some tools need paid plans or specific account roles; `get_account_capabilities` reports what the connection can use.
- API keys are for the REST API only; the MCP connection is OAuth.

## FAQ

### Which promotion types can it create?

Giveaway, contest, form, instant_win, purchase and survey, with aliases like sweepstakes accepted. The type is set explicitly at creation and cannot be changed later.

### Is there a preview before it goes live?

Yes: `validate_promotion` returns readiness warnings, `render_preview` returns a revision-bound JPEG per viewport, and `preview_promotion` returns the preview, public and share links. There is no separate approval gate, so review before sharing the public link.

### Can it message participants or pick winners?

No. Messaging, winner selection, participant exports and payments are not exposed over MCP; they remain in the Revup app.

### What stops a retried edit from double-applying?

Idempotency keys: reuse the same key only to retry the identical call; a new operation needs a new key, and stale revisions are refused until you read and reconcile.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Toffu MCP - AI Marketing Agent for Ad Accounts](/hermes/mcp/servers/external/toffu-mcp/)
- [Solnk MCP - Publish to Nine Social Platforms](/hermes/mcp/servers/external/solnk-mcp/)
