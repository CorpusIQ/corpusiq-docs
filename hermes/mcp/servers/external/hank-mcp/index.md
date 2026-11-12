---
title: "Hank MCP - Who Is On Call, Answered From the Chat"
description: "AI receptionist for restoration and home services: 40 tools behind OAuth, routing changes as reviewable plans, and an audit log without values"
category: "Communication"
stars: "not applicable (hosted service)"
added: 2026-11-12
source: "the mcp.so feed card stamped 2026-11-12 17:21Z, the official registry record com.dialhank/hank 1.0.0, both OAuth metadata documents read the same day, the vendor's tool reference and permissions pages at docs.dialhank.com, and a live keyless probe of https://app.dialhank.com/api/mcp at 18:05Z"
relevance: ★★★
tags: [ai-receptionist, answering-service, call-routing, on-call, scheduling, restoration, home-services, oauth, mcp, remote]
last_updated: "2026-11-12"
---

# Hank MCP

**The routing decision that matters is made at 11:40 on a Saturday night, by nobody.** A restoration crew gets a burst-pipe call at 2am, the after-hours route points at a technician who took the weekend off, and the job goes to whoever answers next. The rules that decide this live in a settings page that one person in the company maintains and nobody else opens. Hank answers the phone for restoration and home-service companies; its MCP server puts the on-call calendar, the transfer routes, the office hours, the service-area ZIPs and the lead policy in front of an assistant, so the question *who is on call this weekend and who takes emergencies after hours* is answerable in a sentence and changeable in a sentence.

```text
Server type:  remote Streamable HTTP, OAuth 2.1 with dynamic client registration
Endpoint:     https://app.dialhank.com/api/mcp
Auth:         OAuth; two scopes, hank.settings.read and hank.settings.write
Registry:     com.dialhank/hank 1.0.0, remote declared as the same URL
Access:       role-bound - the assistant holds exactly your permissions
Probe:        keyless initialize answered 401 with protected-resource metadata;
              both metadata documents fetched and read
Tools:        40 documented in the vendor's tool reference (not measured this
              pass - the endpoint refuses every call without a connection)
```

## The evidence tier

A keyless `initialize` answered **401** with the header `WWW-Authenticate: Bearer resource_metadata="https://app.dialhank.com/.well-known/oauth-protected-resource/api/mcp", error="invalid_token"`, and the body was the same two fields. The metadata pointer is the part that separates a wall from a door: a client that follows it can register itself.

The protected-resource document answered **200** and named one resource, one authorization server at `https://app.dialhank.com`, **two** scopes - **`hank.settings.read`** and **`hank.settings.write`** - `header` as the bearer method, and `resource_name: Hank`. Two scopes for forty tools is a coarse grant by modern practice: a client that can read routing can also change it unless the server enforces the split per call, and the vendor's own tool reference labels each tool as reading or changing, so the enforcement is server-side rather than scope-side.

The authorization-server document answered on the RFC 8414 path with `authorization_endpoint` `/oauth/authorize`, `token_endpoint` `/api/mcp-oauth/token`, `registration_endpoint` `/api/mcp-oauth/register`, `revocation_endpoint` `/api/mcp-oauth/revoke`, `code` as the only response type, `authorization_code` and `refresh_token` as the grants, **`S256`** as the only PKCE method, and `none` as the only token and revocation auth method. So a client onboards with no pre-shared secret, and revocation is available to the client as well as to the operator.

`com.dialhank/hank` **1.0.0** answers in the official registry with the same remote and the description *manage call routing, on-call rotations and office hours for your AI receptionist*.

**The honest limit, stated rather than papered over:** no Hank account exists on this host, so nothing beyond the handshake was measured. The tool list below is the vendor's published reference, read on 2026-11-12, labelled as documentation rather than as an observation. The 401 is the measured part.

## What the forty tools cover

The reference groups them exactly the way the dashboard does, which is a good sign for whoever writes the prompts:

