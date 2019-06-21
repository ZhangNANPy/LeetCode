# -*- coding: utf-8 -*-
# @File  : 114_FlattenBinaryTree2LinkedList.py
# @Author: ZRN
# @Date  : 2019/6/21
"""
给定一个二叉树，原地将它展开为链表。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)
        if root.left:
            right = root.right
            self.flatten(root.left)
            root.right = root.left
            root.left = None
            p = root
            while p.right:
                p = p.right
            p.right = right
        return
