# -*- coding: utf-8 -*-
# @File  : NodeList.py
# @Author: ZRN
# @Date  : 2019/5/23
"""
创建链表
"""


def create_node_list(node, l):
    if not l:
        return None
    h = node(l[0])
    p = h
    for e in l:
        p.next = node(e)
        p = p.next
    return h.next


def print_node_list(get, head):
    if not head:
        return []
    p = head
    res = []
    while p:
        res.append(get(p))
        p = p.next
    return res
