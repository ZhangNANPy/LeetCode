# -*- coding: utf-8 -*-
# @File  : 64_MinimumPathSum.py
# @Author: ZRN
# @Date  : 2019/4/30
"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。
"""


class Solution:
    def minPathSum(self, grid) -> int:
        grid.insert(0, [float('inf')] * len(grid[0]))
        for row in grid:
            row.insert(0, float('inf'))
        grid[1][0] = 0
        grid[0][1] = 0

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


if __name__ == '__main__':
    a = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    s = Solution()
    print(s.minPathSum(a))
