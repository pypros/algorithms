"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

104. Maximum Depth of Binary Tree
Easy
Topics
Companies
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
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
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     stack = [[root,1]]
    #     res = 0
    #     while stack:
    #         node, depth = stack.pop()
    #         if node:
    #             res = max(res, depth)
    #             stack.append([node.left, depth+1])
    #             stack.append([node.right, depth+1])
    #     return res

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        max-depth -> DFS
        """
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)


import unittest


class SolutionTestCase(unittest.TestCase):
    solution = Solution()

    def test_example_1_leetcode(self):
        # Input: root = [3,9,20,null,null,15,7]
        #                                       3 (l:1 n:1)
        #                 /                                             \
        #             9 (l:2 n:1)                                   20 (l:2 n:2)
        #         /                  \                            /              \
        #     null (l:3 n:1)       null (l:3 n:2)        15 (l:3 n:3)         7 (l:3 n:4)

        tree_level_1_node1 = TreeNode(val=3)
        tree_level_2_node1 = TreeNode(val=9)
        tree_level_2_node2 = TreeNode(val=20)
        tree_level_3_node1 = None
        tree_level_3_node2 = None
        tree_level_3_node3 = TreeNode(val=15)
        tree_level_3_node4 = TreeNode(val=7)

        tree_level_1_node1.left = tree_level_2_node1
        tree_level_1_node1.right = tree_level_2_node2


        tree_level_2_node1.left = tree_level_3_node1
        tree_level_2_node1.right = tree_level_3_node2
        tree_level_2_node2.left = tree_level_3_node3
        tree_level_2_node2.right = tree_level_3_node4        


        self.assertEqual(self.solution.maxDepth(root=tree_level_1_node1), 3)

    def test_example_2_leetcode(self):
        # Input: root =  [1,null,2]
        #            1 (l:1 n:1)
        #    /                       \
        #  None                     2 (l:2 n:2)

        tree_level_1_node1 = TreeNode(val=1)
        tree_level_2_node1 = None
        tree_level_2_node2 = TreeNode(val=2)

        tree_level_1_node1.left = tree_level_2_node1
        tree_level_1_node1.right = tree_level_2_node2
     

        self.assertEqual(self.solution.maxDepth(root=tree_level_1_node1), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
