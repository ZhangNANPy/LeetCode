# -*- coding: utf-8 -*-
# @File  : 103_BinaryTreeZigzagLevelOrderTraversal.py
# @Author: ZRN
# @Date  : 2019/6/19
"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
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
        for i in range(1, len(res), 2):
            res[i].reverse()
        return res
