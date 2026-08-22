---
title: "Crisphive MCP - Field Service Dispatch and Scheduling"
description: "Field service dispatch and technician scheduling over MCP with 43 tools generated from the same OpenAPI spec as the REST SDKs. Preview/commit pairs on every mutation, idempotency keys, typed error codes and sub-3-second cascade rescheduling. OAuth 2.1 or API key."
category: Business Operations
stars: n/a (new listing)
added: 2026-08-22
source: "mcp.so GitHub issue #3690"
relevance: ★★★
tags: [field-service, dispatch, scheduling, hvac, crm, work-orders, remote-mcp]
---

# Crisphive MCP

**A hosted field-service dispatch and scheduling server with 43 tools generated from the same OpenAPI spec as the REST SDKs.** Crisphive gives an agent live access to customers, the service catalog, real scheduling availability, job booking, work orders, dispatch, CRM and fleet for a field-service business (HVAC, plumbing, electrical, home services). Every mutating flow is a preview/commit pair, so the agent shows its plan before it touches the schedule. The endpoint is live (HTTP 401 auth gate confirmed), stateless, and speaks Streamable HTTP with plain JSON responses.

```
Server type: Remote (Streamable HTTP, stateless - no SSE, no sessions)
Auth: OAuth 2.1 (DCR + PKCE) or API key (chsk_live_ / chsk_test_ sandbox keys)
Endpoint: https://api.crisphive.com/mcp
Registry: com.crisphive/mcp
Tools: 43 (customers, service catalog, availability, job booking, work orders, dispatch, CRM, fleet)
Pricing: Commercial (via Crisphive business dashboard); test keys hit an isolated sandbox
Built by: Crisphive (docs.crisphive.com); repo github.com/crisphive/crisphive-mcp
```

## Why This Matters for Operators

Field-service scheduling is the scheduling problem from hell: skills, service territories, live availability and an emergency that lands at 3 PM all have to reconcile in seconds. **Crisphive's deterministic scheduling engine does sub-3-second cascade rescheduling when an emergency lands**, and the LLM only sits at the intake and explanation edges - never inside the math. An operator gets a crew matched to the job on skills and location, a real booking window, and a quote without playing dispatch-phone-tag.

The safety model is the differentiator. Every mutating flow is a preview/commit pair, idempotency keys make retried calls safe, and errors are typed stable codes the agent can branch on. A test key (`chsk_test_...`) can only ever touch sandbox data, so you can let an agent experiment freely before it ever sees production.

## Tools & Capabilities

Tool names below are the operationIds from the public OpenAPI spec (api.crisphive.com/developers/openapi.json); the live tool list is served from the endpoint after auth.

| Area | Tools |
|---|---|
| Customers | `createCustomer`, `getCustomer`, `updateCustomer`, `deleteCustomer`, `listCustomers` |
| Technicians | `createTechnician`, `getTechnician`, `updateTechnician`, `deleteTechnician`, `listTechnicians`, `getTechnicianSchedule`, `listTechnicianSkills`, `replaceTechnicianSkills`, `replaceTechnicianLeads`, `replaceTechnicianBuddies`, `replaceTechnicianServiceAreas`, `replaceTechnicianVehicles`, `listNearbyTechnicians` |
| Skills & catalog | `listSkills`, `listSkillsByCategory`, `listSkillCategories`, `listJobTypes`, `getJobType`, `listServiceAreas`, `getServiceArea` |
| Scheduling & dispatch | `listMatchingSlots`, `listJobRequestBookingWindows`, `listCrewCandidates`, `listEmergencyCandidates`, `quoteJobRequest`, `createJobRequest`, `confirmJobRequest`, `updateJobPriority`, `getJobRequest`, `getJobRequestTimeline`, `listJobRequests`, `listJobRequestChanges`, `previewJobRequestMove`, `commitJobRequestMove`, `previewEmergencyReschedule`, `commitEmergencyReschedule` |
| Fleet | `listVehicles`, `getVehicle` |

## Installation

```bash
# OAuth - authorize in the browser on first connect
claude mcp add --transport http crisphive https://api.crisphive.com/mcp

# Or pass an API key to skip the browser step
claude mcp add --transport http crisphive https://api.crisphive.com/mcp \
  --header "Authorization: Bearer chsk_test_YOUR_KEY"
```

Per-client walkthroughs (Claude Code, Claude Desktop, Cursor, VS Code, ChatGPT, Gemini CLI) are published at docs.crisphive.com/mcp.

## Configuration

```json
{
  "mcpServers": {
    "crisphive": {
      "type": "http",
      "url": "https://api.crisphive.com/mcp"
    }
  }
}
```

Keys are created in the Crisphive business dashboard and carried as a bearer token. The key prefix decides the data plane: `chsk_live_` works production data, `chsk_test_` is isolated sandbox data. A full OAuth 2.1 flow (RFC 9728 resource discovery, RFC 8414 AS discovery, DCR, PKCE) is available for products where users bring their own Crisphive business, with scoped grants like `customers_view job_requests_view`.

## Business Relevance

- **HVAC, plumbing, electrical and home-services owners** let an agent book jobs, match crews and reschedule emergencies without a dispatcher in the loop
- **Dispatch managers** get skill- and territory-matched crew candidates with live availability instead of whiteboard guesswork
- **Operations teams** run quote-to-confirm workflows with idempotency and preview/commit safety on every write
- **Fleet supervisors** read vehicle assignments and technician schedules from one endpoint

## Integration with CorpusIQ

Crisphive owns the schedule; CorpusIQ owns the money and the books. A composed workflow books a job in Crisphive, then reads the invoice against Stripe and QuickBooks through CorpusIQ connectors to confirm payment landed before the next dispatch cycle. Field-service operators can also pair Crisphive's technician and job data with CorpusIQ's GA4 and HubSpot reads to tie service volume back to lead source - which marketing channel produced the jobs on the board, not just the clicks.

## Limitations

- Brand new listing (Aug 2026); repo created July 2026 with no stars yet
- Commercial platform - production data needs a Crisphive business account and keys
- Field-service vertical only (HVAC, plumbing, electrical, home services)
- No self-host option; hosted remote server
- 43 tools is a large surface - agents need scoped OAuth grants or sandbox keys to stay safe

## See Also

- [AskRentAI MCP](/hermes/mcp/servers/external/askrentai-mcp/)
- [Taskfolk MCP](/hermes/mcp/servers/external/taskfolk-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
