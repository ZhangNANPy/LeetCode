# -*- coding: utf-8 -*-
# @File  : 94_BinaryTreeInorderTraversal.py
# @Author: ZRN
# @Date  : 2019/5/24
"""
给定一个二叉树，返回它的中序 遍历。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        stack = [[root, False]]
        res = []
        while stack:
            if not stack[-1][1] and stack[-1][0].left:
                stack[-1][1] = True
                stack.append([stack[-1][0].left, False])
                continue
            cur = stack.pop()[0]
            res.append(cur.val)
            if cur.right:
                stack.append([cur.right, False])
        return res
