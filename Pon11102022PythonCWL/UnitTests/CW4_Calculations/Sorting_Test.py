# importing sys
from copy import deepcopy
import sys
import unittest
import random
sys.path.append("..")
from src.Cw4_Calculations.Sorting import sort

class Sort_Test(unittest.TestCase):
    def test_equal_reverse(self):
        # given
        x = random.sample(range(1, 100), 50)
        correct = deepcopy(x)
        # when
        x_sorted = sort(x)
        correct.sort(reverse=True)#descending
        # then
        self.assertEqual(correct, x_sorted)
    def test_equal_normal(self):
        #given
        x = random.sample(range(1, 100), 50)
        correct = deepcopy(x)
        #when
        x_sorted = sort(x)
        correct.sort()
        #then
        self.assertNotEqual(correct, x_sorted)
    def test_empty_array(self):
        #given
        x = []
        correct = deepcopy(x)
        #when
        x_sorted = sort(x)
        correct.sort()
        #then
        self.assertEqual(correct, x_sorted)
    def test_non_numerical_input(self):
        #given
        x = [1, 2, 3, 'a', "SDDD"]
        #when
        #then
        self.assertRaises(TypeError, sort, x)

if __name__ == "__main__":
    unittest.main()