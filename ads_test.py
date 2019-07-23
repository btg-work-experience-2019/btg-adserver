import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def test_placement(self):
        client = Client()
        response = client.get('/main/placements/')
        self.assertEqual(response.status_code, 200)
