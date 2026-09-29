"""Basic automated tests for result calculation."""
import sys
import unittest
from pathlib import Path

# Make project root importable when tests are run from the project directory.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from marks_manager import calculate_result


class ResultCalculationTests(unittest.TestCase):
    def test_average_and_grade(self):
        student = {"marks": {"Python": 80, "Maths": 90}}
        result = calculate_result(student)
        self.assertEqual(result["total"], 170)
        self.assertEqual(result["percentage"], 85)
        self.assertEqual(result["grade"], "A")

    def test_no_marks(self):
        result = calculate_result({"marks": {}})
        self.assertEqual(result["grade"], "Not available")
        self.assertEqual(result["percentage"], 0.0)

    def test_failing_grade(self):
        result = calculate_result({"marks": {"Python": 25}})
        self.assertEqual(result["grade"], "F")


if __name__ == "__main__":
    unittest.main()
