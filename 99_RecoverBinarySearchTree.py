# -*- coding: utf-8 -*-
# @File  : 99_RecoverBinarySearchTree.py
# @Author: ZRN
# @Date  : 2019/5/25
"""
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        l = self.BST2List(root)
        wrong = []
        l.insert(0, TreeNode(-float('inf')))
        l.append(TreeNode(float('inf')))
        for i in range(1, len(l) - 1):
            if not l[i - 1].val < l[i].val < l[i + 1].val and l[i - 1].val < l[i + 1].val:
                wrong.append(l[i])
        wrong[0].val, wrong[1].val = wrong[1].val, wrong[0].val

    def BST2List(self, root: TreeNode):
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
            res.append(cur)
            if cur.right:
                stack.append([cur.right, False])
        return res


if __name__ == '__main__':
    s = Solution()
    r = TreeNode(1)
    r.left = TreeNode(3)
    r.left.right = TreeNode(2)
    s.recoverTree(r)
