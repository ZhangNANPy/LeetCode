# -*- coding: utf-8 -*-
# @File  : mergeTwoLists.py
# @Author: ZRN
# @Date  : 2018/9/27
"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            l1, l2 = l2, l1
        p = l1
        while p.next and l2:
            if p.val <= l2.val < p.next.val:
                temp = p.next
                p.next = l2
                l2 = l2.next
                p = p.next
                p.next = temp
            else:
                p = p.next
        if l2:
            p.next = l2
        return l1