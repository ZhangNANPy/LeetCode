# -*- coding: utf-8 -*-
# @File  : strStr.py
# @Author: ZRN
# @Date  : 2018/9/29
"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack or len(needle) > len(haystack):
            return -1
        i = 0
        step = len(haystack) - len(needle) + 1
        while i < step:
            if haystack[i] == needle[0]:
                flag = True
                for j, char in enumerate(needle):
                    if haystack[i + j] != char:
                        flag = False
                        break
                if flag:
                    return i
            i += 1
        return -1
