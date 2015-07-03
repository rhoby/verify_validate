__author__ = 'hoby'

import unittest
import tools36
import solutioneuler36

class ToolTester(unittest.TestCase):

    def setUp(self):
        pass

    def test_IsPalindromic_585(self):
        self.assertEqual(585, tools36.IsPalindromic(585), 'is not a palindromic number')

    def test_convert_binary_2(self):
        self.assertEqual('10', tools36.convert_binary(2), '2 is not convertible')

    def test_main3(self):
        self.assertEqual(157, solutioneuler36.main3(100), 'check your sum')

if __name__ == '__main__':
    unittest.main()