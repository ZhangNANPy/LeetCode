# -*- coding: utf-8 -*-
# @File  : 110_BalancedBinaryTree.py
# @Author: ZRN
# @Date  : 2019/6/20
"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.deep_balanced(root) >= 0

    def deep_balanced(self, root):
        if not root:
            return 0
        left_deep = self.deep_balanced(root.left)
        right_deep = self.deep_balanced(root.right)
        if left_deep >= 0 and right_deep >= 0 and abs(left_deep - right_deep) <= 1:
            return 1 + max(left_deep, right_deep)
        return -1
