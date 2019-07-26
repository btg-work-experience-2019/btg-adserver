import unittest
from django.test import TestCase
from django.test import Client
from .utils import converter
# Create your tests here.

class SimpleTest(unittest.TestCase):
    def test_placement(self):
        client = Client()
        response = client.get('/placements/99/')
        #self.assertEqual(response.status_code, 200)
        #self.assertEqual(str(response.content, 'utf-8'), '99')


class BasicTest(unittest.TestCase):
    def test_one_plus_one(self):
        self.assertEqual(1+1, 2)


class ConverterTest (unittest.TestCase):
    def test_single_line_input_output_line_count(self):
        input = "hello world"
        output = converter(input)
        output_line_count = len(output.split('\n'))
        self.assertEqual(output_line_count, 1)

    def test_multi_line_input_output_line_count(self):
        input = "hello\nworld"
        output = converter(input)
        output_line_count = len(output.split("\n"))
        self.assertEqual(output_line_count, 2)

    def test_single_line_wrapping(self):
        input = "hsjkjh"
        output = converter(input)
        self.assertEqual(output, 'document.write("%s");' % input)

    def test_multi_line_wrapping(self):
        line_1 = "bjkd"
        line_2 = "saklk"
        input = "%s\n%s" % (line_1, line_2)
        output = converter(input)
        lines= output.split("\n")
        self.assertEqual(lines[0], 'document.write("%s");' % line_1)
        self.assertEqual(lines[1], 'document.write("%s");' % line_2)
