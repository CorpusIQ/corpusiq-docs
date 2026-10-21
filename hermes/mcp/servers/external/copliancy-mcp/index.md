---
title: "Copliancy MCP - Licenses, Leases and Incidents per Site"
description: "Seven Copliancy MCP servers put multi-location licenses, leases, incidents, credentials and maintenance in front of an agent, scoped by role and location."
category: Operations
stars: n/a (commercial SaaS, free sign-up)
added: 2026-10-20
source: "mcp.so /feed page 1 (seven Copliancy Inc cards posted 2026-10-21T03:00Z) + vendor provider documentation and live OAuth metadata probes"
relevance: ★★★
tags: [operations, multi-location, compliance, lease-accounting, asc-842, incidents, claims, cmms, workforce-scheduling, remote-mcp, oauth, scopes, mcp-apps]
---

# Copliancy MCP Suite

**One vendor, seven operational systems, and a design that assumes the person asking is a store manager who should not see the other 400 stores.**

```
Vendor: Copliancy Inc (copliancy.com), US multi-location compliance and record platform
Servers: 7 remote Streamable HTTP endpoints, one per product
Auth: OAuth with dynamic client registration, tenant administrator must enable MCP and API access first
Scope model: domain-named read and write scopes, plus the user's own role and location limits enforced on every call
Write model: write scopes are opt-in and every modifying tool produces a saved preview a person approves inside the product
Live check: all seven endpoints answered a POST initialize probe in this sweep (401 or 403, never a 200 without credentials)
Tool surface: not published as a list; the scope sets below are what each server declares
Price: free sign-up at app.copliancy.com/sign-up, tier pricing not published in text
```

## Why This Matters for Operators

A single-location business keeps its records in the owner's head. A fifty-location business cannot. Licenses expire in forty jurisdictions, a lease renews in a strip mall nobody visits, an employee's food handler card lapses on a shift they are already working, a slip-and-fall becomes a claim with a reserve attached, and the walk-in cooler has a compressor that fails every August.

None of that is hard analysis. It is the arithmetic of many locations against a calendar, and it fails because the records live in seven tools and a filing cabinet. The person who gets hurt by the failure is never the person holding the record.

That is the specific thing this suite does that a general-purpose agent does not: it knows which location a record belongs to, and it refuses to answer past the boundary of the person asking. An agent with that boundary can be given to a store manager. An agent without it cannot.

## The Seven Servers

| Server | Endpoint (probed this sweep) | What it holds | Scopes declared |
|---|---|---|---|
| IncidentVault | `https://app.incidentvault.com/api/mcp/apps/server` | Incidents, claims, reserves, settlements, legal spend, risk checks, regulatory inspections, tasks | 38 scopes: 19 read and 19 write (`read:incidents`, `write:claims`, `read:reserve_adjustments`, `read:regulatory_inspections`, `write:settlements`) plus `offline_access` |
| PolicyTrak | `https://app.policytrak.com/api/mcp` | Sites, compliance fields, policies, SOPs, evidence files, roles, members, laws, imports, research | 57 scopes across `company`, `members`, `roles`, `locations`, `fields`, `tabs`, `policies`, `sops`, `employees`, `requests`, `tasks`, `books`, `files`, `laws`, `workflows`, `acknowledgements`, `analytics`, `audit`, `state_guide` |
| RetailHardHat | `https://app.retailhardhat.com/api/mcp` | Sites, deals, projects, budgets, vendors, permits, bids, RFIs, RFPs, invoices, change requests, purchase lists, documents, field operations | 20 `mcp:*` scopes (`sites`, `deals`, `budgets`, `permits`, `rfis`, `change_requests`, `field_operations`, and so on) |
| CredentialCamp | `https://app.credentialcamp.com/api/mcp` | Employee credentials, certifications, training records, catalog, compliance gaps | 5 scopes: `mcp:self`, `mcp:catalog`, `mcp:compliance`, `mcp:draft`, `mcp:business` |
| QuipAssist | `https://app.quipassist.com/api/mcp` | Equipment, work orders, preventive maintenance, repairs, parts, vendors, IoT readings, sensitive documents | 13 scopes: `equipment`, `repairs`, `maintenance`, `parts`, `vendors`, `iot`, `documents`, `documents:sensitive`, `reports`, `data:export` |
| LeaseCommand | `https://app.leasecommand.com/api/mcp` | Sites, leases, rent schedules, critical dates, ASC 842 amortization and journal entries | Declared by the product, not published as protected-resource metadata |
| SmartShifts | `https://app.smartshifts.com/api/mcp/apps/server` | Shifts, coverage, time off, tasks | Declared by the product, not published as protected-resource metadata |

Two of the seven answer discovery probes differently from the rest, and that is worth knowing before an integration is scheduled. `/.well-known/oauth-protected-resource` on SmartShifts returns a 404 `NOT_FOUND`, and LeaseCommand serves its single-page application HTML on that path, so neither advertises its resource metadata the way the other five do. Their MCP endpoints still answer an unauthenticated `initialize` with 401 `Unauthorized`, so the connection exists; discovery is what is missing.

