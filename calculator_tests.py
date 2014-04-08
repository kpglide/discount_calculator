import unittest

from discount_calculator import Discount_Calculator

class Discount_Calculator_TDD(unittest.TestCase):

	def setUp(self):
		self.calc = Discount_Calculator()

	def test_calculate_discount_method_percent_input(self):
		result = self.calc.calculate_discount(250, 10, 'percent')
		self.assertEqual(25, result)

	def test_calculate_discount_method_whole_num_input(self):
		result = self.calc.calculate_discount(250, 20, 'absolute')
		self.assertEqual(20, result)

	def test_calculator_returns_error_message_if_both_args_not_numbers(self):
		self.assertRaises(ValueError, self.calc.calculate_discount, 'two', 'three', 'percent')		

	def test_calculator_returns_error_message_if_x_arg_not_number(self):	
		self.assertRaises(ValueError, self.calc.calculate_discount, 'two', 3, 'percent')

	def test_calculator_returns_error_message_if_y_arg_not_number(self):
		self.assertRaises(ValueError, self.calc.calculate_discount, 2, 'three', 'percent')

	def test_handles_floats_percent(self):
		result = self.calc.calculate_discount(250.0, 10.0, 'percent')
		self.assertEqual(25, result)

	def test_handles_floats_absolute(self):
		result = self.calc.calculate_discount(250.0, 10.0, 'absolute')
		self.assertEqual(10, result)	
	
	def test_invalid_discount_type(self):
		self.assertRaises(ValueError, self.calc.calculate_discount, 250, 10, 'random')

	def test_discount_greater_than_total(self):
		self.assertRaises(ValueError, self.calc.calculate_discount, 200, 201, 'percent')

	def test_discount_percent_over_one_hundred(self):
		self.assertRaises(ValueError, self.calc.calculate_discount, 200, 101, 'percent')		