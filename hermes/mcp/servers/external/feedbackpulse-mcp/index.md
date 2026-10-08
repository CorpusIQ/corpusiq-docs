---
title: "FeedbackPulse MCP - Employee Surveys and Reviews"
description: "Hosted MCP server for employee engagement: 19 tools over surveys, performance and peer reviews, and recognition, with admin-scoped writes and four guided prompts, over OAuth."
category: People Operations
stars: n/a (new listing)
added: 2026-10-08
source: "mcpservers.org /all (October 8, 2026 night sweep)"
relevance: ★★★
tags: [hr, employee-engagement, surveys, performance-reviews, recognition, people-ops]
---

# FeedbackPulse MCP

**Hosted MCP server that answers people-ops questions from your engagement data** - survey results and completion rates, review-cycle progress by department, recognition stats and employee lists, as 19 tools with the same permission model as your dashboard role. Write actions (survey drafts and templates) are admin-scoped.

```
Server type: Remote (Streamable HTTP at https://app.feedbackpulse.com/mcp)
Auth: OAuth (an admin grants MCP access in Settings > Integrations; AI Integration must be enabled on the organisation)
Tools: 19 across surveys, reviews, recognitions, employees and admin audit
Prompts: 4 guided workflows - analyze_survey_results, engagement_health_check, performance_review_prep, team_pulse
Pricing: requires a FeedbackPulse plan (the performance-review prompt needs reviews enabled)
Category: People Operations
Built by: FeedbackPulse
```

## Why This Matters for Operators

Engagement data usually dies in a dashboard nobody opens between survey cycles. The questions leaders actually ask are conversational - "what is the completion rate for this review cycle by department?", "who are our top recognition recipients this quarter?", "which employees have not started their reviews?" - and this server answers them from the live data with four pre-built workflows for the recurring ones. The privacy design is the part to respect: anonymous responses are protected by a minimum-response threshold, managers see reviews and employee tools but no survey or recognition data through MCP at all, and every write needs an admin-scoped token.

## Tools & Capabilities

| Area | Tools |
|---|---|
| Surveys | list surveys with status and completion rates, survey detail, results and response statistics, AI-generated theme summaries, template listing and management, draft creation (returns a dashboard link for review and launch) |
| Reviews | review cycles with completion statistics, department-level breakdowns, individual performance reviews with status, peer reviews with reviewer info, aggregated peer review stats |
| Recognitions | aggregate recognition metrics and top recipients, individual recognition records with feedback text |
| Employees | employee list with department and manager info |
| Administration | read-only audit of MCP tokens (no secrets returned) and the MCP tool-call activity log |
| Guided prompts | analyze_survey_results, engagement_health_check, performance_review_prep, team_pulse |

## Installation

```bash
claude mcp add --transport http feedbackpulse https://app.feedbackpulse.com/mcp
```

```json
{
  "mcpServers": {
    "feedbackpulse": {
      "url": "https://app.feedbackpulse.com/mcp"
    }
  }
}
```

Sign in with your FeedbackPulse credentials through the browser prompt and approve the listed permissions.

## Configuration

Your organisation needs AI Integration enabled (Settings > Features) and the admin must grant MCP access (Settings > Integrations), unless you are the admin. Write scopes (survey drafts and templates) require `mcp:write` and Admin. Live probe: POST initialize returns 401 "Unauthenticated.", confirming the endpoint is live and auth-gated.

## Example Prompts

- "Run the engagement health check for Engineering over the last 90 days."
- "What is the completion rate for the current review cycle, broken down by department?"
- "Show me recognition stats for this quarter and the top recipients."
- "Which employees have not started their performance reviews?"

## Integration with CorpusIQ

CorpusIQ gives your AI clients consistent business numbers - revenue, orders, customers - read-only, cited and cross-client. FeedbackPulse covers the people signal beside them, so the same assistant can move from "how is the business performing" to "how are the teams that run it doing" without switching tools.

## Limitations

- Access mirrors the role of the account that connects; managers do not see survey or recognition data through MCP, and anonymous responses respect the configured privacy threshold.
- Writes are limited to drafts and templates and need admin scope; launches still happen in the dashboard.
- Requires an existing FeedbackPulse organisation with the AI Integration feature enabled.
- New listing - no published third-party track record yet.

## FAQ

### Can it read everything in the organisation?

Only what the connecting account is authorised to see. Admins see organisation data; managers see their reports for review and employee tools, but no survey or recognition data through MCP.

### Are anonymous survey responses exposed?

Individual text responses are withheld when the number of responses falls below the configured privacy threshold.

### Can the agent create surveys?

It can create a real but unlaunched survey draft from a template and returns a dashboard link to review and launch - admin scope required. It cannot launch on its own.

## See Also

- [TheDeskMonitor MCP - Workforce Analytics from Chat](/hermes/mcp/servers/external/thedeskmonitor-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
