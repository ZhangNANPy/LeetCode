# -*- coding: utf-8 -*-
"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ''。
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        ss = min(strs, key=len)
        lcp = 0
        for i in range(len(ss)):
            char = strs[0][i]
            flag = True
            for s in strs:
                if char != s[i]:
                    flag = False
                    break
            if flag:
                lcp += 1
            else:
                break
        return strs[0][:lcp]

    def longestCommonPrefixNB(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

