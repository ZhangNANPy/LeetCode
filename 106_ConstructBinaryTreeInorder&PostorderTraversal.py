# -*- coding: utf-8 -*-
# @File  : 106_ConstructBinaryTreeInorder&PostorderTraversal.py
# @Author: ZRN
# @Date  : 2019/6/20
"""
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(postorder[~0])
        cur = inorder.index(postorder[~0])
        root.left = self.buildTree(inorder[:cur], postorder[:cur])
        root.right = self.buildTree(inorder[cur + 1:], postorder[cur:-1])
        return root
