"""
https://leetcode.com/problems/climbing-stairs/description/

70. Climbing Stairs
Easy
Topics
Companies
Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""

from dataclasses import dataclass


@dataclass
class Solution:
    def climbStairs(self, n: int) -> int:
        one = two = 1
        for _ in range(n-1):
            one , two = one + two, one
        return one


import unittest


class SolutionTestCase(unittest.TestCase):
    solution = Solution()

    def test_example_1_leetcode(self):
        self.assertEqual(self.solution.climbStairs(2), 2)

    def test_example_2_leetcode(self):
        self.assertEqual(self.solution.climbStairs(3), 3)

if __name__ == "__main__":
    unittest.main(verbosity=2)
