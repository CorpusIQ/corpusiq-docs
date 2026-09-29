---
title: "EQIQs MCP - Team Working-Style Insights for Agents"
description: "EQIQs brings working-style and compatibility insights from 21 frameworks (DISC, Big Five, MBTI-style) into your assistant: team reads up to 12 people, 1:1 prep, meeting tips and coaching narratives."
category: "Productivity"
stars: n/a (new listing)
added: 2026-09-28
source: "mcp.so server page (eqiqs.com)"
relevance: ★★★
tags: [hr, team-building, coaching, compatibility, meeting-prep, remote-mcp]
---

# EQIQs MCP

**Working-style and compatibility insights for managers and coaches.** EQIQs scores people and teams across 21 working-style frameworks, including DISC, Big Five and MBTI-style preferences, then turns those scores into practical outputs: how to prepare for a 1:1, how two people will work together, and who on the team is best placed to lead a project.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (sign in with your EQIQs account); Bearer token for clients that cannot complete OAuth
Endpoint: https://adgmsnwjynqkhawhioil.supabase.co/functions/v1/mcp
Tools: 16 named tools across profiles, compatibility, teams, meetings and assessments
Pricing: free core tools; generate_narrative is a premium coaching read priced before it runs
Category: Productivity / HR, Team Building and Coaching
Built by: EQIQs (eqiqs.com)
```

## Why This Matters for Operators

Most manager tooling collects personality data and stops there. EQIQs is built for the decision moments around that data: the 1:1 you need to prepare for, the pair you are about to staff together, the team of up to 12 you inherited and need to read quickly. Instead of paging through assessment reports, you ask the assistant questions and get scoped answers.

Privacy posture matters here too: work views hide personal-life data such as love language, attachment style and date of birth, and the vendor is explicit that EQIQs supports decisions but is not for making hiring decisions.

## Tools & Capabilities

| Tool area | Tools | Purpose |
|---|---|---|
| Profile | get_my_profile, list_profiles, get_profile, create_profile | Read your own 21-framework profile and the people in your workspace |
| Compatibility and teams | score_compatibility, score_team, suggest_lead | Compare two people, read a team of up to 12, find who is best placed to lead |
| Meeting prep | prep_meeting | Tips that fit the meeting's goal |
| Invites and assessments | invite_person, list_invites, start_assessment, submit_assessment | Invite someone with clear notice of who sees their results, run the assessment in chat |
| Notes and relationships | add_note, list_notes, list_relationships | Private notes on people and your connections |
| Premium coaching | generate_narrative | In-depth coaching read, price shown before it runs |

All 16 tool names come from the vendor's published tool list on the mcp.so listing.

## Installation

```bash
npx -y mcp-remote https://adgmsnwjynqkhawhioil.supabase.co/functions/v1/mcp
```

Add the server address, sign in with your EQIQs account when prompted, then approve access. Docs at eqiqs.com/mcp, support at support@eqiqs.com.

## Configuration

```json
{
  "mcpServers": {
    "eqiqs": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://adgmsnwjynqkhawhioil.supabase.co/functions/v1/mcp"]
    }
  }
}
```

## Business Relevance

- **Managers** prepare for 1:1s with tips matched to the person and the goal
- **Team leads** read a team of up to 12 without commissioning a workshop
- **Coaches** run assessments in chat and get narrative reads with visible pricing
- **Founders** check who is best placed to lead a project before assigning it

## Integration with CorpusIQ

EQIQs supplies the people layer; CorpusIQ supplies the business layer. Pair team reads with the CorpusIQ CRM connectors so the agent can answer "who on the team is best placed to lead this deal?" with both working-style data and pipeline history in the same conversation. Meeting prep fits the CorpusIQ calendar connector workflow: pull the next 1:1 from the calendar, then ask EQIQs for prep tips for that person and that goal.

## Limitations

- New listing with no track record yet
- Team reads cap at 12 people
- OAuth 2.1 required for remote use; Bearer token exists for clients that cannot complete OAuth
- Not for hiring decisions; results support decisions only
- generate_narrative is premium, priced per run

## FAQ

### Is this a hiring tool?

No. EQIQs is explicit that it supports decisions and is not for making hiring decisions. Work views also hide personal-life data such as love language, attachment style and date of birth.

### How many people can a team read cover?

A team read covers up to 12 people. For larger groups, run multiple reads or compare pairs with score_compatibility.

### What is paid?

The core tools are free to use. generate_narrative, the in-depth coaching read, is premium and shows its price before it runs.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
