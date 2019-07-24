import unittest
from django.test import TestCase
from django.test import Client
# Create your tests here.

class SimpleTest(unittest.TestCase):
    def test_placement(self):
        client = Client()
        response = client.get('/placements/')
        self.assertEqual(response.status_code, 200)
