import sys

sys.path.append("..")
from src.Cw4_Calculations.quadraticEquation import quadratic_equation

import unittest
from copy import deepcopy
import math
import random
import numpy as np


class quadraticEquation(unittest.TestCase):
    def test_no_real_roots(self):
        # given
        a = 1
        b = -3
        c = 4
        correct = {1.5, -math.sqrt(7)/2}, {1.5, math.sqrt(7)/2};
        # when
        result = quadratic_equation(a, b, c)
        # then
        self.assertEqual(result, correct)

    def test_one_root(self):
        # given
        a = 1
        b = -10
        c = 25
        correct = 5
        # when
        result = quadratic_equation(a, b, c)
        # then
        self.assertEqual(result, correct)

    def test_two_roots(self):
        # given
        a = 1
        b = 3
        c = 2
        correct = (-2.0, -1.0)
        # when
        result = quadratic_equation(a, b, c)
        # then
        self.assertEqual(result, correct)

    def test_missing_argument(self):
        self.assertRaises(TypeError, quadratic_equation,1)

    def test_wrong_input(self):
        self.assertRaises(TypeError, quadratic_equation, 1, "sd", 'a')


if __name__ == "__main__":
    unittest.main()
