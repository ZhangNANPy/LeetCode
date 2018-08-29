# -*- coding: utf-8 -*-
"""

给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rnum = self.get_num(l1) + self.get_num(l2)
        head = ListNode(0)
        end = head
        flag = False
        while rnum != 0:
            flag = True
            n = ListNode(rnum % 10)
            rnum = rnum // 10
            end.next = n
            end = end.next
        if flag:
            return head.next
        else:
            return head

    def get_num(self, l):
        num = 0
        p = l
        counter = 0
        while p:
            num = num + p.val * 10 ** counter
            counter = counter + 1
            p = p.next
        return num


if __name__ == '__main__':
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    a = ListNode(0)
    b = ListNode(4)
    c = ListNode(0)
    d = ListNode(8)
    r = Solution()
    l = r.addTwoNumbers(a, c)
    while l:
        print(l.val)
        l = l.next
