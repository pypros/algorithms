"""
https://leetcode.com/problems/same-tree/description/

100. Same Tree
Easy
Topics
Companies
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""

from dataclasses import dataclass
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


@dataclass
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None or q.val != p.val:
            return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right


import unittest


class SolutionTestCase(unittest.TestCase):
    solution = Solution()

    def test_example_1_leetcode(self):
        tree1_level_1_node1 = TreeNode(val=1)
        tree1_level_2_node1 = TreeNode(val=2)
        tree1_level_2_node2 = TreeNode(val=3)

        tree1_level_1_node1.left = tree1_level_2_node1
        tree1_level_1_node1.right = tree1_level_2_node2

        tree2_level_1_node1 = TreeNode(val=1)
        tree2_level_2_node1 = TreeNode(val=2)
        tree2_level_2_node2 = TreeNode(val=3)

        tree2_level_1_node1.left = tree2_level_2_node1
        tree2_level_1_node1.right = tree2_level_2_node2

        self.assertEqual(self.solution.isSameTree(p=tree1_level_1_node1, q=tree2_level_1_node1), True)

    def test_example_2_leetcode(self):
        tree1_level_1_node1 = TreeNode(val=1)
        tree1_level_2_node1 = TreeNode(val=2)
        tree1_level_2_node2 = None

        tree1_level_1_node1.left = tree1_level_2_node1
        tree1_level_1_node1.right = tree1_level_2_node2

        tree2_level_1_node1 = TreeNode(val=1)
        tree2_level_2_node1 = None
        tree2_level_2_node2 = TreeNode(val=2)

        tree2_level_1_node1.left = tree2_level_2_node1
        tree2_level_1_node1.right = tree2_level_2_node2

        self.assertEqual(self.solution.isSameTree(p=tree1_level_1_node1, q=tree2_level_1_node1), False)

    def test_example_3_leetcode(self):
        tree1_level_1_node1 = TreeNode(val=1)
        tree1_level_2_node1 = TreeNode(val=2)
        tree1_level_2_node2 = TreeNode(val=1)

        tree1_level_1_node1.left = tree1_level_2_node1
        tree1_level_1_node1.right = tree1_level_2_node2

        tree2_level_1_node1 = TreeNode(val=1)
        tree2_level_2_node1 = TreeNode(val=1)
        tree2_level_2_node2 = TreeNode(val=2)

        tree2_level_1_node1.left = tree2_level_2_node1
        tree2_level_1_node1.right = tree2_level_2_node2

        self.assertEqual(self.solution.isSameTree(p=tree1_level_1_node1, q=tree2_level_1_node1), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)
