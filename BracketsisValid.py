# -*- coding: utf-8 -*-
# @File  : BracketsisValid.py
# @Author: ZRN
# @Date  : 2018/9/27
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) % 2 == 1:
            return False
        bd = {'}': '{', ']': '[', ')': '('}
        bl = {'[', '{', '('}
        stack = []
        for b in s:
            if b in bl:
                stack.append(b)
            elif not stack or bd[b] != stack.pop(-1):
                return False
        if stack:
            return False
        return True
