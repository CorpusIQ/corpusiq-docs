# Case Study: Nonprofit Organizations

Nonprofits operate with constrained resources, mission-driven metrics, and complex stakeholder relationships. Hermes automation amplifies lean teams by handling repetitive administrative work, improving donor relationships, and demonstrating impact to funders.

## Donor Management

Donor relationships are the lifeblood of most nonprofits. Hermes skills help manage these relationships at scale without losing the personal touch that drives giving.

**Donor intelligence skill.** When a major donor is identified (through giving history, event attendance, or board referral), a skill builds a comprehensive profile:

- Giving history: total lifetime value, frequency, campaign preferences, average gift size
- Engagement history: events attended, volunteer hours, board service, program visits
- Communication history: last contact date, preferred channel, topics of interest
- Suggested next actions based on giving patterns: upgrade ask, recurring gift conversion, planned giving conversation, or stewardship touch

This profile arrives before donor meetings so fundraisers walk in prepared, not scrambling through spreadsheets.

**Lapsed donor reactivation.** A cron runs monthly identifying donors whose last gift falls outside their historical giving cadence. For a donor who gives quarterly but hasn't given in 5 months, the skill drafts a personalized re-engagement message referencing their specific interests. The development team reviews and customizes before sending.

**Gift acknowledgment workflow.** Timely, personal thank-you notes correlate strongly with donor retention. A "Gift acknowledgment" skill monitors for new donations daily and:

- For gifts under $100: generates a draft email acknowledgment with the correct gift amount, fund designation, and tax language
- For gifts $100-$999: generates a personalized acknowledgment referencing the donor's history
- For gifts $1,000+: alerts the development team for personal outreach within 24 hours, and drafts a customized acknowledgment incorporating program impact data relevant to the restricted fund

## Grant Tracking and Reporting

Grants fund most nonprofit programs but the administrative overhead of tracking deadlines, requirements, and reporting can consume 20-30% of program staff time.

**Grant calendar skill.** A skill that ingests all active grants and produces:

- Upcoming deadlines (applications, reports, renewals) in a prioritized calendar view
- Requirements checklist per grant (financial report, narrative report, metrics, board sign-off)
- Historical win/loss data to inform pursuit decisions
- Grant writer workload balance — who is writing what, and what's the pipeline capacity?

**Grant report assembly.** When a grant report is due, a skill gathers the required components:

1. Financial data from the accounting system (expenditures against grant budget)
2. Program metrics from the monitoring system (beneficiaries served, outputs delivered)
3. Narrative highlights from program reports and success stories
4. Compliance checklist verification

The skill assembles a draft report matching the funder's template. Program staff review, add qualitative context, and submit — saving hours of data gathering per report.

## Volunteer Coordination

Volunteer management involves matching skills to opportunities, tracking hours, and maintaining engagement.

**Volunteer matching skill.** When a new volunteer registers with skills and availability, the skill matches them against open opportunities. For an event needing Spanish-speaking volunteers on Saturday mornings, the skill surfaces the three registered volunteers who match those criteria.

**Hour tracking and recognition.** A cron aggregates volunteer hours monthly by program. When volunteers hit milestones (50 hours, 100 hours, one-year anniversary), the skill generates recognition messages and alerts the volunteer coordinator.

**No-show follow-up.** When a volunteer misses a scheduled shift, the skill sends a gentle check-in (not automated — queued for coordinator review) asking if everything is okay and offering to reschedule. The tone is support, not scolding.

## Impact Reporting

Demonstrating impact is how nonprofits attract funding and maintain trust. Hermes skills transform program data into compelling narratives.

**Impact dashboard skill.** "Show me our impact this quarter" produces:

- Key metrics vs. targets: beneficiaries served, services delivered, outcomes achieved
- Geographic distribution of impact
- Demographic breakdown of beneficiaries served
- Cost per outcome (calculated: total program spend / outcomes achieved)
- Comparison to previous quarter and same quarter last year

**Annual report assembly.** A skill that gathers the year's data — financials, program metrics, donor recognition lists, board member listings, success stories — and produces a draft annual report structured for the organization's template. The communications team adds polish and design, but the data gathering is automated.

**Grant proposal data.** When a grant application asks "how many people did you serve last year?" the answer lives in spreadsheets, program databases, and volunteer logs. A skill aggregates this across sources so grant writers aren't hunting through files.

## Common Nonprofit Patterns

**Works well:**
- Stewardship automation that keeps the human touch (drafts for review, never auto-send)
- Grant calendar as the single source of truth for deadlines
- Impact metrics that flow automatically from program data
- Donor segmentation based on demonstrated interests, not just giving capacity

**Avoid:**
- Automating donor communications without review (donors can tell, and it damages trust)
- Over-engineering metrics that programs can't reliably collect
- Applying for-ecommerce patterns to nonprofit fundraising (different motivations, different metrics)
- Storing sensitive beneficiary data in logs or memory

## Integration Patterns

Nonprofit Hermes setups typically connect to:
- CRM/donor database (Salesforce Nonprofit Cloud, Bloomerang, DonorPerfect)
- Accounting (QuickBooks, Sage Intacct)
- Email marketing (Mailchimp, Constant Contact)
- Grant management (Fluxx, GrantHub)
- Volunteer management (VolunteerMatch, Galaxy Digital)
- Program monitoring (custom databases, survey tools)

The nonprofit sector runs on relationships. Hermes handles the data so humans can focus on the connection.
