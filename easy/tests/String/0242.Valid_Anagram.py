"""
https://leetcode.com/problems/valid-anagram/description/

242. Valid Anagram
Easy
Topics
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

from dataclasses import dataclass
from collections import Counter

@dataclass
class Solution(object):
    def isAnagram(self, s, t):
        counter = {}
        if len(s) != len(t):
            return False
        for schar in s:
            if schar not in counter:
                counter[schar] = 1
            else:
                counter[schar] += 1
        for tchar in t:
            if tchar not in counter:
                return False
            else:
                if counter[tchar] == 0:
                    return False
                else:
                    counter[tchar] -= 1
        return counter
import unittest


class SolutionTestCase(unittest.TestCase):
    solution = Solution()

    def test_example_1_leetcode(self):
        self.assertEqual(self.solution.isAnagram("anagram", "nagaram"), True)

    def test_example_2_leetcode(self):
        self.assertEqual(self.solution.isAnagram("rat", "car"), False)

    def test_example_3_leetcode(self):
        self.assertEqual(self.solution.isAnagram("anagram", "nagaram"), True)

    def test_example_4_leetcode(self):
        self.assertEqual(self.solution.isAnagram("rat", "car"), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)
