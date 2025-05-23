"""
https://leetcode.com/problems/valid-palindrome/description/

125. Valid Palindrome
Easy
Topics
Companies

A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

"""

from dataclasses import dataclass


@dataclass
class Solution(object):
    def isPalindrome(self, s: str):
        # ogolnie spoko problem z indexem


import unittest


class SolutionTestCase(unittest.TestCase):
    solution = Solution()

    def test_example_1_leetcode(self):
        self.assertEqual(self.solution.isPalindrome("A man, a plan, a canal: Panama"), True)

    def test_example_2_leetcode(self):
        self.assertEqual(self.solution.isPalindrome("race a car"), False)

    def test_example_3_leetcode(self):
        self.assertEqual(self.solution.isPalindrome(" "), True)

    def test_example_3_leetcode(self):
        self.assertEqual(self.solution.isPalindrome("a l a"), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)
