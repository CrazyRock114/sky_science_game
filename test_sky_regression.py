import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CANONICAL_HOST = "https://" + "www." + "igcse.xyz"
LEGACY_HOST = "https://" + "igcse.xyz"


class TestSkyRegressionVaccines(unittest.TestCase):
    """Static regression vaccines for Sky (W1-SKY-01 & core baselines)."""

    def test_reactivity_hidpi_and_raf_lifecycle(self):
        app_js = (ROOT / "reactivity" / "app.js").read_text(encoding="utf-8")
        self.assertIn("devicePixelRatio", app_js)
        self.assertIn("Math.min(window.devicePixelRatio || 1, 2)", app_js)
        self.assertIn("let animationFrameId = null", app_js)
        self.assertIn("cancelAnimationFrame(animationFrameId)", app_js)
        self.assertIn("visibilitychange", app_js)
        self.assertIn("setupHiDPICanvas", app_js)

    def test_reactivity_25_metals_order_intact(self):
        app_js = (ROOT / "reactivity" / "app.js").read_text(encoding="utf-8")
        symbols = re.findall(r'symbol:\s*"([A-Za-z]+)"', app_js)
        expected = [
            "K", "Na", "Li", "Ba", "Sr", "Ca",
            "Mg", "Al", "Mn", "Zn", "Cr", "Fe", "Cd", "Co", "Ni", "Sn", "Pb",
            "H",
            "Sb", "Bi", "Cu", "Hg", "Ag", "Au", "Pt",
        ]
        self.assertEqual(symbols, expected)
        self.assertEqual(len(symbols), 25)

    def test_main_html_unified_ecosystem_nav_and_sticky(self):
        main_pages = ["index.html", "exercise_lab.html", "g8_exam_rush.html"]
        for page in main_pages:
            html = (ROOT / page).read_text(encoding="utf-8")
            self.assertIn(
                f"{CANONICAL_HOST}/ecosystem-nav.js",
                html,
                f"{page} missing {CANONICAL_HOST}/ecosystem-nav.js",
            )
            self.assertIn(
                f"{CANONICAL_HOST}/ecosystem-nav.css",
                html,
                f"{page} missing {CANONICAL_HOST}/ecosystem-nav.css",
            )
            self.assertNotIn(
                f"{LEGACY_HOST}/ecosystem-nav.",
                html,
                f"{page} still references non-www {LEGACY_HOST}/ecosystem-nav.*",
            )
            self.assertRegex(
                html,
                r'<igcse-nav\b[^>]*\bactive="sky"[^>]*\bsticky\b[^>]*>',
                f'{page} missing sticky attribute on <igcse-nav active="sky">',
            )

    def test_g8_exam_rush_fullscreen_overlay_z_index(self):
        html = (ROOT / "g8_exam_rush.html").read_text(encoding="utf-8")
        match = re.search(r"#confetti-canvas\s*\{[^}]*z-index:\s*(\d+)\s*;", html)
        self.assertIsNotNone(match, "#confetti-canvas z-index rule not found")
        self.assertGreaterEqual(int(match.group(1)), 100000)

    def test_stale_root_ecosystem_nav_copies_removed(self):
        self.assertFalse((ROOT / "ecosystem-nav.js").exists())
        self.assertFalse((ROOT / "ecosystem-nav.css").exists())

    def test_267_exercises_ids_unique(self):
        p1 = json.loads((ROOT / "g8_science_exercises_bilingual.json").read_text(encoding="utf-8"))
        p2 = json.loads((ROOT / "g8_science_part2_exercises_bilingual.json").read_text(encoding="utf-8"))
        all_items = p1 + p2
        ids = [item["id"] for item in all_items]
        self.assertEqual(len(all_items), 267)
        self.assertEqual(len(set(ids)), 267)

    def test_inquiry_pages_nav_and_homepage_mount(self):
        inquiry_pages = [
            "inquiry/index.html",
            "inquiry/acidic-water/index.html",
            "inquiry/ammonia-smell/index.html",
        ]
        for rel in inquiry_pages:
            p = ROOT / rel
            self.assertTrue(p.exists(), f"Missing {rel}")
            html = p.read_text(encoding="utf-8")
            self.assertIn(f"{CANONICAL_HOST}/ecosystem-nav.js", html)
            self.assertIn(f"{CANONICAL_HOST}/ecosystem-nav.css", html)
            self.assertRegex(
                html,
                r'<igcse-nav\b[^>]*\bactive="sky"[^>]*\bsticky\b[^>]*>',
                f'{rel} missing sticky attribute on <igcse-nav active="sky">',
            )

        index_html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="inquiry/"', index_html)

    def test_inquiry_simulations_hidpi_raf_and_css_layers(self):
        for rel in ["inquiry/acidic-water/app.js", "inquiry/ammonia-smell/app.js"]:
            js = (ROOT / rel).read_text(encoding="utf-8")
            self.assertIn("devicePixelRatio", js)
            self.assertIn("Math.min(window.devicePixelRatio || 1, 2)", js)
            self.assertIn("cancelAnimationFrame", js)
            self.assertIn("visibilitychange", js)

        css = (ROOT / "inquiry" / "inquiry.css").read_text(encoding="utf-8")
        self.assertRegex(css, r"\.inquiry-subbar\s*\{[^}]*top:\s*52px\s*;")
        self.assertRegex(css, r"z-index:\s*100000\s*;")


if __name__ == "__main__":
    unittest.main()
