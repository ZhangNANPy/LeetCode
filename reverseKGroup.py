# -*- coding: utf-8 -*-
# @File  : reverseKGroup.py
# @Author: ZRN
# @Date  : 2018/9/29
"""
给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        fake_head = ListNode(-1)
        fake_head.next = head
        p = fake_head
        while p.next:
            end = p.next
            nl = []
            while end and len(nl) < k:
                nl.append(end)
                end = end.next
            if len(nl) == k:
                p.next = end
                for node in nl:
                    node.next = p.next
                    p.next = node
                p = nl[0]
            else:
                return fake_head.next
        return fake_head.next


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    s = Solution()
    pr = s.reverseKGroup(a, 1)
    while pr:
        print(pr.val)
        pr = pr.next

