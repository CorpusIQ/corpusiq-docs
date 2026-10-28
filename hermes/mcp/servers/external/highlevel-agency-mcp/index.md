---
title: "HighLevel Agency MCP - Guarded GoHighLevel Sub-Account Ops"
description: "Thirteen guarded tools for HighLevel agencies: snapshot diffs, domain SSL onboarding, workflow builds and read-only audits."
category: Agency Operations / Marketing Automation
stars: ★★★ (keyless public listing, 13 tools live-probed)
added: 2026-10-28
source: "live probe of https://ghlagencymcp.com/mcp returning HTTP 200 keyless on initialize with serverInfo highlevel-agency-mcp 1.0.0 and a full tools/list of 13 tools, plus the mcpservers.org listing at mcpservers.org/servers/mooshee/highlevel-agency-mcp whose card advertises 481 tools across 39 families"
relevance: ★★★
tags: [gohighlevel, highlevel, agency, sub-accounts, snapshots, funnels, workflows, ivr, governance, mcp]
last_updated: "2026-10-28"
---

# HighLevel Agency MCP

**An agency with forty client sub-accounts has forty chances to ship a wrong setting to the wrong client, and the one that does is the one nobody diffed first.**

```
Server type: Remote (Streamable HTTP), keyless initialize
Endpoint:    https://ghlagencymcp.com/mcp
Auth:        Private Integration Token per agency context
Tools:       13 at tools/list
Policy:      Safe-Writes presets: read-only, dry-run-first, standard
Site:        ghlagencymcp.com
```

## Why This Matters for Operators

A GoHighLevel agency runs its clients inside one platform, and the danger is not that the platform lacks features. It is that every sub-account is configured by hand, from a template, at speed. Custom values drift, merge tags break silently in SMS templates, phone numbers get reassigned and keep billing, and staff roles accumulate permissions nobody intended.

What makes this server worth cataloguing is not its size. It is that it is built around the audit and the diff rather than the write. The tool list is dominated by things that read a sub-account and tell you what is wrong with it.

## What It Returns, Verified

The endpoint is live and open: a bare `POST initialize` on `https://ghlagencymcp.com/mcp` returned **HTTP 200** with `serverInfo` name `highlevel-agency-mcp`, title `HighLevel Agency & Builder MCP`, version `1.0.0`, on protocol `2025-06-18`, declaring tools, prompts and resources. A full `tools/list` returned **13 tools**:

- `ghl_agency_connection_health`, `ghl_agency_doctor`, `ghl_agency_contexts`, `ghl_agency_locations` for connection and context readiness
- `ghl_agency_tools_enable` sets the Safe-Writes Policy preset for the session: read-only, dry-run-first or standard
- `ghl_snapshot_diff_audit` compares a live client sub-account against a reference Master Snapshot **without overwriting assets**
- `ghl_site_builder_sync` syncs a funnel step layout while preserving 2-step carts and 1-click upsells
- `ghl_domain_ssl_onboard` plans, verifies and attaches custom funnel domains and branded short-link CNAME, A and TXT records with SSL checks
- `ghl_workflow_ivr_builder` builds and publishes workflows, LeadShield form spam guards and call-screening IVRs
- `ghl_custom_values_audit` reads Custom Values and SMS/email templates for broken merge tags and missing placeholders
- `ghl_phone_wallet_audit` reads LC Phone numbers, number pools, forwarding loops and unassigned monthly wallet drain
- `ghl_user_role_governance` audits staff permissions against least-privilege presets for va-support, sales-rep, client-admin and agency-admin
- `ghl_agency_tools_search` finds automation blueprint presets by keyword or category

## Correction Worth Recording

The directory card advertises **481 tools across 39 domain families**. The live endpoint serves **thirteen**. That is not a fault in the server, it is the server being clearer than its own listing: what is exposed is a curated, policy-gated set aimed at agency operations rather than a raw API proxy, and the exposed set is arguably the more useful half. The count is recorded here as measured, not as advertised, because a catalogue that repeats a card's number without probing it is a catalogue that can be wrong for months.

## Limits Worth Recording

The Safe-Writes Policy is the load-bearing control and it defaults mattering: `dry-run-first` is the preset to start on, because `standard` writes. A Private Integration Token is per agency context, so one token across several clients erases the per-client separation that makes the audit meaningful. **Real Wave GHL MCP** in this catalogue covers the workflow-building slice specifically, so the two overlap on that one tool and differ everywhere else.

## FAQ

### Does it really expose 481 tools?
No. The listing card says 481 across 39 families, the live `tools/list` returns 13. The 13 are curated agency operations tools with a policy gate rather than a full API surface.

### What does the Safe-Writes Policy do?
It sets the session behaviour to read-only, dry-run-first or standard through `ghl_agency_tools_enable`. Start on dry-run-first and read the planned change before allowing a write.

### What can it audit without changing anything?
Snapshot drift against a Master Snapshot, Custom Values and template merge tags, LC Phone numbers and forwarding loops, and staff roles against least-privilege presets.

### Does it need a key to connect?
The `initialize` handshake is keyless and lists the tools, but real work needs a Private Integration Token and CRM session per agency context, which `ghl_agency_doctor` verifies.
