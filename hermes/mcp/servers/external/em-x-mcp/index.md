---
title: "EM+x MCP - CorpusIQ Docs - CorpusIQ"
description: Board-ready consulting deliverables from chat — steerco readouts, executive briefs, market scans, and QBR decks built by an agentic consulting team on your own templates
category: Productivity
stars: n/a (new listing)
added: 2026-08-12
source: mcp.so
relevance: ★★★
tags: [productivity, consulting, presentations, powerpoint, decks, strategy, executive, remote-mcp]
---

# EM+x MCP

**Remote MCP server (Streamable HTTP, OAuth) for EM+x.** Turns your conversation into board-ready deliverables — steering-committee readouts, executive briefs, market scans, QBR decks, and program updates — each built by an agentic consulting team using your own templates. The brief builds itself from the chat (audience, the decision it must drive, the evidence), a storyline is proposed where every section title states an argument, and nothing gets drafted until you approve it. Deterministic quality gates check structure, data, and layout; an adversarial partner review checks the finished document against the brief before you ever see it. Output is a native .pptx or .docx on your own template's slide masters, palette, and fonts.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in on first connect)
Endpoint: https://emplusx.com/api/mcp
Tools: 33 (deliverable lifecycle, templates, versioning, billing, interactive panels)
Pricing: Free — 1 project + 5 revisions/month; paid plans from $8/month
Category: Productivity / Consulting
Built by: Cubed Studios (github.com/sundar2012/emplusx-mcp)
```

## Why This Matters for Operators

Every operator has the same meeting rhythm: steerco readouts, QBR decks, exec briefs, market scans. Agents draft them today, but the drafts still look agent-drafted — generic structure, no house style, no evidence discipline. EM+x inverts the flow: you describe the decision, it proposes an argument-led storyline you approve *before* drafting, then a consulting-style team drafts, charts, and designs every page from your evidence, with deterministic gates and an adversarial review catching weak pages automatically. The deliverable is a native .pptx/.docx on your own template — not an export that approximates it. This is the first MCP that treats the deliverable, not the draft, as the product.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `create_deliverable` | Files the brief from chat and proposes a section structure for approval (retry-safe via idempotency key) |
| `update_brief` | Re-proposes structure after more evidence or a sharper decision |
| `confirm_and_generate` | Builds the deliverable from the user-approved structure |
| `get_job_status` | Polls build/edit jobs (done, error, interrupted) |
| `refine_deliverable` | Revises a built version by instruction ("tighten section 2", "add a risks page") |
| `approve_deliverable` | Pins approval to the exact version the user saw |
| `list_projects` / `list_versions` | Project portfolio and version history with gate status |
| `list_templates` / `get_template_upload_link` | Brand-template library; upload links minted from chat (30-min expiry) |
| `clone_style` | Copy brand style from one project to another ("make it look like my Q3 deck") |
| `get_download_link` | Short-lived download link for a built artifact |
| `show_deliverable_panel` | Interactive project panel: outline editing, live build progress, page previews |

Plus billing tools (`get_upgrade_link`, `get_billing_portal_link`) — surfaced only when an allowance is hit or the user asks.

## Installation

```bash
claude mcp add em-x --transport http https://emplusx.com/api/mcp
```

Works with any MCP client that supports Streamable HTTP + OAuth (Claude Code, Codex, Cursor, VS Code). Setup walkthroughs: [emplusx.com/connect](https://emplusx.com/connect)

## Configuration

```json
{
  "mcpServers": {
    "em-x": {
      "type": "http",
      "url": "https://emplusx.com/api/mcp"
    }
  }
}
```

First connect opens a browser for OAuth sign-in; credentials are reused for later sessions.

## Business Relevance

- **Founders and executives** get a zero-drafting path to steerco decks and exec briefs — describe the decision, approve the storyline, receive a board-ready document
- **Consultants and agencies** get a tier-1-style drafting team at $8/month, cloning client brand styles across projects
- **RevOps and FP&A teams** get QBR decks whose every page is argued, not titled by topic — with data gates that fail pages whose numbers don't hold up
- **Operators with template libraries** get true native output — the .pptx/.docx uses your slide masters, palette, and fonts, not an approximation

## Integration with CorpusIQ

EM+x pairs naturally with CorpusIQ's business-data connectors on the evidence side of the stack. The weak link in AI-generated decks is the data: an agent pulls live numbers through CorpusIQ (Stripe MRR, QuickBooks P&L, HubSpot pipeline, GA4 traffic, Shopify orders), then hands the evidence set to EM+x, whose quality gates check that every chart is backed by that data before the deck reaches you. CorpusIQ supplies the ground truth; EM+x supplies the argumentation and the native formatting. A concrete composition: a QBR agent reads Stripe revenue and churn via CorpusIQ, files the brief in EM+x with the decision it must drive, approves the storyline, and returns a template-native QBR deck with zero manual slide work.

## Limitations

- Brand new — listed on mcp.so Aug 12, 2026; no ecosystem track record yet
- Commercial hosted service; your documents and evidence pass through their cloud
- Free tier is tight (1 project, 5 revisions/month) — realistically a trial tier
- Built around consulting-deck workflows; not a general document or report generator
- OAuth only — no API-key or self-hosted option

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
