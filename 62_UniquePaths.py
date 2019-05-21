# -*- coding: utf-8 -*-
# @File  : 62_UniquePaths.py
# @Author: ZRN
# @Date  : 2019/4/30
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？
"""


class Solution:
    def __init__(self):
        self.rs = {}

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        if (m - 1, n) not in self.rs:
            self.rs[(m - 1, n)] = self.uniquePaths(m - 1, n)
        l = self.rs[(m - 1, n)]
        if (m, n - 1) not in self.rs:
            self.rs[(m, n - 1)] = self.uniquePaths(m, n - 1)
        r = self.rs[(m, n - 1)]
        return l + r
