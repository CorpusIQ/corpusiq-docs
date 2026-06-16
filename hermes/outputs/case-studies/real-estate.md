# Real Estate: Listing Automation & Lead Management

Real estate professionals manage a high-velocity pipeline: listings come and go, leads arrive from multiple channels, market conditions shift, and transaction paperwork piles up. Hermes Agent can automate the repetitive data work, giving agents and brokers more time for client relationships and negotiations.

## The Real Estate Workflow

A typical agent or brokerage deals with: MLS listing management, lead capture from portals and websites, market analysis for pricing, showing coordination, offer and counter-offer tracking, document preparation, and transaction milestone monitoring. Many of these involve checking multiple systems and manually moving data between them.

Hermes sits in the middle, connecting your CRM, MLS data feeds, calendar, email, and document systems.

## Property Listing Automation

Listing a property involves entering the same data into multiple systems: the MLS, your brokerage website, syndication platforms, social media, and email marketing. Hermes can manage the multi-platform distribution.

**Listing Syndication Monitor**

```yaml
- name: listing-sync-check
  schedule: "0 */6 * * *"  # Every 6 hours
  skill: listing-syndication-check
  description: Verifies active listings appear correctly across all platforms
```

This skill queries your CRM (HubSpot, Close, LeadConnector) for active listings, then checks each syndication destination for accuracy: Are all photos present? Is the price correct? Are status changes (active, pending, sold) reflected everywhere? Discrepancies generate alerts with specific corrections needed.

**Market Analysis Automation**

```yaml
- name: weekly-market-analysis
  schedule: "0 7 * * 1"  # Monday at 7 AM
  skill: market-analysis
  description: Pulls comparable sales data and generates pricing insights
```

The skill queries MLS data (via API or database connector) for recent comparable sales, active listings, and market absorption rates within target neighborhoods. It produces a Monday-morning market pulse: median days on market, list-to-sale price ratios, inventory levels, and price-per-square-foot trends — segmented by property type and price band.

## Lead Qualification & Routing

Real estate leads arrive from diverse sources: Zillow, Realtor.com, brokerage website forms, open house sign-ins, social media, and past-client referrals. Manual triage means leads age while agents sort through them.

**Automated Lead Qualification**

```yaml
- name: lead-qualification
  schedule: "*/15 * * * *"  # Every 15 minutes
  skill: real-estate-lead-qualify
  description: Scores and routes new leads from all sources
```

The skill:
1. Monitors lead sources (email inbox for portal notifications, CRM for web forms, calendar for open house registrations)
2. Enriches each lead: checks the CRM for existing relationships, searches property databases for ownership history, estimates timeline from lead behavior
3. Scores leads on a configurable rubric (pre-approved, timeline urgency, property type match with agent specialties)
4. Routes high-scoring leads immediately (Slack notification, SMS, CRM assignment)
5. Places lower-scoring leads into nurture sequences for automated follow-up

**Showing Coordination**

```yaml
- name: showing-scheduler
  schedule: "*/10 * * * *"  # Every 10 minutes
  skill: showing-coordinator
  description: Processes showing requests and coordinates with agent calendars
```

When a showing request arrives (via calendar, email, or showing service), Hermes checks agent availability, property access constraints, and travel time between appointments, then proposes optimal time slots. For confirmed showings, it sends the agent a prep packet: property details, comparable sales, client notes, and any disclosure documents.

## Transaction Management

Once a property goes under contract, a cascade of deadlines and documents begins: inspection periods, appraisal, financing contingencies, title work, and closing coordination. Missing a deadline can kill a deal.

**Transaction Milestone Tracker**

```yaml
- name: transaction-milestone-monitor
  schedule: "0 7,13,19 * * *"  # Three times daily
  skill: transaction-milestones
  description: Checks all active transactions for upcoming and overdue milestones
```

The skill:
1. Queries the CRM or transaction management system for all active deals
2. Calculates days remaining for each contingency period
3. Flags approaching deadlines (48-hour warning, 24-hour warning)
4. Identifies overdue items (missing inspection report, unsigned amendment, unconfirmed financing)
5. Routes alerts to the agent and transaction coordinator with direct links to relevant documents

**Document Preparation**

```yaml
- name: document-readiness-check
  schedule: "0 8 * * *"
  skill: transaction-documents
  description: Verifies all required documents exist for transactions closing within 2 weeks
```

The skill checks closings scheduled in the next 14 days and verifies: signed contract, disclosures, inspection reports, appraisal, title commitment, HOA documents, and closing statement draft. Missing items generate a checklist for the transaction coordinator.

## CRM Integration Patterns

Real estate runs on CRM. Key integration patterns:

- **HubSpot**: Use the CRM connector to manage contacts, deals, and companies. Each property = a deal with pipeline stages matching your transaction workflow.
- **Close CRM**: Use the Close connector for lead management and opportunity tracking with activity timeline.
- **LeadConnector**: For brokerages using HighLevel, the CRM connector covers contacts, opportunities, appointments, and conversations.
- **Email**: Gmail and Outlook connectors let Hermes monitor listing inquiries, offer emails, and closing communications directly.

## Getting Started in Real Estate

1. **Connect your CRM first.** Everything else builds on the contact and deal data in your CRM. Get that connector running before anything else.
2. **Start with lead routing.** It's the highest-volume, highest-ROI automation. Fifteen-minute lead response times dramatically improve conversion rates.
3. **Add listing monitoring second.** Listing accuracy across platforms protects your reputation and avoids MLS compliance issues.
4. **Build transaction tracking last.** It's the most complex but also the most valuable per-incident (one missed deadline can cost a deal).
5. **Use Slack for alerts.** Real estate teams live in their phones. Slack notifications beat email every time for time-sensitive items.

The outcome: agents spend less time on data entry and more time on showings and negotiations, while deals move through the pipeline with fewer dropped balls.
