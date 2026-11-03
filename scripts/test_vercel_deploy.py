"""Exercise the workflow's actual packaging commands without deploying."""

import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]


class VercelDeployTests(unittest.TestCase):
    def test_uploaded_site_contains_output_config_routes_and_feeds(self):
        workflow = yaml.safe_load(
            (ROOT / ".github/workflows/vercel-deploy.yml").read_text()
        )
        steps = workflow["jobs"]["deploy"]["steps"]
        build = next(i for i, step in enumerate(steps) if step["name"] == "Build site")
        deploy = next(
            i for i, step in enumerate(steps)
            if step["name"] == "Deploy to Vercel production"
        )
        # The CLI treats site/, not the repository, as its project root.
        self.assertIn("deploy site", steps[deploy]["run"])
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            site = root / "site"
            site.mkdir()
            (site / "index.html").write_text(
                '<html><head><link rel="canonical" '
                'href="https://www.corpusiq.io/docs/"></head>'
                "<body><h1>Built docs</h1></body></html>"
            )
            for name in ("vercel.json", "llms.txt", "llms-full.txt"):
                shutil.copyfile(ROOT / name, root / name)
            # The no-slash gate and the asset stabilizer both run from the repo
            # root; give the harness its own copies so the packaging steps run
            # exactly as the workflow defines them.
            (root / "scripts").mkdir()
            for script in ("normalize_site_no_slash.py", "stabilize_hashed_assets.py"):
                shutil.copyfile(
                    ROOT / "scripts" / script,
                    root / "scripts" / script,
                )
            for step in steps[build + 1:deploy]:
                subprocess.run(
                    ["bash", "-e", "-c", step["run"]], cwd=root, check=True
                )
            config_path = site / "vercel.json"
            self.assertTrue(
                config_path.is_file(),
                "deploy site omits repository vercel.json; Vercel defaults to public",
            )
            config = json.loads(config_path.read_text())
            self.assertEqual(config["outputDirectory"], ".")
            self.assertTrue((site / config["outputDirectory"] / "index.html").is_file())
            # Preserve all redirects/asset rewrites as well as the output override.
            self.assertEqual(config, json.loads((ROOT / "vercel.json").read_text()))
            self.assertTrue(config["rewrites"])
            self.assertTrue(config["redirects"])
            for name in ("llms.txt", "llms-full.txt"):
                self.assertEqual((site / name).read_bytes(), (ROOT / name).read_bytes())


# ---------------------------------------------------------------------------
# Setup hub link contract
#
# Production runs with ``trailingSlash: false`` and normalize_site_no_slash
# strips the trailing slash, so the setup hub is served at ``/hermes/setup``.
# A relative markdown link such as ``[Session Cleanup](session-cleanup)`` is
# then resolved by the browser against ``/hermes/`` and becomes
# ``/hermes/session-cleanup`` - for the body link and for the generated
# MkDocs sidebar alike.
#
# Every setup page therefore needs an explicit
# ``/hermes/<slug> -> /hermes/setup/<slug>`` redirect in ``vercel.json``.
# The session cleanup page shipped without its entry (e7ccecd) and its nav
# link 404'd while the page itself returned 200. These assertions lock the
# contract so the next setup page cannot repeat it.
# ---------------------------------------------------------------------------

SETUP_DIR = ROOT / "hermes" / "setup"
SETUP_HUB = SETUP_DIR / "index.md"

# [text](target) - anchors, absolute paths and external URLs are not relative.
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


class SetupHubRedirectTests(unittest.TestCase):
    def redirects(self):
        config = json.loads((ROOT / "vercel.json").read_text())
        return [item for item in config.get("redirects", []) if isinstance(item, dict)]

    def relative_hub_links(self):
        targets = set()
        for raw in MD_LINK.findall(SETUP_HUB.read_text()):
            target = raw.split("#", 1)[0].split("?", 1)[0]
            if not target or target.startswith(("/", "http://", "https://", "mailto:")):
                continue
            targets.add(target.rstrip("/"))
        return targets

    def setup_page_slugs(self):
        return {
            path.stem
            for path in SETUP_DIR.glob("*.md")
            if path.stem not in {"index", "README"}
        }

    def test_every_relative_hub_link_has_a_production_redirect(self):
        sources = {item.get("source"): item for item in self.redirects()}
        missing = [
            f"/hermes/{slug} -> /hermes/setup/{slug}"
            for slug in sorted(self.relative_hub_links())
            if sources.get(f"/hermes/{slug}", {}).get("destination")
            != f"/hermes/setup/{slug}"
        ]
        self.assertEqual(
            missing,
            [],
            "relative links on the setup hub resolve to /hermes/<slug> on "
            "production; add these redirects to vercel.json: " + ", ".join(missing),
        )

    def test_every_setup_page_is_reachable_from_the_hub_url_shape(self):
        sources = {item.get("source"): item for item in self.redirects()}
        missing = [
            f"/hermes/{slug} -> /hermes/setup/{slug}"
            for slug in sorted(self.setup_page_slugs())
            if sources.get(f"/hermes/{slug}", {}).get("destination")
            != f"/hermes/setup/{slug}"
        ]
        self.assertEqual(
            missing,
            [],
            "setup pages without a hub redirect are unreachable from the "
            "sidebar and hub body links: " + ", ".join(missing),
        )

    def test_setup_redirect_targets_still_exist(self):
        broken = [
            f"{item['source']} -> {item['destination']}"
            for item in self.redirects()
            if str(item.get("destination", "")).startswith("/hermes/setup/")
            and not (
                SETUP_DIR / f"{item['destination'].rsplit('/', 1)[-1]}.md"
            ).is_file()
        ]
        self.assertEqual(
            broken,
            [],
            "redirects pointing at setup pages that no longer exist: "
            + ", ".join(broken),
        )

    def test_redirect_sources_are_unique(self):
        seen, duplicates = set(), []
        for item in self.redirects():
            source = item.get("source")
            if source in seen:
                duplicates.append(str(source))
            seen.add(source)
        self.assertEqual(
            duplicates, [], "duplicate redirect sources: " + ", ".join(duplicates)
        )


if __name__ == "__main__":
    unittest.main()
