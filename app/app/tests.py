"""
sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test calc module."""

    def test_add_numbers(self):
        "Test adding numbers together."
        res = calc.add(6, 7)

        self.assertEqual(res, 13)
        