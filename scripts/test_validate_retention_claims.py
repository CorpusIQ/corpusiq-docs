#!/usr/bin/env python3
"""Adversarial regression tests for the public retention-claim gate."""

from __future__ import annotations

import json
import re
import tempfile
import unittest
from pathlib import Path

from scripts import validate_retention_claims as validator
from scripts.feed_text import TRUNCATION_NOTICE, truncate_for_feed


class RetentionClaimValidatorTests(unittest.TestCase):
    def findings_for(self, text: str) -> list[validator.Finding]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs" / "index.md").write_text(text, encoding="utf-8")
            return validator.validate_repository(root)

    def test_rejects_known_blanket_claim_bypasses(self) -> None:
        claims = {
            "contraction": "MCP servers don't store data.",
            "curly_contraction": "MCP servers don’t store data.",
            "passive_contraction": "Customer data isn't stored.",
            "stores_no_data": "CorpusIQ stores no customer data.",
            "never_anything": (
                "CorpusIQ never retains anything; it does not retain raw customer "
                "files or full connector response payloads."
            ),
            "coordinated_nothing": "Nothing is copied, stored, or warehoused.",
            "nothing_copied": "Nothing is copied into a separate store.",
            "coordinated_never": "The MCP layer never aggregates or stores.",
            "zero_file_storage": "Zero file storage.",
            "reverse_table": "| Data Storage | ✅ Zero -- read-only OAuth |",
            "bold_reverse_table": "| **Data Storage** | ✅ Zero -- read-only OAuth |",
            "coordinated_no_data": "No data is moved, copied, or stored.",
            "qualified_financial": (
                "No financial data is persisted after a query completes."
            ),
            "no_data_cached": "No data cached.",
            "stores_no_information": "CorpusIQ stores no information.",
            "never_kept": "Customer data is never kept.",
            "do_not_save": "We do not save data.",
            "standalone_no_storage": "No storage. No training. Gone after response.",
            "transient_only": "Transient processing only.",
            "no_embedding_store": "No embedding store or secondary data store.",
            "logs_no_business_data": "Audit logs contain no business data.",
            "blanket_deletion": "All user data has been permanently deleted.",
            "keep_no_records": "We keep no customer records.",
            "save_nothing": "We don't save anything.",
            "records_not_written": "Customer records are not written to disk.",
            "context_only": "Your data exists only in the context window.",
            "immediate_delete": "Data is deleted immediately after each response.",
            "delete_information": "Permanently delete all customer information.",
            "full_deletion_now": "Full deletion with no waiting period.",
            "no_data_duplication": "No data duplication.",
            "no_copies": "No copies, no ETL.",
            "persistent": "No persistent business data storage.",
            "table": "| Data Storage | None -- ephemeral access |",
            "markdown_no": "**Q: Does this store my data?**\nNo. It uses scoped logs.",
            "html_no": (
                "<summary><strong>Is my data stored?</strong></summary>\n\n"
                "No. Scoped logs apply."
            ),
            "same_line_bold_no": "**Does this store data?** **No.** Scoped logs apply.",
            "scoped_suffix_bypass": (
                "CorpusIQ doesn't store data; it does not retain raw customer "
                "files or full connector response payloads."
            ),
            "never_leaves": "Data never leaves its source system.",
            "zero_records_variant": "We retain zero customer records.",
            "save_none_variant": "We save none of your information.",
            "keep_none_variant": "We keep none of your records.",
            "never_touches_disk": "Customer records never touch disk.",
            "response_disappears": "The response disappears immediately after answering.",
            "erase_every_record": "We erase every customer record after answering.",
            "second_copy": "No second copy of your data is created.",
            "vendor_stays": "Your CRM data stays in HubSpot.",
            "platform_stays": "Your store data stays in your platforms.",
            "no_copy_sync": "There is no copy to fall out of sync.",
            "without_duplication": "The layer works without data duplication.",
            "retention_none_table": "| Retention | None |",
            "retained_faq_no": "Is customer data retained? A: No, direct MCP is scoped.",
            "scoped_plus_blanket": (
                "Direct MCP doesn't retain raw customer files or full connector "
                "response payloads, or anything else."
            ),
            "ephemeral_design": "Direct retrieval is ephemeral by design.",
            "unqualified_training": "This prevents model training on customer data.",
            "soc_overclaim": "CorpusIQ provides SOC 2 compliance.",
            "immediate_deletion_endpoint": "Use the immediate deletion endpoint.",
            "zero_records_passive": "Zero customer records are retained.",
            "absolutely_no_records": "We retain absolutely no customer records.",
            "not_single_record": "Not a single customer record is retained.",
            "none_saved_short": "We save none.",
            "retention_colon_none": "**Retention:** None",
            "retention_yaml_none": "retention: none",
            "leaves_no_records": "Each request leaves no customer records behind.",
            "writes_nothing_disk": "The service writes nothing to disk.",
            "source_only_copy": "The source system remains the only copy of the data.",
            "stays_where_it_is": "The data stays where it is.",
            "never_crosses_boundary": "Customer content never crosses the corporate boundary.",
            "all_processing_in_region": "All data processing stays in your Microsoft 365 region.",
            "faq_retention_no": "Is any customer data retained? A: No. Logs are scoped.",
            "scoped_composition": (
                "Direct MCP does not retain raw customer files or full connector "
                "response payloads and keeps nothing else."
            ),
            "training_never": "Your information never trains a model.",
            "training_no_content": "No customer content enters model training.",
            "training_prevented": "The architecture prevents model training on customer data.",
            "soc_ready": "CorpusIQ is SOC 2 ready.",
            "soc_type_two": "CorpusIQ is SOC 2 Type 2 certified.",
            "soc_attested": "CorpusIQ has a SOC 2 attestation.",
            "instant_purge": "Customer information is purged instantly.",
            "response_erase": "Records are erased as soon as the response completes.",
            "gone_moment": "Your data is gone the moment the answer is returned.",
            "maintain_zero": "CorpusIQ maintains zero customer records.",
            "none_remain": "No customer records remain after the response.",
            "zero_days": "Retention period: 0 days.",
            "stored_none": "Stored duration: none.",
            "zero_seconds": "Customer data is kept for zero seconds.",
            "nothing_survives": "Nothing survives between requests.",
            "leaves_no_trace": "Each query leaves no data trace.",
            "never_persisted_anywhere": "Customer information is never persisted anywhere.",
            "source_exclusive": "Your records remain exclusively in the source system.",
            "never_exits_tenant": "Customer data never exits your tenant.",
            "customer_environment_only": "Processing occurs solely in the customer environment.",
            "no_region_crossing": "No customer data crosses the regional boundary.",
            "faq_absolutely_not": "Does CorpusIQ retain customer data? Absolutely not.",
            "faq_never": "Do you keep copies of customer records? Never.",
            "scoped_nothing_stored": (
                "Direct MCP does not retain raw customer files or full connector "
                "response payloads; nothing else is stored."
            ),
            "no_learning": "We do not learn from customer data.",
            "no_model_improvement": "Customer content is never used to improve models.",
            "prompts_excluded": "Your prompts are excluded from model training.",
            "soc_audited": "CorpusIQ is SOC 2 audited and verified.",
            "soc_assured": "CorpusIQ is SOC 2 assured.",
            "delete_without_delay": "Customer records are removed without delay.",
            "wiped_immediately": "Customer information is wiped immediately.",
            "blanket_no_index": "CorpusIQ does not index customer data.",
            "blanket_no_indexing": "No indexing. No embeddings. Just live answers.",
            "blanket_no_pipeline": "There is no indexing pipeline or stale index.",
            "preserve_no_information": "We preserve no customer information.",
            "nothing_remains": "Nothing remains on our servers.",
            "source_solely": "Customer records remain solely in Salesforce.",
            "records_feed_no_model": "Records do not feed any model.",
            "nothing_indexed": "Nothing is indexed.",
            "closing_removes_trace": "Closing the account removes every trace.",
            "faq_html_no": "Do you retain records? <p>No</p>",
            "scoped_composed_zero": (
                "Direct MCP does not retain raw customer files or full connector "
                "response payloads; no other records remain."
            ),
        }
        for label, claim in claims.items():
            with self.subTest(label=label):
                self.assertTrue(self.findings_for(claim))

    def test_allows_precisely_scoped_direct_mcp_claim(self) -> None:
        claim = (
            "Direct MCP does not retain raw customer files or full connector "
            "response payloads. Operational logs are retained for up to 30 days."
        )
        self.assertEqual(self.findings_for(claim), [])

    def test_allows_truthful_soc_and_training_qualification(self) -> None:
        claim = (
            "CorpusIQ maintains a SOC 2 aligned posture; formal SOC 2 Type II "
            "certification is not claimed. CorpusIQ does not train models on customer "
            "data; conversation handling follows the selected AI provider's plan and "
            "settings."
        )
        self.assertEqual(self.findings_for(claim), [])

    def test_allows_direct_mcp_index_scope_with_optional_mode(self) -> None:
        claim = (
            "Direct MCP does not build embeddings or file indexes; optional indexed "
            "search separately retains embeddings and minimal metadata until revocation "
            "or account deletion."
        )
        self.assertEqual(self.findings_for(claim), [])

    def test_allows_legitimate_cost_compliance_and_provider_controls(self) -> None:
        controls = (
            "No data storage cost is added to your invoice.",
            "CorpusIQ is preparing for SOC 2 certification.",
            "CorpusIQ does not use customer data to train models; conversation handling "
            "follows the selected AI provider's plan and settings.",
            "Direct MCP does not retain raw customer files or full connector response "
            "payloads; operational logs may persist for up to 30 days.",
        )
        for control in controls:
            with self.subTest(control=control):
                self.assertEqual(self.findings_for(control), [])

    def test_broad_semantic_matrix_rejects_forbidden_claims_and_allows_controls(
        self,
    ) -> None:
        matrix_path = Path(__file__).with_name("retention_claim_probe_matrix.json")
        matrix = json.loads(matrix_path.read_text(encoding="utf-8"))

        for family, probes in matrix["forbidden_families"].items():
            for probe in probes:
                with self.subTest(family=family, label=probe["label"]):
                    self.assertTrue(self.findings_for(probe["text"]))

        for control in matrix["legitimate_controls"]:
            with self.subTest(control=control["label"]):
                self.assertEqual(self.findings_for(control["text"]), [])

    def test_broad_semantic_probes_cannot_bypass_validation_in_tables(self) -> None:
        matrix_path = Path(__file__).with_name("retention_claim_probe_matrix.json")
        matrix = json.loads(matrix_path.read_text(encoding="utf-8"))

        for family, probes in matrix["forbidden_families"].items():
            for probe in probes:
                table = (
                    "| Control | Claim |\n"
                    "|---|---|\n"
                    f"| {family} | {probe['text']} |\n"
                )
                with self.subTest(family=family, label=probe["label"]):
                    self.assertTrue(self.findings_for(table))

    def test_scans_mkdocs_metadata_and_corpusiq_hermes_pages(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "mkdocs.yml").write_text(
                'site_name: CorpusIQ\nsite_description: "Zero customer data storage"\n'
                "nav:\n"
                "  - Case Study: hermes/outputs/case-studies/example.md\n"
                "  - Generic Agent: hermes/agents/example.md\n"
                "  - Local Advice: hermes/best-practices/local.md\n",
                encoding="utf-8",
            )
            hermes_page = root / "hermes" / "setup" / "corpusiq-mcp.md"
            hermes_page.parent.mkdir(parents=True)
            hermes_page.write_text(
                "CorpusIQ stores no information.\n", encoding="utf-8"
            )
            rendered_output = (
                root / "hermes" / "outputs" / "by-company-size" / "enterprise.md"
            )
            rendered_output.parent.mkdir(parents=True)
            rendered_output.write_text(
                "CorpusIQ is SOC 2 Type 2 certified.\n", encoding="utf-8"
            )
            nav_output = root / "hermes" / "outputs" / "case-studies" / "example.md"
            nav_output.parent.mkdir(parents=True)
            nav_output.write_text("Customer records are retained for zero days.\n")
            generic_agent = root / "hermes" / "agents" / "example.md"
            generic_agent.parent.mkdir(parents=True)
            generic_agent.write_text("CorpusIQ stores no customer information.\n")
            unlisted_page = root / "hermes" / "community" / "unlisted.md"
            unlisted_page.parent.mkdir(parents=True)
            unlisted_page.write_text(
                "CorpusIQ stores no customer information.\n", encoding="utf-8"
            )
            local_advice = root / "hermes" / "best-practices" / "local.md"
            local_advice.parent.mkdir(parents=True)
            local_advice.write_text(
                "A local password manager never stores secrets in agent memory.\n"
            )

            findings = validator.validate_repository(root)

        paths = {str(finding.path) for finding in findings}
        self.assertIn("mkdocs.yml", paths)
        self.assertIn("hermes/setup/corpusiq-mcp.md", paths)
        self.assertIn("hermes/outputs/by-company-size/enterprise.md", paths)
        self.assertIn("hermes/outputs/case-studies/example.md", paths)
        self.assertIn("hermes/agents/example.md", paths)
        self.assertIn("hermes/community/unlisted.md", paths)
        self.assertNotIn("hermes/best-practices/local.md", paths)

    def test_feed_truncation_uses_a_complete_boundary_and_notice(self) -> None:
        body = (
            "First complete paragraph.\n\n"
            "## Complete heading\n"
            "| Column A | Column B |\n"
            "|---|---|\n"
            "| complete | row |\n"
            "[complete link](https://example.com/complete)\n"
            + ("unfinished-link-[label](https://example.com/very-long-path " * 10)
        )
        truncated = truncate_for_feed(body, limit=180)

        self.assertIn(TRUNCATION_NOTICE, truncated)
        self.assertTrue(truncated.startswith("First complete paragraph."))
        excerpt = truncated.split(TRUNCATION_NOTICE)[0].rstrip()
        self.assertTrue(
            excerpt.endswith("[complete link](https://example.com/complete)")
        )
        self.assertEqual(excerpt.count("["), excerpt.count("]"))
        self.assertEqual(excerpt.count("("), excerpt.count(")"))
        self.assertEqual(truncate_for_feed("short body", limit=80), "short body")

    def test_feed_truncation_backs_off_incomplete_markdown_blocks(self) -> None:
        prefix = (
            "First complete paragraph with enough context to stay beyond the "
            "minimum structural-boundary window."
        )
        cases = {
            "orphan-heading": (
                prefix + "\n\n## Related Pages\n\n" + ("later text " * 80),
                180,
            ),
            "open-details": (
                prefix
                + "\n\n<details>\n<summary>Can I use this?</summary>\n\n"
                + ("later text " * 80),
                180,
            ),
            "open-fence": (
                prefix + "\n```python\nprint('unfinished')\n" + ("later text " * 80),
                180,
            ),
            "partial-table": (
                prefix
                + "\n\n| A | B |\n|---|---|\n| one | two |\n"
                + ("later text " * 80),
                250,
            ),
        }
        for label, (body, limit) in cases.items():
            with self.subTest(label=label):
                truncated = truncate_for_feed(body, limit=limit)
                excerpt = truncated.split(TRUNCATION_NOTICE)[0].rstrip()
                self.assertEqual(excerpt, prefix)
                self.assertIn(TRUNCATION_NOTICE, truncated)

    def test_generated_full_feed_has_no_incomplete_truncation_blocks(self) -> None:
        feed = Path("llms-full.txt").read_text(encoding="utf-8")
        notices = list(re.finditer(re.escape(TRUNCATION_NOTICE), feed))
        self.assertGreater(len(notices), 0)
        failures: list[str] = []
        for notice in notices:
            section_start = feed.rfind("\n---\n# ", 0, notice.start())
            section = feed[section_start + 1 : notice.start()].rstrip()
            tail = section.splitlines()[-1].strip() if section.splitlines() else ""
            if re.match(r"^#{1,6}\s", tail):
                failures.append(f"orphan heading: {tail}")
            if re.match(r"^(?:---+|\*\*\*+|___+)$", tail):
                failures.append(f"orphan thematic break: {tail}")
            if re.match(r"^<summary\b", tail, re.IGNORECASE):
                failures.append(f"orphan summary: {tail}")
            if tail.startswith("|") and tail.endswith("|"):
                failures.append(f"partial table: {tail}")
            if section.count("```") % 2 or section.count("~~~") % 2:
                failures.append("open code fence")
            if len(re.findall(r"<details\b", section, re.IGNORECASE)) != len(
                re.findall(r"</details>", section, re.IGNORECASE)
            ):
                failures.append("open details block")
        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
