# -*- coding: utf-8 -*-
"""
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
"""


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = len(s) - 1
        res = 0
        while i >= 0:
            res += roman[s[i]]
            if roman[s[i]] % 5 == 0 and i > 0 and roman[s[i]] > roman[s[i - 1]]:
                res -= roman[s[i - 1]]
                i -= 1
            i -= 1
        return res
