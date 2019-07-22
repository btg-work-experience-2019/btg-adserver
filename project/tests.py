from django.test import TestCase
from adserver.one_plus_one import Number

class test_print_number(TestCase):
    def test_print_number(self):
        self.assertEqual(1 + 1, 2)
