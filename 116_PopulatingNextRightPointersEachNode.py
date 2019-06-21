# -*- coding: utf-8 -*-
# @File  : 116_PopulatingNextRightPointersEachNode.py
# @Author: ZRN
# @Date  : 2019/6/21
"""
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root:
            return
        cur = [root]
        next_level = []
        while cur:
            for i in range(len(cur)):
                if cur[i].left:
                    next_level.append(cur[i].left)
                    next_level.append(cur[i].right)
                if i == len(cur) - 1:
                    continue
                cur[i].next = cur[i + 1]
            cur = next_level
            next_level = []
        return root
