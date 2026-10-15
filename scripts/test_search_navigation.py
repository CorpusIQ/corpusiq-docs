"""Material must resolve search against directory URLs, even without a slash.

Render the real override with a minimal parent and execute its inline scripts in
Node. No browser dependencies or MkDocs installation needed for this CI gate.
The browser acceptance additionally exercises the full generated site.
"""
import json
from pathlib import Path
import re
import subprocess
import unittest

from jinja2 import DictLoader, Environment

ROOT = Path(__file__).resolve().parents[1]


class SearchNavigationTests(unittest.TestCase):
    def render_scripts(self):
        env = Environment(loader=DictLoader({
            "main.html": (ROOT / "docs/overrides/main.html").read_text(),
            "base.html": '{% block scripts %}<script src="bundle.js"></script>{% endblock %}',
        }))
        html = env.get_template("main.html").render()
        # Only code before the bundle can influence Material initialization.
        return "\n".join(re.findall(r"<script>(.*?)</script>", html.split('<script src="bundle.js"')[0], re.S))

    def test_search_urls_keep_the_mount_path(self):
        script = self.render_scripts()
        for mount in ("https://www.corpusiq.io/docs", "https://docs.corpusiq.io", "http://localhost:8000/staging"):
            for path, base, worker in (("", ".", "assets/worker.js"), ("/api/authentication", "../..", "../../assets/worker.js")):
                for slash in ("", "/", "/index.html"):
                    url = mount + path + slash + "?h=authentication#authentication"
                    config = {"base": base, "search": worker, "features": ["search.highlight"]}
                    program = f'''
const location = new URL({json.dumps(url)});
const element = {{textContent: JSON.stringify({json.dumps(config)})}};
const document = {{getElementById: () => element}};
{script}
const config = JSON.parse(element.textContent);
const base = new URL(config.base, location);
console.log(JSON.stringify({{
  result: new URL("api/authentication/?h=authentication#authentication", base).href,
  index: new URL("search/search_index.json", base).href,
  worker: new URL(config.search, location).href,
  features: config.features
}}));
'''
                    with self.subTest(url=url):
                        run = subprocess.run(["node", "-e", program], capture_output=True, text=True, check=True)
                        actual = json.loads(run.stdout)
                        self.assertEqual(actual["result"], mount + "/api/authentication/?h=authentication#authentication")
                        self.assertEqual(actual["index"], mount + "/search/search_index.json")
                        self.assertEqual(actual["worker"], mount + "/assets/worker.js")
                        self.assertEqual(actual["features"], config["features"])


if __name__ == "__main__":
    unittest.main()
