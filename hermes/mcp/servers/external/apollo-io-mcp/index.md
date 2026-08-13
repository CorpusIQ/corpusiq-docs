---
title: "Apollo.io MCP — Integration Guide"
description: "MCP server for Apollo.io — 45+ tools for lead search, contact enrichment, sequence management, and CRM. 275M+ contacts, 30M+ companies."
category: "Sales & Outreach"
stars: "★★★"
source: mcpservers.org
github: https://github.com/Inferensys/apollo-io-mcp
date_added: 2026-07-28
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/apollo-io-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# Apollo.io MCP

MCP server wrapping Apollo.io's full API — 45+ tools giving AI agents access to the world's largest B2B contact database (275M+ contacts, 30M+ companies). Combined with the LinkedIn MCP by GTM API, this forms an end-to-end AI-driven outbound pipeline.

## What It Does

- **Lead Search:** Query Apollo's database by title, company, industry, location, technologies used, funding, and 100+ other filters
- **Contact Enrichment:** Get direct dials, verified emails, and firmographic data for any person or company
- **Sequence Management:** Create, update, and monitor email sequences from your AI agent
- **CRM Sync:** Push enriched contacts to Salesforce, HubSpot, or any connected CRM
- **Job Changes:** Track when prospects change companies (trigger for outreach)

## Why It Matters for Operators

Apollo.io is the dominant B2B data platform. Before this MCP:
1. Human logs into Apollo, runs searches, exports CSVs
2. Human uploads CSVs to CRM or outreach tool
3. Human writes sequences and triggers them manually

Now: AI agent searches Apollo → qualifies leads → enriches with direct contact data → pushes to CRM → triggers sequences — in one conversation.

Paired with LinkedIn MCP, the workflow becomes:
1. AI agent searches LinkedIn for target personas
2. AI agent enriches those profiles with Apollo (email, phone, company data)
3. AI agent sends LinkedIn connection request
4. AI agent triggers email sequence in Apollo
5. AI agent logs everything to CRM

## Setup

### Prerequisites
- Apollo.io account ([apollo.io](https://www.apollo.io))
- Apollo.io API key (Settings → Integrations → API Keys)
- Node.js ≥ 18

### Install
```bash
npx @inferensys/apollo-io-mcp
```

### Claude Desktop
```json
{
  "mcpServers": {
    "apollo-io": {
      "command": "npx",
      "args": ["@inferensys/apollo-io-mcp"],
      "env": {
        "APOLLO_API_KEY": "your-apollo-api-key"
      }
    }
  }
}
```

### Cursor / VS Code
```json
{
  "mcpServers": {
    "apollo-io": {
      "command": "npx",
      "args": ["@inferensys/apollo-io-mcp"],
      "env": {
        "APOLLO_API_KEY": "${APOLLO_API_KEY}"
      }
    }
  }
}
```

### Hermes Agent
```yaml
# ~/.hermes/config.yaml
mcp_servers:
  apollo-io:
    command: npx
    args: ["@inferensys/apollo-io-mcp"]
    env:
      APOLLO_API_KEY: "${APOLLO_API_KEY}"
```

## Tools (45+ total)

### Search & Discovery
| Tool | Description |
|------|-------------|
| `search_contacts` | Search 275M+ contacts with 100+ filter dimensions |
| `search_companies` | Search 30M+ companies by industry, size, tech stack, revenue |
| `people_search` | Find people matching specific criteria |
| `organization_search` | Find organizations by name, domain, or attributes |
| `bulk_people_enrichment` | Enrich up to 100 contacts at once |
| `saved_searches` | List and run saved Apollo searches |

### Contact Data
| Tool | Description |
|------|-------------|
| `enrich_person` | Get full contact details: email, phone, title, company, social profiles |
| `enrich_organization` | Get company details: employees, revenue, tech stack, funding |
| `reveal_email` | Get verified email addresses for contacts |
| `reveal_phone` | Get direct dial phone numbers |
| `job_change_monitor` | Check if contacts changed jobs recently |

### Sequences & Outreach
| Tool | Description |
|------|-------------|
| `list_sequences` | Get all active email sequences |
| `create_sequence` | Create a new outreach sequence |
| `add_to_sequence` | Add contacts to an existing sequence |
| `pause_contact` | Pause a contact in a sequence |
| `get_sequence_stats` | Get open/click/reply rates for a sequence |

### CRM & Integrations
| Tool | Description |
|------|-------------|
| `push_to_crm` | Push enriched contacts to Salesforce/HubSpot |
| `sync_status` | Check CRM sync status |
| `export_contacts` | Export contact lists to CSV or CRM |

## Pricing

Apollo.io plans (required):
- **Free:** 100 email credits/month, basic search
- **Basic:** $59/user/month — 900 email credits, sequences
- **Professional:** $99/user/month — 1,200 email credits, advanced filters, A/B testing
- **Organization:** $149/user/month — 2,400 email credits, CRM sync, job changes

The MCP server itself is free and open source (MIT).

## Use Cases

### Automated Lead Qualification
```
Agent: "Find companies using Snowflake that raised Series B in the last 12 months and have 50-200 employees"
→ search_companies(filters) → enrich_organization for each → qualify by tech stack + funding
```

### Contact Discovery Pipeline
```
Agent: "Find the Head of Data at every company in our target account list and get their email and phone"
→ search_contacts(company_list) → bulk_enrich → export to CRM
```

### Job Change Monitoring
```
Agent: "Check our CRM contacts for job changes this month and flag anyone who moved to a target account"
→ job_change_monitor(all_contacts) → filter by target_accounts → alert for outreach
```

### Sequence Automation
```
Agent: "Add these 50 qualified leads to our 'Enterprise Outbound' sequence and start tomorrow at 8 AM"
→ add_to_sequence(sequence_id, contacts) → schedule
```

## Limitations

- **Apollo.io plan required:** The MCP server needs an Apollo API key, which requires at minimum a Free plan.
- **Email credits:** Each enrichment consumes Apollo email credits. Bulk operations can exhaust credits quickly.
- **Job change data:** Available on Organization plan only ($149/mo).
- **Not a LinkedIn replacement:** Apollo provides contact data, not LinkedIn engagement. Pair with LinkedIn MCP for full coverage.

## See Also

- [[linkedin-mcp-gtm]] — LinkedIn automation (complementary)
- [[atlassian-mcp]] — Jira/Confluence for product teams
- [[stripe-mcp]] — Billing and payments
