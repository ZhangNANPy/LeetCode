# -*- coding: utf-8 -*-
# @File  : 118_PascalTriangle.py
# @Author: ZRN
# @Date  : 2019/6/21
"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。
"""


class Solution:
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            res.append(self.getRow(i))
        return res

    def getRow(self, rowIndex):
        res = []
        f = [1]
        for i in range(1, rowIndex + 1):
            f.append(i * f[i - 1])
        for i in range(rowIndex + 1):
            res.append(f[-1] // (f[i] * f[rowIndex - i]))
        return res
