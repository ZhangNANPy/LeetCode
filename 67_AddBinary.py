# -*- coding: utf-8 -*-
# @File  : 67_AddBinary.py
# @Author: ZRN
# @Date  : 2019/5/6
"""
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a and b:
            return a
        if not b and a:
            return b
        if not a and not b:
            return a
        if len(b) > len(a):
            a, b = b, a
        carry = 0
        res = ''
        for i in range(-1, -len(b) - 1, -1):
            if (a[i], b[i], carry) == ('0', '0', 0):
                res += '0'
                carry = 0
                continue
            if (a[i], b[i], carry) == ('1', '0', 0) or (a[i], b[i], carry) == ('0', '1', 0) \
                    or (a[i], b[i], carry) == ('0', '0', 1):
                res += '1'
                carry = 0
                continue
            if (a[i], b[i], carry) == ('1', '1', 0) or (a[i], b[i], carry) == ('1', '0', 1) \
                    or (a[i], b[i], carry) == ('0', '1', 1):
                res += '0'
                carry = 1
                continue
            if (a[i], b[i], carry) == ('1', '1', 1):
                res += '1'
                carry = 1
                continue

        for i in range(-len(b) - 1, -len(a) - 1, -1):
            if (a[i], carry) == ('0', 0):
                res += '0'
                carry = 0
                continue
            if (a[i], carry) == ('1', 0) or (a[i], carry) == ('0', 1):
                res += '1'
                carry = 0
                continue
            if (a[i], carry) == ('1', 1):
                res += '0'
                carry = 1
                continue
        if carry:
            res += '1'
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('11', '1'))
