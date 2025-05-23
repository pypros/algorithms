"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

235. Lowest Common Ancestor of a Binary Search Tree
Medium
Topics
Companies
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:
           6
         /   \
        2     8
       / \   / \
      0   4 7   9
         / \
        3   5

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
           6
         /   \
        2     8
       / \   / \
      0   4 7   9
         / \
        3   5

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
           2
         /   
        1    
Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.

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
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode],) -> Optional[TreeNode]:
        # cur = root
        # while cur:
        #     if p.val > cur.val and q.val > cur.val:
        #         cur = cur.right
        #     elif p.val < cur.val and q.val < cur.val:
        #         cur = cur.left
        #     else:
        #         return cur
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root


import unittest
from collections import deque

class SolutionTestCase(unittest.TestCase):
    solution = Solution()


    def test_example_1_leetcode(self):
        tree1_level_1_node1 = TreeNode(val=6)
    
        tree1_level_2_node1 = TreeNode(val=2)
        tree1_level_2_node2 = TreeNode(val=8)

        tree1_level_3_node1 = TreeNode(val=0)
        tree1_level_3_node2 = TreeNode(val=4)
        tree1_level_3_node3 = TreeNode(val=7)
        tree1_level_3_node4 = TreeNode(val=9)

        tree1_level_4_node1 = None # Not used because None is as default
        tree1_level_4_node2 = None # Not used because None is as default
        tree1_level_4_node3 = TreeNode(val=3)
        tree1_level_4_node4 = TreeNode(val=5)
        tree1_level_4_node5 = None # Not used because None is as default
        tree1_level_4_node6 = None # Not used because None is as default
        tree1_level_4_node7 = None # Not used because None is as default
        tree1_level_4_node8 = None # Not used because None is as default
    
        tree1_level_1_node1.left = tree1_level_2_node1
        tree1_level_1_node1.right = tree1_level_2_node2
    
        tree1_level_2_node1.left = tree1_level_3_node1
        tree1_level_2_node1.right = tree1_level_3_node2
        tree1_level_2_node2.left = tree1_level_3_node3
        tree1_level_2_node2.right = tree1_level_3_node4

        tree1_level_3_node2.left = tree1_level_4_node3
        tree1_level_3_node2.right = tree1_level_4_node4

        result = self.solution.lowestCommonAncestor(tree1_level_1_node1, p = TreeNode(2), q = TreeNode(8))

        self.assertEqual(result.val, 6)

    def test_example_2_leetcode(self):
        tree1_level_1_node1 = TreeNode(val=6)
    
        tree1_level_2_node1 = TreeNode(val=2)
        tree1_level_2_node2 = TreeNode(val=8)

        tree1_level_3_node1 = TreeNode(val=0)
        tree1_level_3_node2 = TreeNode(val=4)
        tree1_level_3_node3 = TreeNode(val=7)
        tree1_level_3_node4 = TreeNode(val=9)

        tree1_level_4_node1 = None # Not used because None is as default
        tree1_level_4_node2 = None # Not used because None is as default
        tree1_level_4_node3 = TreeNode(val=3)
        tree1_level_4_node4 = TreeNode(val=5)
        tree1_level_4_node5 = None # Not used because None is as default
        tree1_level_4_node6 = None # Not used because None is as default
        tree1_level_4_node7 = None # Not used because None is as default
        tree1_level_4_node8 = None # Not used because None is as default
    
        tree1_level_1_node1.left = tree1_level_2_node1
        tree1_level_1_node1.right = tree1_level_2_node2
    
        tree1_level_2_node1.left = tree1_level_3_node1
        tree1_level_2_node1.right = tree1_level_3_node2
        tree1_level_2_node2.left = tree1_level_3_node3
        tree1_level_2_node2.right = tree1_level_3_node4

        tree1_level_3_node2.left = tree1_level_4_node3
        tree1_level_3_node2.right = tree1_level_4_node4

        result = self.solution.lowestCommonAncestor(tree1_level_1_node1, p = TreeNode(2), q = TreeNode(4))

        self.assertEqual(result.val, 2)

    def test_example_3_leetcode(self):
        tree1_level_1_node1 = TreeNode(val=2)
        tree1_level_2_node1 = TreeNode(val=1)
    
        tree1_level_1_node1.left = tree1_level_2_node1
        tree1_level_1_node1.right = None
   
        result = self.solution.lowestCommonAncestor(tree1_level_1_node1, p = TreeNode(2), q = TreeNode(1))

        self.assertEqual(result.val, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
