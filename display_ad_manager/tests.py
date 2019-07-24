from django.test import TestCase
import unittest

class BasicTest(unittest.TestCase):

    def test_one_plus_one(self):
        self.assertEqual(1+1, 2)
