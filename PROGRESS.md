# PROGRESS.md — corpusiq-docs build status

Snapshot of what was produced across three writing rounds, what's solid,
and what still needs human attention.

## File count

- **Total Markdown files:** 26 (excluding this PROGRESS.md).
- **Total lines:** ~2,150 across all docs.

Round-by-round breakdown:

| Round | Tree | Files | Notes |
|---|---|---|---|
| Round 1 | `README.md`, `quickstart/`, `prompts/`, `connectors/README.md` | 12 | Foundation. Quickstart is 5 steps, prompts are 9 topic pages. |
| Round 2A | `connectors/` per-connector pages | (see below) | Written by a parallel subagent. |
| Round 2B | `how-it-works/`, `troubleshooting/`, this file | 10 | Orientation + failure-mode pages. |

## Round 2B output (this round)

- `how-it-works/README.md`
- `how-it-works/what-is-corpusiq.md`
- `how-it-works/connectors-explained.md`
- `how-it-works/skills-explained.md`
- `how-it-works/privacy-and-security.md`
- `troubleshooting/README.md`
- `troubleshooting/connector-auth-failed.md`
- `troubleshooting/connector-shows-no-data.md`
- `troubleshooting/claude-cant-see-corpusiq.md`
- `troubleshooting/chatgpt-cant-see-corpusiq.md`

## Skills cited across the prompts tree (top 15)

Frequency from `grep '\`...\`' prompts/`:

1. `executive-snapshot` — 4
2. `financial-command-center` — 3
3. `ad-spend-truth-report` — 3
4. `sales-call-prep-brief` — 2
5. `missed-critical-email` — 2
6. `email-lifecycle-intel` — 2
7. `ecommerce-command-center` — 2
8. `customer-health-scorecard` — 2
9. `crm-pipeline-health` — 2
10. `board-update-drafter` — 2
11. `board-meeting-prep` — 2
12. `weekly-ops-review` — 1
13. `today-focus` — 1
14. `seo-authority-tracker` — 1
15. `qbr-prep-assembler` — 1

Additional skills cited once: `morning-briefing`, `meeting-funnel-analyst`,
`data-discrepancy-detector`. All cited skills verified to exist as
directories under `/home/tmalone/DevOps/skillsmcp/skills/` at write time.

## Connectors

The connector registry at
`/home/tmalone/DevOps/multi-source-mcp/config/connector_registry.json`
lists **31 connectors**. Per-connector setup pages live under
`connectors/` and were written by Round 2A; check that tree for
completeness and the presence of any `DOC-GAP` markers indicating a
connector that had no internal SETUP doc to translate from.

Internal SETUP docs available in
`/home/tmalone/DevOps/multi-source-mcp/Documentation/`:
ActiveCampaign, Airtable, Calendly, ChatGPT, ConstantContact, CosmosDB,
Custom App, Device Login, Dropbox, eBay, Facebook, Google Ads, HubSpot,
IMAP, Klaviyo, Mailchimp, Microsoft, Monday, MongoDB, MSSQL, Odoo,
QuickBooks, Semrush, Shopify, Slack, TikTok, YouTube.

Connectors in the registry that **do not** have an internal SETUP doc
and therefore likely need a doc-gap note in their `connectors/` page:
- Amazon Seller
- GunBroker
- LeadConnector / GoHighLevel
- PostScript
- GA4 (only an architecture mention)
- Search Console
- PostgreSQL (PG specifically — Cosmos/MSSQL/Mongo have setups)

## Voice / audience defaults

- **Audience:** Adam-class non-technical SaaS founder. Has 12-20 SaaS
  tools, doesn't write code, makes business decisions.
- **Voice:** Short sentences. Specific facts. No "leverage," "unlock,"
  "empower," "seamless." No exclamation points. No headlines selling
  the product back to a user who's already paying.
- **Page length:** 80-150 lines each. Quality over volume.
- **Mood:** Honest. Says what doesn't work, not just what does.

## Screenshots needed (placeholders found in repo)

All in `quickstart/`. The agent inserted `<!-- screenshot: ... -->`
markers where a screenshot would help; Ted needs to capture and embed:

- `quickstart/01-create-account.md`
  - corpusiq.io signup page
  - Dashboard landing view after first login
- `quickstart/02-connect-claude.md`
  - CorpusIQ Integrations panel showing Claude config block
  - Claude Desktop Developer settings
  - Claude conversation with the MCP tools indicator
