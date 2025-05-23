"""
https://leetcode.com/problems/number-of-1-bits/description/

191. Number of 1 Bits
Easy
Topics
Companies
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

 

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 

Constraints:

1 <= n <= 231 - 1
 

Follow up: If this function is called many times, how would you optimize it?
"""

from dataclasses import dataclass


@dataclass
class Solution:
    def hammingWeight(self, n: int) -> int:
        # spoko

import unittest


class SolutionTestCase(unittest.TestCase):
    solution = Solution()

    def test_example_1_leetcode(self):
        self.assertEqual(self.solution.hammingWeight(11), 3)

    def test_example_2_leetcode(self):
        self.assertEqual(self.solution.hammingWeight(128), 1)

    def test_example_3_leetcode(self):
        self.assertEqual(self.solution.hammingWeight(2147483645), 30)

if __name__ == "__main__":
    unittest.main(verbosity=2)
