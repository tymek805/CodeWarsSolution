import unittest
from code_wars_solution import material


class CodeWarsSolutionTester(unittest.TestCase):
    def test_case_website_1(self):
        self.assertEqual(6, material([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    def test_case_website_2(self):
        self.assertEqual(8, material([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]))

    def test_case_website_3(self):
        self.assertEqual(9, material([4, 2, 0, 3, 2, 5]))

    def test_case_website_4(self):
        self.assertEqual(83, material([6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]))

    def test_case_website_5(self):
        self.assertEqual(50, material([6, 2, 1, 1, 8, 0, 5, 5, 0, 1, 8, 9, 6, 9, 4, 8, 0, 0]))

    def test_case_private_1(self):
        self.assertEqual(9, material([0, 5, 5, 0, 5, 4, 0, 4]))
