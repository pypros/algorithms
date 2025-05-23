"""
https://leetcode.com/problems/invert-binary-tree/description/

226. Invert Binary Tree
Easy
Topics
Companies
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right) 
        return root

import unittest
from collections import deque

class SolutionTestCase(unittest.TestCase):
    solution = Solution()

    def tree_to_list(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result

    def test_example_1_leetcode(self):
        tree1_level_1_node1 = TreeNode(val=4)
        tree1_level_2_node1 = TreeNode(val=2)
        tree1_level_2_node2 = TreeNode(val=7)
        tree1_level_3_node1 = TreeNode(val=1)
        tree1_level_3_node2 = TreeNode(val=3)
        tree1_level_3_node3 = TreeNode(val=6)
        tree1_level_3_node4 = TreeNode(val=9)

        tree1_level_1_node1.left = tree1_level_2_node1
        tree1_level_1_node1.right = tree1_level_2_node2        

        tree1_level_2_node1.left = tree1_level_3_node1
        tree1_level_2_node1.right = tree1_level_3_node2
        tree1_level_2_node2.left = tree1_level_3_node3
        tree1_level_2_node2.right = tree1_level_3_node4

        tree2_level_1_node1 = TreeNode(val=4)
        tree2_level_2_node1 = TreeNode(val=7)
        tree2_level_2_node2 = TreeNode(val=2)
        tree2_level_3_node1 = TreeNode(val=9)
        tree2_level_3_node2 = TreeNode(val=6)
        tree2_level_3_node3 = TreeNode(val=3)
        tree2_level_3_node4 = TreeNode(val=1)

        tree2_level_1_node1.left = tree2_level_2_node1
        tree2_level_1_node1.right = tree2_level_2_node2
        tree2_level_2_node1.left = tree2_level_3_node1
        tree2_level_2_node1.right = tree2_level_3_node2
        tree2_level_2_node2.left = tree2_level_3_node3
        tree2_level_2_node2.right = tree2_level_3_node4

        result = self.tree_to_list(self.solution.invertTree(tree1_level_1_node1))
        expected = self.tree_to_list(tree2_level_1_node1)
        self.assertEqual(expected, [4,7,2,9,6,3,1])
        self.assertEqual(result, expected)

    def test_example_2_leetcode(self):
        tree1_level_1_node1 = TreeNode(val=2)
        tree1_level_2_node1 = TreeNode(val=1)
        tree1_level_2_node2 = TreeNode(val=3)

        tree1_level_1_node1.left = tree1_level_2_node1
        tree1_level_1_node1.right = tree1_level_2_node2

        tree2_level_1_node1 = TreeNode(val=2)
        tree2_level_2_node1 = TreeNode(val=3)
        tree2_level_2_node2 = TreeNode(val=1)

        tree2_level_1_node1.left = tree2_level_2_node1
        tree2_level_1_node1.right = tree2_level_2_node2

        result = self.tree_to_list(self.solution.invertTree(tree1_level_1_node1))
        expected = self.tree_to_list(tree2_level_1_node1)
        self.assertEqual(expected, [2,3,1])
        self.assertEqual(result, expected)

    def test_example_3_leetcode(self):
        result = self.tree_to_list(self.solution.invertTree(None))
        expected = self.tree_to_list(None)
        self.assertEqual(expected, [])
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)
