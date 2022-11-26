"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    '''test a calc module'''

    def test_add_numbers(self):
        """testing Adding numbers"""
        res = calc.add(5,6)

        self.assertEqual(res,11)
    
    def test_subtract_numbers(self):
        """testing subtraction of 2 numbers"""
        res = calc.subtract(11,5)

        self.assertEqual(res,6)