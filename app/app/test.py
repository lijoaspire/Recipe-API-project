"""Sample testing"""

from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        res = calc.add(5,3)

        self.assertEqual(res, 8)