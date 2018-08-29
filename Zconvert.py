# -*- coding: utf-8 -*-
"""
将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：
P   A   H   N
A P L S I I G
Y   I   R
之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"

实现一个将字符串进行指定行数变换的函数:
"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows >= len(s) or numRows == 1:
            return s
        i = 0
        re = ''
        while i < len(s):
            re += s[i]
            i += 2 * numRows - 2
        for i in range(1, numRows - 1):
            j = i
            k = 0
            while j < len(s):
                re += s[j]
                if k % 2 == 0:
                    j += 2 * (numRows - i) - 2
                else:
                    j += 2 * i
                k += 1
        i = numRows - 1
        while i < len(s):
            re += s[i]
            i += 2 * numRows - 2

        return re


if __name__ == '__main__':
    s = Solution()
    print(s.convert("AB", 1))
