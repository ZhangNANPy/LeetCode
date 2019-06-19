# -*- coding: utf-8 -*-
# @File  : 102_BinaryTreeLevelOrderTraversal.py
# @Author: ZRN
# @Date  : 2019/6/19
"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        cur = [root]
        next_level = []
        while cur:
            res.append([])
            for node in cur:
                res[-1].append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur = next_level
            next_level = []
        return res
