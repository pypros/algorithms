"""
https://leetcode.com/problems/merge-two-sorted-lists/description/

21. Merge Two Sorted Lists
Easy
Topics
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from dataclasses import dataclass

@dataclass
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2 
        return dummy_head.next

import unittest


class SolutionTestCase(unittest.TestCase):
    solution = Solution()

    def _convert_linked_list_to_list(self, merged_two_lists):
        result = []
        current = merged_two_lists
        while current:
            if current.val is not None:
                result.append(current.val)
            current = current.next
        return result
     
    def test_example_1_leetcode(self):
        list_1_node_0 = ListNode(1)
        list_1_node_1 = ListNode(2)
        list_1_node_2 = ListNode(4)
        
        list_1_node_0.next = list_1_node_1
        list_1_node_1.next = list_1_node_2

        head_list_1 = list_1_node_0
        list_1 = head_list_1

        list_2_node_0 = ListNode(1)
        list_2_node_1 = ListNode(3)
        list_2_node_2 = ListNode(4)

        list_2_node_0.next = list_2_node_1
        list_2_node_1.next = list_2_node_2

        head_list_2 = list_2_node_0
        list_2 = head_list_2

        merged_two_lists = self.solution.mergeTwoLists(list_1, list_2)
        result = self._convert_linked_list_to_list(merged_two_lists)
        self.assertEqual(result, [1,1,2,3,4,4])

    def test_example_2_leetcode(self):
        list_1 = None
        list_2 = None
        merged_two_lists = self.solution.mergeTwoLists(list_1, list_2)
        result = self._convert_linked_list_to_list(merged_two_lists)
        self.assertEqual(result, [])

    def test_example_3_leetcode(self):
        list_1 = None
        list_2 = ListNode(val=0)

        merged_two_lists = self.solution.mergeTwoLists(list_1, list_2)

        result = self._convert_linked_list_to_list(merged_two_lists)
        self.assertEqual(result, [0])

    def test_example_4_leetcode(self):
        list_1 = ListNode(val=0)
        list_2 = None

        merged_two_lists = self.solution.mergeTwoLists(list_1, list_2)

        result = self._convert_linked_list_to_list(merged_two_lists)
        self.assertEqual(result, [0])

    def test_example_5_leetcode(self):
        list_1_node_0 = ListNode(2)
        list_1_node_1 = ListNode(4)
        list_1_node_2 = ListNode(6)

        list_1_node_0.next = list_1_node_1
        list_1_node_1.next = list_1_node_2

        head_list_1 = list_1_node_0
        list_1 = head_list_1

        list_2_node_0 = ListNode(1)
        list_2_node_1 = ListNode(3)
        list_2_node_2 = ListNode(5)

        list_2_node_0.next = list_2_node_1
        list_2_node_1.next = list_2_node_2

        head_list_2 = list_2_node_0
        list_2 = head_list_2

        merged_two_lists = self.solution.mergeTwoLists(list_1, list_2)
        result = self._convert_linked_list_to_list(merged_two_lists)
        self.assertEqual(result, [1,2,3,4,5,6])


    def test_example_6_leetcode(self):
        list_1_node_0 = ListNode(2)
        list_1_node_1 = ListNode(4)

        list_1_node_0.next = list_1_node_1

        head_list_1 = list_1_node_0
        list_1 = head_list_1

        list_2_node_0 = ListNode(1)
        list_2_node_1 = ListNode(3)
        list_2_node_2 = ListNode(5)

        list_2_node_0.next = list_2_node_1
        list_2_node_1.next = list_2_node_2

        head_list_2 = list_2_node_0
        list_2 = head_list_2

        merged_two_lists = self.solution.mergeTwoLists(list_1, list_2)
        result = self._convert_linked_list_to_list(merged_two_lists)
        self.assertEqual(result, [1,2,3,4,5])

    def test_example_7_leetcode(self):
        list_1_node_0 = ListNode(2)
        list_1_node_1 = ListNode(4)
        list_1_node_2 = ListNode(6)

        list_1_node_0.next = list_1_node_1
        list_1_node_1.next = list_1_node_2

        head_list_1 = list_1_node_0
        list_1 = head_list_1

        list_2_node_0 = ListNode(1)
        list_2_node_1 = ListNode(3)
 
        list_2_node_0.next = list_2_node_1
 
        head_list_2 = list_2_node_0
        list_2 = head_list_2

        merged_two_lists = self.solution.mergeTwoLists(list_1, list_2)
        result = self._convert_linked_list_to_list(merged_two_lists)
        self.assertEqual(result, [1,2,3,4,6])


if __name__ == "__main__":
    unittest.main(verbosity=2)