```text
Reviewing and planning   explain_call_routing, plan_routing_change, apply_routing_change
Calls                    search_calls, get_call_details
Identity and scope       whoami, list_organizations, list_locations
Routing config           get_call_routing, set_routing_assignment, update_call_routing_options,
                         upsert_routing_contact, remove_routing_contact,
                         upsert_routing_employee, remove_routing_employee,
                         upsert_department, remove_department, upsert_tpa, remove_tpa,
                         upsert_transfer_route, remove_transfer_route
On-call                  get_on_call, create_on_call_schedule, assign_on_call_schedule,
                         set_on_call_rotation, manage_on_call_rotation,
                         upsert_on_call_coverage, remove_on_call_coverage,
                         update_on_call_schedule, remove_on_call_schedule,
                         delete_on_call_schedule
Caller context           get_caller_information, update_caller_information
Office hours             get_office_hours, update_office_hours,
                         update_office_notification_email
Service area             get_service_area_zips, update_service_area_zips
Lead policy              get_lead_policy, update_lead_policy
```

Every tool accepts `environment` (`production`, `staging`, `local`), `orgId` and `locationId`, plus `settingsScope` on the settings that can differ per location and `confirm` on the tools that preview a change first. `search_calls` runs indexed full-text search across caller name, summary, intake, original and repaired transcripts and transfer screening, which is the tool that turns *find last week's calls that mention a burst pipe* into a record instead of a guess.

## The plan primitive is the interesting part

Most write-capable MCP servers expose the write and let the client behave. This one separates the decision from the execution:

- `plan_routing_change` prepares an **expiring, reviewable plan** for several route, schedule or office-hours operations at once, using the existing tool arguments rather than a new scheduling model. It never applies anything.
- `apply_routing_change` applies a reviewed plan **exactly once**, and **refuses expired, changed, differently scoped or unauthorized plans**. Existing settings changes invalidate pending plans. A repeated apply returns the recorded result instead of writing twice, and an interrupted execution is answered with *inspect the settings and create a fresh plan*, not with a retry.

The plan is bound to the user, app, organization, location and environment that created it. For an operator this is the difference between *the assistant changed the after-hours route* and *the assistant proposed the change, the router showed what every emergency number would reach afterwards, and someone said yes*.

## What it can and cannot do

From the vendor's permissions page, read the same day:

- **The assistant acts as you.** Its permissions are yours in each organization: Admin and Owner can read and change everything, an Operator can read everything and change routing, on-call and ZIP codes for their own locations, a Viewer reads everything and changes nothing.
- **Office hours and lead policy are Admin and Owner only**, whatever the scope in the token allows.
- **Removals preview first.** Removing a contact, employee, route, department, TPA, on-call schedule or coverage shows what will change before it changes, and the server refuses a change that would leave a gap - removing a contact a route still calls - and says what to change first.
- **Read-only connections exist.** At connect time the assistant can be granted read access only, and that holds whatever your role is.
- **Every action is recorded**: which tool, by whom, through which connection, and whether it succeeded - **what changed, never the values**, so phone numbers and names do not land in the log.
- **Disconnecting is immediate**, from Settings → Team → Connected apps, which also lists every app connected, when it was approved and when it was last used.
- **Call data travels with the connection.** `search_calls` and `get_call_details` are reachable from read-only connections without separate approval - transcripts, caller details, recording links, notes and linked appointments - limited to the locations you can access. That is the trade to decide at approval time, not after.

## Where it sits

[Upfirst MCP](/hermes/mcp/servers/external/upfirst-mcp/) is the closest neighbour: an answering service configured through MCP (greetings, knowledge, transfer rules, schedules) with transcripts audited in the chat. [Vocenya MCP](/hermes/mcp/servers/external/vocenya-mcp/) covers the same ground for small business calls, leads and bookings. [PlaceCall MCP](/hermes/mcp/servers/external/placecall-mcp/) makes outbound calls rather than answering them, and [PhoneScreen MCP](/hermes/mcp/servers/external/phonescreen-mcp/) applies the same voice stack to hiring. Hank is the first entry here where the **on-call rotation itself** is the object the assistant edits, with a plan-approve primitive in front of the write.

### Does connecting Hank let an assistant change call routing without asking?

It lets the assistant prepare the change. `plan_routing_change` returns a reviewable, expiring plan and `apply_routing_change` executes it once, refusing plans that expired or were scoped differently; a read-only connection cannot apply anything at all.

### Can an assistant read call transcripts?

Yes, through `search_calls` and `get_call_details`, including from a read-only connection. Access is limited to locations the signed-in user can reach, and recording links open through the operator's own signed-in session rather than as public audio URLs.

### What stops the assistant from breaking the routing?

The server refuses changes that would leave a gap - a contact a route still calls, for example - and previews removals before they happen. Office hours and lead policy are restricted to Admin and Owner roles, and the audit log records every action even though it never records the values.
