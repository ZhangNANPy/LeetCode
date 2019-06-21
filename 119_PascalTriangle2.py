# -*- coding: utf-8 -*-
# @File  : 119_PascalTriangle2.py
# @Author: ZRN
# @Date  : 2019/6/21
"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。
"""


class Solution:
    def getRow(self, rowIndex):
        res = []
        f = [1]
        for i in range(1, rowIndex + 1):
            f.append(i * f[i - 1])
        for i in range(rowIndex + 1):
            res.append(f[-1] // (f[i] * f[rowIndex - i]))
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(1))
