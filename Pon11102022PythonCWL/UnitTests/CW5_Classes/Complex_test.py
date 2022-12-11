import unittest
from ast import Expression
import numpy as np

import sys
sys.path.append("..")
from src.Cw5_Classes.Classes import Complex

class Complex_Test(unittest.TestCase):
	def test_complex_add(self):
		#given
		num1 = Complex(1,1)
		num2 = Complex(2,1)
		correct = Complex(3, 2)
		#when
		out = num1 + num2
		#then
		self.assertEqual(correct, out)
	def test_complex_sub(self):
		#given
		num1 = Complex(1,1)
		num2 = Complex(2,1)
		correct = Complex(-1, 0)
		#when
		out = num1 - num2
		#then
		self.assertEqual(correct, out)
	def test_complex_mul(self):
		#given
		num1 = Complex(1,1)
		num2 = Complex(2,1)
		correct = Complex(1, 3)
		#when
		out = num1 * num2
		#then
		self.assertEqual(correct, out)
	def test_complex_div(self):
		#given
		num1 = Complex(1,1)
		num2 = Complex(2,1)
		correct = Complex(0.6, 0.2)
		#when
		out = num1 / num2
		#then
		self.assertEqual(correct, out)
	def test_complex_con(self):
		#given
		num2 = Complex(2,1)
		correct = Complex(2,-1)
		#when
		num2.conjugate()
		#then
		self.assertEqual(correct, num2)

if __name__ == "__main__":
    unittest.main();