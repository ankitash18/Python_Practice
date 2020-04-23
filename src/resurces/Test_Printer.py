from unittest import TestCase

from src.resurces.Class_testing import Printer,PrintError


class TestPrinter(TestCase):
    def setup(self):
        self.printer =  Printer(pages_per_s= 2.0,capacity =300)

    def test_print_within_capacity(self):

        messge = self.printer.print(25)
        self.assertEqual(f"Printer 25 page in 12.500000 seconds",messge)
        