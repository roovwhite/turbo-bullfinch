"""Regression tests for the mechanical checks."""
from pathlib import Path
import runpy
import unittest

EVALS = Path(__file__).resolve().parent
lint = runpy.run_path(
    str(EVALS.parent / "skills" / "humanized" / "lint.py")
)["lint"]


class LintTests(unittest.TestCase):
    def test_eval_inputs(self):
        findings = {
            "01-inflation-triads/input.md": [(1, "chatbot")],
            "09-check-mode/input-generated.md": [(1, "chatbot"), (7, "chatbot")],
            "11-utm-link/input.md": [(1, "utm"), (3, "utm")],
        }
        paths = sorted(EVALS.glob("*/input*.md"))
        for path in paths:
            name = path.relative_to(EVALS).as_posix()
            with self.subTest(name=name):
                text = path.read_text(encoding="utf-8")
                self.assertEqual([(n, rule) for n, rule, _ in lint(text)], findings.get(name, []))

    def test_punctuation_is_opt_in(self):
        text = (EVALS / "13-client-voice" / "input.md").read_text(encoding="utf-8")
        self.assertEqual(lint(text), [])
        self.assertEqual(
            [(n, rule) for n, rule, _ in lint(text, ascii_punctuation=True)],
            [(3, "dash"), (3, "quotes")],
        )

    def test_ordinary_replies_and_requests(self):
        text = "Конечно, пришлю сегодня.\n\nНапишите, если дата не подходит."
        self.assertEqual(lint(text), [])

    def test_wrapper_after_heading(self):
        text = "# Отчёт\nНиже представлен подробный обзор.\nСервис упал в 10:20."
        self.assertEqual([(n, rule) for n, rule, _ in lint(text)], [(2, "chatbot")])

    def test_ignores_protected_content(self):
        text = (
            "> Конечно! Вот переписанный текст — «пример».\n"
            "> https://example.org/?utm_source=openai\n"
            "````markdown\n````nested\n"
            "Ниже представлен обзор.\n````\n"
            "`https://example.org/?utm_source=chatgpt.com`\n"
            "Итог готов."
        )
        self.assertEqual(lint(text, ascii_punctuation=True), [])

    def test_tracking_parameter_must_match(self):
        text = (
            "[план](https://example.org/?not_utm_source=openai)\n"
            "https://example.org/?utm_source=openaix\n"
            "https://example.org/#?utm_source=openai\n"
            "[план](https://example.org/?q=test&utm_source=ChatGPT.com#part)\n"
            "[план](https://example.org/archive(v2)?utm_source=openai)"
        )
        self.assertEqual([(n, rule) for n, rule, _ in lint(text)], [(4, "utm"), (5, "utm")])

    def test_initial_horizontal_rule_without_frontmatter(self):
        text = "---\n\nНиже представлен обзор.\nСервис упал."
        self.assertEqual([(n, rule) for n, rule, _ in lint(text)], [(3, "chatbot")])


if __name__ == "__main__":
    unittest.main()
