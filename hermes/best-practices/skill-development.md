# Skill Development Guide

Skills are Hermes's superpower — they encode repeatable expertise into reusable, shareable packages. A well-written skill transforms "I need to do X" into a single invocation that handles tool orchestration, error recovery, and output formatting.

## When to Create a Skill

Not every task deserves a skill. Create a skill when:

**You've done it three times manually.** The first time, you figure it out. The second time, you refine it. The third time, it's a pattern — encode it as a skill. The "rule of three" prevents premature abstraction.

**Someone else needs to do it.** If a teammate asks "how do I check our marketing performance?" more than once, the answer should be a skill, not a verbal explanation. Skills transfer institutional knowledge without requiring everyone to become prompt engineers.

**It involves multiple tool calls in sequence.** A skill that chains "fetch data from X, transform it, enrich it from Y, format as a report" saves significant context and reduces error rates compared to manual multi-step prompting.

**It needs guardrails.** When a task requires specific validation, approval gates, or error handling, encoding those in a skill ensures they're applied consistently. Manual prompting inevitably skips steps when you're in a hurry.

## Skill Structure

A well-structured skill has these components:

**Metadata block.** Name, description, version, author, tags. This is how people discover your skill. Write the description for someone who has never used it: what problem does it solve and what does it need to work?

**Trigger patterns.** Define the natural-language patterns that should activate this skill. Be specific enough to avoid false positives but broad enough to catch real user intent. "Check marketing performance" and "How are our ads doing" should both trigger the marketing health skill.

**Required tools and permissions.** Declare what connectors and tools the skill needs upfront. This lets Hermes verify availability before starting execution and gives users a clear understanding of what access they're granting.

**Step-by-step workflow.** Each step should be a discrete action: call a tool, transform data, validate output, present to user. Steps should be idempotent where possible. Use clear names so the execution trace is readable.

**Error handling per step.** For each tool call, define what to do on common failures. Timeout → retry once. Rate limit → back off and retry. Auth error → prompt user to re-authenticate. Data not found → present partial results with caveat.

**Output format specification.** Define the final presentation: table, chart, bullet list, executive summary. Include example output so users know what to expect.

## Testing Your Skill

**Unit test each step in isolation.** Can you run step 3 without steps 1 and 2 by providing mock data? If not, refactor until you can. Isolated steps are debuggable steps.

**Integration test the full workflow.** Run the skill end-to-end with real (or realistic test) data. Time it. Check the output format. Verify error handling by deliberately breaking one connector.

**Regression test after changes.** When you update a skill, re-run the full test suite. Skills that depend on external APIs can break silently when those APIs change. Schedule a weekly smoke test for production skills.

**Edge case testing.** Test with empty data, maximum data, malformed data, missing permissions. The skill should degrade gracefully in every case — partial results with clear caveats are better than cryptic errors.

## Documentation Patterns

**Every skill gets a README section.** What it does, what it needs, how to invoke it, what to expect. Include a screenshot or example output. This is what users read before installing.

**Inline comments in complex steps.** If a step has non-obvious logic (a regex that extracts a specific field, a calculation with domain-specific assumptions), document the "why" in a comment. The next maintainer will thank you.

**Changelog discipline.** When you update a skill, record what changed and why. Skills that silently change behavior break user trust. A changelog also helps users decide whether to update.

## Skill Lifecycle

**Draft.** The skill exists but hasn't been reviewed. It works for the author but may have rough edges. Label it clearly as draft.

**Beta.** The skill has been tested by the author and at least one other person. It handles common error cases. Ready for wider team use but may still evolve.

**Production.** The skill has been used for at least two weeks without modification. Error rates are known and acceptable. Documentation is complete. It's safe to rely on.

**Deprecated.** The skill still works but a better alternative exists. Add a deprecation notice pointing to the replacement. Remove after a migration window (typically 30-90 days).

**Archived.** The skill is no longer maintained or available. Remove from the active catalog but keep the source for reference.

## Community Contribution Guidelines

When publishing a skill for the Hermes community:

- Test it against the documented trigger patterns before publishing
- Remove all hardcoded values specific to your environment
- Provide a setup guide: what credentials, connectors, or configuration the user needs
- Include a sample invocation with expected output
- Use example.com domains and placeholder values — never publish real data
- Tag accurately: don't tag a skill as "production" if it's only been tested on one setup
- Respond to issues and update the skill when underlying APIs change

The best skills become community infrastructure. Treat skill authorship as a responsibility, not just a contribution.
