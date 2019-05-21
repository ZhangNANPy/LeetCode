# -*- coding: utf-8 -*-
# @File  : 86_PartitionList.py
# @Author: ZRN
# @Date  : 2019/5/18
"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        p = head
        headl = ListNode(-float('inf'))
        headg = ListNode(float('inf'))
        pl = headl
        pg = headg
        while p:
            if p.val < x:
                pl.next = p
                pl = pl.next
                p = p.next
                pl.next = None
            else:
                pg.next = p
                pg = pg.next
                p = p.next
                pg.next = None
        pl.next = headg.next
        return headl.next