- `quickstart/03-connect-chatgpt.md`
  - CorpusIQ Custom GPT landing page
  - OAuth approval prompt
  - ChatGPT Connectors settings
- `quickstart/04-first-connector.md`
  - CorpusIQ Connectors page with QuickBooks row
  - Intuit OAuth approval screen
  - Connector list showing QuickBooks Connected

Total: 11 screenshot slots.

## Doc gaps and contradictions noted

- **GA4 vs Search Console as connectors.** The registry lists both, but
  there's no internal SETUP doc for either; the system docs treat them
  as Google Workspace sub-products. The per-connector pages may need
  manual review.
- **GunBroker, Amazon Seller, PostScript.** Listed in the registry and
  exposed as tools, but no SETUP doc in
  `multi-source-mcp/Documentation/`. Round 2A had to infer setup steps
  from the tool descriptions.
- **GoHighLevel / LeadConnector.** Same connector under two names in
  different parts of the codebase. We standardize on "LeadConnector
  (GoHighLevel)" in user-facing docs.
- **Skill-engine docs.** There is no single source-of-truth doc for the
  skills catalog at the system level; we cite individual skill names
  from `/home/tmalone/DevOps/skillsmcp/skills/` and trust the SKILL.md
  in each. If the catalog churns, prompts/ and how-it-works/ will need
  to be re-checked.

## Items punted / skipped

- **No "developer" tree.** This is a user-facing repo; technical
  architecture lives in `multi-source-mcp/Documentation/`.
- **No pricing page.** Pricing is on corpusiq.io and changes
  independently of these docs.
- **No changelog.** Versioning of these docs is via git history.
- **No FAQ.** Folded into `how-it-works/` and `troubleshooting/`
  instead. A formal FAQ.md can be added later if user questions warrant
  it.
- **No CONTRIBUTING.md or LICENSE.** Ted to add if/when the repo goes
  public.

## Suggested next steps for Ted

1. **Capture the 11 screenshots** listed above. Replace the
   `<!-- screenshot: ... -->` markers with real `![alt](path)` links.
2. **Review Round 2A connector pages** for `DOC-GAP` markers. Fill in
   the missing pieces for Amazon Seller, GunBroker, PostScript,
   LeadConnector, Search Console.
3. **Decide on a public URL.** If corpusiq-docs becomes
   docs.corpusiq.io, add a deployment workflow (mkdocs, Docusaurus, or
   plain GitHub Pages).
4. **Add a feedback channel.** Either `support@corpusiq.io` or a
   GitHub Discussions link from the README so users have one place to
   send corrections.
5. **Wire skills doc back to the catalog.** As soon as the skills team
   has a public-friendly skill index, link to it from
   `how-it-works/skills-explained.md`.
6. **Round 3 candidates** (optional, not done here):
   - `recipes/` — copy-pasteable multi-step playbooks ("monthly close
     in 15 minutes," "board prep in 30").
   - `changelog/` — when the connector list or skills catalog moves.
   - `glossary.md` — OAuth, MCP, skill, connector, tool, runbook —
     defined in one place.

---

## Final state — 2026-05-25 (post-completion)

All four rounds shipped. Repo state:

- **59 markdown files**, **3,599 lines** of user-facing documentation
- **31 per-connector pages** — full coverage of the registry
- **7 DOC-GAP markers** (connectors without internal SETUP docs in `multi-source-mcp/Documentation/`): amazon_seller, gohighlevel, google_workspace, gunbroker, mongodb, postgres, postscript. Vendor click-paths for these were inferred from registry + vendor public docs and should be verified before publish.
- **10 prompt-library files** covering 9 categories + index, with skill-runbook attribution on every prompt where one applies.
- **5 quickstart files** + **5 how-it-works files** + **5 troubleshooting files**.

### Ready-to-consume

This documentation tree is suitable for Marin to convert into website pages or for direct hosting via MkDocs / Docusaurus / similar.

### Suggested next steps (for whoever picks this up)

1. Fill the `<!-- screenshot: ... -->` placeholders across `quickstart/` and `connectors/` once a real instance of the dashboard exists.
2. Verify the 7 DOC-GAP connector pages against the actual vendor UIs before publish.
3. Decide hosting: MkDocs Material → `docs.corpusiq.io` is the obvious answer.
4. Add a CHANGELOG section once content stabilizes, so users can see what shipped per release.
