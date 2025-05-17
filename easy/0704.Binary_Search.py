"""
https://leetcode.com/problems/binary-search/description/

704. Binary Search
Easy
Topics
Companies
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""

from dataclasses import dataclass


@dataclass
class Solution(object):
    def searchMoje(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left_index = 0
        right_index = len(nums) - 1
        last_index = -1
        while left_index <= right_index:
            index = (left_index + right_index) // 2  
            if last_index == left_index or last_index == right_index:
                break

            if nums[index] == target:
                return index
            if nums[index] > target:
                last_index = right_index
                right_index =  index
            if nums[index] < target:
                last_index = left_index
                left_index =  index
        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left_index = 0
        right_index = len(nums) - 1
        while left_index <= right_index:
            index = (left_index + right_index) // 2  
            if nums[index] > target:
                right_index =  index - 1
            elif nums[index] < target:
                left_index =  index + 1
            else:
                return index
        return -1



import unittest


class SolutionTestCase(unittest.TestCase):
    solution = Solution()

    def test_example_1_leetcode(self):
        self.assertEqual(self.solution.search([-1,0,3,5,9,12], 9 ), 4)

    def test_example_2_leetcode(self):
        self.assertEqual(self.solution.search([-1,0,3,5,9,12], 2), -1)

    def test_example_3_leetcode(self):
        self.assertEqual(self.solution.search([-1,0,3,5,6,9,12], 9), 5)

if __name__ == "__main__":
    unittest.main(verbosity=2)