## What It Actually Does

The products are separate systems that a multi-location operator would otherwise buy separately:

- **Compliance evidence.** PolicyTrak holds what an inspector asks for: which SOP, which signed acknowledgement, which evidence file, at which site, current or expired. CredentialCamp covers the employee side, the certifications and mandated training that lapse quietly.
- **Claims and incidents.** IncidentVault runs incident intake, claims, tasks, risk checks and regulatory inspections with reserves and settlements attached, which is the part of operations that costs the most and gets tracked the least.
- **Development and construction.** RetailHardHat tracks a new site from due diligence through permits, bids, project budgets, change requests and invoices to opening day.
- **Lease accounting.** LeaseCommand carries rent schedules, critical dates and ASC 842 amortization with journal entries, which is the record a finance team needs and an operator never has in a queryable form.
- **Equipment.** QuipAssist is the maintenance layer: assets, work orders, preventive schedules, parts and vendors, with IoT readings available read-only.
- **Scheduling.** SmartShifts covers shifts, coverage, time off and tasks. Paid time off and open shifts are the two facts that decide whether a location opens on time.

The design detail that matters more than the feature list is that each server declares the user's limits as scopes and enforces role, location and record restrictions on every call, rather than scoping at connection time. An agent connected by a regional manager cannot enumerate another region, because the check happens per call, not per session.

## The Redaction Model

IncidentVault publishes two endpoints, and the difference is the reason this is safe to hand to a manager.

The operational endpoint (`/api/mcp/apps/server`) returns opaque record IDs, allowlisted status and priority, dates, location IDs and audit percentages. Names, narratives, medical details, custom fields, attachments, arbitrary fields, financial transfers and administrative or security tools are excluded. Source links open the protected record inside IncidentVault for the sensitive detail.

The private endpoint (`/api/mcp/server`) keeps the full authorized catalog, including the sensitive records, and the vendor's own guidance is to grant only the permissions needed and review the connection's data-sharing controls.

In a hosted MCP App host such as ChatGPT or Claude, IncidentVault renders a working dashboard with filters, paging, record review and follow-up creation. Other hosts receive structured facts and citation links as text. The vendor states explicitly that Gemini widget support is not assumed. GitHub Copilot connects with a dedicated API key rather than OAuth.

## What It Cannot Do

Writes are staged, not executed. Every modifying tool creates a saved preview that a person approves inside the product, and the documentation is explicit that pending or approved is not executed success. An agent that reports "the incident is filed" from a preview response is lying, so a workflow needs to read the state back rather than trust the acknowledgement.

IncidentVault's OAuth tokens last at most one hour, with rotating refresh tokens at 30 days and grants at 90 days, so a connection left unused for a quarter needs re-consent. Revocation stops future access but does not retract what was already shared.

The catalogue is not complete from the MCP side. The operational endpoint counts describe loaded pages, not the whole tenant, so pagination is required before any total is quoted. Renewal obligations with issuing authorities still live in the Copliancy core product rather than a listed MCP endpoint, so license renewal work is not fully covered by these seven servers.

Pricing is not published in a form that can be quoted. Free sign-up exists; the plan comparison is an image table with no numbers in text.

## FAQ

### Is this one server or seven?

Seven, with separate hosts, separate OAuth authorization servers in most cases and separate scope vocabularies. They share a vendor, a data model built around locations, and an approval convention for writes. In practice that means seven connector entries in a client, not one, and a tenant administrator enabling MCP access per product.

### Does it work for a business with two locations, or only for chains?

It works, but the value curve is steep in the middle. Two locations can be run from a spreadsheet. The cost of a missed license or a lapsed certification is the same regardless of size, so the first location that gets cited makes the case for the cheaper plans.

### What does an agent actually answer that the dashboards do not?

The cross-record questions. Which locations have an expired certification and an open claim in the same quarter. What the rent schedule looks like two renewals out. Which preventive maintenance is overdue on equipment past warranty. Each dashboard answers its own question; only an agent reads across them.

### What happens to sensitive data in a connected chat client?

It leaves the product and enters whichever model provider is behind the client, under that provider's terms. IncidentVault narrows what leaves by default on its operational endpoint, but the connection is a pass-through of the user's own permissions on the private endpoint, and no vendor can un-share a record already read into a conversation.

## See Also

- [A4B CMMS MCP - Assets and Maintenance](/hermes/mcp/servers/external/a4b-cmms-mcp)
- [ZenSched MCP - Field Workforce Scheduling](/hermes/mcp/servers/external/zensched-mcp)
- [STEADYWRK Dispatch MCP - Field Service Operations](/hermes/mcp/servers/external/steadywrk-dispatch-mcp)
- [fynk MCP - Contract Lifecycle Management](/hermes/mcp/servers/external/fynk-mcp)
- [Accountable MCP - AI Bookkeeping](/hermes/mcp/servers/external/accountable-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
