"""Базовые проверки структуры M00 без сторонних Python-зависимостей."""

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
        self.assertEqual(missing, [], f"Отсутствуют документы: {missing}")

    def test_rating_invariants_are_documented(self):
        content = (ROOT / "docs/RATING-001.md").read_text(encoding="utf-8")
        for token in ("0.70", "0.30", "Q >= 80", "18 | 21 | 24 | 27 | 30",
                      "1000 Elo", "24", "72", "одном матче"):
            with self.subTest(token=token):
                self.assertIn(token, content)

    def test_explicit_acceptance_rule(self):
        content = (ROOT / "docs/GOVERNANCE-001.md").read_text(encoding="utf-8")
        self.assertIn("явной приёмки владельца продукта", content)

    def test_issue_templates_have_required_fields(self):
        for name in ("feature", "bug", "tech-debt"):
            with self.subTest(name=name):
                content = (ROOT / f".github/ISSUE_TEMPLATE/{name}.yml").read_text(encoding="utf-8")
                self.assertIn("body:", content)
                self.assertIn("required: true", content)


if __name__ == "__main__":
    unittest.main()
