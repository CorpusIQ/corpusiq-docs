---
title: ZplFlow MCP - Thermal Label Streams for Agents
description: "Hosted MCP for ZPL and PDF shipping-label conversion, 10 tools over async jobs and ZPL pipelines, API key auth, token pricing."
category: Logistics and Supply Chain
stars: n/a (commercial hosted service, API key, free tier 6,000 tokens)
added: "2026-11-06"
source: "The mcpservers.org /all newest page slug zplflow-mcp, its detail card, and the vendor's own documentation at zplflow.io/docs/mcp, /docs/conversions, /docs/jobs, /docs/pipelines, /docs/authentication, plus the pricing and feature pages; and a keyless initialize probe of https://mcp.zplflow.io/v1/mcp (301 to /v1/mcp/, which answers 401 UNAUTHORIZED)"
relevance: ★★★
tags: [logistics, shipping, labels, zebra, zpl, pdf, warehouse, api-key, remote-mcp, streamable-http]
last_updated: "2026-11-06"
---

# ZplFlow MCP

**The label is where an order stops being a decision and becomes a physical object, and it is the one step an assistant could never touch.** A fulfilment decision is easy to describe in a chat: consolidate these three orders, split this shipment, reprint this one with a GS1-128 barcode. The printer does not take instructions in English, the ERP that produces the label stream is older than the person operating it, and the format the printer accepts is a command language. ZplFlow sits in that gap. It converts PDF labels to ZPL and back, applies programmable transformations before the label reaches the printer, and runs the high-volume conversions asynchronously. The MCP server is the first surface on this catalog that speaks to label infrastructure rather than to the business system behind it.

```
Server type:  Remote, Streamable HTTP, stateless mode
Endpoint:     https://mcp.zplflow.io/v1/mcp/
Auth:         API key, Authorization: Bearer <key>; no OAuth, no dynamic client
              registration, every request must carry the key
Tools:        10 (account balance, job lifecycle, cost estimate, pipelines)
Plans:        Free with 6,000 tokens and no card plus a 30-day full platform
              trial; Lite EUR 9 (15,000), Starter EUR 39 (60,000), Growth
              EUR 149 (240,000), Scale EUR 399 (900,000), Enterprise EUR 800
              (3,000,000); overage billed per 1,000 tokens
Pricing unit: 1 standard label = 1 token. ZPL to PDF is 1 token per page.
              PDF to ZPL is 3 tokens at 203 DPI and 4 at 300 DPI, flat
              regardless of the output size budget
Category:     Logistics and Supply Chain
Built by:     MTech S.r.l. (Italy), hosted on European infrastructure
First call:   getAccountBalance, which returns available and reserved tokens
```

**Evidence tier: documented, not driven.** There is no ZplFlow account on this machine, so no conversion was measured. What was verified is the endpoint itself and the vendor's machine-facing contract. A keyless `initialize` against `https://mcp.zplflow.io/v1/mcp` is answered with an **HTTP 301** to `/v1/mcp/`, and that path returns **HTTP 401** with `{"error_code":"UNAUTHORIZED","message":"missing authorization header"}`. Both the redirect and the 401 carry the same site security headers, so the route is served by the vendor's own stack rather than by a generic edge, and a client that follows redirects, as MCP clients do, lands on a keyed surface and stops. Unlike the OAuth servers this catalog usually covers, there is no `WWW-Authenticate` header and no protected-resource document to read, because the credential is a static key rather than a browser sign-in. Re-probed 2026-11-06 19:01Z. Tool names, scopes, limits and prices below come from the vendor's documentation at `zplflow.io/docs`, written for integrators rather than for buyers.

## What a connected assistant can do

| Tool | Scope | What it does |
| --- | --- | --- |
| `getAccountBalance` | `account:read` | Available tokens and tokens reserved by jobs still in flight |
| `estimateCost` | `convert:estimate` | Exact token cost of a conversion before it runs |
| `getStorageUploadURL` | `jobs:create` | Presigned upload URL for the file to convert |
| `submitConversion` | `jobs:create` | Creates the job: `pdf_to_zpl`, `zpl_to_pdf` or `pipeline_run` |
| `startJob` | `jobs:write` | Starts processing an uploaded job |
| `getJob` | `jobs:read` | Status and presigned result URLs for one job |
| `listJobs` | `jobs:read` | Recent conversions for the account, with a limit |
| `cancelJob` | `jobs:write` | Cancels a queued job and releases its reserved tokens |
| `listPipelines` | `pipelines:read` | Pre-configured and custom ZPL transformation recipes |
| `getPipeline` | `pipelines:read` | The step configuration of one pipeline |

The operational shape is a job, not a function call. The assistant asks for an upload URL, puts the PDF or ZPL file there, submits the conversion, starts it, and polls until it can hand back the result link. That is the correct shape for a print run and the wrong shape for a single label, and the vendor knows it: the synchronous conversion endpoints exist in the REST API (`POST /v1/convert/pdf-to-zpl` and `/v1/convert/zpl-to-pdf`, idempotent, 5 MB body, sub-200ms) but the MCP tool table marks them as not exposed publicly, so the connector's conversions all travel through the asynchronous engine.

**What the connector deliberately does not expose is the write half of pipelines.** `listPipelines` and `getPipeline` are MCP tools; creating a pipeline, editing one, applying one and previewing one are REST routes with `pipelines:write` and `pipelines:apply` scopes and are marked "no" in the vendor's public-MCP-tool column. An agent can therefore see the label recipes and read their steps, and cannot rewrite them from a chat. For a shared label pipeline that multiple systems on the line depend on, that is the right boundary.

