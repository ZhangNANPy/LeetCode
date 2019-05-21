# -*- coding: utf-8 -*-
# @File  : 61_RotateList.py
# @Author: ZRN
# @Date  : 2019/4/30
"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        list_len = 1
        last = head
        while last.next:
            list_len += 1
            last = last.next
        k = k % list_len
        b = list_len - k - 1
        bp = head
        for i in range(b):
            bp = bp.next
        last.next = head
        head = bp.next
        bp.next = None
        return head
