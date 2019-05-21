# -*- coding: utf-8 -*-
# @File  : 82_RemoveDuplicatesFromSortedListII.py
# @Author: ZRN
# @Date  : 2019/5/16
"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        hd = ListNode(None)
        hd.next = head
        head = hd
        pre = head
        cur = head.next
        delete = float('inf')
        while cur:
            if cur.val == delete:
                pre.next = cur.next
                cur = pre.next
                continue
            if cur.next and cur.val == cur.next.val:
                delete = cur.val
            else:
                pre = cur
                cur = cur.next
        return head.next
