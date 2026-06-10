# Contributing to CorpusIQ Docs

This repository is the community hub for CorpusIQ connector documentation, recipes, and examples.
Reference: github.com/CorpusIQ/corpusiq-docs

Contributions come in three forms: enhancement requests, recipes, and examples.
Each has a defined path. Follow it and your contribution ships faster.

If you are still shaping an early connector or feature idea, start in
[Community Discussions](community/README.md) so the team and other users can
ask questions and upvote the direction. Use this guide when you have a concrete
request, bug report, recipe, or tested example ready to track.

---

## Enhancement Requests

Use the issue tracker. Do not open freeform issues.

1. Go to https://github.com/CorpusIQ/corpusiq-docs/issues/new/choose
2. Select "Connector Enhancement Request"
3. Fill out every field — connector name, use case, current workaround, business impact
4. Apply the relevant `connector:` label (e.g. `connector:shopify`)

Enhancement requests without a clear use case and business impact will be deprioritized.
The CorpusIQ team reviews open enhancements weekly. Status moves through:
`status:reviewing` → `status:accepted` → `status:in-progress` → `status:shipped`

---

## Recipes

Recipes are reusable query patterns for CorpusIQ connectors. See `recipes/` for format.

To submit a recipe:

1. Fork this repository
2. Copy `recipes/TEMPLATE.md` to `recipes/<your-recipe-slug>.md`
3. Fill out all sections: title, connectors, use case, query, sample output, notes
4. Open a pull request targeting `main`
5. Title your PR: `recipe: <short description>`
6. Apply labels `type:recipe` and the relevant `connector:` labels

Recipes must use real connector field names. No placeholder schemas.
If your recipe spans multiple connectors, list all of them.

---

## Examples

Examples are runnable code samples — configs, scripts, integrations.
See `examples/` for existing examples.

To submit an example:

1. Fork this repository
2. Add your example as `examples/<your-example-name>.md`
3. Include: what it does, prerequisites, full working code or config, expected output
4. Open a pull request targeting `main`
5. Title your PR: `example: <short description>`
6. Apply label `type:example`

Examples must be tested. Do not submit untested configs or scripts.

---

## Bug Reports

Use the issue tracker.

1. Go to https://github.com/CorpusIQ/corpusiq-docs/issues/new/choose
2. Select "Bug Report"
3. Provide exact steps to reproduce, expected vs actual behavior, and your environment

---

## Style

- Be direct. Operators are reading this under time pressure.
- Avoid filler. Every sentence earns its place.
- Use real field names, real connector names, real queries.
- No marketing language in technical docs.

---

## Questions

Use GitHub Discussions, not issues:
https://github.com/CorpusIQ/corpusiq-docs/discussions

The [Community guide](community/README.md) explains which Discussion category to
use for Q&A, early ideas, announcements, and show-and-tell posts.
