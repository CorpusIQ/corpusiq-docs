---
title: "Klarefi MCP - Applicant Intake Where a Person Decides"
description: "AI intake for lending, insurance and legal teams: 21 tools that read applicant files, cite every fact and leave the decision with a person."
category: "Finance and Compliance"
stars: "0 (jmqcooper-ai/klarefi-mcp, ISC licence; registry record com.klarefi/mcp 0.4.0, npm @klarefi/mcp 0.4.0)"
added: 2026-11-28
source: "chatmcp/mcpso submission #8316 on 2026-11-28 at 17:52:31Z, server.json at www.klarefi.com/.well-known/mcp/server.json, and a keyless session against https://www.klarefi.com/mcp: initialize 200 as klarefi-mcp 0.4.0, a 21-tool tools/list, resources/list naming one MCP App, a keyless resources/read of 2,115 bytes, and five tools/call attempts"
relevance: "★★★"
tags: [intake, lending, insurance, legal, case-file, citations, human-in-the-loop, mcp-app, workflow, remote-mcp]
last_updated: "2026-11-28"
---

# Klarefi MCP

**Every intake process in lending, insurance and law runs on the same broken loop: a document arrives, nobody notices what is missing until someone opens it hours or days later, the missing item is chased by email, and the eventual case file mixes what the applicant said, what a document proved and what someone assumed. Klarefi answers that loop with an agent that reads each document as it lands, asks for the gap while the applicant is still in the conversation, and attaches every fact to the page and line it came from. What it deliberately will not do is decide: the review tools can record a human decision but cannot complete or reopen a case. It is the first intake-origination surface on this shelf, and it was read directly rather than summarised from its filing.**

```
Server type:  Remote (Streamable HTTP, stateless - no Mcp-Session-Id)
Endpoint:     https://www.klarefi.com/mcp
Registry:     com.klarefi/mcp 0.4.0 (npm @klarefi/mcp, stdio package beside the remote)
Auth:         customer plane needs an API key; applicant plane needs a signed intake link
Tools:        21 - 9 read-only, 12 that write or stage a change
App:          1 MCP Apps resource, ui://klarefi/case-review
Licence:      ISC
```

`initialize` answered **200** with no credential, naming itself `klarefi-mcp`, titled **Klarefi 0.4.0**, capable of `tools` and `resources` with `listChanged` on both, and its own description states the boundary that defines the product: *"it reads files, asks for missing items, cites every fact. A person decides."*

## What does an applicant agent actually do, and where does it stop?

The 21 tools split across two planes, and the split is the design worth copying.

**Applicant plane, nine tools, no API key.** `open_intake` opens a session from a signed link, `get_intake_state` returns the distilled state with a typed `next_action` of `consent`, `fill_form`, `answer`, `upload`, `wait` or `none`, then `answer_question`, `answer_fields`, `upload_document`, `save_intake_draft`, `give_intake_consent` and `submit_intake` move it forward. `wait_for_next_action` polls until the session leaves processing.

**Customer plane, twelve tools, API key with per-tool scopes.** `list_workflows` needs `workflows:read`; `get_case`, `get_case_workspace`, `get_case_package` and `get_review_command` need `cases:read`; `list_operator_queue` and `submit_case_review` need `cases:review`; `create_intake_session` needs `intake:sessions:create`; the three connector tools need `connectors:write`. The vendor documentation names the scope beside each tool, which is more than most of this shelf does.

The credential model is the unusual part. The signed intake link *is* the credential, scoped to one session: anyone holding it can act on that session until it expires or is revoked, which is why the docs describe it as scoped applicant access rather than as a secret. And because the hosted server keeps **no protocol session**, every applicant tool call must carry the signed `url` or `session_id` with `access_token`. Local stdio clients call `open_intake` once and reuse it; remote clients cannot.

## The consent gate comes first

When the organisation requires consent, nothing is accepted before it. The manifest carries `consent.pending` and, while pending, `consent.notice` - the sentence the applicant agrees to, with the lawful basis, retention and privacy notice. `give_intake_consent` records it, and the event records that **an agent** gave it **and which client** it came from. Repeating the call changes nothing. Until consent is recorded the manifest marks the draft and upload tools unavailable, so a reviewing agent cannot start collecting ahead of the paperwork.

That is a small piece of engineering with a large compliance consequence: the audit trail distinguishes a person who agreed on the hosted page from an assistant that agreed on their behalf, and names the assistant.

## Where a person decides, in the tools themselves

Four boundaries are enforced in code rather than described in a policy page:

