# Case Study: Legal Firms

Legal practices manage confidential client matters under strict ethical obligations, bill by the tenth of an hour, and face relentless deadlines. Hermes automation helps legal professionals spend more time on high-value legal work and less on administrative process.

## Case Research and Analysis

Legal research is the foundation of effective representation but consumes hours per matter. Hermes skills accelerate research while keeping attorneys in control of strategy and judgment.

**Initial case assessment skill.** When a new matter opens, this skill performs a structured intake analysis:

1. **Jurisdictional analysis** — identifies the governing law, applicable statutes, and relevant court rules based on the matter's venue and subject matter
2. **Preliminary research** — searches legal databases for recent cases with similar fact patterns, identifying key holdings, procedural postures, and judicial treatment
3. **Elements checklist** — maps the legal elements of each claim or defense against the facts provided, flagging gaps that need further investigation
4. **Statute of limitations check** — verifies filing deadlines haven't lapsed and calendars critical dates

The output is a research memorandum draft that the attorney reviews, corrects, and expands — not a final work product, but a structured starting point that transforms "blank page" anxiety into "edit and refine" efficiency.

**Case law update monitoring.** A cron monitors new decisions in specified practice areas and jurisdictions. When a published opinion affects an active matter (same legal issue, same judge, same opposing counsel's firm), the skill alerts the responsible attorney with a summary of the decision and its potential impact.

**Brief citator check.** Before filing, a skill runs all cited authorities through citator databases to verify each case is still good law. It flags cases with negative subsequent treatment and provides the treating case citation. This catches Shepard's/Signal issues before the court or opposing counsel does.

## Document Review and Discovery

Document review in litigation and transactions is the legal profession's biggest time sink. Hermes skills provide first-pass review assistance.

**Privilege review assistance.** A skill pre-screens documents for potential privilege:

- Flags communications involving attorneys (attorney-client privilege)
- Identifies documents created in anticipation of litigation (work product doctrine)
- Highlights settlement communications and mediation materials
- Suggests privilege log entries with the claimed privilege and basis

The skill never makes privilege determinations — it surfaces likely privileged documents for attorney review. The attorney confirms or rejects each designation, creating the privilege log entries and the defensible record of review.

**Contract clause extraction.** For due diligence or contract review, a skill extracts key clauses across a document set:

- Indemnification provisions
- Limitation of liability
- Assignment and change of control
- Termination rights
- Governing law and dispute resolution
- Non-compete and exclusivity

Output is a comparison table showing how each contract handles each clause type, with deviation highlights. This transforms "read 200 contracts" into "review the outliers and customize the analysis."

**Deposition preparation.** A skill gathers relevant documents, prior testimony from the same witness, key exhibits, and suggested lines of questioning organized by topic. The attorney reviews and customizes — the skill handles the document gathering and organization.

## Billing Automation

Legal billing is precise, contentious, and regulated. Hermes skills improve accuracy and reduce write-offs.

**Time capture assistance.** A skill monitors the attorney's work patterns during the day (calendar events, email threads, document edits) and generates a draft timesheet with suggested time entries. The skill captures what happened and when — the attorney reviews for accuracy and adds narrative detail. This reduces the "what did I do last Tuesday?" problem.

**Billing guideline compliance.** A cron reviews draft invoices against client billing guidelines before submission:

- Block billing violations (multiple tasks in one time entry)
- Excessive time on routine tasks
- Unapproved timekeeper billing
- Vague narrative descriptions
- Out-of-policy expense entries

Flagged items go back to the billing attorney for correction before the invoice reaches the client — reducing write-offs and billing disputes.

**Alternative fee arrangement tracking.** For fixed-fee or capped-fee matters, a skill tracks actual time against the fee arrangement and alerts when the matter approaches 75%, 90%, and 100% of the cap. This prevents the unpleasant discovery that a fixed-fee matter consumed 150% of the agreed amount.

## Deadline Tracking and Docket Management

Missing a deadline in legal practice can mean malpractice. Hermes crons provide defense-in-depth for deadline management.

**Court deadline calculator.** A skill calculates deadlines from triggering events using the applicable rules. "A complaint was served on June 10th in federal court — when is the answer due?" The skill applies FRCP Rule 12 (21 days), checks for weekends/holidays, and returns the deadline with a note about the rule applied. It then calendars the deadline, a 7-day warning, and a 3-day warning.

**Statute of limitations monitoring.** A cron monitors all active matters and pre-litigation files for approaching statutes of limitations. Alerts trigger at 90, 60, 30, and 14 days before expiration. An expired statute of limitations with an alerted attorney who didn't act is a different problem than an expired statute no one saw coming.

**Court docket monitoring.** A cron checks court dockets for new filings, scheduled hearings, and judicial orders on active matters. New activity is summarized and routed to the responsible attorney within hours of docketing — no more discovering at the weekly team meeting that the court ruled on your motion three days ago.

## Conflict Checking

Ethical walls require that firms don't represent adverse parties. Hermes skills strengthen conflict-checking processes.

**New matter conflict check.** When a new matter opens, a skill searches the firm's client and matter database for potential conflicts:

- Direct adversity (proposed client vs. existing client)
- Positional conflicts (the legal position would harm an existing client's interests)
- Business conflicts (the matter involves a competitor of a major client)
- Former client conflicts (attorney previously represented the adverse party)

The skill flags potential conflicts for the conflicts committee or designated partner. It never clears conflicts — that's an ethical decision reserved for attorneys.

## Key Principles for Legal Deployments

**Attorney work product, not AI work product.** Every output from a Hermes skill is a draft for attorney review. The attorney's professional judgment transforms it into work product. This isn't just best practice — it's consistent with the duty of competence and the unauthorized practice of law prohibitions.

**Confidentiality is paramount.** Client confidences must never be stored in persistent model context, shared across matters, or exposed through logs. Each matter should be logically separated. Attorney-client privileged material requires the highest level of data protection.

**Transparency with clients.** Clients should understand the role of technology in their representation. Some clients request that AI not be used on their matters — firms need mechanisms to honor those requests.

**Supervision and training.** Attorneys using Hermes tools must understand their capabilities and limitations. A skill that summarizes 50 cases is a research accelerator; it doesn't replace reading the key cases. Training on proper use is an ethical obligation.

## Anti-Patterns Specific to Legal

- Using Hermes to draft legal advice without attorney review and sign-off
- Training models on client confidential information
- Auto-filing documents with courts (always human-reviewed and human-filed)
- Cross-matter data mixing in logs or memory
- Relying on Hermes as the sole deadline tracking system (defense in depth)
- Substituting AI analysis for Shepardizing/citator checks

Legal automation succeeds when it handles the process so attorneys can focus on the advocacy.
