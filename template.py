"""
Description
"""

from dataclasses import dataclass


@dataclass
class Solution(object):
    def name(self, args):
        return args


import unittest


class SolutionTestCase(unittest.TestCase):
    solution = Solution()

    def test_example_1_leetcode(self):
        self.assertEqual(self.solution.name(True), True)

    def test_example_2_leetcode(self):
        self.assertEqual(self.solution.name(False), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)
