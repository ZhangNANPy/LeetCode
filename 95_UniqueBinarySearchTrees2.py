# -*- coding: utf-8 -*-
# @File  : 95_UniqueBinarySearchTrees2.py
# @Author: ZRN
# @Date  : 2019/5/24
"""
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int):
        nodes = [i + 1 for i in range(n)]
        return self.RecursiveBST(nodes)

    def RecursiveBST(self, nodes):
        if not nodes:
            return []
        res = []
        for i, v in enumerate(nodes):
            left = self.RecursiveBST(nodes[:i])
            right = self.RecursiveBST(nodes[i + 1:])
            if left and right:
                for l in left:
                    for r in right:
                        node = TreeNode(v)
                        node.left = l
                        node.right = r
                        res.append(node)
            elif not left and right:
                for r in right:
                    node = TreeNode(v)
                    node.right = r
                    res.append(node)
            elif left and not right:
                for l in left:
                    node = TreeNode(v)
                    node.left = l
                    res.append(node)
            else:
                res.append(TreeNode(v))
        return res
