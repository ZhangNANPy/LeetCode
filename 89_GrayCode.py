# -*- coding: utf-8 -*-
# @File  : 89_GrayCode.py
# @Author: ZRN
# @Date  : 2019/5/18
"""
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。
"""


class Solution:
    def grayCode(self, n: int):
        return [i ^ i >> 1 for i in range(2 ** n)]


if __name__ == '__main__':
    s = Solution()
    print(s.grayCode(11))
