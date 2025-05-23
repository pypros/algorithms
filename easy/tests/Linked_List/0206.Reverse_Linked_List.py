"""
https://leetcode.com/problems/reverse-linked-list/description/

206. Reverse Linked List
Solved
Easy
Topics
Companies
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""





# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ...

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
        # return list(reversed(result))
        return result

    def test_example_1_leetcode(self):

        list_1_node_1 = ListNode(1)
        list_1_node_2 = ListNode(2)
        list_1_node_3 = ListNode(3)
        list_1_node_4 = ListNode(4)
        list_1_node_5 = ListNode(5)
        
        list_1_node_1.next = list_1_node_2
        list_1_node_2.next = list_1_node_3
        list_1_node_3.next = list_1_node_4
        list_1_node_4.next = list_1_node_5

        list_1 = list_1_node_1

        reverse_list = self.solution.reverseList(list_1)
        result = self._convert_linked_list_to_list(reverse_list)
        self.assertEqual(result,  [5,4,3,2,1])

    def test_example_2_leetcode(self):
        list_1_node_1 = ListNode(1)
        list_1_node_2 = ListNode(2)
        list_1_node_1.next = list_1_node_2
        list_1 = list_1_node_1

        reverse_list = self.solution.reverseList(list_1)

        result = self._convert_linked_list_to_list(reverse_list)
        self.assertEqual(result, [2,1])


    def test_example_3_leetcode(self):
        list_1 = ListNode(val=None)
        reverse_list = self.solution.reverseList(list_1)
        result = self._convert_linked_list_to_list(reverse_list)
        self.assertEqual(result, [])





if __name__ == "__main__":
    unittest.main(verbosity=2)
