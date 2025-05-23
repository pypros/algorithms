
"""
https://leetcode.com/problems/contains-duplicate/description/

217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

from dataclasses import dataclass

@dataclass
class Solution(object):
    def containsDuplicateEasy(self, args):
        # Umiem -> moglo by byc lepiej
        ...
    def containsDuplicate(self, args):
        # Umiem -> moglo by byc lepiej
        ...

import unittest


class SolutionTestCase(unittest.TestCase):
    solution = Solution()

    def test_example_1_leetcode(self):
        self.assertEqual(self.solution.containsDuplicateEasy([1,2,3,1]), True)

    def test_example_2_leetcode(self):
        self.assertEqual(self.solution.containsDuplicateEasy([1,2,3,4]), False)

    def test_example_3_leetcode(self):
        self.assertEqual(self.solution.containsDuplicateEasy([1,1,1,3,3,4,3,2,4,2]), True)

    def test_example_4_leetcode(self):
        self.assertEqual(self.solution.containsDuplicate([1,2,3,1]), True)

    def test_example_5_leetcode(self):
        self.assertEqual(self.solution.containsDuplicate([1,2,3,4]), False)

    def test_example_6_leetcode(self):
        self.assertEqual(self.solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)