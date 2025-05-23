"""
https://leetcode.com/problems/two-sum/description/

1. Two Sum
#Easy #Topics #Companies #Hint

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from dataclasses import dataclass


@dataclass
class Solution(object):
    def twoSumSlideWindowNaive(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        This solution was create because test case prepared on Leetcode are very bad.
        Time: O(n)
        Space: O(1)
        """
        index = 0
        length = len(nums)-1
        while index < length:
            print(index)
            if nums[index] + nums[index + 1] == target:
                return [index, index + 1]
            index += 1
        return []
    
    def twoSumOnlyCheckIfExist(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        This solution was create because I saw a lot of solution on the Internet which request only return true or false
        Time: O(n)
        Space: O(n)
        """
        results = set()
        index = 0
        while index < len(nums):
            num = nums[index]
            rest = target - num
            if num in results:
                return True
            results.add(rest)
            index += 1
        return False

    def twoSumGetIndexes(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Expected solution.
        Time: O(n)
        Space: O(n)
        """
        results = {} # O(1)
        index = 0 # O(1)
        while index < len(nums):  # O(n)
            value = nums[index] # O(1)
            rest = target - value # O(1)
            if rest in results: # O(1)
                return [results[rest], index] # O(1)
            results[value] = index # O(1)
            index += 1 # O(1)
        return [] # O(1)

    def twoSumGetNlogN(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Expected solution.
        Time: O(nlogn)
        Space: O(1)
        """
        # https://en.wikipedia.org/wiki/Timsort
        # https://en.wikipedia.org/wiki/Powersort
        nums.sort() # O(n log n) 
        left = 0 # O(1)
        right = len(nums) - 1 # O(n)
        while left != right: # O(1)
            result = nums[left] + nums[right]
            if result == target: # O(1)
                return True # O(1)
            elif result > target: # O(1)
                right -= 1 # O(1)
            elif result < target: # O(1)
                left +=1 # O(1)
        return False # O(1)


import unittest


class TwoSumTestCase(unittest.TestCase):
    solution = Solution()

    def test_example_one_leetcode_twoSumWrong(self):
        self.assertEqual(self.solution.twoSumSlideWindowNaive(nums=[2, 7, 11, 15], target=9), [0, 1])

    def test_example_two_leetcode_twoSumWrong(self):
        self.assertEqual(self.solution.twoSumSlideWindowNaive(nums=[3, 2, 4], target=6), [1, 2])

    def test_example_three_leetcode_twoSumWrong(self):
        self.assertEqual(self.solution.twoSumSlideWindowNaive(nums=[3, 3], target=6), [0, 1])

    def test_example_four_leetcode_twoSumWrong(self):
        self.assertEqual(self.solution.twoSumSlideWindowNaive(nums=[3,3,3], target=5), [])

    def test_example_one_leetcode_twoSumOnlyCheckIfExist(self):
        self.assertEqual(self.solution.twoSumOnlyCheckIfExist(nums=[2, 7, 11, 15], target=9), True)

    def test_example_two_leetcode_twoSumOnlyCheckIfExist(self):
        self.assertEqual(self.solution.twoSumOnlyCheckIfExist(nums=[3, 2, 4], target=6), True)

    def test_example_three_leetcode_twoSumOnlyCheckIfExist(self):
        self.assertEqual(self.solution.twoSumOnlyCheckIfExist(nums=[3, 3], target=6), True)

    def test_example_four_leetcode_twoSumOnlyCheckIfExist(self):
        self.assertEqual(self.solution.twoSumOnlyCheckIfExist(nums=[3,3,3], target=5), False)

    def test_example_one_leetcode_twoSumGetIndexes(self):
        self.assertEqual(self.solution.twoSumGetIndexes(nums=[2, 7, 11, 15], target=9), [0, 1])

    def test_example_two_leetcode_twoSumGetIndexes(self):
        self.assertEqual(self.solution.twoSumGetIndexes(nums=[3, 2, 4], target=6), [1, 2])

    def test_example_three_leetcode_twoSumGetIndexes(self):
        self.assertEqual(self.solution.twoSumGetIndexes(nums=[3, 3], target=6), [0, 1])

    def test_example_four_leetcode_twoSumGetIndexes(self):
        self.assertEqual(self.solution.twoSumGetIndexes(nums=[3,3,3], target=5), [])

    def test_example_five_leetcode_twoSumGetIndexes(self):
        self.assertEqual(self.solution.twoSumGetIndexes(nums=[3, 5, -4, 8, 11, 1, -1, 6], target=10), [4,6])

    def test_example_one_leetcode_twoSumGetNlogN(self):
        self.assertEqual(self.solution.twoSumGetNlogN(nums=[2, 7, 11, 15], target=9), True)

    def test_example_two_leetcode_twoSumGetNlogN(self):
        self.assertEqual(self.solution.twoSumGetNlogN(nums=[3, 2, 4], target=6), True)

    def test_example_three_leetcode_twoSumGetNlogN(self):
        self.assertEqual(self.solution.twoSumGetNlogN(nums=[3, 3], target=6), True)

    def test_example_four_leetcode_twoSumGetNlogN(self):
        self.assertEqual(self.solution.twoSumGetNlogN(nums=[3,3,3], target=5), False)

    def test_example_five_leetcode_twoSumGetNlogN(self):
        self.assertEqual(self.solution.twoSumGetNlogN(nums=[3, 5, -4, 8, 11, 1, -1, 6], target=10), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)
