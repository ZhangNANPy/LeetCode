# -*- coding: utf-8 -*-
# @File  : divide.py
# @Author: ZRN
# @Date  : 2018/9/29
"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。
"""


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend >= 0 and divisor > 0) or (dividend <= 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
        qmax = 2 ** 31 -1
        qmin = 2 ** 31 * -1
        if abs(divisor) == 1:
            res = abs(dividend) * sign
            if res > qmax:
                return qmax
            elif res < qmin:
                return qmin
            return res
        quotient = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while divisor <= dividend:
            tdvs = divisor
            tq = 1
            while dividend > tdvs << 1:
                tdvs <<= 1
                tq <<= 1
            quotient += tq
            dividend -= tdvs
        res = quotient * sign
        if res > qmax:
            return qmax
        elif res < qmin:
            return qmin
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.divide(23465, 2))

