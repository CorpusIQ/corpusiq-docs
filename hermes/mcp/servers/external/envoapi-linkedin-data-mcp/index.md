---
title: "EnvoAPI LinkedIn Data MCP - B2B Enrichment for Agents"
description: "Official LinkedIn data MCP: 40 read-only tools to look up people, companies, jobs and posts and find or verify work emails - OAuth or API key."
category: "Sales & Outreach"
stars: n/a (new listing)
added: 2026-10-08
source: "mcpservers.org /all (October 8, 2026 midday sweep)"
relevance: ★★★
tags: [linkedin, data-enrichment, sales, recruiting, prospecting, b2b, people-search]
---

# EnvoAPI LinkedIn Data MCP

**Hosted MCP server that gives your assistant LinkedIn data with no scraping stack** - look up people, companies, jobs and posts, and find or verify work emails, all read-only. 40 tools on one endpoint with OAuth or an API key, on the same credits as the vendor's REST API.

```
Server type: Remote (Streamable HTTP at https://api.envoapi.com/mcp)
Auth: OAuth sign-in or API key (one key works for MCP and the REST API)
Docs: https://docs.envoapi.com/guides/mcp/
Tools: 40, all read-only (profiles, companies, search, jobs, posts, emails, websites)
Credits: plan-based; 100 free credits on new accounts
Data: public LinkedIn data via EnvoAPI (independent service, not affiliated with LinkedIn)
Category: Sales & Outreach
Built by: EnvoAPI (envoapi.com)
```

## Why This Matters for Operators

Sales, recruiting and market-research workflows all start the same way: who is this person, where do they work, what is the company doing, and what is the best way to reach them. This server turns those questions into plain-language prompts - find the VP of Sales at a company and summarize their background, list the jobs a prospect has open by team, summarize the comments on a post, or find and verify a work email - without building a scraping pipeline or paying for a separate enrichment seat per teammate.

## Tools & Capabilities

| Group | Tools |
|---|---|
| Profiles (13) | `get_profile_details`, `get_profile_contact`, `get_profile_full_experience`, `get_profile_education`, `get_profile_skills`, `get_profile_certifications`, `get_profile_courses`, `get_profile_company_interests`, `get_profile_volunteer_experience`, `get_profile_posts`, `get_profile_comments`, `get_profile_reactions`, `get_similar_profiles` |
| Companies (6) | `get_company_details`, `get_company_people`, `get_company_posts`, `get_company_products`, `get_company_jobs`, `get_similar_companies` |
| Search (11) | `search_people_by_keyword`, `search_companies_by_domain`, `search_companies_by_keyword`, `search_schools_by_keyword`, `search_all_results_by_keyword`, `search_posts_by_hashtag`, `search_posts_by_keyword`, `search_locations_by_keyword`, `search_industries_by_keyword`, `search_service_categories`, `get_search_typeahead` |
| Jobs (2) | `search_jobs`, `get_job_details` |
| Posts (3) | `get_post`, `get_post_comments`, `get_post_reactions` |
| Emails (2) | `find_email`, `verify_email` |
| Websites (3) | `get_website_content`, `get_website_text`, `search_website_emails` |

Each call returns one page of results (3 per page for people and hashtag post searches, 10 for most other lists); ask for the next page to keep going.

## Installation

```bash
claude mcp add --transport http envoapi https://api.envoapi.com/mcp
```

```json
{
  "mcpServers": {
    "envoapi": {
      "url": "https://api.envoapi.com/mcp"
    }
  }
}
```

Clients with built-in OAuth sign in on first connect; clients without OAuth support attach an API key created in the EnvoAPI dashboard.

## Credits & Access

- Calls use your plan's credits and rate limits, the same as the REST API - one account and one balance across MCP, REST and the Python, TypeScript and Go SDKs.
- Typical costs: profile, company, post, job and search lookups 1 credit; profile contact and email verification 2; reading a web page 2; collecting a site's emails 5; finding a work email 10.
- Bad input is rejected before any credits are taken and provider-broken calls are refunded; finished contact and email lookups are charged even when they return nothing.
- New accounts get 100 free credits; pricing is at envoapi.com/pricing.

## Configuration

Live probe (October 8, 2026): POST initialize returns HTTP 401 with "The access credential is missing or invalid." - the endpoint is live and auth-gated. OAuth connections can be revoked from the dashboard (MCP page, Connected clients) and API keys from Dashboard > API keys, stopping every client that uses them.

## Example Prompts

- "Find the VP of Sales at Northstar Systems and summarize their background."
- "Brief me on Northstar Systems: size, HQ, open roles and recent posts."
- "Show me the jobs Northstar Systems has open right now, grouped by team."
- "Find the work email for Northstar's Head of Marketing and verify it."

## Integration with CorpusIQ

EnvoAPI supplies the outside people-and-company picture; CorpusIQ keeps your own records consistent. Pair a prospect brief from EnvoAPI with the customer, revenue and pipeline answers CorpusIQ reads from HubSpot, Stripe or your CRM - one conversation, cited on both sides.

## Limitations

- Independent service: it returns public LinkedIn data, not the official LinkedIn API, and you never connect your own LinkedIn account.
- Strictly read-only: the tools cannot post, message, connect or change anything.
- The email finder works on company domains; catch-all domains are charged but may return no address.
- Credit-metered per call; batch enrichment work belongs in the REST API rather than chat.

## FAQ

### Can this post or message on LinkedIn for me?

No. All 40 tools are read-only by design - they can look up and enrich, but they cannot post, message, connect or change anything.

### Is this the official LinkedIn API?

No. EnvoAPI is an independent service that returns public LinkedIn data; you sign in to EnvoAPI, not LinkedIn. The vendor publishes a comparison of the official and unofficial options.

### Does it work without CorpusIQ?

Yes - it is a standalone hosted server. CorpusIQ is one convenient way to pair enriched people and company data with your own business records in the same chat.

## See Also

- [LinkedIn MCP by GTM API - Integration Guide](/hermes/mcp/servers/external/linkedin-mcp-gtm/)
- [Snov.io MCP - B2B Sales and Outreach for Agents](/hermes/mcp/servers/external/snovio-mcp/)
- [looot MCP - One Balance for 2,350 Data APIs](/hermes/mcp/servers/external/looot-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
