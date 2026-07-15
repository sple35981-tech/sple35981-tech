from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
HTML = (ROOT / "docs/index.html").read_text(encoding="utf-8")
SVG_PATH = ROOT / "assets/noxen-index.svg"
SVG = SVG_PATH.read_text(encoding="utf-8")

BANNED = [
    "SYSTEM ONLINE", "SIGNAL", "UNKNOWN ORIGIN", "ACCESS GRANTED",
    "ENTER THE SPACE", "three.min.js", "<canvas", "linearGradient",
    "radialGradient", "<animate", "visitor counter", "skill bar",
]

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.scripts = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "a" and data.get("href"):
            self.links.append(data["href"])
        if tag == "script" and data.get("src"):
            self.scripts.append(data["src"])

class ProfileTests(unittest.TestCase):
    def test_old_ai_profile_language_and_effects_are_absent(self):
        combined = README + HTML + SVG
        for phrase in BANNED:
            self.assertNotIn(phrase.lower(), combined.lower(), phrase)

    def test_readme_is_compact_and_points_to_new_cover(self):
        self.assertIn("./assets/noxen-index.svg", README)
        self.assertLess(len(README.splitlines()), 60)
        self.assertIn("keep the useful part", README)
        self.assertIn("claude-cc-switch-bat", README)

    def test_svg_is_valid_static_monochrome_artwork(self):
        root = ET.parse(SVG_PATH).getroot()
        self.assertTrue(root.tag.endswith("svg"))
        self.assertIn("Noxen", SVG)
        self.assertNotRegex(SVG, r"<animate(?:Transform)?\\b")
        self.assertNotRegex(SVG, r"Gradient\\b")

    def test_pages_site_has_no_external_script_dependency(self):
        parser = LinkParser(); parser.feed(HTML)
        self.assertEqual(parser.scripts, [])
        self.assertTrue(any("claude-cc-switch-bat" in link for link in parser.links))
        self.assertIn("J / K TO MOVE", HTML)
        self.assertIn("prefers-reduced-motion", HTML)

    def test_referenced_local_assets_exist(self):
        refs = re.findall(r'(?:src|href)=["\\'](\\.?\\.?/[^"\\']+)["\\']', README + HTML)
        for ref in refs:
            if ref.startswith("./"):
                target = ROOT / ref[2:]
                self.assertTrue(target.exists(), f"missing {target}")

if __name__ == "__main__":
    unittest.main()
