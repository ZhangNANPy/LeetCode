# -*- coding: utf-8 -*-
# @File  : 101_SymmetricTree.py
# @Author: ZRN
# @Date  : 2019/6/19
"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSymmetricTrees(root.left, root.right)

    def isSymmetricTrees(self, root1, root2) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val and self.isSymmetricTrees(root1.left, root2.right) \
                and self.isSymmetricTrees(root1.right, root2.left):
            return True
        return False
