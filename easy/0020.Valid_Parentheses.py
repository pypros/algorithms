"""
https://leetcode.com/problems/valid-parentheses/description/

20. Valid Parentheses
Easy
Topics
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
from dataclasses import dataclass

@dataclass
class Solution(object):
    def isValid(self, s):
        """
        """
    def isValid(self, s):
        stack = []
        parentheses = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        for ch in s:
            if ch in parentheses:
                stack.append(ch)
            else:
                sch = stack.pop()
                if parentheses[ch] != sch:
                    return False
        return not s




import unittest


class TwoSumTestCase(unittest.TestCase):
    solution = Solution()
    # def test_example_1_leetcode_isValid(self):
    #     self.assertEqual(self.solution.isValid(s="()"), True)

    def test_example_1_leetcode_isValid(self):
        self.assertEqual(self.solution.isValid(s="()"), True)
    def test_example_2_leetcode_isValid(self):
        self.assertEqual(self.solution.isValid(s="()[]{}"), True)
    def test_example_3_leetcode_isValid(self):
        self.assertEqual(self.solution.isValid(s="(]"), False)
    def test_example_4_leetcode_isValid(self):
        self.assertEqual(self.solution.isValid(s="([])"), True)
    def test_example_5_leetcode_isValid(self):
        self.assertEqual(self.solution.isValid(s="([]"), False)
    def test_example_6_leetcode_isValid(self):
        self.assertEqual(self.solution.isValid(s=""), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)