# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3305/
"""
Return the root node of a binary search tree that matches the given preorder traversal.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.i=0

        return self.buildSubtree(preorder, 2147483647)
    
    def buildSubtree(self, preorder, maxPossible):
        if len(preorder)==self.i:
            return None
        if preorder[self.i]>maxPossible:
            return None
        node=TreeNode(preorder[self.i])
        self.i+=1
        node.left=self.buildSubtree(preorder, node.val)
        node.right=self.buildSubtree(preorder, maxPossible)
        return node
