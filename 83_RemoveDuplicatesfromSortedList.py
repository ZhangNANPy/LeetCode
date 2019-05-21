# -*- coding: utf-8 -*-
# @File  : 83_RemoveDuplicatesfromSortedList.py
# @Author: ZRN
# @Date  : 2019/5/16
"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
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
        p = head
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
