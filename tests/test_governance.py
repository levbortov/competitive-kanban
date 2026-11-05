"""M00 repository governance smoke checks (Python stdlib only)."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = (
    "README.md",
    "CONTRIBUTING.md",
    "docs/VISION.md",
    "docs/RATING-001.md",
    "docs/GOVERNANCE-001.md",
    "docs/ARCHITECTURE.md",
    "docs/ROADMAP.md",
    "docs/adr/README.md",
    "docs/adr/0001-modular-monolith.md",
    ".github/ISSUE_TEMPLATE/feature.yml",
    ".github/ISSUE_TEMPLATE/bug.yml",
    ".github/ISSUE_TEMPLATE/tech-debt.yml",
    ".github/pull_request_template.md",
    ".github/workflows/governance.yml",
)


class GovernanceTests(unittest.TestCase):
    def test_required_files_exist(self):
        missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
        self.assertEqual(missing, [], f"Missing governance files: {missing}")

    def test_rating_invariants_are_documented(self):
        content = (ROOT / "docs/RATING-001.md").read_text(encoding="utf-8")
        for token in ("0.70", "0.30", "Q >= 80", "18 | 21 | 24 | 27 | 30",
                      "1000 Elo", "24h", "72h", "one match"):
            with self.subTest(token=token):
                self.assertIn(token, content)

    def test_explicit_acceptance_rule(self):
        content = (ROOT / "docs/GOVERNANCE-001.md").read_text(encoding="utf-8")
        self.assertIn("explicit acceptance before merge", content)

    def test_issue_templates_have_required_fields(self):
        for name in ("feature", "bug", "tech-debt"):
            with self.subTest(name=name):
                text = (ROOT / f".github/ISSUE_TEMPLATE/{name}.yml").read_text(encoding="utf-8")
                self.assertIn("body:", text)
                self.assertIn("required: true", text)


if __name__ == "__main__":
    unittest.main()
