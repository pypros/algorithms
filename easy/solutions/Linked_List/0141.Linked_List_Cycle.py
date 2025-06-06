"""
https://leetcode.com/problems/linked-list-cycle/description/

141. Linked List Cycle
Easy
Topics
Companies
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?

"""

from dataclasses import dataclass

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next

from typing import Optional

@dataclass
class Solution(object):
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            slow = slow. next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


import unittest


class SolutionTestCase(unittest.TestCase):
    solution = Solution()
     
    def test_example_1_leetcode(self):
        node0 = ListNode(3)
        node1 = ListNode(2)
        node2 = ListNode(0)
        node3 = ListNode(-4)

        node0.next = node1
        node1.next = node2
        node2.next = node3
        node3.next = node1

        list_1 = node3



        self.assertEqual(self.solution.hasCycle(list_1), True)

    def test_example_2_leetcode(self):
        node0 = ListNode(1)
        node1 = ListNode(2)
        node0.next = node0
        node1.next = node1
        list_1 = node1

        self.assertEqual(self.solution.hasCycle(list_1), True)


    def test_example_3_leetcode(self):
        node0 = ListNode(1)
        list_1 = node0
        self.assertEqual(self.solution.hasCycle(list_1), False)





if __name__ == "__main__":
    unittest.main(verbosity=2)
