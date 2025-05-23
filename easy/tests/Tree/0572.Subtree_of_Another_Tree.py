"""
https://leetcode.com/problems/subtree-of-another-tree/description/

572. Subtree of Another Tree
Easy
Topics
Companies
Hint
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:





import unittest
from collections import deque

class SolutionTestCase(unittest.TestCase):
    solution = Solution()


    def test_example_1_leetcode(self):
        # Input: root = [3,4,5,1,2], subRoot = [4,1,2]
        # Output: true
        tree1_level_1_node1 = TreeNode(val=3)
        tree1_level_2_node1 = TreeNode(val=4)
        tree1_level_2_node2 = TreeNode(val=5)
        tree1_level_3_node1 = TreeNode(val=1)
        tree1_level_3_node2 = TreeNode(val=2)

        tree1_level_1_node1.left = tree1_level_2_node1
        tree1_level_1_node1.right = tree1_level_2_node2
        tree1_level_2_node1.left = tree1_level_3_node1
        tree1_level_2_node1.right = tree1_level_3_node2


        tree2_level_1_node1 = TreeNode(val=4)
        tree2_level_2_node1 = TreeNode(val=1)
        tree2_level_2_node2 = TreeNode(val=2)

        tree2_level_1_node1.left = tree2_level_2_node1
        tree2_level_1_node1.right = tree2_level_2_node2

        self.assertEqual(self.solution.isSubtree(tree1_level_1_node1, tree2_level_1_node1), True)

    def test_example_2_leetcode(self):
        # Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
        # Output: false
        #      3
        #     / \
        #    4   5
        #   / \
        #  1   2
        #       \
        #        0
        tree1_level_1_node1 = TreeNode(val=3)
        tree1_level_2_node1 = TreeNode(val=4)
        tree1_level_2_node2 = TreeNode(val=5)
        tree1_level_3_node1 = TreeNode(val=1)
        tree1_level_3_node2 = TreeNode(val=2)
        tree1_level_3_node3 = None # Not used because None is as default 
        tree1_level_3_node4 = None # Not used because None is as default
        tree1_level_4_node1 = None # Not used because None is as default
        tree1_level_4_node2 = None # Not used because None is as default
        tree1_level_4_node3 = None # Not used because None is as default
        tree1_level_4_node4 = TreeNode(val=0)

        tree1_level_1_node1.left = tree1_level_2_node1
        tree1_level_1_node1.right = tree1_level_2_node2

        tree1_level_2_node1.left = tree1_level_3_node1
        tree1_level_2_node1.right = tree1_level_3_node2

        tree1_level_3_node2.right = tree1_level_4_node4

        tree2_level_1_node1 = TreeNode(val=4)
        tree2_level_2_node1 = TreeNode(val=1)
        tree2_level_2_node2 = TreeNode(val=2)

        tree2_level_1_node1.left = tree2_level_2_node1
        tree2_level_1_node1.right = tree2_level_2_node2

        self.assertEqual(self.solution.isSubtree(tree1_level_1_node1, tree2_level_1_node1), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
