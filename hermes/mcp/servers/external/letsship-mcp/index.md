---
title: "SHIP MCP - AI Coding Agent Team for Your Repo"
description: "Assign a Linear, Jira or GitHub issue to an autonomous agent team that plans, builds, reviews and tests, then opens a pull request in your repo."
category: DevOps
stars: n/a (new listing)
added: 2026-10-12
source: "mcp.so /feed (Oct 12, 2026 midday supplement sweep)"
relevance: ★★
tags: [ai-coding, coding-agents, software-delivery, pull-requests, code-review, developer-ops, linear, jira, remote-mcp]
---

# SHIP MCP

**Remote MCP server (Streamable HTTP, OAuth sign-in or a project-scoped token)** - an agentic software delivery platform: assign a Linear, Jira or GitHub issue to a team of coding agents that plans, builds, reviews and tests the change in your own repository, ending in a pull request that passed your CI, a code review and a test of its acceptance criteria.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in on first connect, or a SHIP personal access token (a token bound to one project reaches only that project's missions)
Endpoint: https://mcp.letsship.ai/mcp
Tools: 71 (missions, agent runs and logs, projects, sandboxes, scheduled tasks, preview environments, proof artifacts, MCP server bindings, credits and billing)
Pricing: First missions free, no card needed; credit packs plus Starter and Scale monthly plans; Enterprise by contract
Category: DevOps
Built by: SHIP (letsship.ai, hosted service)
Website: letsship.ai
Listing: mcp.so /feed (Oct 12, 2026 midday supplement sweep)
```

## Why This Matters for Operators

Agents write a growing share of production code, and the hard part has moved from generating the change to verifying it, attributing it and funding it. SHIP's answer is a pipeline: each mission runs through defined roles (Researcher, Planner, Builder, Reviewer, Operator, Tester), and your CI plus a preview deploy act as gates between the stages. Work that fails a gate goes back to the Builder with the reason, not silently forward.

You delegate from the tools your team already uses. File or assign the issue in Linear, Jira or GitHub and the agents work where the thread already lives; you can send a follow-up instruction to a running mission and read its progress, verdicts, cost and session logs from a chat client, a tracker or the terminal. Every mission ends as a normal pull request in your repository, so code review, CODEOWNERS and your merge rules stay where they are, and you decide whether SHIP merges automatically once the checks, review and acceptance test pass.

The operator dividend is visibility. Mission detail shows what each agent did on its turn, which agent and model ran it and what it cost, and the proof surface carries the QA screenshots, video and test traces behind each acceptance criterion. That turns AI coding spend from an open question into a per-mission ledger, which is the part most teams cannot answer today.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Missions | start_mission, create_mission, list_missions, get_mission, inspect_mission: dispatch an issue to the agent team, follow stages, verdicts and cost |
| Mission control | pause_mission, resume_mission, stop_mission, send_mission_instruction, approve_mission_ceiling, merge_mission, decline_mission, set_mission_auto_merge, archive_mission, unarchive_mission, set_mission_disposition: steer, approve, cap and close work |
| Agent runs and logs | list_agent_runs, get_agent_run, get_agent_run_logs, watch_agent_run, stop_agent_run: per-agent sandbox runs, resource metrics and session logs |
| Proof artifacts | list_artifacts, get_artifact: QA screenshots, video and test traces with signed links |
| Projects | list_projects, get_project, update_project: repository and tracker connections, auto-merge and default sandbox settings |
| Mission overrides | set_agents_override, get_agents_override, clear_agents_override: per-issue harness, model, effort and prompt overrides |
| Scheduled tasks | list_scheduled_tasks, list_scheduled_task_templates, get_scheduled_task, create_scheduled_task, update_scheduled_task, run_scheduled_task, list_scheduled_task_runs, delete_scheduled_task: recurring missions such as dependency upkeep |
| Sandboxes | list_sandbox_templates, get_sandbox_capacity, list_sandbox_starters, list_sandbox_template_versions, get_sandbox_build_log, save_sandbox_template, build_sandbox_template, activate_sandbox_template_version, list_sandbox_registries, save_sandbox_registry, delete_sandbox_template, delete_sandbox_registry: the environments agents start in |
| Preview environments | list_environments, get_environment, destroy_environment: per-pull-request previews |
| MCP server bindings | list_mcp_servers, list_mcp_bindings, set_mcp_config_path, bind_mcp_server, unbind_mcp_server, refresh_mcp_server_tools, start_mcp_server_oauth: the MCP servers the agents themselves may use, with role and tool approvals |
| Workspace | whoami, get_setup_progress, get_notices, dismiss_notice, get_billing, list_billing_ledger, list_credit_offers, start_credit_checkout, update_team_subscription, request_more_credits, healthz, list_orgs: identity, setup, notices, credits and billing |

## Installation

```bash
claude mcp add ship --transport http https://mcp.letsship.ai/mcp
```

The vendor publishes one-step setup snippets for the major MCP clients; any Streamable HTTP client can use the endpoint directly.

## Configuration

```json
{
  "mcpServers": {
    "ship": {
      "type": "http",
      "url": "https://mcp.letsship.ai/mcp"
    }
  }
}
```

On the first connection your client opens a browser sign-in (OAuth); SHIP can also issue personal access tokens, and a token bound to one project reaches only that project's missions. You need a SHIP account and a connected GitHub repository.

## Business Relevance

- **Engineering leads** hand a backlog issue to the agent team and read the outcome in the tracker thread, with per-stage reports instead of another dashboard to check.
- **CTOs and technical founders** keep the governance shape: CI and preview deploys gate the stages, the deliverable is a normal pull request, and auto-merge is a deliberate setting rather than a default.
- **Operators tracking AI spend** get a per-mission cost ledger with role and model breakdowns, plus credit notices before work is dispatched.
- **Platform teams** can schedule recurring maintenance missions (for example a weekly dependency upgrade) and give agents the MCP servers the project declares, with tool-level approvals.
- **Compliance-minded teams** can run inference on their own provider accounts and regions, and every mission carries an audit trail of runs, verdicts and proof artifacts.

## Integration with CorpusIQ

SHIP executes in the repository; CorpusIQ answers from the business systems around it. Ask a connected assistant what changed and what it cost, and read the same work through both lenses: CorpusIQ's read-only connectors (GitHub, Stripe, QuickBooks, GA4, Shopify and the rest of the stack) show the business picture, while SHIP's mission tools report which issue is in flight, which stage it reached, what it cost and what proof it produced for the same repository.

A practical composed workflow: an operator asks in chat which tickets have gone stale and what software work is consuming budget; CorpusIQ pulls the issue and billing context, and SHIP takes the next issue as a mission and returns the pull request. The pair covers the loop from "what does the business need" to "the change is merged", with the human approving direction rather than relaying tasks.

## Limitations

- Brand new: the server was first listed on October 12, 2026 and runs platform version 0.24.x, so there is no long track record yet.
- Hosted and commercial: first missions are free, then credits are consumed per mission under credit packs, Starter and Scale plans, or an Enterprise contract.
- Requires a SHIP account and a connected GitHub repository; the agent team runs on SHIP's platform, and the vendor states SOC 2 Type II, GDPR and HIPAA compliance work is in progress.
- Not self-hosted: your models and regions are supported for inference, but the orchestration platform is SHIP's, not yours.
- The MCP surface is broad and includes billing actions; scope tokens deliberately (project-bound tokens limit an agent to one project's missions).

## FAQ

### What do I need to start?

A SHIP account (GitHub or email signup) and a connected GitHub repository. The first missions are free and no card is needed.

### Which trackers can hand work to SHIP?

Linear, Jira and GitHub issues. File a mission from a tracker issue, or create the issue and start the run in one call from any MCP client.

### Does SHIP merge pull requests without a person?

Not by default: each mission ends in a normal pull request, and merging is an explicit tool call or a per-project auto-merge setting you control once CI, the review and the acceptance test pass.

### Can agents use our own MCP servers and model keys?

Yes. Project repositories declare the MCP servers agents may use, with enabled roles and approved tools, and provider keys stay at the platform edge rather than entering agent sandboxes.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
