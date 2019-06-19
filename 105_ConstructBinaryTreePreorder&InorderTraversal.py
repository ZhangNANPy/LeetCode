# -*- coding: utf-8 -*-
# @File  : 105_ConstructBinaryTreePreorder&InorderTraversal.py
# @Author: ZRN
# @Date  : 2019/6/19
"""
根据一棵树的前序遍历与中序遍历构造二叉树。

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
    def buildTree(self, preorder, inorder) -> TreeNode:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        cur = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:cur+1], inorder[:cur])
        root.right = self.buildTree(preorder[cur+1:], inorder[cur+1:])
        return root


if __name__ == "__main__":
    s = Solution()
    s.buildTree([3,9,20,15,7], [9,3,15,20,7])