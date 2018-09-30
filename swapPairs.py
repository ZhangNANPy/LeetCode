# -*- coding: utf-8 -*-
# @File  : swapPairs.py
# @Author: ZRN
# @Date  : 2018/9/28
"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
说明:

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = ListNode(-1)
        p.next = head
        head = p
        while p.next and p.next.next:
            temp = p.next
            p.next = p.next.next
            temp.next = temp.next.next
            p.next.next = temp
            p = p.next.next
        return head.next


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(4)
    a.next.next = ListNode(5)
    s = Solution()
    pr = s.swapPairs(a)
    while pr:
        print(pr.val)
        pr = pr.next