- **A review command cannot complete or reopen a case.** `submit_case_review` accepts commands that review or correct facts, update evidence, escalate, or record a case-wide `checks_go` with `go`, `not_now` or `withdraw` plus a rationale. There is no approve-the-loan tool, so the final decision stays outside the agent's reach.
- **A workflow cannot be published by an agent.** `save_workflow_draft` validates and saves a versioned Form, Fact and Verify declaration, and cannot publish or activate it. To change a published version 1.0.0 the agent must save a `1.0.0-draft`, which keeps the live workflow in force while the change waits.
- **A connector can be staged rather than activated.** `create_connector`, `create_connector_from_openapi` and `delete_connector` report whether the configuration is active or staged for operator approval, verified against a live check on this pass for the delete path.
- **A case file leaves as evidence, not as data.** `get_case_package` returns the `case_package.v1` artifact - the facts, the calculated facts, the offer or decline - plus a signed read-only link to the case file, so what a reviewer receives can be opened but not edited.

## What a case workspace contains

`get_case_workspace` is the operator view and does not mutate the case: facts with their cited evidence, blockers, ownership and a timeline. On the vendor's own worked example a turnover fact carries the source page and line - *Annual accounts 2025.pdf, p.4* - the extracted value **2,184,300** and the reasoning line that produced it. The product page states the failure mode it is built against: when a fact cannot be found in the documents, the field is marked **missing** rather than guessed. For an operator whose reviewers are accountable for what they sign, missing-marked beats confident-and-wrong.

## The MCP App, read keylessly

`resources/list` returns one resource: `ui://klarefi/case-review`, `text/html;profile=mcp-app`, described as a read-only cited case workspace rendered inside an MCP host. A keyless `resources/read` returned the whole template, **2,115 bytes**, with `_meta.ui.prefersBorder: true` and a content-security block that declares **no** connect or resource domains - the app loads nothing from anywhere.

The template renders what the review workflow needs and nothing else: the case id, a `why_here` line, a three-column fact grid of label, value and status pill, and a blockers list, with every value escaped through a single `esc()` helper. It listens for a `message` event and lifts `structuredContent` from whichever of three shapes the host sends. For anyone building an MCP App against a business workflow, this is a compact and honest reference: one screen, no network, no state.

## Three defects, all reproducible keylessly

1. **Authentication failures are in band.** Every customer-plane tool answers HTTP **200** with `isError: true` and one identical sentence - *"Customer-plane tools require Authorization: Bearer \*\*\*"* - whether the caller is missing the header or holding a key without the scope. A client that checks only the MCP result transport sees a successful call; a client that reads `isError` still cannot tell which of the twelve tools' scopes was missing, even though the documentation assigns one per tool.
2. **Argument validation runs before authentication.** `create_intake_session` with no arguments answered "Provide exactly one of workflow_id or case_type_id" with no credential at all, while the same call with an argument answered the auth refusal. That order is defensible - a schema error is not a secret - but it means an unauthenticated caller can probe the argument contract of every customer tool.
3. **The version negotiation and the app listener are both one-way.** A client asking for protocol **2025-06-18** was answered **2025-11-25**: legal per the specification, but a client that pins the version it requested may refuse the connection. The app, in turn, renders only on a `message` event and never requests the tool output itself, so a host that delivers `structuredContent` by another path, or that renders before the listener attaches, shows the placeholder card instead of the case.

## Where it belongs

Nothing else on this shelf does intake. `allclear-lending-mcp` finds lenders for a business; `easydocforms-mcp` collects blank healthcare forms with PHI kept out of agent context; the document-conversion entries turn files into text. Klarefi sits one step earlier than all of them and one step later than a form: it runs the conversation that produces a complete, cited file and hands it to a reviewer who must still decide.

Two honest limits. It is **not** a decisioning engine, and the tool surface proves it rather than claiming it - no approval tool exists. And a customer-plane evaluation needs an API key; this entry was read at the applicant-plane boundary, so the scoped behaviour of the twelve customer tools is documented from the vendor contract rather than driven.

```json
{
  "mcpServers": {
    "klarefi": {
      "type": "http",
      "url": "https://www.klarefi.com/mcp",
      "headers": {
        "Authorization": "Bearer ${KLAREFI_API_KEY}"
      }
    }
  }
}
```

## Also worth knowing

### How big is the file a hosted client can send?

Inline content on the hosted endpoint is capped at **5 MB** decoded; a local stdio client can upload a file of up to **25 MB**. That asymmetry is the one to plan around: a hosted intake assistant handles statements and identity documents, and a 20 MB scanned pack belongs on the stdio package or on the hosted page the applicant opens in a browser.

The repository is young and small - created 2026-08-10, last pushed 2026-11-27, zero stars at the time of reading - so the reference is the vendor's documentation and the live surface, not a community track record. The docs are also candid about their own gaps, marking the Cursor configuration and the Claude web custom connector as **yet to be tested** with Klarefi's remote server, which is a rarer honesty than a green checkmark.
