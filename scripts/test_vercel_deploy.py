"""Exercise the workflow's actual packaging commands without deploying."""

import json
from pathlib import Path
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
            (site / "index.html").write_text("<h1>Built docs</h1>")
            for name in ("vercel.json", "llms.txt", "llms-full.txt"):
                shutil.copyfile(ROOT / name, root / name)
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


if __name__ == "__main__":
    unittest.main()
