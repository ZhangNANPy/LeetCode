# -*- coding: utf-8 -*-
# @File  : 69_Sqrtx.py
# @Author: ZRN
# @Date  : 2019/5/7
"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return x
        xn = 1
        while not ((xn ** 2 <= x) and ((xn + 1) ** 2 > x)):
            xn = int((xn + x / xn) / 2)
        return int(xn)


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(5))