**Pipelines are where the label logic actually lives.** The engine carries 24 programmable transformers: `add_text`, `add_barcode`, `add_qrcode`, `add_datamatrix`, `add_box`, `add_line`, `replace_text`, `replace_barcode_value`, `remove_graphics`, `regex_replace`, `add_timestamp`, `format_date`, plus the geometric set covering rotate, scale and crop. That is the layer that makes a PDF from an accounting system acceptable to a Zebra printer, and the layer that injects GS1-128 compliance into a barcode an ERP generated without it. The preview route (`POST /v1/pipelines/preview`) spends no tokens and returns a PNG of the rendered output, which is the cheapest way to test a transformation before it reaches a production line.

## Why this matters for operators

Fulfilment breaks at the edges, and the edge is the label. A warehouse manager's real month-end problem is not picking a carrier, it is that 5,000 labels produced by a system nobody wants to touch print at the wrong size, or carry a barcode the scanner rejects, or are in a format the printer on the floor does not accept. Every catalog entry beside this one stops one step short of that: LoadOptimizer decides what fits in the truck, PackIndex prices the packaging, Container Tracking follows the box, ProShip creates shipments and prints PDF labels for one regional carrier set. None of them touches the label stream itself.

The vendor's commercial promise is the one that matters in a shipping week: **dynamic over-budget scaling**, where exceeding the monthly token allowance does not stop the line, it bills overage per 1,000 tokens at a slightly higher rate. Read it as an operational guarantee with a bill attached rather than as a free feature. An operator wiring an agent to a month-end print run wants to know both halves of that sentence, because the failure mode of the alternative is a halted fulfilment line at the worst hour of the quarter.

Start with `estimateCost` and a free pipeline preview. That pair answers the two questions a business owner asks before authorising anything: what will this cost, and will the label come out right.

## The cost model, in plain numbers

One standard label is one token. ZPL to PDF is 1 token per page. PDF to ZPL is flat per page regardless of the output quality budget: 3 tokens at 203 DPI, 4 tokens at 300 DPI. The free tier of 6,000 tokens is roughly 6,000 labels a month for ZPL to PDF, or 1,500 to 2,000 labels for a PDF to ZPL run at 300 DPI. Lite at EUR 9 carries 15,000 tokens with EUR 3.00 per 1,000 overage, Starter at EUR 39 carries 60,000 at EUR 2.50, Growth at EUR 149 carries 240,000 at EUR 1.50, Scale at EUR 399 carries 900,000 at EUR 1.00, and Enterprise at EUR 800 carries 3,000,000. Annual billing is two months free. The sign-up is free, needs no card, and the 30-day trial includes the Pipelines and Async features rather than gating them.

## Where it stops, and the details that bite

- **The key is the whole security model.** No OAuth, no scopes negotiated at sign-in, no browser consent: a Bearer key pasted into a connector config. That makes key hygiene the control that matters. The vendor's scope model is real and enforced per key (`account:read`, `jobs:read`, `jobs:write`, `jobs:create`, `convert:estimate`, `pipelines:read`, and the REST-only write scopes), with a deny-by-default mode where a locked key returns `403 INSUFFICIENT_SCOPE` plus the exact scope it needed. Issue a key per client, not one shared key for the floor.
- **Upload URLs expire in 15 minutes and results in 1 hour.** An assistant that creates a job and then goes quiet for a coffee has to start over. Anything that pieces jobs together across a long workflow needs its own storage in front of this.
- **Async job data is removed eight hours after submission, configurable to zero.** The vendor states the service is stateless, European-hosted and that the audit log is retained for 365 days. Those are the vendor's claims about its own service and are recorded here as such, not as measurements.
- **Five megabytes per synchronous request**, 203 or 300 DPI only, and an `Idempotency-Key` header is required on job creation and conversion, so a retried call does not double-charge.
- **Zebra and ZPL-compatible printers.** ZPL output targets Zebra thermal printers and anything that speaks ZPL. A non-ZPL printer, or a label format that depends on a proprietary driver, is outside the surface.
- **This is infrastructure, not data.** The connector reads no business records. It cannot tell you what is in an order, only turn the document your system produced into the format the printer accepts. Pair it with a business connector; do not read it as one.

## Connecting it

```
Endpoint:  https://mcp.zplflow.io/v1/mcp/
Header:    Authorization: Bearer <your API key>
Transport: Streamable HTTP
```

```json
{
  "mcpServers": {
    "zplflow": {
      "type": "remote",
      "url": "https://mcp.zplflow.io/v1/mcp/",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

The vendor documents a one-line CLI path as well, `npx add-mcp 'https://mcp.zplflow.io'`, which writes the entry into Claude Code, Codex and Cursor configurations. Its own verification step is the one to copy: call `tools/list` over a JSON-RPC POST with the key in the header, and a correct key returns the full catalog of ten tools. Then call `getAccountBalance` and confirm the balance matches the dashboard before trusting anything downstream. The errors worth translating for an operator are `UNAUTHORIZED` for a missing or revoked key, `APIKEY_EXPIRED` when a key carried an expiry, and `INSUFFICIENT_SCOPE`, which names the missing scope in the response body and is a permissions problem rather than a broken connector.

## Related in this catalog

- [ProShip MCP](/hermes/mcp/servers/external/proship-mcp/) - the closest neighbour: creates Thailand Post shipments and prints PDF labels inside one order-management platform. That is a shipping system with a label output; ZplFlow is the label layer without the shipping system.
- [LoadOptimizer MCP](/hermes/mcp/servers/external/loadoptimizer-mcp/) - what fits, in what order, and what is left over, planned before anything is labelled.
- [PackIndex MCP](/hermes/mcp/servers/external/packindex-mcp/) - packaging costs per order, the number that decides which label gets printed.
- [Container Tracking](/hermes/mcp/servers/external/) and HaulierScope - where the box goes after the label is on it.
