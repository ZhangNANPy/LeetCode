# -*- coding: utf-8 -*-
# @File  : 63_UniquePaths2.py
# @Author: ZRN
# @Date  : 2019/4/30
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = [[1 - cell for cell in row] for row in obstacleGrid]
        flag = 1
        for i in range(len(m[0])):
            if not m[0][i]:
                flag = 0
            m[0][i] = flag
        flag = 1
        for i in range(len(m)):
            if not m[i][0]:
                flag = 0
            m[i][0] = flag
        for i in range(1, len(m)):
            for j in range(1, len(m[i])):
                if m[i][j]:
                    m[i][j] = m[i - 1][j] + m[i][j - 1]
        return m[-1][-1]


if __name__ == '__main__':
    o = [[0, 0],
         [1, 1],
         [0, 0]]
    s = Solution()
    print(s.uniquePathsWithObstacles(o))
