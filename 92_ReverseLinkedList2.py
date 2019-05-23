# -*- coding: utf-8 -*-
# @File  : 92_ReverseLinkedList2.py
# @Author: ZRN
# @Date  : 2019/5/23
"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        t = ListNode(float('inf'))
        t.next = head
        head = t
        re = ListNode(float('inf'))
        bp = head
        i = 0
        for i in range(m - 1):
            bp = bp.next
        i = m
        end = bp.next
        p = bp.next
        while p and i <= n:
            bp.next = p.next
            p.next = re.next
            re.next = p
            p = bp.next
            i += 1
        if end:
            end.next = bp.next
            bp.next = re.next
        return head.next


if __name__ == '__main__':
    s = Solution()
    from Common import create_node_list, print_node_list

    nl = create_node_list(ListNode, [3, 5])
    l = print_node_list(lambda x: x.val, s.reverseBetween(nl, 1, 2))
    print(l)
