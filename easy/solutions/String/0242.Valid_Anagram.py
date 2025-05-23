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
    # def isAnagram(self, s, t):
    #     if len(s) != len(t):
    #         return False
    #     return Counter(s) == Counter(t)

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        s_counter = {}
        for sch in s:
            if sch in s_counter:
                s_counter[sch] += 1
            else:
                s_counter[sch] = 1
        for tch in t:
            if tch not in s_counter:
                return False
            elif s_counter[tch] == 0:
                return False
            else:
                s_counter[tch] -= 1

        return not s_counter

import unittest


class SolutionTestCase(unittest.TestCase):
    solution = Solution()

    def test_example_1_leetcode(self):
        self.assertEqual(self.solution.isAnagram("anagram", "nagaram"), True)

    def test_example_2_leetcode(self):
        self.assertEqual(self.solution.isAnagram("rat", "car"), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)
