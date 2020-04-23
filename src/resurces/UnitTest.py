from unittest import TestCase


from src.resurces.test_functions import divide,multiply




class TestFunctions(TestCase):
    def test_divide_result(self):
        dividend = 15
        divisor = 3
        #divide = dividend/divisor
        expected_result = 5.0
        self.assertEqual(divide(dividend,divisor),expected_result)

    def test_divide_negative(self):
        dividend = 15
        divisor = -3
        #divide = dividend / divisor
        expected_result = -5.0
        self.assertEqual(divide(dividend,divisor), expected_result)

    def test_divide_dividend_zero(self):
        dividend = 0
        divisor = 5
        #divide = dividend / divisor
        expected_result = 0
        self.assertEqual(divide(dividend,divisor), expected_result)


    def test_divide_zer(self):
        self.assertRaises(ValueError,lambda :divide(25,0))

    def test_multply_empty(self):
        self.assertRaises(ValueError,lambda:multiply())

    def test_multiply_single(self):
        expected = 15
        self.assertEqual(multiply(expected),expected)

    def test_multiply_zero(self):
        expected = 0
        self.assertEqual(multiply(expected),0)

    def multiply_est_result(self):
        input = (3,5)
        expected =15
        self.assertEqual(multiply(*input),expected)


