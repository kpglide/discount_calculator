import unittest

from discount_calculator import Discount_Calculator

class Discount_Calculator_TDD(unittest.TestCase):

	def setUp(self):
		self.calc = Discount_Calculator()

	def test_calculate_discount_method_percent_input(self):
		result = self.calc.calculate_discount(100, 10, 'percent')
		self.assertEqual(10, result)

	def test_calculate_discount_method_whole_num_input(self):
		result = self.calc.calculate_discount(100, 20, 'whole_num')
		self.assertEqual(20, result)

	def test_calculator_returns_error_message_if_both_args_not_numbers(self):
		self.assertRaises(ValueError, self.calc.calculate_discount, 'two', 'three', 'percent')		

	def test_calculator_returns_error_message_if_x_arg_not_number(self):	
		self.assertRaises(ValueError, self.calc.calculate_discount, 'two', 3, 'percent')

	def test_calculator_returns_error_message_if_y_arg_not_number(self):
			self.assertRaises(ValueError, self.calc.calculate_discount, 2, 'three', 'percent')

