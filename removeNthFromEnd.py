# -*- coding: utf-8 -*-
"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        nth = head
        end = head
        counter = 0
        while end:
            if counter < n + 1:
                end = end.next
                counter += 1
            else:
                end = end.next
                nth = nth.next
        if counter == n:
            head = head.next
        else:
            nth.next = nth.next.next
        return head
