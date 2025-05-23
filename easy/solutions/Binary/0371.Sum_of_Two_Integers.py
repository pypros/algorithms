"""
https://leetcode.com/problems/sum-of-two-integers/description/

371. Sum of Two Integers
Attempted
Medium
Topics
Companies
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000

"""


from dataclasses import dataclass


@dataclass
class Solution(object):
    # def getSum(self, a: int, b: int) -> int:
    #     mask = 0xffffffff
    #     while (mask & b) > 0:
    #         a, b = a^b, (a & b) << 1
    #     return (mask & a) if b > 0 else a

    def getSum(self, a: int, b: int) -> int:
        mask = 0x7fffffff
        while (mask & b) > 0:
            a, b = a^b, (a & b) << 1
        return (mask & a) if b > 0 else a

import unittest


class SolutionTestCase(unittest.TestCase):
    solution = Solution()

    def test_example_1_leetcode(self):
        self.assertEqual(self.solution.getSum(a = 1, b = 2), 3)

    def test_example_2_leetcode(self):
        self.assertEqual(self.solution.getSum(a = 2, b = 3), 5)

    def test_example_3_leetcode(self):
        self.assertEqual(self.solution.getSum(a = -1, b = 0), -1)

    def test_example_4_leetcode(self):
        self.assertEqual(self.solution.getSum(a = -1, b = 1), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
