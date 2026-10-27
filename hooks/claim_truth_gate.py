"""Abort the docs build when a page asserts a claim we cannot substantiate.

Why this exists
---------------
scripts/validate_claim_truth.py already knew how to catch false public claims,
but nothing ran it: it was not in any workflow, and it only scanned the docs/
folder. On 2026-10-27 the page hermes/compare/corpusiq-vs-microsoft-copilot
shipped saying CorpusIQ "reads Microsoft Copilot" and that readers should
"connect Microsoft Copilot once" - while the corpusiq.io FAQ on the same domain
said Copilot has no MCP connector and CorpusIQ cannot plug into it. Two answers
to the same question, both public, published for months.

Why a build hook instead of a workflow step
-------------------------------------------
A workflow step only runs in CI, and the push credential for this repository has
no `workflow` scope, so a workflow-file change cannot be pushed from the agent
account at all. An MkDocs hook gets the same enforcement where it matters: the
Vercel deploy workflow runs `mkdocs build`, so a forbidden claim now fails the
build that produces the deployed site, plus every local build.

Behaviour
---------
on_config runs the gate once per build. Clean tree: returns the config and the
build continues. Any hit: raises SystemExit with the file, line and text, so the
build stops before deploying and the message names exactly what to rewrite.

Scope is whatever scripts/validate_claim_truth.py scans: every Markdown page in
the repository (code, build output and this hook's fixtures are skipped), for
affirmative directory-listing claims and platform-support claims, with the
negation escape so honest copy ("does not plug into Microsoft Copilot") passes.
"""

import importlib.util
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GATE_PATH = os.path.join(REPO, "scripts", "validate_claim_truth.py")


def _load_gate():
    spec = importlib.util.spec_from_file_location("validate_claim_truth", GATE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def on_config(config):
    gate = _load_gate()
    hits = []
    for path in gate.iter_targets():
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for lineno, line in gate.scan_text(text):
            hits.append("%s:%s: %s" % (os.path.relpath(path, REPO), lineno, line))
    if hits:
        raise SystemExit(
            "claim-truth gate: %d forbidden claim(s) - build aborted.\n"
            "CorpusIQ is not in Anthropic's Connector Directory, and Microsoft "
            "Copilot has no MCP connector, so neither can be claimed.\n%s\n"
            "Rewrite to the supported path, or drop the claim. "
            "Run: python3 scripts/validate_claim_truth.py" % (len(hits), "\n".join(hits[:25]))
        )
    return config
