import unittest
from django.test import TestCase
from django.test import Client
from .utils import converter
# Create your tests here.

class SimpleTest(unittest.TestCase):
    def test_placement(self):
        client = Client()
        response = client.get('/placements/')
        self.assertEqual(response.status_code, 200)


class BasicTest(unittest.TestCase):
    def test_one_plus_one(self):
        self.assertEqual(1+1, 2)


class ConverterTest (unittest.TestCase):
    def test_new_line(self):
        input= 'hsjkjh'
        output= converter(input)
        self.assertEqual(output, 'document.write(%s)' %input)

    def test_add_line(self):
        line1 = 'bjkds'
        line2 = 'saklk'

        input= """bjkds
saklk"""
        output= converter(input)
        self.assertEqual(output, """document.write(bjkds)
        document.write(saklk)""")
