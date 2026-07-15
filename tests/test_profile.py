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
TAGLINE_PATH = ROOT / "assets/noxen-tagline-typewriter.svg"
TAGLINE = TAGLINE_PATH.read_text(encoding="utf-8")
DOCS_SVG_PATH = ROOT / "docs/noxen-index.svg"
DOCS_SVG = DOCS_SVG_PATH.read_text(encoding="utf-8")

BANNED = [
    "SYSTEM ONLINE", "SIGNAL", "UNKNOWN ORIGIN", "ACCESS GRANTED",
    "ENTER THE SPACE", "three.min.js", "<canvas", "linearGradient",
    "radialGradient", "visitor counter", "skill bar", "glow",
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
        combined = README + HTML + SVG + TAGLINE
        for phrase in BANNED:
            self.assertNotIn(phrase.lower(), combined.lower(), phrase)

    def test_readme_is_compact_and_uses_two_svg_layers(self):
        self.assertIn("./assets/noxen-index.svg", README)
        self.assertIn("./assets/noxen-tagline-typewriter.svg", README)
        self.assertNotIn("<code>reverse engineering</code>", README)
        self.assertLess(len(README.splitlines()), 60)
        self.assertIn("keep the useful part", README)
        self.assertIn("claude-cc-switch-bat", README)

    def test_svg_has_single_clean_signature_and_radar(self):
        root = ET.parse(SVG_PATH).getroot()
        self.assertTrue(root.tag.endswith("svg"))
        self.assertEqual(SVG.count('class="signature"'), 1)
        self.assertIn('pathLength="1"', SVG)
        self.assertIn("@keyframes signature-loop", SVG)
        self.assertIn("stroke-dasharray:1", SVG)
        self.assertIn('class="radar-arm"', SVG)
        self.assertIn("prefers-reduced-motion", SVG)
        self.assertNotIn("signature-under", SVG)
        self.assertNotIn('stroke-dasharray="2 8"', SVG)
        self.assertNotIn("M816 48V312", SVG)
        self.assertNotRegex(SVG, r"<animate(?:Transform)?\b")
        self.assertNotRegex(SVG, r"Gradient\b")

    def test_tagline_svg_is_centered_transparent_and_accessible(self):
        root = ET.parse(TAGLINE_PATH).getroot()
        self.assertTrue(root.tag.endswith("svg"))
        self.assertEqual(root.attrib.get("viewBox"), "0 0 1200 64")
        self.assertIn('x="336"', TAGLINE)
        self.assertIn('width="528"', TAGLINE)
        self.assertIn("@keyframes reveal", TAGLINE)
        self.assertIn("@keyframes caret-move", TAGLINE)
        self.assertIn("prefers-reduced-motion", TAGLINE)
        self.assertNotRegex(TAGLINE, r'<rect[^>]+width="1200"[^>]+fill=')
        self.assertNotRegex(TAGLINE, r"<script\b")

    def test_pages_site_uses_approved_signature_and_preserves_interactions(self):
        parser = LinkParser()
        parser.feed(HTML)
        self.assertEqual(parser.scripts, [])
        self.assertIn('src="./noxen-index.svg"', HTML)
        self.assertEqual(DOCS_SVG, SVG)
        self.assertNotIn('stroke-dasharray="2 8"', DOCS_SVG)
        self.assertNotIn("M816 48V312", DOCS_SVG)
        self.assertIn('id="coordinates"', HTML)
        self.assertIn('class="motion-layer"', HTML)
        self.assertIn("--mx", HTML)
        self.assertIn("animationend", HTML)
        self.assertIn("J", HTML.upper())
        self.assertIn("prefers-reduced-motion", HTML)

    def test_referenced_local_assets_exist(self):
        readme_refs = re.findall(r'(?:src|href)=["\'](\./[^"\']+)["\']', README)
        html_refs = re.findall(r'(?:src|href)=["\'](\./[^"\']+)["\']', HTML)
        for ref in readme_refs:
            target = ROOT / ref[2:]
            self.assertTrue(target.exists(), f"missing {target}")
        for ref in html_refs:
            target = ROOT / "docs" / ref[2:]
            self.assertTrue(target.exists(), f"missing {target}")

if __name__ == "__main__":
    unittest.main()
