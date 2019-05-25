# -*- coding: utf-8 -*-
# @File  : 98. Validate Binary Search Tree.py
# @Author: ZRN
# @Date  : 2019/5/25
"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.reValidBST(root)[0]

    def reValidBST(self, root: TreeNode):
        if not root.left and not root.right:
            return True, root.val, root.val
        elif not root.left:
            right_flag, right_min, right_max = self.reValidBST(root.right)
            return root.val < right_min and right_flag, root.val, right_max
        elif not root.right:
            left_flag, left_min, left_max = self.reValidBST(root.left)
            return left_max < root.val and left_flag, left_min, root.val
        else:
            right_flag, right_min, right_max = self.reValidBST(root.right)
            left_flag, left_min, left_max = self.reValidBST(root.left)
            return left_max < root.val < right_min and left_flag and right_flag, left_min, right_max
