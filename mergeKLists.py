# -*- coding: utf-8 -*-
# @File  : mergeKLists.py
# @Author: ZRN
# @Date  : 2018/9/28
"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        TLE
        lists are ordered!
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        res = ListNode(0)
        p = res
        while len(lists) > 1:
            i = 0
            min_index = 0
            while i < len(lists):
                if not lists[i]:
                    del lists[i]
                    continue
                if lists[i].val < lists[min_index].val:
                    min_index = i
                i += 1
            if lists and lists[min_index]:
                p.next = lists[min_index]
                p = p.next
                lists[min_index] = lists[min_index].next
        if lists and lists[0]:
            p.next = lists[0]
        return res.next

    def mergeKListsOrder(self, lists):
        i = 0
        while i < len(lists):
            if not lists[i]:
                del lists[i]
                continue
            i += 1
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        res = ListNode(0)
        p = res

        def get_val(node):
            return node.val

        lists.sort(key=get_val)
        while len(lists) > 1:
            p.next = lists[0]
            p = p.next
            while p.next and p.next.val <= lists[1].val:
                p = p.next
            del lists[0]
            if p.next:
                i = 0
                while i < len(lists) and p.next.val > lists[i].val:
                    i += 1
                lists.insert(i, p.next)
        p.next = lists[0]
        return res.next


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(4)
    a.next.next = ListNode(5)
    b = ListNode(1)
    b.next = ListNode(3)
    b.next.next = ListNode(4)
    c = ListNode(2)
    c.next = ListNode(6)
    l = [a, c, b]
    s = Solution()
    pr = s.mergeKListsOrder([None, None])
    while pr:
        print(pr.val)
        pr = pr.next
