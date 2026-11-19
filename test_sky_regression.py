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

    def test_chem_exam_rush_page_nav_layers_and_print(self):
        rush_path = ROOT / "g8_chem_exam_rush.html"
        self.assertTrue(rush_path.exists(), "Missing g8_chem_exam_rush.html")
        html = rush_path.read_text(encoding="utf-8")
        self.assertIn(f"{CANONICAL_HOST}/ecosystem-nav.js", html)
        self.assertIn(f"{CANONICAL_HOST}/ecosystem-nav.css", html)
        self.assertRegex(html, r'<igcse-nav\b[^>]*\bactive="sky"[^>]*\bsticky\b[^>]*>')
        self.assertRegex(html, r"#chem-fullscreen-overlay\s*\{[^}]*z-index:\s*100000\s*;")
        self.assertRegex(html, r"\.mock-sticky-bar\s*\{[^}]*top:\s*52px\s*;")
        self.assertIn("@media print", html)
        self.assertIn("print-blank-paper", html)
        self.assertIn("print-answer-key", html)

        index_html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="g8_chem_exam_rush.html"', index_html)

    def test_chem_u2_bank_expansion_citations_and_mock_papers(self):
        chem = json.loads((ROOT / "g8_chemistry_u2_exercises.json").read_text(encoding="utf-8"))
        bio1 = json.loads((ROOT / "g8_science_exercises_bilingual.json").read_text(encoding="utf-8"))
        bio2 = json.loads((ROOT / "g8_science_part2_exercises_bilingual.json").read_text(encoding="utf-8"))

        self.assertGreaterEqual(len(chem), 120)
        all_ids = [x["id"] for x in (chem + bio1 + bio2)]
        self.assertEqual(len(all_ids), len(set(all_ids)), "Global IDs must be 100% unique")

        for item in chem:
            self.assertTrue(item.get("answer_en"), f"Empty answer_en on {item['id']}")
            self.assertTrue(item.get("answer_cn"), f"Empty answer_cn on {item['id']}")
            if item.get("game_type") == "mcq" and item.get("source_tag") != "baseline":
                self.assertEqual(len(item.get("options", [])), 4, f"Bad options on {item['id']}")
                self.assertIn(item.get("correct_letter"), {"A", "B", "C", "D"})

        wb_pdf_items = [
            x for x in chem
            if "G8_U2_Acids_and_Bases_Workbook_PDF.pdf" in x.get("citation_textbook", "")
            and re.search(r"p\.\d+", x.get("citation_textbook", ""))
        ]
        sm_orig = [x for x in chem if x.get("source_tag") == "school_mistake"]
        sm_var = [x for x in chem if x.get("source_tag") == "school_mistake_variant"]
        self.assertGreaterEqual(len(wb_pdf_items), 30)
        self.assertEqual(len(sm_orig), 30)
        self.assertEqual(len(sm_var), 60)

        mock_js = (ROOT / "g8_chem_mock_papers.js").read_text(encoding="utf-8")
        self.assertIn("paperA:", mock_js)
        self.assertIn("paperB:", mock_js)
        self.assertIn("part1_mcq:", mock_js)
        self.assertIn("part2_calc:", mock_js)
        self.assertIn("part3_theory:", mock_js)

    def test_no_nitric_acid_metal_hydrogen_misconception(self):
        chem = json.loads((ROOT / "g8_chemistry_u2_exercises.json").read_text(encoding="utf-8"))
        metals = ("zinc", "magnesium", "iron", "aluminium", "calcium", "metal")
        for item in chem:
            prompt_l = str(item.get("prompt_en", "")).lower()
            ans_l = str(item.get("answer_en", "")).lower()
            if "nitric acid" in prompt_l and any(m in prompt_l for m in metals):
                self.assertNotIn(
                    "hydrogen",
                    ans_l,
                    f"Scientific misconception in {item['id']}: metal + nitric acid must NOT yield hydrogen",
                )

    def test_no_cloze_placeholder_leak_in_chem_bank(self):
        chem = json.loads((ROOT / "g8_chemistry_u2_exercises.json").read_text(encoding="utf-8"))
        placeholder_re = re.compile(r"\{b\d+\}")
        for item in chem:
            for field in ("answer_en", "answer_cn", "prompt_en", "prompt_cn", "rationale_en", "rationale_cn"):
                val = str(item.get(field, ""))
                self.assertIsNone(
                    placeholder_re.search(val),
                    f"Unresolved placeholder found in {item['id']}.{field}: {val[:80]}",
                )

    def test_all_chem_mcqs_options_breakdown_dict_schema(self):
        chem = json.loads((ROOT / "g8_chemistry_u2_exercises.json").read_text(encoding="utf-8"))
        mcqs = [x for x in chem if x.get("game_type") == "mcq"]
        self.assertGreaterEqual(len(mcqs), 150)
        for item in mcqs:
            bd = item.get("options_breakdown")
            self.assertIsInstance(bd, dict, f"{item['id']} options_breakdown must be dict")
            for letter in ("A", "B", "C", "D"):
                self.assertIn(letter, bd, f"{item['id']} options_breakdown missing key {letter}")
                entry = bd[letter]
                self.assertIsInstance(entry, dict, f"{item['id']} options_breakdown[{letter}] must be dict")
                self.assertTrue(entry.get("en"), f"{item['id']} options_breakdown[{letter}].en empty")
                self.assertTrue(entry.get("cn"), f"{item['id']} options_breakdown[{letter}].cn empty")
                self.assertIsInstance(entry.get("correct"), bool, f"{item['id']} options_breakdown[{letter}].correct must be bool")


if __name__ == "__main__":
    unittest.main()
